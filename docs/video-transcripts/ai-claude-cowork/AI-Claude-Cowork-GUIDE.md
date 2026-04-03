# Claude Cowork

Most AI tools demand your attention. Claude Cowork is built around the opposite premise: assign the task, walk away, review the result.

This guide synthesizes practical knowledge on Claude Cowork, Computer Use, and Dispatch — Anthropic's three-layer system for autonomous background work. It covers how each layer differs, which tasks each handles reliably, and how to combine them for async workflows that run while you sleep.

---

## Three Layers, Three Use Cases

Claude's desktop ecosystem has three distinct execution modes, and conflating them leads to mismatched expectations. Understanding the boundaries is the first step to using them effectively.

**Claude Cowork** operates in a designated folder. The user grants Claude access to a specific directory, assigns a task, and Claude works in the background — the user can continue using the computer while Claude processes files, writes code, or generates documents within that scope. This is the most stable and production-ready mode.

**Claude Computer Use** gives Claude access to the full Mac: screen, keyboard, mouse, and all installed applications. Claude can open any app, navigate any window, and take any action a human user could. The tradeoff is exclusivity — the user cannot use the computer while Claude controls it. This is the newest and most experimental mode.

**Dispatch** is the remote layer. Through the Claude mobile app, users can send tasks to Claude running on their desktop from anywhere — phone, tablet, or another machine. The desktop runs the task autonomously; the user reviews results on return. Dispatch works with both Cowork and Computer Use.

> **Key insight**: The real shift is not from chatbot to agent — it's from synchronous collaboration to asynchronous delegation. [^1]

**The takeaway**: Match the mode to the task. Cowork for folder-scoped file work. Computer Use for cross-application operations. Dispatch for anything you want to delegate before stepping away.

---

## Computer Use: What Works and What Doesn't

Early-stage tools are most useful when their actual capabilities are understood clearly, not oversold. Computer Use as of early 2026 has a well-defined capability ceiling.

Tasks that complete reliably involve **named files and single-application operations**: finding a specific document by name, opening a specific application, copying and pasting content, saving output to a designated path. The document-to-PDF demo — find a 1,700-word Word document in Dropbox, summarize it, rewrite as a blog post, export as PDF — completed correctly in real time. [^1]

Tasks that fail or stall involve **imprecision, speed requirements, or complex GUI interactions**. If a file name is vague, Claude searches the entire computer and may never converge. Web form filling is possible in principle but too slow for practical use. Video editing — making cuts, moving clips — failed even at the basic level. The first demo (importing a video file into Adobe Premiere) took approximately 10 minutes for a task any human editor does in under 60 seconds. [^1]

> **Key insight**: Specificity is not a preference — it's a prerequisite. Vague instructions produce wandering searches; exact file names produce fast, reliable results. [^1]

The practical ceiling for current Computer Use is: **async, non-time-sensitive, well-defined operations on known files**. This is a meaningful capability, but it is not yet a general-purpose computer operator.

- **Works**: named-file find, single-app open, document-to-output conversion, browse-and-generate [^1]
- **Struggles**: vague file searches, multi-step GUI editing, web form entry, anything time-sensitive [^1]
- **Not yet**: video editing, calendar and email management (most users exclude these intentionally), complex multi-application workflows [^1]

**The takeaway**: Use Computer Use for tasks where you can describe the exact file, the exact app, and the exact output — nothing more, nothing less.

---

## Dispatch as Async Work Multiplier

The most underrated feature in the Claude desktop ecosystem is not Computer Use — it is Dispatch. While Computer Use gets the attention for its visual drama, Dispatch changes the fundamental relationship between a knowledge worker and their machine.

The core pattern: **assign a task before stepping away, review results on return**. This applies whether "stepping away" means a one-hour meeting, a cross-city flight, or sleeping. The computer runs the task unattended; the user's only obligation is to write a clear prompt and check the result. [^1]

Setup requires pairing the Claude mobile app with the desktop app, enabling the Dispatch toggle in Cowork settings, and enabling "Keep Computer Awake" so the machine stays accessible. Once configured, the phone becomes a task dispatcher and the desktop becomes an autonomous worker. Tasks can also be scheduled to run at specific times, not just triggered on demand. [^1]

The Dispatch demo demonstrated a realistic workflow: find the latest screen recording in Downloads, rename it, move it to Dropbox, and surface the link. Claude completed all four steps correctly — the only gap was that the Dropbox link appeared in a desktop text editor rather than being returned directly to the phone. This is a rough edge, not a fundamental failure, and will likely close quickly as the product matures. [^1]

> **Key insight**: "If you're sleeping or away from your computer, you could just send a message, go to sleep, and this will do things that might take a couple of hours. It will just do it in the background for you." [^1]

**The takeaway**: Dispatch is production-ready for file operations, document conversion, and cloud storage tasks — exactly the category of work that interrupts focused time when done manually.

---

