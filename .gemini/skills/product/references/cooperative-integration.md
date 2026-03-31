# Cooperative Integration for Product Management

## Cooperative Triggers

Invoke `/cooperative` when you detect:
- Keywords: "cooperative", "coop", "RA 9520", "CDA", "CSEA"
- Topics: Member product needs, cooperative product development, patronage-linked products
- Entities: Cooperative members, officers, BOD, GA, committees

## Integration Pattern

```
Product Management + /cooperative Integration
|
+-- Detect cooperative context in user request
+-- Invoke /cooperative for domain knowledge
+-- Apply Product methodology with cooperative context
|   +-- Feature priorities consider member needs
|   +-- Roadmap includes democratic input
|   +-- Product decisions go through governance
+-- Reference /cooperative assets as needed
```

## Key /cooperative Assets

| Asset | Path | Use When |
|-------|------|----------|
| RA 9520 Full Text | `../cooperative/assets/ra-9520-philippine-cooperative-code-2008.md` | Verbatim legal citations |
| RA 9520 Guide | `../cooperative/references/ra-9520-guide.md` | Understanding product provisions |
| Templates Index | `../cooperative/assets/templates/index.md` | Product planning templates |
| Memorandum Circulars | `../cooperative/references/memorandum-circulars/index.md` | Regulatory guidelines |
