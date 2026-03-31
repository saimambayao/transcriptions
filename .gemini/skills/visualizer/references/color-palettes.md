# Professional Color Palettes

A collection of curated color palettes for data visualization. No purple colors are used in any palette.

---

## How to Use

Each palette is defined as a Python list of hex colors. Copy into your script:

```python
palette = ['#2C3E50', '#E74C3C', '#3498DB', '#2ECC71', '#F39C12']
```

For matplotlib:
```python
import matplotlib.pyplot as plt
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=palette)
```

For seaborn:
```python
import seaborn as sns
sns.set_palette(palette)
```

For plotly:
```python
fig.update_layout(colorway=palette)
```

---

## Government and Institutional

### Government Blue
Clean, authoritative palette for government reports and official documents.
```python
GOVT_BLUE = ['#1B4F72', '#2980B9', '#5DADE2', '#85C1E9', '#AED6F1', '#D6EAF8']
```
- Primary: `#1B4F72` (dark navy)
- Use for: Official reports, policy documents, BARMM publications

### Government Formal
Traditional institutional palette with warm accents.
```python
GOVT_FORMAL = ['#1A3C5E', '#C0392B', '#196F3D', '#B7950B', '#5D6D7E', '#ABB2B9']
```
- Use for: Formal government publications, legislative documents

### Civic Trust
Balanced palette that conveys stability and public service.
```python
CIVIC_TRUST = ['#2C3E50', '#16A085', '#2980B9', '#D4AC0D', '#E74C3C', '#7F8C8D']
```
- Use for: Public-facing reports, community presentations

---

## Corporate and Professional

### Corporate Steel
Modern corporate palette with blue-gray foundation.
```python
CORPORATE_STEEL = ['#2C3E50', '#34495E', '#1ABC9C', '#3498DB', '#E74C3C', '#F39C12']
```
- Use for: Business proposals, annual reports

### Neutral Professional
Sophisticated muted tones for executive presentations.
```python
NEUTRAL_PRO = ['#2C3E50', '#5D6D7E', '#1A5276', '#148F77', '#B7950B', '#A04000']
```
- Use for: Board presentations, executive summaries

### Modern Business
Fresh, contemporary palette for forward-looking documents.
```python
MODERN_BIZ = ['#0E4D64', '#137177', '#188C8B', '#1DA89E', '#22C3B1', '#F4B942']
```
- Use for: Innovation reports, strategic plans

---

## Cooperative and Community

### Cooperative Green
Palette centered on growth, community, and sustainability.
```python
COOP_GREEN = ['#196F3D', '#27AE60', '#52BE80', '#82E0AA', '#D5F5E3', '#F39C12']
```
- Primary: `#196F3D` (deep green)
- Use for: Cooperative reports, membership documents, sustainability reports

### Community Warm
Welcoming, people-centered palette.
```python
COMMUNITY_WARM = ['#E67E22', '#D35400', '#2ECC71', '#27AE60', '#2980B9', '#2C3E50']
```
- Use for: Community engagement materials, training documents

### Social Impact
Palette emphasizing positive change and development.
```python
SOCIAL_IMPACT = ['#1ABC9C', '#16A085', '#2ECC71', '#F39C12', '#E74C3C', '#2C3E50']
```
- Use for: Impact reports, development program visuals

---

## Financial

### Financial Trust
Conservative palette conveying reliability and trust.
```python
FINANCIAL_TRUST = ['#1B4F72', '#154360', '#1A5276', '#1F618D', '#2980B9', '#D4AC0D']
```
- Use for: Financial statements, audit reports, banking documents

### Financial Performance
Dynamic palette for financial dashboards and performance reports.
```python
FINANCIAL_PERF = ['#27AE60', '#E74C3C', '#2C3E50', '#F39C12', '#3498DB', '#1ABC9C']
```
- Green/red for gain/loss; neutral for context
- Use for: Profit/loss charts, KPI dashboards

### Money Green
Classic financial palette based on currency aesthetics.
```python
MONEY_GREEN = ['#0B5345', '#148F77', '#1ABC9C', '#76D7C4', '#D1F2EB', '#D4AC0D']
```
- Use for: Savings reports, investment summaries

---

## Warm Palettes

### Warm Confidence
Energetic warm palette for engaging presentations.
```python
WARM_CONFIDENCE = ['#E74C3C', '#F39C12', '#F1C40F', '#E67E22', '#D35400', '#2C3E50']
```
- Use for: Motivational presentations, campaign materials

### Sunset Professional
Warm gradient palette with professional feel.
```python
SUNSET_PRO = ['#C0392B', '#E74C3C', '#F39C12', '#F1C40F', '#27AE60', '#2C3E50']
```
- Use for: Year-end reports, achievement highlights

### Earth Tones
Natural, grounded palette for development and agriculture topics.
```python
EARTH_TONES = ['#6E2C00', '#A04000', '#D4AC0D', '#196F3D', '#1A5276', '#5D6D7E']
```
- Use for: Agricultural cooperative reports, rural development, environmental data

### Terracotta
Warm, earthy palette with Southeast Asian aesthetic.
```python
TERRACOTTA = ['#A04000', '#D35400', '#E67E22', '#F0B27A', '#1A5276', '#2C3E50']
```
- Use for: Cultural documents, regional development reports

---

## Cool Palettes

