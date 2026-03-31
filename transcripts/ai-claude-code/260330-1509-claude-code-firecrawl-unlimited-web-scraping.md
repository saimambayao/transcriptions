# Claude Code + Firecrawl = UNLIMITED Web Scraping

**Channel**: Chase AI
**Duration**: 10:53
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=phuyYL0L7AA
**Transcribed**: 2026-03-30 15:09

---

## Organized Notes

**The Problem: Claude Code's Web Scraping Limitations**

- Claude Code's built-in **web fetch** struggles with three categories of websites:
  1. **Anti-bot protections** -- sites like Yellow Pages return 403 errors repeatedly
  2. **JavaScript-heavy sites** -- dynamic content (SimilarWeb metrics) isn't in the HTML shell that web fetch grabs
  3. **Token inefficiency** -- Amazon product pages dump 13,000+ lines of HTML into context when you only need 5 fields
- Even when web fetch succeeds, it's **slow** -- 5.5 minutes for 4 Amazon pages vs. 45 seconds with Firecrawl

**Firecrawl: What It Is and How It Works**

- **Firecrawl** is a web scraping tool with a CLI and Claude Code skills integration
- It grabs web data and returns it in **markdown format** optimized for LLM consumption -- structured, schema-filtered, token-efficient
- You can set a **schema on the front end** -- tell Firecrawl "I just want product name, price, rating, review count, seller" and it returns only that, not the entire page
- **Open-source** with a hosted product (free tier: 500 credits one-time; paid: hobby/standard/growth tiers)

**The 8 Firecrawl Actions**

- **Scrape** -- give it a URL, get all content from that page (most basic)
- **Crawl** -- give it a starting URL, it systematically goes through the entire website
- **Search** -- don't have a URL? Firecrawl finds it on the internet, then scrapes it
- **Extract** -- JSON-specific output from a web page with structured schema
- **Map** -- discover all URLs on a site
- **Agent** -- most powerful, autonomous decision-making (search, extract, map on its own). Uses the most credits
- **Browser Interact** -- brand new, spins up live Chromium sessions with click/type/scroll (like Playwright)
- **Batch Scrape** -- scrape multiple URLs in one call

**Head-to-Head Tests: Firecrawl vs Web Fetch**

- **Test 1: SimilarWeb** (JavaScript rendering)
  - Web fetch: got only the HTML shell, hung for 5 minutes, returned nothing useful
  - Firecrawl: **42 seconds**, full metrics, traffic by country, by source, social media breakdown

- **Test 2: Yellow Pages** (anti-bot protection) -- plumbers in Nashville
  - Web fetch: "aggressively blocking all direct page fetches," hit with 403s over and over
  - Firecrawl: **53 seconds**, 16 results with business name, phone, years, services

- **Test 3: Amazon** (heavy HTML) -- 4 product pages
  - Web fetch: succeeded but took **5.5 minutes**
  - Firecrawl: same data in **45 seconds** -- 7x faster

**Setup in Claude Code**

- Install Firecrawl CLI + skills (link in video description)
- Easiest method: copy the setup page, paste into Claude Code, say "install Firecrawl skill and CLI"
- Authenticate with a Firecrawl account (one-click)
- Then use **natural language** -- Claude Code's skills know how to match actions to use cases

**Open-Source vs Hosted**

- Self-hosted Firecrawl is free but **loses**: anti-bot protections (proprietary "fire engine"), Agent action, Browser Interact action
- Requires Docker knowledge for setup
- Hosted version has all features but costs money at scale

*Quotable Quotes:*

> "The second we start talking about scraping at scale, where we do need to think about time and we do need to think about token cost, Firecrawl just makes a ton of sense." [09:15]

---

## What This Means for Your Work

Firecrawl directly addresses a gap in several of your workflows. Your `/legal-researcher` skill searches for legislation online, your `/deep-research` skill fetches web sources, and your `/fact-checker` verifies claims against official websites. All of these use Claude Code's built-in web fetch, which struggles with JavaScript-heavy government portals and anti-bot protections.

**BARMM government websites** (parliament.bangsamoro.gov.ph, bangsamoro.gov.ph) use dynamic rendering -- exactly the kind of site where web fetch fails and Firecrawl succeeds. The same applies to Philippine government sites like lawphil.net (where you scraped 11,866 RAs, 2,572 EOs, and 38,857 SC decisions) and officialgazette.gov.ph.

