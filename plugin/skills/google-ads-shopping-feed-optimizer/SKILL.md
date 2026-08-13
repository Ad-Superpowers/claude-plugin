---
name: google-ads-shopping-feed-optimizer
description: "This skill should be used when the user asks to \"optimize Shopping feed\", \"fix product disapprovals\", \"improve product titles\", \"set up custom labels\", or mentions \"Merchant Center\", \"feed rules\", \"product data quality\", or \"free listings optimization\". Do NOT use for: Shopping campaign structure advice (use shopping-campaign-structure-advisor), PMax retail optimization (use pmax-retail-optimizer), general PMax setup (use performance-max-optimizer)."
---
# Shopping Feed Optimizer

Complete guide for optimizing Google Merchant Center product feeds for Shopping campaigns and Performance Max.

## Feed Quality Impact

```
FEED QUALITY -> PERFORMANCE IMPACT
====================================

+--------------------------------------------------------------+
|  FEED ELEMENT          |  IMPACT ON PERFORMANCE               |
+--------------------------------------------------------------+
|  Product Title         |  ***** Highest impact on CTR/relevance|
|  Product Image         |  ***** Direct impact on CTR           |
|  Price Accuracy        |  ****  Conversion and trust            |
|  Availability          |  ****  Waste prevention                |
|  GTIN/MPN              |  ***   Matching and comparison         |
|  Description           |  ***   Extended relevance              |
|  Product Type          |  ***   Google categorization           |
|  Custom Labels         |  **    Campaign segmentation           |
|  Additional Attributes |  **    Filtering and rich results      |
+--------------------------------------------------------------+
```

## Product Title Optimization

### Title Structure Framework

```
TITLE FORMULA (priority order)
===================================

FORMULA: [Brand] + [Product Type] + [Key Attributes] + [Model/Variant]

E-COMMERCE EXAMPLES:
---------------------
Fashion:
+-- Bad:    "Blue Dress"
+-- Better: "Nike Air Max 90 Sneakers Men's White Size 10"
+-- Best:   "Nike Air Max 90 - Men's Sneakers - White/Black - Size 10"

Electronics:
+-- Bad:    "Laptop"
+-- Better: "Apple MacBook Pro 14 inch M3 16GB"
+-- Best:   "Apple MacBook Pro 14 inch (2024) - M3 Pro - 16GB RAM - 512GB SSD"

Home & Garden:
+-- Bad:    "Lamp"
+-- Better: "Philips Hue White Ambiance E27 LED Lamp"
+-- Best:   "Philips Hue White Ambiance - E27 LED Smart Lamp - Dimmable - Bluetooth"

MAXIMUM LENGTH: 150 characters (use at least 70+)
```

### Title Optimization Checklist

```
TITLE CHECKLIST
===============

[ ] Brand name present (at the beginning or prominent)
[ ] Product type clearly named
[ ] Key attributes included (color, size, material)
[ ] Model/variant specific
[ ] No keyword stuffing
[ ] No promotional text ("Sale!", "Free shipping")
[ ] No all-caps for full words (NIKE -> Nike)
[ ] Spelling and grammar correct

REQUIRED ATTRIBUTES BY CATEGORY:
---------------------------------
Apparel:
+-- Gender (Men's/Women's/Unisex)
+-- Size or size indication
+-- Color
+-- Material (if relevant)

Electronics:
+-- Brand
+-- Model number
+-- Key specs
+-- Capacity/Size

Furniture:
+-- Furniture type
+-- Material
+-- Dimensions or size
+-- Color/Finish
```

### Title Generation Script

