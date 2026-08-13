---
name: ga4-conversion-import
description: "This skill should be used when the user asks to \"import GA4 conversions to Google Ads\", \"set up Smart Bidding conversions\", \"configure conversion counting\", or mentions \"offline conversion import\", \"primary vs secondary conversions\", or \"GA4 to Google Ads export\". Do NOT use for: attribution model selection (use ga4-attribution-advisor), e-commerce event setup (use ga4-ecommerce-setup)."
---
# GA4 Conversion Import Guide

Complete guide for importing GA4 conversions into Google Ads for optimal Smart Bidding performance.

## Google Ads Link Verification

```
GOOGLE ADS LINK VERIFICATION
==============================

STEP 1: CHECK GA4 SIDE
LOCATION: GA4 Admin → Product Links → Google Ads Links

┌─────────────────────┬────────────────────────────────────────┐
│ Check item          │ Expected status                        │
├─────────────────────┼────────────────────────────────────────┤
│ Link status         │ "Active"                               │
├─────────────────────┼────────────────────────────────────────┤
│ Personalized ads    │ Enabled (for remarketing)              │
├─────────────────────┼────────────────────────────────────────┤
│ Auto-tagging        │ Enabled in Google Ads                  │
├─────────────────────┼────────────────────────────────────────┤
│ Linked accounts     │ All relevant Google Ads accounts       │
└─────────────────────┴────────────────────────────────────────┘

STEP 2: CHECK GOOGLE ADS SIDE
LOCATION: Google Ads → Tools → Data Manager → Google Analytics 4

┌─────────────────────┬────────────────────────────────────────┐
│ Check item          │ Expected status                        │
├─────────────────────┼────────────────────────────────────────┤
│ Property status     │ "Linked"                               │
├─────────────────────┼────────────────────────────────────────┤
│ Data sharing        │ Enabled                                │
├─────────────────────┼────────────────────────────────────────┤
│ Import status       │ "Active" per conversion                │
└─────────────────────┴────────────────────────────────────────┘

TROUBLESHOOTING LINK ISSUES:
├── Link not visible? Check permissions on both platforms
├── Status "Error"? Unlink and re-link
├── Data mismatch? Check auto-tagging is ON
└── No import options? Wait 24-48 hours after linking
```

## Configuring GA4 Key Events

```
GA4 KEY EVENTS (CONVERSIONS) SETUP
====================================

TERMINOLOGY NOTE:
├── GA4 UI calls them "Key Events" (since March 2024)
├── Google Ads still calls them "Conversions" after import — this is correct
├── Do not confuse the names: the data is the same, only the label differs
└── When a client says "I don't see conversions in GA4" → show them "Key Events"

LOCATION: GA4 Admin → Data display → Events → Mark as key event

STEP 1: IDENTIFY KEY EVENTS
────────────────────────────
┌─────────────────────┬───────────┬───────────────────────────────┐
│ Event type          │ Priority  │ Import as                     │
├─────────────────────┼───────────┼───────────────────────────────┤
│ purchase            │ HIGH      │ Primary - Every conversion    │
├─────────────────────┼───────────┼───────────────────────────────┤
│ generate_lead       │ HIGH      │ Primary - One per click       │
├─────────────────────┼───────────┼───────────────────────────────┤
│ sign_up             │ HIGH      │ Primary - One per click       │
├─────────────────────┼───────────┼───────────────────────────────┤
│ begin_checkout      │ MEDIUM    │ Secondary observation only    │
├─────────────────────┼───────────┼───────────────────────────────┤
│ add_to_cart         │ MEDIUM    │ Secondary observation only    │
├─────────────────────┼───────────┼───────────────────────────────┤
│ page_view           │ LOW       │ Do not import                 │
├─────────────────────┼───────────┼───────────────────────────────┤
│ scroll              │ LOW       │ Do not import                 │
└─────────────────────┴───────────┴───────────────────────────────┘

STEP 2: MARK AS KEY EVENT
──────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Go to Admin → Data display → Events                       │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Find your event in the list                               │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Toggle "Mark as key event" → ON                           │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Event now appears in Admin → Key events                   │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Wait 24-48 hours for import availability                  │
└────┴────────────────────────────────────────────────────────────┘

KEY EVENT LIMITS:
├── Maximum 30 key events per property
├── Select only events with business value
├── Avoid marking page_view or scroll as key event
└── Custom events must have data first
```

