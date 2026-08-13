---
name: google-ads-enhanced-conversions-setup
description: "This skill should be used when the user asks to \"implement Enhanced Conversions\", \"set up server-side tagging\", \"configure Consent Mode V2\", \"hash customer data\", or mentions \"first-party data integration\", \"GDPR compliance for Google Ads\", or \"Enhanced Conversions for leads\". Do NOT use for: general conversion tracking setup (use conversion-tracking-setup), conversion tracking debugging (use conversion-tracking-debugger), GA4 integration (use ga4-integration-guide)."
---
# Enhanced Conversions Setup

Complete guide for implementing Enhanced Conversions for better conversion attribution in a privacy-first world with first-party data and consent management.



## GAQL: Check Enhanced Conversion Status

Use `google_ads_run_gaql` to verify conversion actions and enhanced conversion setup:

```sql
SELECT conversion_action.name, conversion_action.status,
    conversion_action.type, conversion_action.category,
    conversion_action.attribution_model_settings.attribution_model,
    conversion_action.tag_snippets
FROM conversion_action
WHERE conversion_action.status = 'ENABLED'
ORDER BY conversion_action.name
```

```sql
-- Check conversion volume (to see if EC is capturing data)
SELECT conversion_action.name, metrics.conversions,
    metrics.all_conversions, metrics.all_conversions_value
FROM conversion_action
WHERE segments.date DURING LAST_30_DAYS
AND conversion_action.status = 'ENABLED'
ORDER BY metrics.all_conversions DESC
```

## Enhanced Conversions Overview

### What Are Enhanced Conversions?

```
ENHANCED CONVERSIONS FUNDAMENTALS
═════════════════════════════════

TRADITIONAL CONVERSION TRACKING:
────────────────────────────────
User clicks ad → Cookie stored → Converts → Cookie matched
├── Problem 1: Cookie blocking (ITP, browsers)
├── Problem 2: Cross-device gaps
├── Problem 3: Privacy regulations
└── Result: ~40-60% conversion loss

ENHANCED CONVERSIONS:
─────────────────────
User clicks ad → Cookie stored → Converts → First-party data hashed & sent
├── Email (SHA256 hashed)
├── Phone (SHA256 hashed)
├── Name + Address (SHA256 hashed)
└── Google matches with signed-in users

┌─────────────────────────────────────────────────────────────────┐
│  ENHANCED CONVERSIONS FLOW                                      │
│                                                                 │
│  1. User clicks ad                                              │
│     └─► GCLID stored in cookie                                 │
│                                                                 │
│  2. User converts (fills form/buys)                             │
│     └─► First-party data collected (email, phone, etc.)        │
│                                                                 │
│  3. Data hashed on client/server                                │
│     └─► SHA256 one-way hash (irreversible)                     │
│                                                                 │
│  4. Hashed data sent to Google                                  │
│     └─► Matched with Google account data                       │
│                                                                 │
│  5. Conversion attributed                                       │
│     └─► Even without cookies!                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Privacy & Compliance

```
PRIVACY COMPLIANCE CHECKLIST
════════════════════════════

GDPR REQUIREMENTS:
──────────────────
□ Consent obtained BEFORE data collection
□ Privacy policy describes data usage
□ Data minimization (only necessary data)
□ User has opt-out option
□ Data not shared with third parties (only hashed)

CONSENT MODE V2 (REQUIRED EU - March 2024):
───────────────────────────────────────────
□ ad_storage consent
□ ad_user_data consent (NEW)
□ ad_personalization consent (NEW)
□ analytics_storage consent

IMPLEMENTATION:
──────────────
Consent = GRANTED:
├── Full tracking enabled
├── First-party data can be collected
└── Enhanced conversions active

Consent = DENIED:
├── Cookieless pings (for modeling)
├── No first-party data sent
└── Conversion modeling is used
```

## Enhanced Conversions for Web

### Setup via Google Tag (Automatic)

```
ENHANCED CONVERSIONS FOR WEB - AUTO SETUP
═════════════════════════════════════════

WHEN: E-commerce or forms with standard fields

STEP 1: ENABLE IN GOOGLE ADS
─────────────────────────────
1. Tools & Settings → Conversions
2. Click on your purchase/lead conversion
3. "Enhanced conversions" section → Turn on
4. Choose: "Google tag"
5. Select: "Automatic collection"

