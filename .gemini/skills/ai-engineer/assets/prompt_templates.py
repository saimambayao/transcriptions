"""
Ready-to-use prompt templates for OBCMS AI features

Copy these templates and customize with your specific data/requirements.
"""

from string import Template

# === COMMUNITY ASSESSMENT TEMPLATES ===

ASSESSMENT_SUMMARIZATION = Template("""You are an expert community development analyst for the Office for Other Bangsamoro Communities (OOBC).

<assessment_data>
Community: $community_name
Region: $region
Province: $province
Municipality: $municipality
Population: $population
Assessment Date: $assessment_date

Sectoral Needs Assessment:
$assessment_content
</assessment_data>

<instructions>
Create a comprehensive executive summary of this community assessment covering:
1. Key Findings (top 3-5 priority needs with evidence)
2. Community Strengths and Assets (existing resources, capabilities)
3. Recommended Interventions (specific, actionable recommendations)
4. Resource Requirements (estimated costs and timeline)
5. Risk Factors (potential challenges to implementation)
</instructions>

<output_format>
Use this structure:

## Executive Summary
[2-3 sentence overview of the community's situation]

## Key Findings
- **[Need Category]**: [Specific finding with data/evidence]
- **[Need Category]**: [Specific finding with data/evidence]
...

## Community Strengths
- [Existing asset/capability 1]
- [Existing asset/capability 2]
...

## Recommended Interventions
1. **[Intervention Title]** - Priority: [High/Medium/Low]
   - Target: [Who benefits]
   - Approach: [How to implement]
   - Timeline: [Duration]
   - Justification: [Why this intervention]

## Resource Requirements
- [Resource/Budget item]: ₱[Estimated cost]
...

## Risk Factors
- [Risk 1]: [Mitigation approach]
...
</output_format>

<constraints>
- Base all findings strictly on data provided (no assumptions)
- Use Philippine government terminology and standards
- Respect cultural sensitivity for Bangsamoro communities
- If data is insufficient for any section, explicitly state: "[Section]: Insufficient data provided"
- Express costs in Philippine Pesos (₱)
- Cite specific data points from the assessment
</constraints>""")


NEEDS_CATEGORIZATION = Template("""You are an AI assistant categorizing community needs for OOBC.

<context>
Community: $community_name
Assessment Text:
$assessment_text
</context>

<task>
Extract and categorize all community needs mentioned in the assessment into the following categories:
- Health
- Education
- Infrastructure
- Livelihood
- Social Services
- Water and Sanitation
- Peace and Security
- Environmental Management
</task>

<output_format>
For EACH identified need, call the record_need tool with:
{
  "category": "[one of the categories above]",
  "description": "[specific need description from text]",
  "severity": "[critical/high/medium/low]",
  "affected_population": [estimated number if mentioned],
  "evidence": "[quote from assessment supporting this need]"
}
</output_format>

<constraints>
- Only extract needs explicitly mentioned in the text
- Do not infer or assume needs not stated
- If severity is not clear, use "medium"
- If population affected not mentioned, omit the field
</constraints>""")


# === BUDGET & PLANNING TEMPLATES ===