```javascript
/**
 * Shopping Feed Title Optimizer Script
 *
 * Analyzes product titles and generates optimization suggestions.
 *
 * Setup:
 * 1. Update SPREADSHEET_URL
 * 2. Run manually or schedule weekly
 */

var CONFIG = {
  SPREADSHEET_URL: 'YOUR_SPREADSHEET_URL',
  MIN_TITLE_LENGTH: 70,
  MAX_TITLE_LENGTH: 150
};

function main() {
  var products = ShoppingContent.Products.list(
    AdsApp.currentAccount().getCustomerId().replace(/-/g, '')
  );

  var issues = [];

  if (products.resources) {
    for (var i = 0; i < products.resources.length; i++) {
      var product = products.resources[i];
      var titleIssues = analyzeTitleQuality(product);

      if (titleIssues.length > 0) {
        issues.push({
          productId: product.offerId,
          currentTitle: product.title,
          issues: titleIssues,
          suggestedTitle: generateOptimizedTitle(product)
        });
      }
    }
  }

  writeToSpreadsheet(issues);
  Logger.log('Analyzed ' + (products.resources ? products.resources.length : 0) + ' products');
  Logger.log('Found ' + issues.length + ' products with title issues');
}

function analyzeTitleQuality(product) {
  var issues = [];
  var title = product.title || '';

  // Check length
  if (title.length < CONFIG.MIN_TITLE_LENGTH) {
    issues.push('Title too short (' + title.length + ' chars, min: ' + CONFIG.MIN_TITLE_LENGTH + ')');
  }

  // Check for brand
  if (product.brand && title.toLowerCase().indexOf(product.brand.toLowerCase()) === -1) {
    issues.push('Brand missing from title');
  }

  // Check for all caps words
  var words = title.split(' ');
  for (var i = 0; i < words.length; i++) {
    if (words[i].length > 3 && words[i] === words[i].toUpperCase()) {
      issues.push('Avoid all caps: ' + words[i]);
      break;
    }
  }

  // Check for promotional text
  var promoPatterns = ['sale', 'discount', 'free', 'promo', '!', '%'];
  for (var i = 0; i < promoPatterns.length; i++) {
    if (title.toLowerCase().indexOf(promoPatterns[i]) !== -1) {
      issues.push('Promotional text found: ' + promoPatterns[i]);
      break;
    }
  }

  return issues;
}

function generateOptimizedTitle(product) {
  var parts = [];

  // Brand first
  if (product.brand) {
    parts.push(product.brand);
  }

  // Product type
  if (product.productTypes && product.productTypes.length > 0) {
    var lastType = product.productTypes[product.productTypes.length - 1];
    parts.push(lastType.split('>').pop().trim());
  }

  // Color
  if (product.color) {
    parts.push(product.color);
  }

  // Size
  if (product.sizes && product.sizes.length > 0) {
    parts.push('Size ' + product.sizes[0]);
  }

  // Gender for apparel
  if (product.gender) {
    var genderMap = {'male': "Men's", 'female': "Women's", 'unisex': 'Unisex'};
    if (genderMap[product.gender]) {
      parts.push(genderMap[product.gender]);
    }
  }

  return parts.join(' - ');
}

function writeToSpreadsheet(issues) {
  // Implementation for spreadsheet export
  Logger.log('Would write ' + issues.length + ' issues to spreadsheet');
}
```

## Product Description Optimization

```
DESCRIPTION BEST PRACTICES
==========================

STRUCTURE:
+-- Opening sentence: Unique selling point
+-- Key features: 3-5 bullet points
+-- Specifications: Technical details
+-- Use case: What it's suitable for
+-- Avoid: URLs, prices, promotions

EXAMPLE (Electronics):
----------------------
"The Samsung Galaxy S24 Ultra combines cutting-edge AI with
a professional camera. Features a 200MP main camera, S Pen
support, and titanium design. Ideal for power users
who want the best.

Specifications:
- 6.8 inch Dynamic AMOLED 2X display
- Snapdragon 8 Gen 3 processor
- 200MP + 50MP + 12MP + 10MP camera system
- 5000mAh battery with 45W fast charging
- IP68 water and dust resistant"

MAXIMUM LENGTH: 5000 characters (recommended: 500-1500)

WHAT TO AVOID:
+-- Links to your website
+-- Prices or price comparisons
+-- Shipping information
+-- Promotions or sale info
+-- Competitive claims ("best", "cheapest")
+-- Text in ALL CAPS
```

