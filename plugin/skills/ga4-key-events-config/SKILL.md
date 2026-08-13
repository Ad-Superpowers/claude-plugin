---
name: ga4-key-events-config
description: "This skill should be used when the user asks to \"configure key events\", \"set up conversions\", \"mark events as key events\", or mentions \"conversion values\", \"primary vs secondary conversions\", or \"GA4 goal setup\". Do NOT use for: event tracking setup (use ga4-event-tracking-setup), Google Ads conversion import details (use ga4-conversion-import), or attribution models (use ga4-attribution-advisor)."
---
# GA4 Key Events Configuration

Complete guide for configuring Key Events (formerly "Conversions") in Google Analytics 4 for optimal advertising performance.

## Quick Decision Tree

```
WHICH EVENTS SHOULD BECOME KEY EVENTS?
│
├─► BUSINESS-CRITICAL ACTIONS
│   ├── E-commerce: purchase, begin_checkout
│   ├── Lead Gen: generate_lead, sign_up, contact_form
│   ├── SaaS: trial_start, subscription_start
│   └── Content: newsletter_signup, download
│       └─► MARK AS KEY EVENT ✅
│
├─► ENGAGEMENT EVENTS
│   ├── page_view, scroll, video_start
│   ├── cta_click, outbound_click
│   └── time_on_page
│       └─► NOT as Key Event (unless primary goal)
│
├─► MICRO-CONVERSIONS
│   ├── add_to_cart, view_item
│   ├── pricing_page_view
│   └── chat_open
│       └─► CONSIDER as secondary conversion
│
└─► FOR GOOGLE ADS IMPORT
    ├─► Primary Conversion: Main KPI (purchase, lead)
    ├─► Secondary Conversion: Optimization signals
    └─► Choose MAX 1-2 primary per campaign type
```

## Key Events vs Events

```
KEY EVENTS EXPLAINED (2024+ terminology)
==========================================

┌────────────────────────────────────────────────────────────────┐
│  EVENTS                          KEY EVENTS                   │
│  ═══════════════════════════     ═══════════════════════════  │
│  All user actions                Most important actions        │
│                                                                │
│  Automatically tracked:          Marked by you:                │
│  ├── page_view                   ├── purchase                 │
│  ├── scroll                      ├── generate_lead            │
│  ├── click                       ├── sign_up                  │
│  ├── file_download               └── [your business goals]    │
│  └── etc.                                                      │
│                                                                │
│  Visible in: Events reports      Visible in: Key Events       │
│                                  + Conversion reports          │
│                                  + Can import to Ads           │
└────────────────────────────────────────────────────────────────┘

TERMINOLOGY CHANGE:
├── "Conversions" → "Key Events" (GA4 interface, 2024)
├── Still "Conversions" in Google Ads
├── Same functionality, new name
└── Import to Google Ads remains "Conversion Import"
```

## Marking a Key Event

```
MARKING AN EVENT AS KEY EVENT
==============================

METHOD 1: Via Events Report
────────────────────────────
LOCATION: Reports → Engagement → Events

STEPS:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Go to Events report                                       │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Find the event you want to mark                           │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click the toggle in "Mark as key event" column            │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Toggle to ON (blue)                                       │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Event is now a Key Event                                  │
└────┴────────────────────────────────────────────────────────────┘

METHOD 2: Via Admin → Key Events
─────────────────────────────────
LOCATION: Admin → Data display → Key events

STEPS:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Click "New key event"                                     │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Enter the exact event name (case-sensitive!)              │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Save"                                              │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Event becomes a Key Event once data arrives               │
└────┴────────────────────────────────────────────────────────────┘

IMPORTANT:
├── Event name must match EXACTLY (case-sensitive)
├── Event must already exist OR becomes active on first trigger
├── Retroactive: only new data from moment of marking
└── Max ~30 key events per property (soft limit)
```

## Conversion Value Setup

