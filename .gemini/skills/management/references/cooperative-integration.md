# Cooperative Integration for Management

## Cooperative Triggers

Invoke `/cooperative` when you detect:
- Keywords: "cooperative", "coop", "RA 9520", "CDA", "CSEA"
- Topics: Cooperative management, democratic management, committee management
- Entities: Cooperative members, officers, BOD, GA, committees, statutory funds

## Integration Pattern

```
Management + /cooperative Integration
|
+-- Detect cooperative context in user request
+-- Invoke /cooperative for domain knowledge
|   +-- RA 9520 provisions on management structure
|   +-- CDA memorandum circulars on management standards
|   +-- BARMM/CSEA requirements
+-- Apply Management methodology with cooperative context
+-- Reference /cooperative assets as needed
```

## Key /cooperative Assets

| Asset | Path | Use When |
|-------|------|----------|
| RA 9520 Full Text | `../cooperative/assets/ra-9520-philippine-cooperative-code-2008.md` | Verbatim legal citations |
| RA 9520 Guide | `../cooperative/references/ra-9520-guide.md` | Understanding management provisions |
| Templates Index | `../cooperative/assets/templates/index.md` | Management document templates |
| Memorandum Circulars | `../cooperative/references/memorandum-circulars/index.md` | Regulatory guidelines |