STEP 2: VERIFY DATA COLLECTION
───────────────────────────────
Google Tag automatically looks for:
├── Email fields (input type="email")
├── Phone fields (input type="tel")
├── Name fields (autocomplete="name")
└── Address fields (autocomplete="address-line1")

STEP 3: TEST
────────────
1. Tag Assistant (legacy) or Preview mode
2. Perform a test conversion
3. Check if "user_data" parameter is present
4. Google Ads → Conversions → Check enhanced conv. status

WARNING — AUTOMATIC DOES NOT ALWAYS WORK:
├── Custom form frameworks (React, Vue forms)
├── Non-standard field names
├── Forms in iframes
└── → Use Manual setup instead
```

### Setup via GTM (Manual)

```
ENHANCED CONVERSIONS VIA GTM - MANUAL SETUP
════════════════════════════════════════════

STEP 1: DATA LAYER SETUP
─────────────────────────
Add to your form success page or event:

<script>
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  'event': 'conversion',
  'enhanced_conversion_data': {
    'email': 'user@example.com',           // Plain text, will be hashed
    'phone_number': '+31612345678',         // E.164 format
    'first_name': 'John',
    'last_name': 'Smith',
    'home_address': {
      'street': 'Main Street 1',
      'city': 'Amsterdam',
      'region': 'North Holland',
      'postal_code': '1012LG',
      'country': 'NL'
    }
  }
});
</script>

NOTE: Send plain text, GTM/Google hashes automatically

STEP 2: GTM VARIABLES
──────────────────────
Create Data Layer Variables:

Variable 1: dlv_email
├── Variable Type: Data Layer Variable
└── Data Layer Variable Name: enhanced_conversion_data.email

Variable 2: dlv_phone
├── Variable Type: Data Layer Variable
└── Data Layer Variable Name: enhanced_conversion_data.phone_number

(Repeat for other fields)

STEP 3: USER-PROVIDED DATA VARIABLE
────────────────────────────────────
1. Variables → New → User-Provided Data
2. Fill in:
   ├── Email: {{dlv_email}}
   ├── Phone: {{dlv_phone}}
   ├── First Name: {{dlv_first_name}}
   └── etc.

STEP 4: CONVERSION TAG UPDATE
──────────────────────────────
1. Open your Google Ads Conversion Tag
2. Include user-provided data: Yes
3. User-provided data variable: {{User-Provided Data}}
4. Save

STEP 5: TEST & VERIFY
──────────────────────
1. GTM Preview mode
2. Perform a conversion
3. Check tag → "user_data" parameter present
4. Google Ads diagnostics after 48-72 hours
```

### Data Formatting Requirements

```
DATA FORMATTING FOR ENHANCED CONVERSIONS
═════════════════════════════════════════

EMAIL:
──────
□ Lowercase
□ No leading/trailing spaces
□ Do not expand aliases (user+alias@example.com = user@example.com; the same rule applies to Gmail plus-aliases)

Example: "John.Doe@Example.com" → "john.doe@example.com"

PHONE:
──────
□ E.164 format (country code + number)
□ No spaces, dashes, parentheses

Examples:
├── Netherlands: +31612345678
├── Belgium: +32471234567
└── Germany: +491521234567

NAME:
─────
□ Only first name OR last name per field
□ No titles (Dr., Mr., etc.)
□ Lowercase (Google normalizes)

ADDRESS:
────────
□ Street: street name and number only
□ City: full city name
□ Postal code: without spaces
□ Country: ISO 3166-1 alpha-2 (NL, BE, DE)

┌────────────────────────────────────────────────────────────────┐
│ DATA QUALITY IMPACT ON MATCH RATE                              │
│                                                                │
│ Data point          │ Impact on match rate                     │
│────────────────────┼────────────────────────────────────────│
│ Email only          │ 40-60% match rate                        │
│ Email + Phone       │ 60-75% match rate                        │
│ Email + Name        │ 55-70% match rate                        │
│ All fields          │ 70-85% match rate                        │
└────────────────────────────────────────────────────────────────┘
```

## Enhanced Conversions for Leads

### Implementation Flow

```
ENHANCED CONVERSIONS FOR LEADS
══════════════════════════════

USE CASE:
─────────
Lead is qualified/converted offline
E.g.: Form submit → Sales call → Close deal

