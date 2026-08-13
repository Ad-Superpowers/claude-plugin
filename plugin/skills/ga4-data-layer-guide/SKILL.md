---
name: ga4-data-layer-guide
description: "This skill should be used when the user asks to \"set up a Data Layer\", \"implement GTM Data Layer\", \"push data to dataLayer\", or mentions \"e-commerce Data Layer\", \"Data Layer debugging\", or \"dataLayer structure\". Do NOT use for: GA4 property setup (use ga4-property-setup-guide), event tracking without Data Layer (use ga4-event-tracking-setup), or BigQuery export (use ga4-bigquery-export)."
---
# GA4 Data Layer Guide

Complete guide for implementing a robust Data Layer for Google Analytics 4 via Google Tag Manager.

## Data Layer Basics

```
WHAT IS THE DATA LAYER?
=======================

┌────────────────────────────────────────────────────────────────┐
│  dataLayer = JavaScript array that shares data with GTM        │
│                                                                │
│  FLOW:                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐ │
│  │ Website  │ -> │ dataLayer│ -> │   GTM    │ -> │   GA4    │ │
│  │  Code    │    │  Array   │    │  Tags    │    │ Property │ │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘ │
│                                                                │
│  ADVANTAGES:                                                   │
│  ├── Separation of data and tracking logic                     │
│  ├── Flexibility: modify tracking without code changes         │
│  ├── Reliability: data available when needed                   │
│  ├── Structured data: consistent formats                       │
│  └── Debug-friendly: easy to inspect                           │
└────────────────────────────────────────────────────────────────┘

BASIC SYNTAX:
─────────────
// Initialize dataLayer (before GTM snippet)
window.dataLayer = window.dataLayer || [];

// Push data to dataLayer
dataLayer.push({
  'event': 'event_name',
  'key': 'value'
});
```

## Data Layer Initialization

```
CORRECT DATA LAYER SETUP
=========================

STEP 1: Initialize before GTM
──────────────────────────────

PLACE IN <head>, BEFORE GTM snippet:

```html
<script>
  window.dataLayer = window.dataLayer || [];

  // Optional: initial page data
  dataLayer.push({
    'pageType': 'product',
    'pageCategory': 'electronics',
    'userLoggedIn': true,
    'userId': 'user_12345',
    'userType': 'returning'
  });
</script>

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){...})(window,document,'script','dataLayer','GTM-XXXXX');</script>
<!-- End Google Tag Manager -->
```

STEP 2: GTM Container Code
───────────────────────────
GTM snippet comes AFTER the Data Layer initialization.
This ensures data is available at page load.

ORDER IS CRITICAL:
──────────────────
1. dataLayer = window.dataLayer || [];
2. dataLayer.push({initial page data});
3. GTM <script> tag
4. Rest of the page
5. dataLayer.push() for events (forms, clicks, etc.)
```

## Data Layer Variables in GTM

```
CONFIGURING DATA LAYER VARIABLES
==================================

STEP 1: Create Data Layer Variable
────────────────────────────────────
LOCATION: GTM → Variables → User-Defined Variables → New

CONFIGURATION:
┌────────────────────────────────────────────────────────────────┐
│ Variable Type: Data Layer Variable                             │
│                                                                │
│ Data Layer Variable Name: [exact key name]                     │
│ Example: pageType                                              │
│                                                                │
│ Data Layer Version: Version 2 (recommended)                    │
│                                                                │
│ Set Default Value: [optional fallback]                         │
└────────────────────────────────────────────────────────────────┘

NAMING CONVENTION:
├── Prefix: DLV - (Data Layer Variable)
├── Example: {{DLV - pageType}}
├── Example: {{DLV - user.membershipLevel}}
└── Example: {{DLV - ecommerce.items}}

NESTED VALUES:
──────────────
dataLayer.push({
  'user': {
    'id': '12345',
    'type': 'premium',
    'ltv': 500
  }
});

GTM Variable Name: user.id → returns '12345'
GTM Variable Name: user.type → returns 'premium'

ARRAY VALUES:
─────────────
For e-commerce items (array):
Data Layer Variable Name: ecommerce.items
→ Returns entire array, use in GA4 Event tag
```

## Page Data Layer