**Key applications:**

- **Legal research at scale** -- when `/legal-researcher` needs to scan multiple government websites for BAA implementations, policy documents, or IRRs, Firecrawl's crawl action could systematically grab entire sites instead of one-page-at-a-time web fetch
- **Competitive analysis for MoroTech/MoroMarket** -- the Content Marketing Employee could use Firecrawl to scrape competitor platforms, cooperative marketplaces, and social enterprise directories for market intelligence
- **Lead generation for MoroAcademy** -- scrape directories of Bangsamoro cooperatives, MSMEs, and government training programs to identify potential training clients
- **Schema-filtered extraction** is the biggest win -- instead of dumping full HTML into context (burning tokens), define exactly what fields you need and get clean structured data back

**Cost consideration:** The free tier (500 credits) is enough to evaluate. For sustained use across your 9 projects, the standard plan would be more practical than self-hosting given your solo dev bandwidth.

### How This Can Improve Your Claude Skills and Workflows

**Skills that would benefit from Firecrawl integration:**

- `/legal-researcher` -- replace web fetch calls with Firecrawl scrape for government portals. The SEARCH action is especially useful: "find the IRR for BAA No. 84" without knowing the exact URL
- `/deep-research` -- Firecrawl's crawl action could replace the manual URL-by-URL web fetch in Phase 2 (source gathering), dramatically reducing research time
- `/fact-checker` -- Tier 2 and Tier 3 verification (BARMM official websites, web search) would be faster and more reliable with Firecrawl handling anti-bot protections
- `/content-research-writer` -- market research and competitor analysis for content creation
- `/webapp-testing` -- Firecrawl's Browser Interact is essentially Playwright-like browser automation; could complement or replace some Playwright workflows

**New skill opportunity: `/web-scraper`**. Checking your index, you don't have a dedicated web scraping skill. A `/web-scraper` skill wrapping Firecrawl's 8 actions with your common use cases (legal research, market research, lead generation, content research) would be a reusable building block across multiple AI employees.

**Project applications:**
- **MoroMarket** -- automated product/price scraping from competing marketplaces
- **e-Bangsamoro** -- scrape BARMM government portals for data feeds (budget releases, legislative updates, appointment announcements)
- **Parliamentarian** -- scrape lawphil.net more efficiently for jurisprudence updates (your current scraper uses custom Python; Firecrawl could simplify this)

---

## Transcript

[00:00] Claude Code sucks at web scraping. It can't handle anti-bot protections. It struggles with JavaScript heavy sites and half the time it will come back with nothing at all. But if we bring in a

[00:11] tool like Firecrawl, we can solve all of these problems very easily. And today I'm going to show you how Firecrawl works, how to set it up inside of Claude Code, and we're going to demo a real use case so you can see this thing in action. So why should you even care about improving Claude Code's ability to web scrape? Well, the answer is pretty

[00:28] simple. It's because there are a ton of extremely high leverage use cases that require us to be able to web scrape effectively at scale. Think of anything to do with competitive analysis or market research or enriching lead generation prospects. Right? If I go to

[00:43] Claude Code and I say something like, "All right, take a look at these five Amazon web pages. Show me their pricing and the ratings, what customers are talking about." Claude Code's going to struggle. Same thing as if I tell it to

[00:54] go look at a company website and scrape the whole thing and come back with like 50 prospects. Again, web fetch from Claude Code is not enough. We need to be able to solve this problem. Enter Firecrawl

[01:05] and its relatively new CLI tool and skills. So, the way Firecrawl works is relatively simple. Like I said, it gives Claude Code the ability to now scrape websites that either have really heavy JavaScript or something that has anti-bot protection because the normal web fetch is really just looking at their HTML. Now when Firecrawl takes a

[01:22] look at those websites, what it's doing is it grabs all the data, but it brings it back to Claude Code in a format that large language models can use. It essentially just puts it into a markdown file, but it's also in a schema that makes it very simple for Claude Code to ingest. It also doesn't use a bunch of tokens. So it is more efficient and

[01:42] more effective than your standard web fetch. So if for example I pointed Firecrawl at this web page on Amazon, it's not just going to bring all the data back in Claude Code. I mean think of all the stuff going on here, right?

[01:52] There's like a billion in one photos, videos, there's multiple items that have prices with it, but I can set the schema on the front end. So I tell Firecrawl, hey, I just want the product name, the price, the rating, the review count, the seller, and it brings the data back to Claude Code like this, right? Much easier for it to handle this than try to essentially parse all of this HTML, right? This is crazy,