FLOW:
─────
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  1. User clicks ad               2. User submits form          │
│     └─► GCLID captured              └─► Lead data + GCLID saved│
│                                                                 │
│  3. Enhanced conv captures       4. Lead qualifies (offline)    │
│     └─► Email hashed & sent         └─► In CRM: status updated │
│                                                                 │
│  5. Upload offline conversion    6. Attribution complete        │
│     └─► Via API, GCLID match        └─► Google Ads sees close  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

STEP 1: CAPTURE GCLID
──────────────────────
JavaScript to capture GCLID:

<script>
function getGclid() {
  var params = new URLSearchParams(window.location.search);
  var gclid = params.get('gclid');
  if (gclid) {
    // Store in cookie (30 days)
    var d = new Date();
    d.setTime(d.getTime() + 30*24*60*60*1000);
    document.cookie = "gclid=" + gclid + ";expires=" + d.toUTCString() + ";path=/";

    // Store in hidden form field
    var gclidField = document.getElementById('gclid');
    if (gclidField) gclidField.value = gclid;
  }
}
window.onload = getGclid;
</script>

STEP 2: STORE IN CRM
─────────────────────
On form submit, save:
├── Lead data (email, phone, name)
├── GCLID (if present)
├── Timestamp of conversion
└── UTM parameters

STEP 3: ENABLE IN GOOGLE ADS
─────────────────────────────
1. Conversions → [Lead Conversion] → Edit
2. Enhanced conversions for leads: ON
3. Choose method: Google tag or API

STEP 4: OFFLINE CONVERSION IMPORT
──────────────────────────────────
When lead converts (sale):
1. Export from CRM: email + GCLID + conversion time + value
2. Upload via Google Ads UI or API
3. Google matches with enhanced conversion data
```

### Offline Conversion Import

```
OFFLINE CONVERSION IMPORT SETUP
═══════════════════════════════

OPTION 1: MANUAL UPLOAD (UI)
─────────────────────────────
1. Tools → Conversions → Uploads
2. Download template
3. Fill in:
   ├── Google Click ID (GCLID)
   ├── Conversion Name (exact match)
   ├── Conversion Time (timezone aware)
   └── Conversion Value

4. Upload CSV
5. Monitor status

CSV FORMAT:
───────────
Google Click ID,Conversion Name,Conversion Time,Conversion Value
EAIaIQobChMI...,Lead Qualified,2025-01-15 14:30:00+01:00,500

OPTION 2: GOOGLE ADS API
─────────────────────────
For automatic sync from CRM:

// Python example (Google Ads API)
from google.ads.googleads.client import GoogleAdsClient

def upload_offline_conversion(client, customer_id, gclid, conversion_action_id, conversion_datetime, conversion_value):
    conversion_upload_service = client.get_service("ConversionUploadService")

    click_conversion = client.get_type("ClickConversion")
    click_conversion.gclid = gclid
    click_conversion.conversion_action = f"customers/{customer_id}/conversionActions/{conversion_action_id}"
    click_conversion.conversion_date_time = conversion_datetime
    click_conversion.conversion_value = conversion_value
    click_conversion.currency_code = "EUR"

    request = client.get_type("UploadClickConversionsRequest")
    request.customer_id = customer_id
    request.conversions = [click_conversion]
    request.partial_failure = True

    response = conversion_upload_service.upload_click_conversions(request=request)
    return response

OPTION 3: ENHANCED CONVERSIONS FOR LEADS (Without GCLID)
─────────────────────────────────────────────────────────
If GCLID is not available:

1. On form submit: send email (hashed) to Google
2. On offline sale: upload with same email (hashed)
3. Google matches based on hashed email

// CSV with enhanced matching
Email,Conversion Name,Conversion Time,Conversion Value
8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92,Lead Qualified,2025-01-15,500

WARNING: Email must be SHA256 hashed
```

## Consent Mode V2 Implementation

### Consent Mode Setup

```
CONSENT MODE V2 IMPLEMENTATION
═══════════════════════════════

WHY REQUIRED (EU, March 2024):
──────────────────────────────
□ Google requires consent signals for personalization
□ Remarketing audiences do not work without consent
□ Enhanced conversions require ad_user_data consent
□ Measurement can continue with conversion modeling

CONSENT TYPES:
──────────────
ad_storage         - Advertising cookies
analytics_storage  - Analytics cookies
ad_user_data      - First-party data for ads (NEW)
ad_personalization - Personalized ads (NEW)

IMPLEMENTATION VIA GTM:
───────────────────────

