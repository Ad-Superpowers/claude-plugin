---
name: ga4-revenue-analysis
description: "This skill should be used when the user asks to \"analyze GA4 revenue\", \"review product performance\", \"build a checkout funnel\", or mentions \"purchase journey insights\", \"e-commerce KPI dashboard\", or \"revenue trends in GA4\". Do NOT use for: e-commerce event implementation (use ga4-ecommerce-setup), promotion and coupon tracking (use ga4-promotion-tracking)."
---
# GA4 Revenue Analysis Guide

Complete guide for analyzing e-commerce revenue, product performance, and checkout funnels in Google Analytics 4.

## Quick Decision Tree

```
GA4 REVENUE ANALYSIS FLOW
|
+---> WHAT DO YOU WANT TO ANALYZE?
|   +---> Overall revenue & trends
|   |   +---> Monetization overview report
|   |       +---> Date comparison for trends
|   |
|   +---> Product performance
|   |   +---> E-commerce purchases report
|   |       +---> Items viewed vs purchased
|   |
|   +---> Checkout dropoff
|   |   +---> Custom funnel exploration
|   |       +---> Checkout step analysis
|   |
|   +---> Customer journey
|       +---> Path exploration
|           +---> Purchase path analysis
|
+---> WHICH DIMENSIONS NEEDED?
|   +---> Traffic source impact
|   |   +---> Session source/medium breakdown
|   |
|   +---> Device/platform
|   |   +---> Device category, platform
|   |
|   +---> Audience segments
|       +---> Custom segments or audiences
|
+---> REPORTING NEEDS?
    +---> Ad-hoc analysis
    |   +---> Explorations (free-form analysis)
    |
    +---> Recurring reports
    |   +---> Custom reports in Library
    |
    +---> External dashboards
        +---> Looker Studio / BigQuery export
```

## Monetization Reports Overview

```
GA4 MONETIZATION REPORTS
========================

LOCATION: Reports -> Monetization

AVAILABLE REPORTS:
+-------------------------+------------------------------------------+
| Report                  | Shows                                    |
+-------------------------+------------------------------------------+
| Overview                | Revenue KPIs, trends, top items          |
+-------------------------+------------------------------------------+
| E-commerce purchases    | Product-level metrics (views, carts,     |
|                         | purchases, revenue)                      |
+-------------------------+------------------------------------------+
| In-app purchases        | App subscription/purchase data           |
+-------------------------+------------------------------------------+
| Publisher ads           | Ad revenue (AdMob/Ad Manager)            |
+-------------------------+------------------------------------------+
| Promotions              | Promotion performance                    |
+-------------------------+------------------------------------------+

MONETIZATION OVERVIEW METRICS:
------------------------------
+-------------------------+------------------------------------------+
| Metric                  | Definition                               |
+-------------------------+------------------------------------------+
| Total revenue           | purchase + in_app_purchase + ad revenue  |
+-------------------------+------------------------------------------+
| E-commerce revenue      | Purchase event revenue only              |
+-------------------------+------------------------------------------+
| Total purchasers        | Unique users with purchase event         |
+-------------------------+------------------------------------------+
| First-time purchasers   | Users with their first ever purchase     |
+-------------------------+------------------------------------------+
| ARPPU                   | Average Revenue Per Paying User          |
+-------------------------+------------------------------------------+
| Average purchase value  | Average order value                      |
+-------------------------+------------------------------------------+
```

## Product Performance Analysis

```
E-COMMERCE PURCHASES REPORT
============================

LOCATION: Reports -> Monetization -> E-commerce purchases

KEY METRICS PER PRODUCT:
+-------------------------+------------------------------------------+
| Metric                  | Meaning                                  |
+-------------------------+------------------------------------------+
| Items viewed            | Number of view_item events               |
+-------------------------+------------------------------------------+
| Items added to cart     | Number of add_to_cart events             |
+-------------------------+------------------------------------------+
| Items purchased         | Number of items in purchase events       |
+-------------------------+------------------------------------------+
| Item revenue            | Total revenue per product                |
+-------------------------+------------------------------------------+
| Cart-to-view rate       | (added to cart / viewed) x 100%          |
+-------------------------+------------------------------------------+
| Purchase-to-view rate   | (purchased / viewed) x 100%             |
+-------------------------+------------------------------------------+

AVAILABLE DIMENSIONS:
+-- Item name
+-- Item ID
+-- Item brand
+-- Item category (1-5 levels)
+-- Item variant
+-- Item list name

ANALYSIS TIPS:
--------------
1. VIEW-TO-CART RATE < 5%
   +-- Product page optimization needed
       +-- Better product photos
       +-- Clearer pricing
       +-- Improve product descriptions

2. CART-TO-PURCHASE RATE < 30%
   +-- Checkout optimization needed
       +-- Make shipping costs clearer
       +-- Add trust badges
       +-- Simplify checkout

3. HIGH VIEWS, LOW REVENUE
   +-- Investigate product issues
       +-- Pricing vs competition
       +-- Stock availability
       +-- Product-market fit
```

