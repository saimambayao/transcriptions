# NotebookLM Changed Completely: Here's What Matters (in 2026)

**Channel**: Jeff Su
**Duration**: 20:30
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=_uXnyhrqmsU
**Transcribed**: 2026-03-23 02:08

---

## Organized Notes

**NotebookLM's Core Advantage (Unchanged)**

- Best when three conditions are true:
  1. You **already know which documents** contain the answers
  2. Sources are in **different formats** (PDFs, spreadsheets, slides, audio, video)
  3. You need AI to **stick to what's in the documents** — no hallucinations allowed
- Simple **three-column layout**: Sources (left) → Chat (middle) → Studio (right) — work left to right

**Sources Panel — Building Your Knowledge Base**

- Add PDFs, slides, audio, spreadsheets, and more — tells NotebookLM "the answers are in here"
- **Web + Fast Research**: like Google Search without leaving NotebookLM — returns a list of sources to manually review
  - Rule of thumb: select **max 3 sources** as a built-in quality filter
- **Drive + Fast Research**: like Google Drive search bar — find files by describing them naturally
- **Web + Deep Research**: finds sources AND synthesizes them into a full research report
  - **Not recommended** — domain experts filter better than NotebookLM, and Gemini/ChatGPT/Claude do deep research better
- Pro tip: **Google Docs/Slides/Sheets are living documents** — can sync latest changes; PDFs are static uploads
- Pro tip: for blocked websites, use **reading mode → copy text → paste as "copied text" source**
- NotebookLM handles **non-English sources** — can extract info and answer in English

**Chat Panel — Uncovering Insights**

- **Configure chat with custom instructions** — frame every response around your specific goal
  - Use a prompt template in Gemini to generate the custom instruction, then paste into NotebookLM
- **Delete chat history** before starting a new conversation thread to avoid AI being influenced by prior context
- Save useful data points as **notes**, and promote critical insights to **sources** so they factor into all future outputs
- **Source guides** at the top of each source help you find starting points in dense documents — surfaces things you wouldn't have thought to ask

**Studio Panel — Tier 1 Tools (Must-Use)**

- **Reports**: raw sources → finished briefing doc or competitive analysis in minutes
  - Skip default formats; use **suggested formats** (dynamically generated from your sources)
  - Use "create your own" with a Gemini-generated custom instruction for full control
- **Slide Decks**: generates complete presentations from sources
  - Two modes: **presenter slides** (visual, for presenting) and **detailed deck** (self-contained, for reading)
  - Output is **images, not editable elements** — best used for **proposing presentation narratives** and brainstorming structure
  - **Revise button** lets you leave editing instructions on individual slides and regenerate
  - Can export as PDF or PowerPoint (Google Slides export may come)
  - Pro tip: use custom prompt for **vertical 9:16 portrait slides** for LinkedIn/Instagram carousels
- **Infographics**: turns sources into a single polished visual for social media
  - Choose orientation (square for social), visual style, and detail level
  - Avoid "detailed" level — has the most text typos; use **concise** instead
  - Pro tip: **upload brand guidelines as a source** and reference them in custom instructions — works for reports and slide decks too
- **Mind Maps**: visualize everything in your sources at a glance
  - Lets you **cherry-pick topics** worth exploring before reading a single page
  - **Interactive**: click any node to open a focused chat grounded in sources about that subtopic
  - Great for **content planning** — instantly see what's worth covering vs. too technical

**Studio Panel — Tier 2 Tools (Situational)**

- **Data Tables**: pull scattered info into structured, sortable tables; export to Google Sheets
  - More trustworthy than Gemini/ChatGPT tables because answers are **grounded in sources**
- **Video Overviews**: narrated slideshow from sources; good for consuming long-form content visually
  - **Cinematic mode** (Ultra subscribers): uses Google's VO video model for animated sequences