[02:19] right? I don't want to dump 13,000 lines into Claude Code. Now, after seeing that, your mind probably goes straight to pricing, right? Okay, like what's the

[02:25] hidden cost here? Well, there is a free plan. You get 500 credits. It's a

[02:29] one-time thing. And then you have hobby, standard, and growth, right? Standard sort of pricing for these sort of things. And your results will vary

[02:35] depending on the scale you're operating at. That being said, Firecrawl is an open-source product, which we'll talk about at the end of this video and kind of what you gain and lose if you decide to go the open source route versus their product. Now, because Firecrawl gives us a set of skills as well as the CLI tool, when it comes to actually using it inside of Claude Code, we're going to just use natural language, but it helps for us to understand like what our options are because there's like five or six different abilities Firecrawl has. And I actually lied. There

[03:03] are eight actions available to us with Firecrawl. Remember Claude Code has all the skills. So it knows how to match the action to your particular use case. But

[03:10] the ones you want to kind of like have a working knowledge of are scrape, crawl, search, extract, and agent in my opinion. Right? So what is scrape? It's

[03:21] the most basic one. It's where we are going to give Firecrawl a URL and it's just going to grab all the content from that page. Again, think of the headphones example I just showed you. We

[03:29] also have crawl. So crawl means I can give it a webpage URL and then it will systematically go through the entire website, right? It just needs a starting URL and it'll do the rest. We also have

[03:39] search. So the difference between search and crawl and scrape is with crawl and scrape, you show up with a URL, so you already know what you want. With search, I'm kind of saying like, hey, I don't really know exactly where this thing exists on the internet. Go ahead and

[03:52] find it. And then once you find it, go ahead and scrape. Then we have extract, which kind of is a JSON specific output you're going to be grabbing from the web page. And then lastly, we have agent,

[04:02] which is their most powerful one. So again, it's almost like you're just talking to Claude Code, right? It's acting in an agent format. Like it will

[04:09] decide on its own, okay, do I need to search? Do I need to extract? Do I need to map it? Right? So agent is the most

[04:14] powerful, but it uses the most credits. So essentially, you can kind of see the difference between all these actions kind of depends on what your starting point is. Like do you have a starting URL or do you need to go and find it?

[04:24] And then it also depends on like how many actions do you want it to take on its own because if I'm using something like agent, it's going to do everything. It just costs a little bit more. And lastly, this one, Browser Interact. This

[04:34] just came out a few days ago and essentially it's like their version of Playwright, right? It will actually spin up live Chromium sessions. It'll click, type, scroll. It'll do everything as

[04:42] if you were at the keyboard doing it yourself. All right, so how do we actually get started with this and start running inside of Claude Code? Very simple. We just need to add the skills

[04:50] and the CLI, right? So, I'll put a link to this down in the description. This walks you through it. The easiest way to

[04:55] do this is frankly to copy the page, hop inside of Claude Code, paste the page into there, and say, "Hey, let's install the Firecrawl skill and the Firecrawl CLI." It will ask you to authenticate. So, at this point, you will need to have gone to Firecrawl and create an account, but it's essentially just a one-click thing, and then you'll be all set. Now

[05:14] before we dive into the Firecrawl tests, just wanted to talk about the Claude Code masterclass really quickly. I just released this a couple weeks ago and it is the number one place to go from zero to AI dev, especially if you do not come from a technical background. I focus on real use cases. I update this

[05:29] every week. And if you want to get your hands on it, you can find the link down in the pinned comment. I also have the free Chase AI community. There's a link

[05:37] to that in the description. So if you're just getting started with AI, have no idea where to go, definitely check that out. So now let's run it through some tests. So over here on the left we have

[05:47] Claude Code with Firecrawl. On the right we have just normal Claude Code which we'll be using web fetch. Now for this test we're having it look at SimilarWeb. Now SimilarWeb is something you

[05:57] can use for competitive research. It gives you stats on different websites. So imagine you have some competitor and you want to keep tabs on how they're doing on their site. Now, the reason we

[06:05] are testing this is because this website has some JavaScript rendering. Some of these statistics that you would want to know for competitive analysis aren't going to be found necessarily in the HTML that web fetch will grab us. So, Claude Code normally should struggle here. Yet, with Firecrawl, we should get

