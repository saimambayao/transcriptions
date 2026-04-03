# Responsible AI Implementation

Comprehensive guide to ensuring AI safety, bias detection, and compliance in OBCMS.

## Why Responsible AI Matters

**Legal Requirements:**
- Philippines Data Privacy Act 2012 (DPA)
- EU AI Act (if serving EU citizens)
- Government transparency requirements

**Ethical Obligations:**
- Fairness for Bangsamoro communities
- Avoiding perpetuation of bias
- Transparency in AI decision-making
- Accountability for AI outputs

**Business Risks:**
- Reputational damage from biased outputs
- Legal liability for harmful recommendations
- Loss of user trust
- Regulatory penalties

---

## Safety Guardrails Implementation

### 1. Input Validation

**Prevent prompt injection:**
```python
def validate_ai_input(user_input: str, max_length: int = 10000) -> str:
    """Validate and sanitize user input before LLM processing."""

    # Check length
    if len(user_input) > max_length:
        raise ValueError(f"Input exceeds maximum length of {max_length}")

    # Detect prompt injection patterns
    injection_patterns = [
        r"ignore\s+(all\s+)?previous\s+instructions",
        r"disregard\s+(all|everything)",
        r"you\s+are\s+now",
        r"forget\s+(everything|all)",
        r"system\s*:\s*",
        r"<\s*system\s*>",
    ]

    import re
    for pattern in injection_patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            logger.warning(f"Prompt injection detected: {pattern}")
            raise SecurityError("Input contains suspicious patterns")

    # Sanitize HTML/script tags
    import bleach
    sanitized = bleach.clean(user_input, strip=True)

    return sanitized
```

**Django view integration:**
```python
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@login_required
def ai_query_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('query', '')

        try:
            # Validate input
            sanitized_input = validate_ai_input(user_input)

            # Process with AI
            response = process_with_ai(sanitized_input, request.user.organization)

            return JsonResponse({'response': response})

        except SecurityError as e:
            return JsonResponse({'error': str(e)}, status=400)
```

---

### 2. Output Moderation

**Content filtering:**
```python
def moderate_ai_output(response: str, user_context: dict) -> str:
    """Check AI output for harmful content before showing to users."""

    # 1. Check for toxic content
    toxicity_score = check_toxicity(response)
    if toxicity_score > 0.7:
        logger.warning(f"High toxicity detected: {toxicity_score}")
        return "[Response blocked: inappropriate content detected]"

    # 2. Check for PII leakage
    if contains_pii(response):
        logger.warning("PII detected in AI response")
        response = redact_pii(response)

    # 3. Check for organization data leakage
    if leaks_other_org_data(response, user_context['organization']):
        logger.critical("Data isolation breach detected!")
        return "[Response blocked: data isolation violation]"

    # 4. Fact-check critical claims (optional)
    if contains_factual_claims(response):
        flagged_claims = verify_claims(response)
        if flagged_claims:
            logger.info(f"Unverified claims: {flagged_claims}")
            response += "\n\n⚠️ Note: Some claims in this response are AI-generated and should be verified."

    return response


def check_toxicity(text: str) -> float:
    """Check text for toxic content using external API or local model."""
    # Option 1: Perspective API (Google)
    # from googleapiclient import discovery
    # client = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)
    # response = client.comments().analyze(body={'comment': {'text': text}}).execute()
    # return response['attributeScores']['TOXICITY']['summaryScore']['value']

    # Option 2: Local transformer model
    from transformers import pipeline
    classifier = pipeline("text-classification", model="unitary/toxic-bert")
    result = classifier(text[:512])[0]  # First 512 chars
    if result['label'] == 'toxic':
        return result['score']
    return 0.0


def contains_pii(text: str) -> bool:
    """Detect Personal Identifiable Information."""
    import re

    pii_patterns = [
        r'\b\d{3}-\d{2}-\d{4}\b',  # SSN-like patterns
        r'\b\d{4}-\d{4}-\d{4}-\d{4}\b',  # Credit card
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
        r'\b\d{3}-\d{3}-\d{4}\b',  # Phone
    ]

    for pattern in pii_patterns:
        if re.search(pattern, text):
            return True

    return False
```

---

### 3. Bias Detection

