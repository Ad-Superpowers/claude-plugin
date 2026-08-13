---
name: google-ads-shopping-campaign-structure-advisor
description: "This skill should be used when the user asks to \"structure Shopping campaigns\", \"choose between Standard Shopping and PMax\", \"set up product group subdivisions\", \"migrate from Standard Shopping to PMax\", or mentions \"campaign priority\", \"query sculpting\", or \"Shopping campaign setup\". Do NOT use for: PMax general optimization (use performance-max-optimizer), PMax auditing (use pmax-audit-checklist), Shopping feed optimization (use shopping-feed-optimizer)."
---
# Shopping Campaign Structure Advisor

Framework for choosing and setting up the optimal Shopping campaign structure. Based on proven structures from the PPC community (SavvyRevenue, Smarter Ecommerce, Optmyzr).

## Quick Decision Guide

```
WHICH SHOPPING STRUCTURE?
==========================

Budget?
|
+---> <$1k/mo
|   +---> PMAX RETAIL ONLY
|       +-- Not enough data for multiple campaigns
|       +-- 1-2 asset groups max
|       +-- Bid strategy: Maximize Conversion Value
|
+---> $1k-5k/mo
|   +---> PMAX RETAIL PRIMARY
|       +-- PMax Retail as main campaign
|       +-- Optional: Standard Shopping catchall (low budget)
|       +-- 2-5 asset groups per category/margin
|       +-- Bid strategy: Target ROAS (if >30 conv/mo)
|
+---> $5k-20k/mo
|   +---> CHOICE:
|       +---> Maximum control -> STANDARD SHOPPING + PMAX (split)
|       |   +-- Standard Shopping for top performers
|       |   +-- PMax for discovery + scale
|       |   +-- Product exclusions to prevent overlap
|       |
|       +---> Maximum scale -> PMAX RETAIL ONLY
|           +-- Multiple campaigns per segment
|           +-- 3-7 asset groups per campaign
|           +-- Custom labels for margin tiers
|
+---> >$20k/mo
    +---> HYBRID STRUCTURE RECOMMENDED
        +-- Standard Shopping for branded + top products
        +-- PMax Retail for non-brand discovery
        +-- Campaign-level budget control
        +-- Advanced listing group filters
```

## 7 Shopping Structures That Work

### Structure 1: Single PMax Retail (All Products)

```
WHEN TO USE:
+-- Small product catalog (<50 products)
+-- Budget <$1k/mo
+-- New account without historical data
+-- Maximum simplicity desired

SETUP:
Campaign: PMax Retail - All Products
+-- Budget: $30-50/day
+-- Bidding: Maximize Conversion Value
+-- Asset Group 1: All Products
    +-- Listing Group: UNIT_INCLUDED (everything)
    +-- 15 headlines, 5 descriptions
    +-- 5-10 images (product + lifestyle)
    +-- Audience Signals: Website visitors + In-Market
```

**GAQL check** -- do you have enough products for PMax?

```sql
SELECT segments.product_title, metrics.impressions
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC LIMIT 100
```

### Structure 2: PMax per Category

```
WHEN TO USE:
+-- 50-500 products
+-- Clear product categories
+-- Budget $1k-10k/mo
+-- Different margins per category

SETUP:
Campaign: PMax Retail - Clothing
+-- Asset Group: Men's
|   +-- Listing Group: productType L1 = "Men's"
|   +-- Signals: Men's fashion interests
+-- Asset Group: Women's
|   +-- Listing Group: productType L1 = "Women's"
|   +-- Signals: Women's fashion interests
+-- Asset Group: Kids
    +-- Listing Group: productType L1 = "Kids"
    +-- Signals: Parents

Campaign: PMax Retail - Shoes
+-- Asset Group: Sneakers
+-- Asset Group: Boots
+-- Asset Group: Sandals
```

### Structure 3: PMax per Margin Tier (Custom Labels)

```
WHEN TO USE:
+-- Large spread in profit margins
+-- Goal = maximum profit (not revenue)
+-- Budget >$3k/mo
+-- Custom labels already set up in feed

SETUP:
Campaign 1: PMax - High Margin (Custom Label 0 = "high_margin")
+-- Budget: 60% of total
+-- Bidding: Target ROAS (higher target, e.g. 500%)
+-- Asset Groups: Per subcategory

Campaign 2: PMax - Standard Margin
+-- Budget: 30% of total
+-- Bidding: Target ROAS (standard, e.g. 300%)
+-- Asset Groups: Per subcategory

Campaign 3: PMax - Low Margin / Clearance
+-- Budget: 10% of total
+-- Bidding: Maximize Conversion Value
+-- Asset Groups: Per subcategory
```

