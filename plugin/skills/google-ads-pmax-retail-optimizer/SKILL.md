---
name: google-ads-pmax-retail-optimizer
description: "This skill should be used when the user asks to \"optimize PMax retail campaigns\", \"fix zombie products in PMax\", \"set up listing group filters\", \"configure custom labels for PMax\", or mentions \"PMax e-commerce\", \"asset group budget allocation\", or \"product feed PMax\". Do NOT use for: general PMax setup (use performance-max-optimizer), PMax auditing (use pmax-audit-checklist), Shopping feed optimization outside PMax (use shopping-feed-optimizer)."
---
# PMax Retail Optimizer

Specific optimizations for Performance Max campaigns with product feeds (PMax Retail). Focused on e-commerce accounts using Merchant Center feeds.

## Quick Diagnostic

```
PMAX RETAIL HEALTH CHECK
==========================

1. Zombie Products?
   -> >20% products without impressions (30d) --> ACTION NEEDED

2. Listing Group Filters set?
   -> Only UNIT_INCLUDED (all) --> SUBOPTIMAL

3. Custom Labels active in feed?
   -> No custom labels --> OPPORTUNITY MISSED

4. Asset group spend distribution?
   -> >60% budget to 1 asset group --> REBALANCE

5. Product ROAS spread?
   -> Top 20% products = 80% revenue --> SEGMENT
```

## 1. Zombie Inventory Detection

### Data Retrieval

Zombie products = products with 0 impressions in the last 30 days.

```sql
-- Products WITH impressions (active products)
SELECT segments.product_title, segments.product_brand,
    segments.product_type_l1, segments.product_item_id,
    metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions ASC
LIMIT 100
```

```sql
-- Total shopping performance (for zombie % calculation)
SELECT segments.product_title, metrics.impressions,
    metrics.clicks, metrics.cost_micros
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
AND metrics.impressions = 0
LIMIT 200
```

### Zombie Analysis Framework

```
ZOMBIE PRODUCT CLASSIFICATION
==============================

TYPE 1: Feed Quality Zombies
+-- Cause: Disapprovals, poor data quality
+-- Detection: Products with warnings/disapprovals in MC
+-- Solution: Fix feed issues (title, image, price)
+-- Impact: High -- these products CANNOT run

TYPE 2: Competition Zombies
+-- Cause: Too much competition, bids too low
+-- Detection: Product exists in feed, no disapprovals, 0 impressions
+-- Solution: Higher bids OR separate asset group with more budget
+-- Impact: Medium -- bid increase can help

TYPE 3: Low Demand Zombies
+-- Cause: Little search volume for this product
+-- Detection: Niche product, few search terms
+-- Solution: Accept OR improve titles with more popular terms
+-- Impact: Low -- sometimes there's just no demand

TYPE 4: Structural Zombies
+-- Cause: Product not in active listing group filter
+-- Detection: Product in feed but outside asset group scope
+-- Solution: Expand listing group filters
+-- Impact: High -- configuration error
```

### Zombie Solution Matrix

| Zombie Rate | Severity | Action |
|-------------|----------|-------|
| <10% | Normal | No action, focus on performers |
| 10-20% | Attention | Check feed quality, optimize titles |
| 20-40% | Problem | Separate asset group for zombies, feed audit |
| 40-60% | Serious | Full feed review, restructure campaigns |
| >60% | Critical | Feed fundamentally broken or insufficient budget |

### Action: Separate Asset Group for Zombie Products

Via `google_ads_mutate`:

```json
operations=[
    {"assetGroupOperation": {"create": {
        "resourceName": "customers/{CID}/assetGroups/-10",
        "campaign": "customers/{CID}/campaigns/{PMAX_CAMPAIGN_ID}",
        "name": "Asset Group - Revive Zombies"
    }}},
    {"assetGroupListingGroupFilterOperation": {"create": {
        "assetGroup": "customers/{CID}/assetGroups/-10",
        "type": "UNIT_INCLUDED",
        "vertical": "SHOPPING",
        "caseValue": {"productCustomAttribute": {
            "index": "INDEX1",
            "value": "zombie"
        }}
    }}}
]
```