## Enabling Computer Use: Required Configuration

Computer Use is disabled by default and requires explicit permission grants at three levels: application settings, system permissions, and per-session app access.

In the Claude desktop app (Settings → General), three settings must be enabled: **Keep Computer Awake** (prevents the machine from sleeping during remote tasks), **Allow Browser Use** (lets Claude interact with Chrome without per-action prompts), and **Computer Use** (grants screen recording and keyboard/mouse control). The **Denied Apps** list lets users explicitly exclude sensitive applications — most users starting out exclude email clients and calendars as a precaution. [^1]

At the macOS system level, Screen Recording and Accessibility permissions must be granted to the Claude desktop app. These do not activate automatically. On first use, Claude will prompt for per-app permissions as it encounters each application — granting these upfront reduces mid-task friction. [^1]

One practical finding from testing: desktop overlays and pointer-highlighting apps interfere with Computer Use's screen analysis. Any app that draws over the screen should be quit before running Computer Use tasks. [^1]

**The takeaway**: Run the full configuration checklist before the first real task — permission friction mid-task is disruptive and causes unnecessary delays.

---

## The Trajectory: Why Early Adoption Has Value

Claude ships updates to the desktop app on a near-daily cadence. Computer Use as demonstrated in early April 2026 is a foundation, not a finished product. The patterns that work today — named-file retrieval, document transformation, browse-and-generate — will expand as speed and precision improve.

The early-adopter value is not in immediately replacing human workflows. It is in **developing the mental model** of what autonomous computer delegation looks like: how to write precise task descriptions, which file operations are safe to delegate, which applications to keep excluded, and what result formats to expect. This experiential knowledge compounds. Users who develop it now will extract disproportionate value as the reliability curve steepens. [^1]

> **Key insight**: "Claude ships new updates pretty much every single day. It's not going to be long till Claude Computer Use inside Claude Cowork inside Claude Code becomes the next big leap for AI." [^1]

**The takeaway**: The right posture for 2026 is systematic low-risk experimentation, not production deployment — build the muscle memory for a tool that will be significantly more capable in six months.

---

## For Your Work

Claude Cowork and Dispatch address a real constraint in the current setup: as a solo developer managing 9+ active repos alongside government consulting work, attention is the scarcest resource. Cowork's background execution model is already familiar — the question is where Computer Use and Dispatch add incremental value beyond the existing folder-scoped workflows.

### Applications

- **e-Bangsamoro / all active repos** — Use Dispatch for async file operations that currently interrupt focused dev time: export DB migrations, move build artifacts, rename and archive files across project folders. Write the task prompt, send from phone before a meeting, review on return. [^1]
- **Guidebook production pipeline** — The document-to-PDF demo maps directly to the WeasyPrint generation step. Computer Use could eventually open a Word draft, read it, reformat it, and export the final PDF — replacing the current Python script dependency for one-off conversions. [^1]
- **Parliamentarian app** — The browse-and-act loop (Demo 3: analyze website → generate 2,000 lines of code) suggests that Computer Use + Claude Code can close the research-to-implementation gap. For the Parliamentarian, this means navigating to lawphil.net, extracting a case, and returning the text — without pre-scraped files. [^1]
- **BTA Bills Scraper fallback** — If the parliament.bangsamoro.gov.ph WP REST API closes or changes, Computer Use could serve as a browser-based fallback scraper: navigate the parliament website, extract bill text, save to `legislation/bills/scraped/`. Not needed now, but worth tracking. [^1]
- **`/youtube-transcriber` skill** — The find-read-rewrite-PDF pattern could eventually be Cowork-native rather than requiring a Claude Code session. A Dispatch-triggered transcription task ("transcribe this URL and save to vault") aligns with the async delegation model. [^1]

### Priority Actions

1. **This week**: Enable Dispatch on the Claude mobile app. Pair with the desktop. Test one low-risk task: find the latest file in `legislation/bills/scraped/bta-2/`, copy it to `~/Vault/`, and confirm the copy. This is a safe, named-file operation that tests the full Dispatch loop without risk.
2. **This week**: Add email and calendar to the Denied Apps list before enabling Computer Use broadly. Then test Computer Use on one document task: find the most recent guidebook chapter draft in `~/Library/Application Support/Claude/`, summarize it, and save a one-paragraph summary to `docs/`.
3. **This month**: Design a standard Dispatch task format for common async operations: file moves, PDF exports, folder audits. Write 3-5 template prompts that can be reused across projects with minimal modification.
4. **This quarter**: Monitor Computer Use reliability improvements. When form-filling becomes reliable, evaluate whether it could automate BangsamoroHR data entry tasks — a current repetitive manual workflow.

---

## References

[^1]: Skill Leap AI. "Claude Can Control Your Computer - Everything You Need To Know." *Skill Leap AI*, 17:52. YouTube, April 2026.
      https://youtube.com/watch?v=Dl36TDBFUdo