[06:22] everything. So, let's see what happens when we run it. So, we can see here over on the left, it loads the Firecrawl scrape skill. Over here on the right,

[06:28] it's just doing a standard fetch. All right, so it's still going after 4 minutes and 30 seconds. So we're going to shut down the normal web fetch. And

[06:35] we can kind of see what happened here. So right away it tells us the page loads dynamically via JavaScript. So the direct fetch only got the shell. Let me

[06:44] try alternative approaches. So essentially then tried another web search to like find the data in another place. And then on its last fetch, it pretty much got hung. So I let it

[06:54] run for about 3 minutes before we cut it off. So we really didn't get anything from the normal web fetch versus over here with Firecrawl it had no issues handling that right in 42 seconds it gave us a ton of information. So it gave us all the metrics, breaks down the traffic by country, by source, social media breakdown. Right? So it went all

[07:15] out and again in 42 seconds we had no issues. Over here we're hung up for 5 minutes and that was one website, one competitor. Imagine that at scale. Now

[07:22] let's do test number two. This time again Firecrawl is on the left. We are searching Yellow Pages for plumbers in Nashville, Tennessee. Give me a list

[07:28] with business name, phone number, years, and businesses and services they offer. Why Yellow Pages? Why this test? Because

[07:34] it has some anti-bot protections built into their system, right? They don't want you just scraping all their stuff from a terminal. So, let's see how Firecrawl does and let's see how normal Claude Code does. All right. And we're

[07:45] only a minute 30 into this one, but I'm going to cancel this one as well because what do we see here? Boom. Right away, Yellow Pages is aggressively blocking all direct page fetches. Let me try more

[07:56] targeted searches. So, again, it tries to kind of go around the problem to find it. Yet, it just keeps hitting errors. So you just see this error,

[08:05] error, error, error -- just gets hit with 403s over and over and over again. So something like Yellow Pages is already putting up a wall against Claude Code. Yet with Firecrawl, what do we see?

[08:15] Really no issues, right? It used the Firecrawl scrape ability and then pulls in 16 different results in 53 seconds, right? Again, clear win for Firecrawl. And to be honest, I had

[08:28] another demo ready for you with Booking.com, which has even more aggressive anti-bots. But I mean, I don't really want to waste your time because you see what happens if there's almost any bot restrictions to these websites. Claude Code with normal web

[08:40] fetch struggles. Let alone like you saw with SimilarWeb, if there's any sort of JavaScript rendering, it's also going to struggle. And even in cases where Claude Code can push through the JavaScript, again, sort of like these Amazon ones, it does it much less effectively. So I ran

[08:59] it through a test having it look at four Amazon web pages with Firecrawl versus normal. Pretty much the same test we saw. Claude Code was able to do it, but the difference in time was 45 seconds for Firecrawl versus it took Claude Code about 5 and a half minutes to go through the same amount of information.

[09:15] So the answer is pretty clear. When it's like, all right, where does Firecrawl make sense? The second we start talking about scraping at scale where we do need to think about time and we do need to think about token cost, Firecrawl just makes a ton of sense. Especially if there's any sort of anti-bot stuff located at all in the websites you're trying to find. Lastly, let's very quickly cover the open-source version of Firecrawl because this is something you could theoretically run for free. But it's important to know what we do lose if we go this route. And the big things we are

[09:46] going to lose if we go the self-hosted route are the anti-bot protections, right? Firecrawl has its own proprietary fire engine, which is what gets it through all these sort of anti-bot situations. And also you aren't going to be able to use some of the more powerful abilities like Agent or their brand new Browser Interact which is like their version of Playwright. And

[10:08] beyond that there's just a bit more of a technical setup. Like anything if you're going the open source route and you should probably know your way around Docker. But if the open source route is something that appeals to you I will put the link in the description so you can totally check it out. So I hope I was able to open your eyes a little bit when it comes to Firecrawl. This is a really powerful web scraping tool that integrates so nicely with Claude Code now that they have a CLI tool available as well as the skills, right? Super easy to

[10:31] install. We can operate it through natural language. And as you saw with the demo, there are some serious weak points with Claude Code when we're trying to use it as a web scraper, right? And

[10:39] this kind of just shores up those weak points. So, as always, let me know in the comments what you thought. Make sure to check out Chase AI Plus, there's a link to that in the comments if you want to get your hands on my Claude Code Masterclass.

[10:51] And I'll see you around.