- **Quiz**: multiple-choice questions from sources — useful for **live events** (town halls, workshops) with SlideU or Menty
- **Flashcards**: key terms and concepts from sources — useful for **certification exam prep**
- **Audio Overviews**: mostly a gimmick — chat gives faster results
  - One valid use case: **long newsletters** turned into audio for commuting/cleaning

**Recurring Notebook Ideas**

- **Health reports**: upload annual reports, flag significant changes and trends over time
- **Meeting notes knowledge base**: auto-generated meeting transcripts for targeted pre-meeting questions
- **Tax and accounting**: financial statements + tax code → ask about eligible deductions

**Key Limitation**

- NotebookLM's biggest strength (**high accuracy**) is also its biggest limitation (**low creativity**)
- For brainstorming, creative copy, or coding → use **Gemini, ChatGPT, Claude, or Grok** instead
- Google has integrated NotebookLM within Gemini to bridge this gap

## What This Means for Your Work

**NotebookLM's three-condition sweet spot maps precisely to your legislative research workflow.** You know which documents contain the answers (BOL, BDP, existing BAAs), those sources are in different formats (PDFs, transcriptions, spreadsheets), and you need AI to stick to what is in the documents because legislative accuracy is non-negotiable. For any bill-drafting or policy research task, creating a dedicated NotebookLM notebook with the relevant BOL articles, BDP chapters, and comparable national legislation gives you a grounded research environment where hallucination risk is minimized.

**The reports tool is your fastest path to legislative briefings and policy analysis.** Instead of manually drafting briefing documents for the Office of the Chief Minister, load your sources into NotebookLM and use the "suggested formats" feature (dynamically generated from your sources) to get a tailored starting point. For OOBC policy recommendations, upload the relevant BOL provisions, BDP priority chapters, and any existing BAAs on the topic. The custom instruction approach -- using Gemini to generate a precise prompt, then pasting into NotebookLM -- ensures every output is framed around your specific policy goal.

**The slide deck tool solves your presentation workflow for parliamentary and policy briefings.** Two modes matter for your work: "detailed deck" for self-contained briefings that Parliament members can read independently (committee packets), and "presenter slides" for in-person presentations to the Chief Minister's office. The limitation (output is images, not editable elements) means this is best used for proposing presentation narratives and structures, which you then refine. The vertical 9:16 portrait slide option is immediately useful for sharing policy highlights through social media channels used by Bangsamoro constituents.

**The mind map tool is underrated for legislative analysis.** Before reading through a 50-page draft bill or a complex BAA, generating a mind map lets you cherry-pick which provisions are worth deep examination. The interactive feature -- clicking any node opens a focused chat grounded in sources about that subtopic -- means you can go from a bird's-eye view of an entire piece of legislation to a focused analysis of a specific provision in one click. For your OOBC work, this could reveal policy implications across provisions that are not obvious from linear reading.

**The "high accuracy / low creativity" limitation reinforces your workflow division.** NotebookLM for research and analysis (where accuracy matters), Claude for drafting and creative work (where voice and structure matter). Your existing pipeline -- /bangsamoro for context, NotebookLM for research, Claude for drafting via /bill-drafter or /humanizer -- already respects this boundary. The key insight is to never ask NotebookLM to brainstorm or draft creative policy language; use it exclusively as a grounded research tool that feeds into Claude's drafting capabilities.

### How This Can Improve Your Claude Skills and Workflows

**The reports tool should become the default first step in your /legislative-briefer skill.** Instead of having Claude generate briefing documents from scratch (risking hallucination on legislative details), your /legislative-briefer skill should include a step that creates a NotebookLM notebook with relevant BOL articles, BDP chapters, and existing BAAs, then uses the reports tool with suggested formats to generate a grounded first draft. Claude's role shifts from author to editor and policy voice shaper -- a division that respects the accuracy/creativity boundary.

**The "suggested formats" feature in reports is a concrete improvement for /auto-research eval design.** When NotebookLM analyzes your sources and dynamically suggests the most useful output formats, it is performing a kind of source-aware eval. Your /auto-research and /skill-optimizer skills could adopt this pattern: before running optimization loops, have the system analyze the skill's reference materials and suggest evaluation criteria based on what the sources actually contain, rather than relying on manually written evals that may miss important dimensions.

