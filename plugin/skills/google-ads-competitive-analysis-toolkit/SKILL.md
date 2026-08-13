---
name: google-ads-competitive-analysis-toolkit
description: "This skill should be used when the user asks to \"analyze Auction Insights\", \"monitor competitor strategies\", \"calculate market share in Google Ads\", \"build a competitive response plan\", or mentions \"Share of Voice\", \"impression share analysis\", or \"competitor bidding\". Do NOT use for: keyword strategy (use keyword-strategy-planner), bid strategy selection (use bid-strategy-selector), or campaign performance diagnosis (use performance-troubleshooter)."
---
# Competitive Analysis Toolkit

Complete guide for analyzing competition in Google Ads, from Auction Insights interpretation to strategic response to competitor activities.

## Pull Competitive Data via MCP

### Impression Share Metrics (Campaign Level)

```
google_ads_run_gaql(query="
  SELECT campaign.name,
         metrics.search_impression_share,
         metrics.search_budget_lost_impression_share,
         metrics.search_rank_lost_impression_share,
         metrics.search_absolute_top_impression_share,
         metrics.search_top_impression_share,
         metrics.average_cpc, metrics.cost_micros
  FROM campaign
  WHERE segments.date DURING LAST_30_DAYS
    AND campaign.status = 'ENABLED'
    AND campaign.advertising_channel_type = 'SEARCH'
  ORDER BY metrics.cost_micros DESC
  LIMIT 20
")
```

Interpret:
- `search_rank_lost_impression_share` rising → competitors increasing bids/QS
- `search_budget_lost_impression_share` rising → you are budget-capped
- `search_absolute_top_impression_share` dropping → someone pushed you down

### Auction Insights (Competitor Domain Data)

The `auction_insight` resource provides per-competitor overlap, position above, and outranking metrics via GAQL:

```
google_ads_run_gaql(query="
  SELECT auction_insight.display_domain,
         metrics.auction_insight_search_impression_share,
         metrics.auction_insight_search_overlap_rate,
         metrics.auction_insight_search_position_above_rate,
         metrics.auction_insight_search_outranking_share,
         metrics.auction_insight_search_top_impression_percentage,
         metrics.auction_insight_search_absolute_top_impression_percentage
  FROM auction_insight
  WHERE segments.date DURING LAST_30_DAYS
  ORDER BY metrics.auction_insight_search_impression_share DESC
  LIMIT 20
")
```

This returns the same data as the UI's Auction Insights report, including competitor domain names. Filter by campaign or ad group for segment-specific analysis.

## Auction Insights Metrics

| Metric | What It Measures |
|--------|------------------|
| Impression Share | % of impressions you received vs total available |
| Overlap Rate | % of your impressions where competitor also appeared |
| Position Above Rate | % of overlapping impressions where competitor was above you |
| Top of Page Rate | % of impressions in top positions (above organic) |
| Abs. Top of Page Rate | % of impressions at first position |
| Outranking Share | % of auctions where you ranked above competitor or appeared when they didn't |

Outranking Share = (You higher + You appeared, they didn't) / Total eligible auctions.

## Interpretation Scenarios

**High Overlap, Low Outranking:** Competitor targets same keywords and wins more often. Check Quality Score difference, evaluate bid strategy.

**Low Overlap, High Impression Share:** You dominate this segment with little direct competition. Maintain position, don't overbid.

**New Competitor Appears:** 40% overlap, 60% position above in first week. Monitor trends, analyze their ads manually.

**Competitor IS Rising (yours dropping):** Competitor investing more. Evaluate ROI of these keywords — increase bids if profitable, or shift to less competitive segments.

## Competitive Benchmark Analysis

Build a benchmark table for top 5 competitors from Auction Insights data (minimum 30 days):

```
┌──────────────┬───────────┬─────────┬───────────┬────────────┬──────────┐
│ Competitor   │ Imp Share │ Overlap │ Pos Above │ Outranking │ Trend    │
├──────────────┼───────────┼─────────┼───────────┼────────────┼──────────┤
│ You          │ 45%       │ -       │ -         │ -          │ Baseline │
│ Competitor A │ 52%       │ 78%     │ 55%       │ 42%        │ ↑ +5%   │
│ Competitor B │ 38%       │ 65%     │ 35%       │ 58%        │ → Stable│
└──────────────┴───────────┴─────────┴───────────┴────────────┴──────────┘

Threat Score = (Overlap Rate x Position Above Rate) / 100
Example: Competitor A = (78% x 55%) / 100 = 42.9 (HIGH)
```

## Market Share Calculation

**Method 1 — Impression Share basis:** Your IS = your share of eligible searches. Lost IS (Budget) + Lost IS (Rank) = room to grow.

**Method 2 — Relative Share:** Your IS / Sum of all known IS. Note: overlap means sum can exceed 100%.

**Method 3 — Share of Voice:** Your Impressions / Estimated total searches (from Keyword Planner).

## Competitive Position Matrix

```
        HIGH IS
           │
    MARKET │  DOMINANT PLAYERS
    LEADERS│  (large budgets, strong QS — differentiate)
           │
LOW ───────┼─────────── HIGH Position Above
           │
    NICHE  │  AGGRESSIVE CHALLENGERS
    PLAYERS│  (selective but strong — monitor and learn)
           │
        LOW IS
```

## Competitor Strategy Patterns

| Pattern | Signals | Your Response |
|---------|---------|---------------|
| Aggressive Market Share | Top positions always, broad coverage, aggressive offers | Don't match — focus on efficiency and niche |
| Cherry-Picking | High position only on specific keywords, low IS overall | Test their high-value keywords, learn from selection |
| Defensive/Brand | Dominant on brand terms, low non-brand presence | Opportunity on non-brand generics |
| Promotional Surge | Sudden IS increase, aggressive offers, temporary | Track timing, plan your own promotions around their baseline periods |

> Competitive response decision tree and tactical responses in [references/decision-trees.md](references/decision-trees.md). Monitoring setup, weekly review checklist, and Google Ads Script in [references/detailed-reference.md](references/detailed-reference.md).

## Output: Competitive Analysis Report Template

```markdown
# Competitive Analysis Report

## Executive Summary
- **Period:** [Date range]
- **Market position:** [Leader/Challenger/Follower]
- **Key trend:** [Describe]
- **Action required:** [Yes/No + brief explanation]

## Top Competitors
| Competitor | Imp Share | Overlap | Position Above | Outranking | Trend |
|------------|-----------|---------|----------------|------------|-------|
| [You] | [X]% | - | - | - | Baseline |
| [Comp A] | [X]% | [X]% | [X]% | [X]% | [up/down/stable] |

## Competitor Deep Dives
### [Competitor A]
- **Strategy type:** [Aggressive/Selective/Defensive]
- **Observed tactics:** [List]
- **Ad messaging:** [Headlines, offers, USPs]
- **Threat level:** [High/Medium/Low]

## Strategic Recommendations
### Immediate (This Week)
1. [Action] - [Rationale]

### Short-term (This Month)
1. [Action] - [Rationale]

## Monitoring Plan
- **Daily:** CPC and IS changes
- **Weekly:** Auction Insights review, manual spot check
- **Monthly:** Full competitive landscape analysis
```
