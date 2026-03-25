# Google just changed the future of UI/UX design...

**Channel**: Fireship
**Duration**: 4:50
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=qaB5HF4ax9M
**Transcribed**: 2026-03-23 03:18

---

## Organized Notes

**Google Stitch — What's New**

- **Infinite canvas** tool for generating UI/UX designs — web pages and app screens
- Input options: text prompts, **screenshot/URL references** for style stealing, or **voice input** via Gemini
- Generates **interactive components**, not static images — each element is individually modifiable
- Outputs are **responsive** — preview on different devices directly in browser
- Can **export to Figma** for manual editing
- New feature: **design markdown file** export — a design system file you can use across multiple projects and integrate with coding models (Claude, OpenAI Codex)

**How It Changes the Workflow**

- No wireframes needed — **start with a vibe** (describe the feel, audience, and aesthetic)
- Can generate a **full design system** from an existing website URL in seconds
- Turns static designs into **interactive prototypes** with simulated user flows in one click
- Design system as a portable file means **consistent AI designs across projects**
- Voice-driven design via Gemini: describe what you want conversationally, get screens back in real time

**Impact on the Design/Dev Ecosystem**

- **Tailwind CSS hit hard** — laid off most of its team; the tool was about making implementation faster, but AI makes that irrelevant
- Tailwind tried monetizing with premium templates, but **"nobody buys premium templates in 2026"**
- Despite being more popular than ever, Tailwind is now **surviving on donations**
- The shift: instead of memorizing utility classes, you describe what you want and AI builds it
- UI/UX designers are being disrupted — **"you don't need to start with a wireframe anymore"**

**Limitations**

- Still can't implement **reliable full-stack features** like authentication
- Best for design generation and prototyping, not production backend logic

## What This Means for Your Work

**The design markdown file export is the single most valuable Stitch feature for your multi-platform operation.** You are building 9 government-scale platforms on React 19 + Tailwind CSS. A portable design.md that codifies color strategy, typography rules, and component conventions means you can enforce visual consistency across e-Bangsamoro, e-Negosyo, MoroMarket, Tarbiyyah-MS, BangsamoroHR, SBP, OBCMS, Parliamentarian, and IPP without manually synchronizing design tokens between projects. Export the design.md from Stitch, drop it into each Claude Code project, and your /frontend-design skill reads from a single authoritative source.

**The Tailwind CSS disruption narrative has a different implication for you as a solo dev.** Fireship frames Tailwind's layoffs as proof that implementation tools are becoming irrelevant. But you are not selling Tailwind templates -- you are using Tailwind as your CSS layer across all 9 platforms. The real takeaway is that your workflow of describing interfaces to Claude Code and having it generate Tailwind classes is now the dominant pattern, not the exception. Your existing stack is already positioned correctly.

**Voice-driven design via Gemini could accelerate your stakeholder collaboration workflow.** When presenting design options to BARMM officials or the Office of the Chief Minister, you could run Stitch's voice mode during meetings to iterate on interface concepts in real time -- describe what the Bangsamoro Scholars portal should look like, get screens back instantly, and gather feedback on the spot. This is faster than scheduling a separate design review cycle.

**The limitation Fireship flags -- no reliable full-stack features -- confirms your two-tool split.** Stitch handles the visual layer, Claude Code handles Django backend logic, PostgreSQL schemas, authentication, and API integration. For the SEED Initiative's 124+ training courses in Tarbiyyah-MS or the cooperative marketplace logic in e-Negosyo, you still need Claude Code doing the heavy engineering. Stitch is a visual accelerator, not a replacement for your development pipeline.

### How This Can Improve Your Claude Skills and Workflows

**The portable design.md concept Fireship highlights should become the connective tissue between your /stitch-design, /frontend-design, and /brand-guidelines skills.** Fireship calls this "the best new feature" -- a single markdown file that codifies an entire design system and can be used across multiple projects and integrated with coding models. Create a skill chain where /brand-guidelines generates the master design system for MoroTech, /stitch-design exports project-specific design.md files that inherit from the master, and /frontend-design reads the project-specific design.md at the start of every implementation session. This three-layer system (brand > project > page) ensures visual consistency from MoroMarket's marketplace to Tarbiyyah-MS's learning management interface without manual synchronization.

**The Tailwind CSS disruption narrative has a workflow implication for your /frontend skill.** Fireship notes that memorizing utility classes is becoming irrelevant because you describe what you want and AI builds it. Your /frontend skill should lean further into semantic descriptions ("professional data table with sortable columns and zebra striping") rather than Tailwind-specific instructions ("use bg-gray-50 on even rows"). This makes your skills model-agnostic -- if you ever move from Claude Code to another coding agent, or if Tailwind is replaced by something else, your skill prompts remain valid because they describe intent, not implementation.

**Voice-driven design creates a new workflow for your governance stakeholder meetings that your /presentation skill should support.** Fireship shows Stitch's voice mode generating screens from conversational descriptions. Combine this with your /presentation skill: before a design review meeting with the Office of the Chief Minister, prepare a /presentation deck with the current state, then use Stitch voice mode during the meeting for live iteration based on feedback. Your /presentation skill could include a "live design session" template that structures the meeting flow -- current state, feedback round, live Stitch generation, selection, next steps.

