---
description: "Get a 0-100 health score for each account with prioritized issue list and quick win recommendations. Perfect for managing large portfolios. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Account Health Scoring

Calculate health scores (0-100) and prioritize accounts needing attention.

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### PORTFOLIO SUMMARY
- Total Accounts: [X] | Average Score: [XX]
- Excellent (80+): [X] | Good (60-79): [X] | Needs Attention (40-59): [X] | Critical (<40): [X]

### HEALTH SCORE RANKINGS
| Rank | Account | Platform | Score | Status | Top Issue |
|------|---------|----------|-------|--------|-----------|
| 1 | [name] | [platform] | XX | Excellent/Good/Attention/Critical | [issue or "None"] |

### CRITICAL ACCOUNTS (Score <40)
For each:
- **Issues:** [list with points lost per issue]
- **Quick Wins:** [actions that could improve score by X points]
- **Est. Revenue Impact:** [amount if fixed]

### PORTFOLIO INSIGHTS
- Health score trend: [improving/stable/declining]
- Most common issue: [issue affecting most accounts]
- Estimated total revenue impact of fixes: [amount]

## EXECUTION STEPS

### Step 1: Discover All Accounts
- `meta_list_ad_accounts()`
- `google_ads_list_accounts()`
- `linkedin_list_ad_accounts()`
- `tiktok_get_advertiser_info()`

### Step 2: Pull Performance Data (last 30 days + previous 30 days)

**Meta:** `meta_get_insights(account_id="...", date_preset="last_30d", level="account", fields=["spend","impressions","clicks","actions","action_values","purchase_roas","frequency","cpm","cpc","ctr"])`

**Google Ads:** `google_ads_run_gaql(customer_id="...", query="SELECT metrics.cost_micros, metrics.impressions, metrics.clicks, metrics.conversions, metrics.conversions_value, metrics.search_impression_share FROM customer WHERE segments.date DURING LAST_30_DAYS")`

**TikTok:** `tiktok_get_report(start_date="30_DAYS_AGO", end_date="TODAY", level="account")`

**LinkedIn:** `linkedin_get_analytics(account_id="...", start_date="30_DAYS_AGO", end_date="TODAY")`

### Step 3: Calculate Health Score (5 components)

| Component | Weight | Scoring |
|-----------|--------|---------|
| Performance vs Target | 30% | ROAS/CPA within target = 30, deviation reduces |
| Budget Efficiency | 20% | Proper pacing = 20, over/underspend reduces |
| Account Structure | 15% | Clean structure = 15, issues reduce |
| Creative Health | 15% | Fresh creatives = 15, fatigue reduces |
| Trend Direction | 20% | Improving WoW = 20, stable = 15, declining = 5 |

**Score interpretation:** 80-100: Excellent | 60-79: Good | 40-59: Needs Attention | 0-39: Critical

### Step 4: Present Results
Follow OUTPUT FORMAT above. Sort by score ascending (worst first for action priority).

## EDGE CASES
- Single account: Still score it, compare to platform benchmarks instead of portfolio
- New account (<7 days): Score as "Insufficient Data", exclude from portfolio average
- No conversion tracking: Skip Performance component, weight others proportionally
- Account with zero spend: Flag as inactive, exclude from scoring
- API error on a platform: Score remaining accounts, note the error