## Importing Conversions in Google Ads

```
GOOGLE ADS IMPORT STEPS
=========================

LOCATION: Google Ads → Goals → Conversions → New conversion action

STEP 1: START IMPORT
─────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Click "+ New conversion action"                           │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Select "Import"                                           │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Choose "Google Analytics 4 properties"                    │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Select "Web" or "App" (match your data stream)            │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Click "Continue"                                          │
└────┴────────────────────────────────────────────────────────────┘

STEP 2: SELECT CONVERSIONS
───────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Check the key events you want to import                   │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Verify each conversion has at least 1 event               │
│    │ (otherwise not importable)                                │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Import and continue"                               │
└────┴────────────────────────────────────────────────────────────┘

STEP 3: CONFIGURE EACH CONVERSION
──────────────────────────────────
For EACH imported conversion, configure:

┌─────────────────────┬────────────────────────────────────────────┐
│ Setting             │ Recommendation per type                    │
├─────────────────────┼────────────────────────────────────────────┤
│ Goal and action     │ Choose most fitting category               │
│ optimization        │ (Purchase, Lead, Sign-up, etc.)            │
├─────────────────────┼────────────────────────────────────────────┤
│ Conversion name     │ Prefix with "GA4 - " for recognition      │
│                     │ E.g.: "GA4 - Purchase"                     │
├─────────────────────┼────────────────────────────────────────────┤
│ Value               │ - E-commerce: "Use different values"       │
│                     │ - Leads: "Use same value" + fill in        │
│                     │ - Note: GA4 sends value along              │
├─────────────────────┼────────────────────────────────────────────┤
│ Count               │ - Purchase: "Every"                        │
│                     │ - Lead/Sign-up: "One"                      │
├─────────────────────┼────────────────────────────────────────────┤
│ Click-through       │ 30-90 days (match your sales cycle)        │
│ window              │                                            │
├─────────────────────┼────────────────────────────────────────────┤
│ View-through        │ 1-7 days (conservative)                    │
│ window              │ Display/Video: 7 days                      │
├─────────────────────┼────────────────────────────────────────────┤
│ Attribution model   │ Data-driven (recommended)                  │
│                     │ Sync with GA4 model if possible            │
└─────────────────────┴────────────────────────────────────────────┘
```

## Primary vs Secondary Conversions

```
PRIMARY VS SECONDARY CONVERSIONS
==================================

DEFINITION:
├── PRIMARY: Used for Smart Bidding optimization
├── SECONDARY: For observation/reporting only
└── Account default: New imports are secondary

LOCATION: Google Ads → Goals → Conversions → [Conversion] → Edit goal

┌─────────────────────┬───────────────────┬───────────────────────┐
│ Conversion type     │ Primary/Secondary │ Rationale             │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Purchase            │ PRIMARY           │ Main e-commerce goal  │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Generate Lead       │ PRIMARY           │ Main lead gen goal    │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Sign Up             │ PRIMARY           │ Main SaaS goal        │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Phone Call (60s+)   │ PRIMARY           │ Qualified call        │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Begin Checkout      │ SECONDARY         │ Micro-conversion      │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Add to Cart         │ SECONDARY         │ Micro-conversion      │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Contact Form View   │ SECONDARY         │ Too early in funnel   │
├─────────────────────┼───────────────────┼───────────────────────┤
│ PDF Download        │ SECONDARY         │ Soft conversion       │
└─────────────────────┴───────────────────┴───────────────────────┘

CONFIGURING PRIMARY CONVERSION:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Go to Goals → Conversions → Summary                       │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click the conversion name                                 │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Edit goal"                                         │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ At "Goal and action optimization":                        │
│    │ - Primary: "Use as primary action for bidding"            │
│    │ - Secondary: "Use as secondary action (observe only)"     │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Save                                                      │
└────┴────────────────────────────────────────────────────────────┘

IMPORTANT RULES:
├── Maximum 1-3 primary conversions (focus bidding)
├── Avoid conflicting primary conversions (lead + purchase)
├── PMax requires minimum 1 primary conversion
├── Too many primary = confusing bidding signals
└── Secondary conversions are still valuable for analysis
```