### Structure 4: Standard Shopping Priority Tiers (Query Sculpting)

```
WHEN TO USE:
+-- Maximum control over bidding desired
+-- Experience with Shopping campaigns
+-- Want to route specific queries to specific campaigns
+-- Budget >$5k/mo

SETUP:
Campaign A: Shopping - Brand + Top Products (Priority LOW = 0)
+-- Contains only your top 20% products
+-- NO negatives -> catches everything not caught by B/C
+-- Highest bids
+-- Bidding: Manual CPC or Enhanced CPC

Campaign B: Shopping - Category Terms (Priority MEDIUM = 1)
+-- All products
+-- Negative keywords: branded + exact product terms
+-- Medium bids
+-- Bidding: Manual CPC or Target ROAS

Campaign C: Shopping - Generic/Discovery (Priority HIGH = 2)
+-- All products
+-- Negative keywords: branded + category + product terms
+-- Lowest bids (discover new queries)
+-- Bidding: Manual CPC with low budget

HOW QUERY SCULPTING WORKS:
+-- Search query: "nike air max 90 black"
|   +-- Campaign C (priority 2): Checked first -> "nike" is negative -> SKIP
|   +-- Campaign B (priority 1): Checked -> "nike air max" is negative -> SKIP
|   +-- Campaign A (priority 0): MATCH -> Shows ad with high bid
|
+-- Search query: "men's running shoes"
|   +-- Campaign C (priority 2): -> "running shoes" is negative -> SKIP
|   +-- Campaign B (priority 1): MATCH -> Shows ad with medium bid
|   +-- Campaign A: Not reached
|
+-- Search query: "cheap sports shoes"
    +-- Campaign C (priority 2): MATCH -> Shows ad with low bid
    +-- Campaign B/A: Not reached
    +-- Result: Generic query = lower bid = discovery
```