**The mind map tool should be integrated into your /bill-drafter's pre-drafting phase.** Before writing any bill text, generating a NotebookLM mind map from the relevant BOL articles, comparable national legislation, and existing BAAs would give you and Claude a visual overview of the legislative landscape. The interactive node-to-chat feature means you can drill into any provision's implications before committing to bill structure. This is the legislative equivalent of Matt Pocock's /grill-me -- exhausting the decision tree before writing.

**The slide deck tool fills the gap between /pptx and /presentation skills.** Your /pptx skill generates PowerPoint files, but the two-mode approach (presenter slides for in-person briefings, detailed deck for self-contained reading) is a distinction your current skill doesn't enforce. Adding a mode parameter to /pptx that routes to NotebookLM for grounded content generation -- then to Claude for styling and voice -- would produce parliamentary committee packets and Chief Minister briefings with higher factual reliability.

**Brand guidelines as a NotebookLM source is directly applicable to /brand-guidelines and /stitch-design.** Uploading your MoroTech, e-Bangsamoro, or SEED Initiative brand guidelines as a source and referencing them in custom instructions ensures all NotebookLM outputs (infographics, slide decks, reports) stay on-brand. Your /brand-guidelines skill could include a step that pushes the current brand spec into NotebookLM as a persistent source for the active project's notebook.

---

## Transcript

[00:00] Notebook LM after receiving a massive amount of updates recently is now more popular than even Gemini in terms of usage and interest, which is pretty wild. So, if you're still using Notebook LM like you were a few weeks ago, you're missing out on some incredible capabilities. In this video, I cover what Notebook LM is still the best at, then go through the features and the workflows that actually matter. Let's

[00:21] get started. Even with all the updates, Notebook LM's core advantage has not changed. Here's a simple illustration.

[00:27] Three different health insurance providers send you their coverage options. The first one gives you a PDF brochure. The second gives you a spreadsheet. And the third recorded a

[00:36] video walkthrough. Instead of digging through all that dense material, you'll throw them into Notebook LM and ask something like, "Which provider offers the best dental coverage?" And Notebook LM parses through everything to give you a grounded answer. In other words,

[00:49] Notebook LM is still the perfect tool when three things are true. One, you already know which documents or files contain the answers and you just need help getting through them. Two, those sources are in different formats like PDFs, spreadsheets, and slides or different mediums, text, audio, video, and no single one gives you the full picture. Three, you need the AI to stick

[01:10] to what's actually in the documents and not make things up because the stakes are too high for hallucinations. Jumping into the app, I'm in an empty notebook right now and as you can see, there's a simple three column layout. And the way to use this is to simply go from left to right. One, two, three. Starting off

[01:26] with the sources panel on the left. This is where you add everything Notebook LM needs to work with. PDFs, slides, audio recordings, spreadsheets, you name it.

[01:34] You're basically telling Notebook LM the answers are in here somewhere. Moving on to the chat panel in the middle. This is where you interact with your sources by asking questions, requesting summaries, or pulling out specific details. And all

[01:47] the way to the right, the studio panel. This is where we generate actual deliverables. we can use in the real world. Things like reports and slide

[01:53] decks. We're going to spend most of our time here today. To quickly recap, first we load in everything we're working with on the left. Then we uncover insights in

[02:01] the middle. And on the right, we turn all of that into something we can actually use. Next, let's walk through the sources panel with a real example.

[02:08] At Google, I had to build a proposal on increasing Gemini usage in the Asia-Pacific region. So, I create a notebook and add two sources. I already have an internal strategy document and a PDF with regional data. But I'm still

[02:20] missing some market specific data. So I select the web plus fast research combination within the discover sources field and type top five AI models by usage in the Japan market with monthly active users for each model. Hit enter.

