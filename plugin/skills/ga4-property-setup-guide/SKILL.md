---
name: ga4-property-setup-guide
description: "This skill should be used when the user asks to \"set up GA4\", \"create a GA4 property\", \"configure data streams\", or mentions \"Enhanced Measurement\", \"GA4 installation\", or \"link Google Ads to GA4\". Do NOT use for: event tracking (use ga4-event-tracking-setup), key events/conversions (use ga4-key-events-config), or audience building (use ga4-audience-builder)."
---
# GA4 Property Setup Guide

Complete guide for correctly setting up and configuring a Google Analytics 4 property for advertisers and agencies.

## Quick Decision Tree

```
GA4 PROPERTY SETUP FLOW
│
├─► NEED A NEW PROPERTY?
│   ├─► YES, no GA4 property yet
│   │   └─► Step 1: Create property in Admin
│   │       └─► Step 2: Add Data Stream
│   │           └─► Step 3: Implement tag
│   │
│   └─► NO, optimizing existing property
│       └─► Go to "Property Audit Checklist"
│
├─► WHICH TYPE OF DATA STREAM?
│   ├─► Website only
│   │   └─► Web Data Stream + GTM or gtag.js
│   │
│   ├─► App only (iOS/Android)
│   │   └─► Firebase SDK integration
│   │
│   └─► Website + App
│       └─► Multiple streams, 1 property
│       └─► Cross-platform user tracking
│
└─► ADVERTISING USE CASE?
    ├─► Google Ads optimization
    │   └─► Link Google Ads account
    │   └─► Enable Google Signals
    │
    └─► Multi-platform advertising
        └─► Correct UTM setup
        └─► Cross-domain tracking if needed
```

## Property Setup Steps

### Step 1: Create Property

```
CREATING A GA4 PROPERTY
=========================

LOCATION: admin.google.com → Admin → Create Property

REQUIRED INFORMATION:
┌─────────────────────┬────────────────────────────────────────┐
│ Field               │ Recommendation                         │
├─────────────────────┼────────────────────────────────────────┤
│ Property name       │ [Brand] - [Environment]                │
│                     │ Example: "Acme Corp - Production"      │
├─────────────────────┼────────────────────────────────────────┤
│ Reporting timezone  │ Choose local timezone of business      │
│                     │ (important for reports!)               │
├─────────────────────┼────────────────────────────────────────┤
│ Currency            │ Choose business currency               │
│                     │ (important for revenue tracking!)      │
├─────────────────────┼────────────────────────────────────────┤
│ Industry category   │ Select most fitting category           │
│                     │ (used for benchmarking)                │
├─────────────────────┼────────────────────────────────────────┤
│ Business size       │ Number of employees (for benchmarks)   │
└─────────────────────┴────────────────────────────────────────┘

IMPORTANT:
├── Timezone and currency CANNOT be easily changed later
├── ALWAYS choose production timezone, not UTC
└── One property per brand/business (not per domain)
```

### Step 2: Configure Data Stream

```
WEB DATA STREAM SETUP
=======================

LOCATION: Admin → Data Streams → Add Stream → Web

CONFIGURATION:
┌─────────────────────┬────────────────────────────────────────┐
│ Field               │ Recommendation                         │
├─────────────────────┼────────────────────────────────────────┤
│ Website URL         │ Primary domain (without www)           │
│                     │ Example: example.com                   │
├─────────────────────┼────────────────────────────────────────┤
│ Stream name         │ "Web - [domain]"                       │
│                     │ Example: "Web - example.com"           │
├─────────────────────┼────────────────────────────────────────┤
│ Enhanced            │ ON (always enable!)                    │
│ Measurement         │ Fine-tune specific events              │
└─────────────────────┴────────────────────────────────────────┘

MEASUREMENT ID FORMAT:
├── G-XXXXXXXXXX (Web streams)
├── Use this ID in GTM or gtag.js
└── Keep this ID safe
```

### Step 3: Configure Enhanced Measurement

