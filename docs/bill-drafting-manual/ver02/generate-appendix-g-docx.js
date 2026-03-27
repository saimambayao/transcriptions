/**
 * Generate Appendix G — Budget Briefer Template
 * Bill Drafting Guidebook for the Bangsamoro Parliament
 *
 * Usage: NODE_PATH=$(npm root -g) node generate-appendix-g-docx.js
 */

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, HeadingLevel, BorderStyle,
  WidthType, ShadingType, VerticalAlign, PageNumber, PageBreak, TabStopType, TabStopPosition
} = require('docx');

// ─── Design Tokens ───
const NAVY = '1B365D';
const GOLD = 'C5A54E';
const CHARCOAL = '2D2D2D';
const WHITE = 'FFFFFF';
const LIGHT_GRAY = 'F5F7F9';
const MID_GRAY = 'D0D0D0';
const FONT = 'Calibri';

const MM_TO_DXA = 56.7;
const PAGE_WIDTH_A4 = 11906;
const MARGIN_LEFT = Math.round(25 * MM_TO_DXA);
const MARGIN_RIGHT = Math.round(25 * MM_TO_DXA);
const MARGIN_TOP = Math.round(20 * MM_TO_DXA);
const MARGIN_BOTTOM = Math.round(25 * MM_TO_DXA);
const USABLE_WIDTH = PAGE_WIDTH_A4 - MARGIN_LEFT - MARGIN_RIGHT;

const COL_35 = Math.round(USABLE_WIDTH * 0.35);
const COL_65 = Math.round(USABLE_WIDTH * 0.65);

// ─── Reusable Helpers ───
const thinBorder = { style: BorderStyle.SINGLE, size: 1, color: MID_GRAY };
const cellBorders = { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder };

function headerCell(text, width) {
  return new TableCell({
    borders: cellBorders,
    width: { size: width, type: WidthType.DXA },
    shading: { fill: NAVY, type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({
      alignment: AlignmentType.LEFT,
      spacing: { before: 60, after: 60 },
      children: [new TextRun({ text, bold: true, color: WHITE, font: FONT, size: 20 })]
    })]
  });
}

function labelCell(text, width, opts = {}) {
  return new TableCell({
    borders: cellBorders,
    width: { size: width, type: WidthType.DXA },
    shading: { fill: opts.shading || WHITE, type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({
      spacing: { before: 40, after: 40 },
      children: [new TextRun({ text, bold: true, color: CHARCOAL, font: FONT, size: 22 })]
    })]
  });
}

