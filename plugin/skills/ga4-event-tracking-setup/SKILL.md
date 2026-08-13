---
name: ga4-event-tracking-setup
description: "This skill should be used when the user asks to \"set up GA4 events\", \"configure custom events\", \"track form submissions\", or mentions \"click tracking\", \"GA4 event parameters\", or \"user properties\". Do NOT use for: Data Layer implementation (use ga4-data-layer-guide), key events/conversions setup (use ga4-key-events-config), or e-commerce event tracking (use ga4-ecommerce-setup)."
---
# GA4 Event Tracking Setup

Complete guide for implementing custom event tracking in Google Analytics 4 via Google Tag Manager.

## GA4 Event Model Basics

```
GA4 EVENT STRUCTURE
===================

┌────────────────────────────────────────────────────────────────┐
│  EVERY HIT IN GA4 IS AN EVENT                                  │
│                                                                │
│  Event Name: generate_lead                                     │
│  ├── Parameter 1: form_name = "contact_form"                   │
│  ├── Parameter 2: form_location = "footer"                     │
│  ├── Parameter 3: lead_value = 50                              │
│  └── Parameter 4: page_location = (automatic)                  │
│                                                                │
│  AUTOMATIC PARAMETERS (always included):                       │
│  ├── page_location (URL)                                       │
│  ├── page_title                                                │
│  ├── page_referrer                                             │
│  ├── screen_resolution                                         │
│  ├── language                                                  │
│  └── engagement_time_msec                                      │
└────────────────────────────────────────────────────────────────┘

LIMITS:
├── Event name: max 40 characters
├── Parameter name: max 40 characters
├── Parameter value: max 100 characters
├── Parameters per event: max 25
└── Unique event names per property: max 500
```

## Event Naming Conventions

```
EVENT NAMING BEST PRACTICES
============================

FORMAT: [object]_[action] in snake_case

EXAMPLES:
┌─────────────────────┬────────────────────────────────────────┐
│ Action              │ Event Name                             │
├─────────────────────┼────────────────────────────────────────┤
│ Submit form         │ form_submit                            │
├─────────────────────┼────────────────────────────────────────┤
│ Click CTA           │ cta_click                              │
├─────────────────────┼────────────────────────────────────────┤
│ Play video          │ video_play                             │
├─────────────────────┼────────────────────────────────────────┤
│ Download PDF        │ pdf_download                           │
├─────────────────────┼────────────────────────────────────────┤
│ Newsletter signup   │ newsletter_signup                      │
├─────────────────────┼────────────────────────────────────────┤
│ Open chat           │ chat_open                              │
├─────────────────────┼────────────────────────────────────────┤
│ Use calculator      │ calculator_use                         │
├─────────────────────┼────────────────────────────────────────┤
│ View pricing        │ pricing_view                           │
└─────────────────────┴────────────────────────────────────────┘

AVOID:
├── Spaces: "form submit" → form_submit
├── Capitals: "FormSubmit" → form_submit
├── Special characters: "form-submit!" → form_submit
├── Too-long names: "user_clicked_the_contact_button" → contact_click
└── Generic names: "click", "event", "action"

USE RECOMMENDED EVENTS where possible:
├── generate_lead (not: lead_generated, form_complete)
├── sign_up (not: signup, registration, user_signup)
├── purchase (not: buy, order, transaction)
└── add_to_cart (not: cart_add, add_item)
```

## Form Tracking Setup

