# Advanced Concepts from Running Lean

## Table of Contents
- [Cohort Analysis](#cohort-analysis)
- [Customer Happiness Index (CHI)](#customer-happiness-index-chi)
- [Conversion Dashboard Building](#conversion-dashboard-building)
- [Feature Backlog Management](#feature-backlog-management)
- [The Feature Lifecycle (8 Steps)](#the-feature-lifecycle-8-steps)
- [Pivot Experiments](#pivot-experiments)
- [Product/Market Fit Exit Criteria](#productmarket-fit-exit-criteria)
- [Key Quotes and Principles](#key-quotes-and-principles)

---

## Cohort Analysis

**Weekly cohort reports** are essential for accurate measurement during Product/Market Fit stage.

**Why Cohorts Matter:**
- Traffic naturally fluctuates week to week
- Comparing raw metrics across time periods is misleading
- Cohorts allow apples-to-apples comparison of user behavior

**Building a Cohort Report:**

| Reporting Period: Month | Week 1 Cohort | Week 2 Cohort | Week 3 Cohort | Week 4 Cohort |
|-------------------------|---------------|---------------|---------------|---------------|
| **Acquisition** | 90 (70%) | 100 (71%) | 110 (70%) | 120 (69%) |
| **Activation** | 78 (87%) | 85 (85%) | 100 (91%) | 112 (93%) |
| **Retention** | 20 (26%) | 22 (26%) | 27 (27%) | 32 (29%) |
| **Revenue** | 15 (19%) | 16 (19%) | 20 (20%) | 25 (22%) |

**Dealing with Traffic Fluctuations:**
1. Group users by signup week
2. Track each group's progress through funnel over time
3. Compare cohort rates (percentages), not raw numbers
4. Look for upward trending across cohorts = improvement

**Segmenting Your Funnel:**
- Start with the leakiest bucket first (highest drop-off)
- Analyze user properties at each step (device, source, etc.)
- Identify patterns in failed conversions
- A/B test improvements within cohorts

---

## Customer Happiness Index (CHI)

A leading indicator of retention, measured during trial period.

**Formula:**
```
CHI = [ (Days Logged In / Desired Logins) x 0.2 + (Key Activity Completed) x 0.8 ] x 100
```

**Components:**
| Component | Weight | Description |
|-----------|--------|-------------|
| Login frequency | 20% | How often user returns to product |
| Key activity completion | 80% | Did user perform the core value action? |

**Example Calculation:**
- Desired logins: 7 per week
- Actual logins: 4 (57%)
- Key activity: Completed (100%)
- CHI = [(0.57 x 0.2) + (1.0 x 0.8)] x 100 = 91.4

**Interpreting CHI:**
| CHI Score | Interpretation | Action |
|-----------|----------------|--------|
| 80-100 | High engagement | Convert to paid |
| 50-79 | Moderate engagement | Re-engage, troubleshoot |
| 0-49 | Low engagement | Risk of churn, intervene |

**Usage:**
- Calculate weekly for each user during trial
- Trigger lifecycle emails based on CHI thresholds
- Prioritize high-CHI users for conversion outreach

---

## Conversion Dashboard Building

Visualize your entire funnel to identify leaky buckets.

**Dashboard Structure:**

```
CONVERSION DASHBOARD
+-- Period: [Weekly/Monthly]
+-- Cohort: [Week starting date]
|
+-- ACQUISITION
|   +-- Visitors: [count]
|   +-- Rate: [% of total traffic]
|
+-- ACTIVATION
|   +-- Signups: [count]
|   +-- Rate: [% of acquisition]
|
+-- RETENTION
|   +-- Active users: [count]
|   +-- Rate: [% of activation]
|
+-- REVENUE
|   +-- Paying customers: [count]
|   +-- Rate: [% of retention]
|
+-- REFERRAL
    +-- Referrers: [count]
    +-- Rate: [% of revenue]
```

**Retention Trending View:**

| Week Joined | 1 wk | 2 wk | 3 wk | 4 wk | 5 wk | 6 wk |
|-------------|------|------|------|------|------|------|
| Jun 1 | 100% | 45% | 38% | 35% | 32% | 30% |
| Jun 8 | 100% | 48% | 40% | 37% | 35% | ? |
| Jun 15 | 100% | 50% | 42% | 40% | ? | |

**Goal:** See numbers trend UP across cohorts (not just within).

---

## Feature Backlog Management

How to process feature requests without becoming a "feature pusher."

**The 80/20 Rule for Features:**
- 80% of effort -> Improve/optimize EXISTING features
- 20% of effort -> Build NEW features

**Feature Request Workflow:**

```
INCOMING REQUEST
|
+-- Is it Right Action, Right Time?
|   +-- NO -> Ignore it
|   +-- YES
|
+-- Is it a small bug/feature?
|   +-- YES -> Is it an emergency?
|   |         +-- YES -> Fix immediately
|   |         +-- NO -> Add to Task Board
|   +-- NO -> Add to Kanban Board
```

**Kanban Board for Features:**

```
+-------+----------+------+------+---------+----------+---------+---------+
|BACKLOG| MOCKUP   | DEMO | CODE | PARTIAL | VALIDATE | FULL    | VERIFY  |
|       |          |      |      | ROLLOUT | QUAL.    | ROLLOUT | QUANT.  |
+-------+----------+------+------+---------+----------+---------+---------+
| [F1]  | [F4]     |      | [F6] |         |          | [F7]    | [F8]    |
| [F2]  |          | [F5] |      |         |          |         | [F9]    |
| [F3]  |          |      |      |         |          |         |         |
+-------+----------+------+------+---------+----------+---------+---------+
```

**Work-In-Progress (WIP) Limit:** Max 3 features at once in "IN PROGRESS" stages.

---

## The Feature Lifecycle (8 Steps)

1. **Backlog** - Vet against current goals: "Is this Right Action, Right Time?"
2. **Mockup** - Build paper sketches, progress to HTML/CSS mockups
3. **Demo** - Conduct Solution Interview with mockup, kill if no signal
4. **Code** - Break into smaller tasks, continuous deployment
5. **Partial Rollout** - Deploy to subset of users first
6. **Validate Qualitatively** - Conduct usability interviews, iterate
7. **Full Rollout** - Release to all users, WIP lock released
8. **Verify Quantitatively** - Compare cohort before/after, split-test if needed

---

## Pivot Experiments

Systematic approach to testing hypotheses during Product/Market Fit stage.

**The Running Lean Meta Process:**

```
BUILD -> MEASURE/LEARN cycles:

1. Formulate Testable Hypotheses -> TEST PROBLEM
2. Build Mock Solution -> TEST MOCK SOLUTION
3. Build Actual Solution -> TEST SOLUTION QUALITATIVELY
4. Verify Quantitatively -> TEST SOLUTION QUANTITATIVELY
```

**Weekly Rhythm:**
1. **Monday:** Review Conversion Dashboard with entire team
2. **Identify:** Leakiest buckets to fix first
3. **Prioritize:** Features backlog against goals
4. **Formulate:** Bold hypotheses (avoid micro-optimization)
5. **Build:** Smallest thing to test hypothesis
6. **Monitor:** Retention cohorts for upward movement

**When to Split-Test:**

| Scenario | Split-Test? |
|----------|-------------|
| Brand new feature | No - compare to older cohorts |
| Strong signal in qualitative testing | No - proceed to rollout |
| Medium signal in qualitative testing | Yes - validate quantitatively |
| Alternate flows / improvements | Yes - measure which performs better |

---

## Product/Market Fit Exit Criteria

| Criterion | Target | How to Measure |
|-----------|--------|----------------|
| **Retention** | >=40% monthly | Cohort retention at 30+ days |
| **Sean Ellis Test** | >=40% "very disappointed" | Survey activated users |
| **Revenue** | Customers paying | First revenue on dashboard |
| **Bonus** | Break-even | Revenue >= Costs |

**What's Next After Product/Market Fit?**
- Shift from learning to scaling
- Focus moves to Acquisition and Referral optimization
- Quantitative metrics and split testing play larger role
- Build referral/viral loops

---

## Key Quotes and Principles

> **"Customers don't care about your solution. They care about their problems."** - Dave McClure

> **"Life's too short to build something nobody wants."** - Ash Maurya

> **"Having more passion for the solution than the problem is a problem."**

> **"Your competitors are NOT who you think they are BUT who your customers think they are."**

> **"An early adopter is a customer who ranks one or more of the problems you're solving as a must-have and will generally pay to have it solved."**

> **"Before you launch, measure what customers say. After you launch, measure what customers do."**

> **"You have achieved Product/Market Fit when you are retaining 40% of your activated users month over month."**

> **"The job of your UVP is making a compelling promise. The job of the MVP is delivering on that promise."**

> **"The right price is one the customer accepts but with a little resistance."**

> **"Put down the compiler until you learn why they're not buying."** - Jason Cohen
