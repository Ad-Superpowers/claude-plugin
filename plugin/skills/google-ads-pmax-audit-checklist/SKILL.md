---
name: google-ads-pmax-audit-checklist
description: "This skill should be used when the user asks to \"audit Performance Max\", \"review PMax health\", \"score PMax campaigns\", \"evaluate asset group performance\", or mentions \"PMax scorecard\", \"PMax health check\", or \"Ad Strength improvement\". Do NOT use for: PMax initial setup (use performance-max-optimizer), PMax retail-specific issues (use pmax-retail-optimizer), PMax vs Search cannibalization (use pmax-search-cannibalization-detector)."
---
# PMax Audit Checklist

Structured audit framework for Performance Max campaigns with scoring (100 points). Uses all available GAQL recipes for maximum data coverage.

## Audit Overview

```
PMAX AUDIT SCORECARD (100 POINTS)
===================================

1. Account Structure         /15 points
2. Budget & Bidding          /15 points
3. Asset Quality             /20 points
4. Search Term Quality       /15 points
5. Channel Performance       /15 points
6. Shopping/Feed Health      /10 points
7. Audience Signals          /10 points

TOTAL:                       /100 points

SCORE INTERPRETATION:
+-- 80-100: Excellent -- fine-tuning and scaling
+-- 60-79:  Good -- specific improvement areas
+-- 40-59:  Fair -- significant optimization needed
+-- <40:    Poor -- consider restructuring
```

## 1. Account Structure Audit (15 points)

### Data Retrieval

```sql
-- All PMax campaigns with status and budget
SELECT campaign.id, campaign.name, campaign.status,
    campaign.advertising_channel_type,
    campaign_budget.amount_micros,
    campaign.bidding_strategy_type,
    metrics.impressions, metrics.clicks, metrics.cost_micros,
    metrics.conversions, metrics.conversions_value
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
AND segments.date DURING LAST_30_DAYS
```

```sql
-- Asset groups per campaign
SELECT campaign.name, asset_group.id, asset_group.name,
    asset_group.status, metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions
FROM asset_group
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

### Scoring Criteria

```
ACCOUNT STRUCTURE SCORING
==========================

[ ] Number of PMax campaigns (5 points)
+-- 1-3 campaigns with clear segmentation -> 5/5
+-- 4-6 campaigns, logical distribution -> 4/5
+-- 7+ campaigns OR no logical structure -> 2/5
+-- 1 campaign for everything -> 3/5 (ok for small account)

[ ] Asset groups per campaign (5 points)
+-- 2-7 asset groups with product/theme segmentation -> 5/5
+-- 1 asset group per campaign -> 3/5 (underutilized)
+-- 8-15 asset groups -> 3/5 (too fragmented)
+-- >15 asset groups -> 1/5 (too many, consolidate)

[ ] Asset group delivery distribution (5 points)
+-- All asset groups >10% spend share -> 5/5
+-- 1-2 asset groups <10% spend -> 3/5
+-- >50% asset groups <10% spend -> 1/5
+-- Asset groups with 0 impressions -> 0/5
```

### Decision Matrix: Number of Asset Groups

| Number of Products | Recommended Asset Groups | Segmentation |
|-------------------|------------------------|-------------|
| 1-10 | 1-2 | Per product line |
| 11-50 | 2-5 | Per category |
| 51-200 | 3-7 | Per category + bestsellers |
| 200+ | 5-10 | Category + margin tier + bestsellers |

## 2. Budget & Bidding Audit (15 points)

### Data Retrieval

```sql
-- Budget utilization and bidding details
SELECT campaign.name, campaign.status,
    campaign_budget.amount_micros, campaign_budget.has_recommended_budget,
    campaign_budget.recommended_budget_amount_micros,
    campaign.bidding_strategy_type,
    campaign.maximize_conversions.target_cpa_micros,
    campaign.maximize_conversion_value.target_roas,
    metrics.cost_micros, metrics.impressions,
    metrics.conversions, metrics.conversions_value
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
AND campaign.status = 'ENABLED'
AND segments.date DURING LAST_30_DAYS
```

### Scoring Criteria

```
BUDGET & BIDDING SCORING
=========================