```
FORM SUBMISSION TRACKING
=========================

METHOD 1: GTM Form Submission Trigger (simplest)
─────────────────────────────────────────────────

TRIGGER SETUP:
┌────────────────────────────────────────────────────────────────┐
│ Trigger Type: Form Submission                                  │
│                                                                │
│ Wait for Tags: ✅ Check                                        │
│ Max wait time: 2000ms                                          │
│                                                                │
│ Check Validation: ✅ Check (valid submits only)                │
│                                                                │
│ Trigger fires on:                                              │
│ ├── Some Forms (recommended)                                   │
│ └── Form ID / Form Classes contains: [your form identifier]   │
└────────────────────────────────────────────────────────────────┘

TAG SETUP (GA4 Event):
┌────────────────────────────────────────────────────────────────┐
│ Tag Type: Google Analytics: GA4 Event                          │
│                                                                │
│ Configuration Tag: [Your GA4 Config tag]                       │
│ Event Name: generate_lead                                      │
│                                                                │
│ Event Parameters:                                              │
│ ├── form_name: {{Form ID}} or hardcoded                        │
│ ├── form_location: {{Page Path}}                               │
│ └── method: "form"                                             │
└────────────────────────────────────────────────────────────────┘

METHOD 2: dataLayer Push (for complex forms)
─────────────────────────────────────────────

JAVASCRIPT (on form success):
```javascript
// After successful form submit
dataLayer.push({
  'event': 'form_submit',
  'form_name': 'contact_form',
  'form_location': 'homepage_hero',
  'lead_value': 50
});
```

GTM TRIGGER:
├── Type: Custom Event
├── Event name: form_submit
└── Fires on: All Custom Events

TAG (GA4 Event):
├── Event name: generate_lead
├── Parameters: Pull from Data Layer variables
└── form_name: {{DLV - form_name}}

METHOD 3: Thank You Page (fallback)
────────────────────────────────────

TRIGGER:
├── Type: Page View
├── Fires on: Some Page Views
└── Page Path contains: /thank-you or /thanks

TAG:
├── Event name: generate_lead
├── Parameters: form_name = {{Page Referrer}} or hardcoded
└── DOWNSIDE: Misses direct form context
```

## Click Tracking Setup

```
CLICK TRACKING CONFIGURATION
==============================

STEP 1: Enable Built-in Variables (GTM)
────────────────────────────────────────
Variables → Configure → Enable:
├── Click Element
├── Click Classes
├── Click ID
├── Click Target
├── Click URL
└── Click Text

STEP 2: Create Click Trigger
─────────────────────────────

TYPE A: All Elements Click (for buttons, divs, etc.)
┌────────────────────────────────────────────────────────────────┐
│ Trigger Type: Click - All Elements                             │
│                                                                │
│ Trigger fires on: Some Clicks                                  │
│                                                                │
│ Conditions (one or more):                                      │
│ ├── Click Classes contains: cta-button                         │
│ ├── Click ID equals: main-cta                                  │
│ ├── Click Text contains: "Request Demo"                        │
│ └── Click Element matches CSS: .hero-section .btn-primary      │
└────────────────────────────────────────────────────────────────┘

TYPE B: Just Links Click (for <a> tags)
┌────────────────────────────────────────────────────────────────┐
│ Trigger Type: Click - Just Links                               │
│                                                                │
│ Wait for Tags: ✅ Check                                        │
│ Max wait time: 2000ms                                          │
│                                                                │
│ Check Validation: ✅ Check                                     │
│                                                                │
│ Trigger fires on: Some Link Clicks                             │
│ Click URL contains: tel: / mailto: / .pdf                      │
└────────────────────────────────────────────────────────────────┘

STEP 3: Create GA4 Event Tag
─────────────────────────────
┌────────────────────────────────────────────────────────────────┐
│ Tag Type: GA4 Event                                            │
│                                                                │
│ Event Name: cta_click                                          │
│                                                                │
│ Event Parameters:                                              │
│ ├── click_text: {{Click Text}}                                 │
│ ├── click_url: {{Click URL}}                                   │
│ ├── click_location: {{Page Path}}                              │
│ └── click_element: {{Click Classes}}                           │
└────────────────────────────────────────────────────────────────┘
```

## Phone & Email Click Tracking