## Custom Labels Strategy

### Custom Labels Overview

```
CUSTOM LABELS USAGE
=====================

You have 5 custom labels (0-4) available for segmentation.

RECOMMENDED STRATEGY:
---------------------

CUSTOM LABEL 0: Margin Category
+-- Values: high_margin, medium_margin, low_margin
+-- Use: Bid strategy per margin tier
+-- Example: Products >40% margin = high_margin

CUSTOM LABEL 1: Performance Tier
+-- Values: bestseller, standard, slow_mover
+-- Use: Budget allocation
+-- Example: Top 20% by sales = bestseller

CUSTOM LABEL 2: Seasonality
+-- Values: summer, winter, evergreen, holiday
+-- Use: Seasonal campaigns
+-- Example: Winter coats = winter

CUSTOM LABEL 3: Product Lifecycle
+-- Values: new, core, clearance, discontinued
+-- Use: Promo campaigns
+-- Example: Older collections = clearance

CUSTOM LABEL 4: Price Range
+-- Values: budget, mid_range, premium, luxury
+-- Use: Audience targeting
+-- Example: >$500 = luxury
```

### Custom Label Feed Rules

```
FEED RULES FOR CUSTOM LABELS
=============================

Location: Merchant Center -> Products -> Feeds -> [Feed] -> Feed Rules

RULE 1: High Margin Products
-----------------------------
If: custom_attribute_0 > 40
Then: Set custom_label_0 to "high_margin"
Else If: custom_attribute_0 > 20
Then: Set custom_label_0 to "medium_margin"
Else: Set custom_label_0 to "low_margin"

RULE 2: Bestsellers
--------------------
If: sale_count_30d > [threshold]
Then: Set custom_label_1 to "bestseller"
Note: Requires sales data in supplemental feed

RULE 3: Price Tiers
--------------------
If: price < 25 USD
Then: Set custom_label_4 to "budget"
Else If: price < 100 USD
Then: Set custom_label_4 to "mid_range"
Else If: price < 500 USD
Then: Set custom_label_4 to "premium"
Else: Set custom_label_4 to "luxury"

RULE 4: New Products
---------------------
If: date_added > [30 days ago]
Then: Set custom_label_3 to "new"
```

## Required vs Optional Attributes

```
FEED ATTRIBUTES OVERVIEW
=========================

REQUIRED (all products):
+-- id: Unique product identifier
+-- title: Product name (max 150 chars)
+-- description: Product description
+-- link: Product page URL
+-- image_link: Main image URL
+-- price: Price with currency (e.g. "49.99 USD")
+-- availability: in_stock / out_of_stock / preorder
+-- condition: new / refurbished / used

REQUIRED (specific categories):
-------------------------------
Apparel/Fashion:
+-- gender: male / female / unisex
+-- age_group: adult / kids / etc.
+-- color: Color name
+-- size: Size designation

Electronics/Variant Products:
+-- gtin: EAN/UPC barcode
+-- mpn: Manufacturer Part Number
+-- brand: Brand name

STRONGLY RECOMMENDED:
+-- additional_image_link: Extra product photos (max 10)
+-- sale_price: Sale price
+-- sale_price_effective_date: Sale period
+-- google_product_category: Google taxonomy ID
+-- product_type: Your category hierarchy
+-- shipping: Shipping costs
+-- shipping_weight: Weight for calculation
+-- custom_label_0-4: Segmentation labels
+-- product_highlight: Key benefits (max 150 chars, max 10)

OPTIONAL BUT VALUABLE:
+-- material: Material
+-- pattern: Pattern
+-- multipack: Number in package
+-- is_bundle: true/false for bundles
+-- energy_efficiency_class: EU energy label
+-- unit_pricing_measure: Price per unit
+-- unit_pricing_base_measure: Base unit
```