```
ENHANCED MEASUREMENT EVENTS
=============================

LOCATION: Data Stream → Enhanced measurement → Settings icon

┌───────────────────────┬────────┬────────────────────────────────┐
│ Event                 │ Status │ Notes                          │
├───────────────────────┼────────┼────────────────────────────────┤
│ Page views            │ ✅ ON  │ Always on, basic tracking      │
├───────────────────────┼────────┼────────────────────────────────┤
│ Scrolls               │ ✅ ON  │ 90% scroll depth trigger       │
├───────────────────────┼────────┼────────────────────────────────┤
│ Outbound clicks       │ ✅ ON  │ Clicks to external domains     │
├───────────────────────┼────────┼────────────────────────────────┤
│ Site search           │ ✅ ON  │ Configure search parameter     │
│                       │        │ (usually: q, s, search, query) │
├───────────────────────┼────────┼────────────────────────────────┤
│ Video engagement      │ ✅ ON  │ YouTube embeds automatically   │
├───────────────────────┼────────┼────────────────────────────────┤
│ File downloads        │ ✅ ON  │ PDF, docx, xlsx, etc.          │
├───────────────────────┼────────┼────────────────────────────────┤
│ Form interactions     │ ⚠️     │ Test first! Can double-count   │
│                       │        │ with custom form tracking      │
└───────────────────────┴────────┴────────────────────────────────┘

SITE SEARCH PARAMETER CONFIGURATION:
──────────────────────────────────────
1. Check current search URL: example.com/search?q=term
2. Identify parameter: "q"
3. Enter in Enhanced Measurement → Site search
4. Test with DebugView

COMMON SEARCH PARAMETERS:
├── q (Google default)
├── s (WordPress default)
├── search
├── query
├── keyword
└── term
```

## Configure Google Signals

```
GOOGLE SIGNALS SETUP
=====================

WHAT IT IS:
├── Cross-device tracking via Google accounts
├── Required for remarketing audiences
├── Demographic data in reports
└── Enhanced conversions support

LOCATION: Admin → Data Settings → Data Collection

SETUP STEPS:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Go to Admin → Data Settings → Data Collection             │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click "Get Started" at Google signals data collection     │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Review and Accept the data collection terms               │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Toggle "Enable Google signals data collection" → ON       │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Choose regions (usually "All regions")                    │
└────┴────────────────────────────────────────────────────────────┘

PRIVACY CONSIDERATIONS:
├── Data thresholding may limit reports at low volume
├── Requires cookie consent in EU (GDPR)
├── Not available for all users (opt-in required)
└── May increase data sampling at high volume
```

## Configure Data Retention

```
DATA RETENTION SETTINGS
========================

LOCATION: Admin → Data Settings → Data Retention

OPTIONS:
┌───────────────────┬────────────────────────────────────────────┐
│ Setting           │ Recommendation                             │
├───────────────────┼────────────────────────────────────────────┤
│ Event data        │ 14 months (maximum for free)               │
│ retention         │ GA360: up to 50 months                     │
├───────────────────┼────────────────────────────────────────────┤
│ User data         │ 14 months (maximum for free)               │
│ retention         │ Contains user-level dimensions              │
├───────────────────┼────────────────────────────────────────────┤
│ Reset user data   │ ON - reset on new activity                 │
│ on new activity   │ Keeps active users longer                  │
└───────────────────┴────────────────────────────────────────────┘

IMPORTANT:
├── Aggregated data (reports) always remains available
├── Retention applies to user-level and event-level data
├── Explorations may be limited after expiry
└── BigQuery export is not affected (if configured)
```

## Google Ads Linking

```
GOOGLE ADS LINKING
===================

WHY LINK:
├── Import GA4 conversions to Google Ads
├── Build remarketing audiences in GA4
├── See Google Ads data in GA4 reports
├── Enable cross-platform attribution
└── Smart Bidding optimization with GA4 data

LOCATION: Admin → Product Links → Google Ads Links

SETUP STEPS:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Click "Link" → Select Google Ads account(s)               │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Enable "Personalized advertising" (for remarketing)       │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Enable auto-tagging in Google Ads (recommended)           │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Click "Submit" → Link is now active                       │
└────┴────────────────────────────────────────────────────────────┘

VERIFICATION:
├── GA4: Admin → Product Links → Google Ads Links → Status "Active"
├── Google Ads: Tools → Linked accounts → Google Analytics
└── Test: Acquisition report should show Google Ads data

AUTO-TAGGING VS UTM:
─────────────────────
✅ AUTO-TAGGING (Recommended):
├── Automatic by Google Ads
├── More accurate than UTM
├── Required for RLSA and remarketing
└── gclid parameter automatically added

UTM ADDITION:
├── Only needed if auto-tagging causes issues
├── Or for third-party tracking alongside GA4
└── Never let UTM + auto-tagging create duplicate data
```