## Smart Bidding Optimization

```
SMART BIDDING WITH GA4 CONVERSIONS
====================================

MINIMUM VOLUME REQUIREMENTS:
┌─────────────────────────────┬─────────────────────────────────┐
│ Bidding Strategy            │ Minimum conversions             │
├─────────────────────────────┼─────────────────────────────────┤
│ Maximize Conversions        │ 15/month per campaign           │
├─────────────────────────────┼─────────────────────────────────┤
│ Target CPA                  │ 30/month per campaign           │
├─────────────────────────────┼─────────────────────────────────┤
│ Target ROAS                 │ 50/month per campaign           │
│                             │ (with revenue value)            │
├─────────────────────────────┼─────────────────────────────────┤
│ Performance Max             │ 30/month per account            │
└─────────────────────────────┴─────────────────────────────────┘

LEARNING PERIOD:
├── New conversion import: 7-14 days
├── Significant changes: 7 days
├── Avoid major changes during learning
└── Check "Learning" status in campaign overview

CONVERSION LAG SETTINGS:
─────────────────────────
LOCATION: Goals → Conversions → Settings → Conversion window

┌─────────────────────┬────────────────────┬───────────────────┐
│ Business type       │ Click-through      │ View-through      │
├─────────────────────┼────────────────────┼───────────────────┤
│ E-commerce          │ 30 days            │ 1 day             │
├─────────────────────┼────────────────────┼───────────────────┤
│ Lead generation     │ 30-60 days         │ 1-7 days          │
├─────────────────────┼────────────────────┼───────────────────┤
│ B2B SaaS            │ 60-90 days         │ 7 days            │
├─────────────────────┼────────────────────┼───────────────────┤
│ High-value purchase │ 90 days            │ 7 days            │
└─────────────────────┴────────────────────┴───────────────────┘

REPORTING DELAY:
├── GA4 to Google Ads sync: up to 24 hours
├── Conversion reporting: up to 48 hours
├── Attribution updates: up to 7 days
└── Plan your analyses with these delays
```

## Conversion Value Optimization

