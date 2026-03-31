---
name: xlsx
description: |
  Comprehensive Excel spreadsheet skill for creation, editing, analysis, and visualization.
  Use when: (1) creating new spreadsheets with formulas/formatting, (2) reading/analyzing Excel data,
  (3) editing existing spreadsheets while preserving formulas, (4) data analysis with pivot tables,
  (5) generating charts and visualizations, (6) recalculating formulas, (7) financial modeling.
  Supports .xlsx, .xlsm, .csv, .tsv files.
argument-hint: "[file-path]"
allowed-tools: Read, Bash
---

# Excel Skill

Comprehensive spreadsheet creation, editing, analysis, and visualization.

## Use Cases

1. **Create spreadsheets** - New files with formulas, formatting, and structure
2. **Edit existing files** - Modify while preserving formulas and formatting
3. **Data analysis** - Statistics, grouping, filtering, pivot tables
4. **Visualization** - Charts, graphs, conditional formatting
5. **Financial modeling** - Color-coded models with proper conventions
6. **Formula recalculation** - Update calculated values via LibreOffice

## Setup

```bash
# Python packages
pip install pandas openpyxl xlrd xlsxwriter matplotlib

# For formula recalculation
brew install libreoffice
```

## Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `recalc.py` | Recalculate all formulas | `python recalc.py <xlsx> [timeout]` |

---

## Library Selection Guide

| Task | Library | Why |
|------|---------|-----|
| Data analysis, statistics | pandas | Powerful data manipulation |
| Bulk data operations | pandas | Fast vectorized operations |
| Simple data export | pandas | Quick `to_excel()` |
| Complex formatting | openpyxl | Full Excel feature support |
| Formulas | openpyxl | Preserves formula strings |
| Editing existing files | openpyxl | Preserves structure |
| Charts in Excel | openpyxl | Native Excel charts |
| Charts as images | matplotlib | More customization |

---

## Reading Excel Files

### Basic Reading with pandas

```python
import pandas as pd

# Read Excel - default first sheet
df = pd.read_excel('file.xlsx')

# Read specific sheet
df = pd.read_excel('file.xlsx', sheet_name='Sales')

# Read all sheets as dict
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)

# Read with options
df = pd.read_excel('file.xlsx',
    usecols=['A', 'C', 'E'],      # Specific columns
    dtype={'id': str},            # Force data types
    parse_dates=['date_column']   # Parse dates
)
```

### Reading Multiple Sheets

```python
import pandas as pd

excel_file = pd.ExcelFile('workbook.xlsx')

for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    print(f"\n{sheet_name}:")
    print(df.head())
```

### Reading with openpyxl (Preserves Formulas)

```python
from openpyxl import load_workbook

# Load with formulas as strings
wb = load_workbook('file.xlsx')
sheet = wb.active
print(sheet['A1'].value)  # Shows formula like '=SUM(B1:B10)'

# Load with calculated values (WARNING: loses formulas on save)
wb = load_workbook('file.xlsx', data_only=True)
print(sheet['A1'].value)  # Shows calculated value
```

---

## Creating Excel Files

### Simple Creation with pandas

```python
import pandas as pd

df = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Sales': [100, 200, 150],
    'Profit': [20, 40, 30]
})

df.to_excel('output.xlsx', sheet_name='Sales', index=False)
```

### With Formulas and Formatting (openpyxl)

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active

# Add data
sheet['A1'] = 'Item'
sheet['B1'] = 'Amount'
sheet.append(['Widget', 100])
sheet.append(['Gadget', 200])
sheet.append(['Total', '=SUM(B2:B3)'])  # Formula

# Formatting
sheet['A1'].font = Font(bold=True)
sheet['B4'].font = Font(bold=True)
sheet.column_dimensions['A'].width = 15

wb.save('output.xlsx')
```

### CRITICAL: Use Formulas, Not Hardcoded Values

```python
# BAD - Hardcoding calculated values
total = df['Sales'].sum()
sheet['B10'] = total  # Hardcodes 5000

# GOOD - Let Excel calculate
sheet['B10'] = '=SUM(B2:B9)'
```

---

## Editing Existing Files

```python
from openpyxl import load_workbook

wb = load_workbook('existing.xlsx')
sheet = wb.active  # or wb['SheetName']

# Modify cells
sheet['A1'] = 'New Value'

# Insert/delete rows and columns
sheet.insert_rows(2)
sheet.delete_cols(3)

# Add new sheet
new_sheet = wb.create_sheet('NewSheet')
new_sheet['A1'] = 'Data'

wb.save('modified.xlsx')
```

---

## Data Analysis

### Basic Analysis

```python
import pandas as pd

df = pd.read_excel('data.xlsx')

# Preview and info
df.head()
df.info()
df.describe()

# Filter
high_sales = df[df['sales'] > 10000]

# Group and aggregate
sales_by_region = df.groupby('region')['sales'].sum()

# Calculate new columns
df['profit_margin'] = (df['revenue'] - df['cost']) / df['revenue']

# Sort
df_sorted = df.sort_values('sales', ascending=False)
```

### Pivot Tables

```python
import pandas as pd

df = pd.read_excel('sales_data.xlsx')

