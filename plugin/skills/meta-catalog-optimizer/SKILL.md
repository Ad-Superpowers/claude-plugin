---
name: meta-catalog-optimizer
description: "This skill should be used when the user asks to \"optimize product catalog\", \"improve catalog ad performance\", \"fix catalog feed issues\", or mentions \"Advantage+ Catalog Ads\", \"product set strategy\", or \"catalog feed optimization\". Do NOT use for: campaign structure (use campaign-structure-advisor), creative diversification (use creative-diversification-generator), full-funnel design (use full-funnel-designer)."
---
# Catalog Optimizer

## Overview

This skill helps optimize Meta Product Catalogs for maximum Advantage+ Catalog Ads and Advantage+ Sales performance, including feed optimization, product set strategies, and troubleshooting of common issues.

> **Heads-up: catalog data is not reachable through MCP yet.** This release ships no catalog tool, so catalogs, product sets, and product-set items can be neither read nor created through Ad Superpowers. Use this skill for feed and product-set **strategy and diagnosis**, then build and inspect the catalog ad in Ads Manager. For non-catalog ad creation via MCP, `use ad-launch-playbook`.

## Catalog Fundamentals

### Catalog Ecosystem

```
┌─────────────────────────────────────────────────────────────────┐
│  META CATALOG STRUCTURE                                         │
│                                                                 │
│  DATA FEED (your source)                                        │
│  ├── Shopify, WooCommerce, Magento feed                         │
│  ├── Google Merchant Center feed                                │
│  └── Custom CSV/XML feed                                        │
│         │                                                       │
│         v                                                       │
│  PRODUCT CATALOG (Meta)                                         │
│  ├── All products from feed                                     │
│  ├── Product sets (filtered subsets)                            │
│  └── Catalog settings                                           │
│         │                                                       │
│         v                                                       │
│  AD TYPES                                                       │
│  ├── Advantage+ Catalog Ads (formerly DPA)                      │
│  ├── Advantage+ Sales Campaigns                              │
│  └── Collection Ads with catalog                                │
└─────────────────────────────────────────────────────────────────┘
```

## Feed Optimization

### Required Fields

```
REQUIRED FIELDS
===============

Field           │ Description               │ Best Practice
────────────────┼───────────────────────────┼────────────────────
id              │ Unique product ID         │ Consistent with pixel
title           │ Product name              │ Keywords first
description     │ Product description       │ 150-300 words
availability    │ in stock / out of stock   │ Real-time sync
condition       │ new / refurbished / used  │ Accurate
price           │ Price with currency       │ Format: "29.99 USD"
link            │ Product URL               │ Deep link to PDP
image_link      │ Main image URL            │ Min 500x500px
brand           │ Brand name                │ Consistent spelling
```

### Recommended Fields (High Impact)

```
RECOMMENDED FIELDS
==================

Field               │ Impact │ Use
────────────────────┼────────┼────────────────────────────
additional_image_link│ High   │ 3-8 extra images
sale_price          │ High   │ Strikethrough pricing
product_type        │ High   │ Categorization for sets
google_product_category│Med  │ Better matching
custom_label_[0-4]  │ High   │ Segmentation (see below)
color               │ Medium │ Filter option
size                │ Medium │ Filter option
gender              │ Medium │ Targeting option
age_group           │ Medium │ Targeting option
shipping            │ Low    │ Free shipping highlight
```

### Custom Labels Strategy

```
CUSTOM LABEL BEST PRACTICES
===========================

Custom labels = 5 extra fields (0-4) for segmentation

RECOMMENDED SETUP:

custom_label_0: MARGIN
├── "high_margin" (>40% margin)
├── "medium_margin" (20-40%)
└── "low_margin" (<20%)

custom_label_1: BESTSELLER STATUS
├── "bestseller" (top 20% sales)
├── "regular"
└── "slow_mover" (bottom 20%)

custom_label_2: PRICE RANGE
├── "budget" (<$25)
├── "mid_range" ($25-75)
├── "premium" ($75-150)
└── "luxury" (>$150)

custom_label_3: SEASONAL
├── "evergreen"
├── "summer"
├── "winter"
└── "holiday"

custom_label_4: INVENTORY STATUS
├── "plenty" (>50 units)
├── "limited" (10-50)
└── "almost_gone" (<10)
```

## Title & Description Optimization

### Title Best Practices

```
TITLE OPTIMIZATION
==================

FORMAT: [Brand] + [Product Type] + [Key Feature] + [Variant]

EXAMPLES:
Bad: "Nice dress"
Good: "Zara Maxi Dress Floral Print Blue Size M"

Bad: "iPhone case"
Good: "Apple iPhone 15 Pro Silicone Case Midnight Black"

RULES:
├── Max 150 characters (65-70 char optimal)
├── Most important keywords first
├── No ALL CAPS
├── No promotional text ("SALE", "BEST DEAL")
└── Include variant info (size, color)
```

### Description Best Practices