## Checkout Funnel Analysis

```
CHECKOUT FUNNEL EXPLORATION
============================

LOCATION: Explore -> Funnel exploration

SETUP STEPS:
+----+--------------------------------------------------------------------+
| 1  | Explore -> Blank -> Choose "Funnel exploration"                    |
+----+--------------------------------------------------------------------+
| 2  | Tab Settings -> Steps -> Edit                                      |
+----+--------------------------------------------------------------------+
| 3  | Add checkout events as steps:                                      |
|    | +-- Step 1: view_cart                                              |
|    | +-- Step 2: begin_checkout                                        |
|    | +-- Step 3: add_shipping_info                                     |
|    | +-- Step 4: add_payment_info                                      |
|    | +-- Step 5: purchase                                              |
+----+--------------------------------------------------------------------+
| 4  | Optional: Make steps "closed" for strict sequence                  |
+----+--------------------------------------------------------------------+
| 5  | Add breakdown (device, source, etc.)                               |
+----+--------------------------------------------------------------------+

FUNNEL METRICS:
---------------
+-------------------------+------------------------------------------+
| Metric                  | Meaning                                  |
+-------------------------+------------------------------------------+
| Users (per step)        | Unique users reaching step               |
+-------------------------+------------------------------------------+
| Completion rate         | % users reaching next step               |
+-------------------------+------------------------------------------+
| Abandonment rate        | % users dropping off at step             |
+-------------------------+------------------------------------------+
| Time to convert         | Average time through funnel              |
+-------------------------+------------------------------------------+

BENCHMARK COMPLETION RATES:
----------------------------
+-------------------------+--------------+---------------------------+
| Step                    | Benchmark    | Action if lower           |
+-------------------------+--------------+---------------------------+
| Cart -> Checkout        | 50-70%       | Cart abandonment emails   |
+-------------------------+--------------+---------------------------+
| Checkout -> Shipping    | 70-85%       | Simplify form fields      |
+-------------------------+--------------+---------------------------+
| Shipping -> Payment     | 80-90%       | More shipping options     |
+-------------------------+--------------+---------------------------+
| Payment -> Purchase     | 70-85%       | More payment options      |
+-------------------------+--------------+---------------------------+
| Overall funnel          | 25-40%       | End-to-end optimization   |
+-------------------------+--------------+---------------------------+
```

## Revenue per Traffic Source

```
TRAFFIC SOURCE REVENUE ANALYSIS
================================

LOCATION: Reports -> Acquisition -> Traffic acquisition

ADDING SECONDARY DIMENSION:
----------------------------
1. Click "+" next to primary dimension
2. Select "E-commerce" -> "Total revenue"
3. Or add metrics via "Edit comparisons"

CUSTOM EXPLORATION FOR REVENUE:
-------------------------------
SETUP:
+-- Technique: Free form
+-- Rows: Session source/medium
+-- Values:
|   +-- Total revenue
|   +-- Transactions
|   +-- Average purchase value
|   +-- E-commerce conversion rate
|   +-- Sessions
+-- Filter: Only sessions with transactions (optional)

KEY ANALYSES:
-------------
1. REVENUE PER SOURCE
   +-- Which sources generate the most revenue?
   +-- Which have the highest conversion rate?
   +-- Which have the highest AOV?

2. ROAS CALCULATION (manual)
   +-- Export revenue per source
   +-- Match with ad spend data
   +-- Calculate: Revenue / Ad Spend

3. ASSISTED CONVERSIONS
   +-- Which sources assist purchases?
   +-- See Attribution -> Conversion paths
```

## Key E-commerce KPIs

