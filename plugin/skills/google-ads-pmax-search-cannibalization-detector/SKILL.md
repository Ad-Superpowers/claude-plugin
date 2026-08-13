---
name: google-ads-pmax-search-cannibalization-detector
description: "This skill should be used when the user asks to \"detect PMax Search cannibalization\", \"check if PMax is stealing brand traffic\", \"analyze branded ROAS inflation\", \"set up brand exclusions\", or mentions \"PMax cannibalizing Search\", \"incrementality testing\", or \"PMax stealing traffic\". Do NOT use for: general PMax optimization (use performance-max-optimizer), SEO vs SEA keyword gaps (use seo-sea-keyword-gap-analyzer), Shopping structure advice (use shopping-campaign-structure-advisor)."
---
# PMax Search Cannibalization Detector

Framework for detecting and resolving Performance Max stealing Search campaign traffic. The #1 frustration in the PPC community -- PMax claims branded conversions making ROAS appear artificially high.

## Quick Diagnosis

```
IS PMAX CANNIBALIZING YOUR SEARCH?
====================================

Step 1: Check PMax search terms report
        -> Many branded terms? --> PROBABLY YES

Step 2: Compare blended vs non-brand ROAS
        -> PMax ROAS 2x higher than Search? --> RED FLAG

Step 3: Check Search campaign metrics since PMax launch
        -> Search impressions/clicks dropped? --> CONFIRMED

RISK LEVELS:
+-- LOW:      <20% brand traffic in PMax search terms
+-- MEDIUM:   20-50% brand traffic -> monitor + consider exclusion
+-- HIGH:     50-70% brand traffic -> enable brand exclusion
+-- CRITICAL: >70% brand traffic -> PMax ROAS is misleading
```

## Step 1: Data Collection

### 1A: PMax Search Terms Report

Use `google_ads_run_gaql` to retrieve PMax search terms:

```sql
SELECT campaign.name, search_term_view.search_term,
    metrics.impressions, metrics.clicks, metrics.cost_micros,
    metrics.conversions, metrics.conversions_value
FROM search_term_view
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
LIMIT 200
```

### 1B: Search Campaign Search Terms

```sql
SELECT campaign.name, search_term_view.search_term,
    metrics.impressions, metrics.clicks, metrics.cost_micros,
    metrics.conversions, metrics.conversions_value
FROM search_term_view
WHERE campaign.advertising_channel_type = 'SEARCH'
AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
LIMIT 200
```

### 1C: Campaign Performance per Channel Type

```sql
SELECT campaign.name, campaign.advertising_channel_type,
    campaign.status, metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions,
    metrics.conversions_value, metrics.search_impression_share
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
```

### 1D: PMax Channel-Level Breakdown (where the budget goes)

Available from API v22+: `segments.ad_network_type` works in PMax campaigns, enabling per-channel cost/conversion breakdown.

```sql
SELECT campaign.name, segments.ad_network_type,
    metrics.impressions, metrics.clicks, metrics.cost_micros,
    metrics.conversions, metrics.conversions_value
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

Network type values: `SEARCH`, `SEARCH_PARTNERS`, `CONTENT` (Display/YouTube), `MIXED`.

## Step 2: Brand Traffic Analysis

### Brand vs Non-Brand Classification

```
BRAND TRAFFIC IDENTIFICATION
============================

Step 1: Define brand terms
+-- Exact brand name + variations
+-- Brand + product combinations
+-- Common typos of brand name
+-- URL-based searches (domain.com)

Step 2: Classify PMax search terms
+-- BRANDED:     Contains brand name or variation
+-- NON-BRANDED: No brand reference
+-- AMBIGUOUS:   Could be either (e.g., product name = brand name)

Step 3: Calculate ratios
+-- Brand Traffic %  = branded impressions / total PMax impressions
+-- Brand Spend %    = branded cost / total PMax cost
+-- Brand Conv %     = branded conversions / total PMax conversions
+-- Brand ROAS       = branded conv value / branded cost
```

### ROAS Inflation Calculation

```
ROAS INFLATION FRAMEWORK
========================

Blended PMax ROAS = Total conversion value / Total cost
Non-Brand PMax ROAS = Non-brand conversion value / Non-brand cost
Brand-Only ROAS = Brand conversion value / Brand cost

EXAMPLE:
+-- Blended PMax ROAS:   8.5x  <-- This is what Google reports
+-- Brand-Only ROAS:     15.0x <-- Brand traffic always converts well
+-- Non-Brand PMax ROAS: 3.2x  <-- THIS is your real PMax performance
+-- Search Campaign ROAS: 4.1x <-- Compare with this

INFLATION RATIO = Blended ROAS / Non-Brand ROAS
+-- <1.5x -> Minimal inflation
+-- 1.5-2.5x -> Significant inflation
+-- >2.5x -> Severe inflation, PMax claiming mainly brand conversions
```

## Step 3: Decision Tree -- Brand Exclusions

```
BRAND EXCLUSION DECISION TREE
==============================