1. DEFAULT CONSENT STATE
─────────────────────────
In GTM: Tags → Consent Initialization - All Pages

<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

// Default: denied (EU users)
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'wait_for_update': 500  // Wait for CMP
});

// Region-specific defaults
gtag('consent', 'default', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted',
  'region': ['US', 'CA']  // Non-EU = granted
});
</script>

2. CONSENT UPDATE (After CMP interaction)
──────────────────────────────────────────
Your CMP (Cookiebot, OneTrust, etc.) must trigger:

<script>
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted'
});
</script>

3. GTM CONSENT MODE SETTINGS
─────────────────────────────
1. Admin → Container Settings
2. Enable consent overview
3. Per tag: configure consent requirements
4. Google tags: Require ad_storage, ad_user_data

CONSENT MODE BEHAVIOR:
──────────────────────
┌─────────────────────┬─────────────────────────────────────────┐
│ Consent State       │ Behavior                                │
├─────────────────────┼─────────────────────────────────────────┤
│ ad_storage: denied  │ No advertising cookies                  │
│ ad_user_data: denied│ No first-party data sent to Google     │
│ analytics: denied   │ No analytics cookies                    │
│                     │                                         │
│ ALL denied          │ Cookieless pings (for modeling)         │
│                     │ Conversion modeling active              │
│                     │ Enhanced conversions: NOT active        │
├─────────────────────┼─────────────────────────────────────────┤
│ ALL granted         │ Full tracking                           │
│                     │ Enhanced conversions: ACTIVE            │
│                     │ Remarketing: ACTIVE                     │
└─────────────────────┴─────────────────────────────────────────┘
```

### CMP Integration

```
CMP (CONSENT MANAGEMENT PLATFORM) SETUP
════════════════════════════════════════

POPULAR CMPs WITH NATIVE GTM INTEGRATION:
─────────────────────────────────────────
□ Cookiebot
□ OneTrust
□ Usercentrics
□ Cookie Information
□ Complianz (WordPress)

COOKIEBOT EXAMPLE:
──────────────────

1. Create Cookiebot account
2. Configure cookie categories:
   ├── Necessary: always enabled
   ├── Preference: analytics_storage
   ├── Statistics: analytics_storage
   └── Marketing: ad_storage, ad_user_data, ad_personalization

3. GTM Setup:
   └── Cookiebot offers a template in GTM Gallery

4. Mapping Cookiebot → Consent Mode:
   ├── marketing=true → ad_storage: granted
   ├── marketing=true → ad_user_data: granted
   ├── marketing=true → ad_personalization: granted
   └── statistics=true → analytics_storage: granted

GTM TRIGGER FOR CONSENT UPDATE:
───────────────────────────────
Trigger Type: Custom Event
Event Name: cookie_consent_update

OR via Cookiebot listener:
window.addEventListener('CookiebotOnAccept', function() {
  if (Cookiebot.consent.marketing) {
    gtag('consent', 'update', {
      'ad_storage': 'granted',
      'ad_user_data': 'granted',
      'ad_personalization': 'granted'
    });
  }
});
```

## Server-Side Tagging

### GTM Server Container Setup

```
SERVER-SIDE TAGGING SETUP
═════════════════════════

ADVANTAGES:
───────────
□ First-party context (your own domain)
□ More control over data sent to vendors
□ Better against ad blockers
□ Lower page load impact
□ GDPR compliance (data stays in EU)

HOSTING OPTIONS:
────────────────
1. Google Cloud Run (recommended)
   ├── Auto-scaling
   ├── Pay-per-use
   └── ~$50-200/month for medium traffic

2. Manual deployment (AWS, Azure)
   └── More control, more work

SETUP STEPS:
────────────

1. CREATE GTM SERVER CONTAINER
──────────────────────────────
1. tagmanager.google.com
2. Create Container → Server
3. Choose: Manually provision

2. CLOUD RUN DEPLOYMENT
───────────────────────
1. Cloud Run → Create Service
2. Container image: gcr.io/cloud-tagging-public/gtm-cloud-image:stable
3. Environment variables:
   ├── CONTAINER_CONFIG: [from GTM]
   ├── PORT: 8080
4. Allow unauthenticated invocations
5. Set region (EU for GDPR)

3. CUSTOM DOMAIN SETUP
──────────────────────
□ Subdomain of your site: data.yoursite.com
□ DNS: CNAME to Cloud Run URL
□ SSL: automatic via Google