### Ocean Depth
Cool, calming palette with depth variation.
```python
OCEAN_DEPTH = ['#0B3D91', '#1565C0', '#1E88E5', '#42A5F5', '#90CAF9', '#16A085']
```
- Use for: Maritime cooperatives, fisheries data, water resource reports

### Teal Focus
Modern teal-centered palette.
```python
TEAL_FOCUS = ['#0E4D64', '#137177', '#188C8B', '#1ABC9C', '#76D7C4', '#F39C12']
```
- Use for: Health cooperatives, technology reports

### Arctic Clean
Crisp, clean palette with high contrast.
```python
ARCTIC_CLEAN = ['#1B4F72', '#2E86C1', '#85C1E9', '#D6EAF8', '#E74C3C', '#2C3E50']
```
- Use for: Clean data presentations, minimalist reports

---

## High Contrast and Accessibility

### Colorblind Safe (8 colors)
Optimized for deuteranopia, protanopia, and tritanopia.
```python
COLORBLIND_SAFE = ['#0072B2', '#E69F00', '#009E73', '#CC79A7', '#D55E00', '#56B4E9', '#F0E442', '#000000']
```
- Use for: Any document where accessibility is important
- Source: Based on Wong (2011) colorblind-safe palette (adapted, no purple)

### High Contrast
Maximum readability for small charts and projector presentations.
```python
HIGH_CONTRAST = ['#2C3E50', '#E74C3C', '#2ECC71', '#3498DB', '#F39C12', '#1ABC9C']
```
- Use for: Projected presentations, small embedded charts

### Print Safe
Palette that reproduces well in grayscale printing.
```python
PRINT_SAFE = ['#2C3E50', '#7F8C8D', '#BDC3C7', '#1ABC9C', '#E74C3C', '#F39C12']
```
- Ensure distinct values in grayscale: dark, medium-dark, medium-light, teal, red, gold
- Use for: Documents that may be printed in black and white

---

## Diverging Palettes (for scales with a midpoint)

### Red to Green (Performance)
For good/bad scales where green = positive, red = negative.
```python
DIVERGING_RG = ['#C0392B', '#E74C3C', '#F5B7B1', '#FDFEFE', '#ABEBC6', '#27AE60', '#196F3D']
```
- Use for: Performance scorecards, compliance ratings

### Blue to Orange (Neutral)
Diverging palette without value judgment.
```python
DIVERGING_BO = ['#1B4F72', '#2980B9', '#AED6F1', '#FDFEFE', '#F5CBA7', '#E67E22', '#A04000']
```
- Use for: Survey results (agree-disagree), temperature/variance data

### Teal to Red
Modern diverging palette.
```python
DIVERGING_TR = ['#0E4D64', '#1ABC9C', '#A3E4D7', '#FDFEFE', '#F5B7B1', '#E74C3C', '#922B21']
```
- Use for: Comparative analysis, deviation from target

---

## Sequential Palettes (for continuous data)

### Blue Sequential
Light to dark blue for single-variable intensity.
```python
SEQ_BLUE = ['#D6EAF8', '#AED6F1', '#85C1E9', '#5DADE2', '#2E86C1', '#1B4F72']
```

### Green Sequential
Light to dark green for growth/positive metrics.
```python
SEQ_GREEN = ['#D5F5E3', '#ABEBC6', '#82E0AA', '#52BE80', '#27AE60', '#196F3D']
```

### Warm Sequential
Light gold to deep red for heat/intensity.
```python
SEQ_WARM = ['#FEF9E7', '#F9E79F', '#F4D03F', '#F39C12', '#E67E22', '#C0392B']
```

### Gray Sequential
Neutral scale for background or secondary data.
```python
SEQ_GRAY = ['#F2F3F4', '#D5D8DC', '#ABB2B9', '#808B96', '#566573', '#2C3E50']
```

---

## BARMM / Regional Specific

### BARMM Official
Based on the Bangsamoro region's visual identity.
```python
BARMM_OFFICIAL = ['#1A5276', '#196F3D', '#D4AC0D', '#C0392B', '#2C3E50', '#F39C12']
```
- Blue (governance), Green (Islamic/growth), Gold (prosperity), Red (courage)
- Use for: BARMM official reports and publications

### Philippine Government
Based on Philippine flag and government visual standards.
```python
PH_GOVT = ['#0038A8', '#CE1126', '#FCD116', '#2C3E50', '#27AE60', '#5D6D7E']
```
- Blue, red, gold from the flag; supplemented with neutral tones
- Use for: National-level government documents

---

## Palette Selection Quick Reference

| Context | Recommended Palette |
|---|---|
| BARMM government report | BARMM Official or Government Blue |
| Philippine government doc | PH Govt or Government Formal |
| Cooperative annual report | Cooperative Green or Social Impact |
| Financial statement | Financial Trust or Money Green |
| Executive presentation | Neutral Professional or Corporate Steel |
| Training materials | Community Warm or Warm Confidence |
| Agricultural data | Earth Tones or Terracotta |
| Fisheries/maritime | Ocean Depth |
| Impact/development report | Social Impact or Civic Trust |
| Performance dashboard | Financial Performance or High Contrast |
| Printed document (B&W risk) | Print Safe |
| Accessibility required | Colorblind Safe |
| Heatmap / continuous data | Any Sequential palette |
| Good/bad scale | Diverging Red-Green |
| Neutral scale | Diverging Blue-Orange |
