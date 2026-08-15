---
name: google-ads-account-auditor
description: "This skill should be used when the user asks to \"audit a Google Ads account\", \"do an account takeover review\", \"run a health check on Google Ads\", \"identify optimization opportunities\", or mentions \"account audit\", \"periodic review\", or \"account health score\". Do NOT use for: single campaign troubleshooting (use performance-troubleshooter), keyword-only analysis (use keyword-strategy-planner)."
---
# Account Auditor

Systematic framework for performing complete Google Ads account audits, including health scoring, issue identification, and prioritized recommendations.

## MCP Tool Integration

```
STEP 1: Account-level performance snapshot
google_ads_run_gaql(query="
  SELECT
    campaign.name, campaign.status,
    campaign.advertising_channel_type,
    campaign.bidding_strategy_type,
    metrics.cost_micros, metrics.conversions,
    metrics.cost_per_conversion,
    metrics.search_impression_share,
    metrics.search_budget_lost_impression_share,
    metrics.search_rank_lost_impression_share
  FROM campaign
  WHERE campaign.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")

STEP 2: Keyword quality check
google_ads_run_gaql(query="
  SELECT
    campaign.name, ad_group.name,
    ad_group_criterion.keyword.text,
    ad_group_criterion.keyword.match_type,
    ad_group_criterion.quality_info.quality_score,
    metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions
  FROM keyword_view
  WHERE campaign.status = 'ENABLED'
    AND ad_group.status = 'ENABLED'
    AND ad_group_criterion.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
  LIMIT 100
")

STEP 3: Conversion action review
google_ads_run_gaql(query="
  SELECT
    conversion_action.name, conversion_action.status,
    conversion_action.category,
    conversion_action.counting_type,
    conversion_action.include_in_conversions_metric,
    conversion_action.attribution_model_settings.attribution_model
  FROM conversion_action
  WHERE conversion_action.status = 'ENABLED'
")
```

> Full GAQL examples and interaction patterns in [references/api-patterns.md](references/api-patterns.md).

## Audit Framework

### Audit Scope (7 Areas + Unused Features)

```
GOOGLE ADS ACCOUNT AUDIT AREAS
1. CONVERSION TRACKING & DATA QUALITY
   └── Tags, Enhanced Conversions, Attribution, Values
2. ACCOUNT STRUCTURE
   └── Campaigns, Ad Groups, Naming, Organization
3. KEYWORD STRATEGY
   └── Match Types, Negatives, Quality Score, Search Terms
4. AD COPY & CREATIVE
   └── RSAs, Ad Strength, Extensions, Asset Groups
5. BIDDING & BUDGET
   └── Smart Bidding, Targets, Budget Allocation
6. AUDIENCES
   └── Remarketing, Customer Match, Signals, Exclusions
7. PERFORMANCE METRICS
   └── KPIs, Trends, Benchmarks, Efficiency
8. UNUSED FEATURES (NEW)
   └── PMax, Enhanced Conversions, Extensions, Demand Gen
```

## Complete Audit Checklist

### Section 1: Conversion Tracking (Score: /50)

- Conversion actions: active, Primary vs Secondary, counting method, data-driven attribution
- Google Tag: installed all pages, no duplicates, fires correctly, values sent
- Enhanced Conversions: enabled, user data (email/phone), match rate >70%, Consent Mode v2
- Data quality: conversion rate realistic, values match backend/GA4, no duplicates
- Offline conversions (lead gen): imported, frequency (weekly min), lead-to-sale tracking

### Section 2: Account Structure (Score: /50)

- Campaign organization: 3-10 active, logical types mix, clear objectives, no overlap, naming
- Ad group structure: 3-20 per campaign, thematic, sufficient ads (3-5 RSAs), keyword alignment
- PMax structure: logical asset groups, correct listing groups, audience signals, search themes, campaign-level negatives (v20+), search terms reviewed (v21+)
- Shopping/Merchant Center: feed health, disapprovals <5%, custom labels, product data quality

### Section 3: Keyword Strategy (Score: /50)

- Coverage: brand vs non-brand, category coverage, long-tail present
- Match types: distribution (exact/phrase/broad), broad + Smart Bidding combo
- Negative keywords: account-level, campaign-level, lists, regular search terms review
- Quality Score: average >6 account-wide, keywords with QS <5 identified

### Section 4: Ad Copy & Creative (Score: /50)

- RSAs: 2+ per ad group, 8-15 unique headlines, 4 descriptions, varied messaging
- Ad Strength: % Excellent, Poor/Average identified
- Extensions: sitelinks (4+), callouts (4+), structured snippets, image, call, location, price, promotion
- PMax assets: 10+ images, video present, asset performance reviewed (UI only, not in API v22+)
- Landing pages: relevant, mobile-friendly, speed <3s, clear CTA

### Section 5: Bidding & Budget (Score: /50)

- Bid strategy: appropriate for maturity, learning phase status, no "Limited" statuses
- Bid targets: realistic, data-based, regular evaluation, delivery stable
- Budget allocation: distributed, top performers funded, no "Limited by Budget"
- Portfolio strategies: used where logical, sufficient data per portfolio

### Section 6: Audiences (Score: /40)