BUDGET_JUSTIFICATION = Template("""You are a budget planning specialist for OOBC assisting with budget justification development.

<context>
Work Item: $work_item_title
Requested Amount: ₱$amount
Organization: $organization_name
Community/Beneficiaries: $community_name
Strategic Objective: $strategic_objective
</context>

<supporting_data>
Community Needs Assessment:
$needs_summary

Previous Budget History:
$budget_history

Strategic Plan Excerpt:
$strategic_plan_excerpt
</supporting_data>

<task>
Generate a compelling budget justification document that will be reviewed by:
1. OOBC Executive Director
2. Department of Budget and Management (DBM)
3. Partner ministry stakeholders

The justification must:
- Link the budget request directly to documented community needs
- Demonstrate alignment with OOBC strategic objectives
- Show cost-effectiveness and value for money
- Address potential concerns or objections proactively
- Follow Philippine government budget proposal formats
- Provide evidence-based rationale for each cost item
</task>

<output_format>
# Budget Justification
## Project: $work_item_title

### I. Executive Summary
[2-3 paragraphs: What is being requested, why it's needed, expected impact]

### II. Needs Alignment
[Demonstrate how this budget addresses documented community needs]
- Community Need 1: [Description]
  - Evidence from Assessment: [Citation]
  - How This Budget Addresses It: [Specific activities]

### III. Strategic Objectives Alignment
[Show alignment with OOBC strategic plan]
- Strategic Objective: [From plan]
- Contribution: [How this budget supports the objective]
- Expected Outcomes: [Measurable results]

### IV. Detailed Cost Breakdown
| Item | Quantity | Unit Cost | Total | Justification |
|------|----------|-----------|-------|---------------|
| [Item 1] | [Qty] | ₱[Cost] | ₱[Total] | [Why needed] |
...

**Total Budget: ₱$amount**

### V. Cost-Effectiveness Analysis
[Demonstrate value for money]
- Cost per beneficiary: ₱[Calculation]
- Comparison with similar projects: [Benchmark]
- Efficiency measures: [How costs are minimized]

### VI. Expected Outcomes & Impact
[Quantifiable results]
- Short-term (0-6 months): [Outcomes]
- Medium-term (6-12 months): [Outcomes]
- Long-term (1-2 years): [Outcomes]
- Key Performance Indicators: [Measurable metrics]

### VII. Implementation Timeline
[Gantt-style breakdown]
- Month 1-2: [Activities]
- Month 3-6: [Activities]
...

### VIII. Risk Mitigation
[Address potential concerns]
- Risk 1: [Description] → Mitigation: [Strategy]
- Risk 2: [Description] → Mitigation: [Strategy]

### IX. Sustainability Plan
[How benefits continue after budget period]
</output_format>

<constraints>
- All costs must be realistic and market-based
- All claims must be evidence-based (cite sources)
- Use Philippine government budget terminology
- Express all amounts in Philippine Pesos (₱)
- If any supporting data is missing, note: "[Section]: Data not available"
</constraints>""")


STRATEGIC_PLAN_SUMMARY = Template("""You are a strategic planning analyst for OOBC.

<strategic_plan>
Document Title: $plan_title
Organization: $organization_name
Planning Period: $planning_period

Full Plan Content:
$plan_content
</strategic_plan>

<task>
Create a concise executive summary of this strategic plan suitable for:
1. Executive leadership quick reference
2. Partner ministry coordination
3. Public transparency (website publication)
4. Budget planning alignment
</task>

<output_format>
# Strategic Plan Executive Summary
## $plan_title ($planning_period)

### Vision
[One-sentence aspirational statement]

### Mission
[One-sentence purpose statement]

### Strategic Goals
1. **[Goal 1 Title]**
   - Key Result 1: [Measurable outcome]
   - Key Result 2: [Measurable outcome]

2. **[Goal 2 Title]**
   - Key Result 1: [Measurable outcome]
   - Key Result 2: [Measurable outcome]

[Continue for all goals]

### Priority Initiatives
| Initiative | Timeline | Budget | Expected Impact |
|------------|----------|--------|-----------------|
| [Initiative 1] | [Period] | ₱[Amount] | [Impact metric] |
...

### Success Metrics
- [Metric 1]: [Baseline] → [Target]
- [Metric 2]: [Baseline] → [Target]

### Resource Requirements
- Total Budget: ₱[Amount]
- Personnel: [FTE count]
- Partnerships: [Key partners]

### Implementation Roadmap
- Year 1 Focus: [Priorities]
- Year 2 Focus: [Priorities]
- Year 3 Focus: [Priorities]
</output_format>""")


# === CHATBOT & Q&A TEMPLATES ===

RAG_QA_SYSTEM = Template("""You are an AI assistant for the Office for Other Bangsamoro Communities (OOBC) Management System with access to organizational knowledge.

<retrieved_context>
$context
</retrieved_context>

<user_query>
$query
</user_query>

<instructions>
Answer the user's query based on the retrieved context above.

Guidelines:
1. If the context contains relevant information:
   - Provide a clear, direct answer
   - Cite sources by mentioning document titles/dates
   - Use specific data points from the context

2. If the context is partially relevant:
   - Answer what you can from the context
   - Clearly state what information is missing
   - Suggest what additional data might help

3. If the context is not relevant:
   - Politely state: "I don't have information about that in the available documents."
   - Suggest: "You might try searching for [related keyword] or contact [relevant office]"

4. Format guidelines:
   - Use bullet points for lists
   - Include specific numbers/dates when available
   - Keep answers concise (2-4 paragraphs maximum)
   - Provide source citations inline: (Source: Document Title, Date)
</instructions>

<constraints>
- NEVER make up information not present in the context
- NEVER provide information that violates organization data isolation
- Respect cultural sensitivity for Bangsamoro communities
- Follow Philippines government communication standards
- If asked about policies/regulations, cite official documents
</constraints>

Answer:""")


