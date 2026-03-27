/**
 * Generate Appendix F — Legislative Research Briefer Template
 * Bill Drafting Guidebook for the Bangsamoro Parliament
 *
 * Usage: NODE_PATH=$(npm root -g) node generate-appendix-f-docx.js
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

// A4 dimensions in DXA (1 inch = 1440 DXA)
const MM_TO_DXA = 56.7; // approx 1mm = 56.7 DXA
const PAGE_WIDTH_A4 = 11906; // A4 width in DXA
const MARGIN_LEFT = Math.round(25 * MM_TO_DXA);   // 25mm
const MARGIN_RIGHT = Math.round(25 * MM_TO_DXA);  // 25mm
const MARGIN_TOP = Math.round(20 * MM_TO_DXA);    // 20mm
const MARGIN_BOTTOM = Math.round(25 * MM_TO_DXA); // 25mm
const USABLE_WIDTH = PAGE_WIDTH_A4 - MARGIN_LEFT - MARGIN_RIGHT; // ~10488 DXA

// Column width helpers
const COL_35 = Math.round(USABLE_WIDTH * 0.35);
const COL_65 = Math.round(USABLE_WIDTH * 0.65);

// ─── Reusable Helpers ───
const thinBorder = { style: BorderStyle.SINGLE, size: 1, color: MID_GRAY };
const cellBorders = { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder };
const noBorders = {
  top: { style: BorderStyle.NONE, size: 0 },
  bottom: { style: BorderStyle.NONE, size: 0 },
  left: { style: BorderStyle.NONE, size: 0 },
  right: { style: BorderStyle.NONE, size: 0 },
};

function headerCell(text, width, opts = {}) {
  return new TableCell({
    borders: cellBorders,
    width: { size: width, type: WidthType.DXA },
    shading: { fill: NAVY, type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({
      alignment: opts.align || AlignmentType.LEFT,
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
  // A fill-in cell with minimum height
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

// Multi-column table with header row
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

// ─── Build Document Sections ───

function buildContent() {
  const children = [];

  // ─── Title Block ───
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 600, after: 120 },
    children: [new TextRun({ text: 'LEGISLATIVE RESEARCH BRIEFER', bold: true, color: NAVY, font: FONT, size: 36, smallCaps: true })]
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
    ['Control No.:', 'LB-________-________'],
    ['Date Prepared:', ''],
    ['Prepared by:', ''],
    ['Designation:', ''],
    ['Office of MP:', ''],
    ['Version:', '\u2610 Initial    \u2610 Updated (Version ____)'],
    ['Classification:', '\u2610 Full Briefer    \u2610 Short-Form Briefer'],
  ]));

  // ─── Section 1 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 1 — Brief Description of the Measure'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.3.1)'));

  children.push(kvTable([
    ['Bill/Resolution No.:', ''],
    ['Long Title:', ''],
    ['Short Title:', ''],
    ['Author(s):', ''],
    ['Co-Author(s):', ''],
    ['Date Filed:', ''],
    ['Committee Referred To:', ''],
    ['Type:', '\u2610 Government Bill    \u2610 Private Member Bill    \u2610 Resolution'],
    ['Status:', '(check the current stage below)'],
  ]));

  children.push(spacer(180));
  children.push(new Paragraph({
    spacing: { before: 60, after: 80 },
    children: [new TextRun({ text: 'Legislative Stage:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));

  const stageW1 = Math.round(USABLE_WIDTH * 0.55);
  const stageW2 = Math.round(USABLE_WIDTH * 0.15);
  const stageW3 = Math.round(USABLE_WIDTH * 0.30);
  const stages = [
    ['Proposal Stage (pre-filing)', '\u2610', ''],
    ['First Reading / Order of Business (for co-authorship)', '\u2610', 'Session No. ________'],
    ['Committee Referral', '\u2610', ''],
    ['Public Consultation', '\u2610', ''],
    ['Committee Deliberation', '\u2610', ''],
    ['Committee Report / Second Reading / Plenary', '\u2610', 'Session No. ________'],
    ['Third Reading / Plenary Vote', '\u2610', 'Session No. ________'],
    ['Other: ________________________', '\u2610', ''],
  ];
  children.push(dataTable(['Stage', 'Check', 'Session No.'], [stageW1, stageW2, stageW3], stages));

  children.push(spacer(120));
  children.push(kvTable([
    ['Date of Next Proceeding:', ''],
    ['Immediate Action Needed:', '(check one)'],
  ]));

  children.push(spacer(80));
  const actW1 = Math.round(USABLE_WIDTH * 0.75);
  const actW2 = Math.round(USABLE_WIDTH * 0.25);
  children.push(dataTable(['Action', 'Check'], [actW1, actW2], [
    ['Will be under "Business for the Day" / Simple Resolution', '\u2610'],
    ['Will be referred to a Committee / TWG', '\u2610'],
    ['Will undergo public consultation', '\u2610'],
    ['Will be deferred', '\u2610'],
    ['Other: ________________________', '\u2610'],
  ]));

  children.push(spacer(80));
  children.push(kvTable([
    ['Will MP co-author?', '\u2610 Principal Author    \u2610 Co-Author    \u2610 Will not author'],
  ]));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 40 },
    children: [new TextRun({ text: 'Summary of the Measure:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(guidanceText('(In two to four paragraphs, describe what the bill does: subject matter, key provisions, scope and coverage, obligations created, institutions established, rights conferred.)'));
  children.push(...dottedLines(8));

  // ─── Section 2 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 2 — Related Laws, Issuances, and Specific Provisions'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.3.2)'));
  children.push(guidanceText('Identify every law, issuance, or regulation that the bill interacts with. For each, state the specific provision and explain the relationship.'));

  const s2w1 = Math.round(USABLE_WIDTH * 0.28);
  const s2w2 = Math.round(USABLE_WIDTH * 0.32);
  const s2w3 = Math.round(USABLE_WIDTH * 0.40);
  children.push(dataTable(
    ['Law / Issuance', 'Relevant Provisions', 'Relationship to Proposed Measure'],
    [s2w1, s2w2, s2w3],
    [
      ['BOL (RA 11054) — Art. ___, Sec. ___', null, '\u2610 Implements  \u2610 Supplements  \u2610 Conflicts'],
      [null, null, '\u2610 Implements  \u2610 Supplements  \u2610 Conflicts'],
      [null, null, '\u2610 Implements  \u2610 Supplements  \u2610 Conflicts'],
      [null, null, '\u2610 Implements  \u2610 Supplements  \u2610 Conflicts'],
      [null, null, '\u2610 Implements  \u2610 Supplements  \u2610 Conflicts'],
      [null, null, '\u2610 Implements  \u2610 Supplements  \u2610 Conflicts'],
      [null, null, '\u2610 Implements  \u2610 Supplements  \u2610 Conflicts'],
    ]
  ));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 40 },
    children: [new TextRun({ text: 'Analysis of Conflicts or Overlaps:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(...dottedLines(4));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 80 },
    children: [new TextRun({ text: "Shari'ah Considerations:", bold: true, color: NAVY, font: FONT, size: 22 })]
  }));

  const sharW1 = Math.round(USABLE_WIDTH * 0.60);
  const sharW2 = Math.round(USABLE_WIDTH * 0.40);
  children.push(dataTable(
    ['Question', 'Assessment'],
    [sharW1, sharW2],
    [
      ['Does the bill affect personal, family, or property relations involving Muslims?', '\u2610 Yes    \u2610 No'],
      ["If yes, does the bill respect the Shari'ah court jurisdiction under BOL Article X?", '\u2610 Yes    \u2610 No    \u2610 N/A'],
      ['Does the bill affect Islamic banking, finance, or commercial transactions?', '\u2610 Yes    \u2610 No'],
      ["Are there provisions that may conflict with Islamic principles?", '\u2610 Yes    \u2610 No'],
      ['If yes, describe:', null],
    ]
  ));

  // ─── Section 3 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading("Section 3 — Impact Assessment and Alignment with the MP's Agenda"));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.3.3)'));

  children.push(new Paragraph({
    spacing: { before: 120, after: 80 },
    children: [new TextRun({ text: "Alignment with the MP's Legislative Agenda:", bold: true, color: NAVY, font: FONT, size: 22 })]
  }));

  const qa60 = Math.round(USABLE_WIDTH * 0.55);
  const qa40 = Math.round(USABLE_WIDTH * 0.45);
  children.push(dataTable(
    ['Question', 'Assessment'],
    [qa60, qa40],
    [
      ["Does the bill advance the MP's stated legislative priorities?", null],
      ["Does the bill benefit or burden the MP's constituency?", null],
      ["Does the bill align with the MP's committee work?", null],
      ['What are the political dimensions? (Government priority? Certified as urgent? Allied or rival sponsor?)', null],
    ]
  ));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 80 },
    children: [new TextRun({ text: 'Broader Impact Assessment:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));

  children.push(dataTable(
    ['Dimension', 'Assessment'],
    [qa60, qa40],
    [
      ['Social Impact — Who benefits? Who bears the costs?', null],
      ['Economic Impact — Investment, employment, costs to businesses and households?', null],
      ['Institutional Impact — New agencies, expanded mandates, restructuring required?', null],
    ]
  ));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 80 },
    children: [new TextRun({ text: 'BDP 2023-2028 Alignment', bold: true, color: NAVY, font: FONT, size: 22 }),
               new TextRun({ text: ' (check all goals the bill serves):', italics: true, color: '666666', font: FONT, size: 20 })]
  }));

  const bdpW0 = Math.round(USABLE_WIDTH * 0.08);
  const bdpW1 = Math.round(USABLE_WIDTH * 0.42);
  const bdpW2 = Math.round(USABLE_WIDTH * 0.50);
  children.push(dataTable(
    ['', 'Goal', 'How the Bill Serves This Goal'],
    [bdpW0, bdpW1, bdpW2],
    [
      ['\u2610', 'Goal 1 — Stable, just, and accountable government', null],
      ['\u2610', 'Goal 2 — Equitable, competitive, and robust economy', null],
      ['\u2610', 'Goal 3 — Peaceful, safe, and resilient communities', null],
      ['\u2610', 'Goal 4 — Inclusive, responsive, and quality social services', null],
      ['\u2610', 'Goal 5 — Rich and diverse Bangsamoro culture and identity', null],
      ['\u2610', 'Goal 6 — Strategic, adequate, and climate-resilient infrastructure', null],
    ]
  ));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 80 },
    children: [new TextRun({ text: 'Gender and Development (GAD) Assessment:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));

  children.push(dataTable(
    ['Question', 'Assessment'],
    [qa60, qa40],
    [
      ['Does the bill affect women and men differently?', '\u2610 Yes    \u2610 No'],
      ['Does the bill specifically address the needs of women, youth, children, or PWDs?', '\u2610 Yes    \u2610 No'],
      ['Does the bill affect indigenous peoples within the Bangsamoro?', '\u2610 Yes    \u2610 No'],
      ['Does the bill affect internally displaced persons (IDPs)?', '\u2610 Yes    \u2610 No'],
      ['If the bill creates programs, does it require sex-disaggregated data and reporting?', '\u2610 Yes    \u2610 No    \u2610 N/A'],
    ]
  ));

  // ─── Section 4 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 4 — Implementing Agencies'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.3.4)'));

  const s4w1 = Math.round(USABLE_WIDTH * 0.20);
  const s4w2 = Math.round(USABLE_WIDTH * 0.25);
  const s4w3 = Math.round(USABLE_WIDTH * 0.25);
  const s4w4 = Math.round(USABLE_WIDTH * 0.30);
  children.push(dataTable(
    ['Agency', 'Role Under the Bill', 'Current Mandate Covers This?', 'Capacity Assessment'],
    [s4w1, s4w2, s4w3, s4w4],
    [
      [null, null, '\u2610 Yes  \u2610 Partially  \u2610 No', '\u2610 Adequate  \u2610 Limited  \u2610 Insufficient'],
      [null, null, '\u2610 Yes  \u2610 Partially  \u2610 No', '\u2610 Adequate  \u2610 Limited  \u2610 Insufficient'],
      [null, null, '\u2610 Yes  \u2610 Partially  \u2610 No', '\u2610 Adequate  \u2610 Limited  \u2610 Insufficient'],
      [null, null, '\u2610 Yes  \u2610 Partially  \u2610 No', '\u2610 Adequate  \u2610 Limited  \u2610 Insufficient'],
    ]
  ));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 40 },
    children: [new TextRun({ text: 'Coordination Requirements:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(...dottedLines(3));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 40 },
    children: [new TextRun({ text: 'Capacity Gaps Identified:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(...dottedLines(3));

  // ─── Section 5 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 5 — Implementation Mechanisms and Timeline'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.3.5)'));

  children.push(kvTable([
    ['IRR Required?', '\u2610 Yes    \u2610 No'],
    ['IRR Deadline:', '________ days from effectivity'],
    ['Responsible for IRR:', ''],
    ['Phase-In Provisions?', '\u2610 Yes    \u2610 No'],
    ['Phase-In Description:', ''],
    ['Reporting Requirements?', '\u2610 Yes    \u2610 No'],
    ['Reports To:', ''],
    ['Reporting Frequency:', ''],
    ['Sunset Clause?', '\u2610 Yes    \u2610 No'],
    ['Expiry Date / Review Period:', ''],
  ]));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 40 },
    children: [new TextRun({ text: 'Gap Between Effectivity and Implementation Readiness:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(...dottedLines(3));

  // ─── Section 6 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 6 — Budgetary and Financial Implications'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.3.6)'));

  const s6w1 = Math.round(USABLE_WIDTH * 0.30);
  const s6w2 = Math.round(USABLE_WIDTH * 0.20);
  const s6w3 = Math.round(USABLE_WIDTH * 0.25);
  const s6w4 = Math.round(USABLE_WIDTH * 0.25);
  children.push(dataTable(
    ['Category', 'Estimated Cost', 'Recurring / One-Time', 'Notes'],
    [s6w1, s6w2, s6w3, s6w4],
    [
      ['Personnel Services (new positions, salary upgrades)', null, '\u2610 Recurring  \u2610 One-Time', null],
      ['MOOE (operations, training, travel)', null, '\u2610 Recurring  \u2610 One-Time', null],
      ['Capital Outlay (facilities, equipment, vehicles)', null, '\u2610 Recurring  \u2610 One-Time', null],
      ['Total Estimated Cost', null, '', null],
    ]
  ));

  children.push(spacer(120));
  children.push(kvTable([
    ['Funding Source Identified in the Bill?', '\u2610 Yes    \u2610 No'],
    ['If Yes, Source:', ''],
    ['Amount Appropriated in the Bill:', ''],
    ['Revenue Implications (if revenue measure):', ''],
    ['Fiscal Sustainability Assessment:', ''],
  ]));

  children.push(...dottedLines(3));

  // ─── Section 7 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 7 — Highlights of Previous Proceedings'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.3.7)'));

  const s7w1 = Math.round(USABLE_WIDTH * 0.22);
  const s7w2 = Math.round(USABLE_WIDTH * 0.15);
  const s7w3 = Math.round(USABLE_WIDTH * 0.38);
  const s7w4 = Math.round(USABLE_WIDTH * 0.25);
  children.push(dataTable(
    ['Proceeding', 'Date', 'Key Issues Raised', 'Outcome'],
    [s7w1, s7w2, s7w3, s7w4],
    [
      ['Committee Hearing', null, null, null],
      ['Committee Hearing (2nd)', null, null, null],
      ['Plenary (if applicable)', null, null, null],
    ]
  ));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 40 },
    children: [new TextRun({ text: 'Committee Amendments Made:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(...dottedLines(3));

  children.push(spacer(120));
  children.push(new Paragraph({
    spacing: { before: 60, after: 40 },
    children: [new TextRun({ text: 'Unresolved Issues:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(...dottedLines(3));

  // ─── Section 8 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 8 — Interpellation Questions'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.4)'));
  children.push(guidanceText('Prepare three to seven interpellation sequences. Each follows the six-part structure. Arrange in order of importance — most critical questions first.'));

  const iqW1 = Math.round(USABLE_WIDTH * 0.35);
  const iqW2 = Math.round(USABLE_WIDTH * 0.65);

  for (let q = 1; q <= 3; q++) {
    children.push(spacer(120));
    children.push(new Paragraph({
      spacing: { before: 120, after: 80 },
      children: [new TextRun({ text: `Question No. ${q}`, bold: true, color: NAVY, font: FONT, size: 22 })]
    }));
    children.push(dataTable(
      ['Part', 'Content'],
      [iqW1, iqW2],
      [
        ['Introduction / Context ("Hugot")', null],
        ['Question', null],
        ['Anticipated Answer', null],
        ['Manifestation (if answer is satisfactory)', null],
        ['Manifestation (if answer is evasive or reveals a gap)', null],
        ['Proposed Amendment (if applicable)', null],
        ['Justification for Amendment', null],
      ]
    ));
  }

  children.push(spacer(80));
  children.push(guidanceText('(Add additional question sequences as needed. Prepare up to seven for complex bills.)'));

  // ─── Section 9 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 9 — Summary of Proposed Amendments'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.5)'));

  const s9w1 = Math.round(USABLE_WIDTH * 0.06);
  const s9w2 = Math.round(USABLE_WIDTH * 0.10);
  const s9w3 = Math.round(USABLE_WIDTH * 0.22);
  const s9w4 = Math.round(USABLE_WIDTH * 0.22);
  const s9w5 = Math.round(USABLE_WIDTH * 0.22);
  const s9w6 = Math.round(USABLE_WIDTH * 0.18);
  children.push(dataTable(
    ['No.', 'Section', 'Current Text', 'Proposed Amendment', 'Justification', 'Priority'],
    [s9w1, s9w2, s9w3, s9w4, s9w5, s9w6],
    [
      ['1', null, null, null, null, '\u2610 High  \u2610 Medium  \u2610 Low'],
      ['2', null, null, null, null, '\u2610 High  \u2610 Medium  \u2610 Low'],
      ['3', null, null, null, null, '\u2610 High  \u2610 Medium  \u2610 Low'],
      ['4', null, null, null, null, '\u2610 High  \u2610 Medium  \u2610 Low'],
      ['5', null, null, null, null, '\u2610 High  \u2610 Medium  \u2610 Low'],
    ]
  ));

  // ─── Section 10 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading("Section 10 — MP's Position — Brief Speech / Manifestation"));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.6.1)'));

  children.push(new Paragraph({
    spacing: { before: 120, after: 80 },
    children: [
      new TextRun({ text: 'Recommended Position: ', bold: true, color: CHARCOAL, font: FONT, size: 22 }),
      new TextRun({ text: '\u2610 Support    \u2610 Support with Amendments    \u2610 Oppose    \u2610 Reserve Position', color: CHARCOAL, font: FONT, size: 22 }),
    ]
  }));

  children.push(new Paragraph({
    spacing: { before: 120, after: 40 },
    children: [new TextRun({ text: 'Draft Speech (2-4 minutes):', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(...dottedLines(10));

  // ─── Section 11 ───
  children.push(spacer(240));
  children.push(sectionHeading('Section 11 — 1-Minute Vote Manifestation'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.6.2)'));

  children.push(new Paragraph({
    spacing: { before: 120, after: 40 },
    children: [new TextRun({ text: 'Draft (3-5 sentences):', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(...dottedLines(5));

  // ─── Section 12 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 12 — Matters for Information of the MP'));
  children.push(chapterRef('(Refer to Chapter 8, Section 8.7)'));

  children.push(dataTable(
    ['Category', 'Details'],
    [COL_35, COL_65],
    [
      ['Stakeholder Positions', null],
      ['Media Coverage', null],
      ['Related Developments (Chief Minister statements, committee chair signals, parallel bills)', null],
      ['Political Dynamics', null],
      ['Pending Court Cases', null],
      ['Constituency Feedback', null],
      ['Comparative Legislation (Congress, other regions, LGUs)', null],
      ['Expert Opinions', null],
      ['Timing / Procedural Considerations', null],
    ]
  ));

  // ─── Section 13 ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 13 — Action Log'));

  const alW1 = Math.round(USABLE_WIDTH * 0.15);
  const alW2 = Math.round(USABLE_WIDTH * 0.40);
  const alW3 = Math.round(USABLE_WIDTH * 0.18);
  const alW4 = Math.round(USABLE_WIDTH * 0.27);
  children.push(dataTable(
    ['Date', 'Action', 'Responsible', 'Status'],
    [alW1, alW2, alW3, alW4],
    [
      [null, 'Bill received / identified for analysis', null, '\u2610 Complete'],
      [null, 'Legislative analysis prepared', null, '\u2610 Complete  \u2610 In Progress'],
      [null, 'Interpellation questions drafted', null, '\u2610 Complete  \u2610 In Progress'],
      [null, 'Proposed amendments drafted', null, '\u2610 Complete  \u2610 In Progress'],
      [null, 'Briefer submitted to MP for review', null, '\u2610 Complete  \u2610 Pending'],
      [null, 'Committee hearing', null, '\u2610 Complete  \u2610 Upcoming — ________'],
      [null, 'Plenary deliberation', null, '\u2610 Complete  \u2610 TBD'],
      [null, 'Post-proceeding update', null, '\u2610 Complete  \u2610 Pending'],
      [null, null, null, null],
      [null, null, null, null],
    ]
  ));

  // ─── Section 14 ───
  children.push(spacer(240));
  children.push(sectionHeading('Section 14 — Supervisory Review'));

  const s14w1 = Math.round(USABLE_WIDTH * 0.20);
  const s14w2 = Math.round(USABLE_WIDTH * 0.20);
  const s14w3 = Math.round(USABLE_WIDTH * 0.35);
  const s14w4 = Math.round(USABLE_WIDTH * 0.13);
  const s14w5 = Math.round(USABLE_WIDTH * 0.12);
  children.push(dataTable(
    ['Action', 'Reviewer', 'Review / Clearance Notes', 'Date', 'Time'],
    [s14w1, s14w2, s14w3, s14w4, s14w5],
    [
      ['First Review / Clearance', null, null, null, null],
      ['Second Review / Clearance', null, null, null, null],
      ['Chief of Staff Clearance', null, null, null, null],
      [null, null, null, null, null],
    ]
  ));

  // ─── Section 15 — Approval ───
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(sectionHeading('Section 15 — Approval'));

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
    children: [new TextRun({ text: 'Comments by the MP:', bold: true, color: NAVY, font: FONT, size: 22 })]
  }));
  children.push(new Paragraph({
    spacing: { before: 80, after: 0 },
    border: { bottom: { style: BorderStyle.DOTTED, size: 1, color: MID_GRAY } },
    children: [new TextRun({ text: '1.  ', color: CHARCOAL, font: FONT, size: 22 })]
  }));
  children.push(new Paragraph({
    spacing: { before: 200, after: 0 },
    border: { bottom: { style: BorderStyle.DOTTED, size: 1, color: MID_GRAY } },
    children: [new TextRun({ text: '2.  ', color: CHARCOAL, font: FONT, size: 22 })]
  }));
  children.push(new Paragraph({
    spacing: { before: 200, after: 0 },
    border: { bottom: { style: BorderStyle.DOTTED, size: 1, color: MID_GRAY } },
    children: [new TextRun({ text: '3.  ', color: CHARCOAL, font: FONT, size: 22 })]
  }));

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
        size: { width: 11906, height: 16838 }, // A4
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 120 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: GOLD } },
          children: [new TextRun({
            text: 'APPENDIX F \u2014 LEGISLATIVE RESEARCH BRIEFER TEMPLATE',
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
const outPath = path.join(outDir, 'Appendix-F-Legislative-Briefer-Template.docx');

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outPath, buffer);
  console.log(`Created: ${outPath}`);
  console.log(`Size: ${(buffer.length / 1024).toFixed(1)} KB`);
}).catch(err => {
  console.error('Error generating DOCX:', err);
  process.exit(1);
});
