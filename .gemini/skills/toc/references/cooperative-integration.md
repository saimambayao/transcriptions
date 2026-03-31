# Cooperative Integration for Theory of Change

## Cooperative Triggers

Invoke `/cooperative` when you detect:
- Keywords: "cooperative", "coop", "RA 9520", "CDA", "CSEA"
- Topics: Cooperative impact measurement, member benefit assessment, community development tracking
- Entities: Cooperative members, officers, BOD, GA, committees, statutory funds

## Integration Pattern

```
ToC + /cooperative Integration
|
+-- Detect cooperative context in user request
+-- Invoke /cooperative for domain knowledge
|   +-- RA 9520 provisions on cooperative purpose and impact
|   +-- CDA memorandum circulars on reporting
|   +-- BARMM/CSEA requirements
+-- Apply ToC methodology with cooperative context
|   +-- Impact pathways consider member AND community benefit
|   +-- Indicators include patronage and democratic participation
|   +-- Assumptions test cooperative principles alignment
+-- Reference /cooperative assets as needed
```

## Key /cooperative Assets

| Asset | Path | Use When |
|-------|------|----------|
| RA 9520 Full Text | `../cooperative/assets/ra-9520-philippine-cooperative-code-2008.md` | Verbatim legal citations |
| RA 9520 Guide | `../cooperative/references/ra-9520-guide.md` | Understanding impact provisions |
| Templates Index | `../cooperative/assets/templates/index.md` | M&E document templates |
| Memorandum Circulars | `../cooperative/references/memorandum-circulars/index.md` | Regulatory guidelines |