function valueCell(text, width, opts = {}) {
  return new TableCell({
    borders: cellBorders,
    width: { size: width, type: WidthType.DXA },
    shading: { fill: opts.shading || WHITE, type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.CENTER,
    columnSpan: opts.columnSpan,
    children: [new Paragraph({
      spacing: { before: 40, after: 40 },
      children: [new TextRun({ text: text || '', color: CHARCOAL, font: FONT, size: 22 })]
    })]
  });
}

function emptyValueCell(width, opts = {}) {
  return new TableCell({
    borders: cellBorders,
    width: { size: width, type: WidthType.DXA },
    shading: { fill: opts.shading || WHITE, type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.TOP,
    columnSpan: opts.columnSpan,
    children: [new Paragraph({
      spacing: { before: 80, after: 80 },
      children: [new TextRun({ text: '', font: FONT, size: 22 })]
    })]
  });
}

function checkboxCell(text, width, opts = {}) {
  return new TableCell({
    borders: cellBorders,
    width: { size: width, type: WidthType.DXA },
    shading: { fill: opts.shading || WHITE, type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.CENTER,
    columnSpan: opts.columnSpan,
    children: [new Paragraph({
      spacing: { before: 40, after: 40 },
      children: [new TextRun({ text, color: CHARCOAL, font: FONT, size: 22 })]
    })]
  });
}

function sectionHeading(text) {
  return new Paragraph({
    spacing: { before: 360, after: 80 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: GOLD } },
    children: [new TextRun({ text, bold: true, color: NAVY, font: FONT, size: 28 })]
  });
}

function chapterRef(text) {
  return new Paragraph({
    spacing: { before: 40, after: 120 },
    children: [new TextRun({ text, italics: true, color: '888888', font: FONT, size: 18 })]
  });
}

function guidanceText(text) {
  return new Paragraph({
    spacing: { before: 40, after: 120 },
    children: [new TextRun({ text, italics: true, color: '666666', font: FONT, size: 20 })]
  });
}

function dottedLines(count) {
  const lines = [];
  for (let i = 0; i < count; i++) {
    lines.push(new Paragraph({
      spacing: { before: 200, after: 0 },
      border: { bottom: { style: BorderStyle.DOTTED, size: 1, color: MID_GRAY } },
      children: [new TextRun({ text: '', font: FONT, size: 22 })]
    }));
  }
  return lines;
}

function spacer(pts = 120) {
  return new Paragraph({ spacing: { before: pts, after: 0 }, children: [] });
}

function kvRow(label, value, rowIndex) {
  const shading = rowIndex % 2 === 1 ? LIGHT_GRAY : WHITE;
  return new TableRow({
    children: [
      labelCell(label, COL_35, { shading }),
      value !== null ? checkboxCell(value, COL_65, { shading }) : emptyValueCell(COL_65, { shading })
    ]
  });
}

function kvTable(rows) {
  return new Table({
    columnWidths: [COL_35, COL_65],
    rows: rows.map((r, i) => kvRow(r[0], r[1], i))
  });
}

function dataTable(headers, widths, dataRows) {
  const hRow = new TableRow({
    tableHeader: true,
    children: headers.map((h, i) => headerCell(h, widths[i]))
  });
  const rows = [hRow];
  dataRows.forEach((dr, ri) => {
    const shading = ri % 2 === 1 ? LIGHT_GRAY : WHITE;
    rows.push(new TableRow({
      children: dr.map((cellText, ci) => {
        if (cellText === null) return emptyValueCell(widths[ci], { shading });
        return checkboxCell(cellText, widths[ci], { shading });
      })
    }));
  });
  return new Table({ columnWidths: widths, rows });
}

function subHeading(text) {
  return new Paragraph({
    spacing: { before: 180, after: 80 },
    children: [new TextRun({ text, bold: true, color: NAVY, font: FONT, size: 22 })]
  });
}

// ─── Build Content ───
function buildContent() {
  const children = [];

  // Title Block
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 600, after: 120 },
    children: [new TextRun({ text: 'BUDGET BRIEFER', bold: true, color: NAVY, font: FONT, size: 36, smallCaps: true })]
  }));
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 60 },
    children: [new TextRun({ text: 'Bangsamoro Transition Authority Parliament', color: CHARCOAL, font: FONT, size: 24 })]
  }));
  children.push(new Paragraph({
    spacing: { before: 60, after: 200 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: GOLD } },
    children: []
  }));

  // ─── Control Information ───
  children.push(sectionHeading('Control Information'));
  children.push(kvTable([
    ['Control No.:', 'BB-________-________'],
    ['Date Prepared:', ''],
    ['Prepared by:', ''],
    ['Designation:', ''],
    ['Office of MP:', ''],
    ['Version:', '\u2610 Initial    \u2610 Updated (Version ____)'],
    ['For:', '\u2610 Committee on Finance Hearing    \u2610 Plenary Deliberation'],
  ]));

  // ─── Section 1 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 1 — Ministry / Agency / Office'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.3.1)'));

  children.push(kvTable([
    ['Full Name:', ''],
    ['Abbreviation:', ''],
    ['Type:', '\u2610 Ministry    \u2610 Office under OCM    \u2610 Parliamentary Office    \u2610 GOCC    \u2610 Constitutional Body    \u2610 Other: ________'],
    ['Head of Agency:', ''],
    ['Date of Appointment:', ''],
    ['BEP Code:', ''],
    ['BEP Page Number:', ''],
    ['No. of Divisions/Bureaus:', ''],
    ['No. of Field Offices:', ''],
    ['Provinces Covered:', ''],
    ['Total Authorized Positions:', ''],
    ['Total Filled Positions:', ''],
    ['Fill Rate:', '________%'],
  ]));

  children.push(spacer(120));
  children.push(subHeading('Organizational Notes:'));
  children.push(...dottedLines(3));

  // ─── Section 2 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 2 — Mandate and Legal Basis'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.3.2)'));

  children.push(kvTable([
    ['Primary Legal Basis:', ''],
    ['Creating Law / Issuance:', ''],
  ]));

  children.push(spacer(120));
  children.push(subHeading('Core Functions (2-3 sentences):'));
  children.push(...dottedLines(4));

  children.push(spacer(120));
  children.push(kvTable([
    ['Has the mandate changed since the last budget cycle?', '\u2610 Yes    \u2610 No'],
    ['If yes, describe the change and its fiscal impact:', ''],
  ]));
  children.push(...dottedLines(3));

  // ─── Section 3 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 3 — Overall Development Goals'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.3.3)'));
  children.push(guidanceText('Check all BDP 2023-2028 goals the agency primarily serves:'));

  const bdpW0 = Math.round(USABLE_WIDTH * 0.08);
  const bdpW1 = Math.round(USABLE_WIDTH * 0.52);
  const bdpW2 = Math.round(USABLE_WIDTH * 0.40);
  children.push(dataTable(
    ['', 'Goal', 'Primary?'],
    [bdpW0, bdpW1, bdpW2],
    [
      ['\u2610', 'Goal 1 — Stable, just, and accountable government', '\u2610 Primary    \u2610 Secondary'],
      ['\u2610', 'Goal 2 — Equitable, competitive, and robust economy', '\u2610 Primary    \u2610 Secondary'],
      ['\u2610', 'Goal 3 — Peaceful, safe, and resilient Bangsamoro communities', '\u2610 Primary    \u2610 Secondary'],
      ['\u2610', 'Goal 4 — Inclusive, responsive, and quality social services', '\u2610 Primary    \u2610 Secondary'],
      ['\u2610', 'Goal 5 — Rich and diverse Bangsamoro culture and identity preserved and recognized', '\u2610 Primary    \u2610 Secondary'],
      ['\u2610', 'Goal 6 — Strategic, adequate, and climate-resilient infrastructure', '\u2610 Primary    \u2610 Secondary'],
    ]
  ));

  children.push(spacer(120));
  children.push(subHeading('Alignment Assessment:'));
  children.push(guidanceText('(Compare what the agency claims to prioritize (goals checked above) against where its money actually goes (Section 5). If an agency checks "Goal 4 — Social Services" but allocates 80% to administrative MOOE, that is an alignment gap. Note any such gaps below.)'));
  children.push(...dottedLines(4));

  // ─── Section 4 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 4 — Organizational Outcomes and Key Performance Indicators'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.4)'));

  const kpiW1 = Math.round(USABLE_WIDTH * 0.25);
  const kpiW2 = Math.round(USABLE_WIDTH * 0.15);
  const kpiW3 = Math.round(USABLE_WIDTH * 0.15);
  const kpiW4 = Math.round(USABLE_WIDTH * 0.25);
  const kpiW5 = Math.round(USABLE_WIDTH * 0.20);
  children.push(dataTable(
    ['KPI', 'Target', 'Baseline', 'Met?', 'BDP Goal'],
    [kpiW1, kpiW2, kpiW3, kpiW4, kpiW5],
    Array(6).fill(null).map(() => [null, null, null, '\u2610 Yes  \u2610 No  \u2610 Partial', null])
  ));

  children.push(spacer(120));
  children.push(subHeading('For KPIs that fell short of target — root cause analysis:'));
  children.push(guidanceText('(For each KPI marked "No" or "Partial" above, write 2-3 sentences: what was the target, what was actually achieved, and why the gap exists. Sources: agency annual reports, BEP narratives, COA findings.)'));
  children.push(...dottedLines(4));

  children.push(spacer(120));
  children.push(subHeading('Service Quality and Satisfaction:'));
  children.push(guidanceText('(Check whether the agency tracks these. If the agency does not have an SQI or CSI, mark "No" and note "N/A." This is itself a finding worth raising during the hearing.)'));

  const sqW1 = Math.round(USABLE_WIDTH * 0.40);
  const sqW2 = Math.round(USABLE_WIDTH * 0.25);
  const sqW3 = Math.round(USABLE_WIDTH * 0.35);
  children.push(dataTable(
    ['Dimension', 'Agency Tracks?', 'Assessment'],
    [sqW1, sqW2, sqW3],
    [
      ['Service Quality Index (SQI)', '\u2610 Yes  \u2610 No  \u2610 N/A', null],
      ['  — Accessibility (ease of reaching/using services)', null, null],
      ['  — Reliability (consistent, accurate delivery)', null, null],
      ['  — Timeliness (speed, punctuality of delivery)', null, null],
      ['  — Responsiveness (willingness to assist promptly)', null, null],
      ['  — Assurance (trust, competence, security)', null, null],
      ['  — Sustainability (environmental and social responsibility)', null, null],
      ['Customer Satisfaction Index (CSI)', '\u2610 Yes  \u2610 No  \u2610 N/A', null],
      ['  — Survey or feedback system in place?', null, null],
      ['  — Most recent score or result:', null, null],
    ]
  ));

  // ─── Section 5 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 5 — Budget Comparison'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.5)'));

  // 5a
  children.push(subHeading('5a. Three-Year Budget Comparison'));
  const b5w = Math.round(USABLE_WIDTH / 5);
  children.push(dataTable(
    ['Category', 'FY (Year-2)', 'FY (Year-1)', 'FY (Current)', 'Variance'],
    [b5w, b5w, b5w, b5w, b5w],
    [
      ['PS', null, null, null, null],
      ['MOOE', null, null, null, null],
      ['CO', null, null, null, null],
      ['Total', null, null, null, null],
      ['GAD', null, null, null, null],
    ]
  ));

  children.push(spacer(80));
  children.push(new Paragraph({
    spacing: { before: 40, after: 40 },
    children: [
      new TextRun({ text: '3-Year Trend: ', bold: true, color: CHARCOAL, font: FONT, size: 22 }),
      new TextRun({ text: '\u2610 Increasing    \u2610 Stable    \u2610 Decreasing', color: CHARCOAL, font: FONT, size: 22 }),
    ]
  }));
  children.push(new Paragraph({
    spacing: { before: 40, after: 80 },
    children: [
      new TextRun({ text: 'GAD meets 5% minimum? ', bold: true, color: CHARCOAL, font: FONT, size: 22 }),
      new TextRun({ text: '\u2610 Yes    \u2610 No', color: CHARCOAL, font: FONT, size: 22 }),
    ]
  }));

  // 5b
  children.push(subHeading('5b. Absorption Capacity (Previous FY)'));
  const b5bw = Math.round(USABLE_WIDTH / 4);
  children.push(dataTable(
    ['Category', 'Allocation', 'Actual Expenditure', 'Absorption Rate'],
    [b5bw, b5bw, b5bw, b5bw],
    [
      ['PS', null, null, null],
      ['MOOE', null, null, null],
      ['CO', null, null, null],
      ['Total', null, null, null],
    ]
  ));

  // 5c
  children.push(subHeading('5c. Personnel Services Detail'));
  children.push(dataTable(
    ['Item', 'Details'],
    [COL_35, COL_65],
    [
      ['New positions requested', '________ positions'],
      ['Position titles and salary grades', null],
      ['Administrative-to-program delivery ratio', '________:________'],
      ['Positions vacant > 12 months', null],
      ['Overtime/allowance as % of base salaries', '________%'],
    ]
  ));

  // 5d
  children.push(subHeading('5d. MOOE Detail'));
  children.push(dataTable(
    ['Item', 'Details'],
    [COL_35, COL_65],
    [
      ['Program delivery MOOE vs. administrative MOOE', '________% : ________%'],
      ['Travel budget as % of total MOOE', '________%'],
      ['Training/capacity-building budget', null],
      ['Consultant fees', null],
    ]
  ));

  // 5e
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(subHeading('5e. Capital Outlay Detail'));
  const coW1 = Math.round(USABLE_WIDTH * 0.25);
  const coW2 = Math.round(USABLE_WIDTH * 0.18);
  const coW3 = Math.round(USABLE_WIDTH * 0.20);
  const coW4 = Math.round(USABLE_WIDTH * 0.18);
  const coW5 = Math.round(USABLE_WIDTH * 0.19);
  children.push(dataTable(
    ['Project', 'Prev FY Alloc', 'Status', 'Current FY', 'Total Cost'],
    [coW1, coW2, coW3, coW4, coW5],
    [
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
    ]
  ));

  children.push(spacer(80));
  children.push(new Paragraph({
    spacing: { before: 40, after: 80 },
    children: [
      new TextRun({ text: 'CO Utilization Rate (3-Year): ', bold: true, color: CHARCOAL, font: FONT, size: 22 }),
      new TextRun({ text: 'FY ____: ____%    FY ____: ____%    FY ____: ____%', color: CHARCOAL, font: FONT, size: 22 }),
    ]
  }));

  // 5f
  children.push(subHeading('5f. Line-Item Variance Analysis'));
  const lvW1 = Math.round(USABLE_WIDTH * 0.16);
  const lvW2 = Math.round(USABLE_WIDTH * 0.14);
  const lvW3 = Math.round(USABLE_WIDTH * 0.14);
  const lvW4 = Math.round(USABLE_WIDTH * 0.16);
  const lvW5 = Math.round(USABLE_WIDTH * 0.14);
  const lvW6 = Math.round(USABLE_WIDTH * 0.10);
  const lvW7 = Math.round(USABLE_WIDTH * 0.16);
  children.push(dataTable(
    ['Line Item', 'FY (Y-2) Actual', 'FY (Y-1) Actual', 'FY (Curr) Proposed', 'Variance', 'F/U?', 'Explanation'],
    [lvW1, lvW2, lvW3, lvW4, lvW5, lvW6, lvW7],
    Array(5).fill(null).map(() => [null, null, null, null, null, '\u2610 F  \u2610 U', null])
  ));

  children.push(spacer(60));
  children.push(guidanceText('(For any line item that changed by more than 20% from the previous year, explain the variance. F = Favorable, U = Unfavorable.)'));

  children.push(spacer(120));
  children.push(subHeading('Mid-Year Adjustments or Reallocations (Previous FY):'));
  children.push(...dottedLines(3));

  children.push(spacer(120));
  children.push(subHeading('Internal Controls Assessment:'));
  children.push(...dottedLines(3));

  // ─── Section 6 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 6 — Existing PPAS (Tier 1)'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.6)'));

  const ppW1 = Math.round(USABLE_WIDTH * 0.16);
  const ppW2 = Math.round(USABLE_WIDTH * 0.20);
  const ppW3 = Math.round(USABLE_WIDTH * 0.12);
  const ppW4 = Math.round(USABLE_WIDTH * 0.12);
  const ppW5 = Math.round(USABLE_WIDTH * 0.12);
  const ppW6 = Math.round(USABLE_WIDTH * 0.14);
  const ppW7 = Math.round(USABLE_WIDTH * 0.14);
  children.push(dataTable(
    ['PPAS', 'Type', 'FY Alloc', 'FY Actual', 'FY Request', 'Variance', 'Absorption'],
    [ppW1, ppW2, ppW3, ppW4, ppW5, ppW6, ppW7],
    Array(5).fill(null).map(() => [null, '\u2610 Core  \u2610 Support  \u2610 Admin  \u2610 Cross-cutting', null, null, null, null, null])
  ));

  children.push(spacer(80));
  children.push(new Paragraph({
    spacing: { before: 40, after: 80 },
    children: [
      new TextRun({ text: 'Budget Distribution: ', bold: true, color: CHARCOAL, font: FONT, size: 22 }),
      new TextRun({ text: 'Core Mandate ____%    Support ____%    Administrative ____%    Cross-cutting ____%', color: CHARCOAL, font: FONT, size: 22 }),
    ]
  }));

  children.push(subHeading('Performance Evaluation of Key Tier 1 Programs:'));
  const peW1 = Math.round(USABLE_WIDTH * 0.22);
  const peW2 = Math.round(USABLE_WIDTH * 0.15);
  const peW3 = Math.round(USABLE_WIDTH * 0.15);
  const peW4 = Math.round(USABLE_WIDTH * 0.22);
  const peW5 = Math.round(USABLE_WIDTH * 0.26);
  children.push(dataTable(
    ['Program', 'Target', 'Actual', 'Met?', 'Issues'],
    [peW1, peW2, peW3, peW4, peW5],
    [
      [null, null, null, '\u2610 Yes  \u2610 Partial  \u2610 No', null],
      [null, null, null, '\u2610 Yes  \u2610 Partial  \u2610 No', null],
      [null, null, null, '\u2610 Yes  \u2610 Partial  \u2610 No', null],
    ]
  ));

  children.push(spacer(120));
  children.push(subHeading('Outcome indicators for key programs:'));
  children.push(guidanceText('(1-2 sentences per program: what indicator was tracked, what was achieved, and whether the budget was the limiting factor.)'));
  children.push(...dottedLines(4));

  // ─── Section 7 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 7 — New and Expanded PPAS (Tier 2)'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.7)'));

  for (let p = 1; p <= 3; p++) {
    children.push(subHeading(`New/Expanded Program ${p}:`));
    children.push(dataTable(
      ['Field', 'Details'],
      [COL_35, COL_65],
      [
        ['PPAS Name:', null],
        ['Type:', '\u2610 New Initiative    \u2610 Expansion    \u2610 Pilot    \u2610 One-Time Project'],
        ['Priority:', '\u2610 High    \u2610 Medium    \u2610 Low'],
        ['Budget:', 'PS: ________    MOOE: ________    CO: ________'],
        ['Rationale:', null],
        ['Expected Outcomes:', null],
      ]
    ));
    children.push(spacer(80));
  }

  children.push(subHeading('Tier 2 Scrutiny:'));
  children.push(guidanceText('(For each new program, answer the questions below. "Evidence of need" = a written document. "Feasibility study" = a document addressing cost, timeline, staffing, and risks. If the agency cannot provide these, write "Not provided" — this is a red flag to raise during the hearing.)'));

  const scW1 = Math.round(USABLE_WIDTH * 0.34);
  const scW2 = Math.round(USABLE_WIDTH * 0.22);
  const scW3 = Math.round(USABLE_WIDTH * 0.22);
  const scW4 = Math.round(USABLE_WIDTH * 0.22);
  children.push(dataTable(
    ['Question', 'Program 1', 'Program 2', 'Program 3'],
    [scW1, scW2, scW3, scW4],
    [
      ['Evidence of need provided?', null, null, null],
      ['Legal or policy basis?', null, null, null],
      ['BEDC endorsement?', null, null, null],
      ['Feasibility study provided?', null, null, null],
      ['Specific first-year targets?', null, null, null],
      ['Exit strategy or evaluation trigger?', null, null, null],
      ['Total lifecycle cost (if multi-year)?', null, null, null],
      ['What happens if NOT funded?', null, null, null],
    ]
  ));

  children.push(spacer(80));
  children.push(new Paragraph({
    spacing: { before: 40, after: 80 },
    children: [
      new TextRun({ text: 'Tier 2 programs as % of total budget increase: ', bold: true, color: CHARCOAL, font: FONT, size: 22 }),
      new TextRun({ text: '________%', color: CHARCOAL, font: FONT, size: 22 }),
    ]
  }));

  // ─── Section 8 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 8 — Sector, Clientele, and Beneficiary Analysis'));
  children.push(chapterRef('(Source: BB09 of the CSW Budget Briefer framework)'));
  children.push(guidanceText('Identify the sectors and populations directly affected by the agency\'s programs. This section helps the MP understand who the budget actually serves.'));

  children.push(subHeading('Sectors Served:'));
  const ssW1 = Math.round(USABLE_WIDTH * 0.20);
  const ssW2 = Math.round(USABLE_WIDTH * 0.30);
  const ssW3 = Math.round(USABLE_WIDTH * 0.25);
  const ssW4 = Math.round(USABLE_WIDTH * 0.25);
  children.push(dataTable(
    ['Sector', 'PPAS Serving This Sector', 'Estimated Beneficiaries', 'Geographic Coverage'],
    [ssW1, ssW2, ssW3, ssW4],
    Array(4).fill(null).map(() => [null, null, null, null])
  ));

  children.push(spacer(120));
  children.push(subHeading('Priority Constituencies:'));
  const pcW1 = Math.round(USABLE_WIDTH * 0.25);
  const pcW2 = Math.round(USABLE_WIDTH * 0.40);
  const pcW3 = Math.round(USABLE_WIDTH * 0.35);
  children.push(dataTable(
    ['Group', 'How Served', 'Gaps Identified'],
    [pcW1, pcW2, pcW3],
    [
      ['Women', null, null],
      ['Youth', null, null],
      ['Children', null, null],
      ['Indigenous Peoples', null, null],
      ['Persons with Disabilities', null, null],
      ['Internally Displaced Persons', null, null],
      ['Other: ________________________', null, null],
    ]
  ));

  children.push(spacer(120));
  children.push(subHeading('Equity and Inclusion Assessment:'));
  const eiW1 = Math.round(USABLE_WIDTH * 0.55);
  const eiW2 = Math.round(USABLE_WIDTH * 0.45);
  children.push(dataTable(
    ['Question', 'Assessment'],
    [eiW1, eiW2],
    [
      ["Does the agency's budget equitably serve diverse groups?", null],
      ['Are there populations the agency should serve but does not?', null],
      ['How does the agency collect beneficiary data?', null],
      ['Are there feedback mechanisms for beneficiaries?', '\u2610 Yes    \u2610 No'],
      ['If yes, describe:', null],
    ]
  ));

  children.push(spacer(120));
  children.push(subHeading('Service Delivery Models:'));
  children.push(guidanceText('(In 3-5 sentences: How does the agency deliver services — directly, through LGUs, through NGOs, or through fund transfers? Is the model reaching beneficiaries effectively? What are the bottlenecks?)'));
  children.push(...dottedLines(5));

  // ─── Section 9 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 9 — Laws Mandated for Agency Implementation'));
  children.push(chapterRef('(Source: BB10 of the CSW Budget Briefer framework)'));
  children.push(guidanceText('List all laws, regulations, and issuances the agency is mandated to implement — not just the creating law, but every law that assigns duties to this agency.'));

  const lawW1 = Math.round(USABLE_WIDTH * 0.18);
  const lawW2 = Math.round(USABLE_WIDTH * 0.20);
  const lawW3 = Math.round(USABLE_WIDTH * 0.17);
  const lawW4 = Math.round(USABLE_WIDTH * 0.22);
  const lawW5 = Math.round(USABLE_WIDTH * 0.23);
  children.push(dataTable(
    ['Law / Issuance', 'Key Provisions', "Agency's Role", 'Implementation Status', 'Challenges'],
    [lawW1, lawW2, lawW3, lawW4, lawW5],
    Array(5).fill(null).map(() => [null, null, null, '\u2610 Full  \u2610 Partial  \u2610 Not Started', null])
  ));

  children.push(spacer(120));
  children.push(subHeading('Inter-Agency Coordination Requirements:'));
  const iaW1 = Math.round(USABLE_WIDTH * 0.25);
  const iaW2 = Math.round(USABLE_WIDTH * 0.40);
  const iaW3 = Math.round(USABLE_WIDTH * 0.35);
  children.push(dataTable(
    ['Partner Agency', 'Nature of Coordination', 'Budgetary Implications'],
    [iaW1, iaW2, iaW3],
    [[null, null, null], [null, null, null]]
  ));

  children.push(spacer(120));
  children.push(subHeading('Legal Gaps or Overlaps Identified:'));
  children.push(guidanceText('(List any laws that overlap with other agencies\' mandates, or areas where no law covers a function the agency performs.)'));
  children.push(...dottedLines(3));

  children.push(spacer(120));
  children.push(subHeading("Shari'ah and Islamic Governance Considerations:"));
  children.push(dataTable(
    ['Question', 'Assessment'],
    [eiW1, eiW2],
    [
      ["Does the agency operate in areas governed by Shari'ah (family, personal status, Islamic finance)?", '\u2610 Yes    \u2610 No'],
      ['If yes, are Shari\'ah-related functions funded in the budget?', '\u2610 Yes    \u2610 No    \u2610 N/A'],
      ['Does the budget include allocations for Shari\'ah courts, halal certification, or Islamic affairs?', '\u2610 Yes    \u2610 No    \u2610 N/A'],
    ]
  ));

  children.push(spacer(120));
  children.push(subHeading('Pending Legislation Affecting This Agency:'));
  children.push(...dottedLines(3));

  // ─── Section 10 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 10 — GAD Budget Review'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.5.5)'));

  children.push(dataTable(
    ['Item', 'Assessment'],
    [COL_35, COL_65],
    [
      ['GAD allocation included?', '\u2610 Yes    \u2610 No'],
      ['GAD as % of total budget', '________%'],
      ['Meets 5% minimum?', '\u2610 Yes    \u2610 No'],
      ['Genuine gender-responsive programs or relabeled existing activities?', null],
      ['GAD targets included in agency KPIs?', '\u2610 Yes    \u2610 No'],
      ['Gender analysis of core programs conducted?', '\u2610 Yes    \u2610 No'],
      ['Previous FY GAD outcomes', null],
    ]
  ));
  children.push(...dottedLines(3));

  // ─── Section 11 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 11 — Analysis of Special Provisions'));
  children.push(chapterRef('(Source: BB14 of the CSW Budget Briefer framework)'));
  children.push(guidanceText('Special provisions in the budget proposal may include earmarks, conditional releases, or programmatic riders. These require separate scrutiny.'));

  children.push(subHeading('Special Provisions in the Current FY Budget Proposal:'));
  const spW1 = Math.round(USABLE_WIDTH * 0.18);
  const spW2 = Math.round(USABLE_WIDTH * 0.25);
  const spW3 = Math.round(USABLE_WIDTH * 0.20);
  const spW4 = Math.round(USABLE_WIDTH * 0.14);
  const spW5 = Math.round(USABLE_WIDTH * 0.23);
  children.push(dataTable(
    ['Provision', 'Summary', 'Legal Basis', 'In Prev FY?', 'Fiscal Impact'],
    [spW1, spW2, spW3, spW4, spW5],
    Array(4).fill(null).map(() => [null, null, null, '\u2610 Yes  \u2610 No', null])
  ));

  children.push(spacer(120));
  children.push(subHeading('Changes from Previous FY:'));
  children.push(guidanceText('(List provisions added, removed, or modified.)'));
  children.push(...dottedLines(3));

  children.push(spacer(120));
  children.push(subHeading('Assessment:'));
  children.push(dataTable(
    ['Question', 'Assessment'],
    [eiW1, eiW2],
    [
      ['Do the special provisions have clear legal basis?', null],
      ['Do any provisions require inter-agency coordination?', null],
      ['Are there new provisions not in the previous FY? Justify:', null],
      ['Are there previous FY provisions that were removed? Why:', null],
      ['Do any provisions require legislative action for clarification?', null],
      ['What are the broader social and economic impacts?', null],
    ]
  ));

  children.push(spacer(120));
  children.push(subHeading('Transparency and Accountability Measures:'));
  children.push(...dottedLines(3));

  // ─── Section 12 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 12 — Budget Scrutiny Questions'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.8)'));
  children.push(guidanceText('Select the most important questions for this agency. Rank by priority — ask these first if hearing time is limited.'));

  children.push(subHeading('Priority Questions (Top 5-10):'));
  const pqW1 = Math.round(USABLE_WIDTH * 0.10);
  const pqW2 = Math.round(USABLE_WIDTH * 0.25);
  const pqW3 = Math.round(USABLE_WIDTH * 0.65);
  children.push(dataTable(
    ['Priority', 'Category', 'Question'],
    [pqW1, pqW2, pqW3],
    Array(10).fill(null).map((_, i) => [`${i + 1}`, null, null])
  ));

  children.push(spacer(120));
  children.push(subHeading('Additional Questions by Category:'));

  const categories = [
    'Agency Profile and Mandate:',
    'Performance and KPIs:',
    'Personnel Services:',
    'MOOE:',
    'Capital Outlay:',
    'GAD Budget:',
    'New Programs (Tier 2):',
    'Overall Budget:',
  ];
  categories.forEach(cat => {
    children.push(new Paragraph({
      spacing: { before: 120, after: 40 },
      children: [new TextRun({ text: cat, italics: true, bold: true, color: CHARCOAL, font: FONT, size: 20 })]
    }));
    children.push(...dottedLines(2));
  });

  // ─── Section 13 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 13 — Recommendations for the MP'));
  children.push(chapterRef('(Refer to Chapter 9, Section 9.9)'));

  children.push(new Paragraph({
    spacing: { before: 120, after: 80 },
    children: [
      new TextRun({ text: 'Recommended Position on Overall Budget: ', bold: true, color: CHARCOAL, font: FONT, size: 22 }),
      new TextRun({ text: '\u2610 Support    \u2610 Support with Amendments    \u2610 Oppose    \u2610 Reserve Position', color: CHARCOAL, font: FONT, size: 22 }),
    ]
  }));

  children.push(subHeading('Conditions (if conditional support):'));
  children.push(...dottedLines(3));

  children.push(spacer(120));
  children.push(subHeading('Recommended Budget Amendments:'));
  const raW1 = Math.round(USABLE_WIDTH * 0.05);
  const raW2 = Math.round(USABLE_WIDTH * 0.25);
  const raW3 = Math.round(USABLE_WIDTH * 0.20);
  const raW4 = Math.round(USABLE_WIDTH * 0.15);
  const raW5 = Math.round(USABLE_WIDTH * 0.15);
  const raW6 = Math.round(USABLE_WIDTH * 0.20);
  children.push(dataTable(
    ['No.', 'Type', 'Line Item / Program', 'Current Amount', 'Proposed Change', 'Justification'],
    [raW1, raW2, raW3, raW4, raW5, raW6],
    [
      ['1', '\u2610 Reduction  \u2610 Reallocation  \u2610 Conditional Release  \u2610 Deletion', null, null, null, null],
      ['2', '\u2610 Reduction  \u2610 Reallocation  \u2610 Conditional Release  \u2610 Deletion', null, null, null, null],
      ['3', '\u2610 Reduction  \u2610 Reallocation  \u2610 Conditional Release  \u2610 Deletion', null, null, null, null],
    ]
  ));

  children.push(spacer(120));
  children.push(subHeading('Top Priority Questions for the Hearing (from Section 12):'));
  children.push(...dottedLines(4));

  children.push(spacer(120));
  children.push(subHeading('Items Requiring Follow-Up:'));
  const fuW1 = Math.round(USABLE_WIDTH * 0.20);
  const fuW2 = Math.round(USABLE_WIDTH * 0.45);
  const fuW3 = Math.round(USABLE_WIDTH * 0.35);
  children.push(dataTable(
    ['Item', 'Details', 'Follow-Up Action Needed'],
    [fuW1, fuW2, fuW3],
    [[null, null, null], [null, null, null], [null, null, null]]
  ));

  // ─── Section 14 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 14 — 1-Minute Manifestation for Budget Approval'));
  children.push(chapterRef('(Source: BB16 of the CSW Budget Briefer framework)'));
  children.push(guidanceText('Prepare a concise 1-minute speech for the MP to deliver during the Committee on Finance hearing or plenary budget deliberation. The speech should reflect the position recommended in Section 13.'));

  children.push(spacer(80));
  children.push(new Paragraph({
    spacing: { before: 40, after: 80 },
    children: [
      new TextRun({ text: "MP's Preferred Language: ", bold: true, color: CHARCOAL, font: FONT, size: 22 }),
      new TextRun({ text: '\u2610 English    \u2610 Filipino    \u2610 Arabic    \u2610 Other: ________', color: CHARCOAL, font: FONT, size: 22 }),
    ]
  }));

  children.push(subHeading('Structure:'));
  children.push(dataTable(
    ['Part', 'Content'],
    [COL_35, COL_65],
    [
      ["Opening — One sentence stating the MP's position on this agency's budget", null],
      ['Strategic Alignment — How the budget serves BDP goals and BARMM priorities', null],
      ['Key Programs — 2-3 PPAS highlights with quick statistics', null],
      ['Legal Compliance — Budget aligns with mandated laws and policies', null],
      ["Impact — Benefits to the MP's priority constituencies and sectors", null],
      ['Fiscal Responsibility — Value for money, absorption capacity', null],
      ['Closing — Call to action, vote recommendation', null],
    ]
  ));

  children.push(spacer(120));
  children.push(subHeading('Draft Manifestation (keep under 1 minute — approximately 150-200 words):'));
  children.push(...dottedLines(8));

  // ─── Section 15 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 15 — Action Log'));

  const alW1 = Math.round(USABLE_WIDTH * 0.15);
  const alW2 = Math.round(USABLE_WIDTH * 0.40);
  const alW3 = Math.round(USABLE_WIDTH * 0.18);
  const alW4 = Math.round(USABLE_WIDTH * 0.27);
  children.push(dataTable(
    ['Date', 'Action', 'Responsible', 'Status'],
    [alW1, alW2, alW3, alW4],
    [
      [null, 'BEP submitted to Parliament', null, '\u2610 Complete'],
      [null, 'Agency budget data compiled', null, '\u2610 Complete  \u2610 In Progress'],
      [null, 'Previous FY expenditure data obtained', null, '\u2610 Complete  \u2610 In Progress'],
      [null, 'Audit findings reviewed', null, '\u2610 Complete  \u2610 N/A'],
      [null, 'Budget briefer prepared', null, '\u2610 Complete  \u2610 In Progress'],
      [null, 'Briefer submitted to MP for review', null, '\u2610 Complete  \u2610 Pending'],
      [null, 'Committee on Finance hearing', null, '\u2610 Complete  \u2610 Upcoming — ________'],
      [null, 'Plenary budget deliberation', null, '\u2610 Complete  \u2610 TBD'],
      [null, 'Post-hearing update', null, '\u2610 Complete  \u2610 Pending'],
      [null, null, null, null],
      [null, null, null, null],
    ]
  ));

  // ─── Section 16 — Approval ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 16 — Approval'));

  children.push(kvTable([
    ['Prepared by:', ''],
    ['Designation:', ''],
    ['Date Submitted:', ''],
    ['Recommended Position:', '\u2610 Support    \u2610 Support with Amendments    \u2610 Oppose    \u2610 Reserve Position'],
  ]));

  children.push(spacer(200));
  children.push(new Paragraph({
    spacing: { before: 60, after: 80 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: GOLD } },
    children: [new TextRun({ text: "MP's Decision:", bold: true, color: NAVY, font: FONT, size: 22 })]
  }));

  children.push(kvTable([
    ['\u2610 Approved as recommended', ''],
    ['\u2610 Approved with modifications:', ''],
    ['', ''],
    ['\u2610 Disapproved / Return for further study', ''],
    ["MP's Signature:", ''],
    ['Date:', ''],
  ]));

  children.push(spacer(200));
  children.push(new Paragraph({
    spacing: { before: 60, after: 80 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: GOLD } },
    children: [new TextRun({ text: 'Post-Hearing Notes:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(guidanceText('(After the committee hearing or plenary deliberation, record actual outcomes: questions asked, answers given, amendments adopted, commitments made by the agency, MP\'s vote.)'));
  children.push(...dottedLines(8));

  children.push(spacer(300));
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 200, after: 0 },
    children: [new TextRun({
      text: 'This template is designed to be reproduced and used as a standalone document. Permission is granted to photocopy or print this appendix for use in legislative offices of the Bangsamoro Parliament.',
      italics: true, color: '888888', font: FONT, size: 18
    })]
  }));

  return children;
}