Do you have a dedicated Brand Search campaign?
|
+---> NO
|   +---> FIRST: Create Brand Search campaign
|       +-- Exact match brand keywords
|       +-- High budget (brand converts cheaply)
|       +-- Wait 2-4 weeks for data -> go to YES
|
+---> YES -> Analyze PMax brand traffic %
    |
    +---> <20% brand traffic in PMax
    |   +---> NO ACTION NEEDED
    |       +-- PMax is finding mostly new traffic
    |       +-- Monitor monthly
    |
    +---> 20-50% brand traffic in PMax
    |   +---> CONSIDER BRAND EXCLUSION
    |       +-- Compare: Brand Search CPA vs PMax brand CPA
    |       +-- If Search cheaper -> enable exclusion
    |       +-- If PMax cheaper -> monitor, no action
    |
    +---> 50-70% brand traffic in PMax
    |   +---> BRAND EXCLUSION RECOMMENDED
    |       +-- PMax ROAS is misleading
    |       +-- Brand Search campaign is more efficient
    |       +-- Implement exclusion (see action recipes)
    |
    +---> >70% brand traffic in PMax
        +---> BRAND EXCLUSION REQUIRED
            +-- PMax is functioning as expensive Brand campaign
            +-- Non-brand ROAS is probably low
            +-- Also consider: is PMax even valuable?
```

## Step 4: Setting Up Brand Exclusions

### Via google_ads_mutate -- Campaign-Level Brand Exclusions

Add negative keywords to PMax campaign (Recipe #7):

```json
operations=[
    {"campaignCriterionOperation": {"create": {
        "campaign": "customers/{CID}/campaigns/{PMAX_CAMPAIGN_ID}",
        "negative": true,
        "keyword": {"text": "[brand name]", "matchType": "PHRASE"}
    }}},
    {"campaignCriterionOperation": {"create": {
        "campaign": "customers/{CID}/campaigns/{PMAX_CAMPAIGN_ID}",
        "negative": true,
        "keyword": {"text": "[brand variation]", "matchType": "PHRASE"}
    }}},
    {"campaignCriterionOperation": {"create": {
        "campaign": "customers/{CID}/campaigns/{PMAX_CAMPAIGN_ID}",
        "negative": true,
        "keyword": {"text": "[brand typo]", "matchType": "BROAD"}
    }}}
]
```

### Via Shared Negative Keyword List (Recipe #9)

Better for multiple PMax campaigns:

```json
operations=[
    {"sharedSetOperation": {"create": {
        "resourceName": "customers/{CID}/sharedSets/-10",
        "name": "Brand Exclusions - PMax", "type": "NEGATIVE_KEYWORDS"
    }}},
    {"sharedCriterionOperation": {"create": {
        "sharedSet": "customers/{CID}/sharedSets/-10",
        "keyword": {"text": "brand name", "matchType": "PHRASE"}
    }}},
    {"sharedCriterionOperation": {"create": {
        "sharedSet": "customers/{CID}/sharedSets/-10",
        "keyword": {"text": "brand.com", "matchType": "BROAD"}
    }}},
    {"campaignSharedSetOperation": {"create": {
        "campaign": "customers/{CID}/campaigns/{PMAX_CAMPAIGN_ID}",
        "sharedSet": "customers/{CID}/sharedSets/-10"
    }}}
]
```

## Step 5: Incrementality Testing Protocol

### 2-Week On/Off Test

```
INCREMENTALITY TEST PROTOCOL
==============================

GOAL: Determine if PMax actually delivers incremental conversions
      or only claims existing branded traffic.

WEEK 1-2: BASELINE (PMax ON)
+-- Record: Total account conversions
+-- Record: Search campaign conversions
+-- Record: PMax conversions
+-- Record: Total revenue

WEEK 3-4: TEST (PMax OFF)
+-- Pause PMax campaign
+-- Do NOT increase Search budget (important!)
+-- Measure: Total account conversions
+-- Measure: Search campaign conversions
+-- Measure: Total revenue

ANALYSIS:
+-- Total conversions dropped >20%?
|   +---> PMax delivers incremental value -> turn back on
+-- Total conversions dropped 5-20%?
|   +---> Mixed result -> PMax with brand exclusions
+-- Total conversions same or increased?
|   +---> PMax was only claiming brand traffic
+-- Search conversions increased while total stayed same?
    +---> Confirmed: PMax was cannibalizing Search
```

### Statistical Significance Checklist

```
SIGNIFICANCE REQUIREMENTS
========================

[ ] Minimum 100 conversions per phase (baseline + test)
[ ] Minimum 14 days per phase (seasonal effects)
[ ] No major external factors (sales, holidays, PR)
[ ] No other campaign changes during test
[ ] Budget kept constant
[ ] No new competitor activity

