---
description: "Compare two campaigns, time periods, or campaign types head-to-head. Includes statistical significance indicators for A/B tests. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Campaign Battle Report

Compare two campaigns or time periods side-by-side.

**Comparison Type:** ab_test

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### CONTESTANTS
- **A:** [Campaign/Period A Name]
- **B:** [Campaign/Period B Name]
- Period: [Date Range]

### HEAD-TO-HEAD
| Metric | A | B | Difference | Winner |
|--------|---|---|------------|--------|
| Spend | [amount] | [amount] | +/-XX% | A/B |
| Impressions | [value] | [value] | +/-XX% | A/B |
| Clicks | [value] | [value] | +/-XX% | A/B |
| CTR | X.XX% | X.XX% | +/-XX% | A/B |
| Conversions | [value] | [value] | +/-XX% | A/B |
| Conv. Rate | X.XX% | X.XX% | +/-XX% | A/B |
| CPA | [amount] | [amount] | +/-XX% | A/B |
| ROAS | X.XXx | X.XXx | +/-XX% | A/B |

### WINNER DECLARATION
**WINNER: [A or B]**
- Primary KPI ([metric]): [Winner] outperformed by XX%
- Statistical Significance: [Significant / Not Significant / Need More Data]
- Confidence Level: [High / Medium / Low]

### KEY INSIGHTS
1. [Main takeaway]
2. [Secondary insight]
3. [Unexpected finding]

### RECOMMENDED ACTIONS
1. [Action based on results]
2. [Action based on results]

### CAVEATS
- [Data quality issues, external factors, sample size notes]

## EXECUTION STEPS

### Step 1: Identify Campaigns to Compare
Ask user for campaign names/IDs and platform, or time periods.

### Step 2: Pull Campaign Data

**Meta (A/B test):** `meta_get_insights(account_id="...", level="campaign", filtering=[{"field":"campaign.name","operator":"CONTAIN","value":"CAMPAIGN_A"}], date_preset="last_30d", fields=["spend","impressions","clicks","actions","action_values","ctr","cpc","cpm","purchase_roas"])`

Repeat for Campaign B.

**Meta (period comparison):** Same campaign, different `time_range` parameters.

**Google Ads:** `google_ads_run_gaql(customer_id="...", query="SELECT campaign.name, metrics.cost_micros, metrics.impressions, metrics.clicks, metrics.conversions, metrics.conversions_value, metrics.ctr, metrics.average_cpc FROM campaign WHERE campaign.name LIKE '%CAMPAIGN_A%' AND segments.date DURING LAST_30_DAYS")`

**TikTok:** `tiktok_get_report(start_date="...", end_date="...", level="campaign", metrics=["spend","impressions","clicks","conversions","conversion_rate"])`

**LinkedIn:** `linkedin_get_analytics(account_id="...", start_date="...", end_date="...")`

### Step 3: Statistical Significance (for A/B tests)

```python
rate_a = conversions_a / clicks_a
rate_b = conversions_b / clicks_b
relative_lift = (rate_b - rate_a) / rate_a * 100

if sample_a > 100 and sample_b > 100:
    if abs(relative_lift) > 10: significance = "Likely Significant"
    else: significance = "Not Significant - Need more data"
else:
    significance = "Insufficient sample size"
```

Min sample: 100 conversions per variant for reliable results.

### Step 4: Present Results
Follow OUTPUT FORMAT above. Declare winner on primary KPI.

## EDGE CASES
- Insufficient data (<100 conversions per side): Note low confidence, don't declare winner
- Different budgets: Normalize by spend (efficiency metrics) for fair comparison
- Missing campaigns: Ask user to verify campaign names/IDs
- Cross-platform comparison: Note attribution differences between platforms
- Zero conversions on one side: Flag as clear loser, no significance test needed