```
PHONE & EMAIL TRACKING
=======================

PHONE CLICKS (tel: links)
──────────────────────────

TRIGGER:
├── Type: Click - Just Links
├── Fires on: Some Link Clicks
└── Click URL starts with: tel:

TAG:
├── Event name: phone_click
├── Parameters:
│   ├── phone_number: {{Click URL}} (strip 'tel:' via variable)
│   └── click_location: {{Page Path}}

VARIABLE (Clean phone number):
├── Type: Custom JavaScript
└── Code:
```javascript
function() {
  var url = {{Click URL}};
  return url.replace('tel:', '').replace(/\s/g, '');
}
```

EMAIL CLICKS (mailto: links)
─────────────────────────────

TRIGGER:
├── Type: Click - Just Links
├── Fires on: Some Link Clicks
└── Click URL starts with: mailto:

TAG:
├── Event name: email_click
├── Parameters:
│   ├── email_address: (consider privacy implications)
│   └── click_location: {{Page Path}}

PRIVACY NOTE:
├── Consider hashing email addresses
├── Or only count occurrences, don't store the value
└── Check GDPR compliance
```

## Video Tracking Setup

```
VIDEO TRACKING CONFIGURATION
==============================

YOUTUBE VIDEOS (Enhanced Measurement)
──────────────────────────────────────
GA4 automatically tracks YouTube embeds with Enhanced Measurement:
├── video_start
├── video_progress (10%, 25%, 50%, 75%)
└── video_complete

Requirements:
├── Enhanced Measurement → Video engagement: ON
├── YouTube embed with JS API enabled
└── ?enablejsapi=1 in iframe src (added automatically)

CUSTOM VIDEO PLAYERS (Vimeo, HTML5, etc.)
──────────────────────────────────────────

STEP 1: YouTube Video Trigger in GTM
├── Type: YouTube Video
├── Capture: Start, Complete, Pause, Progress
├── Progress percentages: 25, 50, 75, 90

STEP 2: For Vimeo/HTML5 - Custom JavaScript
```javascript
// HTML5 Video Tracking
document.querySelectorAll('video').forEach(function(video) {

  video.addEventListener('play', function() {
    dataLayer.push({
      'event': 'video_play',
      'video_title': this.getAttribute('data-title') || 'Unknown',
      'video_provider': 'html5',
      'video_url': this.currentSrc
    });
  });

  video.addEventListener('ended', function() {
    dataLayer.push({
      'event': 'video_complete',
      'video_title': this.getAttribute('data-title') || 'Unknown',
      'video_provider': 'html5'
    });
  });
});
```

STEP 3: GA4 Event Tag
├── Trigger: Custom Event = video_play / video_complete
├── Event name: video_start / video_complete
├── Parameters:
│   ├── video_title: {{DLV - video_title}}
│   ├── video_provider: {{DLV - video_provider}}
│   └── video_percent: {{DLV - video_percent}}
```

## Scroll Depth Tracking

```
SCROLL DEPTH TRACKING
======================

ENHANCED MEASUREMENT (default)
───────────────────────────────
GA4 automatically tracks 90% scroll depth.
Event name: scroll

CUSTOM SCROLL DEPTH (multiple thresholds)
──────────────────────────────────────────

TRIGGER SETUP:
┌────────────────────────────────────────────────────────────────┐
│ Trigger Type: Scroll Depth                                     │
│                                                                │
│ Scroll Depth Type: ✅ Vertical Scroll Depths                   │
│ Percentages: 25, 50, 75, 90                                    │
│                                                                │
│ Trigger fires on: All Pages or Some Pages                      │
│ (Filter on important content pages)                            │
└────────────────────────────────────────────────────────────────┘

ENABLE BUILT-IN VARIABLES:
├── Scroll Depth Threshold
├── Scroll Depth Units
└── Scroll Direction

TAG SETUP:
├── Event name: scroll_depth
├── Parameters:
│   ├── scroll_percent: {{Scroll Depth Threshold}}
│   ├── page_path: {{Page Path}}
│   └── content_type: (optional, hardcoded or via variable)

NOTE:
├── Disable Enhanced Measurement scroll if using custom
├── Otherwise you get duplicate data
└── Custom provides more granularity
```