4. ADJUST CLIENT-SIDE GTM
──────────────────────────
Google tag configuration:
├── server_container_url: https://data.yoursite.com
└── First-party mode: enabled

5. CONFIGURE SERVER-SIDE TAGS
─────────────────────────────
In Server Container:
├── GA4 Client (receives hits)
├── Google Ads Conversion Tracking tag
├── Enhanced Conversions tag
└── Consent Mode settings

ARCHITECTURE:
─────────────
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Browser                Server Container          Third Parties │
│  ───────               ─────────────────         ───────────── │
│                                                                 │
│  GTM Web Container ──────► Server Container ──────► Google Ads  │
│  (sends to your domain)   (data.yoursite.com)     (via API)    │
│                                                                 │
│  ADVANTAGE: First request is first-party (your domain)         │
│  Ad blockers do not block it                                   │
│  You control which data passes through                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Server-Side Enhanced Conversions

```
ENHANCED CONVERSIONS VIA SERVER-SIDE
════════════════════════════════════

SETUP IN SERVER CONTAINER:

1. GA4 CLIENT
─────────────
□ Client receives all hits from web container
□ Parses user_data from requests

2. GOOGLE ADS CONVERSION TAG (Server)
─────────────────────────────────────
Tag Type: Google Ads Conversion Tracking

Settings:
├── Conversion ID: [from Google Ads]
├── Conversion Label: [from Google Ads]
├── Use Data Layer: enhanced_conversion_data
└── Hash user data: enabled (if plain text)

3. STAG ENHANCED CONVERSIONS TAG
────────────────────────────────
Dedicated tag for enhanced conversions:

Tag Type: Google Ads: User-Provided Data

Settings:
├── Email: {{user_data.email}}
├── Phone: {{user_data.phone}}
├── First Name: {{user_data.first_name}}
├── Last Name: {{user_data.last_name}}
├── Street: {{user_data.address.street}}
├── City: {{user_data.address.city}}
├── Postal Code: {{user_data.address.postal_code}}
├── Country: {{user_data.address.country}}
└── Hash data: enabled

TRIGGER:
────────
Event Name: purchase, form_submit, etc.
Condition: user_data present
```





## Output: Enhanced Conversions Implementation Plan

```markdown
# Enhanced Conversions Implementation Plan

## Current Status
- **Enhanced Conversions status:** [Not enabled / Enabled - Web / Enabled - Leads]
- **Consent Mode V2:** [Not implemented / Implemented]
- **Server-side tagging:** [No / Yes]
- **Current conversion tracking:** [Client-side only / Mixed]

## Implementation Checklist

### Phase 1: Consent Mode V2 (Week 1)
- [ ] CMP chosen/configured
- [ ] Default consent state set (denied for EU)
- [ ] Consent update triggers working
- [ ] GTM tags configured with consent requirements
- [ ] Testing: consent flows work correctly

### Phase 2: Enhanced Conversions for Web (Week 2)
- [ ] Conversion action enhanced conversions enabled
- [ ] Data layer setup for form data
- [ ] GTM User-Provided Data variable created
- [ ] Google Ads Conversion tag updated
- [ ] Testing: user_data visible in tag assistant

### Phase 3: Enhanced Conversions for Leads (Week 3)
- [ ] GCLID capture script implemented
- [ ] CRM fields added (GCLID storage)
- [ ] Offline conversion import process set up
- [ ] API integration or manual upload workflow
- [ ] Testing: offline conversions match

### Phase 4: Server-Side Tagging (Optional, Week 4+)
- [ ] Server container deployed (Cloud Run)
- [ ] Custom domain configured
- [ ] Clients and tags migrated
- [ ] Testing: server-side conversions work

## Data Requirements

### Fields to Capture:
| Field | Format | Required |
|-------|--------|----------|
| Email | lowercase, trimmed | Yes |
| Phone | E.164 (+31612345678) | Recommended |
| First Name | lowercase | Recommended |
| Last Name | lowercase | Recommended |
| Street | street + number | Optional |
| City | full name | Optional |
| Postal Code | no spaces | Optional |
| Country | ISO alpha-2 | Optional |

## Success Metrics
- [ ] Enhanced conversions match rate: Target 40%+
- [ ] Consent rate: Track % granted vs denied
- [ ] Conversion delta: Compare before/after EC implementation
- [ ] Attribution improvement: Measured vs modeled conversions
```
