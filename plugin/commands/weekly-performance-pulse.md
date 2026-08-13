---
description: "A deterministic weekly account-performance summary for Meta Ads and Google Ads."
disable-model-invocation: true
---

> **Platforms:** meta, google_ads
> **Tier:** free
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Weekly Performance Pulse

Create a weekly performance summary for one connected account per platform using only observed Meta Ads and Google Ads data.

## EXECUTION STEPS

This workflow supplies a client-directed plan; it does not provide a server-side runtime executor. Run exactly these four calls in order for the baseline run. Select at most one account per platform, and do not paginate or retry a call in the baseline run.

### Step 1: Discover one account per platform

```
meta_list_ad_accounts()
google_ads_list_accounts()
```

Choose at most one available account for Meta and one available customer for Google Ads. If a source has no available account or its discovery call fails, record that source as unavailable and continue with the other source.

### Step 2: Gather the 14 daily observations

**Meta Ads**
```
meta_get_insights(
    account_id="FROM_STEP_1",
    date_preset="last_14d",
    time_increment="1",
    level="account",
    fields=["spend", "impressions", "clicks", "actions", "action_values", "cpm", "cpc", "ctr", "purchase_roas"]
)
```

**Google Ads**
```
google_ads_run_gaql(
    customer_id="FROM_STEP_1",
    query="SELECT segments.date, metrics.cost_micros, metrics.impressions, metrics.clicks, metrics.conversions, metrics.conversions_value FROM customer WHERE segments.date DURING LAST_14_DAYS ORDER BY segments.date DESC"
)
```

## OUTPUT FORMAT

### TL;DR
Give a concise, evidence-based summary of the available sources. Do not invent metrics, values, currencies, conversions, or causes.

### Platform views
For each available platform, report only returned metrics and identify the selected account. Keep Meta `actions` and Google Ads `conversions` in separate platform views; do not aggregate conversion types across platforms. Do not aggregate monetary values across currencies.

### Week-over-week comparison
Calculate week-over-week changes only when a source returned a complete 14-day daily series that divides into two complete seven-day halves. Otherwise, omit the comparison for that source and state why.

### Sources used
List each source by platform, account, period, and daily granularity.
Cite the relevant entry from **Sources used** for every conclusion and recommendation.

### Incomplete coverage
List unavailable sources, missing dates, failed calls, and omitted metrics. Omit absent metrics from all other sections rather than estimating them.

### Recommended next actions
Offer up to four evidence-based actions, clearly labelled as recommendations. These are not runtime actions and no action has been executed by this workflow.

## EDGE CASES

- If both sources are unavailable, report the unavailable sources and request a rerun; do not produce performance claims.
- If only one source is available, provide only that platform's view without cross-platform comparisons.
- If a metric, currency, conversion definition, or date is absent, omit it and explain the gap in **Incomplete coverage**.
- If the daily series is incomplete, show available absolute observations but do not calculate week-over-week change.