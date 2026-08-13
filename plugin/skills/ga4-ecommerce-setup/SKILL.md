---
name: ga4-ecommerce-setup
description: "This skill should be used when the user asks to \"set up e-commerce tracking in GA4\", \"implement purchase events\", \"configure add_to_cart tracking\", or mentions \"view_item events\", \"product dataLayer\", or \"enhanced e-commerce GA4\". Do NOT use for: promotion and coupon tracking (use ga4-promotion-tracking), revenue analysis and reporting (use ga4-revenue-analysis)."
---
# GA4 E-commerce Setup Guide

Complete guide for implementing e-commerce tracking in Google Analytics 4 with all required events and parameters.

## Quick Decision Tree

```
GA4 E-COMMERCE IMPLEMENTATION FLOW
|
+---> WHAT TYPE OF STORE?
|   +---> Shopify / WooCommerce / Magento
|   |   +---> Use platform-specific integration
|   |       +---> Check plugin/app configuration
|   |
|   +---> Custom store
|       +---> Manual dataLayer implementation
|           +---> Follow e-commerce event specs
|
+---> WHICH EVENTS NEEDED?
|   +---> Basic funnel tracking
|   |   +---> view_item -> add_to_cart -> purchase
|   |
|   +---> Complete funnel tracking
|   |   +---> All events + checkout steps
|   |
|   +---> Advanced tracking
|       +---> + promotions, refunds, wishlists
|
+---> IMPLEMENTATION METHOD?
    +---> Google Tag Manager (Recommended)
    |   +---> DataLayer events -> GTM tags
    |
    +---> gtag.js direct
        +---> JavaScript event calls
```

## E-commerce Event Hierarchy

```
GA4 E-COMMERCE EVENTS OVERVIEW
===============================

DISCOVERY EVENTS:
+---------------------+-----------------------------------------+
| Event               | When to trigger                         |
+---------------------+-----------------------------------------+
| view_item_list      | Product list viewed (category,          |
|                     | search results, recommendations)        |
+---------------------+-----------------------------------------+
| select_item         | Product clicked in list                 |
+---------------------+-----------------------------------------+
| view_item           | Product page viewed                     |
+---------------------+-----------------------------------------+

CART EVENTS:
+---------------------+-----------------------------------------+
| Event               | When to trigger                         |
+---------------------+-----------------------------------------+
| add_to_cart         | Product added to cart                   |
+---------------------+-----------------------------------------+
| remove_from_cart    | Product removed from cart               |
+---------------------+-----------------------------------------+
| view_cart           | Cart page viewed                        |
+---------------------+-----------------------------------------+

CHECKOUT EVENTS:
+---------------------+-----------------------------------------+
| Event               | When to trigger                         |
+---------------------+-----------------------------------------+
| begin_checkout      | Checkout process started                |
+---------------------+-----------------------------------------+
| add_shipping_info   | Shipping details submitted              |
+---------------------+-----------------------------------------+
| add_payment_info    | Payment details submitted               |
+---------------------+-----------------------------------------+
| purchase            | Transaction completed (thank you page)  |
+---------------------+-----------------------------------------+

POST-PURCHASE EVENTS:
+---------------------+-----------------------------------------+
| Event               | When to trigger                         |
+---------------------+-----------------------------------------+
| refund              | (Partial) refund issued                 |
+---------------------+-----------------------------------------+
```

## DataLayer Implementation

### view_item Event