**Detect stereotypes and unfair treatment:**
```python
def detect_bias(response: str, protected_attributes: list = None) -> list:
    """Detect potential bias in AI responses."""

    if protected_attributes is None:
        protected_attributes = ['gender', 'ethnicity', 'religion', 'age', 'disability']

    bias_signals = []

    # 1. Check for gendered language
    if 'gender' in protected_attributes:
        gendered_terms = detect_gendered_language(response)
        if gendered_terms:
            bias_signals.append({
                'attribute': 'gender',
                'type': 'gendered_language',
                'severity': 'low',
                'terms': gendered_terms,
            })

    # 2. Check for ethnic stereotypes
    if 'ethnicity' in protected_attributes:
        stereotypes = detect_ethnic_stereotypes(response)
        if stereotypes:
            bias_signals.append({
                'attribute': 'ethnicity',
                'type': 'stereotype',
                'severity': 'high',
                'patterns': stereotypes,
            })

    # 3. Check for religious bias
    if 'religion' in protected_attributes:
        religious_bias = detect_religious_bias(response)
        if religious_bias:
            bias_signals.append({
                'attribute': 'religion',
                'type': 'bias',
                'severity': 'high',
                'evidence': religious_bias,
            })

    # Log all bias signals
    if bias_signals:
        logger.warning(f"Bias detected: {bias_signals}")

    return bias_signals


def detect_gendered_language(text: str) -> list:
    """Detect unnecessarily gendered language."""
    import re

    gendered_patterns = [
        (r'\bhe\b.*\b(doctor|engineer|scientist|leader)', 'male-default profession'),
        (r'\bshe\b.*\b(nurse|teacher|secretary|assistant)', 'female-default profession'),
    ]

    findings = []
    for pattern, description in gendered_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            findings.append({
                'pattern': pattern,
                'description': description,
            })

    return findings
```

---

### 4. Fairness Testing

**Test AI for disparate impact:**
```python
class FairnessEvaluator:
    """Evaluate AI system for fairness across protected groups."""

    def test_demographic_parity(self, predictions: pd.DataFrame,
                                protected_attribute: str) -> dict:
        """
        Test if positive outcomes are distributed equally across groups.

        Demographic Parity: P(Y=1|A=a) = P(Y=1|A=b) for all groups a, b
        """
        results = {}

        for group in predictions[protected_attribute].unique():
            group_data = predictions[predictions[protected_attribute] == group]
            positive_rate = (group_data['prediction'] == 1).mean()
            results[group] = positive_rate

        # Check if rates are similar (within 10% threshold)
        max_rate = max(results.values())
        min_rate = min(results.values())
        disparity = max_rate - min_rate

        return {
            'metric': 'demographic_parity',
            'groups': results,
            'disparity': disparity,
            'passes': disparity < 0.10,  # 10% threshold
        }

    def test_equal_opportunity(self, predictions: pd.DataFrame,
                              protected_attribute: str, ground_truth: str) -> dict:
        """
        Test if true positive rates are equal across groups.

        Equal Opportunity: P(Y^=1|Y=1,A=a) = P(Y^=1|Y=1,A=b)
        """
        results = {}

        for group in predictions[protected_attribute].unique():
            group_data = predictions[predictions[protected_attribute] == group]
            # True positive rate
            positive_actual = group_data[ground_truth] == 1
            tpr = (group_data.loc[positive_actual, 'prediction'] == 1).mean()
            results[group] = tpr

        disparity = max(results.values()) - min(results.values())

        return {
            'metric': 'equal_opportunity',
            'groups': results,
            'disparity': disparity,
            'passes': disparity < 0.10,
        }


# Usage example
def audit_ai_recommendations():
    """Audit AI recommendation system for fairness."""
    evaluator = FairnessEvaluator()

    # Get recommendations for different demographic groups
    predictions = get_ai_recommendations_with_demographics()

    # Test fairness
    parity_result = evaluator.test_demographic_parity(predictions, 'ethnicity')
    opportunity_result = evaluator.test_equal_opportunity(predictions, 'ethnicity', 'actual_need')

    if not parity_result['passes']:
        logger.warning(f"Demographic parity violation: {parity_result}")

    if not opportunity_result['passes']:
        logger.warning(f"Equal opportunity violation: {opportunity_result}")

    return {
        'demographic_parity': parity_result,
        'equal_opportunity': opportunity_result,
    }
```

---

### 5. Audit Logging