pivot = pd.pivot_table(
    df,
    values='sales',
    index='region',
    columns='product',
    aggfunc='sum',
    fill_value=0
)

pivot.to_excel('pivot_report.xlsx')
```

### Data Cleaning

```python
import pandas as pd

df = pd.read_excel('messy_data.xlsx')

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(0)  # or df.dropna()

# Clean strings
df['name'] = df['name'].str.strip()

# Convert types
df['date'] = pd.to_datetime(df['date'])
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

df.to_excel('cleaned_data.xlsx', index=False)
```

### Merging Files

```python
import pandas as pd

# Concatenate vertically
df1 = pd.read_excel('q1.xlsx')
df2 = pd.read_excel('q2.xlsx')
combined = pd.concat([df1, df2], ignore_index=True)

# Merge on common column
customers = pd.read_excel('customers.xlsx')
sales = pd.read_excel('sales.xlsx')
merged = pd.merge(sales, customers, on='customer_id', how='left')

merged.to_excel('merged_data.xlsx', index=False)
```

---

## Charts and Visualization

### With matplotlib (Save as Image)

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx')

# Bar chart
df.plot(x='category', y='value', kind='bar')
plt.title('Sales by Category')
plt.tight_layout()
plt.savefig('chart.png')

# Pie chart
df.set_index('category')['value'].plot(kind='pie', autopct='%1.1f%%')
plt.title('Market Share')
plt.savefig('pie_chart.png')
```

### With openpyxl (Native Excel Charts)

```python
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
sheet = wb.active

# Add data
data = [['Product', 'Sales'], ['A', 100], ['B', 200], ['C', 150]]
for row in data:
    sheet.append(row)

# Create chart
chart = BarChart()
chart.title = 'Sales by Product'
data_ref = Reference(sheet, min_col=2, min_row=1, max_row=4)
cats_ref = Reference(sheet, min_col=1, min_row=2, max_row=4)
chart.add_data(data_ref, titles_from_data=True)
chart.set_categories(cats_ref)
sheet.add_chart(chart, 'D2')

wb.save('chart.xlsx')
```

---

## Conditional Formatting

```python
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font

wb = load_workbook('data.xlsx')
ws = wb.active

red_fill = PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid')
green_fill = PatternFill(start_color='00FF00', end_color='00FF00', fill_type='solid')

for row in range(2, ws.max_row + 1):
    cell = ws[f'B{row}']
    if cell.value and cell.value < 150:
        cell.fill = red_fill
    else:
        cell.fill = green_fill

# Bold headers
for cell in ws[1]:
    cell.font = Font(bold=True)

wb.save('formatted.xlsx')
```

---

## Formula Recalculation

Excel files created/modified by openpyxl contain formulas as strings but not calculated values. Use the recalc script:

```bash
python recalc.py output.xlsx [timeout_seconds]
```

The script:
- Recalculates all formulas in all sheets via LibreOffice
- Scans for Excel errors (#REF!, #DIV/0!, #VALUE!, #NAME?, #N/A)
- Returns JSON with error details

**Output format:**
```json
{
  "status": "success",
  "total_errors": 0,
  "total_formulas": 42,
  "error_summary": {}
}
```

If errors found:
```json
{
  "status": "errors_found",
  "total_errors": 2,
  "error_summary": {
    "#REF!": {
      "count": 2,
      "locations": ["Sheet1!B5", "Sheet1!C10"]
    }
  }
}
```

---

## Financial Model Standards

### Color Coding (Industry Standard)

| Color | RGB | Use For |
|-------|-----|---------|
| Blue text | 0,0,255 | Hardcoded inputs, scenario variables |
| Black text | 0,0,0 | All formulas and calculations |
| Green text | 0,128,0 | Links from other worksheets |
| Red text | 255,0,0 | External links to other files |
| Yellow background | 255,255,0 | Key assumptions needing attention |

### Number Formatting

| Type | Format | Example |
|------|--------|---------|
| Years | Text | "2024" not "2,024" |
| Currency | $#,##0 | Specify units in headers |
| Zeros | Show as "-" | $#,##0;($#,##0);- |
| Percentages | 0.0% | One decimal |
| Multiples | 0.0x | EV/EBITDA, P/E |
| Negatives | Parentheses | (123) not -123 |

### Formula Rules

- Place ALL assumptions in separate cells
- Use cell references, not hardcoded values: `=B5*(1+$B$6)` not `=B5*1.05`
- Document sources for hardcoded values

---

## Common Workflow

1. **Choose library**: pandas for data, openpyxl for formulas/formatting
2. **Create/Load**: New workbook or existing file
3. **Modify**: Add data, formulas, formatting
4. **Save**: Write to file
5. **Recalculate** (if using formulas): `python recalc.py output.xlsx`
6. **Verify**: Check for errors, fix if needed

---

## Performance Tips

- Use `usecols` to read specific columns only
- Use `chunksize` for very large files
- Use `read_only=True` or `write_only=True` for large files in openpyxl
- Specify `dtype` for faster reading

## Code Style

- Write minimal, concise code
- Avoid verbose variable names
- Skip unnecessary print statements
- Add comments to cells with complex formulas
