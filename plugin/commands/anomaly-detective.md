---
description: "Automatically detect unusual performance shifts across all accounts with severity levels, budget impact estimation, vertical seasonality context, and action urgency indicators. Catches issues before they become expensive problems. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Anomaly Detective

Scan all accounts for unusual performance anomalies. Sensitivity: medium.

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### EXECUTIVE SUMMARY
| Severity | Count | Daily Budget at Risk |
|----------|-------|---------------------|
| CRITICAL | | |
| HIGH | | |
| MEDIUM | | |
| LOW | | |
| **Total Weekly Impact if Unaddressed** | | **amount** |

### CRITICAL - ACT NOW (0-4 hours)
For each:
| Account | Platform | Anomaly | Change | Daily Impact | Root Cause | Action |
|---------|----------|---------|--------|-------------|------------|--------|

### HIGH - ACT TODAY (4-24 hours)
Same table format as CRITICAL.

### MEDIUM - MONITOR (24-48 hours)
| Account | Platform | Anomaly | Change | Seasonal? | Recommendation |
|---------|----------|---------|--------|-----------|----------------|

### LOW - REVIEW THIS WEEK
Bullet list: [Account]: [metric] [change]% - [context]

### SEASONALITY CONTEXT
| Account | Anomaly | Seasonal? | Confidence | Expected Pattern |
|---------|---------|-----------|------------|-----------------|
(Mark: YES = don't panic | MAYBE = monitor | NO = investigate)

### INVESTIGATION CHECKLISTS
**Conversion drops:** Pixel/tag firing? Landing page loading? Checkout flow? Payment processing? Ad disapprovals?
**Spend spikes:** Budget caps? Bid strategy? Bid limits? Audience expansion?

### NO ANOMALIES
[List accounts with stable performance - GREEN status]

## EXECUTION STEPS

### Step 1: Discover Accounts
- `meta_list_ad_accounts()`
- `google_ads_list_accounts()`
- `linkedin_list_ad_accounts()`
- `tiktok_get_advertiser_info()`

### Step 2: Pull Time-Series Data (Last 14 Days, Daily Granularity)

**Meta:** `meta_get_insights(account_id="FROM_STEP_1", date_preset="last_14d", level="account", fields=["spend","impressions","clicks","actions","action_values","cpm","cpc","ctr","purchase_roas"], time_increment=1)`

**Google Ads:** `google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT segments.date, metrics.impressions, metrics.clicks, metrics.ctr, metrics.average_cpc, metrics.cost_micros, metrics.conversions, metrics.conversions_value FROM customer WHERE segments.date DURING LAST_14_DAYS ORDER BY segments.date DESC")`

**TikTok:** `tiktok_get_report(start_date="14_DAYS_AGO", end_date="YESTERDAY", level="campaign", metrics=["spend","impressions","clicks","conversions","conversion_rate","cpc","cpm"], group_by="stat_time_day")`

**LinkedIn:** `linkedin_get_analytics(account_id="FROM_STEP_1", start_date="14_DAYS_AGO", end_date="YESTERDAY", fields=["impressions","clicks","costInLocalCurrency","externalWebsiteConversions"])`

### Step 3: Detect Anomalies

**Baseline:** 7-day rolling average (same day-of-week when possible). Minimum 20 impressions to avoid noise.

**Alert thresholds by sensitivity (medium):**

| Alert Type | LOW sens. | MEDIUM sens. | HIGH sens. |
|------------|-----------|--------------|------------|
| Spend Spike | >200% | >150% | >120% |
| Conversion Drop | >50% | >30% | >20% |
| CPC Anomaly | >40% | >25% | >15% |
| Impression Loss | >60% | >40% | >25% |
| CTR Drop | >35% | >20% | >15% |

**Severity assignment:**

| Level | Criteria | Urgency | Budget Impact |
|-------|----------|---------|---------------|
| CRITICAL | >200% deviation OR conversions = 0 | ACT NOW (0-4h) | >500/day |
| HIGH | >100% deviation OR core metric collapse | ACT TODAY (4-24h) | 100-500/day |
| MEDIUM | >50% deviation | MONITOR (24-48h) | 50-100/day |
| LOW | >25% deviation | REVIEW (this week) | <50/day |

**Budget impact estimation:**
- Spend anomaly: daily_impact = abs(current_spend - baseline_spend)
- Conversion anomaly: daily_impact = abs(change_pct) * daily_spend * 0.01
- Efficiency anomaly: daily_impact = daily_spend * abs(change_pct) * 0.005

### Step 4: Seasonality Check

Before flagging, check against vertical patterns:

**E-commerce:** Nov BFCM +100-300% (normal), Dec holiday +50-100%, Jan post-holiday -40-60%
**B2B/SaaS:** Q1 +30-50% (new budgets), Aug -30-40% (summer), Dec 20-Jan 5 -50-70%
**Travel:** Jul-Aug +40-80% (summer peak), Jan -30-50%, Dec 15-25 -40%
**Education:** Aug-Sep +60-100% (enrollment), Jun-Jul -40-60%
**Healthcare:** Jan +50-100% (resolutions), Sep +20-30% (back-to-routine)

Mark each anomaly: YES (seasonal, high confidence) | MAYBE (possible, monitor) | NO (investigate)

### Step 5: Present Results
Follow OUTPUT FORMAT above EXACTLY. Include all tables with real data.

## EDGE CASES
- No data for a platform: Skip it, note "No data available for [platform]"
- Account with <3 days of data: Exclude from anomaly detection, note "Insufficient history"
- All metrics are 0: Flag as CRITICAL - potential tracking failure, not a normal anomaly
- Weekday vs weekend variance: Use same-day-of-week baseline to avoid false positives
- Multiple anomalies on same account: List all, but group under the highest severity
- API error on one platform: Note the error, continue with remaining platforms