[02:34] And while it's running, the rule of thumb is to treat the web plus fast research combination as Google search without leaving Notebook LM. Notebook LM returns a list of sources for me to review. So let's open this up. And my

[02:46] rule of thumb is to select three sources maximum because it forces me to actually go in and check each source. And so that acts as a built-in quality filter. After reading through the results, I've decided to add these three. And you'll

[03:00] notice one of them is in Japanese, a language I definitely can't speak. But pro tip, you can still add it because Notebook LM can pull out the relevant information and answer your questions in English. Moving on, you want to treat the drive plus fast research combination like the Google Drive search bar. For

[03:18] example, I can type something like find that report with the AI model statistics on the Japan market since I remember the Japan team actually sent me something a while back and I can find the file like this without having to dig through my drive. I can also tell notebook LM to find that start on Android slide deck from the global team because I want to reference their structure when building out my own presentation. And there it is. Now the web plus deep research

[03:46] combination. I'll ask for a report on LLM model usage by country in Asia. And I'll fast forward this part. As you can

[03:52] see, the biggest difference is that deep research finds sources and synthesizes them into a full research report you can add as a source along with a list of sources it pulled from. Put simply, fast research gives you a list of sources to manually review. Deep research takes the extra step of reading those sources and writing a report for you. While that

[04:11] sounds great in theory, I don't recommend using deep research here because number one, if you have any domain expertise on the topic, you can probably filter out lowquality sources better than Notebook LM. And number two, the deep research tools in Gemini, ChachiT, and Claude will just perform better. Pro tip number one, if you add Google Docs, Slides, or Sheets as sources, they're treated as living documents, meaning we can fetch the latest changes from those files. So, for

[04:36] example, if someone adds new slides to the Starta Android deck, I can click to sync the latest version so it's updated by the next time I query this notebook. PDFs, on the other hand, are static uploads. So, keep that in mind. Pro tip

[04:50] number two. For websites that cannot be added as a source directly, as you can see, it's highlighted in red here. We can go to that website, rightclick, open up reading mode, highlight all the text here, then paste it back into notebook LM under the copied text selection. So,

[05:08] to recap, we started with two sources we already had, then use the discover sources function to fill in what we were missing, and now we have everything we need to work with. Moving over to the chat panel in the middle. The most important feature here is the configure chat window. For a highstake tasks, you

[05:24] always want to add a custom instruction. So, every response in this notebook is framed around your specific goal. What I usually do is go over to Gemini and paste in this prompt template. I'll

[05:34] leave a link down below. I need a custom instruction for a notebook. LM notebook blah blah blah. The goal of this

[05:40] notebook is you insert your end goal here. And for this example, I'm just going to paste what I have. develop a business proposal for increasing Gemini's monthly active users. I'm going

[05:48] to let this run. I then copy Gemini's output here and paste it back into my notebook. And now every response from Notebook LM is filtered through that lens. And I usually leave the response

[06:01] length on default since I can always ask Notebook LM to expand later on. Next, after I've had a few back and forths with this notebook, I want to go up here and click delete chat history before I start a completely new conversation so the AI isn't influenced by my previous conversations. But before I delete, I check if there's anything worth keeping.

[06:22] For example, if there's a useful data point I know I'll refer to again, I'll save this as a note. Or if it's a really important insight, I can take this a step further by turning that note into a source so it gets factored into every future studio output. Pro tip, if you click into any source, you'll see a source guide at the top. And I found

[06:44] this to be incredibly useful after adding in a dense source and you're not sure where to start. For example, here I see that Gemini is rapidly growing in India thanks to massive telecom partnerships and Android integration. And that immediately gives me a follow-up question. Why aren't we

[07:02] replicating this telecom partnership strategy in Indonesia, Pakistan, and Japan? And that's something I wouldn't have asked without the source guide surfacing it first. Now, earlier I mentioned that if you want to use deep research, you're better off doing it in Gemini directly. Today's sponsor,