## Search Console Linking

```
SEARCH CONSOLE LINKING
=======================

WHY LINK:
├── See organic search queries in GA4
├── Landing page performance data
├── Search impressions and CTR
└── SEO ↔ Analytics alignment

LOCATION: Admin → Product Links → Search Console Links

REQUIREMENTS:
├── Verified Search Console property
├── Property owner or full user access
└── Same Google account as GA4 admin

SETUP STEPS:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Click "Link" → Select Search Console property             │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Match web stream with Search Console property             │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Submit"                                            │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Data appears within 48 hours                              │
└────┴────────────────────────────────────────────────────────────┘

DATA AVAILABLE AFTER LINKING:
├── Reports → Search Console → Queries
├── Reports → Search Console → Google organic search traffic
└── Explorations with Search Console dimensions
```

## Cross-Domain Tracking

```
CROSS-DOMAIN TRACKING SETUP
=============================

WHEN NEEDED:
├── Checkout on different domain (shop.brand.com → checkout.provider.com)
├── Subdomains that need to be tracked separately
├── Multi-brand sites with shared cart
└── Third-party booking/payment systems

LOCATION: Data Stream → Configure tag settings → Configure your domains

SETUP:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Go to Admin → Data Streams → [your stream]               │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click "Configure tag settings"                            │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Configure your domains"                            │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Add all domains that need to be linked                    │
│    │ Match type: "Contains" usually sufficient                 │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Save and test with DebugView                              │
└────┴────────────────────────────────────────────────────────────┘

EXAMPLE CONFIGURATION:
├── Domain 1: example.com (Contains)
├── Domain 2: checkout.example-pay.com (Contains)
└── Domain 3: shop.example.nl (Contains)

VERIFICATION:
├── Go to domain A → click link to domain B
├── Check URL: should contain _gl parameter
├── Check DebugView: session should continue
└── Check reports: no session breaks
```

## Property Audit Checklist

```
GA4 PROPERTY AUDIT CHECKLIST
==============================

[] PROPERTY SETTINGS
├── [] Correct timezone set
├── [] Correct currency set
├── [] Industry category selected
└── [] Property name is clear

[] DATA STREAMS
├── [] Web stream active
├── [] Measurement ID correctly implemented
├── [] Enhanced Measurement configured
├── [] Site search parameter correct
└── [] Cross-domain tracking (if needed)

[] DATA COLLECTION
├── [] Google Signals enabled (for remarketing)
├── [] Data retention set to 14 months
├── [] User data reset on activity: ON
├── [] Consent Mode v2 implemented (required for EEA since March 2024)
└── [] analytics_storage and ad_storage consent signals verified

[] PRODUCT LINKS
├── [] Google Ads linked
├── [] Search Console linked
├── [] BigQuery export (optional)
└── [] Other products (Merchant Center, etc.)

[] ACCESS & PERMISSIONS
├── [] Correct users with correct roles
├── [] Admin access restricted
├── [] Service accounts documented
└── [] Audit log reviewed

[] KEY EVENTS
├── [] Key events configured in Admin → Key Events
├── [] Key events tested in DebugView
├── [] No duplicate key events
└── [] Primary key events marked (for Google Ads import)

[] AUDIENCES
├── [] Basic audiences created
├── [] Remarketing audiences for Google Ads
└── [] Predictive audiences (if eligible)
```

## Common Problems

