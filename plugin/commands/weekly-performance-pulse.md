---
description: Quick weekly summary with platform-specific insights. Includes TL;DR, top wins, concerns, and platform-appropriate benchmarks (TikTok creative health, LinkedIn CPL vs industry, etc.).
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** free
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Weekly Performance Pulse

Generate a quick weekly performance summary for all connected accounts.

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### TL;DR (Copy-Paste Ready for Slack/Email)
1-2 sentence summary, max 280 characters. Examples:
- "Good week: +15% more sales from ads. One thing to fix: TikTok ads are getting stale (refresh needed). LinkedIn leads cost €X — that's healthy."
- "Flat week across platforms. No fires, but TikTok creatives need a refresh before next week."

### #1 Priority — If You Do ONE Thing This Week
Single most impactful action in plain language. Example:
"Refresh your TikTok creatives — they're 8 days old (TikTok ads work best when refreshed every 5-7 days). This could save you €XX-XX/week."
If all good: "No urgent actions. Consider testing new ad creative."

### The Numbers (Plain English)
- Spent this week: €X,XXX (vs €X,XXX last week = up/down X%)
- Results: XXX conversions (up/down X% vs last week)
- Cost per result: €XX (better/worse than last week's €XX)
- Return on ad spend: €X.XX back for every €1 spent (up/down)

### Platform Quick View

| Platform | Spent | Results | How It's Going | vs Last Week |
|----------|-------|---------|----------------|--------------|
| Meta | €X,XXX | XXX | Great/OK/Needs work | +/-XX% |
| Google | €X,XXX | XXX | Great/OK/Needs work | +/-XX% |
| TikTok | €X,XXX | XXX | Great/OK/Needs work | +/-XX% |
| LinkedIn | €X,XXX | XX | Great/OK/Needs work | +/-XX% |

### Platform-Specific Notes
Only show if relevant — plain language explanations per platform with: what's happening, what it means, and what to do about it.

### This Week's Wins
1-3 specific wins with numbers in plain language. Example: "Meta ads: 20% more sales than last week — new creative is working!"

### Things to Improve
1-3 items, each with: [Platform]: [Plain language issue] — Fix: [specific action]

### This Week's To-Do List
Priority order (do first one first):
- [ ] Most important action (usually TikTok if ads are old)
- [ ] Second action
- [ ] Third action
- [ ] Nice to have if time allows

### Share This Summary
- For Slack/Teams: Copy the TL;DR section
- For email: Copy "The Numbers" section

## EXECUTION STEPS

### Step 1: Discover Accounts
Use `meta_list_ad_accounts`, `google_ads_list_accounts`, `tiktok_query`, `linkedin_list_ad_accounts` to find all connected accounts.

### Step 2: Pull This Week's Data

**Meta Ads:**
```
meta_get_insights(
    account_id=account_id,
    date_preset="last_7d",
    level="account",
    fields=["spend", "impressions", "clicks", "actions", "action_values", "cpm", "cpc", "ctr", "purchase_roas"]
)
```

**Google Ads:**
```
google_ads_run_gaql(
    customer_id=customer_id,
    query="SELECT campaign.id, campaign.name, campaign.status,
        metrics.impressions, metrics.clicks, metrics.ctr,
        metrics.average_cpc, metrics.cost_micros,
        metrics.conversions, metrics.conversions_value
    FROM campaign WHERE segments.date DURING LAST_7_DAYS
    ORDER BY metrics.cost_micros DESC"
)
```

**TikTok Ads:**
```
tiktok_get_report(
    date_range="last 7 days",
    level="campaign",
    metrics=["spend", "impressions", "clicks", "conversions", "cpc", "cpm", "ctr", "conversion_rate"]
)
```

**LinkedIn Ads:**
```
linkedin_get_analytics(
    account_id=account_id,
    date_range="last 7 days",
    time_granularity="ALL",
    fields=["impressions", "clicks", "costInLocalCurrency", "externalWebsiteConversions"]
)
```

### Step 3: Compare Week-over-Week
Calculate WoW changes for all metrics. Pull previous week data using same tool calls with adjusted date ranges. Flag any metric change >10% with a clear indicator.

### Step 4: Platform-Specific Health Checks

**TikTok (check first — fastest fatigue):**
- Creative age: Any ads >5 days? Flag for refresh
- CTR trend over 3 days: Declining >15%? Fatigue signal
- Hook performance: 2-second view rate (target >50%)

**Meta:**
- Frequency: Prospecting >3/week? Monitor closely
- Creative age: Any ads >14 days? Plan refresh

**LinkedIn (B2B context):**
- CPL vs industry benchmark (SaaS: €80-120, Finance: €90-120)
- Long sales cycles — don't judge too quickly

**Google Ads:**
- Quality Score changes
- Impression share trends

Platform-specific context matters: TikTok changes are more urgent (faster fatigue). Keep recommendations actionable and specific.

### Step 5: Present Results
Follow the OUTPUT FORMAT above exactly. Populate all sections with real data. Omit platform sections for platforms the user has no accounts on.

## EDGE CASES
- **First week (no comparison data):** Skip WoW comparisons, present absolute numbers only, note "First week of tracking — comparisons available next week"
- **Single platform only:** Skip cross-platform overview, provide deeper single-platform analysis instead
- **All metrics flat (<3% change):** Note stability positively, suggest proactive experiments (new creative tests, audience expansions)
- **Major holiday week:** Note the context — "This was [holiday] week, so lower/higher volume is expected. Compare to same week last year if possible."
- **Platform outage during period:** Note which platform had incomplete data and for which dates, present available data with caveat