[ ] Budget sufficiency (5 points)
+-- Budget >10x target CPA -> 5/5 (enough learning data)
+-- Budget 5-10x target CPA -> 3/5 (tight but workable)
+-- Budget <5x target CPA -> 1/5 (too little for PMax)
+-- Google recommends higher budget -> -1 point

[ ] Bid strategy alignment (5 points)
+-- Target ROAS with sufficient conversion data (>30/mo) -> 5/5
+-- Maximize Conversions with sufficient data -> 4/5
+-- Target CPA with sufficient data -> 4/5
+-- Maximize Conv Value (no target) -> 3/5
+-- Less than 15 conversions/month with tROAS/tCPA -> 1/5

[ ] Budget distribution across campaigns (5 points)
+-- Logical distribution (high margin = more budget) -> 5/5
+-- Equal distribution -> 3/5
+-- All budget in 1 campaign -> 2/5
+-- Low performers get most budget -> 1/5
```

### Minimum Budget per Strategy

| Bid Strategy | Min. Conversions/Month | Min. Budget Guideline |
|-------------|----------------------|----------------------|
| Maximize Conversions | 0 (no minimum) | $500/mo |
| Target CPA | 15+ (ideally 30+) | 10x target CPA/day |
| Maximize Conv Value | 0 (no minimum) | $750/mo |
| Target ROAS | 15+ (ideally 30+) | 10x target CPA/day |

## 3. Asset Quality Audit (20 points)

### Data Retrieval

```sql
-- Asset list per asset group (performance_label NOT available for PMax since v22)
SELECT asset_group.name, asset_group_asset.field_type,
    asset.name, asset.type, asset.text_asset.text
FROM asset_group_asset
```

```sql
-- Ad Strength per asset group (still available for PMax)
SELECT asset_group.name, asset_group.ad_strength,
    asset_group.status
FROM asset_group
```

### Scoring Criteria

```
ASSET QUALITY SCORING
=========================

⚠️ NOTE: asset_group_asset.performance_label was REMOVED for Performance Max
   campaigns in API v22 (2025). Ad Strength (asset_group.ad_strength) remains
   available and is now the primary asset quality signal for PMax.

[ ] Ad Strength (14 points — replaces Performance Labels for PMax)
+-- All asset groups "Excellent" -> 14/14
+-- Mix of "Excellent" and "Good" -> 10/14
+-- All "Good" -> 8/14
+-- Mix with "Average" -> 5/14
+-- Any "Poor" -> 2/14
+-- All "Poor" or "Incomplete" -> 0/14

[ ] Asset Completeness (6 points)
+-- All asset types at maximum -> 6/6
|   +-- Headlines: 15 (max)
|   +-- Long Headlines: 5 (max)
|   +-- Descriptions: 5 (max)
|   +-- Images: 20 (max)
|   +-- Logos: 5 (max)
|   +-- Videos: 5 (max)
+-- All minimums + 50% extras -> 4/6
+-- Only minimums filled -> 2/6
+-- Below minimums -> 0/6
```

### Asset Quality Decision Matrix

| Ad Strength | Campaign Age | Action |
|-------------|-------------|-------|
| Excellent | Any | Keep structure, add more asset variety |
| Good | <30 days | Let it run, monitor trends |
| Good | >30 days | Add new headline/image angles |
| Average | Any | Review and add more diverse assets |
| Poor | Any | Immediate asset overhaul needed |
| Incomplete | Any | Add missing required asset types |

## 4. Search Term Quality Audit (15 points)

### Data Retrieval

```sql
-- PMax search terms (use campaign_search_term_view, NOT search_term_view — v21+)
SELECT campaign.name, campaign_search_term_view.search_term,
    metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions
FROM campaign_search_term_view
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 200
```

### Scoring Criteria

```
SEARCH TERM QUALITY SCORING
===============================