**The "no wireframe needed, start with a vibe" philosophy should update your /write-a-prd skill's design section.** Traditional PRDs include wireframes or mockup references. Fireship suggests that the new workflow starts with a "vibe" -- what the product should feel like, who it is for, what aesthetic to channel. Update /write-a-prd to include a "Design Vibe" field (replacing or supplementing wireframes) that captures the visual thesis, target aesthetic, and reference URLs. This vibe statement becomes the input for /stitch-design, creating a clean handoff from product specification to visual design to code implementation.

**Cross-pollination with /notebooklm: feed the design.md files from all 9 platforms into a NotebookLM source to create a unified design knowledge base.** When you have design.md files for e-Bangsamoro, MoroMarket, Tarbiyyah-MS, BangsamoroHR, SBP, OBCMS, Parliamentarian, IPP, and e-Negosyo, NotebookLM can analyze them collectively -- identifying shared patterns, inconsistencies, and opportunities for component reuse across platforms. This turns individual design systems into an organizational design language for BARMM's entire digital ecosystem.

---

## Transcript

[00:00] But for years, I've refused to better myself as a web developer by getting really good at design and tools like Figma. Well, yesterday that decision finally started to pay off because Google just murdered Figma by announcing a massive update to their vibe design tool, Stitch. If you've never heard of it, it's an infinite canvas tool that allows you to easily generate designs for your UIUX needs like web pages and app screens. Designer Gary Simon is

[00:24] literally shaking right now. If you are UIUX designer, you are living in the dark ages because you don't need to start with a wireframe anymore. You just start with a vibe. You tell it what your

[00:34] product should feel like, who it's for, maybe throw in a screenshot or a URL of a design you want to steal, or maybe just whisper into your mic like a lunatic. Then it simply summons the devil straight from the hexagon of Saturn to build a UI for you like magic. But here's the crazy part. It doesn't

[00:49] stop at static designs. The Stitch can instantly turn those into interactive prototypes and simulate full user flows with a single click. The tool just got an upgraded new slop renderer, but the best new feature is actually a humble little design markdown file that could completely change your app development workflow. In today's video, we'll take a

[01:08] look at everything new in Google Stitch and find out if it's just more hype or a true game changer for untalented designers. It is March 19th, 2026, and you're watching the Code Report. I've been failing to build good UIs for nearly two decades now. I still remember

[01:22] my very first website which took weeks of painstaking CSS work in Adobe Dreamweaver. Luckily though, many years later, design implementation got way easier thanks to tools like Tailwind CSS. But sadly, now AI tools like Stitch are killing the CSS tooling business. A

[01:38] couple months ago, Tailwind had to lay off most of its team. And honestly, it makes sense because Tailwind was never really about design. It was about making implementation faster. as a free and

[01:47] open- source tool. They tried to monetize the business by selling premium templates, but in 2026, nobody buys premium templates anymore. Why memorize utility classes like Flex, BG Blue-500, GAP 4, and so on when instead you can just say, "Build me a clean SAS dashboard with good spacing and modern typography." And because of that

[02:07] reality, despite being more popular than ever, Tailwind is now surviving on donations like a homeless person. Check this out. I really like the design system used on the fireship.dev website,

[02:17] which was created by a real human named Lynn with real talent. But because I'm lazy, I can now just feed Google Stitch a website URL, and it will instantly build me a design system that I can now use in any project. This stealing is awesome because now I can put this design system to work on my billion-dollar app idea, Horse Tinder. I

[02:34] tell Stitch to build a homepage and it's done in 30 seconds. And this isn't just some static image from Nano Banana. Every element is an actual interactive component that can be modified individually. I can make modifications

[02:46] here directly with AI or even export them into Figma to edit them like a caveman. In addition, everything is responsive. So, I can spin up a prototype right here in the browser and preview it on different devices. But

[02:58] actually, we don't even need to type a prompt to work on a design. I can just talk directly to Gemini. >> Hey, what are we designing?

[03:04] >> Horse Tinder. >> Are you looking to work on the landing page, the swipe stack, or something else? Uh, let's work on a chat feature.

[03:11] >> Ooh, a chat feature. That's essential for connecting those matches. What kind of vibe are we going for?

[03:17] >> Uh, let's make it kind of like Grinder. >> Bold and modern it is. I'll design a clean and energetic chat screen for you.

[03:24] Inspired by that aesthetic on it. The new chat screen is ready. I've gone for that bold, energetic vibe with clean lines and vibrant colors. Take a look.

[03:33] What do you think? Anything else you'd like to adjust? >> Nope. That looks gay enough. Thank you.

[03:37] As you can see, Stitch is basically like having your own designer employee, but it has one more trick up its sleeve. If you remember the original design system we generated, well, we can actually export that as a design file. And now I can take that file into a text editor and easily use it in multiple projects or integrate it with other coding models like Claude or OpenAI codecs. And that's

[03:58] huge because it means consistent AI designs across multiple projects. But there's still one thing Stitch can't do, and that's implement reliable, bulletproof, full stack features like user authentication. And that's why you need Clerk in your life, the sponsor of today's video. Ronnie Coleman once said,

[04:13] "Everybody wants to build a B2B SAS app, but nobody wants to build those annoying ass enterprise features. That's why Clerk created a single platform that lets you easily add O, user management, and billing to your app. Their drop-in components enable your users to onboard their entire org with custom roles and permissions. And clerk billing lets you

[04:33] implement subscription pricing tiers without having to write the payment logic yourself. The clerk is the missing piece that'll help you actually release all the stuff you've been viating and building with agents. And you can try it out for free at the link below. This has

[04:45] been the code report. Thanks for watching and I will see you in the next one.
