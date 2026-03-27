# Policy Recommendations Guidebook — Progress Tracker

## Status: COMPLETE

All files created on 2026-03-26.

## Files Created

| File | Description | Status | Word Count (approx) |
|------|-------------|--------|---------------------|
| `00-table-of-contents.md` | Full TOC with &emsp; indentation | Done | — |
| `00b-about.md` | About this guidebook | Done | ~300 |
| `00c-author.md` | Author bio (verbatim from Bill Drafting Manual) | Done | ~250 |
| `01-introduction.md` | How to use, audience, principles | Done | ~1,800 |
| `02-chapter-01.md` | The Policy Cycle in BARMM | Done | ~2,800 |
| `03-chapter-02.md` | Understanding the Policy Environment | Done | ~2,600 |
| `04-chapter-03.md` | Evidence-Based Policy Analysis | Done | ~3,000 |
| `05-chapter-04.md` | Structuring a Policy Recommendation (Bardach + Template) | Done | ~3,200 |
| `06-chapter-05.md` | Legal Foundations and Compliance | Done | ~2,800 |
| `07-chapter-06.md` | Budgetary and Financial Analysis | Done | ~2,900 |
| `08-chapter-07.md` | Stakeholder Consultation and Validation | Done | ~3,000 |
| `09-chapter-08.md` | Quality Review and Approval | Done | ~3,100 |
| `10-chapter-09.md` | From Recommendation to Action | Done | ~3,000 |
| `11-glossary.md` | Glossary of Policy Terms (35+ terms) | Done | ~1,500 |
| `generate-pdf.py` | PDF generation script (WeasyPrint + Playwright fallback) | Done | — |
| `generate-docx.py` | DOCX generation script (python-docx) | Done | — |
| `guidebook-template.html` | HTML/CSS template for PDF rendering | Done | — |
| `PROGRESS.md` | This file | Done | — |

## Guidebook Structure

- **9 chapters** covering the full policy recommendation lifecycle
- **Introduction** with audience guide and three core principles
- **Glossary** with 35+ policy terms defined
- **Checklists**: Legal Compliance Checklist (Ch5), Quality Review Checklist (Ch8), Self-Review Checklist (Ch8)
- **Templates**: Budget tables (Ch6), Monitoring framework (Ch9), Evidence registry (Ch3)
- **Flowcharts**: Policy Cycle (Ch1), Recommendation Lifecycle (Ch9)

## Key Methodological Features

- **Bardach's Eightfold Path** as the core analytical framework (Chapter 4)
- **Four-Section Template**: Context & Rationale, Policy Framework, Implementation Structure, Management Framework
- **OOBC Policy Recommendations** referenced as practical example throughout
- **BOL compliance** integrated at every stage — not a separate afterthought
- **Budget analysis** required for every recommendation — costing, funding sources, fiscal feasibility

## Voice Rules Applied

- Direct second-person throughout
- Imperative mood for instructions
- WHY-first openings for sections
- Bold key terms for scannability
- 80%+ active voice
- No prohibited phrases used

## Generation

To generate PDF:
```bash
cd docs/policy-recommendations-guidebook/
pip3 install markdown weasyprint
python3 generate-pdf.py
```

To generate DOCX:
```bash
cd docs/policy-recommendations-guidebook/
pip3 install python-docx markdown
python3 generate-docx.py
```
