---
name: ga4-promotion-tracking
description: "This skill should be used when the user asks to \"track internal promotions\", \"measure coupon effectiveness\", \"set up promotion tracking in GA4\", or mentions \"promotion banners\", \"coupon ROI\", or \"A/B testing promotions\". Do NOT use for: e-commerce event setup (use ga4-ecommerce-setup), revenue analysis and reporting (use ga4-revenue-analysis)."
---
# GA4 Promotion Tracking Guide

Complete guide for tracking internal promotions, coupon codes, and sales campaigns in Google Analytics 4.

## DataLayer Implementation

### view_promotion Event

```javascript
VIEW_PROMOTION EVENT
====================

WHEN: Promotion banner/element enters viewport

DATALAYER CODE:
-----------------------------------------------------------------
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "view_promotion",
  ecommerce: {
    items: [{
      promotion_id: "summer_sale_2024",     // REQUIRED
      promotion_name: "Summer Sale 2024",   // REQUIRED
      creative_name: "hero_banner_beach",   // Recommended
      creative_slot: "homepage_hero",       // Recommended
      location_id: "homepage"               // Optional
    }]
  }
});
-----------------------------------------------------------------

VIEWPORT TRACKING IMPLEMENTATION:
---------------------------------
// With Intersection Observer (recommended)
const promotionBanner = document.querySelector('.promo-banner');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      dataLayer.push({ ecommerce: null });
      dataLayer.push({
        event: "view_promotion",
        ecommerce: {
          items: [{
            promotion_id: promotionBanner.dataset.promoId,
            promotion_name: promotionBanner.dataset.promoName,
            creative_name: promotionBanner.dataset.creative,
            creative_slot: promotionBanner.dataset.slot
          }]
        }
      });
      observer.unobserve(entry.target); // Track only once
    }
  });
}, { threshold: 0.5 }); // 50% visible

observer.observe(promotionBanner);

HTML DATA ATTRIBUTES:
---------------------
<div class="promo-banner"
     data-promo-id="summer_sale_2024"
     data-promo-name="Summer Sale 2024"
     data-creative="hero_banner_beach"
     data-slot="homepage_hero">
  <!-- Banner content -->
</div>
```

### select_promotion Event

```javascript
SELECT_PROMOTION EVENT
======================

WHEN: User clicks on promotion element

DATALAYER CODE:
-----------------------------------------------------------------
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "select_promotion",
  ecommerce: {
    items: [{
      promotion_id: "summer_sale_2024",
      promotion_name: "Summer Sale 2024",
      creative_name: "hero_banner_beach",
      creative_slot: "homepage_hero",
      location_id: "homepage"
    }]
  }
});
-----------------------------------------------------------------

CLICK HANDLER IMPLEMENTATION:
-----------------------------
document.querySelectorAll('.promo-banner').forEach(banner => {
  banner.addEventListener('click', function() {
    dataLayer.push({ ecommerce: null });
    dataLayer.push({
      event: "select_promotion",
      ecommerce: {
        items: [{
          promotion_id: this.dataset.promoId,
          promotion_name: this.dataset.promoName,
          creative_name: this.dataset.creative,
          creative_slot: this.dataset.slot
        }]
      }
    });
  });
});
```

## Coupon Custom Dimension Setup

```
REGISTER COUPON CUSTOM DIMENSION
=================================

WHY NEEDED:
+-- coupon parameter is event-scoped
+-- Required as dimension for reporting
+-- Enables grouping and filtering

STEP 1: GA4 ADMIN
-----------------
1. Admin -> Custom definitions -> Create custom dimension
2. Configuration:
   +-- Dimension name: Order Coupon
   +-- Scope: Event
   +-- Event parameter: coupon
   +-- Save

STEP 2: WAIT FOR DATA
---------------------
+-- New dimension visible after ~24 hours
+-- Only events AFTER registration get the dimension
+-- No historical data

ALTERNATIVE: ITEM-SCOPED COUPON
-------------------------------
1. Admin -> Custom definitions -> Create custom dimension
2. Configuration:
   +-- Dimension name: Item Coupon
   +-- Scope: Item
   +-- Event parameter: coupon
   +-- Save

RESULT:
-------
+-- Order Coupon: Coupon at order level
+-- Item Coupon: Coupon at product level
+-- Both usable in reports and explorations
```

## A/B Testing Promotions