```
CONVERSION VALUE CONFIGURATION
================================

WHY ASSIGN VALUE?
├── Value-based bidding in Google Ads (tROAS)
├── ROI calculations in reports
├── Prioritization of conversion types
└── Better budget allocation advice

METHOD 1: Dynamic Value (recommended for e-commerce)
─────────────────────────────────────────────────────

Send value with the event:

GTM GA4 Event Tag:
├── Event name: purchase
├── Event Parameters:
│   ├── value: {{DLV - transaction_value}}
│   ├── currency: EUR
│   └── transaction_id: {{DLV - order_id}}

Or via gtag.js:
```javascript
gtag('event', 'purchase', {
  'transaction_id': 'T12345',
  'value': 150.00,
  'currency': 'EUR',
  'items': [...]
});
```

METHOD 2: Static Value (for lead gen)
──────────────────────────────────────

LOCATION: Admin → Key events → Click event → "Edit"

CONFIGURATION:
┌────────────────────────────────────────────────────────────────┐
│ Default conversion value: [X]                                  │
│ Currency: EUR                                                  │
│                                                                │
│ NOTE: This does NOT override dynamic values                    │
│    Only used when no value is sent with the event              │
└────────────────────────────────────────────────────────────────┘

VALUE CALCULATION FOR LEAD GEN:
────────────────────────────────
Lead Value = Average Deal Size x Close Rate

Example:
├── Average deal: €5,000
├── Close rate: 10%
├── Lead value: €5,000 x 0.10 = €500

Alternative per lead type:
├── Contact form: €100
├── Demo request: €300
├── Phone call: €150
└── Chat lead: €75
```

## Counting Method

```
CONVERSION COUNTING CONFIGURATION
====================================

LOCATION: Admin → Key events → [event] → Edit

OPTIONS:
┌─────────────────┬───────────────────────────────────────────────┐
│ Once per event  │ Every time the event fires = 1 conversion     │
│ (default)       │ ✅ Use for: purchases, form submits            │
│                 │                                                │
│                 │ Example: 3x purchase = 3 conversions           │
├─────────────────┼───────────────────────────────────────────────┤
│ Once per        │ Max 1 conversion per session                  │
│ session         │ ✅ Use for: signups, lead forms                │
│                 │                                                │
│                 │ Example: 3x form submit = 1 conversion         │
└─────────────────┴───────────────────────────────────────────────┘

RECOMMENDATIONS PER USE CASE:
──────────────────────────────

E-COMMERCE:
├── purchase → Once per event (each order counts)
├── begin_checkout → Once per session (1 intent per session)
├── add_to_cart → Once per event (counts volume)
└── view_item → Not as conversion

LEAD GENERATION:
├── generate_lead → Once per session (1 lead per session)
├── phone_click → Once per session (1 intent per session)
├── form_submit → Once per session
└── contact_request → Once per session

SAAS:
├── trial_start → Once per session
├── subscription_purchase → Once per event (each subscription)
├── upgrade → Once per event
└── feature_activation → Once per session
```

## Primary vs Secondary Conversions

```
PRIMARY VS SECONDARY FOR GOOGLE ADS
======================================

CONCEPT:
┌────────────────────────────────────────────────────────────────┐
│  PRIMARY CONVERSIONS              SECONDARY CONVERSIONS        │
│  ═══════════════════════════     ═══════════════════════════  │
│  Used for:                       Used for:                     │
│  ├── Smart Bidding optimization  ├── Reporting/observation     │
│  ├── ROAS/CPA calculation        ├── Funnel insights           │
│  └── Budget optimization         └── Additional signals        │
│                                                                │
│  Impact on bidding: YES          Impact on bidding: NO         │
│                                                                │
│  Example:                        Example:                      │
│  └── purchase                    ├── add_to_cart               │
│  └── qualified_lead              ├── begin_checkout            │
│                                  └── page_view (pricing)       │
└────────────────────────────────────────────────────────────────┘

WHEN TO CHOOSE:
├── Primary is determined at import in Google Ads
├── GA4 only marks as "key event"
├── Google Ads distinguishes primary/secondary
└── Choose in: Google Ads → Goals → Conversions → Settings

BEST PRACTICES:
────────────────
✅ MAX 1-2 PRIMARY conversions per campaign type
✅ Use same primary across related campaigns
✅ Secondary for observation without bidding impact
✅ Keep consistent over time (AI needs history)

AVOID:
├── Too many primary conversions (confuses algorithm)
├── Mix of upper and lower funnel as primary
├── Constantly switching primary
└── Overlapping conversions as primary
```

## Recommended Key Events per Business Type