RELIABILITY:
+-- <100 conversions/phase -> Not reliable, extend test
+-- 100-500 conversions/phase -> Indicative
+-- >500 conversions/phase -> Statistically reliable
```

## Step 6: Monitoring After Exclusions

### GAQL Queries for Ongoing Monitoring

After setting brand exclusions, monitor weekly:

```sql
-- PMax performance after exclusions (compare with baseline)
SELECT campaign.name, metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions,
    metrics.conversions_value
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
AND segments.date DURING LAST_7_DAYS
```

```sql
-- Search campaign performance (should increase)
SELECT campaign.name, metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM campaign
WHERE campaign.advertising_channel_type = 'SEARCH'
AND segments.date DURING LAST_7_DAYS
```

### Expected Results After Brand Exclusion

```
WHAT TO EXPECT AFTER BRAND EXCLUSION
======================================

PMax Campaign:
+-- Impressions: -30 to -60% (normal, branded volume gone)
+-- Clicks: -20 to -50%
+-- ROAS: DROPS (this is the real non-brand ROAS)
+-- Conversions: -20 to -40%
+-- CPA: INCREASES (non-brand is more expensive, this is normal)

Search Campaigns:
+-- Impressions: +10 to +30% (brand traffic recaptured)
+-- Clicks: +15 to +40%
+-- ROAS: Same or INCREASES
+-- Conversions: +10 to +25%
+-- CPA: Same or DECREASES

Total Account:
+-- Conversions: Same or +5-10% (more efficient budget use)
+-- ROAS: Same or better (fairer distribution)
+-- CPA: Same or better
```

## 2026 Updates: PMax Negative Keywords + Search Term Reporting

- **Campaign-level negative keywords** are now supported in PMax (API v20+). Use `google_ads_mutate` Recipe #7 with `campaignCriterionOperation` — no longer limited to account-level negative lists.
- **Search term reporting** for PMax is available (API v21+): query `search_term_view` with `PERFORMANCE_MAX` filter (Step 1A above). This was not possible before v21 — if you had old reports showing no data, rerun.
- **`url_expansion_opt_out`** was removed in v22; URL expansion is now controlled via asset group settings.
- **Asset performance labels** (Best/Good/Low) were removed from the API in v22 — do not reference them in scripts.

## Benchmarks & Red Flags

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Brand traffic % in PMax | <20% | 20-50% | >50% |
| PMax ROAS / Non-Brand ROAS ratio | <1.5x | 1.5-2.5x | >2.5x |
| Search impressions after PMax launch | Stable | -10 to -25% | >-25% |
| PMax search term relevance | >70% relevant | 50-70% | <50% |
| Brand CPA: PMax vs Search | Comparable | PMax 1.5x more expensive | PMax 2x+ more expensive |

## Common Patterns

```
PATTERN 1: "Fantastic PMax ROAS"
+-- Symptom: PMax ROAS 10x+, Search ROAS 3-4x
+-- Cause: PMax claims branded last-click conversions
+-- Diagnosis: Check search terms -> >60% branded
+-- Solution: Brand exclusion -> real ROAS becomes visible

PATTERN 2: "Search performance declining"
+-- Symptom: Search impressions/clicks drop after PMax launch
+-- Cause: PMax wins branded auctions (higher Ad Rank)
+-- Diagnosis: Compare Search metrics before/after PMax
+-- Solution: Brand exclusion on PMax or priority structure

PATTERN 3: "PMax scales budget but no growth"
+-- Symptom: Higher PMax spend, but account ROAS drops
+-- Cause: PMax scales in branded traffic, not new customers
+-- Diagnosis: Calculate non-brand ROAS + incrementality test
+-- Solution: Brand exclusion + budget cap on PMax

PATTERN 4: "Conversion Value Rules not set"
+-- Symptom: All conversions weigh equally
+-- Cause: Brand conversions have different value than non-brand
+-- Diagnosis: Check if CVR differs per traffic source
+-- Solution: Set up value rules (Search Console scope)
```

## Tools Reference

| Action | Tool | Recipe/Query |
|-------|------|--------------|
| Get PMax search terms | `google_ads_run_gaql` | search_term_view + PERFORMANCE_MAX filter |
| Search campaign terms | `google_ads_run_gaql` | search_term_view + SEARCH filter |
| Campaign performance per type | `google_ads_run_gaql` | campaign + advertising_channel_type |
| Set brand exclusion | `google_ads_mutate` | Recipe #7 (negative keywords) |
| Shared brand exclusion list | `google_ads_mutate` | Recipe #9 (shared negative keyword list) |
| Pause PMax (incrementality test) | `google_ads_mutate` | Recipe #2 (pause campaign) |
| Look up accounts | `google_ads_list_accounts` | -- |
