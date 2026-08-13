---
description: "Discover new keyword opportunities in Google Ads. Analyze search terms, find gaps, and get bid recommendations. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** google_ads
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Keyword Opportunity Finder

Discover keyword opportunities in Google Ads campaigns.

> Conditional: if focus_campaign
**Focus Campaign:** [specify focus_campaign]

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### SEARCH TERM GOLD MINES
Converting search terms not yet added as keywords:
| Search Term | Clicks | Conv | Conv Rate | Cost | Recommended Match |
|-------------|--------|------|-----------|------|-------------------|
Potential impact: +XX conversions/month if added

### IMPRESSION SHARE OPPORTUNITIES
Keywords losing impression share to budget:
| Keyword | IS Lost (Budget) | Avg CPC | Conv | Recommendation |
|---------|-----------------|---------|------|---------------|
Estimated opportunity: [amount] additional revenue if captured

### QUALITY SCORE IMPROVEMENTS
Low QS keywords with good conversion rates:
| Keyword | QS | Conv Rate | Issue | Fix |
|---------|-----|-----------|-------|-----|
Estimated CPC savings: XX% if QS improved to 7+

### NEGATIVE KEYWORD RECOMMENDATIONS
| Search Term | Clicks | Spend | Conv | Action |
|-------------|--------|-------|------|--------|
Estimated monthly savings: [amount]

### ACTION SUMMARY
1. Add [X] converting search terms as keywords
2. Exclude [X] irrelevant terms (save [amount]/mo)
3. Increase budget for [X] high-opportunity keywords
4. Improve landing pages for [X] low-QS keywords

## EXECUTION STEPS

### Step 1: Discover Accounts
`google_ads_list_accounts()`

### Step 2: Pull Search Term Report
```
google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT search_term_view.search_term, search_term_view.status, metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions, metrics.conversions_value FROM search_term_view WHERE segments.date DURING LAST_30_DAYS AND metrics.impressions > 10 ORDER BY metrics.conversions DESC LIMIT 200")
```

### Step 3: Pull Keyword Performance with Quality Scores
```
google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type, ad_group_criterion.quality_info.quality_score, metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions, metrics.search_impression_share, metrics.search_rank_lost_impression_share, metrics.search_budget_lost_impression_share FROM keyword_view WHERE segments.date DURING LAST_30_DAYS AND ad_group_criterion.status = 'ENABLED' ORDER BY metrics.cost_micros DESC LIMIT 200")
```

### Step 4: Identify Opportunities

**Converting search terms:** Terms with conversions > 0 and status != ADDED
**Impression share gaps:** Keywords with search_budget_lost_impression_share > 10%
**QS improvements:** Keywords with quality_score < 6 and conversion_rate > 2%
**Negative keywords:** Terms with clicks > 5, spend > 0, conversions = 0

### Step 5: Present Results
Follow OUTPUT FORMAT above. Prioritize by estimated revenue impact.

## EDGE CASES
- No search campaigns: Note this workflow requires Search campaigns, suggest creating one
- Low volume (<1000 impressions total): Note small data set, widen analysis period to 60-90 days
- No converting search terms: Focus on negative keyword savings and impression share gaps
- Smart campaigns without search term data: Note limited visibility, recommend upgrading to Standard
- API error: Note the error, suggest checking account access