```javascript
VIEW_ITEM EVENT
===============

WHEN: Product page loads

DATALAYER CODE:
-----------------------------------------------------------------
dataLayer.push({ ecommerce: null });  // Clear previous ecommerce
dataLayer.push({
  event: "view_item",
  ecommerce: {
    currency: "EUR",
    value: 29.99,                     // Product price
    items: [{
      item_id: "SKU12345",            // REQUIRED: Unique product ID
      item_name: "Product Name",      // REQUIRED: Product name
      affiliation: "Store Name",      // Optional: Store/affiliate
      coupon: "DISCOUNT10",           // Optional: Applied coupon
      discount: 3.00,                 // Optional: Discount amount
      index: 0,                       // Optional: Position in list
      item_brand: "Brand",            // Recommended: Brand name
      item_category: "Category",      // Recommended: Main category
      item_category2: "Subcategory",  // Optional: Subcategory
      item_category3: "Sub-sub",      // Optional: Deeper category
      item_list_id: "related_prod",   // Optional: List ID
      item_list_name: "Related",      // Optional: List name
      item_variant: "Red / L",        // Optional: Variant (color/size)
      price: 29.99,                   // REQUIRED: Unit price
      quantity: 1                     // REQUIRED: Quantity
    }]
  }
});
-----------------------------------------------------------------

WARNING - IMPORTANT:
+-- Always push ecommerce: null first to clear previous data
+-- item_id and item_name are REQUIRED
+-- price must be numeric (not a string)
+-- currency must be ISO 4217 format (EUR, USD, etc.)
```

### add_to_cart Event

```javascript
ADD_TO_CART EVENT
=================

WHEN: Product is added to cart

DATALAYER CODE:
-----------------------------------------------------------------
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "add_to_cart",
  ecommerce: {
    currency: "EUR",
    value: 29.99,                     // Total value added
    items: [{
      item_id: "SKU12345",
      item_name: "Product Name",
      item_brand: "Brand",
      item_category: "Category",
      item_variant: "Red / L",
      price: 29.99,
      quantity: 1
    }]
  }
});
-----------------------------------------------------------------

TRIGGER LOCATIONS:
+-- "Add to cart" button click
+-- Quick-add buttons in product lists
+-- Product configurator submit
+-- Wishlist to cart action
```

### purchase Event

```javascript
PURCHASE EVENT (CRITICAL!)
==========================

WHEN: Order confirmation page (thank you page)

DATALAYER CODE:
-----------------------------------------------------------------
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "purchase",
  ecommerce: {
    transaction_id: "ORD-2024-12345", // REQUIRED: Unique order ID
    value: 89.97,                      // REQUIRED: Total incl. tax
    tax: 15.63,                        // Recommended: Tax amount
    shipping: 4.99,                    // Recommended: Shipping cost
    currency: "EUR",                   // REQUIRED: Currency
    coupon: "DISCOUNT10",              // Optional: Order-level coupon
    items: [
      {
        item_id: "SKU12345",
        item_name: "Product 1",
        item_brand: "Brand A",
        item_category: "Category",
        item_variant: "Red / L",
        price: 29.99,
        quantity: 2
      },
      {
        item_id: "SKU67890",
        item_name: "Product 2",
        item_brand: "Brand B",
        item_category: "Accessories",
        price: 29.99,
        quantity: 1
      }
    ]
  }
});
-----------------------------------------------------------------

WARNING - CRITICAL POINTS:
+-- transaction_id MUST be unique per order
+-- Duplicate transaction_id's are deduplicated (good!)
+-- value = subtotal + tax + shipping - discount
+-- Fire ONLY on successful orders
+-- Never on cart/checkout pages
+-- Test thoroughly with DebugView
```

### Checkout Events Sequence

```javascript
CHECKOUT EVENTS SEQUENCE
========================

STEP 1: begin_checkout
-----------------------
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "begin_checkout",
  ecommerce: {
    currency: "EUR",
    value: 89.97,
    coupon: "DISCOUNT10",             // If already applied
    items: [/* all cart items */]
  }
});

STEP 2: add_shipping_info
-------------------------
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "add_shipping_info",
  ecommerce: {
    currency: "EUR",
    value: 89.97,
    shipping_tier: "Express",          // Shipping method name
    items: [/* all cart items */]
  }
});

STEP 3: add_payment_info
------------------------
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "add_payment_info",
  ecommerce: {
    currency: "EUR",
    value: 89.97,
    payment_type: "iDEAL",             // Payment method
    items: [/* all cart items */]
  }
});

STEP 4: purchase
----------------
// See purchase event above
```

## GTM Configuration