**Setting negatives via google_ads_mutate (Recipe #7):**

```json
operations=[
    {"campaignCriterionOperation": {"create": {
        "campaign": "customers/{CID}/campaigns/{CAMPAIGN_B_ID}",
        "negative": true,
        "keyword": {"text": "[brand name]", "matchType": "PHRASE"}
    }}},
    {"campaignCriterionOperation": {"create": {
        "campaign": "customers/{CID}/campaigns/{CAMPAIGN_C_ID}",
        "negative": true,
        "keyword": {"text": "[brand name]", "matchType": "PHRASE"}
    }}},
    {"campaignCriterionOperation": {"create": {
        "campaign": "customers/{CID}/campaigns/{CAMPAIGN_C_ID}",
        "negative": true,
        "keyword": {"text": "category term", "matchType": "PHRASE"}
    }}}
]
```

### Structure 5: Standard Shopping (Brand) + PMax (Non-Brand)

```
WHEN TO USE:
+-- Brand traffic converts well and predictably
+-- Want to keep brand CPC low
+-- PMax for non-brand discovery
+-- Budget >$3k/mo

SETUP:
Campaign 1: Standard Shopping - Brand Only
+-- Priority: LOW (catches brand queries)
+-- Negative keywords: generic terms
+-- Bidding: Manual CPC (low cost for brand)
+-- Budget: 20-30% of total
+-- All products

Campaign 2: PMax Retail - Non-Brand
+-- Brand exclusions set up (Recipe #7)
+-- Asset groups per category/margin
+-- Bidding: Target ROAS or Max Conv Value
+-- Budget: 70-80% of total
+-- Focus on new customers
```

### Structure 6: PMax (Bestsellers) + Standard Shopping (Long Tail)

```
WHEN TO USE:
+-- Large product catalog (500+ products)
+-- Clear top 20% products
+-- PMax works well for bestsellers
+-- Long tail products have too little data for PMax
+-- Budget >$5k/mo

SETUP:
Campaign 1: PMax Retail - Top 100 Bestsellers
+-- Custom Label: "bestseller"
+-- Asset groups: Per category (3-5)
+-- Bidding: Target ROAS
+-- Budget: 60-70% of total
+-- Regularly update which products are "bestseller"

Campaign 2: Standard Shopping - Remaining Products
+-- All products MINUS bestsellers
+-- Bidding: Enhanced CPC or Target ROAS
+-- Budget: 30-40% of total
+-- Goal: collect data, discover new bestsellers
```

### Structure 7: Campaign Orchestration (4-Level Framework)

```
WHEN TO USE:
+-- Enterprise accounts (>$20k/mo)
+-- Maximum control + maximum scale
+-- Team with PPC experience
+-- 1000+ products

4-LEVEL ORCHESTRATION:
======================

Level 1: BRAND SEARCH (Standard Search)
+-- Exact match brand keywords
+-- Lowest CPA in account
+-- Protects brand against PMax

Level 2: BRANDED SHOPPING (Standard Shopping, Priority LOW)
+-- Catches branded shopping queries
+-- Manual CPC (low, brand converts)
+-- All products

Level 3: PMAX RETAIL (Performance Max)
+-- Brand exclusions active
+-- Asset groups per segment
+-- Focus on non-brand discovery
+-- Largest budget allocation (50-60%)

Level 4: GENERIC SHOPPING CATCHALL (Standard Shopping, Priority HIGH)
+-- Lowest bids
+-- Catches what PMax misses
+-- Budget: 5-10% as safety net
+-- Data discovery for new products/queries
```

## 4 Structures That DON'T Work

```
AVOID THESE STRUCTURES
=========================

X 1. Standard Shopping Manual Bidding + Few Products (<20)
+-- Problem: Too little data for manual optimization
+-- Result: Inconsistent performance, no learning
+-- Better: PMax Retail with 1-2 asset groups

X 2. PMax with 1 Asset Group for 500+ Products
+-- Problem: Google can't create personalized ads
+-- Result: Generic assets for all products
+-- Better: At least 3-5 asset groups per category

X 3. Overlapping PMax Campaigns Without Product Exclusions
+-- Problem: Campaigns bid against each other
+-- Result: Higher CPCs, wasted budget
+-- Better: Clear product splits via listing group filters

X 4. Standard Shopping Without Priority Setup (with multiple campaigns)
+-- Problem: Random which campaign wins the auction
+-- Result: Unpredictable query matching
+-- Better: Priority tiers (HIGH/MEDIUM/LOW) + negatives
```

## Product Group Subdivision Strategy

### When to Use Which Attribute

| Attribute | Use when | Example |
|-----------|----------|---------|
| productBrand | Selling multiple brands | Nike vs Adidas vs own brand |
| productType | Hierarchical categories | Clothing > Men's > Shirts |
| productCustomAttribute (Label 0-4) | Business-specific segmentation | Margin tier, season, bestseller |
| productItemId | Targeting individual products | Top 10 bestsellers separately |
| productChannel | Online vs local | Webshop vs physical store |

### GAQL: Analyze Existing Listing Groups

```sql
SELECT ad_group.name, ad_group_criterion.listing_group.type,
    ad_group_criterion.listing_group.case_value.product_brand.value,
    ad_group_criterion.listing_group.case_value.product_type.value,
    ad_group_criterion.cpc_bid_micros
FROM ad_group_criterion
WHERE ad_group_criterion.type = 'LISTING_GROUP'
```

### Mutate: Product Group Subdivisions (Standard Shopping)

Via `google_ads_mutate` recipe for listing group subdivision:

```json
operations=[
    {"adGroupCriterionOperation": {"create": {
        "adGroup": "customers/{CID}/adGroups/{AG_ID}",
        "listingGroupInfo": {
            "type": "SUBDIVISION",
            "caseValue": {"productBrand": {"value": null}}
        }
    }}},
    {"adGroupCriterionOperation": {"create": {
        "adGroup": "customers/{CID}/adGroups/{AG_ID}",
        "listingGroupInfo": {
            "type": "UNIT",
            "caseValue": {"productBrand": {"value": "Nike"}}
        },
        "cpcBidMicros": "1500000"
    }}},
    {"adGroupCriterionOperation": {"create": {
        "adGroup": "customers/{CID}/adGroups/{AG_ID}",
        "listingGroupInfo": {
            "type": "UNIT",
            "caseValue": {"productBrand": {"value": "Adidas"}}
        },
        "cpcBidMicros": "1200000"
    }}}
]
```

### PMax Listing Group Filters (Asset Group Level)

Via `google_ads_mutate` -- `assetGroupListingGroupFilterOperation`:

```json
operations=[
    {"assetGroupListingGroupFilterOperation": {"create": {
        "assetGroup": "customers/{CID}/assetGroups/{AG_ID}",
        "type": "UNIT_INCLUDED",
        "vertical": "SHOPPING",
        "caseValue": {"productBrand": {"value": "Nike"}}
    }}}
]
```

## Migration Checklist

### Standard Shopping -> PMax

```
MIGRATION: STANDARD SHOPPING -> PMAX
====================================

[ ] PRE-MIGRATION (Week 1)
+-- Export current Shopping performance data (30d + 90d)
+-- Identify top performing products/categories
+-- Collect creative assets (images, headlines, descriptions)
+-- Plan asset group structure
+-- Check Merchant Center feed health

[ ] SETUP (Week 2)
+-- Create PMax Retail campaign (PAUSED)
+-- Configure asset groups with listing group filters
+-- Add all assets (max per type)
+-- Set audience signals
+-- Set brand exclusions (if Brand Search active)
+-- Validate with google_ads_mutate validate_only=True

[ ] LAUNCH (Week 3)
+-- Activate PMax campaign
+-- Reduce Standard Shopping budget by 50%
+-- Monitor daily: PMax vs Shopping performance
+-- DO NOT: Turn off Standard Shopping immediately

[ ] TRANSITION (Week 4-5)
+-- If PMax ROAS >= Shopping ROAS: Reduce Shopping further
+-- If PMax ROAS < Shopping ROAS: Wait, PMax still in learning
+-- After 2 weeks stable: Pause Shopping
+-- Keep Shopping as catchall (low budget) or pause

[ ] POST-MIGRATION (Week 6+)
+-- Compare: Total account performance before/after
+-- Monitor search terms for irrelevance
+-- Optimize asset groups based on data
+-- Evaluate after 30 days fully on PMax
```

### PMax -> Standard Shopping

```
MIGRATION: PMAX -> STANDARD SHOPPING (switching back)
=====================================================

[ ] Reasons to switch back:
+-- PMax ROAS consistently lower than historical Shopping
+-- Too little control over search queries
+-- Budget going to irrelevant channels
+-- Brand cannibalization not resolvable

[ ] APPROACH:
+-- Create Standard Shopping campaign (PAUSED)
+-- Configure product groups and bids
+-- Set priority (if multiple Shopping campaigns)
+-- Activate Standard Shopping
+-- Reduce PMax budget gradually (25% per week)
+-- After 4 weeks: Evaluate, potentially pause PMax
```

## 2026 Updates: PMax Negative Keywords

- **Campaign-level negative keywords** are now fully supported in PMax (API v20+). No need to use brand exclusion lists as a workaround — add negatives directly to PMax campaigns via `google_ads_mutate` Recipe #7.
- **Search term reporting** now available for PMax (API v21+) — use `search_term_view` with `PERFORMANCE_MAX` filter to see which queries PMax is serving.
- **`url_expansion_opt_out`** was removed in API v22 — this parameter no longer exists.
- **Smart Bidding Exploration** (v21+): An optional signal that lets Smart Bidding test broader traffic to find new converting segments. Can be enabled per campaign.

### GAQL: Check Existing PMax Negative Keywords

```sql
SELECT campaign.name, campaign_criterion.keyword.text,
    campaign_criterion.keyword.match_type,
    campaign_criterion.negative
FROM campaign_criterion
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
AND campaign_criterion.negative = TRUE
```

## Tools Reference

| Action | Tool | Recipe/Query |
|--------|------|--------------|
| Create Shopping campaign | `google_ads_mutate` | Recipe #17 |
| Create PMax Retail | `google_ads_mutate` | Recipe #19 |
| Pause campaign | `google_ads_mutate` | Recipe #2 |
| Change budget | `google_ads_mutate` | Recipe #3 |
| Negative keywords | `google_ads_mutate` | Recipe #7 |
| Analyze listing groups | `google_ads_run_gaql` | Listing groups recipe |
| Shopping performance | `google_ads_run_gaql` | Shopping performance recipe |
| Merchant Center detection | `google_ads_run_gaql` | Merchant Center link recipe |
| Look up accounts | `google_ads_list_accounts` | -- |
| Keyword research | `google_ads_run_keyword_planner` | Seed keywords |