[ ] Relevance (5 points)
+-- >80% search terms relevant for business -> 5/5
+-- 60-80% relevant -> 3/5
+-- 40-60% relevant -> 2/5
+-- <40% relevant -> 0/5

[ ] Brand vs Non-Brand mix (5 points)
+-- <20% branded terms -> 5/5 (PMax finds new traffic)
+-- 20-40% branded -> 3/5
+-- 40-60% branded -> 1/5
+-- >60% branded -> 0/5 (see cannibalization detector)
+-- No Brand Search campaign active -> -2 points

[ ] Negative keyword hygiene (5 points)
+-- Campaign-level negatives active on PMax (v20+ feature) -> 3/5
+-- Regularly updated (last 30 days) -> +2/5
+-- No negatives set -> 0/5
+-- Irrelevant terms in report without negatives -> 0/5
+-- Note: Campaign-level negatives for PMax added in API v20 (2024)
+--       Account-level negative keyword lists also apply to PMax
```

### Check Existing Negatives

```sql
-- Campaign-level negative keywords on PMax
SELECT campaign.name, campaign_criterion.keyword.text,
    campaign_criterion.keyword.match_type
FROM campaign_criterion
WHERE campaign_criterion.negative = true
AND campaign_criterion.type = 'KEYWORD'
AND campaign.advertising_channel_type = 'PERFORMANCE_MAX'
```

## 5. Channel Performance Audit (15 points)

### Data Retrieval

PMax distributes budget across Search, Shopping, Display, YouTube, Discover, Gmail. Use `segments.ad_network_type` for direct channel breakdown (v22+):

```sql
-- PMax performance by network/channel (v22+ ad_network_type breakdown)
SELECT campaign.name, segments.ad_network_type,
    metrics.impressions, metrics.clicks, metrics.cost_micros,
    metrics.conversions, metrics.conversions_value,
    metrics.view_through_conversions
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

```sql
-- PMax campaign-level metrics (including conv action breakdown)
SELECT campaign.name, segments.conversion_action_category,
    metrics.impressions, metrics.clicks, metrics.cost_micros,
    metrics.conversions, metrics.all_conversions,
    metrics.view_through_conversions
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
AND segments.date DURING LAST_30_DAYS
```

```sql
-- Asset group performance (proxy for channel mix)
SELECT asset_group.name, asset_group.status,
    metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions,
    metrics.conversions_value
FROM asset_group
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

### Scoring Criteria

```
CHANNEL PERFORMANCE SCORING
=============================

[ ] Conversion distribution (5 points)
+-- Conversions from multiple channels -> 5/5
+-- >80% conversions from 1 channel -> 3/5
+-- Only view-through conversions -> 1/5
+-- No conversions -> 0/5

[ ] View-through vs Click-through ratio (5 points)
+-- VTC <20% of total conversions -> 5/5
+-- VTC 20-40% -> 3/5
+-- VTC 40-60% -> 1/5
+-- VTC >60% -> 0/5 (Display/YouTube claiming incorrectly)

[ ] Spend efficiency (5 points)
+-- Cost per conversion <= target CPA -> 5/5
+-- Cost per conversion 1-1.5x target -> 3/5
+-- Cost per conversion 1.5-2x target -> 1/5
+-- Cost per conversion >2x target -> 0/5
```

### Red Flags per Channel

| Signal | Possible Cause | Action |
|--------|---------------|-------|
| Many impressions, few clicks | Display/YouTube dominant | Check view-through attribution |
| High VTC ratio | Display claiming incorrectly | Compare with Search-only |
| High CPM, low CTR | YouTube/Discover spend | Check video asset quality |
| Many conversions, low value | Low-intent channels | Check conversion value rules |

## 6. Shopping/Feed Health Audit (10 points)

*Only relevant for PMax Retail (with product feed)*

### Data Retrieval

```sql
-- Shopping performance per product
SELECT segments.product_title, segments.product_brand,
    segments.product_type_l1, metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC LIMIT 50
```

```sql
-- Merchant Center link check
SELECT product_link.merchant_center.merchant_center_id,
    product_link.product_link_id