## GAQL: Feed Diagnostics via Google Ads API

Use `google_ads_run_gaql` to diagnose Shopping feed performance directly from Google Ads (without Merchant Center UI):

```sql
-- Products with impressions + disapproval status
SELECT segments.product_title, segments.product_item_id,
    segments.product_brand, segments.product_type_l1,
    metrics.impressions, metrics.clicks, metrics.cost_micros,
    metrics.conversions
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
LIMIT 100
```

```sql
-- Find products with zero impressions (feed/approval issue)
SELECT segments.product_title, segments.product_item_id,
    metrics.impressions, metrics.clicks
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
AND metrics.impressions = 0
LIMIT 50
```

```sql
-- Check Merchant Center link
SELECT customer.id, customer_client_link.client_customer,
    customer_client_link.status
FROM customer_client_link
```

## Resolving Disapprovals

### Most Common Disapprovals

```
TOP DISAPPROVALS & FIXES
========================

1. PRICE MISMATCH
-----------------
Cause: Price in feed != price on landing page
Fix:
+-- Increase feed sync frequency (real-time or hourly)
+-- Update microdata/structured data on page
+-- Include sale_price if product is on sale
+-- Check currency (USD vs $)

2. AVAILABILITY MISMATCH
------------------------
Cause: Feed says in_stock, page says sold out
Fix:
+-- Real-time inventory sync
+-- Out of stock products: availability = "out_of_stock"
+-- Preorder: availability = "preorder"
+-- Automatic feed updates on stock changes

3. MISSING IDENTIFIER (GTIN/MPN/BRAND)
--------------------------------------
Cause: Required identifiers missing
Fix:
+-- Add EAN/GTIN to feed
+-- No GTIN? Use: identifier_exists = false
+-- Ensure mpn OR gtin is present
+-- Brand is always required

4. POLICY VIOLATION - PROHIBITED CONTENT
----------------------------------------
Cause: Product falls under restricted category
Check:
+-- Weapons and ammunition
+-- Drugs and drug-related items
+-- Counterfeit products
+-- Dangerous products
+-- Adult content without age verification

5. LANDING PAGE NOT FOUND (404)
-------------------------------
Cause: Product URL not reachable
Fix:
+-- Check redirects (301/302)
+-- Remove discontinued products from feed
+-- Update URLs after site migration
+-- Ensure trailing slash consistency

6. IMAGE QUALITY ISSUES
-----------------------
Cause: Image doesn't meet specs
Fix:
+-- Minimum 100x100 (250x250 for apparel)
+-- Remove text overlays
+-- No placeholders or stock photos
+-- Good lighting and quality
```

### Disapproval Monitor Script

