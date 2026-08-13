---
description: "Analyze Google Ads auction insights to understand competitive landscape. See who you're competing against and where you're winning or losing. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** google_ads
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Competitive Auction Insights

Analyze the competitive landscape in Google Ads using auction insights data.

- Focus: all campaigns

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### Competitive Position
| Metric | Your Score | Benchmark | Status |
|--------|-----------|-----------|--------|
| Search Impression Share | XX% | 30-40% (non-brand) / 80%+ (brand) | Good/Poor |
| Top of Page Rate | XX% | 40-60% | Good/Poor |
| Absolute Top Rate | XX% | 15-25% | Good/Poor |
| Avg Outranking Share | XX% | - | - |

### Top Competitors (by overlap rate)
| Competitor | Overlap | Pos Above Rate | Outranking Share | Threat |
|------------|---------|----------------|------------------|--------|
| domain.com | XX% | XX% | XX% | HIGH/MED/LOW |

Threat level: HIGH = overlap >60% AND position above >50%. MED = overlap >40%. LOW = all others.

### Competitive Strength Score
```
Score = (Impression Share * 0.3) + (Top of Page Rate * 0.3) + (Avg Outranking Share * 0.4)
90-100: Dominant | 70-89: Strong | 50-69: Competitive | <50: Weak
```

### Recommendations
**Defensive** (protect your position):
1. [Brand protection actions]
2. [Position defense actions]

**Offensive** (gain ground):
1. [Competitor weakness to exploit]
2. [Market gap identified]

**Budget Implication:** To gain 10% more impression share: +EUR X,XXX/month estimate.

## EXECUTION STEPS

### Step 1: List accounts
```
google_ads_list_accounts()
```
Identify the target account. If user specified an account, use it directly.

### Step 2: Pull auction insights for search campaigns
```
google_ads_run_gaql(
    customer_id="CUSTOMER_ID",
    query="SELECT campaign.name, campaign.campaign_budget, metrics.search_impression_share, metrics.search_top_impression_share, metrics.search_absolute_top_impression_share, metrics.search_budget_lost_impression_share, metrics.search_rank_lost_impression_share FROM campaign WHERE campaign.advertising_channel_type = 'SEARCH' AND campaign.status = 'ENABLED' AND segments.date DURING LAST_30_DAYS ORDER BY metrics.impressions DESC LIMIT 20"
)
```

### Step 3: Pull auction insight data per top campaign
For the top 5 campaigns by spend, run:
```
google_ads_run_gaql(
    customer_id="CUSTOMER_ID",
    query="SELECT campaign.name, auction_insight.display_domain, metrics.auction_insight_search_impression_share, metrics.auction_insight_search_overlap_rate, metrics.auction_insight_search_position_above_rate, metrics.auction_insight_search_top_impression_percentage, metrics.auction_insight_search_absolute_top_impression_percentage, metrics.auction_insight_search_outranking_share FROM auction_insight WHERE segments.date DURING LAST_30_DAYS AND campaign.campaign_id = CAMPAIGN_ID"
)
```

> Conditional: if focus_campaign_type == "brand"

Filter to campaigns with brand terms (campaign name contains "brand", "branded", or the company name).

> Otherwise, if focus_campaign_type == "non_brand"

Exclude campaigns with brand terms.

> Otherwise, if focus_campaign_type == "shopping"

Use `campaign.advertising_channel_type = 'SHOPPING'` instead of SEARCH in queries.

### Step 4: Analyze and score
- Calculate Competitive Strength Score per the formula above
- Rank competitors by threat level
- Identify brand vs non-brand competitive dynamics
- Compare impression share lost to budget vs rank (budget = increase spend, rank = improve ads/bids)

### Step 5: Generate recommendations
- If impression share lost to budget >20%: recommend budget increase
- If impression share lost to rank >20%: recommend bid strategy or ad quality improvements
- If a competitor has position above rate >60%: flag as primary threat
- Calculate estimated budget needed for 10% impression share gain using current CPC data

## EDGE CASES
- **No search campaigns found**: Report that no active search campaigns exist; suggest creating search campaigns before running this analysis
- **Low impression share (<5%)**: Account is barely competing; focus recommendations on budget and ad quality fundamentals rather than competitor analysis
- **No competitors returned**: Campaign may have very niche targeting or low volume; auction insights require sufficient impressions to populate
- **Shopping campaigns**: Use SHOPPING channel type; auction insights structure is similar but metrics context differs (price competitiveness matters more)
- **Smart/PMax campaigns**: Auction insights are not available for Performance Max; note this limitation and analyze only standard Search/Shopping campaigns