## User Properties Setup

```
USER PROPERTIES CONFIGURATION
===============================

WHAT ARE USER PROPERTIES?
├── Attributes that belong to a USER (not to an event)
├── Persistent across sessions
├── Used for segmentation
└── Max 25 user properties per property

EXAMPLES:
┌─────────────────────┬────────────────────────────────────────┐
│ User Property       │ Example Value                          │
├─────────────────────┼────────────────────────────────────────┤
│ membership_level    │ free / pro / enterprise                │
├─────────────────────┼────────────────────────────────────────┤
│ customer_type       │ new / returning / vip                  │
├─────────────────────┼────────────────────────────────────────┤
│ industry            │ ecommerce / saas / agency              │
├─────────────────────┼────────────────────────────────────────┤
│ signup_date         │ 2024-01-15                             │
├─────────────────────┼────────────────────────────────────────┤
│ lifetime_value      │ 500                                    │
└─────────────────────┴────────────────────────────────────────┘

IMPLEMENTATION VIA GTM:
────────────────────────

GA4 CONFIG TAG → User Properties:
┌────────────────────────────────────────────────────────────────┐
│ Property Name: membership_level                                │
│ Value: {{DLV - user_membership}} or {{Cookie - membership}}    │
│                                                                │
│ Property Name: customer_type                                   │
│ Value: {{DLV - customer_type}}                                 │
└────────────────────────────────────────────────────────────────┘

OR VIA DATA LAYER:
```javascript
dataLayer.push({
  'user_properties': {
    'membership_level': 'pro',
    'customer_type': 'returning',
    'lifetime_value': 500
  }
});
```

GA4 REGISTRATION:
├── Admin → Custom definitions → Custom dimensions
├── Scope: User
├── Dimension name: Membership Level
├── User property: membership_level
└── Must be registered to appear in reports!
```

## Custom Dimensions & Metrics

```
REGISTERING CUSTOM DIMENSIONS
===============================

LOCATION: Admin → Custom definitions → Custom dimensions

EVENT-SCOPED DIMENSIONS (most commonly used):
┌─────────────────────┬─────────────┬────────────────────────────┐
│ Dimension Name      │ Event Param │ Use Case                   │
├─────────────────────┼─────────────┼────────────────────────────┤
│ Form Name           │ form_name   │ Which form was submitted   │
├─────────────────────┼─────────────┼────────────────────────────┤
│ CTA Location        │ cta_location│ Where the CTA was placed   │
├─────────────────────┼─────────────┼────────────────────────────┤
│ Content Type        │ content_type│ Blog, product, landing page│
├─────────────────────┼─────────────┼────────────────────────────┤
│ Product Category    │ item_category│ For e-commerce            │
├─────────────────────┼─────────────┼────────────────────────────┤
│ Author              │ author      │ Content creator            │
└─────────────────────┴─────────────┴────────────────────────────┘

CUSTOM METRICS:
├── Scope: Event
├── Example: Lead Value, Engagement Score
└── Unit of measurement: Standard / Currency / Time

LIMITS:
├── Event-scoped dimensions: 50
├── User-scoped dimensions: 25
├── Custom metrics: 50
└── Once created, name cannot be changed
```

## GTM Preview & Debug

