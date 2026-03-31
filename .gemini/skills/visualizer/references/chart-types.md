# Chart Type Selection Guide

A comprehensive reference for choosing the right visualization for your data. Organized by the story your data tells.

---

## 1. Comparison — "How do items differ?"

### Bar Chart (Vertical)
- **Best for:** Comparing values across a small number of categories (3-10)
- **Data:** One categorical variable, one numerical variable
- **Example:** Revenue by cooperative type, Budget allocation by department
- **Tip:** Sort bars by value (descending) unless categories have a natural order

### Bar Chart (Horizontal)
- **Best for:** Comparing values when category names are long, or when you have many categories (10+)
- **Data:** One categorical variable, one numerical variable
- **Example:** Member count by municipality, Ranking of cooperatives by assets
- **Tip:** Always sort by value for rankings

### Grouped Bar Chart
- **Best for:** Comparing multiple measures across categories
- **Data:** One categorical variable, two or more numerical variables
- **Example:** Revenue vs. expenses by cooperative, Male vs. female membership by province
- **Tip:** Limit to 3-4 groups per category; beyond that, use small multiples

### Lollipop Chart
- **Best for:** Same as bar chart but with a cleaner, more modern look
- **Data:** One categorical variable, one numerical variable
- **Example:** Performance scores by branch
- **Tip:** Works best when differences between values are subtle

### Dot Plot / Cleveland Dot Plot
- **Best for:** Precise value comparison across many categories
- **Data:** One categorical variable, one or more numerical variables
- **Example:** Interest rates across different cooperative lending products

### Slope Chart
- **Best for:** Showing change between exactly two time points
- **Data:** Categories measured at two points in time
- **Example:** Cooperative rankings 2023 vs. 2024, Before/after intervention scores

### Dumbbell Chart
- **Best for:** Showing the gap between two values per category
- **Data:** One categorical variable, two numerical variables (start/end, min/max)
- **Example:** Target vs. actual performance by department

---

## 2. Composition — "What makes up the whole?"

### Pie Chart
- **Best for:** Showing parts of a whole when there are 2-6 categories
- **Data:** One categorical variable, one numerical variable (proportions)
- **Example:** Loan portfolio distribution, Membership by type
- **Avoid when:** More than 6 slices, or when slices are similar in size
- **Tip:** Start the largest slice at 12 o'clock position

### Donut Chart
- **Best for:** Same as pie chart, with space for a central metric
- **Data:** One categorical variable, one numerical variable
- **Example:** Fund allocation with total amount in center
- **Tip:** Use the center hole to display a key number (total, target, etc.)

### Stacked Bar Chart
- **Best for:** Composition across multiple categories
- **Data:** One categorical variable, multiple numerical sub-categories
- **Example:** Revenue sources by cooperative over multiple years

### 100% Stacked Bar Chart
- **Best for:** Comparing proportions across categories (not absolute values)
- **Data:** One categorical variable, multiple numerical sub-categories
- **Example:** Loan portfolio mix across branches (as percentages)

### Treemap
- **Best for:** Hierarchical composition with many categories
- **Data:** Hierarchical categorical variables with a size metric
- **Example:** Budget allocation by program > sub-program > activity
- **Tip:** Good for 2-3 levels of hierarchy

### Sunburst Chart
- **Best for:** Hierarchical composition with clear parent-child relationships
- **Data:** Hierarchical categorical variables with a size metric
- **Example:** Organizational structure with resource allocation

### Waffle Chart
- **Best for:** Showing percentages in an intuitive grid format
- **Data:** One or few percentages
- **Example:** 73% of cooperatives are compliant (73 filled squares out of 100)

---

## 3. Trend Over Time — "How has it changed?"

### Line Chart
- **Best for:** Showing trends over continuous time periods
- **Data:** Time variable, one or more numerical variables
- **Example:** Monthly membership growth, Quarterly revenue trend
- **Tip:** Limit to 5-6 lines; use color and annotations strategically

### Area Chart
- **Best for:** Emphasizing the magnitude of a trend
- **Data:** Time variable, one numerical variable
- **Example:** Cumulative savings deposits over time
- **Tip:** Use transparency (alpha) if overlapping multiple areas

### Stacked Area Chart
- **Best for:** Showing how composition changes over time
- **Data:** Time variable, multiple numerical sub-categories
- **Example:** Revenue by source over 5 years

### Sparkline
- **Best for:** Compact trend indicator alongside other data (in tables, dashboards)
- **Data:** Time series, one variable
- **Example:** Inline trend next to each cooperative's current balance

### Step Chart
- **Best for:** Values that change at discrete points (not continuously)
- **Data:** Time variable, one numerical variable
- **Example:** Interest rate changes over time, Policy thresholds

---

## 4. Distribution — "How is the data spread?"

### Histogram
- **Best for:** Showing the frequency distribution of a single variable
- **Data:** One continuous numerical variable
- **Example:** Distribution of cooperative asset sizes, Loan amount distribution
- **Tip:** Choose bin width carefully; too few or too many bins obscure the story

### Box Plot
- **Best for:** Summarizing distribution with median, quartiles, and outliers
- **Data:** One numerical variable, optionally grouped by a category
- **Example:** Salary distribution across cooperative positions

### Violin Plot
- **Best for:** Distribution shape comparison across categories
- **Data:** One numerical variable grouped by a category
- **Example:** Revenue distribution by cooperative type

### Density Plot (KDE)
- **Best for:** Smooth approximation of distribution
- **Data:** One continuous numerical variable
- **Example:** Member age distribution