```javascript
/**
 * Merchant Center Disapproval Monitor
 *
 * Monitors product disapprovals and sends daily alerts.
 *
 * Setup:
 * 1. Update EMAIL
 * 2. Schedule daily
 */

var CONFIG = {
  EMAIL: 'you@example.com',
  ALERT_THRESHOLD: 10  // Alert if >10 new disapprovals
};

function main() {
  var merchantId = AdsApp.currentAccount().getCustomerId().replace(/-/g, '');

  try {
    var products = ShoppingContent.Products.list(merchantId);
    var stats = analyzeProducts(products);

    Logger.log('=== Merchant Center Status ===');
    Logger.log('Total products: ' + stats.total);
    Logger.log('Approved: ' + stats.approved);
    Logger.log('Disapproved: ' + stats.disapproved);
    Logger.log('Pending: ' + stats.pending);

    if (stats.disapproved > CONFIG.ALERT_THRESHOLD) {
      sendDisapprovalAlert(stats);
    }

  } catch (e) {
    Logger.log('Error accessing Merchant Center: ' + e.message);
  }
}

function analyzeProducts(products) {
  var stats = {
    total: 0,
    approved: 0,
    disapproved: 0,
    pending: 0,
    issueTypes: {}
  };

  if (products.resources) {
    stats.total = products.resources.length;

    for (var i = 0; i < products.resources.length; i++) {
      var product = products.resources[i];

      // Check product status via issues
      if (product.issues && product.issues.length > 0) {
        var hasDisapproval = false;

        for (var j = 0; j < product.issues.length; j++) {
          var issue = product.issues[j];

          if (issue.servability === 'disapproved') {
            hasDisapproval = true;

            // Track issue types
            var issueType = issue.description || 'Unknown';
            if (!stats.issueTypes[issueType]) {
              stats.issueTypes[issueType] = 0;
            }
            stats.issueTypes[issueType]++;
          }
        }

        if (hasDisapproval) {
          stats.disapproved++;
        } else {
          stats.approved++;
        }
      } else {
        stats.approved++;
      }
    }
  }

  return stats;
}

function sendDisapprovalAlert(stats) {
  var subject = 'Merchant Center Alert: ' + stats.disapproved + ' Disapproved Products';

  var body = 'Merchant Center Disapproval Alert\n';
  body += '==================================\n\n';
  body += 'Total Products: ' + stats.total + '\n';
  body += 'Approved: ' + stats.approved + '\n';
  body += 'Disapproved: ' + stats.disapproved + '\n\n';

  body += 'Top Issues:\n';
  var sortedIssues = Object.keys(stats.issueTypes).sort(function(a, b) {
    return stats.issueTypes[b] - stats.issueTypes[a];
  });

  for (var i = 0; i < Math.min(5, sortedIssues.length); i++) {
    body += '- ' + sortedIssues[i] + ': ' + stats.issueTypes[sortedIssues[i]] + ' products\n';
  }

  body += '\nAction Required: Review disapprovals in Merchant Center\n';
  body += 'https://merchants.google.com/\n';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Free Listings Optimization

```
MAXIMIZING FREE LISTINGS
===========================

FREE LISTINGS = Free product placements on:
+-- Google Search (Shopping tab)
+-- Google Images
+-- YouTube
+-- Google Lens

ENABLING:
Merchant Center -> Growth -> Manage Programs -> Free Product Listings

OPTIMIZATION TIPS:
-------------------
1. Fill in all optional attributes
   +-- Increases visibility in free listings
   +-- More attributes = better matching
   +-- Especially: shipping, availability_date

2. Add Product Ratings
   +-- Integrate review feeds
   +-- Google Customer Reviews
   +-- Third-party review aggregators

3. Shipping information
   +-- Name free shipping
   +-- Delivery times (min_handling_time, max_handling_time)
   +-- Transit times per region

4. Promotions
   +-- Merchant Promotions program
   +-- Discount visible in listing
   +-- Integrate promo codes

5. Product Highlights
   +-- product_highlight attribute
   +-- Max 10 highlights per product
   +-- Key benefits in bullets
```

## Supplemental Feeds

```
SUPPLEMENTAL FEED STRATEGY
===========================

WHAT IS A SUPPLEMENTAL FEED?
+-- Addition to primary feed
+-- Override or add attributes
+-- Useful for bulk updates
+-- No complete product data needed

USE CASES:
----------
1. Custom Labels (margin, performance)
2. Sale Prices (promotions)
3. Seasonal Updates
4. Inventory Exclusions
5. Title/Description Overrides

SETUP:
Merchant Center -> Products -> Feeds -> Supplemental Feed

EXAMPLE SUPPLEMENTAL FEED:
---------------------------
id,custom_label_0,custom_label_1,excluded_destination
SKU001,high_margin,bestseller,
SKU002,low_margin,slow_mover,"Shopping ads"
SKU003,high_margin,standard,
SKU004,,clearance,"Shopping ads,Free listings"