// ─── Assemble Document ───
const doc = new Document({
  styles: {
    default: {
      document: { run: { font: FONT, size: 22, color: CHARCOAL } }
    },
  },
  sections: [{
    properties: {
      page: {
        margin: { top: MARGIN_TOP, right: MARGIN_RIGHT, bottom: MARGIN_BOTTOM, left: MARGIN_LEFT },
        size: { width: 11906, height: 16838 },
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 120 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: GOLD } },
          children: [new TextRun({
            text: 'APPENDIX G \u2014 BUDGET BRIEFER TEMPLATE',
            smallCaps: true, color: NAVY, font: FONT, size: 16
          })]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          border: { top: { style: BorderStyle.SINGLE, size: 1, color: GOLD } },
          spacing: { before: 80 },
          tabStops: [
            { type: TabStopType.RIGHT, position: USABLE_WIDTH }
          ],
          children: [
            new TextRun({ text: 'Bangsamoro Parliament \u2014 Bill Drafting Guidebook', color: '888888', font: FONT, size: 16 }),
            new TextRun({ text: '\t', font: FONT }),
            new TextRun({ text: 'Page ', color: '888888', font: FONT, size: 16 }),
            new TextRun({ children: [PageNumber.CURRENT], color: '888888', font: FONT, size: 16 }),
          ]
        })]
      })
    },
    children: buildContent()
  }]
});

// ─── Write File ───
const outDir = path.join(__dirname, 'appendices');
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
const outPath = path.join(outDir, 'Appendix-G-Budget-Briefer-Template.docx');

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outPath, buffer);
  console.log(`Created: ${outPath}`);
  console.log(`Size: ${(buffer.length / 1024).toFixed(1)} KB`);
}).catch(err => {
  console.error('Error generating DOCX:', err);
  process.exit(1);
});