[07:21] HubSpot, actually put together a free guide that maps out exactly how that works. From running deep research in Gemini to importing the results into Notebook LM to generating deliverables from everything combined. My favorite part about this guide is that it breaks the workflow down across 11 specific use cases like marketing strategy, customer research, and actually something I've used myself, the competitive intelligence program. each with its own

[07:44] step-by-step instructions so you're not guessing how to adapt the process to your role. The guide is completely free, so I'll leave a link down below. Thank you, HubSpot, for sponsoring this video.

[07:52] Now, we get to the really fun part. The studio panel has received the most updates, and it's the main reason Notebook LM has evolved from a Q&A chatbot to a production tool. Here's a simple visualization. Before, you would

[08:03] upload your sources, ask Notebook LM something like, "How do we do this year compared to last year?" Copy that answer, and paste it into a separate document. Now, Notebook LM skips that middle step and generates the report directly. Not every tool here is equally

[08:17] useful, though, so I've split them into tier one must tier 2 situational tools. First up, reports lets you go from raw sources to a finished briefing doc or competitive analysis in minutes instead of spending hours outlining and drafting it yourself. Clicking on reports, you'll see default format options up here, which I skipped because they're pretty generic, and instead I focus on the suggested formats down here because these are dynamic. Notebook LM has

[08:41] analyzed all our sources and suggested the most useful directions to take so we don't waste time brainstorming. Clicking into the competitive positioning analysis format, we see that Notebook LM has autogenerated a tailored prompt for us that helps us identify opportunities for winning over enterprise clients and mobile first consumer segments. Okay, I didn't write this prompt, right?

[09:01] Notebook LM inferred it from my sources. Here's another example. I've uploaded my company's bank statements into this notebook. I click reports and none of

[09:11] the suggested formats actually match what I want. So I click create your own and instead of writing a custom instruction from scratch at Hadon back to Gemini and I paste this prompt template which I'll link below and I just need to provide two inputs the purpose of the report and who the report is for. I copy and paste Gemini's output back into the custom instructions field here, which tells Notebook LM I want a breakdown of my finances and areas to save money. Click generate, and within a

[09:40] few minutes, uh, I'm just going to fast forward here. I have a pretty comprehensive report with everything I asked for. Moving on, the slide deck tool builds you a complete presentation directly from your sources. But there's

[09:51] a catch. It's not easy to edit the final output. Here's how it works. In this

[09:55] notebook, I have a bunch of sources related to my Workspace Academy course, from marketing materials to course scripts. And when I click on the slide decks tool, I can choose presenter slides, which generates visual slides meant to be presented, or detailed deck, which produces a self-contained deck meant to be read without a speaker. We'll go with the detailed option for this example. Leave the length on

[10:16] default and guide the notebook with a custom instruction. Create a deck designed to pitch my course to enterprise clients. Use actionoriented head headlines and three talking points maximum for each slide. And we're going

[10:27] to let this generate. Now, the output is pretty damn good. Let's expand this.

[10:32] Okay. Nice. Okay. Wow. It even created a

[10:36] wireframe of Google Drive to illustrate how this course applies the PAR method. That's that's awesome. But if you download this as a PowerPoint, you'll actually realize when you open it up that all these slides are images and not editable elements. Does that make this

[10:53] tool useless? Of course not. An extremely underrated use case is having Notebook LM propose a presentation narrative to cut down the amount of time we spend on brainstorming. For example,

[11:04] my boss tells me to put together a narrative for the Google IO keynote this year. I can upload all the information I know I need to include and use the slide deck tool to generate a detailed deck first just to see what narrative it proposes. Now I have a starting point to work on. Okay, let's expand this out.

[11:23] The visuals look great and it seems like the narrative starts at a high level then dives into specific, projects, case studies and products which makes sense. And let's say we need to make some edits because this looks pretty good from a narrative standpoint. Let's go back to the first slide. I can

[11:41] click the revise button here to start leaving editing instructions on individual slides. Um, so for this slide, I feel like the key vision on the right is way too complicated. Let's remove all the text and simplify the visual. And this slide is fine. Let's