Requires: Custom Label 1 = "zombie" in the feed for products with 0 impressions.

## 2. Listing Group Filter Optimization

### Analyze Current Filters

```sql
-- Listing group filters per asset group
SELECT asset_group.name, asset_group_listing_group_filter.type,
    asset_group_listing_group_filter.vertical,
    asset_group_listing_group_filter.path
FROM asset_group_listing_group_filter
```

### Filter Strategy Decision Tree

```
LISTING GROUP FILTER STRATEGY
================================

How many products do you have?
|
+---> <50 products
|   +---> UNIT_INCLUDED per asset group (all)
|       +-- 1-2 asset groups max
|       +-- Segmentation is not needed
|
+---> 50-200 products
|   +---> FILTER PER CATEGORY
|       +-- productType L1 or productBrand
|       +-- 3-5 asset groups
|       +-- Each with own assets/signals
|
+---> 200-1000 products
|   +---> FILTER PER CATEGORY + PERFORMANCE
|       +-- productType + productCustomAttribute (margin/performance)
|       +-- 5-10 asset groups
|       +-- Separate group for bestsellers
|       +-- Separate group for zombies
|
+---> >1000 products
    +---> MULTI-CAMPAIGN + GRANULAR FILTERS
        +-- Campaign per main category
        +-- Asset groups per subcategory + margin
        +-- Custom labels for performance tiers
        +-- Regular label updates in feed
```

### Filter Types

| Filter Type | When | Example |
|------------|------|---------|
| UNIT_INCLUDED | All products in scope | Everything |
| UNIT_EXCLUDED | Exclude specific products | Exclude low margin |
| SUBDIVISION + UNIT_INCLUDED | Only specific subset | Only brand "Nike" |
| productBrand | Segment by brand | Nike, Adidas, own brand |
| productType | Segment by category | Clothing, Shoes, Accessories |
| productCustomAttribute | Business-specific | Margin tier, season |
| productItemId | Individual product | Specific SKU |
| productChannel | Online vs local | ONLINE, LOCAL |

### Mutate: Setting Listing Group Filters

Brand-based filter via `google_ads_mutate`:

```json
operations=[
    {"assetGroupListingGroupFilterOperation": {"create": {
        "assetGroup": "customers/{CID}/assetGroups/{AG_ID}",
        "type": "SUBDIVISION",
        "vertical": "SHOPPING",
        "caseValue": {"productBrand": {}}
    }}},
    {"assetGroupListingGroupFilterOperation": {"create": {
        "assetGroup": "customers/{CID}/assetGroups/{AG_ID}",
        "type": "UNIT_INCLUDED",
        "vertical": "SHOPPING",
        "caseValue": {"productBrand": {"value": "Nike"}}
    }}},
    {"assetGroupListingGroupFilterOperation": {"create": {
        "assetGroup": "customers/{CID}/assetGroups/{AG_ID}",
        "type": "UNIT_EXCLUDED",
        "vertical": "SHOPPING",
        "caseValue": {"productBrand": {"value": ""}}
    }}}
]
```

## 3. Custom Label Strategy for PMax

### 5 Custom Labels -- Recommended Usage

```
CUSTOM LABEL STRATEGY
========================

LABEL 0: MARGIN TIER
+-- high_margin   -> Products with >50% margin
+-- medium_margin -> Products with 20-50% margin
+-- low_margin    -> Products with <20% margin
+-- USE: Separate campaigns per margin tier
    +-- High margin = higher ROAS target, more budget

LABEL 1: PERFORMANCE TIER
+-- bestseller -> Top 20% by revenue (last 90 days)
+-- standard   -> Middle 60%
+-- slow_mover -> Bottom 20%
+-- new        -> Products <30 days in assortment
+-- USE: Separate asset groups per tier
    +-- Bestsellers = most budget + best assets

LABEL 2: SEASON
+-- spring, summer, autumn, winter
+-- evergreen (season-independent)
+-- holiday (christmas, black friday)
+-- USE: Seasonal campaigns activate/pause
    +-- Budget shift to relevant seasonal products

LABEL 3: LIFECYCLE
+-- new_arrival    -> First 30 days
+-- core           -> Standard assortment
+-- on_sale        -> Discounted
+-- clearance      -> Clearance sale
+-- last_chance    -> Almost sold out
+-- USE: Align messaging per lifecycle
    +-- New arrival = "New!", Clearance = "Last items"

LABEL 4: PRICE RANGE
+-- premium     -> >$200
+-- mid_range   -> $50-$200
+-- budget      -> <$50
+-- USE: Audience alignment
    +-- Premium = high-income audiences, Budget = deal seekers
```