```
CONVERSION VALUE CONFIGURATION
================================

WHEN TO USE VALUE:
├── E-commerce: always (transaction value)
├── Lead gen: fixed value per lead type
├── SaaS: trial value or LTV-based
└── B2B: deal value if known

SENDING GA4 VALUE:
──────────────────
GA4 event with value parameter:

gtag('event', 'purchase', {
  'value': 150.00,
  'currency': 'EUR'
});

gtag('event', 'generate_lead', {
  'value': 50.00,     // estimated lead value
  'currency': 'EUR'
});

GOOGLE ADS VALUE SETTINGS:
┌─────────────────────┬────────────────────────────────────────────┐
│ Setting             │ When to use                                │
├─────────────────────┼────────────────────────────────────────────┤
│ Use different       │ E-commerce (variable order values)         │
│ values for each     │ GA4 sends value automatically              │
├─────────────────────┼────────────────────────────────────────────┤
│ Use same value      │ Lead gen (fixed value)                     │
│ for each            │ Fill in estimated value                    │
├─────────────────────┼────────────────────────────────────────────┤
│ Don't use value     │ Only for observation conversions           │
│                     │ Not recommended for primary                │
└─────────────────────┴────────────────────────────────────────────┘

LEAD VALUE CALCULATION:
───────────────────────
Formula: Lead Value = (Close Rate x Avg. Deal Size)

Example:
├── Close rate: 10%
├── Avg. deal size: EUR 1,000
├── Lead value: 0.10 x EUR 1,000 = EUR 100 per lead

Lead type tiers:
┌─────────────────────┬────────────┬───────────────────────────────┐
│ Lead Type           │ Value      │ Rationale                     │
├─────────────────────┼────────────┼───────────────────────────────┤
│ Demo request        │ EUR 150    │ High intent, warm lead        │
├─────────────────────┼────────────┼───────────────────────────────┤
│ Contact form        │ EUR 75     │ Medium intent                 │
├─────────────────────┼────────────┼───────────────────────────────┤
│ Newsletter signup   │ EUR 10     │ Low intent, nurture needed    │
├─────────────────────┼────────────┼───────────────────────────────┤
│ Whitepaper download │ EUR 25     │ Research phase                │
└─────────────────────┴────────────┴───────────────────────────────┘
```

## Output: Conversion Import Checklist Template

```markdown
# GA4 Conversion Import Report

## Account Information
- **GA4 Property:** [Property name]
- **Measurement ID:** G-XXXXXXXXXX
- **Google Ads Account:** XXX-XXX-XXXX
- **Link Status:** Active / Not linked

## Key Events Status (GA4)
| Event Name | Key Event | Volume (30d) | Import Status |
|------------|-----------|--------------|---------------|
| purchase | ✅ | [X] | Imported |
| generate_lead | ✅ | [X] | Imported |
| begin_checkout | ❌ | [X] | Secondary only |
| add_to_cart | ❌ | [X] | Not imported |

## Google Ads Conversion Configuration
| Conversion | Goal Type | Count | Value | Attribution | Primary/Sec |
|------------|-----------|-------|-------|-------------|-------------|
| GA4 - Purchase | Purchase | Every | Dynamic | DDA | Primary |
| GA4 - Lead | Lead | One | EUR 100 | DDA | Primary |
| GA4 - Checkout | Add to cart | Every | - | DDA | Secondary |

## Conversion Windows
| Conversion | Click-through | View-through | Rationale |
|------------|---------------|--------------|-----------|
| Purchase | 30 days | 1 day | E-commerce standard |
| Lead | 60 days | 7 days | Long consideration |

## Smart Bidding Readiness
| Check | Status | Details |
|-------|--------|---------|
| Minimum volume (30/mo) | ✅/❌ | [X] conversions |
| Single primary focus | ✅/❌ | [X] primary conversions |
| Value tracking | ✅/❌ | [Dynamic/Fixed/None] |
| Learning period | ✅/❌ | [X] days active |

## Volume Analysis
- **Conversions last 30 days:** [X]
- **Expected volume next 30 days:** [X]
- **Suitable for Smart Bidding:** ✅/❌

## Recommendations

### Immediate Actions
1. [ ] [Action 1]
2. [ ] [Action 2]

### Optimization Suggestions
1. [ ] [Suggestion 1]
2. [ ] [Suggestion 2]

## Data Sync Verification
- **Last GA4 → Google Ads sync:** [Date/time]
- **Data lag:** [X] hours
- **Discrepancy percentage:** [X]% (target: < 15%)

## Notes
[Additional observations, deviations, or special configurations]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, check key event counts before setting up the import to establish a baseline:

```python
# Get key event counts to verify volume and consistency before importing to Google Ads
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["keyEvents", "sessions"],
    dimensions=["date", "sessionDefaultChannelGroup"],
    start_date="30daysAgo",
    end_date="today"
)
```

Use this baseline to detect post-import discrepancies. If Google Ads shows significantly more conversions than GA4 key events, attribution windows or cross-device matching is inflating numbers.
