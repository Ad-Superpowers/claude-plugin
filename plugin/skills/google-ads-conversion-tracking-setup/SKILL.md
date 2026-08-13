---
name: google-ads-conversion-tracking-setup
description: "This skill should be used when the user asks to \"set up conversion tracking\", \"implement Google Tag\", \"configure Enhanced Conversions\", \"import offline conversions\", or mentions \"gtag setup\", \"conversion value tracking\", or \"primary vs secondary conversions\". Do NOT use for: debugging existing tracking issues (use conversion-tracking-debugger), Meta pixel setup (use meta tools), GA4 event setup (use ga4 tools)."
---
# Conversion Tracking Setup

Complete guide for correctly setting up and optimizing Google Ads conversion tracking, including Enhanced Conversions and offline conversion import.



See [detailed-reference.md](references/detailed-reference.md) for details.



## Conversion Actions Configuration

### Conversion Action Types

```
CONVERSION ACTION TYPES
=======================

NOTE: New in v23.1 — YOUTUBE_FOLLOW_ON_VIEWS conversion category
+-- Tracks YouTube views that lead to subsequent organic views
+-- Category: YOUTUBE_FOLLOW_ON_VIEWS
+-- Use for: YouTube campaign brand awareness attribution
+-- Visible in "All Conversions" column

PURCHASE (E-commerce)
+-- Category: Purchase
+-- Value: Dynamic (transaction value)
+-- Count: Every conversion
+-- Window: 30-90 days
+-- Include in Conversions: YES

LEAD (Lead Gen)
+-- Category: Submit lead form
+-- Value: Static or dynamic lead value
+-- Count: One per click
+-- Window: 30-90 days
+-- Include in Conversions: YES (primary)

SIGN UP (SaaS/Registration)
+-- Category: Sign-up
+-- Value: Static (estimated value)
+-- Count: One per click
+-- Window: 30-60 days
+-- Include in Conversions: YES/NO (based on funnel)

PAGE VIEW (Micro-conversions)
+-- Category: Page view
+-- Value: Static (small)
+-- Count: One per click
+-- Window: 7-30 days
+-- Include in Conversions: NO (observation only)

PHONE CALL
+-- Category: Phone call
+-- Value: Per call or static
+-- Count: One/Every (based on use case)
+-- Window: 30 days
+-- Include in Conversions: YES
```

### Primary vs Secondary Conversions

```
PRIMARY VS SECONDARY CONVERSIONS
================================

PRIMARY CONVERSIONS:
+-- "Include in Conversions: YES"
+-- Used for Smart Bidding optimization
+-- Counted in "Conversions" column
+-- Choose: Your main goal (purchase, lead, etc.)

SECONDARY CONVERSIONS:
+-- "Include in Conversions: NO"
+-- NOT used for bidding
+-- Visible in "All Conversions" column
+-- Choose: Micro-conversions, observation metrics

BEST PRACTICE:
--------------
E-commerce:
+-- Primary: Purchase
+-- Secondary: Add to Cart, Begin Checkout, View Product

Lead Gen:
+-- Primary: Qualified Lead (or SQL)
+-- Secondary: Form Submit, Click-to-Call, PDF Download

SaaS:
+-- Primary: Trial Start or Signup
+-- Secondary: Feature Engagement, Pricing Page View
```

### Conversion Settings

```
CONVERSION SETTINGS DETAIL
==========================

COUNT:
+-- "Every": Each conversion counts (e-commerce: every purchase)
+-- "One": One conversion per click (leads: one lead per click)
+-- Recommendation: Purchases = Every, Leads = One

CONVERSION WINDOW:
+-- Click-through: 30-90 days (default 30)
+-- View-through: 1-30 days (default 1)
+-- Engaged-view: 3-30 days (default 3)
+-- Recommendation: Adjust based on sales cycle

ATTRIBUTION MODEL:
+-- Data-driven (recommended, default since 2024)
+-- Last click
+-- First click
+-- Linear / Time decay / Position-based (deprecated)
+-- Recommendation: Use Data-driven (DDA)
```

## Google Ads Tag Setup

### Basic Tag Implementation

