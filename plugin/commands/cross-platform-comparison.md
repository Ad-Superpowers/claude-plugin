---
description: "Compare advertising performance across Meta, Google, LinkedIn, and TikTok with attribution reconciliation, incrementality analysis, and competitive context. Includes expected discrepancy ranges, 'which number to trust' guidance, iROAS framework (incremental ROAS estimates by platform), MMM-lite recommendations, privacy-adjusted confidence framework, specific budget reallocation recommendations, reach/frequency analysis, EU vs US benchmarks, and optional competitive position analysis via Google Ads auction insights. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Cross-Platform Performance Comparison

Compare performance across all connected ad platforms for last 30 days, rank by ROAS, and recommend budget reallocations.

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### PLATFORM OVERVIEW
| Platform | Spend | % Budget | Convs | CPA | ROAS | Rank |
|----------|-------|----------|-------|-----|------|------|

### ATTRIBUTION RECONCILIATION
| Platform | Platform Convs | GA4 Convs | Variance | Status |
|----------|----------------|-----------|----------|--------|
(Normal: Meta <30%, Google <25%, TikTok <40%, LinkedIn <35%)

### WHICH NUMBER TO TRUST
| Use Case | Source | Why |
|----------|--------|-----|
| Single platform optimization | Platform data | Algorithm optimizes on its own signals |
| Cross-channel budget moves | GA4 (adjust +25-35%) | Consistent attribution model |
| Stakeholder reporting | GA4 | Consistency builds trust |

### BUDGET REALLOCATION
| Platform | Current | Recommended | Change | Confidence |
|----------|---------|-------------|--------|------------|
Confidence: HIGH (1000+ convs, >25% diff) | MEDIUM (100-999 convs) | LOW (<100 convs)

### NEXT STEPS
1. [Highest confidence reallocation]
2. [Second priority]
3. [Validation recommendation]

## EXECUTION STEPS

### Step 1: Discover Accounts
- `meta_list_ad_accounts()`
- `google_ads_list_accounts()`
- `linkedin_list_ad_accounts()`
- `tiktok_get_advertiser_info()`
- `ga4_list_properties()`

### Step 2: Gather Data

**Meta:** `meta_get_insights(account_id="FROM_STEP_1", date_preset="last_30d", level="account", fields=["spend","impressions","reach","frequency","clicks","actions","action_values","cpm","cpc","ctr","purchase_roas"])`

**Google Ads:** `google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT campaign.name, metrics.impressions, metrics.clicks, metrics.ctr, metrics.average_cpc, metrics.cost_micros, metrics.conversions, metrics.conversions_value FROM campaign WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC")`

**TikTok:** `tiktok_get_report(start_date="YYYY-MM-DD", end_date="YYYY-MM-DD", level="campaign", metrics=["spend","impressions","reach","frequency","clicks","conversions"])`

**LinkedIn:** `linkedin_get_analytics(account_id="FROM_STEP_1", start_date="YYYY-MM-DD", end_date="YYYY-MM-DD", fields=["impressions","clicks","costInLocalCurrency","externalWebsiteConversions"])`

**GA4:** `ga4_run_report(property_id="FROM_STEP_1", start_date="30daysAgo", end_date="yesterday", metrics=["conversions","totalRevenue"], dimensions=["sessionDefaultChannelGroup"])`

**Auction Insights (optional):** `google_ads_run_gaql(customer_id="...", query="SELECT campaign.name, segments.auction_insight_domain, metrics.auction_insight_search_impression_share, metrics.auction_insight_search_outranking_share FROM auction_insight WHERE segments.date DURING LAST_30_DAYS LIMIT 15")`

### Step 3: Analyze

**Attribution windows** (platforms count differently):
Meta: 7d click + 1d view | Google: Data-driven | TikTok: 7d click + 1d view | LinkedIn: 30d click + 7d view | GA4: Cross-channel DDA (underreports 18-35%)

**Expected discrepancies vs GA4:**
| Comparison | Normal Range | Primary Cause |
|-----------|-------------|---------------|
| Meta vs GA4 | Meta +15-30% | View-through + modeled conversions |
| Google vs GA4 | Google +10-25% | Enhanced Conversions + modeling |
| TikTok vs GA4 | TikTok +20-40% | VTA attribution (30% of convs) |
| LinkedIn vs GA4 | LinkedIn +15-35% | Long B2B cycles, cross-device |

If variance exceeds ranges: investigate pixel firing, CAPI, event dedup, UTMs, Consent Mode V2.

**Incrementality estimates (iROAS = true causal impact):**
| Campaign Type | Reported ROAS | Incrementality | Est. iROAS |
|--------------|--------------|---------------|-----------|
| Meta Retargeting | 8-15x | 30-50% | 2.4-7.5x |
| Meta Prospecting | 3-6x | 60-80% | 1.8-4.8x |
| Google Brand | 10-30x | 10-30% | 1-9x |
| Google Generic | 4-8x | 70-90% | 2.8-7.2x |
| TikTok | 3-6x | 65-85% | 2-5.1x |
| LinkedIn | 2-4x | 75-90% | 1.5-3.6x |

Key: Retargeting/brand search = HIGH ROAS but LOW incrementality.

**Reallocation caveats:**
- Meta ROAS appears lower in GA4 (VTA undercount) - adjust +20%
- LinkedIn ROI undervalued (long B2B cycles, 30d attribution)
- TikTok upper-funnel contribution often uncredited

**Measurement by spend:** <5K: Platform + GA4 | 5-25K: Geo lift tests quarterly | 25-100K: Lift tests + simple MMM | 100K+: Full MMM + continuous testing

**EU privacy:** Cookie consent ~50% (vs 78% US on Meta). Expect 20-35% signal loss. Server-side tracking recovers ~70%.

### Step 4: Present Results
Follow OUTPUT FORMAT above EXACTLY. Include all tables with real data.

## EDGE CASES
- No data for a platform: Skip it, note "No data available"
- Only 1 account connected: Single-platform view with GA4 comparison
- All metrics are 0: Flag as potential tracking issue
- API error: Note the error, continue with remaining platforms
- GA4 not connected: Skip reconciliation, compare using relative efficiency
- Variance >50% on any platform: Flag critical tracking issue requiring investigation