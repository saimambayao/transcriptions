**How to Build Your Metrics Dashboard**

**Introduction and the Information Problem**

**00:00**
Hi, this is Ash with Spark59. Today I'm going to talk about how you build a company-wide metrics dashboard that not only everybody on your team can understand, but one that they'll actually want to use.

**00:13**
First, let's visit the problem. When we launch a product, lots of things can and do go wrong. The common tendency is to want to collect as much data as possible.

**00:22**
But in today's world, where we can measure almost anything, we often end up drowning in a sea of information.

**The Google Analytics Trap**

**00:29**
Most of you should recognize this. This is a Google Analytics page. Almost all of us start here. Between all the tabs on the left, there are literally hundreds of numbers you can look at.

**00:40**
Which ones do you pay attention to? So many of them seem interesting. You can easily spend a ton of time just surfing all these numbers without uncovering any real actionable insights.

**00:51**
Another popular trend right now is real-time. This is a Chartbeat page. I use this on my blog. Here I can see that at 11:45 on January 31st, 14 people were visiting my site and I can see what pages they were on.

**01:05**
Again, very interesting data that helps feed my vanity after I publish the post. But in a blogging context, which isn't inherently real-time for me, the dashboard has little impact on what I do.

**The Failure of Homegrown Dashboards**

**01:18**
Most homegrown dashboards aren't nearly as well designed as these products and make the problem even worse. They start out quite simple. Someone puts a few metrics on a page, and over time it ends up as a hodgepodge of several numbers, tables, and graphs, each requested by a different department in the company.

**01:36**
It's hard to quickly assess the overall health of a product when looking at a dashboard like this.

**Vision vs. Reality**

**01:42**
When we envision the perfect metrics dashboard, this is the image we have in mind. We'd like to be able to pull up any piece of information with just a few hand gestures like Tony Stark here.

**01:53**
But this is what reality really looks like. We start out with a few tools at a time, and pretty soon we're drowning.

**The Goal: Actionable Insights**

**02:00**
The key isn't getting to more numbers but actionable learning. Ultimately, your dashboard needs to be able to answer these three basic questions:

1. Are we making progress? - WHAT
2. What caused the change? - WHY
3. How do we improve? - HOW

**02:23**
Today, I'm going to mostly focus on just the first and maybe a little bit of the second.

**Reason 1: Measuring What is Easy**

**02:30**
But before we get into that, let's take a step back and see why measuring this stuff is so hard in the first place. The first reason is that we tend to measure what's easy to measure.

**02:41**
With just a single snippet of JavaScript code, you can get access to hundreds of data points, which is why tools like Google Analytics are so popular.

**02:50**
But there's an inverse relation between what's easy to measure and what's valuable to measure. Another way of saying this is that measuring the really critical stuff—the stuff that can really 10x your business—is hard work, but it's worth it.

**Reason 2: Vanity Metrics**

**03:04**
The second reason is that we often tend to prefer reporting good news over bad news, which is what in the lean startup world we refer to as vanity metrics.

**03:15**
A vanity metric is typically a number we use to make ourselves feel good or our competitors look bad.

**03:22**
For instance, when Skype launched, they used the number of downloads on their homepage because it was a really big number and growing, even though it was probably not the most accurate indicator of product usage.

**03:34**
Now, there is a place for vanity metrics when used this way. They can be used to dissuade competition or serve as social proof. The danger lies when these numbers are also used as the internal measure of progress.

**03:45**
A litmus test for whether you have a vanity metric on your hands is if the number can go nowhere but up and to the right.

**03:53**
A classic vanity metric is reporting the cumulative number of signups over time. The slope of this chart could vary month over month and even flatline, but it can never go down.

**04:05**
How about if I change the metric from signups to revenue? Is this still a vanity metric? The answer is yes, because it suffers from the same up and to the right problem from earlier. The cumulative revenue can never go down.

**Reason 3: A Constantly Changing Product**

**04:20**
The third reason that measuring progress of a product is so hard is that the product is always changing. You're constantly adding new features and running new marketing campaigns.

**04:31**
Your product is changing constantly, and you need a way to tie back your observed results back to specific and repeatable actions you took in the past so that you can do more of the things that are working and stop doing those that are not.

**The Three A's of Metrics**

**04:45**
So how do you build a dashboard that lets you do all of this? When building your dashboard, it's helpful to run them through Eric Ries's three A's of metrics test.

**04:54**
In order for your metrics dashboard to be effective, it needs to be actionable, accessible, and auditable. Let's first define what each of these things mean, and then we'll dig into how you do them.