```
EVENT TESTING WORKFLOW
=======================

STEP 1: GTM Preview Mode
─────────────────────────
├── In GTM: Click "Preview"
├── Enter website URL
├── Preview window opens
└── Tag Assistant shows all firing tags

STEP 2: Check Tag Firing
─────────────────────────
In Tag Assistant panel:
├── ✅ Green = Tag fired successfully
├── Red = Tag blocked or error
├── Check "Tags Fired" vs "Tags Not Fired"
└── Click tag for details (parameters, trigger)

STEP 3: GA4 DebugView
──────────────────────
LOCATION: GA4 → Admin → DebugView

ENABLE:
├── GTM Preview auto-enables DebugView
├── Or: gtag('config', 'G-XXX', { 'debug_mode': true });
├── Or: URL parameter ?debug_mode=1
└── Check: GA Debugger browser extension

WHAT TO CHECK:
├── Event name correct
├── All parameters present
├── Parameter values correct
├── User properties set
└── Timestamp and order

STEP 4: Realtime Reports
─────────────────────────
LOCATION: GA4 → Reports → Realtime
├── Check event count
├── Check parameter values (click event card)
└── Verify user count
```

## Event Tracking Checklist

```
PRE-LAUNCH EVENT TRACKING CHECKLIST
=====================================

[] PLANNING
├── [] Event tracking plan documented
├── [] Event names follow naming conventions
├── [] Parameters defined per event
└── [] Custom dimensions planned

[] IMPLEMENTATION
├── [] GTM container correctly installed
├── [] GA4 Config tag present
├── [] Built-in variables enabled
├── [] All event tags created
├── [] Triggers correctly configured
└── [] User properties set (if needed)

[] TESTING
├── [] GTM Preview mode tested
├── [] DebugView events verified
├── [] Parameter values correct
├── [] No duplicate events
├── [] Consent Mode v2 working correctly (EEA: analytics_storage + ad_storage signals)
└── [] Cross-browser tested

[] GA4 CONFIGURATION
├── [] Custom dimensions registered
├── [] Custom metrics registered (if needed)
├── [] Key events marked (GA4 UI term since March 2024; still "Conversions" in Google Ads)
└── [] Realtime reports show events

[] DOCUMENTATION
├── [] Event tracking sheet updated
├── [] GTM container documented
└── [] Stakeholders informed
```

## Output: Event Tracking Implementation Template

```markdown
# Event Tracking Implementation Plan

## Overview
- **Website:** [URL]
- **GTM Container:** GTM-XXXXXXX
- **GA4 Property:** G-XXXXXXXXXX
- **Implementation date:** [Date]

## Events Implemented

### Lead Generation Events
| Event Name | Trigger | Parameters | Status |
|------------|---------|------------|--------|
| generate_lead | Form submit | form_name, form_location | ✅ Live |
| phone_click | Tel: link click | phone_number | ✅ Live |
| email_click | Mailto: link click | - | ✅ Live |

### Engagement Events
| Event Name | Trigger | Parameters | Status |
|------------|---------|------------|--------|
| cta_click | Button click | click_text, click_location | ✅ Live |
| video_start | Video play | video_title, video_provider | ✅ Live |
| scroll_depth | 25/50/75/90% | scroll_percent | ✅ Live |

### E-commerce Events
| Event Name | Trigger | Parameters | Status |
|------------|---------|------------|--------|
| view_item | Product view | item_id, item_name, price | Pending |
| add_to_cart | Add to cart | item_id, quantity, value | Pending |
| purchase | Order complete | transaction_id, value, items | Pending |

## Custom Dimensions Registered
| Dimension Name | Scope | Event Parameter |
|----------------|-------|-----------------|
| Form Name | Event | form_name |
| CTA Location | Event | cta_location |
| Customer Type | User | customer_type |

## Testing Results
- [ ] GTM Preview: All tags firing correctly
- [ ] DebugView: Events appearing with correct parameters
- [ ] Realtime: Events counting properly
- [ ] Cross-browser: Chrome, Safari, Firefox verified

## Notes
[Any points of attention or follow-up items]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, verify events are actually firing in production:

```python
# Confirm events are being received and count correctly
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="7daysAgo",
    end_date="today",
    metrics=["eventCount"],
    dimensions=["eventName"]
)
```

Compare the returned event list against the events in the tracking plan above. Missing events = not yet firing. Low counts relative to sessions = potential mis-trigger conditions (wrong page, wrong element, consent block).