```html
<!-- Google Tag (gtag.js) - BASE CODE -->
<!-- Place in <head> of every page -->

<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  // Google Ads Tag
  gtag('config', 'AW-XXXXXXXXX');
</script>
```

### Conversion Event Implementation

```html
<!-- PURCHASE CONVERSION (E-commerce) -->
<!-- Place on thank-you page / order confirmation -->

<script>
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
    'value': 150.00,                    // Transaction value
    'currency': 'EUR',                  // Currency
    'transaction_id': 'ORDER-12345'     // Unique order ID (deduplication)
  });
</script>

<!-- LEAD CONVERSION -->
<!-- Place on thank-you page after form submit -->

<script>
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/ZZZZZZZZZZZZ',
    'value': 50.00,                     // Estimated lead value
    'currency': 'EUR'
  });
</script>

<!-- PHONE CALL CONVERSION -->
<!-- Via Google forwarding number or manual -->

<script>
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/CALLCONVID',
    'value': 25.00,
    'currency': 'EUR'
  });
</script>
```

### Dynamic Value Tracking

```javascript
// DYNAMIC VALUE TRACKING (E-commerce)
// Get transaction value from your e-commerce platform

// Example for standard e-commerce
<script>
  // Ensure these variables are available on confirmation page
  var orderValue = {{order_total}};      // Populate from platform
  var orderId = '{{order_id}}';          // Unique order ID
  var orderCurrency = 'EUR';

  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
    'value': orderValue,
    'currency': orderCurrency,
    'transaction_id': orderId
  });
</script>

// DYNAMIC VALUE WITH ITEMS (Enhanced E-commerce)
<script>
  gtag('event', 'purchase', {
    'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
    'value': 150.00,
    'currency': 'EUR',
    'transaction_id': 'ORDER-12345',
    'items': [
      {
        'id': 'SKU001',
        'name': 'Product Name',
        'quantity': 2,
        'price': 75.00
      }
    ]
  });
</script>
```

## Enhanced Conversions

### What Are Enhanced Conversions?

```
ENHANCED CONVERSIONS EXPLAINED
===============================

WHAT:
+-- Send first-party data (email, phone, name, address)
+-- Data is hashed (SHA256) for privacy
+-- Google matches with logged-in users
+-- Improves conversion attribution, especially after iOS 14.5

BENEFITS:
+-- +5-15% more measured conversions
+-- Better cross-device tracking
+-- Resilient against cookie blocking
+-- Improved Smart Bidding optimization
+-- Required for optimal performance

TYPES:
+-- Enhanced Conversions for Web: Website purchases/leads
+-- Enhanced Conversions for Leads: Offline lead tracking
+-- Customer Match: Audience building

NEW IN v20+: user_ip_address field
+-- The user's IP address can now be sent as an additional match signal
+-- Improves match rates for server-side conversions
+-- Field: user_ip_address (plain text, not hashed)
```

### Enhanced Conversions for Web (GTM)

```
GTM SETUP: ENHANCED CONVERSIONS FOR WEB
========================================

STEP 1: Enable in Google Ads
----------------------------
1. Goals -> Conversions -> Settings
2. Enhanced conversions: Turn on
3. Choose: Google Tag Manager

STEP 2: GTM Configuration
--------------------------
1. Modify Google Ads Conversion Tracking Tag
2. "Include user-provided data from your website": check
3. Choose data source:
   - New Variable: User-Provided Data
   - Or: Data Layer

STEP 3: User Data Variable Setup (GTM)
---------------------------------------
Variable Type: User-Provided Data
Data Source: Manual Configuration or Data Layer

FIELDS (minimum email):
+-- Email: {{user_email}}
+-- Phone: {{user_phone}}
+-- First Name: {{user_firstname}}
+-- Last Name: {{user_lastname}}
+-- Street: {{user_street}}
+-- City: {{user_city}}
+-- Postal Code: {{user_zip}}
+-- Country: {{user_country}}
```

### Enhanced Conversions Code (Direct)