**Actionable Metrics**

**05:06**
Actionable metrics means that it should be possible to tie specific repeatable actions to observed results. Once you know what actions caused the results, you can then make a decision to do more of what worked and stop doing what isn't working.

**Accessible Metrics**

**05:21**
The first part of making your metrics accessible is simply about making them available to everyone in your company. That is not just limiting them to marketing or development teams.

**05:31**
In a lean startup, we encourage entrepreneurs to take a more objective and empirical outlook towards measuring progress, and opening your progress dashboard to everyone in the company, no matter how uncomfortable that may feel, is a prerequisite first step.

**05:47**
But there's a second part to accessibility. It's not enough to just open your metrics dashboard to everyone if not everyone understands what it's telling them.

**05:56**
To illustrate this point, let's take a look at a popular chart often used for cohort analysis. Cohort analysis is the gold standard for measuring progress, which we'll get into a bit later.

**06:06**
But this chart does a poor job of communicating progress that anyone can understand. If people in your company cannot quickly tell if the product is getting better or worse from the dashboard, then it's just not good enough.

**Auditable Metrics**

**06:23**
The last A, making your metrics auditable, is equally as important. If you succeed at effectively communicating progress, particularly the lack of it, you will inevitably be challenged by someone on the team who won't believe the numbers.

**06:38**
In order to address these concerns, you need to provide a way for anyone on your team to be able to go behind the numbers and audit them if they wish.

**06:47**
One effective technique is tying the numbers back to the people or customers who caused them. If someone does not believe the numbers, they're free to pull up the customer record and audit it for themselves.

**06:59**
Tying people to numbers also has a more powerful emotional effect. Saying you have a 20% activation rate doesn't hurt as much as realizing that every single day, you can see 100 real people visit your site, and out of them, 80 people consistently leave and never come back.

**Macro Metrics vs. Micro Events**

**07:17**
In order to build an effective metrics dashboard, you need all three. Your metrics dashboard needs to be actionable, accessible, and auditable. So let's put these principles to work.

**07:30**
The first step is to use just a handful of macro metrics to baseline the progress of your product. Macro metrics capture key customer lifecycle events and are critical for learning.

**07:43**
A particular model we subscribe to is Dave McClure's pirate metrics, which you are probably familiar with already. Even though this model was built with high-tech startups in mind, I find it's just as applicable to other types of businesses.

**07:57**
The model captures the key customer lifecycle events that define the conversion funnel, starting from how customers first learn about you to becoming happy, paying, and passionate customers.

**08:08**
Each of these macro events are in turn made up of a number of sub-funnels or micro events, which are best suited for more detailed troubleshooting.

**Visualization and the Funnel Chart**

**08:21**
The next step is using the right kind of visualization. The pirate metrics model is essentially a conversion funnel, and it's natural to want to use a funnel chart because it's simple, visual, and pretty popular.

**08:36**
But the funnel chart is actually a poor visualization for communicating progress, and here's why. The problem arises when you put two funnel charts next to each other.

**08:44**
Quick, can you tell me which of these is better? Can you tell me if the product was better in June or in May? The funnel visualization itself doesn't answer this question, and you end up having to compare all the numbers.

**09:00**
We could try making the funnel fatter or taller to represent the size of the funnel, but that only makes the chart even harder to read because the elements are no longer aligned.

**09:10**
This version is a lot better. With the up and down traffic light indicators, we can now see that while acquisition and activation were up in June, retention and revenue were down. But the funnel shape itself is providing no value here.

**09:23**
So we could replace it with an even simpler bar chart, which would look something like this. This version is a lot cleaner and easier to read, but it still suffers from a problem.

**09:34**
I can see here that the retention rate dropped in June, but does everyone in the company know if a 50% retention rate is good or bad? Is it something we need to worry over?

**The Bullet Graph**

**09:43**
We can solve this with a bullet graph. The bullet graph was invented by Stephen Few, and it provides two additional enhancements to the bar chart.

**09:52**
The first is the use of shading to designate zones of bad, satisfactory, and good zones. So now I can see that even though the retention rate dropped in June, 50% is still in the good zone and is not something to panic over.

**10:08**
We can optimize this visualization even further. Data visualization experts strive to reduce the ink to information ratio, which is something we can do using the second enhancement provided by the bullet chart.

**10:22**
Instead of placing two funnels side by side, we can use a ticker symbol to encode the previous month's results and collapse this view into a single chart like this.