```
PROMOTION A/B TEST TRACKING
============================

METHOD 1: CREATIVE VARIANTS
----------------------------
Track variants via creative_name:

// Variant A
dataLayer.push({
  event: "view_promotion",
  ecommerce: {
    items: [{
      promotion_id: "summer_sale_2024",
      promotion_name: "Summer Sale 2024",
      creative_name: "hero_variant_a_red",    // Variant identifier
      creative_slot: "homepage_hero"
    }]
  }
});

// Variant B
dataLayer.push({
  event: "view_promotion",
  ecommerce: {
    items: [{
      promotion_id: "summer_sale_2024",
      promotion_name: "Summer Sale 2024",
      creative_name: "hero_variant_b_blue",   // Variant identifier
      creative_slot: "homepage_hero"
    }]
  }
});

ANALYSIS:
+-- Compare CTR per creative_name
+-- Track conversions per variant
+-- Calculate statistical significance

METHOD 2: USER PROPERTY FOR TEST GROUP
---------------------------------------
// On page load, set test group
gtag('set', 'user_properties', {
  promo_test_group: 'variant_b'
});

ADVANTAGES:
+-- User-level tracking
+-- Cross-session consistency
+-- Easier to segment

METHOD 3: GA4 + EXTERNAL A/B TOOL
----------------------------------
+-- (Google Optimize is deprecated)
+-- Use external A/B testing tool
+-- Send experiment ID to GA4
+-- Analyze in custom exploration
```

## Output: Promotion Analysis Report Template

```markdown
# GA4 Promotion Analysis Report

## Reporting Period
- **From:** [Start date]
- **To:** [End date]
- **Campaign:** [Campaign name]

## Executive Summary

| Metric | Value | vs. Previous Period |
|--------|-------|---------------------|
| Promotion Views | XX,XXX | +XX% |
| Promotion Clicks | X,XXX | +XX% |
| Click-through Rate | X.X% | +X.X% |
| Attributed Revenue | $XX,XXX | +XX% |
| Coupon Redemptions | X,XXX | +XX% |

## Promotion Performance per Slot

| Creative Slot | Views | Clicks | CTR | Revenue |
|---------------|-------|--------|-----|---------|
| homepage_hero | XX,XXX | X,XXX | X.X% | $X,XXX |
| category_banner | XX,XXX | XXX | X.X% | $X,XXX |
| product_upsell | XX,XXX | XXX | X.X% | $X,XXX |
| cart_crosssell | X,XXX | XXX | X.X% | $X,XXX |

## Top Performing Promotions

| Promotion Name | Views | CTR | Conversions | Revenue |
|----------------|-------|-----|-------------|---------|
| [Promo 1] | XX,XXX | X.X% | XXX | $X,XXX |
| [Promo 2] | XX,XXX | X.X% | XXX | $X,XXX |
| [Promo 3] | XX,XXX | X.X% | XXX | $X,XXX |

## Creative Variant Performance (A/B Test)

| Variant | Views | CTR | Conv. Rate | Stat. Sig. |
|---------|-------|-----|------------|------------|
| Variant A (Control) | XX,XXX | X.X% | X.X% | - |
| Variant B | XX,XXX | X.X% | X.X% | XX% |
| **Winner:** | Variant [X] | +XX% CTR | +XX% Conv | YES |

## Coupon Code Performance

| Coupon Code | Redemptions | Revenue | Avg. Discount | AOV |
|-------------|-------------|---------|---------------|-----|
| SUMMER20 | XXX | $X,XXX | $XX | $XX |
| NEW10 | XXX | $X,XXX | $XX | $XX |
| VIP30 | XX | $X,XXX | $XX | $XX |

### Coupon Impact Analysis

| Metric | With Coupon | Without Coupon | Difference |
|--------|------------|----------------|------------|
| AOV | $XX | $XX | -XX% |
| Items/Order | X.X | X.X | +XX% |
| Conv. Rate | X.X% | X.X% | +XX% |

## Promotion Funnel

| Step | Users | Drop-off |
|------|-------|----------|
| Promo View | XX,XXX | - |
| Promo Click | X,XXX | XX% |
| Product View | X,XXX | XX% |
| Add to Cart | XXX | XX% |
| Purchase | XXX | XX% |

**Promotion -> Purchase Rate:** X.X%

## Recommendations

### Optimizations
1. **[Slot/Promo]:** [Specific recommendation]
2. **[Slot/Promo]:** [Specific recommendation]

### To Discontinue
1. **[Underperforming promo]:** CTR <X%, consider replacement

### To Test
1. **[Test idea]:** Expected impact
2. **[Test idea]:** Expected impact

## Next Steps
1. [ ] [Action item]
2. [ ] [Action item]
3. [ ] [Action item]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, pull promotion performance to ground recommendations in actual click and conversion rates:

```python
# Get view_promotion and select_promotion event counts by promotion name
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["eventCount"],
    dimensions=["eventName", "customEvent:promotion_name"],
    start_date="30daysAgo",
    end_date="today"
)
```

Compare `view_promotion` vs `select_promotion` counts per promotion slot to calculate CTR per banner. Low CTR (<1%) = poor placement or weak creative; high view count with low revenue = promotion is seen but not compelling.