FROM product_link WHERE product_link.type = 'MERCHANT_CENTER'
```

```sql
-- Listing group filters per asset group
SELECT asset_group.name, asset_group_listing_group_filter.type,
    asset_group_listing_group_filter.listing_source
FROM asset_group_listing_group_filter
```

### Scoring Criteria

```
SHOPPING/FEED HEALTH SCORING
==============================

[ ] Product coverage (5 points)
+-- >80% products have impressions (30d) -> 5/5
+-- 50-80% have impressions -> 3/5
+-- 20-50% have impressions -> 1/5
+-- <20% have impressions (zombie inventory) -> 0/5

[ ] Listing group strategy (5 points)
+-- Logical subdivisions per asset group -> 5/5
+-- UNIT_INCLUDED per asset group (all products) -> 3/5
+-- Overlapping asset groups without filters -> 1/5
+-- No listing group filters -> 0/5

NON-RETAIL PMAX:
+-- Skip this section, score 10/10
```

### Zombie Product Detection

```
IDENTIFYING ZOMBIE PRODUCTS
==============================

Definition: Product with 0 impressions in last 30 days

Causes:
+-- Low bids vs competition
+-- Poor feed quality (disapprovals)
+-- Price too high vs market
+-- Product not in active listing group
+-- Low search volume for this product

Solutions:
+-- <10% zombie rate -> Normal, no action
+-- 10-30% -> Check feed quality, consider separate asset group
+-- 30-50% -> Feed audit needed, restructure listing groups
+-- >50% -> Serious problem, full feed review
```

## 7. Audience Signals Audit (10 points)

### Data Retrieval

```sql
-- Audience signals per asset group
SELECT asset_group.name, asset_group_signal.audience.audience
FROM asset_group_signal
```

### Scoring Criteria

```
AUDIENCE SIGNALS SCORING
=========================

[ ] Signal presence (5 points)
+-- All asset groups have signals -> 5/5
+-- >50% asset groups with signals -> 3/5
+-- <50% with signals -> 1/5
+-- No signals set -> 0/5

[ ] Signal quality (5 points)
+-- Mix of first-party + Google audiences -> 5/5
|   +-- Customer Match lists
|   +-- Website visitors
|   +-- In-Market segments
|   +-- Custom segments (search-based)
+-- Only Google audiences -> 3/5
+-- Only 1 type of signal -> 1/5
+-- Irrelevant or too broad signals -> 0/5
```

## Audit Output Template

```
=============================================
      PMAX AUDIT SCORECARD
      Account: [Account Name]
      Period: Last 30 days
      Date:   [Today]
=============================================

SCORES:
1. Account Structure:     __/15
2. Budget & Bidding:      __/15
3. Asset Quality:         __/20
4. Search Term Quality:   __/15
5. Channel Performance:   __/15
6. Shopping/Feed Health:  __/10
7. Audience Signals:      __/10
                         ------
TOTAL:                    __/100

TOP 3 QUICK WINS:
1. [...]
2. [...]
3. [...]

MEDIUM TERM ACTIONS (2-4 weeks):
1. [...]
2. [...]

STRATEGIC RECOMMENDATIONS:
1. [...]
```

## Tools Reference

| Action | Tool | Recipe/Query |
|-------|------|--------------|
| Get PMax campaigns | `google_ads_run_gaql` | campaign + PERFORMANCE_MAX filter |
| Asset group performance | `google_ads_run_gaql` | PMax asset group performance recipe |
| Asset labels | `google_ads_run_gaql` | PMax asset group assets recipe |
| Search terms | `google_ads_run_gaql` | search_term_view |
| Shopping metrics | `google_ads_run_gaql` | Shopping performance recipe |
| Listing groups | `google_ads_run_gaql` | Listing groups recipe |
| Add negatives | `google_ads_mutate` | Recipe #7 |
| Pause campaign | `google_ads_mutate` | Recipe #2 |
| Change budget | `google_ads_mutate` | Recipe #3 |
| Look up accounts | `google_ads_list_accounts` | -- |