```
ESSENTIAL E-COMMERCE KPIs
==========================

REVENUE KPIs:
+-------------------------+------------------------------------------+
| KPI                     | Calculation / Location                   |
+-------------------------+------------------------------------------+
| Total Revenue           | Monetization -> Overview                 |
+-------------------------+------------------------------------------+
| Average Order Value     | Total revenue / Transactions             |
| (AOV)                   |                                          |
+-------------------------+------------------------------------------+
| Revenue per Session     | Total revenue / Sessions                 |
| (RPS)                   |                                          |
+-------------------------+------------------------------------------+
| Revenue per User        | Total revenue / Total users              |
| (RPU)                   |                                          |
+-------------------------+------------------------------------------+
| Customer Lifetime       | Requires cohort analysis                 |
| Value (CLV)             |                                          |
+-------------------------+------------------------------------------+

CONVERSION KPIs:
+-------------------------+------------------------------------------+
| KPI                     | Calculation                              |
+-------------------------+------------------------------------------+
| E-commerce Conv. Rate   | Purchasers / Total users x 100%         |
+-------------------------+------------------------------------------+
| Cart Abandonment Rate   | (Carts - Purchases) / Carts x 100%      |
+-------------------------+------------------------------------------+
| Checkout Abandon Rate   | (Checkouts - Purchases) / Checkouts     |
+-------------------------+------------------------------------------+
| Add-to-Cart Rate        | Add to cart users / Total users x 100%   |
+-------------------------+------------------------------------------+

PRODUCT KPIs:
+-------------------------+------------------------------------------+
| KPI                     | Calculation                              |
+-------------------------+------------------------------------------+
| Product View Rate       | Item views / Sessions x 100%            |
+-------------------------+------------------------------------------+
| Cart-to-Detail Rate     | Add to cart / Item views x 100%          |
+-------------------------+------------------------------------------+
| Buy-to-Detail Rate      | Purchases / Item views x 100%            |
+-------------------------+------------------------------------------+
| Average Items/Order     | Items purchased / Transactions           |
+-------------------------+------------------------------------------+
```

## Custom Explorations for E-commerce

```
EXPLORATION 1: PRODUCT CATEGORY PERFORMANCE
============================================

SETUP:
+-- Technique: Free form
+-- Rows: Item category
+-- Values:
|   +-- Item revenue
|   +-- Items purchased
|   +-- Item views
|   +-- Cart-to-view rate
|   +-- Purchase-to-view rate
+-- Filters: Date range

INSIGHTS:
+-- Which categories perform best?
+-- Where are optimization opportunities?
+-- Category growth trends

EXPLORATION 2: DEVICE REVENUE COMPARISON
=========================================

SETUP:
+-- Technique: Free form
+-- Rows: Device category
+-- Values:
|   +-- Total revenue
|   +-- Transactions
|   +-- Average purchase value
|   +-- E-commerce conversion rate
|   +-- Sessions
+-- Visualization: Bar chart

INSIGHTS:
+-- Mobile vs Desktop conversion gaps
+-- Where is mobile optimization needed?
+-- Cross-device journey impact

EXPLORATION 3: NEW VS RETURNING PURCHASERS
==========================================

SETUP:
+-- Technique: Free form
+-- Rows: New/established
+-- Values:
|   +-- Total revenue
|   +-- First-time purchasers
|   +-- Purchasers
|   +-- Average purchase value
|   +-- Transactions
+-- Segment by time for trends

INSIGHTS:
+-- Retention health check
+-- New customer acquisition cost
+-- Repeat purchase rate
```

## Cohort Analysis for CLV

```
PURCHASER COHORT ANALYSIS
==========================

LOCATION: Explore -> Cohort exploration

SETUP:
+----+--------------------------------------------------------------------+
| 1  | Cohort inclusion: first_open or first_visit                        |
+----+--------------------------------------------------------------------+
| 2  | Return criteria: purchase (or custom purchase event)               |
+----+--------------------------------------------------------------------+
| 3  | Cohort granularity: Weekly or Monthly                              |
+----+--------------------------------------------------------------------+
| 4  | Values: User retention or Event count or Metric sum                |
+----+--------------------------------------------------------------------+
| 5  | Breakdown: Traffic source (optional)                               |
+----+--------------------------------------------------------------------+

COHORT METRIC OPTIONS:
----------------------
+-- User retention: % users who return and purchase
+-- Event count: Number of purchases per cohort over time
+-- Metric sum: Revenue per cohort over time

ANALYSIS QUESTIONS:
-------------------
+-- What % repurchases after 30/60/90 days?
+-- Which acquisition source has the best CLV?
+-- How long until repeat purchase?
+-- Which cohorts (seasons) perform best?

PREDICTIVE CLV CALCULATION:
---------------------------
CLV = AOV x Purchase Frequency x Customer Lifespan

Example:
+-- AOV: $75
+-- Purchases per year: 3
+-- Average customer lifespan: 2.5 years
+-- CLV = $75 x 3 x 2.5 = $562.50
```

## Common Problems