[11:55] just give one more example here. Uh, use Google brand colors because this is not the Google. And we're going to click generate new deck. All right. After a

[12:04] couple minutes, we have an entirely new deck with the changes applied. As you can see, the key visual here is simplified. There's no more text.

[12:10] Awesome. And we're using the Google brand colors here. Pretty cool, right?

[12:15] Uh once everything is finalized, we can click the three dots and we can choose to download as PDF or PowerPoint. But by the time you're watching this, maybe we'll be able to export to Google Slides as well. Pro tip, you can also use slide decks to generate vertical carousel slides for social media. Instead of the

[12:31] default horizontal format, we're going to open up slide deck and under the custom prompts, we're going to add a prompt specifying a vertical slide deck in 9-6 portrait format that's optimized for mobile screens. And I've already prepared the output here. This is still technically a set of slides, but we can download it as a PDF and attach directly to our LinkedIn or Instagram post.

[12:54] Speaking of social media, the infographic tool turns your sources into a single polished visual you can post or send out right away. Back in the Google IO notebook, I want to create an infographic promoting the event obviously. And for orientation, I'm going to choose one by one square dimension. And I am going to select the

[13:11] instructional visual style. For level of detail, just avoid detailed because this has the most text typos. I'm going to go with concise for this. And I'm just

[13:20] going to type top five takeaways for Gemini Enterprise. use Google brand colors and we're going to click generate. And after a minute, I have a pretty on brand visual and it's pretty clean that I can just post on LinkedIn along with a totally non-c cringey and non-corporate BSE post to extend the events reach. Pro tip, if you have a

[13:37] specific brand guideline, upload it as a source and add follow the attach brand guideline for colors, font, and design style, and notebook LM will match the infographic to your branding. Pro tip, this applies to reports and slide decks as well. Just upload your guideline, reference it in your custom instructions, and all three tools stay on brand. Moving on, the mindmap tool

[13:59] shows you everything in your sources at a glance, so you know exactly what's worth digging into before you read a single page. For instance, when I was preparing for my last ChachiBT video, I added a bunch of sources I know I'll need, but there's no point reading through all of it since most of it won't make it into a 10-minute video. But after generating a mind map, I can instantly see every topic and clicking to these arrows, subtopics laid out visually and cherrypick the ones my viewers would actually benefit from. For example, uh this branch 11

[14:29] practical techniques, I immediately know it's worth exploring further versus something like agentic toggles API tips, right? Since this would be too technical for my audience. And because mind maps are interactive, I can click on any of these nodes, for example, 11 practical techniques, and it opens a chat grounded in my sources about that specific topic.

[14:49] So, I go from a bird's eye view of everything to a focused conversation about one subtopic in a single click. By the way, if you want to boost your Google Workspace productivity by 1% every week, including Gemini tips, you can sign up for my weekly newsletter. Every issue is a bite-siz tip you can read and apply in under 60 seconds. link

[15:07] down below. Moving on, tier 2 tools are a bit more situational, so I won't go as deep into each one, but if you have an underrated use case, let me know in the comments. Data tables are useful when you need to pull scattered information from your sources into a structure table you can sort and filter. In this

[15:23] notebook, I've uploaded pricing pages and feature lists of the top AI models. And I can ask Notebook LM after clicking into the data table tool to generate a competitor comparison table with these columns, pricing, key features, etc. Right? And since I've already prepared

[15:37] this ahead of time, I'm just going to expand this. And as you can see, a table is generated. And I can even click the three dots here to export to Google Sheets directly. Or let's say I want to

[15:46] review my marketing campaign performance. I upload historical data from previous campaigns that might be scattered across different formats, right? Then upload my latest campaign data. And Notebook LM generates a clean

[15:57] sideby-side comparison in minutes. Pro tip, other AI tools like Gemini and Chat GPT can generate tables as well, obviously, but since Notebook LM is grounded in our sources, I trust the answers from Notebook LM significantly more. The video overview tool turns your sources into a short narrated slideshow with simple visuals, which is great when you want to watch something instead of read. Case in point, I'm a big fan of