```
KEY EVENT CONFIGURATION PER BUSINESS TYPE
===========================================

E-COMMERCE
──────────
┌──────────────────┬──────────┬──────────┬─────────────────────┐
│ Event            │ Priority │ Value    │ Counting            │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ purchase         │ Primary  │ Dynamic  │ Once per event      │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ begin_checkout   │ Secondary│ €5-10    │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ add_to_cart      │ Secondary│ €2-5     │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ add_payment_info │ Secondary│ €3-7     │ Once per session    │
└──────────────────┴──────────┴──────────┴─────────────────────┘

LEAD GENERATION (B2B)
─────────────────────
┌──────────────────┬──────────┬──────────┬─────────────────────┐
│ Event            │ Priority │ Value    │ Counting            │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ generate_lead    │ Primary  │ €50-500  │ Once per session    │
│ (demo request)   │          │          │                     │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ phone_click      │ Secondary│ €30-100  │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ contact_submit   │ Secondary│ €20-50   │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ pricing_view     │ Secondary│ €5-10    │ Once per session    │
└──────────────────┴──────────┴──────────┴─────────────────────┘

SAAS / SUBSCRIPTION
───────────────────
┌──────────────────┬──────────┬──────────┬─────────────────────┐
│ Event            │ Priority │ Value    │ Counting            │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ trial_start      │ Primary  │ €25-100  │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ subscription_    │ Primary  │ Dynamic  │ Once per event      │
│ purchase         │          │ (MRR)    │                     │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ sign_up          │ Secondary│ €10-30   │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ feature_activate │ Secondary│ €5-15    │ Once per session    │
└──────────────────┴──────────┴──────────┴─────────────────────┘

CONTENT / PUBLISHER
───────────────────
┌──────────────────┬──────────┬──────────┬─────────────────────┐
│ Event            │ Priority │ Value    │ Counting            │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ newsletter_      │ Primary  │ €5-20    │ Once per session    │
│ signup           │          │          │                     │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ premium_article_ │ Secondary│ €2-5     │ Once per session    │
│ view             │          │          │                     │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ content_download │ Secondary│ €3-10    │ Once per event      │
└──────────────────┴──────────┴──────────┴─────────────────────┘
```

## Key Event Validation

```
KEY EVENT TESTING WORKFLOW
===========================

STEP 1: Check in DebugView
───────────────────────────
LOCATION: Admin → DebugView

VERIFICATION:
├── Event appears in stream
├── Event is marked with key event indicator
├── Parameters correct (value, currency)
└── No duplicate events

STEP 2: Check in Realtime
──────────────────────────
LOCATION: Reports → Realtime

VERIFICATION:
├── Key event count increments
├── Conversion card shows event
└── Value is registered (if applicable)

STEP 3: Check in Key Events Report
────────────────────────────────────
LOCATION: Reports → Engagement → Key events

NOTE: Data may be delayed 24-48 hours

VERIFICATION:
├── Event appears in list
├── Count is correct
├── Value is correct
└── Trend looks normal

STEP 4: Check in Admin → Key Events
─────────────────────────────────────
LOCATION: Admin → Data display → Key events

VERIFICATION:
├── Event status: Active
├── Counting method correct
├── Value correctly configured
└── No duplicate entries
```

## MCP Tool: Verify Key Event Performance

Use `ga4_run_report()` to check key event counts and trends:

```python
# Check key event counts over last 30 days
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="30daysAgo",
    end_date="yesterday",
    metrics=["keyEvents", "sessionKeyEventRate"],
    dimensions=["eventName", "date"]
)
# Note: filter by eventName in your analysis — ga4_run_report returns all events
```

## Google Ads Conversion Import Preparation

```
PREPARING FOR GOOGLE ADS IMPORT
==================================

CHECKLIST FOR GA4 KEY EVENTS:
┌────┬────────────────────────────────────────────────────────────┐
│ [] │ Key Event correctly marked in GA4                         │
├────┼────────────────────────────────────────────────────────────┤
│ [] │ Event has value (dynamic or static)                       │
├────┼────────────────────────────────────────────────────────────┤
│ [] │ Currency correctly set                                    │
├────┼────────────────────────────────────────────────────────────┤
│ [] │ Counting method correct (once per event/session)          │
├────┼────────────────────────────────────────────────────────────┤
│ [] │ Google Ads account linked with GA4                        │
├────┼────────────────────────────────────────────────────────────┤
│ [] │ Sufficient conversions for reliable data (50+/month)      │
├────┼────────────────────────────────────────────────────────────┤
│ [] │ DebugView test passed                                     │
└────┴────────────────────────────────────────────────────────────┘

IMPORT FLOW (AFTER PREPARATION):
──────────────────────────────────
1. Google Ads → Goals → Conversions
2. + New conversion action
3. Import → Google Analytics 4 properties
4. Select your property
5. Select key event(s) to import
6. Configure as Primary or Secondary
7. Save

IMPORT CONSIDERATIONS:
├── Import sync takes 4-6 hours initially
├── Ongoing sync: every few hours
├── 5-15% discrepancy with native GA4 is normal
├── Attribution window differences exist
└── ALWAYS test before modifying live campaigns
```

## Troubleshooting