### Label Update Frequency

| Label | Update Frequency | Source |
|-------|-----------------|--------|
| Margin Tier | Monthly | ERP / purchasing data |
| Performance Tier | Weekly | Google Ads conversion data |
| Season | Per season (4x/year) | Marketing calendar |
| Lifecycle | Daily | Inventory management |
| Price Range | On price change | Product feed |

## 4. Budget Allocation Framework

### Analyze Asset Group Performance

```sql
-- Asset group performance with spend share
SELECT asset_group.name, asset_group.status,
    campaign.name, metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions,
    metrics.conversions_value
FROM asset_group
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

### Budget Allocation Decision Matrix

```
BUDGET ALLOCATION FRAMEWORK
============================

STEP 1: Calculate ROAS per asset group
+-- ROAS = conversions_value / (cost_micros / 1000000)
+-- Rank asset groups by ROAS
+-- Identify top, middle, and low performers

STEP 2: Assess spend share
+-- Spend share = asset group cost / campaign cost
+-- Compare with expected distribution
+-- Ideal: High ROAS asset groups get more budget

PROBLEM SIGNALS:
+-- High ROAS asset group <15% spend -> Underfunded
+-- Low ROAS asset group >40% spend -> Budget waste
+-- Asset group with 0 impressions -> Configuration error
+-- 1 asset group >70% spend -> No diversification

STEP 3: Redistribute budget
+-- Option A: Adjust campaign-level budget
|   +-- Split asset groups across multiple campaigns
|       with own budgets (most control)
+-- Option B: Optimize asset group content
|   +-- Improve assets in underperforming groups
|       so Google allocates more budget
+-- Option C: Refine listing group filters
    +-- Target more precisely so relevance increases
```

### Budget Shift Protocol

```
MAX 20% BUDGET SHIFT PER WEEK
===============================

Week 1: Identify opportunity
+-- Asset Group A: ROAS 5.0x, 15% spend
+-- Asset Group B: ROAS 1.5x, 45% spend
+-- Action: Consider splitting into separate campaigns

Week 2: First shift
+-- Create Campaign 2 for top performers
+-- Move Asset Group A to Campaign 2
+-- Budget Campaign 2: +20% of original budget
+-- Budget Campaign 1: -20%

Week 3: Monitor
+-- Check ROAS both campaigns
+-- Check impressions/conversions distribution
+-- No changes (learning period)

Week 4: Evaluate and continue
+-- Performance improved -> Consider further shift
+-- Performance equal -> Stable, good
+-- Performance worsened -> Roll back
+-- Never shift more than 20% per week
```

## 5. Feed + PMax Coexistence Optimization

### Feed Quality Impact on PMax

```
FEED QUALITY -> PMAX PERFORMANCE
====================================

TITLE QUALITY (Highest impact)
+-- Keyword-first titles -> Better search matching
+-- Brand + product + attribute format
+-- Max 150 chars, first 70 chars most important
+-- Example: "Nike Air Max 90 Men's Running Shoes Black Size 10"

IMAGE QUALITY
+-- White background (Shopping requirement)
+-- High resolution (min 800x800, ideally 1200x1200)
+-- Product fills 75-90% of frame
+-- Lifestyle images as supplement (not primary)

PRICE COMPETITIVENESS
+-- Competitive price -> More impressions
+-- Sale price set -> Shopping annotations
+-- Price higher than competitor -> Less delivery
+-- Google compares prices in real-time