```
GOOGLE TAG MANAGER E-COMMERCE SETUP
===================================

STEP 1: CREATE DATALAYER VARIABLES
----------------------------------
Variable Type: Data Layer Variable

Variables to create:
+---------------------------+-----------------------------+
| Variable name             | Data Layer Variable Name    |
+---------------------------+-----------------------------+
| DLV - ecommerce           | ecommerce                   |
+---------------------------+-----------------------------+
| DLV - ecommerce.items     | ecommerce.items             |
+---------------------------+-----------------------------+
| DLV - ecommerce.value     | ecommerce.value             |
+---------------------------+-----------------------------+
| DLV - transaction_id      | ecommerce.transaction_id    |
+---------------------------+-----------------------------+
| DLV - ecommerce.currency  | ecommerce.currency          |
+---------------------------+-----------------------------+

STEP 2: CREATE TRIGGERS
------------------------
Trigger Type: Custom Event

Per e-commerce event:
+-- view_item trigger     -> Event name: view_item
+-- add_to_cart trigger   -> Event name: add_to_cart
+-- begin_checkout trigger-> Event name: begin_checkout
+-- purchase trigger      -> Event name: purchase
+-- etc.

STEP 3: GA4 EVENT TAG
---------------------
Tag Type: Google Analytics: GA4 Event

Configuration:
+-- Configuration Tag: [Your GA4 Config tag]
+-- Event Name: {{Event}}
+-- Event Parameters:
|   +-- items: {{DLV - ecommerce.items}}
|   +-- value: {{DLV - ecommerce.value}}
|   +-- currency: {{DLV - ecommerce.currency}}
|   +-- transaction_id: {{DLV - transaction_id}}
+-- Trigger: [All e-commerce triggers]

WARNING: OR use "Send Ecommerce data" checkbox:
+-- Check "Send Ecommerce data"
+-- Data source: Data Layer
+-- GTM handles the rest automatically
```

## Platform-Specific Implementations

```
SHOPIFY IMPLEMENTATION
=====================

OPTION 1: Native GA4 integration
+-- Admin -> Online Store -> Preferences
+-- Enter Google Analytics 4 Measurement ID
+-- Basic tracking automatic
+-- LIMITED: Not all events supported

OPTION 2: Shopify Pixels (Recommended)
+-- Admin -> Settings -> Customer Events
+-- Add custom pixel with GA4 code
+-- Full control over events
+-- Supports all e-commerce events

OPTION 3: Third-party apps
+-- Elevar (premium, very comprehensive)
+-- Analyzify (good for beginners)
+-- Littledata (enterprise focus)

WOOCOMMERCE IMPLEMENTATION
===========================

OPTION 1: GTM4WP Plugin (Recommended)
+-- Install GTM4WP (free)
+-- Configure e-commerce tracking
+-- DataLayer automatically populated
+-- Connect with GTM for GA4 tags

OPTION 2: MonsterInsights
+-- Premium feature for e-commerce
+-- Less flexible than GTM4WP
+-- Easier for beginners

MAGENTO IMPLEMENTATION
======================

+-- Use GTM module (Amasty, MagePlaza)
+-- Configure dataLayer output
+-- Manual mapping to GA4 events
+-- Test thoroughly with staged orders
```

## Common Problems

```
TROUBLESHOOTING E-COMMERCE TRACKING
====================================

PROBLEM: Purchase events not visible
-------------------------------------
Causes:
+-- DataLayer not correctly implemented
+-- Thank you page redirect too fast
+-- Tag firing before dataLayer ready
+-- Consent not granted
+-- transaction_id missing

Solution:
+-- Check dataLayer in browser console
+-- Use GTM Preview mode
+-- Add dataLayer.push before page load
+-- Verify in GA4 DebugView
+-- Check consent mode status

PROBLEM: Revenue is incorrect
-----------------------------
Causes:
+-- Price as string instead of number
+-- Tax counted twice
+-- Currency mismatch
+-- Duplicate transactions
+-- Test orders in production

Solution:
+-- Verify: typeof price === 'number'
+-- Check value calculation
+-- Match currency with GA4 property
+-- Check transaction_id uniqueness
+-- Exclude internal IPs

PROBLEM: Items array empty
---------------------------
Causes:
+-- Async loading issues
+-- DataLayer timing
+-- SPA routing problems
+-- Object reference errors

Solution:
+-- Log dataLayer to console
+-- Wait for DOM ready
+-- Use callback after cart update
+-- Clone objects before push

PROBLEM: Checkout funnel incomplete
------------------------------------
Causes:
+-- Not all checkout events implemented
+-- Event order incorrect
+-- Single Page Checkout complications
+-- Payment redirect loses session

Solution:
+-- Implement ALL checkout events
+-- Verify chronological order
+-- Test complete checkout flow
+-- Cross-domain tracking for payment
```