```
PAGE-LEVEL DATA LAYER STRUCTURE
================================

STANDARD PAGE DATA:

```javascript
dataLayer.push({
  // Page identification
  'pageType': 'product',           // home, category, product, cart, checkout, thank-you
  'pageCategory': 'electronics',   // content category
  'pageName': 'iPhone 15 Pro',     // friendly page name

  // Content data
  'contentGroup': 'Products',
  'author': 'Admin',               // for blogs/content
  'publishDate': '2024-01-15',

  // User status
  'userLoggedIn': true,
  'userId': 'user_abc123',         // hashed/anonymous ID
  'userType': 'customer',          // visitor, lead, customer

  // Business context
  'storeLocation': 'Amsterdam',
  'language': 'nl-NL',
  'currency': 'EUR'
});
```

PAGE TYPE EXAMPLES:
───────────────────

HOME PAGE:
```javascript
dataLayer.push({
  'pageType': 'home',
  'pageCategory': 'homepage',
  'userLoggedIn': false
});
```

PRODUCT PAGE:
```javascript
dataLayer.push({
  'pageType': 'product',
  'pageCategory': 'electronics',
  'productId': 'SKU-12345',
  'productName': 'iPhone 15 Pro',
  'productPrice': 1199.00,
  'productCategory': 'Smartphones'
});
```

CATEGORY PAGE:
```javascript
dataLayer.push({
  'pageType': 'category',
  'pageCategory': 'electronics',
  'categoryName': 'Smartphones',
  'productCount': 48
});
```
```

## E-commerce Data Layer (GA4 Format)

```
GA4 E-COMMERCE DATA LAYER
===========================

VIEW ITEM (Product Page View)
──────────────────────────────

```javascript
dataLayer.push({ ecommerce: null });  // Clear previous
dataLayer.push({
  'event': 'view_item',
  'ecommerce': {
    'currency': 'EUR',
    'value': 1199.00,
    'items': [{
      'item_id': 'SKU-12345',
      'item_name': 'iPhone 15 Pro',
      'item_brand': 'Apple',
      'item_category': 'Electronics',
      'item_category2': 'Smartphones',
      'item_variant': '256GB Black',
      'price': 1199.00,
      'quantity': 1
    }]
  }
});
```

ADD TO CART
───────────

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  'event': 'add_to_cart',
  'ecommerce': {
    'currency': 'EUR',
    'value': 1199.00,
    'items': [{
      'item_id': 'SKU-12345',
      'item_name': 'iPhone 15 Pro',
      'item_brand': 'Apple',
      'item_category': 'Electronics',
      'item_variant': '256GB Black',
      'price': 1199.00,
      'quantity': 1
    }]
  }
});
```

BEGIN CHECKOUT
──────────────

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  'event': 'begin_checkout',
  'ecommerce': {
    'currency': 'EUR',
    'value': 1398.00,
    'coupon': 'SUMMER10',
    'items': [
      {
        'item_id': 'SKU-12345',
        'item_name': 'iPhone 15 Pro',
        'price': 1199.00,
        'quantity': 1
      },
      {
        'item_id': 'SKU-67890',
        'item_name': 'AirPods Pro',
        'price': 199.00,
        'quantity': 1
      }
    ]
  }
});
```

PURCHASE
────────

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  'event': 'purchase',
  'ecommerce': {
    'transaction_id': 'T-2024-001234',
    'value': 1398.00,
    'tax': 243.00,
    'shipping': 0.00,
    'currency': 'EUR',
    'coupon': 'SUMMER10',
    'items': [
      {
        'item_id': 'SKU-12345',
        'item_name': 'iPhone 15 Pro',
        'item_brand': 'Apple',
        'item_category': 'Electronics',
        'price': 1199.00,
        'quantity': 1
      },
      {
        'item_id': 'SKU-67890',
        'item_name': 'AirPods Pro',
        'item_brand': 'Apple',
        'item_category': 'Electronics',
        'price': 199.00,
        'quantity': 1
      }
    ]
  }
});
```

IMPORTANT:
├── Clear ecommerce object before each push: dataLayer.push({ ecommerce: null });
├── Items is ALWAYS an array, even for a single item
├── Use GA4 naming: item_id (not productId)
└── currency must be included with value
```

## User Data Layer

```
USER DATA IN DATA LAYER
========================

USER PROPERTIES STRUCTURE:

