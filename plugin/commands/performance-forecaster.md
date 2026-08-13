---
description: "Predicts future campaign performance using historical platform data, seasonality patterns, and trend analysis. Uses Monte Carlo-style uncertainty modeling to provide confidence intervals for projected spend, conversions, and ROAS. Helps set realistic expectations and plan for multiple scenarios. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# AI-Powered Performance Forecasting

Generate performance forecasts with confidence intervals for [specify company_name] ([specify industry]).

**Forecast Period:** Next 90 days
**Monthly Budget:** EUR10,000

> Conditional: if meta_account_id
**Meta Account:** [specify meta_account_id]

> Conditional: if google_ads_customer_id
**Google Ads:** [specify google_ads_customer_id]

> Conditional: if ga4_property_id
**GA4 Property:** [specify ga4_property_id]

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### EXECUTIVE SUMMARY
| Metric | Projection | 70% Confidence Range |
|--------|------------|---------------------|
| Total Spend | [planned amount] | Fixed |
| Conversions | [expected] | [low] - [high] |
| Revenue | [expected] | [low] - [high] |
| Blended ROAS | [expected]x | [low]x - [high]x |
| Avg CPA | [expected] | [low] - [high] |

**Forecast Confidence:** [High/Medium/Low]

### MONTHLY BREAKDOWN
| Month | Budget | Conversions (P/E/O) | ROAS (P/E/O) | Seasonality |
|-------|--------|--------------------|--------------| ------------|
| M1 | [amount] | [low]/[exp]/[high] | [low]/[exp]/[high]x | [index] |
| M2 | [amount] | [low]/[exp]/[high] | [low]/[exp]/[high]x | [index] |
| M3 | [amount] | [low]/[exp]/[high] | [low]/[exp]/[high]x | [index] |
P=Pessimistic (10th %ile), E=Expected (50th), O=Optimistic (90th)

### SCENARIO SUMMARY
| Scenario | Probability | Conversions | Revenue | ROAS |
|----------|------------|-------------|---------|------|
| Downside | 15% | [low] | [low] | [low]x |
| Base Case | 60% | [expected] | [expected] | [exp]x |
| Upside | 25% | [high] | [high] | [high]x |

**Expected Value:** EV = (0.15 x Low) + (0.60 x Expected) + (0.25 x High)

### KEY RISKS
| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|-----------|

### RECOMMENDATIONS
1. Set targets at Expected Case level
2. Build [X%] contingency for downside
3. Trigger optimization reviews if hitting downside range
4. Weekly: check pacing vs forecast | Monthly: full refresh

## EXECUTION STEPS

### Step 1: Collect Historical Data (last 90 days)

**Meta:** `meta_get_insights(account_id="FROM_DISCOVERY", date_preset="last_90d", level="account", time_increment="1", fields=["spend","impressions","clicks","conversions","purchase_roas"])`

**Google Ads:** `google_ads_run_gaql(customer_id="FROM_DISCOVERY", query="SELECT segments.date, metrics.cost_micros, metrics.impressions, metrics.clicks, metrics.conversions, metrics.conversions_value FROM customer WHERE segments.date DURING LAST_90_DAYS ORDER BY segments.date")`

**GA4:** `ga4_run_report(property_id="FROM_DISCOVERY", start_date="90daysAgo", end_date="yesterday", metrics=["sessions","conversions","totalRevenue"], dimensions=["date","sessionDefaultChannelGroup"])`

**TikTok:** `tiktok_get_report(start_date="90_DAYS_AGO", end_date="TODAY", level="campaign", metrics=["spend","impressions","clicks","conversions"])`

**LinkedIn:** `linkedin_get_analytics(account_id="FROM_DISCOVERY", start_date="90_DAYS_AGO", end_date="TODAY")`

If accounts not connected, request manual historical data (spend, conversions, revenue, ROAS for last 30/60/90 days).

### Step 2: Trend Analysis

Calculate 90-day and 30-day trends for: Spend Efficiency, Conversion Rate, ROAS, CPM, CPC.

**Trend classification and forecast impact:**
| Trend | Definition | Forecast Adjustment |
|-------|-----------|-------------------|
| Strong Uptrend | +15%+ | +10% to base |
| Moderate Uptrend | +5 to +15% | +5% to base |
| Stable | -5 to +5% | Use base |
| Moderate Downtrend | -5 to -15% | -5% from base |
| Strong Downtrend | -15%+ | -10% from base |

**Platform variability factors:**
| Factor | Meta | Google | LinkedIn | TikTok |
|--------|------|--------|----------|--------|
| Algorithm changes | Medium | Low | Low | High |
| Privacy impact | High | Medium | Low | Medium |
| Creative fatigue | High | Low | Low | Very High |

### Step 3: Apply Seasonality

**Monthly performance multipliers (adjust for [specify industry]):**
| Month | Index | Notes |
|-------|-------|-------|
| Jan | 0.85 | Post-holiday lull |
| Feb-Mar | 0.90-0.95 | Recovery/spring ramp |
| Apr-May | 1.00 | Baseline |
| Jun-Aug | 0.85-0.95 | Summer slowdown |
| Sep-Oct | 1.05-1.10 | Back-to-business, pre-holiday |
| Nov | 1.25 | Black Friday (CPMs +50-100%) |
| Dec | 1.15 | Holiday peak then drop |

Index: 1.00 = baseline, 0.90 = 10% below, 1.20 = 20% above.

### Step 4: Uncertainty Modeling

**Confidence intervals by metric:**
| Metric | 10th %ile | 50th (Base) | 90th %ile |
|--------|----------|-------------|----------|
| CPM | Base x 0.80 | Historical avg | Base x 1.30 |
| CTR | Base x 0.85 | Historical avg | Base x 1.15 |
| CVR | Base x 0.70 | Historical avg | Base x 1.40 |
| CPA | Base x 0.75 | Historical avg | Base x 1.50 |
| ROAS | Base x 0.60 | Historical avg | Base x 1.50 |

**Platform forecast uncertainty:**
Google Search: Low (+/-15%, stable intent-based) | Meta: Medium (+/-25%, algorithm + creative) | LinkedIn: Medium (+/-20%, B2B volatility) | TikTok: High (+/-35%, creative fatigue + trends)

### Step 5: Build Forecast

**Base formula:**
```
Conversions = (Historical Daily Avg x Days) x Seasonality x Trend Factor
ROAS = Historical ROAS x Trend Factor x (1 - Platform Uncertainty)
Revenue = Budget x ROAS
```

**Three scenarios:**
- **Base Case (60%):** Current trends continue, consistent budget, normal seasonality
- **Upside (25%):** Creative testing wins, algorithm favorability, strong seasonal performance
- **Downside (15%):** Creative fatigue, CPM inflation, competitive pressure increases

**Forecast accuracy expectations:** 30 days: +/-15-20% | 60 days: +/-20-30% | 90 days: +/-25-35% | 180 days: +/-35-50%

### Step 6: Present Results
Follow OUTPUT FORMAT above. Always present ranges, never single-point estimates. Explain confidence level based on data quality.

## EDGE CASES
- No platform accounts connected: Use manual historical data + industry benchmarks
- Less than 30 days of data: Widen confidence intervals by 50%, note reduced accuracy
- All metrics are 0: Flag tracking issue, provide benchmark-only forecast
- Single platform only: Forecast that platform, note inability to cross-validate
- Major platform change during historical period: Exclude pre-change data, note shorter baseline
- API error: Note the error, forecast with available data, widen uncertainty