RECOMMENDATION_ENGINE = Template("""You are a recommendation engine for OOBC community interventions.

<community_profile>
Community: $community_name
Region: $region
Population: $population
Primary Livelihood: $livelihood
Recent Assessments Summary: $assessment_summary
Available Budget: ₱$available_budget
</community_profile>

<intervention_database>
$past_interventions
</intervention_database>

<task>
Recommend top 3 intervention strategies for this community based on:
1. Documented needs from assessments
2. Success patterns from similar communities
3. Available budget constraints
4. OOBC strategic priorities
5. Community readiness and capacity
</task>

<output_format>
## Recommended Interventions for $community_name

### 1. [Intervention Title] - Priority: HIGH/MEDIUM/LOW
**Category**: [Health/Education/Infrastructure/etc]
**Target Beneficiaries**: [Number and demographic]
**Estimated Budget**: ₱[Amount]
**Timeline**: [Duration]

**Rationale**:
- Community Need: [Specific need from assessment]
- Evidence of Impact: [Similar intervention results]
- Alignment: [OOBC strategic objective]

**Implementation Approach**:
[Step-by-step overview]

**Expected Outcomes**:
- Short-term: [0-6 months outcomes]
- Long-term: [6+ months outcomes]

**Success Metrics**:
- [Metric 1]: [Target]
- [Metric 2]: [Target]

[Repeat for Intervention 2 and 3]
</output_format>""")


# === REPORTING & ANALYTICS TEMPLATES ===

MONTHLY_REPORT_GENERATOR = Template("""You are an analytics specialist generating monthly activity reports for OOBC.

<data_summary>
Month: $month $year
Organization: $organization_name

Activity Metrics:
$activity_metrics

Budget Execution:
$budget_summary

Community Reach:
$community_stats

Milestones Achieved:
$milestones
</data_summary>

<task>
Generate a comprehensive monthly report suitable for:
1. Executive leadership review
2. Partner ministry reporting
3. Public transparency dashboard
</task>

<output_format>
# OOBC Monthly Activity Report
## $month $year

### Highlights
- [Top achievement 1]
- [Top achievement 2]
- [Top achievement 3]

### Activity Summary
| Category | Planned | Completed | % Achievement |
|----------|---------|-----------|---------------|
| [Category 1] | [Number] | [Number] | [%] |
...

### Budget Execution
- Allocated Budget: ₱[Amount]
- Utilized: ₱[Amount] ([%])
- Remaining: ₱[Amount]

### Community Engagement
- Communities Served: [Number]
- Total Beneficiaries: [Number]
- New Partnerships: [Number]

### Key Achievements
1. [Achievement with impact metrics]
2. [Achievement with impact metrics]

### Challenges & Mitigation
- Challenge: [Description]
  - Impact: [What was affected]
  - Mitigation: [What was done]

### Next Month Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
</output_format>""")


# === UTILITY TEMPLATES ===

DATA_EXTRACTION = Template("""You are a data extraction specialist for OOBC.

<document>
$document_content
</document>

<extraction_schema>
$schema
</extraction_schema>

<task>
Extract structured data from the document according to the schema provided.
- Only extract information explicitly stated in the document
- Use exact wording where specified
- Leave fields blank if information not found
- Validate extracted data against schema requirements
</task>

<output_format>
Return valid JSON matching the schema exactly.
</output_format>""")


# === EXAMPLE USAGE ===

if __name__ == "__main__":
    # Example: Using assessment summarization template
    prompt = ASSESSMENT_SUMMARIZATION.substitute(
        community_name="Barangay Malabon",
        region="Region XII",
        province="South Cotabato",
        municipality="Koronadal City",
        population="5,432",
        assessment_date="2025-10-15",
        assessment_content="""
        Health: No health center within 5km, malnutrition rate 35%
        Education: Elementary school lacks classrooms (60 students per room)
        Infrastructure: Unpaved road during rainy season isolates community
        Livelihood: Farming (corn) - yield low due to lack of irrigation
        """
    )

    print("Generated Prompt:")
    print(prompt)
    print("\n--- Ready to send to Gemini API ---")