```javascript
// ENHANCED CONVERSIONS - DIRECT IMPLEMENTATION
// Send user data with conversion event

<script>
  // Method 1: Via gtag set command (recommended)
  gtag('set', 'user_data', {
    'email': 'customer@example.com',         // Plain text or SHA256
    'phone_number': '+31612345678',       // E.164 format
    'address': {
      'first_name': 'John',
      'last_name': 'Smith',
      'street': 'Main Street 123',
      'city': 'Amsterdam',
      'postal_code': '1012AB',
      'country': 'NL'
    }
    // user_ip_address: available for server-side Enhanced Conversions (v20+)
    // Improves match rates — send plain text IP, not hashed
  });

  // Then conversion event
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
    'value': 150.00,
    'currency': 'EUR',
    'transaction_id': 'ORDER-12345'
  });
</script>

// Method 2: SHA256 hashing (privacy-first)
<script>
  async function hashData(data) {
    const encoder = new TextEncoder();
    const dataBuffer = encoder.encode(data.toLowerCase().trim());
    const hashBuffer = await crypto.subtle.digest('SHA-256', dataBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  async function sendConversion() {
    const hashedEmail = await hashData('customer@example.com');

    gtag('set', 'user_data', {
      'sha256_email_address': hashedEmail
    });

    gtag('event', 'conversion', {
      'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
      'value': 150.00,
      'currency': 'EUR',
      'transaction_id': 'ORDER-12345'
    });
  }

  sendConversion();
</script>
```

## Enhanced Conversions for Leads

### Lead Conversion Flow

```
ENHANCED CONVERSIONS FOR LEADS
==============================

PURPOSE:
+-- Match offline sales data with ads clicks
+-- Optimize for real sales, not form fills
+-- Import lead -> opportunity -> closed won data
+-- Smart Bidding learns on high-quality leads

FLOW:
-----
1. User clicks on ad
2. User fills in form (email captured)
3. Form submit = "conversion" event WITH email
4. Lead goes to CRM
5. Lead gets qualified/closed
6. Import qualified lead back to Google Ads
7. Smart Bidding learns what good leads look like
```

### Setup Lead Enhanced Conversions

```javascript
// LEAD FORM SUBMISSION - ENHANCED CONVERSIONS
// Send on form submission

<script>
  // On form submit, collect user data
  document.getElementById('leadForm').addEventListener('submit', function(e) {
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;

    // Set user data
    gtag('set', 'user_data', {
      'email': email,
      'phone_number': phone
    });

    // Fire conversion
    gtag('event', 'conversion', {
      'send_to': 'AW-XXXXXXXXX/LEADCONVID',
      'value': 50.00,
      'currency': 'EUR'
    });
  });
</script>
```

## Offline Conversion Import

### When to Use Offline Conversions

```
OFFLINE CONVERSION USE CASES
============================

1. LEAD GEN (B2B)
   +-- Online: Form submit
   +-- Offline: Lead -> Opportunity -> Closed Won
   +-- Import: Qualified leads and deals

2. E-COMMERCE (High-value)
   +-- Online: Quote request
   +-- Offline: Sales call -> Purchase
   +-- Import: Completed purchases

3. HYBRID BUSINESSES
   +-- Online: Store locator, book appointment
   +-- Offline: In-store purchase
   +-- Import: In-store transactions

4. CALL TRACKING
   +-- Online: Click-to-call
   +-- Offline: Call qualified/resulted in sale
   +-- Import: Qualified calls
```

### Offline Conversion Setup

```
OFFLINE CONVERSION SETUP
========================

METHOD 1: GCLID-based (Traditional)
------------------------------------
1. Capture GCLID on click
   - URL parameter: ?gclid=XXXXX
   - Store in CRM with lead record

2. Create Offline Conversion Action
   - Google Ads -> Goals -> Conversions -> + New
   - Type: Import -> CRM, files, or other sources
   - Name: "Qualified Lead" or "Closed Won"

3. Import conversions
   - Via Upload (CSV/Google Sheets)
   - Via API (automated)
   - Via Partner integration (Salesforce, HubSpot, etc.)

UPLOAD FORMAT:
Parameters:
+-- Google Click ID (GCLID)
+-- Conversion Name
+-- Conversion Time
+-- Conversion Value
+-- Conversion Currency

METHOD 2: Enhanced Conversions for Leads
-----------------------------------------
1. Capture user data on form submit (email, phone)
2. Send Enhanced Conversion event
3. Import offline conversions with same user data
4. Google matches based on hashed data

ADVANTAGE: No GCLID capturing needed
```