**10:31**
I can quickly tell the activation rate in June was better than May, the retention rate was lower, and the paid conversion rate was about the same. This version is not only a lot more compact, but it also communicates the full progress story quite effectively.

**People Behind the Numbers**

**10:48**
And finally, you need to provide a way to get to the people behind the numbers. I should be able to take any of my sub-funnel metrics and be able to see the people that either performed the action or failed to perform that particular action.

**11:06**
So now that you know that your metrics dashboard needs to have the three A's, let's see one in action. I'm going to share screenshots of our own metrics dashboard.

**Case Study: Lean Canvas Metrics Dashboard**

**11:18**
We built our dashboard in a hierarchical fashion. At the topmost level, we only show trending of just the five macro metrics that we track on a daily, weekly, and monthly basis.

**11:29**
This gives us a standard measure of progress and a baseline for the health of our product. We can click at any point in the graph to blow up the view and see a side-by-side comparison of the funnel.

**11:41**
In this case, I clicked on July, and I can see how July performed compared to its previous and next months.

**11:47**
There are two more levels. I can click on a particular macro metric in the funnel to see the sub-funnel made up of all the micro events we also track.

**11:56**
In this case, I can see all the micro events that occurred between signup and activation. The ideal conversion dashboard is part metrics and part customer relationship management or CRM.

**12:08**
You have to be able to go behind the numbers to the people, which you can see here as well. We can finally click on any particular person on the right and pull up a Facebook-like timeline of the user's full activity stream.

**12:22**
This is immensely helpful when troubleshooting customer issues.

**Conclusion and Cohort Analysis**

**12:27**
So now that you know what to put on your dashboard, I'm going to throw in a little twist. You also have to know how to accurately measure these metrics. It's not enough to know just what to measure.

**12:37**
Which brings us to the second goal of an effective metrics dashboard. Ironically, as you add more customers, measuring progress actually becomes harder, not easier.

**12:47**
This is because your product is changing, you're adding new features, your customers are changing—you need a way to be able to tie cause and effect more accurately.

**12:55**
Cohort analysis is the gold standard for measuring progress. If you have been following lean startup for a while, you've probably heard of cohort analysis.

**13:02**
Unfortunately, most people make it a lot more complicated than it should be. Next time I'll take a deep dive into the world of cohorts and hopefully explain it in a way that even your mom will be able to understand. Until then, take care.

***

**Organized Notes**

**Core Dashboard Principles (02:00)**
An effective metrics dashboard must answer three critical questions to drive actionable learning:
*   **Are we making progress?** (Determines the "What")
*   **What caused the change?** (Determines the "Why")
*   **How do we improve?** (Determines the "How")

**The Three A's of Metrics (04:45)**
Coined by Eric Ries, these are the standards for assessing metric value:
*   **Actionable (05:06):** Metrics must tie specific, repeatable actions to observed results to inform future decisions.
*   **Accessible (05:21):** Data should be available to everyone in the company. Furthermore, the data must be easy to read and understand viscerally.
*   **Auditable (06:23):** Users should be able to "go behind the numbers" to verify data. Tying metrics to specific customer records provides social/emotional weight and verification.

**The Problem with Vanity Metrics (03:04)**
*   **Definition:** Metrics that make a company look good on paper but do not correlate with actual product health (e.g., cumulative signups or cumulative revenue).
*   **Litmus Test (03:45):** If a chart can only go "up and to the right" and never down, it is likely a vanity metric.

**Optimal Visualization: The Bullet Graph (09:43)**
While funnel charts are popular, they are poor for side-by-side monthly comparisons. The Bullet Graph, created by Stephen Few, is superior because:
*   **Context Shading:** Uses background shading to show zones of "bad," "satisfactory," and "good."
*   **Ticker Symbols:** Uses a small line to show the previous month's results on the current month's bar, allowing for a compact, single-chart comparison.

**Pirate Metrics (AARRR) (07:43)**
Ash Maurya utilizes Dave McClure’s framework for macro metrics:
*   **Acquisition:** How users find you.
*   **Activation:** Do users have a great first experience?
*   **Retention:** Do users come back?
*   **Revenue:** How do you make money?
*   **Referral:** Do users tell others?

**Hierarchical Dashboard Structure (11:18)**
For clarity and utility, the dashboard should follow a drill-down logic:
1.  **Top Level:** Macro metrics trending over time (AARRR).
2.  **Middle Level:** Sub-funnel micro-events (specific steps between sign-up and activation).
3.  **Bottom Level (12:17):** Individual user activity stream (CRM-style timeline).