```
TROUBLESHOOTING GUIDE
======================

PROBLEM: No data in GA4
─────────────────────────
Causes:
├── Tag not correctly implemented
├── Wrong Measurement ID
├── Ad blocker during testing
├── Consent mode blocking tracking
└── Data delay (up to 24-48 hours)

Solution:
├── Check with GA Debugger browser extension
├── Use DebugView in GA4
├── Verify tag fires in GTM Preview mode
└── Test in Incognito without ad blocker

PROBLEM: Data discrepancies with Google Ads
────────────────────────────────────────────
Causes:
├── Different attribution models
├── Conversion counting difference (one per click vs many)
├── Cross-device tracking gaps
├── Consent mode differences
└── Timezone mismatches

Solution:
├── Align attribution windows
├── Document expected differences (5-15% is normal)
├── Use same conversion counting method
└── Verify timezone settings match

PROBLEM: Enhanced Measurement events not working
──────────────────────────────────────────────────
Causes:
├── Custom implementation conflicts
├── SPA (Single Page App) routing issues
├── Events filtered by consent
└── Wrong event parameters

Solution:
├── Check DebugView for event triggering
├── For SPA: use page_view event on route change
├── Review consent mode implementation
└── Disable conflicting custom events

PROBLEM: Google Signals thresholding
──────────────────────────────────────
Causes:
├── Too little data volume
├── Privacy thresholds applied
└── Specific dimensions combined

Solution:
├── Use broader date ranges
├── Aggregate to higher dimensions
├── Consider BigQuery export for raw data
└── Accept that some data is not available
```

## New in 2026: Analytics Advisor & Cross-Channel Budgeting

```
GA4 2026 FEATURES OVERVIEW
============================

ANALYTICS ADVISOR (Gemini AI in GA4):
├── AI-powered insights surface automatically in the GA4 interface
├── Location: GA4 → Reports → Overview (AI Insights panel)
├── Detects anomalies, trends, and optimization opportunities
├── Ask questions in natural language about your data
└── No extra setup required — available for all GA4 properties

CROSS-CHANNEL BUDGETING (Beta, 2026):
├── Budget planning tool that spans Meta, LinkedIn, TikTok, Snapchat + Google
├── Location: GA4 → Advertising → Cross-channel budgeting
├── Compares attributed conversions across platforms in one view
├── Requires platform integrations (Meta, LinkedIn, TikTok data imports)
└── Uses GA4's data-driven attribution as the single source of truth

PER-CONVERSION ATTRIBUTION SETTINGS (Beta, 2026):
├── Override the property-level model for individual key events
├── Location: Admin → Key Events → [event] → Attribution Settings
├── Useful for mixing DDA (purchases) with last-click (leads) in one property
└── Does not affect Google Ads import — bidding uses Google Ads DDA
```

## Output: GA4 Property Setup Recommendation Template

```markdown
# GA4 Property Setup Report

## Property Information
- **Property name:** [Name]
- **Measurement ID:** G-XXXXXXXXXX
- **Timezone:** [Timezone]
- **Currency:** [Currency]
- **Setup date:** [Date]

## Data Stream Configuration
- **Stream type:** Web / iOS / Android
- **Website URL:** [URL]
- **Enhanced Measurement:** ✅ Configured

### Enhanced Measurement Status
| Event | Status | Notes |
|-------|--------|-------|
| Page views | ✅ | - |
| Scrolls | ✅ | - |
| Outbound clicks | ✅ | - |
| Site search | ✅ | Parameter: [X] |
| Video engagement | ✅ | - |
| File downloads | ✅ | - |
| Form interactions | ⚠️ | [Notes] |

## Data Settings
- **Google Signals:** ✅ Enabled
- **Data retention:** 14 months
- **User data reset:** ✅ Enabled

## Product Links
| Product | Status | Account ID |
|---------|--------|------------|
| Google Ads | ✅ Linked | XXX-XXX-XXXX |
| Search Console | ✅ Linked | [Property] |
| BigQuery | [Status] | [Project ID] |

## Key Events Configured
| Event name | Type | Status |
|------------|------|--------|
| purchase | E-commerce | ✅ Active |
| generate_lead | Lead gen | ✅ Active |
| [Custom event] | [Type] | [Status] |

## Cross-Domain Setup
- **Configured domains:** [List of domains]
- **Verification status:** ✅ Tested and working

## Next Steps
1. [ ] [First action]
2. [ ] [Second action]
3. [ ] [Third action]

## Notes
[Any additional remarks or points of attention]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, verify the setup is actually collecting data:

```python
# Confirm sessions are flowing in — proves property is connected and firing
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["sessions", "totalUsers", "screenPageViews"],
    dimensions=["date"],
    start_date="7daysAgo",
    end_date="today"
)
```

Use this to validate the setup before declaring it complete. Zero sessions after 24h = something is wrong (GTM unpublished, wrong measurement ID, consent block).
