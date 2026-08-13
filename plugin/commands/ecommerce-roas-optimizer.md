---
description: "Deep-dive analysis for e-commerce businesses. Analyze product-level ROAS via Meta Shopping, Google Shopping/PMax and GA4 e-commerce data, identify winners/losers, and get actionable recommendations. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# E-commerce ROAS Optimizer

Analyze e-commerce ad performance for last 30 days
> Conditional: if product_category
, focusing on [specify product_category].

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### REVENUE OVERVIEW
| Metric | Value | vs Prior Period | vs Target |
|--------|-------|-----------------|-----------|
| Ad Revenue | | | |
| Ad Spend | | | |
| Blended ROAS | | | |
| Orders from Ads | | | |
| AOV | | | |

### PRODUCT PERFORMANCE - WINNERS
| Product/Category | Revenue | ROAS | Orders | Platform | Action |
|------------------|---------|------|--------|----------|--------|
(Sorted by ROAS descending, top 10)

### PRODUCT PERFORMANCE - LOSERS
| Product/Category | Spend | ROAS | Issue | Recommendation |
|------------------|-------|------|-------|----------------|
(ROAS < 1.5x or below target, sorted by spend descending)

### CATALOG CAMPAIGN BREAKDOWN
| Campaign Type | Platform | Spend | ROAS | Top Products |
|---------------|----------|-------|------|-------------|
| Advantage+ Sales | Meta | | | |
| Shopping / PMax | Google | | | |

### OPTIMIZATION ACTIONS
1. SCALE: [Products with ROAS > target + sufficient volume]
2. PAUSE: [Products with ROAS < 1x after 50+ clicks]
3. FIX: [Products with high spend but low ROAS - bid/creative/landing page]

### BENCHMARKS
Your actual ROAS vs industry:
| Category | Your ROAS | Industry Avg | Status |
|----------|-----------|-------------|--------|

## Industry Benchmarks (Reference)
| Category | Typical ROAS |
|----------|-------------|
| Apparel | ~4.5x |
| Garden/Outdoor | ~6.7x |
| Electronics | ~3.2x |
| Beauty | ~5.1x |
| Home & Furniture | ~3.8x |
| Health & Wellness | ~4.2x |

## EXECUTION STEPS

### Step 1: Discover Accounts
- `meta_list_ad_accounts()`
- `google_ads_list_accounts()`
- `ga4_list_properties()`

### Step 2: Pull Meta Shopping Campaign Data

`meta_get_insights(account_id="FROM_STEP_1", date_preset="last_30d", level="campaign", fields=["campaign_name","spend","impressions","clicks","actions","action_values","purchase_roas","cpm","cpc","ctr"])`

Then drill into top campaigns at ad level:
`meta_get_insights(account_id="FROM_STEP_1", date_preset="last_30d", level="ad", fields=["ad_name","spend","actions","action_values","purchase_roas"], filtering=[{"field":"campaign.name","operator":"CONTAIN","value":"shopping"}])`

### Step 3: Pull Google Ads Shopping/PMax Data

`google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT campaign.name, campaign.advertising_channel_type, metrics.cost_micros, metrics.conversions, metrics.conversions_value, metrics.impressions, metrics.clicks, metrics.ctr, metrics.average_cpc FROM campaign WHERE campaign.advertising_channel_type IN ('SHOPPING', 'PERFORMANCE_MAX') AND segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC")`

For product-level data:
`google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT segments.product_item_id, segments.product_title, segments.product_type_l1, metrics.cost_micros, metrics.conversions, metrics.conversions_value, metrics.clicks, metrics.impressions FROM shopping_performance_view WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC LIMIT 50")`

### Step 4: Pull GA4 Revenue Data

`ga4_run_report(property_id="FROM_STEP_1", start_date="30daysAgo", end_date="yesterday", metrics=["totalRevenue","ecommercePurchases","averagePurchaseRevenue","transactions"], dimensions=["sessionDefaultChannelGroup"])`

For product-level:
`ga4_run_report(property_id="FROM_STEP_1", start_date="30daysAgo", end_date="yesterday", metrics=["itemRevenue","itemsPurchased","itemsViewed"], dimensions=["itemName"])`

### Step 5: Analyze

**ROAS Calculation:**
```
Product ROAS = Revenue attributed to ads / Ad spend on product
Blended ROAS = Total ad revenue / Total ad spend
Efficiency Score = ROAS * Volume Factor (orders > 10 = 1.0, 5-10 = 0.8, <5 = 0.5)
```

**Winner/Loser Thresholds:**
- Winner: ROAS > category benchmark AND orders >= 5
- Loser: ROAS < 1.5x AND spend > €100 AND clicks > 50
- Inconclusive: < 50 clicks (insufficient data)

**Cross-Platform Reconciliation:**
- Compare Meta-reported revenue vs GA4 Paid Social revenue
- Compare Google-reported conversions_value vs GA4 Paid Search revenue
- Flag if variance > 30%

### Step 6: Present Results
Follow OUTPUT FORMAT above EXACTLY. Fill all tables with real data.

## EDGE CASES
- No shopping/PMax campaigns: Analyze all campaigns with purchase conversions instead
- Zero revenue reported: Flag as tracking issue - check purchase event setup in GA4 and platform pixels
- Single platform only: Run analysis for that platform, skip cross-platform comparison
- New account (<7 days data): Note "Insufficient data for reliable ROAS analysis" and show available metrics
- Product-level data unavailable: Fall back to campaign-level analysis