MATCHING RULES:
+-- Match on 'id' (offerId)
+-- Empty cells = no override
+-- Takes effect within minutes after upload
+-- Schedule for automatic updates
```

## Feed Audit Checklist

```markdown
# Shopping Feed Audit Checklist

## Data Quality Score: ___/100

### Product Identifiers
[ ] GTIN/EAN coverage: ___%
[ ] MPN coverage where needed: ___%
[ ] Brand always present: [yes/no]
[ ] identifier_exists correctly used: [yes/no]

### Titles
[ ] Average title length: ___ chars
[ ] Titles contain brand: ___%
[ ] Titles contain key attributes: ___%
[ ] No promotional text: [yes/no]
[ ] No ALL CAPS: [yes/no]

### Images
[ ] All products have image: [yes/no]
[ ] Image quality >800px: ___%
[ ] Additional images used: ___%
[ ] No watermarks/text: [yes/no]

### Pricing & Availability
[ ] Prices in sync with website: [yes/no]
[ ] Sale prices correct: [yes/no]
[ ] Availability real-time: [yes/no]
[ ] Out of stock properly marked: [yes/no]

### Categorization
[ ] Google Product Category set: ___%
[ ] Product Type hierarchy: [yes/no]
[ ] Custom Labels in use: [yes/no]

### Disapproval Status
[ ] Disapproved products: ___
[ ] Top 3 disapproval reasons:
  1. _______________
  2. _______________
  3. _______________

### Recommendations
1. [Highest priority action]
2. [Second priority action]
3. [Third priority action]
```

## Feed Management Best Practices

```
DAILY / ONGOING
===================
[ ] Inventory sync (real-time or hourly)
[ ] Push price updates
[ ] Add new products
[ ] Remove discontinued products

WEEKLY
=========
[ ] Review and fix disapprovals
[ ] Check feed health metrics
[ ] Analyze new product performance
[ ] Monitor competitor pricing

MONTHLY
===========
[ ] Title optimization review
[ ] Update custom labels (performance-based)
[ ] Refresh supplemental feeds
[ ] Full feed audit

SEASONAL
=============
[ ] Tag holiday/seasonal products
[ ] Prepare promotions
[ ] Shift budget allocation to seasonal products
[ ] Mark clearance items
```

## Output: Feed Optimization Report Template

```markdown
# Feed Optimization Report

Date: [DATE]
Merchant ID: [ID]

## Executive Summary

Feed Health Score: [X]/100

### Current Status
- Total Products: [X]
- Approved: [X] ([X]%)
- Disapproved: [X] ([X]%)
- Pending: [X] ([X]%)

### Top Opportunities
1. [Opportunity + estimated impact]
2. [Opportunity + estimated impact]
3. [Opportunity + estimated impact]

## Detailed Findings

### Title Optimization (Score: X/20)
- Average length: [X] chars
- Brand inclusion: [X]%
- Improvements needed: [specifics]

### Image Quality (Score: X/20)
- High-res coverage: [X]%
- Additional images: [X]%
- Issues found: [specifics]

### Data Completeness (Score: X/20)
- GTIN coverage: [X]%
- Optional attributes: [X]%
- Missing critical data: [specifics]

### Price & Inventory (Score: X/20)
- Sync accuracy: [X]%
- Update frequency: [X]
- Issues: [specifics]

### Disapprovals (Score: X/20)
- Active disapprovals: [X]
- Top reasons: [list]
- Resolution plan: [specifics]

## Action Plan

### Week 1 (Critical)
[ ] [Action item]
[ ] [Action item]

### Week 2-3 (High Priority)
[ ] [Action item]
[ ] [Action item]

### Month 1 (Medium Priority)
[ ] [Action item]
[ ] [Action item]

## Expected Impact
- Approved products: +[X]%
- Impression share: +[X]%
- CTR improvement: +[X]%
```