### Offline Conversion Upload Template

```csv
# CSV FORMAT FOR OFFLINE CONVERSIONS (GCLID)
Google Click ID,Conversion Name,Conversion Time,Conversion Value,Conversion Currency
EAIaIQobChMI...,Qualified Lead,2025-01-28 14:30:00,50,EUR
EAIaIQobChMI...,Closed Won,2025-01-28 15:45:00,5000,EUR

# CSV FORMAT FOR ENHANCED CONVERSIONS FOR LEADS
Email,Conversion Name,Conversion Time,Conversion Value,Conversion Currency
customer@example.com,Qualified Lead,2025-01-28 14:30:00,50,EUR
```



See [api-patterns.md](references/api-patterns.md) for details.



## Consent Mode v2

### Consent Mode Implementation

```
CONSENT MODE V2 (Required for EU)
===================================

WHAT:
+-- Respects user consent preferences
+-- Adjusts tag behavior based on consent
+-- Collects aggregated data without consent
+-- Uses modeling to fill gaps
+-- REQUIRED for advertising in EU since March 2024

CONSENT TYPES:
+-- ad_storage: Advertising cookies
+-- analytics_storage: Analytics cookies
+-- ad_user_data: Send user data for ads (NEW)
+-- ad_personalization: Personalized ads
+-- functionality_storage: Functional cookies
```

### Consent Mode Code

```html
<!-- CONSENT MODE DEFAULT STATE -->
<!-- Place BEFORE loading gtag.js -->

<script>
  // Default consent state (denied)
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}

  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied',
    'wait_for_update': 500  // Wait for CMP
  });

  // Enable URL passthrough for cross-domain
  gtag('set', 'url_passthrough', true);

  // Enable ads data redaction when denied
  gtag('set', 'ads_data_redaction', true);
</script>

<!-- After user consent (via CMP) -->
<script>
  // Update consent state when user accepts
  function updateConsent(adConsent, analyticsConsent) {
    gtag('consent', 'update', {
      'ad_storage': adConsent ? 'granted' : 'denied',
      'ad_user_data': adConsent ? 'granted' : 'denied',
      'ad_personalization': adConsent ? 'granted' : 'denied',
      'analytics_storage': analyticsConsent ? 'granted' : 'denied'
    });
  }

  // Example: User clicks "Accept All"
  document.getElementById('acceptAll').addEventListener('click', function() {
    updateConsent(true, true);
  });
</script>
```

## MCP Tool: Audit Conversion Actions

```
Before setting up or modifying conversion tracking, pull the current
conversion action inventory:

google_ads_run_gaql(query="
  SELECT
    conversion_action.name,
    conversion_action.status,
    conversion_action.category,
    conversion_action.type,
    conversion_action.counting_type,
    conversion_action.include_in_conversions_metric,
    conversion_action.value_settings.default_value,
    conversion_action.value_settings.always_use_default_value,
    conversion_action.click_through_lookback_window_days
  FROM conversion_action
  ORDER BY conversion_action.name ASC
")

This shows: all conversion actions, their include/exclude status,
counting type (ONE_PER_CLICK vs MANY_PER_CLICK), and lookback windows.
Use to verify setup before go-live.
```

## Tracking Verification

### Conversion Tracking Test Checklist

```
TRACKING VERIFICATION CHECKLIST
================================

[ ] BASIC SETUP
+-- Google Tag loaded on all pages?
+-- Tag ID correct (AW-XXXXXXXXX)?
+-- No JavaScript errors in console?
+-- Test in Tag Assistant (legacy) or Preview mode

[ ] CONVERSION EVENTS
+-- Event fires on correct page/action?
+-- Correct conversion ID/label?
+-- Value correctly passed?
+-- Transaction ID unique per conversion?
+-- Currency correct (EUR, USD)?

[ ] ENHANCED CONVERSIONS
+-- User data being sent?
+-- Email format correct?
+-- Phone in E.164 format (+31...)?
+-- Data hashed or plain text (both OK)?
+-- Status: "Recording" in Google Ads

[ ] REAL-TIME CHECK
+-- Make test conversion
+-- Verify via GAQL: SELECT conversion_action.name, conversion_action.status,
    metrics.conversions FROM conversion_action WHERE segments.date DURING LAST_7_DAYS
+-- Verify value and details
+-- Latency: Max 3-6 hours for visibility

[ ] DATA QUALITY
+-- No duplicate conversions
+-- Values are realistic
+-- Conversion rate is logical
+-- Compare with GA4/backend data
```