[16:20] Ben Thompson's long- form interviews, but I don't want to read through 20 to 30 pages of text. So, I just upload the transcript onto Notebook LM and click into video overview. Select the detailed explainer format and select the whiteboard visual style. This is just

[16:37] personal preference. And then I just ask for a breakdown of the top five arguments from the interview. After 10 to 15 minutes, these take a while to generate. Notebook condensed that entire

[16:46] interview into its main arguments. Let's play a few seconds from this. >> Evan says that to understand the present, you have to look at the past.

[16:54] And right now, we are in a phase of destruction. before creation. And I found the visuals to really help me understand the concepts as opposed to audio overviews, which I'll touch on in a bit. Now, Google recently upgraded

[17:05] video overviews with a cinematic mode. And here's a difference. The standard video overview is basically audio on top of a slideshow, whereas cinematic video overviews use Google's VO video model to generate actual animated sequences with fluid motion. So, it's closer to a short

[17:22] explainer video than a narrated slide deck. And since it's limited to ultra subscribers for now, I'm not going to go too deep into it right now. The quiz tool generates a set of multiple choice questions grounded in your sources. And

[17:34] I found this surprisingly useful for live events. So I Google for both internal town halls and external workshops. I upload the speaker presentations, generate a quiz with multiple choice questions, then use SlideU or Menty to add an interactive element to the event without having to ask speakers to provide questions themselves. The flashcards tool helps us

[17:54] memorize key terms, concepts, or facts from our sources. So, it's great for certification exam prep. I know I still look 21. Thank you. Thank you. Uh, but

[18:02] it's been a while since I took a test like the GMAT. But if I were preparing for this, I'd upload the prep materials here. Click into the quiz. Um, level

[18:11] difficulty. Click hard cuz I super smart Asian. Uh, let's leave the prompt empty and you can watch me kill these questions. What is the definition of a

[18:19] irrational number? Easy. a number that's not rational. Next,

[18:25] which should be written as infinite non-re repeating decimal. No, that's wrong. All right, moving on to audio overviews. I'll be very honest,

[18:32] this has mainly been a gimmick for me because every use case it's supposedly good for, like deep dive, brief, critique, or debate. I can get to the same result faster by asking a question in chat and reading its answer. And taking this a step further, if I actually wanted like a solid critique on one of my deliverables, like a proposal, I would actually use Gemini because Gemini will reason for longer and actually give me creative recommendations. Notebook LM is not good

[18:59] for this. All that said, I do use it for longer newsletters I can't be bothered to read. I would turn those into audio overviews and actually listen to it on my Notebook LM mobile app while I'm commuting or cleaning. All right, I

[19:12] obviously can't go through every single use case in one video. So, here's a quick lightning round of notebooks I keep coming back to. First up, health reports. I upload my health reports each

[19:20] year and ask Notebook LM to flag anything that's changed significantly from last year and highlight trends I should watch over time. Second, meeting notes knowledge base. I keep meeting transcripts that are automatically generated by Gemini in a notebook so that before any meeting I can just ask targeted questions and I can trust the answers because they are grounded in the meeting notes themselves. Third, tax and

[19:43] accounting. I upload my financial statements along with the tax code and now I can ask things like what deductions am I eligible for based on my income and expenses. Here's something most notebook users forget though.

[19:54] Notebook LM's biggest strength, high accuracy, is also its biggest limitation, low creativity. Since those two dimensions are inherently linked, put another way, if your task requires more creativity, like brainstorming ideas, drafting creative copy, or writing code, you need a tool like Gemini, Chachet, Claude, or Gro. And to Google's credit, they found a way to have their cake and eat it too by integrating Notebook LM within Google Gemini. But this video is already

[20:20] obviously too long. So let me know in the comments if you want a standalone video on that. You can check out my Gemini tutorial here. See you on the

[20:26] next video. And in the meantime, have a great one.
