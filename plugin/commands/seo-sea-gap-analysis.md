---
description: "Compare organic keywords (Search Console) with paid keywords (Google Ads) to find cannibalization, savings opportunities, and content gaps. Identifies keywords where you're paying for clicks you could get organically, and paid keywords that need organic content. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** google_search_console, google_ads
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# SEO vs SEA Keyword Gap Analysis

Compare organic search performance (Google Search Console) with paid search keywords (Google Ads) to identify gaps, overlap, and optimization opportunities.

## Parameters
- Site URL: [specify site_url]
- Google Ads Account: [specify google_ads_account]
- Period: 28 days
- Country: all
- Minimum impressions: 50

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### Executive Summary

| Metric | Value |
|--------|-------|
| Organic keywords | [X] |
| Paid keywords | [Y] |
| Overlap | [Z] ([%]) |
| Est. monthly savings (cannibalization) | [X] |
| Content opportunities worth | [X]/month in ad spend |

### Quadrant Breakdown

| Quadrant | Keywords | Monthly Spend | Action |
|----------|----------|---------------|--------|
| Q1: Cannibalization | [N] | [X] | Test pausing ads |
| Q2: Paid-Only | [N] | [X] | Create content |
| Q3: Organic Winners | [N] | 0 | Monitor |
| Q4: Blind Spots | [N] | 0 | Evaluate |

### Top Cannibalized Keywords (Q1)

| Keyword | Org Pos | Org CTR | Paid Cost/mo | Action |
|---------|---------|---------|--------------|--------|

### Top Content Opportunities (Q2)

| Keyword | CPC | Paid Cost/mo | Conversions | Priority |
|---------|-----|--------------|-------------|----------|

### Recommendations

1. [Highest-impact action]
2. [Second action]
3. [Third action]

## EXECUTION STEPS

### Step 1: Discover Accounts

Use `gsc_list_sites` to confirm access to the GSC property.
Use `google_ads_list_accounts` to confirm access to the Google Ads account.

### Step 2: Gather Organic Data (GSC)

Use `gsc_search_analytics`:
- site_url: "[specify site_url]"
- dimensions: ["query"]
- days: 28
- row_limit: 1000

> Conditional: if country
- country_filter: "[specify country]"

Record: query, clicks, impressions, ctr, position.

### Step 3: Gather Paid Data (Google Ads)

Use `google_ads_run_gaql`:
- customer_id: "[specify google_ads_account]"
- query: "SELECT ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type, metrics.impressions, metrics.clicks, metrics.ctr, metrics.average_cpc, metrics.cost_micros FROM keyword_view WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.impressions DESC LIMIT 500"

Record: keyword, clicks, impressions, cost, conversions, cpa.

### Step 4: Classify Keywords into Four Quadrants

**Q1: Cannibalization** — Organic position <= 5 AND paid ads active
- You may be paying for clicks you'd get organically
- Calculate potential savings if ads were paused

**Q2: Paid-Only** — No organic ranking (position > 20 or absent) AND paid ads active
- Content opportunity: write content to eventually replace ad spend
- Prioritize by monthly cost and conversion rate

**Q3: Organic Winners** — Organic position <= 5 AND no paid ads
- Free traffic — no action needed, monitor rankings

**Q4: Blind Spots** — Weak organic AND no paid ads
- Are these worth pursuing? Check search volume and intent

### Step 5: Present Results

Fill in the output format above with the classified data. Highlight the top 10 keywords per quadrant sorted by potential impact (cost savings for Q1, content ROI for Q2).

## EDGE CASES

- **No GSC property found**: Ask the user to verify the site URL format (sc-domain:example.com vs https://example.com). List available properties with `gsc_list_sites`.
- **No Google Ads account**: Ask the user for the correct customer ID. List available accounts with `google_ads_list_accounts`.
- **No keyword overlap**: Report that organic and paid strategies are fully segmented. Focus on Q2 (content opportunities) and Q4 (blind spots).
- **Low traffic site (<1000 impressions)**: Note that data is thin and results may be directional. Suggest extending the period to 90 days.
- **Brand keywords dominating results**: Separate brand vs non-brand keywords in the analysis. Brand cannibalization is usually intentional (defensive bidding), so flag but don't recommend pausing without context.