```
DESCRIPTION OPTIMIZATION
========================

STRUCTURE:
1. Opening with key benefit (first 50 characters crucial)
2. Product features (bullets don't work, use clear sentences)
3. Specifications (material, dimensions)
4. Use case / scenario

EXAMPLE:
"Stylish maxi dress with floral print, perfect for summer days.
Made from breathable viscose for optimal wearing comfort. The
dress features a flattering A-line silhouette and adjustable
shoulder straps. Suitable for casual outings and beach vacations."

LENGTH: 150-500 characters optimal
```

## Product Set Strategies

### High-Performance Product Sets

```
PRODUCT SET TYPES
=================

SET 1: BESTSELLERS
├── Filter: custom_label_1 = "bestseller"
├── Use: Prospecting campaigns
└── Why: Proven performers, higher CTR

SET 2: HIGH MARGIN
├── Filter: custom_label_0 = "high_margin"
├── Use: ROAS-focused campaigns
└── Why: More profit per sale

SET 3: SALE ITEMS
├── Filter: sale_price is not empty
├── Use: Retargeting, promotions
└── Why: Urgency, higher conversion

SET 4: NEW ARRIVALS
├── Filter: created_date > [30 days ago]
├── Use: Email subscribers, loyal customers
└── Why: Novelty, FOMO

SET 5: PRICE BASED
├── Filter: price > $50 AND price < $100
├── Use: Segmented audiences
└── Why: Match with target audience purchasing power

SET 6: CATEGORY SPECIFIC
├── Filter: product_type contains "Dresses"
├── Use: Interest-based targeting
└── Why: Relevance for specific interest
```

### Dynamic Product Set Logic

```
ADVANCED FILTERS
================

COMBINATION FILTERS:
├── Bestseller + High Margin + In Stock
│   └── custom_label_1 = "bestseller" AND
│       custom_label_0 = "high_margin" AND
│       availability = "in stock"
│
├── Premium products for High-Value audiences
│   └── custom_label_2 = "premium" OR
│       custom_label_2 = "luxury"
│
└── Urgency set (almost sold out)
    └── custom_label_4 = "almost_gone" AND
        availability = "in stock"
```

## Advantage+ Catalog Ads Campaign Structure

### Retargeting Setup

```
ADVANTAGE+ CATALOG ADS RETARGETING STRUCTURE
=============================================

CAMPAIGN: [Brand]_CatalogAds_Retargeting
├── Objective: Sales
├── Optimization: Purchase
└── Catalog: [Your Catalog]

AD SET 1: Viewed Not Purchased (3d)
├── Audience: ViewContent 3d, exclude Purchase 7d
├── Product Set: All products
├── Budget: 40% of catalog ads budget
└── Expected ROAS: 6-12x

AD SET 2: Add to Cart (7d)
├── Audience: AddToCart 7d, exclude Purchase 7d
├── Product Set: All products
├── Budget: 35% of catalog ads budget
└── Expected ROAS: 8-15x

AD SET 3: Past Purchasers - Cross-sell (30d)
├── Audience: Purchase 30d
├── Product Set: Complementary products
├── Budget: 25% of catalog ads budget
└── Expected ROAS: 4-8x
```

### Prospecting Setup

```
ADVANTAGE+ CATALOG ADS PROSPECTING STRUCTURE
=============================================

CAMPAIGN: [Brand]_CatalogAds_Prospecting
├── Objective: Sales
├── Optimization: Purchase
└── Catalog: [Your Catalog]

AD SET 1: Broad Prospecting
├── Audience: Broad (demographics + geo only)
├── Product Set: Bestsellers only
├── Budget: 50% of prospecting budget
└── Expected ROAS: 2-4x

AD SET 2: Interest-Based
├── Audience: Relevant interests
├── Product Set: Category specific
├── Budget: 30% of prospecting budget
└── Expected ROAS: 2.5-4.5x

AD SET 3: Lookalike Purchasers
├── Audience: LAL 1-3% purchasers
├── Product Set: High margin products
├── Budget: 20% of prospecting budget
└── Expected ROAS: 3-5x
```

## Advantage+ Sales Campaigns

### Advantage+ Sales Campaign Optimization

```
ADVANTAGE+ SALES CAMPAIGN SETUP
================================
(Correct term as of v25.0 API — "Advantage+ Shopping" is deprecated)

WHEN TO USE:
├── E-commerce with 50+ conversions/week
├── Catalog with 20+ products
├── Willing to give up control
└── Focus on volume + efficiency

SETUP:
├── Campaign type: Advantage+ Sales Campaign
├── Catalog: Full catalog (or bestseller set)
├── Budget: Start with 2x normal CPA x 50
├── Existing customer budget cap: 30-50%
└── Countries: Focus markets

CREATIVE INPUT (Andromeda engine — quality matters most):
├── 15+ distinct creative assets recommended
├── Mix: lifestyle images, product images, video (Reels-format 9:16)
├── Strong hooks in first 2 seconds of video
└── Headlines & primary text variations

AUTOMATION LEVERS (2026 — 3 unified controls):
├── Budget automation: Advantage Campaign Budget (no "+" sign)
├── Audience automation: Advantage+ Audience (replaces manual targeting)
└── Placement automation: Advantage+ Placements (includes Threads as of Mar 2026)

OPTIMIZATION TIPS:
├── Give campaign at least 7 days without changes
├── Review "Audience segments" for insights
├── Use existing customer cap wisely (30-50%)
├── Andromeda: creative quality drives results more than audience selection
└── Combine with separate retargeting if needed
```