### Strip Plot / Swarm Plot
- **Best for:** Showing individual data points within categories
- **Data:** One categorical, one numerical variable (small-medium datasets)
- **Example:** Individual cooperative capital adequacy ratios by region

---

## 5. Relationship — "How are variables connected?"

### Scatter Plot
- **Best for:** Showing correlation or relationship between two variables
- **Data:** Two continuous numerical variables
- **Example:** Assets vs. revenue across cooperatives, Training hours vs. performance
- **Tip:** Add a trend line to highlight the relationship direction

### Bubble Chart
- **Best for:** Scatter plot with a third dimension (size)
- **Data:** Two continuous numerical variables + one size variable
- **Example:** Assets vs. revenue, with bubble size = member count

### Heatmap
- **Best for:** Showing patterns in a matrix of values
- **Data:** Two categorical variables, one numerical variable (matrix)
- **Example:** Correlation matrix of financial ratios, Activity by month and day

### Connected Scatter Plot
- **Best for:** Showing how the relationship between two variables evolves over time
- **Data:** Two continuous variables measured over time
- **Example:** Deposits vs. loans over quarters (connected chronologically)

---

## 6. Ranking — "What is the order?"

### Horizontal Bar (Sorted)
- **Best for:** Ranking items from highest to lowest (or vice versa)
- **Data:** One categorical, one numerical variable
- **Example:** Top 20 cooperatives by total assets

### Lollipop (Sorted)
- **Best for:** Cleaner version of ranked bar chart
- **Example:** Performance ranking of branches

### Bump Chart
- **Best for:** Showing how rankings change over time
- **Data:** Categories ranked across multiple time periods
- **Example:** Provincial cooperative count rankings 2020-2025

---

## 7. Flow and Process — "How does it work?"

### Flowchart (Graphviz)
- **Best for:** Step-by-step processes, decision trees
- **Example:** CSEA assessment process, Cooperative registration workflow
- **Tool:** graphviz with `digraph`

### Sankey Diagram
- **Best for:** Showing flow quantities between stages
- **Data:** Source, target, and value for each flow
- **Example:** Fund flow from national to regional to local cooperatives
- **Tool:** plotly `go.Sankey`

### Funnel Chart
- **Best for:** Progressive reduction through stages
- **Data:** Stages with decreasing values
- **Example:** Cooperative registration pipeline (applied > screened > approved > active)
- **Tool:** plotly `go.Funnel`

---

## 8. Hierarchy and Organization — "How is it structured?"

### Org Chart (Graphviz)
- **Best for:** Organizational structure, reporting relationships
- **Example:** BARMM cooperative development office structure
- **Tool:** graphviz with `digraph`, `rankdir=TB`

### Tree Diagram (Graphviz)
- **Best for:** Classification, taxonomy, decision trees
- **Example:** Types of cooperatives classification

### Mind Map
- **Best for:** Concept relationships, brainstorming visuals
- **Tool:** graphviz with `graph` (undirected)

---

## 9. Timeline — "When did things happen?"

### Timeline (Horizontal)
- **Best for:** Chronological sequence of events or milestones
- **Data:** Events with dates and descriptions
- **Example:** Cooperative development milestones, Project implementation schedule
- **Tool:** matplotlib custom (broken_barh or annotated line)

### Gantt Chart
- **Best for:** Project schedules with duration and dependencies
- **Data:** Tasks with start dates, end dates, and optionally dependencies
- **Example:** CSEA implementation timeline, Training schedule
- **Tool:** matplotlib broken_barh or plotly timeline

---

## 10. Geographic — "Where is it?"

### Choropleth Map
- **Best for:** Values by geographic region
- **Data:** Region identifiers + numerical values
- **Example:** Cooperative density by BARMM province
- **Tool:** plotly `go.Choropleth` or `px.choropleth`

### Annotated Map
- **Best for:** Specific locations with callouts
- **Tool:** matplotlib with basemap or plotly mapbox

---

## 11. KPI / Dashboard Elements

### Big Number + Sparkline
- **Best for:** Key performance indicators with trend context
- **Example:** "Total Members: 45,230 [sparkline showing growth]"

### Gauge / Meter
- **Best for:** Progress toward a target
- **Example:** Collection efficiency: 87% of 95% target
- **Tool:** plotly `go.Indicator`

### Bullet Chart
- **Best for:** Actual vs. target with qualitative ranges
- **Example:** Revenue actual vs. target vs. stretch goal

---

## Quick Decision Matrix

| Question | Answer | Chart Type |
|---|---|---|
| How many categories? | 2-6 | Pie, donut |
| How many categories? | 7-15 | Bar chart |
| How many categories? | 15+ | Horizontal bar, treemap |
| Showing change over time? | Yes, one series | Line chart |
| Showing change over time? | Yes, composition | Stacked area |
| Comparing two groups? | Yes | Grouped bar, slope chart |
| Showing parts of whole? | Yes, simple | Pie/donut |
| Showing parts of whole? | Yes, hierarchical | Treemap, sunburst |
| Showing a process? | Yes | Flowchart (graphviz) |
| Showing organization? | Yes | Org chart (graphviz) |
| Showing correlation? | Yes | Scatter, heatmap |
| Showing distribution? | Yes | Histogram, box plot |
| Showing ranking? | Yes | Sorted horizontal bar |
| Showing a schedule? | Yes | Gantt chart, timeline |
| Showing flow of quantities? | Yes | Sankey diagram |
| Showing geographic data? | Yes | Choropleth map |