### Debugging Script

```javascript
/**
 * Conversion Tracking Debug Helper
 *
 * Add to console to debug tracking
 */

(function() {
  // Check if gtag exists
  if (typeof gtag === 'undefined') {
    console.error('gtag not found! Google Tag not loaded.');
    return;
  }
  console.log('gtag found');

  // Check dataLayer
  if (window.dataLayer) {
    console.log('dataLayer exists with', window.dataLayer.length, 'items');

    // Find conversion events
    var conversions = window.dataLayer.filter(function(item) {
      return item[0] === 'event' && item[1] === 'conversion';
    });

    if (conversions.length > 0) {
      console.log('Found', conversions.length, 'conversion event(s)');
      conversions.forEach(function(conv, i) {
        console.log('  Conversion', i + 1, ':', conv);
      });
    } else {
      console.warn('No conversion events found in dataLayer');
    }

    // Find user_data
    var userData = window.dataLayer.filter(function(item) {
      return item[0] === 'set' && item[1] === 'user_data';
    });

    if (userData.length > 0) {
      console.log('Enhanced Conversions user_data found');
    } else {
      console.warn('No user_data found - Enhanced Conversions may not be active');
    }

    // Find consent events
    var consent = window.dataLayer.filter(function(item) {
      return item[0] === 'consent';
    });
    console.log('Consent events:', consent.length);

  } else {
    console.error('dataLayer not found!');
  }

  // Check for common issues
  var scripts = document.querySelectorAll('script[src*="googletagmanager.com/gtag"]');
  if (scripts.length === 0) {
    console.error('Google Tag script not found in DOM');
  } else if (scripts.length > 1) {
    console.warn('Multiple Google Tag scripts found - may cause issues');
  } else {
    console.log('Google Tag script found');
  }

})();
```

## Conversion Tracking Audit

```markdown
# Conversion Tracking Audit Report

## Account Info
- Account ID: [AW-XXXXXXXXX]
- Date: [DATE]
- Auditor: [NAME]

## Conversion Actions Summary

| Action Name | Type | Primary | Value | Count | Status |
|-------------|------|---------|-------|-------|--------|
| Purchase | Sale | Yes | Dynamic | Every | OK |
| Lead Form | Lead | Yes | $50 | One | OK |
| Add to Cart | Engagement | No | - | Every | OK |

## Tracking Implementation

### Tag Status
- [ ] Google Tag installed: [Yes/No]
- [ ] Tag on all pages: [Yes/No]
- [ ] No console errors: [Yes/No]
- [ ] Consent Mode active: [Yes/No]

### Enhanced Conversions
- [ ] Enabled in Google Ads: [Yes/No]
- [ ] User data sent: [Yes/No]
- [ ] Match rate: [X%]
- [ ] Data fields: [email, phone, etc.]

### Data Quality
- [ ] Conversion rate logical: [Yes/No]
- [ ] Values accurate: [Yes/No]
- [ ] No duplicates: [Yes/No]
- [ ] GA4 comparison: [Match/Discrepancy X%]

## Issues Found

1. **[Issue]**
   - Impact: [High/Medium/Low]
   - Fix: [Description]

2. **[Issue]**
   - Impact: [High/Medium/Low]
   - Fix: [Description]

## Recommendations

1. [Recommendation with priority]
2. [Recommendation with priority]
3. [Recommendation with priority]

## Action Plan

### Week 1
- [ ] [Action item]
- [ ] [Action item]

### Week 2-4
- [ ] [Action item]
- [ ] [Action item]
```
