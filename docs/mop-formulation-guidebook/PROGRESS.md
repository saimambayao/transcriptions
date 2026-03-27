# MOP Formulation Guidebook — Progress Tracker

## Status: COMPLETE (v1.0)

## Files Created

| File | Description | Status | Words (approx) |
|------|-------------|--------|----------------|
| 00-table-of-contents.md | Full TOC with &emsp; indentation | Done | - |
| 00b-about.md | About This Guidebook | Done | 200 |
| 00c-author.md | Author bio (verbatim from bill-drafting-manual) | Done | 250 |
| 01-introduction.md | Chapter 1: Why MOPs Matter | Done | 2,400 |
| 02-chapter-02.md | Chapter 2: Planning and Preparation | Done | 2,600 |
| 03-chapter-03.md | Chapter 3: Information Gathering | Done | 3,000 |
| 04-chapter-04.md | Chapter 4: Drafting the Manual | Done | 2,800 |
| 05-chapter-05.md | Chapter 5: The PRLS MOP Model (KEY CHAPTER) | Done | 3,500 |
| 06-chapter-06.md | Chapter 6: Grounding MOPs in Legal Mandates | Done | 2,500 |
| 07-chapter-07.md | Chapter 7: Quality Standards and Performance Metrics | Done | 2,800 |
| 08-chapter-08.md | Chapter 8: Review, Approval, and Implementation | Done | 2,700 |
| 09-chapter-09.md | Chapter 9: Monitoring, Evaluation, and Continuous Improvement | Done | 2,600 |
| 10-chapter-10.md | Chapter 10: Adapting MOPs by Entity Size | Done | 2,500 |
| 11-glossary.md | Glossary of MOP and Governance Terms (40+ terms) | Done | 1,500 |
| generate-pdf.py | PDF generation script (WeasyPrint + Playwright fallback) | Done | - |
| generate-docx.py | DOCX generation script (python-docx) | Done | - |
| guidebook-template.html | HTML template with CSS for PDF rendering | Done | - |
| PROGRESS.md | This file | Done | - |

## Key Design Decisions

1. **PRLS MOP Model as gold standard (Ch. 5)**: Output-based organization, four-column workflow tables, six-stage hierarchical approval flow (Reception > Evaluation/Delegation > Execution > Review > Approval > Delivery), standardized forms (Referral and Action Slip, Transmittal Memorandum, Routing Slip, Tracking Log)

2. **Complete sample procedure**: Chapter 5 includes a full 15-step procedure for "Producing a Legislative Analysis Briefer" demonstrating the PRLS format from Reception through Delivery

3. **Legal grounding**: Chapter 6 traces every MOP procedure to BAA 13 (Bangsamoro Administrative Code) and cross-references enabling BAAs (8, 9, 10, 17, 18, 35, 82, 84)

4. **Quality improvement over existing PRLS MOPs**: Chapter 7 adds explicit quality criteria per output type, turnaround time standards, KPIs, and performance monitoring systems -- features missing from existing PRLS MOPs

5. **Three-tier scaling**: Chapter 10 provides Provincial MOP (80-150 pages, 9 chapters), Division MOP (40-80 pages, 5-6 chapters), and Office MOP (20-40 pages, 3-4 chapters)

## BAAs Referenced

| BAA | Subject | Chapters Referenced |
|-----|---------|-------------------|
| BAA 8 | Bangsamoro Women Commission | Ch. 1, 5, 6 |
| BAA 9 | Bangsamoro Human Rights Commission | Ch. 1, 6 |
| BAA 10 | Bangsamoro Youth Commission | Ch. 1, 5, 6 |
| BAA 13 | Bangsamoro Administrative Code | Ch. 1, 3, 4, 5, 6, 7 |
| BAA 17 | Bangsamoro Civil Service Code | Ch. 1, 4, 6 |
| BAA 18 | Bangsamoro Education Code | Ch. 1, 5, 6, 10 |
| BAA 35 | Bangsamoro Electoral Code | Ch. 1, 6 |
| BAA 82 | Bangsamoro Labor Code | Ch. 1, 6 |
| BAA 84 | Budget System Act | Ch. 1, 2, 4, 6 |

## Generation

```bash
# PDF (requires: pip3 install markdown weasyprint)
python3 generate-pdf.py

# DOCX (requires: pip3 install python-docx markdown)
python3 generate-docx.py
```