```
TROUBLESHOOTING REVENUE ANALYSIS
==================================

PROBLEM: Revenue shows $0 or is missing
-----------------------------------------
Causes:
+-- purchase event not implemented
+-- value parameter missing
+-- Currency not configured
+-- Data processing delay (24-48 hours)
+-- Filters in report

Solution:
+-- Verify purchase event in DebugView
+-- Check dataLayer for value parameter
+-- Check property currency setting
+-- Wait for data processing
+-- Remove report filters and test again

PROBLEM: AOV unrealistically high/low
--------------------------------------
Causes:
+-- Test transactions in data
+-- Duplicate purchases
+-- Pricing in wrong currency
+-- Tax/shipping incorrectly included
+-- Item quantities wrong

Solution:
+-- Exclude test orders with segment
+-- Check transaction_id duplicates
+-- Verify currency matching
+-- Review value calculation in code
+-- Audit quantity parameters

PROBLEM: Product data not visible
----------------------------------
Causes:
+-- items array missing in events
+-- Item parameters incorrect
+-- item_id/item_name missing
+-- GA4 report processing time
+-- Insufficient data volume

Solution:
+-- Check items array in dataLayer
+-- Verify required item parameters
+-- Ensure item_id and item_name present
+-- Wait 24-48 hours for processing
+-- Select longer date range

PROBLEM: Funnel shows no data
------------------------------
Causes:
+-- Checkout events not implemented
+-- Event names incorrect
+-- Closed funnel too strict
+-- Segment filters too narrow
+-- Date range too short

Solution:
+-- Verify all checkout events are active
+-- Check exact event names in DebugView
+-- Make funnel "open" for testing
+-- Remove or broaden segments
+-- Select longer date range
```

## MCP Tool: Pull Revenue Reports

```python
# Overall revenue by source/medium (last 30 days)
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["totalRevenue", "ecommercePurchases", "averagePurchaseRevenue", "sessionKeyEventRate"],
    dimensions=["sessionSourceMedium"],
    start_date="30daysAgo",
    end_date="yesterday"
)

# Top products by revenue
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["itemRevenue", "itemsPurchased", "itemsViewed"],
    dimensions=["itemName", "itemCategory"],
    start_date="30daysAgo",
    end_date="yesterday"
)

# Revenue trend by day (for anomaly detection)
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["totalRevenue", "ecommercePurchases", "averagePurchaseRevenue"],
    dimensions=["date"],
    start_date="60daysAgo",
    end_date="yesterday"
)
```

## Output: Revenue Analysis Report Template

```markdown
# GA4 Revenue Analysis Report

## Reporting Period
- **From:** [Start date]
- **To:** [End date]
- **Comparison:** [Previous period/Previous year]

## Executive Summary

| KPI | Current Period | Comparison | Trend |
|-----|----------------|------------|-------|
| Total Revenue | $XX,XXX | $XX,XXX | +X% |
| Transactions | X,XXX | X,XXX | +X% |
| Average Order Value | $XX.XX | $XX.XX | +X% |
| Conversion Rate | X.X% | X.X% | +X% |
| Cart Abandonment | XX% | XX% | -X% |

## Revenue per Traffic Source

| Source/Medium | Revenue | % of Total | Conv. Rate | AOV |
|---------------|---------|------------|------------|-----|
| google / organic | $X,XXX | XX% | X.X% | $XX |
| google / cpc | $X,XXX | XX% | X.X% | $XX |
| direct / (none) | $X,XXX | XX% | X.X% | $XX |
| [Other] | $X,XXX | XX% | X.X% | $XX |

## Top 10 Products (Revenue)

| Product | Revenue | Units Sold | View-to-Cart | Cart-to-Purchase |
|---------|---------|------------|--------------|------------------|
| [Product 1] | $X,XXX | XXX | XX% | XX% |
| [Product 2] | $X,XXX | XXX | XX% | XX% |
| ... | ... | ... | ... | ... |

## Category Performance

| Category | Revenue | Growth | Contribution |
|----------|---------|--------|--------------|
| [Category 1] | $X,XXX | +XX% | XX% |
| [Category 2] | $X,XXX | +XX% | XX% |
| [Category 3] | $X,XXX | -XX% | XX% |

## Checkout Funnel Performance

| Step | Users | Drop-off | Benchmark |
|------|-------|----------|-----------|
| View Cart | X,XXX | - | - |
| Begin Checkout | X,XXX | XX% | 30-50% |
| Add Shipping | X,XXX | XX% | 15-30% |
| Add Payment | X,XXX | XX% | 10-20% |
| Purchase | X,XXX | XX% | 15-30% |

**Overall Funnel Conversion:** XX% (benchmark: 25-40%)

## Device Breakdown

| Device | Revenue | % Share | Conv. Rate | AOV |
|--------|---------|---------|------------|-----|
| Desktop | $X,XXX | XX% | X.X% | $XX |
| Mobile | $X,XXX | XX% | X.X% | $XX |
| Tablet | $X,XXX | XX% | X.X% | $XX |

## Key Insights

### Positive Trends
1. [Insight 1]
2. [Insight 2]

### Areas of Concern
1. [Issue 1] - Impact: [High/Medium/Low]
2. [Issue 2] - Impact: [High/Medium/Low]

## Recommendations

| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| HIGH | [Action 1] | +XX% revenue |
| MEDIUM | [Action 2] | +XX% conversion |
| LOW | [Action 3] | UX improvement |

## Next Steps
1. [ ] [First action]
2. [ ] [Second action]
3. [ ] [Third action]
```