**Comprehensive audit trail:**
```python
class AIInteraction(models.Model):
    """Log every AI interaction for compliance and debugging."""

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    feature = models.CharField(max_length=100)
    model = models.CharField(max_length=50)

    # Input/Output
    prompt = models.TextField()
    response = models.TextField()
    sanitized_prompt = models.TextField(blank=True)  # After PII removal
    moderated_response = models.TextField(blank=True)  # After filtering

    # Metrics
    input_tokens = models.IntegerField()
    output_tokens = models.IntegerField()
    latency_ms = models.IntegerField()
    cost_usd = models.DecimalField(max_digits=10, decimal_places=4)

    # Safety flags
    flagged = models.BooleanField(default=False)
    flag_reason = models.CharField(max_length=200, blank=True)
    bias_signals = models.JSONField(default=list)
    toxicity_score = models.FloatField(null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['organization', 'created_at']),
            models.Index(fields=['flagged', 'created_at']),
            models.Index(fields=['feature', 'created_at']),
        ]


def log_ai_interaction(user, feature, prompt, response, model, metrics):
    """Log every AI interaction with safety checks."""

    # Run safety checks
    bias_signals = detect_bias(response)
    toxicity_score = check_toxicity(response)

    flagged = False
    flag_reason = ""

    if bias_signals:
        flagged = True
        flag_reason = f"Bias detected: {len(bias_signals)} signals"

    if toxicity_score > 0.7:
        flagged = True
        flag_reason += f"; High toxicity: {toxicity_score}"

    # Log interaction
    AIInteraction.objects.create(
        organization=user.organization,
        user=user,
        feature=feature,
        model=model,
        prompt=prompt,
        response=response,
        input_tokens=metrics['input_tokens'],
        output_tokens=metrics['output_tokens'],
        latency_ms=metrics['latency_ms'],
        cost_usd=metrics['cost'],
        flagged=flagged,
        flag_reason=flag_reason,
        bias_signals=bias_signals,
        toxicity_score=toxicity_score,
    )

    # Alert if flagged
    if flagged:
        send_admin_alert(f"AI interaction flagged: {flag_reason}")
```

---

## Compliance Checklist

### Data Privacy Act 2012 (Philippines)

- [ ] **Consent:** Users informed AI is processing their data
- [ ] **Purpose Limitation:** AI only used for stated purposes
- [ ] **Data Minimization:** Only necessary data sent to AI
- [ ] **Accuracy:** AI outputs validated before use
- [ ] **Storage Limitation:** AI interactions logged with retention policy
- [ ] **Security:** AI API keys encrypted, API calls over HTTPS
- [ ] **Accountability:** Audit trail for all AI decisions

### EU AI Act (if applicable)

**Risk Classification:** OBCMS AI features are likely **Limited Risk**

- [ ] **Transparency:** Users notified when interacting with AI
- [ ] **Human Oversight:** AI outputs reviewed by staff
- [ ] **Technical Documentation:** AI system architecture documented
- [ ] **Risk Management:** Bias testing and mitigation implemented
- [ ] **Data Governance:** Training data quality assured

---

## Responsible AI Best Practices

### 1. Transparency

**User-facing:**
```html
<!-- Notify users when AI is involved -->
<div class="ai-disclosure">
    ℹ️ This response was generated by AI based on OOBC documents.
    Please verify critical information.
</div>
```

**Developer-facing:**
```python
# Document AI decision-making
def generate_recommendation(community):
    """
    Generate intervention recommendation using AI.

    AI Model: Claude Sonnet 4
    Training Data: None (zero-shot)
    Context: Last 12 months MANA assessments
    Validation: Human review required before implementation
    """
    ...
```

### 2. Explainability

**Provide reasoning for AI outputs:**
```python
def explain_recommendation(recommendation, community):
    """Generate explanation for AI recommendation."""

    explanation = f"""
    ## Why This Recommendation?

    **Community Profile:**
    - Population: {community.population}
    - Primary needs: {community.top_needs}

    **Data Analyzed:**
    - {len(assessments)} community assessments
    - {len(similar_communities)} similar community outcomes

    **Reasoning:**
    1. Assessment data shows {evidence_1}
    2. Similar communities benefited from {similar_intervention}
    3. Budget aligns with {budget_justification}

    **Confidence:** {confidence_score}/10
    **Human review required:** Yes

    **Alternative considered:**
    - {alternative_1}: Not selected because {reason}
    """

    return explanation
```