- First-party: remarketing lists active, Customer Match uploaded, visitor lists (30/60/90/180d), converters for exclusion
- PMax signals: custom segments, first-party data, in-market, affinity
- RLSA: active on Search, Display remarketing, frequency caps
- Exclusions: converters excluded, irrelevant audiences, employee/competitor exclusions

### Section 7: Performance Review (Score: /50)

- Key metrics vs benchmarks: CTR (3-5% Search), CPC, CPA, ROAS, Conv Rate (2-5%)
- Impression share: Search IS, Lost IS (Budget), Lost IS (Rank), Abs Top IS (Brand)
- Trends: CPA/ROAS/Volume/Spend (30d vs previous 30d)
- Wasted spend: low QS keywords, irrelevant search terms, non-converting placements

### Section 8: Unused Features (Score: /80)

Key areas to check: PMax adoption, Enhanced Conversions match rate, audience assets utilization, ad extensions completeness, automation/rules, Demand Gen/YouTube testing, feed optimization, measurement tools.

> Full unused features checklist with opportunity cost estimates in [references/detailed-reference.md](references/detailed-reference.md).

## Health Score Calculator

```
SECTION                   │ MAX POINTS │ YOUR SCORE
──────────────────────────┼────────────┼───────────
Tracking & Data Quality   │     50     │    ___
Account Structure         │     50     │    ___
Keyword Strategy          │     50     │    ___
Ad Copy & Creative        │     50     │    ___
Budget & Bidding          │     50     │    ___
Audiences                 │     40     │    ___
Performance Metrics       │     50     │    ___
Unused Features           │     80     │    ___
──────────────────────────┼────────────┼───────────
TOTAL                     │    420     │    ___

PERCENTAGE: ___/420 x 100 = ___%

SCORE INTERPRETATION:
├── 85-100%: EXCELLENT - Minor tweaks only
├── 70-84%:  GOOD - Several improvements needed
├── 55-69%:  FAIR - Significant optimization required
├── 40-54%:  POOR - Major restructuring needed
└── <40%:    CRITICAL - Fundamental rebuild required

Per checkbox: OK = 10 pts, Issues = 5 pts, Critical = 0 pts
Adjust for N/A items (subtract from max, recalculate %).
```

## Issue Prioritization Matrix

```
CRITICAL (Fix within 24-48 hours):
- Conversion tracking not working / zero conversions
- Budget limit reached on top campaigns
- Policy violations/suspensions
- Tag errors/major tracking discrepancies (>30%)

HIGH (Fix within 1 week):
- Enhanced Conversions not active
- >20% keywords with QS <5
- Learning phase stuck >3 weeks
- CPA/ROAS >30% above target
- Missing ad extensions on major campaigns

MEDIUM (Fix within 2 weeks):
- Ad strength "Poor"/"Average", naming inconsistent
- Negative keywords incomplete, audience exclusions missing
- Budget misallocation, outdated ad copy (>6 months)

LOW (Fix within 1 month):
- Optimization opportunities, nice-to-have extensions
- Testing new strategies, advanced audience strategies
```

## Quick Audit (15 Minutes)

```
Run these GAQL queries to check 10 items:

□ 1. Conversions in last 7 days?
   → google_ads_run_gaql(query="SELECT metrics.conversions FROM customer WHERE segments.date DURING LAST_7_DAYS")
□ 2. Campaigns with "Limited" status?
   → google_ads_run_gaql(query="SELECT campaign.name, campaign.serving_status FROM campaign WHERE campaign.serving_status != 'SERVING'")
□ 3. Learning phase issues?
   → Check campaign.bidding_strategy_type and recent budget changes
□ 4. CPA/ROAS vs target?
   → google_ads_run_gaql(query="SELECT campaign.name, metrics.cost_per_conversion, metrics.conversions_value, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_7_DAYS AND campaign.status = 'ENABLED' ORDER BY metrics.cost_micros DESC")
□ 5. Top/Worst campaign performance?
   → Same query as #4 — sort by cost_per_conversion ASC/DESC
□ 6. Search Terms check (random sample)?
   → google_ads_run_gaql(query="SELECT search_term_view.search_term, metrics.impressions, metrics.clicks, metrics.conversions FROM search_term_view WHERE segments.date DURING LAST_7_DAYS AND metrics.impressions > 5 ORDER BY metrics.clicks DESC LIMIT 50")
□ 7. Ad Strength distribution?
   → google_ads_run_gaql(query="SELECT ad_group_ad.ad_strength FROM ad_group_ad WHERE ad_group_ad.status = 'ENABLED'")
□ 8. Budget spend rate?
   → Compare metrics.cost_micros vs campaign.campaign_budget (budget resource)
□ 9. Impression Share (top campaign)?
   → google_ads_run_gaql(query="SELECT campaign.name, metrics.search_impression_share, metrics.search_budget_lost_impression_share FROM campaign WHERE segments.date DURING LAST_7_DAYS AND campaign.status = 'ENABLED' ORDER BY metrics.cost_micros DESC LIMIT 5")
□ 10. Recent changes (Change History)? (⚠️ UI-only — change_event resource has limited API access)

QUICK SCORE: ___/10 items OK
├── 9-10: Account healthy, monthly check
├── 7-8:  Attention points, plan action
├── 5-6:  Issues present, prioritize
└── <5:   In-depth audit needed
```

> Google Ads Script for automated health monitoring and full audit report template in [references/detailed-reference.md](references/detailed-reference.md).