## E-commerce Audit Checklist

```
E-COMMERCE TRACKING AUDIT
==========================

[ ] DATALAYER STRUCTURE
+-- [ ] ecommerce object correctly nested
+-- [ ] ecommerce: null before each event
+-- [ ] All required fields present
+-- [ ] Correct data types (number, string)
+-- [ ] Consistent item_id across events

[ ] EVENT IMPLEMENTATION
+-- [ ] view_item on all product pages
+-- [ ] add_to_cart on all add actions
+-- [ ] begin_checkout at checkout start
+-- [ ] purchase ONLY on success
+-- [ ] refund for returns (optional)

[ ] DATA QUALITY
+-- [ ] Prices are numeric
+-- [ ] Currency is ISO 4217
+-- [ ] transaction_id is unique
+-- [ ] Quantities are integers
+-- [ ] No PII in custom parameters

[ ] GTM CONFIGURATION
+-- [ ] All variables created
+-- [ ] Triggers per event type
+-- [ ] GA4 tag correctly configured
+-- [ ] Preview mode tested
+-- [ ] Container published

[ ] GA4 VERIFICATION
+-- [ ] Events visible in DebugView
+-- [ ] Parameters coming through correctly
+-- [ ] Revenue reporting correctly
+-- [ ] Monetization reports populating
+-- [ ] Key Events marked
```

## Output: E-commerce Implementation Template

```markdown
# GA4 E-commerce Implementation Report

## Store Information
- **Platform:** [Shopify/WooCommerce/Custom/etc.]
- **GA4 Property:** G-XXXXXXXXXX
- **Implementation method:** [GTM/Direct/Plugin]
- **Date:** [Date]

## Implemented Events

| Event | Status | Trigger Location |
|-------|--------|------------------|
| view_item_list | OK | Category pages, search results |
| select_item | OK | Product clicks in lists |
| view_item | OK | All product pages |
| add_to_cart | OK | Add to cart buttons |
| remove_from_cart | OK | Cart remove actions |
| view_cart | OK | Cart page |
| begin_checkout | OK | Checkout start |
| add_shipping_info | OK | After shipping selection |
| add_payment_info | OK | After payment selection |
| purchase | OK | Thank you page |
| refund | PENDING | [Still to implement] |

## DataLayer Verification

| Field | Present | Format Correct |
|-------|---------|----------------|
| item_id | OK | OK String |
| item_name | OK | OK String |
| price | OK | OK Number |
| quantity | OK | OK Integer |
| currency | OK | OK ISO 4217 |
| transaction_id | OK | OK Unique |

## Test Results

| Test Case | Result | Notes |
|-----------|--------|-------|
| Product view tracking | OK Pass | - |
| Add to cart tracking | OK Pass | - |
| Complete checkout | OK Pass | Test order ID: [X] |
| Revenue accuracy | OK Pass | Matched backend |
| Multiple items order | OK Pass | - |

## GA4 Monetization Reports

- **Revenue visible:** Yes
- **Product performance:** Working
- **Checkout funnel:** All steps visible

## Next Steps
1. [ ] Implement refund tracking
2. [ ] Add promotion tracking
3. [ ] Expand product scoping

## Notes
[Any additional remarks]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, verify ecommerce events are firing and revenue is being captured correctly:

```python
# Confirm purchase events, transaction count, and revenue totals
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["transactions", "purchaseRevenue", "ecommercePurchases"],
    dimensions=["date"],
    start_date="14daysAgo",
    end_date="today"
)
```

Compare `transactions` against backend order count for the same period. A >5% discrepancy indicates missed events (bots filtered, server-side gap, duplicate transactions, or consent drop-off).