### 3. Human-in-the-Loop

**Critical decisions require human approval:**
```python
class AIRecommendation(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    recommendation = models.TextField()
    confidence = models.FloatField()
    status = models.CharField(max_length=20, choices=[
        ('pending_review', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('modified', 'Modified'),
    ])
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reviewer_notes = models.TextField(blank=True)
```

### 4. Continuous Monitoring

**Dashboard for AI safety metrics:**
```python
def ai_safety_dashboard():
    """Generate safety metrics for AI systems."""
    last_30_days = timezone.now() - timedelta(days=30)

    metrics = {
        'total_interactions': AIInteraction.objects.filter(
            created_at__gte=last_30_days
        ).count(),

        'flagged_count': AIInteraction.objects.filter(
            created_at__gte=last_30_days,
            flagged=True
        ).count(),

        'avg_toxicity': AIInteraction.objects.filter(
            created_at__gte=last_30_days
        ).aggregate(avg=Avg('toxicity_score'))['avg'],

        'bias_incidents': AIInteraction.objects.filter(
            created_at__gte=last_30_days
        ).exclude(bias_signals=[]).count(),

        'cost_total': AIInteraction.objects.filter(
            created_at__gte=last_30_days
        ).aggregate(total=Sum('cost_usd'))['total'],
    }

    metrics['flag_rate'] = (metrics['flagged_count'] / metrics['total_interactions']
                           if metrics['total_interactions'] > 0 else 0)

    return metrics
```

---

## Emergency Response Plan

**If AI produces harmful output:**

1. **Immediate:**
   - Block output from reaching users
   - Log incident with full details
   - Alert AI system administrator

2. **Short-term (24 hours):**
   - Investigate root cause
   - Identify affected users
   - Communicate to stakeholders
   - Implement hotfix if needed

3. **Long-term (1 week):**
   - Review and update safety guardrails
   - Retrain or adjust prompts
   - Update testing procedures
   - Document lessons learned

**Incident Response Template:**
```python
class AIIncident(models.Model):
    incident_id = models.CharField(max_length=50, unique=True)
    severity = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ])
    description = models.TextField()
    affected_users = models.IntegerField()
    root_cause = models.TextField()
    mitigation_steps = models.TextField()
    resolved_at = models.DateTimeField(null=True)
    lessons_learned = models.TextField(blank=True)
```

---

**Remember:** Responsible AI is an ongoing process, not a one-time implementation. Regular audits, user feedback, and continuous improvement are essential for maintaining trust and safety.


---

# Additional Responsible AI Patterns (from SKILL.md)

## Workflow 6: Responsible AI

**For ensuring AI safety, bias detection, and compliance.**

### Safety Guardrails

**1. Input Validation**
```python
def validate_ai_input(user_input, max_length=10000):
    """Validate and sanitize user input before LLM processing."""
    # Check length
    if len(user_input) > max_length:
        raise ValueError(f"Input exceeds maximum length of {max_length}")

    # Check for prompt injection patterns
    injection_patterns = [
        "ignore previous instructions",
        "disregard all",
        "you are now",
        "forget everything",
    ]
    for pattern in injection_patterns:
        if pattern.lower() in user_input.lower():
            raise SecurityError("Potential prompt injection detected")

    return user_input
```

**2. Output Moderation**
```python
def moderate_ai_output(response):
    """Check AI output for harmful content."""
    # Check for PII leakage
    if contains_pii(response):
        response = redact_pii(response)

    return response
```

**3. Audit Logging**
```python
class AIInteraction(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    feature = models.CharField(max_length=100)
    prompt = models.TextField()
    response = models.TextField()
    model = models.CharField(max_length=50)
    input_tokens = models.IntegerField()
    output_tokens = models.IntegerField()
    latency_ms = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

def log_ai_interaction(user, feature, prompt, response, model, metrics):
    """Log every AI interaction for audit and compliance."""
    AIInteraction.objects.create(
        organization=user.organization,
        user=user,
        feature=feature,
        prompt=prompt,
        response=response,
        model=model,
        **metrics
    )
```

**Output:** Production AI with safety guardrails, bias detection, audit trail

**See:** [references/responsible-ai.md](references/responsible-ai.md)

---