AVAILABILITY
+-- Out of stock -> Automatically paused
+-- Limited stock -> Lower priority
+-- Fast sync needed (at least daily)
+-- Feed delays -> Missed sales
```

### GAQL: Product-Level ROAS Analysis

```sql
-- Top performing products (for bestseller label)
SELECT segments.product_title, segments.product_brand,
    segments.product_item_id, segments.product_type_l1,
    metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions,
    metrics.conversions_value
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
AND metrics.cost_micros > 0
ORDER BY metrics.conversions_value DESC
LIMIT 50
```

```sql
-- Underperformers (for exclusion or feed improvement)
SELECT segments.product_title, segments.product_brand,
    segments.product_item_id,
    metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
AND metrics.cost_micros > 0
AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

### Product Exclusion Strategy

```
WHEN TO EXCLUDE PRODUCTS
==========================

EXCLUDE if:
+-- Product has >$50 spend and 0 conversions (30 days)
+-- Product ROAS <25% of average account ROAS
+-- Product is discontinued but still in feed
+-- Product has structurally poor reviews (doesn't convert)
+-- Product market price is too high vs competition

HOW TO EXCLUDE:
+-- Option 1: Remove product from listing group filter
|   +-- assetGroupListingGroupFilterOperation UNIT_EXCLUDED
+-- Option 2: Custom label "exclude" in feed
|   +-- Asset group filter exclude on label
+-- Option 3: Pause product in Merchant Center
|   +-- Stops for all Shopping/PMax campaigns
+-- Option 4: Lower priority via separate asset group
    +-- Less budget, not fully stopped

WHEN NOT TO EXCLUDE:
+-- Product is new (<14 days, insufficient data)
+-- Product is seasonal (wait for the season)
+-- Feed quality is the problem (fix the feed first)
+-- Budget is too low for all products (increase budget)
```

## Check Search Terms & Apply Negative Keywords (v20+)

```
PMax now supports campaign-level negative keywords (added in v20, 2024).
Use search term data to find irrelevant queries and add negatives.

STEP 1: Pull search terms
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign_search_term_view.search_term,
    campaign_search_term_view.status,
    metrics.impressions,
    metrics.clicks,
    metrics.cost_micros,
    metrics.conversions
  FROM campaign_search_term_view
  WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
    AND segments.date DURING LAST_30_DAYS
    AND metrics.cost_micros > 0
  ORDER BY metrics.cost_micros DESC
  LIMIT 200
")

STEP 2: Identify irrelevant high-spend terms
+-- Terms with high cost but 0 conversions
+-- Competitor brand names (if not desired)
+-- Category terms outside your scope

STEP 3: Add campaign-level negative keywords via google_ads_mutate
+-- Use campaign_criterion with negative=true on PMax campaign
+-- Start with exact match negatives for clearly irrelevant terms
```

## Optimization Cadence

```
WEEKLY:
+-- Check zombie product rate
+-- Review asset group spend distribution
+-- Scan search terms for irrelevance (use campaign_search_term_view)
+-- Monitor ROAS trends per asset group

BIWEEKLY:
+-- Update performance tier labels in feed
+-- Replace "Low" performance assets
+-- Evaluate listing group filter effectiveness
+-- Check new product performance

MONTHLY:
+-- Full ROAS analysis per product
+-- Consider budget reallocation
+-- Custom label updates (margin, lifecycle)
+-- Competitor price comparison
+-- Asset group consolidation or splits

QUARTERLY:
+-- Season label updates
+-- Campaign structure evaluation
+-- Feed quality audit
+-- Strategic repositioning
```

## Tools Reference

| Action | Tool | Recipe/Query |
|-------|------|--------------|
| Shopping performance per product | `google_ads_run_gaql` | Shopping performance recipe |
| Asset group performance | `google_ads_run_gaql` | PMax asset group performance recipe |
| View asset labels | `google_ads_run_gaql` | PMax asset group assets recipe |
| Listing group filters | `google_ads_run_gaql` | Listing groups recipe |
| Merchant Center check | `google_ads_run_gaql` | Merchant Center link recipe |
| Set listing group filter | `google_ads_mutate` | assetGroupListingGroupFilterOperation |
| Create asset group | `google_ads_mutate` | Recipe #18/#19 (assetGroupOperation) |
| Change campaign budget | `google_ads_mutate` | Recipe #3 |
| Create PMax Retail | `google_ads_mutate` | Recipe #19 |
| Look up accounts | `google_ads_list_accounts` | -- |