```javascript
// At page load (for logged-in users)
dataLayer.push({
  'event': 'user_data_ready',
  'user': {
    'id': 'usr_abc123',              // Hashed user ID
    'type': 'customer',              // visitor, lead, customer
    'membershipLevel': 'premium',    // free, basic, premium
    'lifetimeValue': 2500,           // LTV in currency
    'firstPurchaseDate': '2023-06-15',
    'totalOrders': 8,
    'lastOrderDate': '2024-01-10',
    'segment': 'high_value'
  }
});
```

PRIVACY-FRIENDLY IMPLEMENTATION:

```javascript
// NEVER put direct PII in Data Layer
// BAD:
dataLayer.push({
  'email': 'jan@example.com',  // Never!
  'phone': '+31612345678'      // Never!
});

// CORRECT: Hashed values or IDs
dataLayer.push({
  'user': {
    'id': 'usr_a1b2c3d4',
    'emailHash': 'sha256_hash_of_email',
    'hasPhone': true
  }
});
```

GTM SETUP FOR USER PROPERTIES:

1. Data Layer Variables:
   ├── DLV - user.id
   ├── DLV - user.type
   ├── DLV - user.membershipLevel
   └── DLV - user.lifetimeValue

2. GA4 Config Tag → User Properties:
   ├── user_id: {{DLV - user.id}}
   ├── customer_type: {{DLV - user.type}}
   ├── membership_level: {{DLV - user.membershipLevel}}
   └── lifetime_value: {{DLV - user.lifetimeValue}}
```

## Form Data Layer

```
FORM DATA VIA DATA LAYER
==========================

FORM SUBMIT PUSH:

```javascript
// On successful form submit
dataLayer.push({
  'event': 'form_submit',
  'form': {
    'id': 'contact-form',
    'name': 'Contact Form',
    'location': 'homepage-hero',
    'type': 'lead',
    'fields': {
      'hasPhone': true,
      'hasCompany': true,
      'interest': 'demo-request'
    }
  }
});
```

MULTI-STEP FORM TRACKING:

```javascript
// Step 1 complete
dataLayer.push({
  'event': 'form_step',
  'form': {
    'name': 'Quote Request',
    'step': 1,
    'stepName': 'Contact Details'
  }
});

// Step 2 complete
dataLayer.push({
  'event': 'form_step',
  'form': {
    'name': 'Quote Request',
    'step': 2,
    'stepName': 'Project Details'
  }
});

// Final submit
dataLayer.push({
  'event': 'form_submit',
  'form': {
    'name': 'Quote Request',
    'step': 3,
    'stepName': 'Submit',
    'complete': true
  }
});
```

GTM SETUP:

Trigger:
├── Type: Custom Event
├── Event name: form_submit

Tag (GA4 Event):
├── Event name: generate_lead
├── Parameters:
│   ├── form_name: {{DLV - form.name}}
│   ├── form_location: {{DLV - form.location}}
│   └── form_type: {{DLV - form.type}}
```

## Custom Event Data Layer

```
CUSTOM EVENTS VIA DATA LAYER
==============================

GENERAL SYNTAX:

```javascript
dataLayer.push({
  'event': 'custom_event_name',    // Triggers GTM
  'eventCategory': 'Videos',        // Optional categorization
  'eventAction': 'play',
  'eventLabel': 'Product Demo',
  // Custom data
  'customKey': 'customValue'
});
```

EXAMPLES:

VIDEO PLAY:
```javascript
dataLayer.push({
  'event': 'video_play',
  'video': {
    'title': 'Product Demo 2024',
    'id': 'vid_123',
    'duration': 180,
    'provider': 'vimeo'
  }
});
```

CTA CLICK:
```javascript
dataLayer.push({
  'event': 'cta_click',
  'cta': {
    'text': 'Get Started',
    'location': 'homepage-hero',
    'destination': '/signup',
    'variant': 'primary'
  }
});
```

CALCULATOR USE:
```javascript
dataLayer.push({
  'event': 'calculator_complete',
  'calculator': {
    'type': 'roi-calculator',
    'result': 25000,
    'inputs': {
      'revenue': 100000,
      'savings': 25
    }
  }
});
```

FILE DOWNLOAD:
```javascript
dataLayer.push({
  'event': 'file_download',
  'file': {
    'name': 'whitepaper-2024.pdf',
    'type': 'pdf',
    'category': 'whitepaper',
    'size': '2.5MB'
  }
});
```
```

## Data Layer Debugging

```
DATA LAYER DEBUG WORKFLOW
==========================

