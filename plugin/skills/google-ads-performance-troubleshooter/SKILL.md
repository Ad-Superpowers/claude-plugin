---
name: google-ads-performance-troubleshooter
description: "This skill should be used when the user asks to \"troubleshoot Google Ads performance\", \"diagnose CPA increase\", \"fix conversion drops\", \"investigate impression share decline\", or mentions \"ROAS degradation\", \"budget issues\", or \"performance problems\". Do NOT use for: full account audits (use account-auditor), keyword strategy planning (use keyword-strategy-planner)."
---
# Performance Troubleshooter

Systematic guide for diagnosing and resolving Google Ads performance problems. Start with the quick diagnosis below, then follow the detailed decision trees in references.

## Quick Diagnosis Guide

```
WHAT PROBLEM DO YOU HAVE?
│
├─► CONVERSIONS DROPPED
│   ���── Check 1: Is tracking intact? (tag firing, consent mode)
│   ├── Check 2: Have clicks dropped? (traffic issue vs conversion rate)
│   ├── Check 3: Landing page changed? (speed, mobile, form broken)
│   ├── Check 4: Traffic quality changed? (search terms, device mix)
│   ├── Check 5: Competition/seasonality? (Auction Insights)
│   └── Detailed tree: See references/decision-trees.md "Conversion Drop Diagnosis"
│
├─► CPA INCREASED / ROAS DECREASED
│   ├── Check: Is conversion volume stable? (CPA up with same volume = bid issue)
│   ├── Check: New keywords/audiences? (lower intent traffic diluting efficiency)
│   ├── Check: Auction competition? (competitor CPCs rising)
│   ├── Check: Smart Bidding learning? (recent strategy change = 2-week volatility)
│   └── Detailed tree: See references/decision-trees.md "Efficiency Degradation"
│
├─► IMPRESSIONS / CLICKS DROPPED
│   ├── Check: Budget sufficient? (Limited by budget status)
│   ├── Check: Impression Share Lost (Budget vs Rank)
│   ├── Check: Ad disapprovals? (Policy violations)
│   ├── Check: Keyword status? (Low search volume, below first page bid)
│   └── Detailed tree: See references/decision-trees.md "Volume Decline"
│
├─► NO DELIVERY (0 impressions)
│   ├── Check: Campaign/ad group/ad enabled?
│   ├── Check: Budget > €0 and not exhausted?
│   ├── Check: Targeting not too narrow?
│   ├── Check: Negative keywords blocking all traffic?
│   └── Detailed tree: See references/decision-trees.md "Delivery Problems"
│
├─► QUALITY SCORE DROPPED
│   ├── Check: Expected CTR (ad relevance vs competition)
│   ├── Check: Ad Relevance (keyword-to-ad alignment)
│   ├── Check: Landing Page Experience (speed, relevance, mobile)
│   └── Detailed tree: See references/decision-trees.md "Quality Score"
│
└─► SMART BIDDING NOT WORKING
    ├── Check: Sufficient conversions? (Min 30/month for tCPA, 50 for tROAS)
    ├── Check: Learning period? (2 weeks after changes)
    ├── Check: Targets realistic? (not > 20% from actual performance)
    ├── Check: Conversion lag? (report may not yet show recent conversions)
    └── Detailed tree: See references/decision-trees.md "Bidding Problems"
```

## MCP Tool Integration

```
STEP 1: Quick performance overview
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign.status,
    campaign.bidding_strategy_type,
    metrics.cost_micros,
    metrics.conversions,
    metrics.cost_per_conversion,
    metrics.conversions_from_interactions_rate,
    metrics.search_impression_share,
    metrics.search_budget_lost_impression_share,
    metrics.search_rank_lost_impression_share
  FROM campaign
  WHERE campaign.status = 'ENABLED'
    AND segments.date DURING LAST_14_DAYS
  ORDER BY metrics.cost_micros DESC
")

STEP 2: Period-over-period comparison (detect degradation)
google_ads_run_gaql(query="
  SELECT
    segments.date,
    metrics.impressions,
    metrics.clicks,
    metrics.conversions,
    metrics.cost_micros,
    metrics.average_cpc
  FROM campaign
  WHERE campaign.name = 'CAMPAIGN_NAME'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY segments.date DESC
")

STEP 3: Ad group & keyword drill-down (find the problem area)
google_ads_run_gaql(query="
  SELECT
    ad_group.name,
    metrics.impressions,
    metrics.clicks,
    metrics.conversions,
    metrics.cost_micros,
    metrics.cost_per_conversion
  FROM ad_group
  WHERE campaign.name = 'CAMPAIGN_NAME'
    AND ad_group.status = 'ENABLED'
    AND segments.date DURING LAST_14_DAYS
  ORDER BY metrics.cost_micros DESC
")

STEP 4: Search terms quality check
google_ads_run_gaql(query="
  SELECT
    search_term_view.search_term,
    metrics.impressions,
    metrics.clicks,
    metrics.conversions,
    metrics.cost_micros
  FROM search_term_view
  WHERE segments.date DURING LAST_14_DAYS
    AND metrics.impressions > 10
  ORDER BY metrics.cost_micros DESC
  LIMIT 50
")
```

## Key Thresholds

```
WHEN TO WORRY (vs normal fluctuation)
──────────────────────────────────────
├── CPA: > 30% increase sustained 7+ days
├── Conversions: > 25% drop week-over-week
├── CTR: > 20% decline (ad fatigue or relevance issue)
├── Impression Share: > 15% drop (budget or competition)
├── Quality Score: Drop of 2+ points on key keywords
├── Smart Bidding: No improvement after 2-week learning period
└── ROAS: > 25% decline for 7+ consecutive days
```

## Output: Troubleshooting Report Template

```markdown
# Performance Troubleshooting Report

## Issue Summary
- **Problem detected:** [Description]
- **First signal:** [Date]
- **Impacted campaigns:** [List]
- **Severity:** [Critical/Warning/Info]

## Symptoms
| Metric | Previous Period | Current Period | Change |
|--------|----------------|----------------|--------|
| Impressions | [X] | [X] | [%] |
| Clicks | [X] | [X] | [%] |
| CTR | [X]% | [X]% | [%] |
| Conversions | [X] | [X] | [%] |
| CPA | €[X] | €[X] | [%] |
| ROAS | [X]% | [X]% | [%] |

## Root Cause Analysis

### Investigated Factors
- [ ] Conversion tracking: [OK/Issue found]
- [ ] Landing page: [OK/Issue found]
- [ ] Ad copy/creatives: [OK/Issue found]
- [ ] Bidding strategy: [OK/Issue found]
- [ ] Budget: [OK/Issue found]
- [ ] Competition: [Changed/Stable]
- [ ] Seasonality: [Yes/No]

### Identified Cause
**[Describe root cause]**

Evidence:
1. [Evidence 1]
2. [Evidence 2]
3. [Evidence 3]

## Solutions

### Immediate Actions (Now)
1. [Action 1]
2. [Action 2]

### Short Term (This Week)
1. [Action 1]
2. [Action 2]

### Long Term (Prevention)
1. [Action 1]
2. [Action 2]

## Monitoring Plan
- Daily check: [Metrics to monitor]
- Weekly review: [KPIs]
- Escalation trigger: [When to escalate again]
```