```
KEY EVENT TROUBLESHOOTING
==========================

PROBLEM: Key Event is not counting
────────────────────────────────────
Checklist:
[] Is the event actually firing? (DebugView)
[] Is the event name EXACTLY correct (case-sensitive)?
[] Is the counting method correctly set?
[] Has consent been given? (consent mode)
[] Are you waiting long enough? (24-48 hours processing)

PROBLEM: Value is not being registered
────────────────────────────────────────
Checklist:
[] Is 'value' parameter being sent?
[] Is value a NUMBER, not a string?
[] Is 'currency' parameter being sent?
[] Currency code correct? (EUR, USD, not "euro")
[] Is default value set as fallback?

PROBLEM: Duplicate Key Events
──────────────────────────────
Causes:
├── Event is triggered multiple times
├── GTM tag fires multiple times
├── SPA route changes re-trigger
└── Page refresh triggers again

Solution:
├── Review trigger conditions in GTM
├── Use "Once per session" counting
├── Implement event deduplication
└── Add session-based blocking trigger

PROBLEM: Key Event not appearing in Google Ads
───────────────────────────────────────────────
Checklist:
[] Is Google Ads account linked?
[] Is the link active? (check both sides)
[] Are you waiting long enough? (24-48 hours first sync)
[] Is the correct property selected?
[] Do you have permissions in both accounts?

PROBLEM: Conversion count differs GA4 vs Google Ads
────────────────────────────────────────────────────
Normal: 5-15% difference is acceptable

Causes for larger difference:
├── Different attribution windows
├── Different counting methods
├── Time zone differences
├── Cross-device tracking differences
└── Consent mode differences

Solution:
├── Align attribution windows
├── Document expected difference
├── Use GA4 as source of truth for reporting
└── Use Google Ads numbers for bidding decisions
```

## Key Event Audit Checklist

```
KEY EVENT CONFIGURATION AUDIT
==============================

[] INVENTORY
├── [] All key events documented
├── [] No unnecessary key events active
├── [] Consistent with business goals
└── [] Aligned with advertising strategy

[] VALUE CONFIGURATION
├── [] Primary conversions have value
├── [] Values are realistic (not €0 or €999999)
├── [] Currency correct
└── [] Dynamic values where possible

[] COUNTING CONFIGURATION
├── [] Counting method fits use case
├── [] No over-counting from duplicates
├── [] Consistent across related events
└── [] Documented

[] GOOGLE ADS ALIGNMENT
├── [] Important key events imported
├── [] Primary/Secondary correctly set
├── [] Attribution settings aligned
└── [] Conversion lag windows appropriate

[] TESTING
├── [] All key events tested in DebugView
├── [] Values correctly registered
├── [] No duplicate counting
└── [] Realtime tracking working
```

## Output: Key Events Configuration Template

```markdown
# Key Events Configuration Report

## Property Information
- **Property:** [Property Name]
- **Measurement ID:** G-XXXXXXXXXX
- **Configuration date:** [Date]

## Key Events Overview

### Primary Key Events (for bidding)
| Event Name | Value | Counting | Google Ads Status |
|------------|-------|----------|-------------------|
| purchase | Dynamic | Per event | ✅ Imported (Primary) |
| generate_lead | €200 | Per session | ✅ Imported (Primary) |

### Secondary Key Events (for observation)
| Event Name | Value | Counting | Google Ads Status |
|------------|-------|----------|-------------------|
| begin_checkout | €10 | Per session | ✅ Imported (Secondary) |
| add_to_cart | €3 | Per session | Not imported |
| phone_click | €50 | Per session | ✅ Imported (Secondary) |

## Value Calculation

### Lead Value Calculation
```
Average Deal Size: €[X]
Close Rate: [X]%
Calculated Lead Value: €[X]
Applied Value: €[X]
```

### E-commerce Value
```
Method: Dynamic (transaction value)
Currency: EUR
Fallback Value: €[X] (if no value sent)
```

## Counting Method Rationale

| Event | Method | Rationale |
|-------|--------|-----------|
| purchase | Per event | Each order is a separate transaction |
| generate_lead | Per session | Prevent duplicate leads |
| begin_checkout | Per session | 1 checkout intent per visit |

## Google Ads Import Status
- **Link Status:** ✅ Active
- **Import Sync:** Every 4-6 hours
- **Last Sync:** [Date/time]

## Validation Status
- [x] DebugView test passed
- [x] Realtime tracking verified
- [x] Value registration confirmed
- [x] No duplicate counting
- [x] Google Ads import verified

## Recommendations
1. [First recommendation]
2. [Second recommendation]
3. [Third recommendation]

## Notes
[Any points of attention or specifics]
```