METHOD 1: Browser Console
──────────────────────────
1. Open Developer Tools (F12)
2. Console tab
3. Type: dataLayer
4. Expand array to see all pushes

PRO TIP:
// Real-time monitoring
dataLayer.push = function(obj) {
  console.log('dataLayer push:', obj);
  Array.prototype.push.call(this, obj);
};

METHOD 2: GTM Preview Mode
───────────────────────────
1. GTM → Preview
2. Enter site URL
3. In Tag Assistant:
   ├── Click event in left panel
   ├── Check "Data Layer" tab
   └── Verify all variables present

WHAT TO CHECK:
├── Event name correct
├── All keys present
├── Values correct type (string/number/array)
├── No undefined values
└── Timing: data present before tag fires

METHOD 3: dataLayer Inspector Extension
────────────────────────────────────────
Browser Extension: "dataLayer Inspector+"
├── Real-time Data Layer monitoring
├── Push history
├── Syntax highlighting
└── Filter by event type

METHOD 4: Console Snippet
──────────────────────────

```javascript
// Paste in console for live monitoring
(function() {
  var originalPush = dataLayer.push;
  dataLayer.push = function() {
    console.group('dataLayer.push');
    console.log(arguments[0]);
    console.groupEnd();
    return originalPush.apply(this, arguments);
  };
  console.log('dataLayer monitoring enabled');
})();
```
```

## Data Layer Checklist

```
DATA LAYER IMPLEMENTATION CHECKLIST
=====================================

[] SETUP
├── [] dataLayer initialized before GTM
├── [] GTM container correctly placed
├── [] No JavaScript errors in console
└── [] dataLayer is globally accessible

[] PAGE DATA
├── [] pageType on all pages
├── [] User status (logged in, user ID)
├── [] Content category/type
└── [] Language/currency

[] E-COMMERCE (if applicable)
├── [] view_item on product pages
├── [] add_to_cart events
├── [] begin_checkout event
├── [] purchase event with transaction_id
├── [] ecommerce object cleared before push
└── [] Items array correctly formatted

[] FORMS
├── [] Form submit events
├── [] Form identification (name, location)
├── [] Multi-step tracking (if needed)
└── [] No PII in Data Layer

[] CUSTOM EVENTS
├── [] Important clicks tracked
├── [] Video engagement
├── [] Downloads
└── [] Tool/calculator usage

[] GTM VARIABLES
├── [] All DLV variables created
├── [] Correctly nested (user.id, etc.)
├── [] Default values set
└── [] Naming convention consistent

[] TESTING
├── [] Console: dataLayer contains correct data
├── [] GTM Preview: variables resolved
├── [] DebugView: events coming through
├── [] Cross-browser tested
└── [] Mobile tested
```

## Output: Data Layer Implementation Template

```markdown
# Data Layer Implementation Specification

## Project Information
- **Website:** [URL]
- **Platform:** [Shopify/WooCommerce/Custom/etc.]
- **GTM Container:** GTM-XXXXXXX
- **Implementation date:** [Date]

## GTM Variables Required

| Variable Name | Type | Data Layer Key |
|---------------|------|----------------|
| DLV - pageType | Data Layer Variable | pageType |
| DLV - user.id | Data Layer Variable | user.id |
| DLV - ecommerce.items | Data Layer Variable | ecommerce.items |
| DLV - form.name | Data Layer Variable | form.name |

## Testing Checklist
- [ ] dataLayer initialized before GTM
- [ ] Page data present on all pages
- [ ] E-commerce events firing correctly
- [ ] No PII in Data Layer
- [ ] GTM Preview shows all variables
- [ ] DebugView receives events
- [ ] Cross-browser tested

## Developer Notes
[Implementation-specific notes]

## Changelog
| Date | Change | Author |
|------|--------|--------|
| [Date] | Initial implementation | [Name] |
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, check event parameter fill rates to spot missing or misconfigured Data Layer pushes:

```python
# Check which custom events are firing and with what frequency
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="7daysAgo",
    end_date="today",
    metrics=["eventCount"],
    dimensions=["eventName", "customEvent:form_name"]
)
```

Low event counts or missing dimension values (showing as `(not set)`) indicate Data Layer variables are not populating. Use this to prioritise which pushes to fix first.
