---
description: "Comprehensive audit of your organic search performance using Google Search Console data. Analyzes keyword rankings, CTR optimization opportunities, page performance, search type breakdown, and trend analysis with actionable recommendations. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** google_search_console
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Organic Search Performance Audit

Comprehensive organic search analysis using Google Search Console data.

- Site: [specify site_url]
- Period: 28 days
- Country: all
- Search type: web
- Min impressions for striking distance: 100

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### Executive Summary
| Metric | Value | vs Previous Period |
|--------|-------|--------------------|
| Total Clicks | X | +/-Y% |
| Total Impressions | X | +/-Y% |
| Average CTR | X% | +/-Y pp |
| Average Position | X.X | +/-Y.Y |
| Health | STRONG / STABLE / DECLINING / NEEDS ATTENTION |

### Top 10 Keywords (by clicks)
| Keyword | Clicks | Impressions | CTR | Position | CTR Status |
|---------|--------|-------------|-----|----------|------------|
Status = "OK" if CTR meets benchmark for position, "LOW" if below.

### CTR Optimization Opportunities
Keywords where actual CTR is below expected for their position:
| Keyword | Position | Actual CTR | Expected CTR | Gap | Fix |
|---------|----------|-----------|-------------|-----|-----|
Fix = improve title tag, meta description, or structured data.

**CTR Benchmarks by Position:**
Position 1: 27-32% | Position 2: 15-18% | Position 3: 10-13%
Position 4-5: 5-9% | Position 6-10: 2-5%

### Striking Distance Keywords (Position 4-20, high impressions)
| Keyword | Position | Impressions | Current Clicks | Potential Clicks |
|---------|----------|-------------|---------------|------------------|
Potential = impressions * expected CTR at position 3.

### Top Pages (by clicks)
| Page URL | Clicks | Impressions | CTR | Avg Position |
|----------|--------|-------------|-----|-------------|

### Trend Summary
[1-2 sentences describing the daily trend: stable, growing, declining, or spiky. Note any sudden drops/spikes and weekday vs weekend patterns.]

### Recommendations
1. [Highest-impact action with specific keywords/pages]
2. [Second recommendation]
3. [Third recommendation]

## EXECUTION STEPS

### Step 1: Get overall performance totals
```
gsc_search_analytics(
    site_url="[specify site_url]",
    days=28,

> Conditional: if country
country_filter="[specify country]",
    search_type="web"
)
```
No dimensions = aggregated totals for clicks, impressions, CTR, position.

### Step 2: Get top keywords
```
gsc_search_analytics(
    site_url="[specify site_url]",
    dimensions=["query"],
    days=28,
    row_limit=50,

> Conditional: if country
country_filter="[specify country]",
    search_type="web"
)
```
Use the top 10 by clicks for the keyword table. Flag any with CTR below benchmark for their position.

### Step 3: Get page-level performance
```
gsc_search_analytics(
    site_url="[specify site_url]",
    dimensions=["page"],
    days=28,
    row_limit=50,

> Conditional: if country
country_filter="[specify country]",
    search_type="web"
)
```
Identify high-impression/low-click pages (CTR optimization candidates).

### Step 4: Find striking distance keywords
```
gsc_search_analytics(
    site_url="[specify site_url]",
    dimensions=["query"],
    days=28,
    row_limit=5000,

> Conditional: if country
country_filter="[specify country]",
    search_type="web"
)
```
Filter results: position between 4 and 20, impressions > 100.
Calculate potential clicks if moved to position 3 (use 11% CTR * impressions).

### Step 5: Get daily trend
```
gsc_search_analytics(
    site_url="[specify site_url]",
    dimensions=["date"],
    days=28,

> Conditional: if country
country_filter="[specify country]",
    search_type="web"
)
```
Identify sudden drops, spikes, or weekly patterns.

> Conditional: if search_type == "all"

### Step 6: Search type breakdown
Run separate queries for search_type="web", "discover", and "image" to compare performance across search types.

### Step 6: Compile and recommend
- Rank CTR optimization opportunities by impression volume (highest impact first)
- Rank striking distance keywords by potential click gain
- Generate 3 prioritized recommendations

## EDGE CASES
- **New site with <7 days of data**: Note limited data; skip trend analysis and previous period comparison. Focus on what data exists.
- **No GSC property verified**: The tool will return an error. Advise user to verify site ownership in Google Search Console first.
- **Low impressions (<100 total)**: Site has minimal search visibility. Focus recommendations on content creation and indexing rather than optimization.
- **All keywords position >20**: Site is not ranking competitively. Recommend content quality audit and backlink strategy rather than CTR optimization.
- **GSC data freshness**: Data is typically 2-3 days delayed. Note the actual date range in the report.