## Catalog Troubleshooting

### Common Problems

```
TROUBLESHOOTING GUIDE
=====================

PROBLEM: Products not approved
├── Check: Policy violations (alcohol, adult, etc.)
├── Check: Missing required fields
├── Check: Image quality issues
└── Fix: Review Diagnostics tab in Commerce Manager

PROBLEM: Feed sync errors
├── Check: Feed URL accessible?
├── Check: XML/CSV format correct?
├── Check: Encoding issues (UTF-8)?
└── Fix: Validate feed with Facebook Debug Tool

PROBLEM: Low delivery in Catalog Ads
├── Check: Product set too small? (min 20 products)
├── Check: Audience too narrow?
├── Check: All products in stock?
└── Fix: Expand product set, broaden audience

PROBLEM: Wrong products shown
├── Check: Product matching correct?
├── Check: Content IDs in pixel = feed IDs?
├── Check: Pixel events firing correctly?
└── Fix: Verify content_id mapping

PROBLEM: High CPA in Catalog Ads
├── Check: Product set quality
├── Check: Catalog completeness
├── Check: Image quality
└── Fix: Focus on bestsellers, optimize feed
```

### Catalog Health Checklist

```
CATALOG AUDIT CHECKLIST
=======================

□ FEED QUALITY
├── All required fields present?
├── Titles optimized (keywords first)?
├── Descriptions informative (>100 char)?
├── Images high quality (500x500+)?
└── Prices correct and up-to-date?

□ SYNC STATUS
├── Last sync recent (<24 hours)?
├── No feed errors?
├── Update schedule configured?
└── Out of stock items correct?

□ PRODUCT SETS
├── At least 3-5 strategic sets?
├── Bestseller set present?
├── High margin set present?
├── Sets regularly updated?
└── No empty sets?

□ PIXEL MATCHING
├── Content IDs match feed IDs?
├── ViewContent, AddToCart, Purchase events OK?
├── Microdata/Pixel helper validated?
└── Deduplication correct?

□ PERFORMANCE REVIEW
├── CTR per product set monitored?
├── Low performers identified?
├── Best performers scaled?
└── Regular feed optimization?
```

## MCP Tool Integration

### Diagnosing Catalog Ad Performance with Live Data

```
1. List product catalogs and check health:
→ meta_query(account_id="...", entity_type="productcatalogs")
→ meta_query(account_id="...", entity_type="productcatalogs", entity_id="CATALOG_ID")
   Returns: product count, feed count, diagnostics (errors/warnings/approved %)

2. Check catalog campaign ROAS and delivery:
→ meta_get_insights(account_id="...", fields=["spend","purchase_roas","cost_per_action_type","impressions","frequency"], date_preset="last_14d", level="campaign")

3. Ad set level — check audience segments:
→ meta_get_insights(account_id="...", fields=["spend","purchase_roas","cost_per_action_type","reach","frequency"], date_preset="last_14d", level="adset")

4. Creative performance across catalog ads:
→ meta_get_creatives(account_id="...", scope="account")
```

Use results to identify feed issues, which product sets, audience windows, or creative overlays are dragging ROAS down.

## Example Interaction

**User**: "My Advantage+ Catalog Ads are performing poorly. The ROAS is only 1.5x while I expected 3x. What can I do?"

**Claude response**:

"Let's systematically troubleshoot your Catalog Ads performance:

---

**DIAGNOSTIC QUESTIONS:**

1. **Feed Quality:**
   - How many products are in your catalog?
   - Do you have custom labels set up?
   - Are titles optimized?

2. **Campaign Setup:**
   - Retargeting or prospecting catalog ads?
   - Which product sets are you using?
   - What is your audience window?

3. **Creative:**
   - Are you using catalog-only or custom creative overlay?
   - Are product images high-quality?

---

**QUICK CHECKS (do now):**

1. **Catalog diagnostics** (use `meta_query(account_id, "productcatalogs", entity_id="CATALOG_ID")`):
   - Are there warnings/errors?
   - % approved products?

2. **Events Manager → Test Events** (⚠️ UI-only — event testing not in API)
   - Are ViewContent/ATC/Purchase firing correctly?
   - Do content_ids match the feed?

3. **Ad performance data** (use `meta_get_insights` with `level="adset"`):
   - Check frequency and delivery metrics
   - Identify underperforming ad sets

---

**QUICK WINS for ROAS improvement:**

1. **Product Set Focus**
   ```
   Create a "Top Performers" set:
   - Filter: Bestsellers + In Stock + High Margin
   - Test this separately from full catalog
   ```

2. **Audience Narrowing**
   ```
   Retargeting: Shorten window from 30d → 14d
   More recent = higher intent = better ROAS
   ```

3. **Creative Overlay**
   ```
   Add "Free Shipping" or "Sale" badges
   Can increase CTR by 15-30%
   ```

Share your specific setup and I'll give more targeted recommendations!"
