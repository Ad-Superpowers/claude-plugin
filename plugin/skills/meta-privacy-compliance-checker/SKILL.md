---
name: meta-privacy-compliance-checker
description: "This skill should be used when the user asks to \"check privacy compliance\", \"validate GDPR setup\", \"implement cookieless tracking\", or mentions \"Meta privacy compliance\", \"iOS 14 tracking setup\", or \"consent management for ads\". Do NOT use for: CAPI implementation details (use capi-implementation-guide), EMQ optimization (use emq-optimizer), attribution window decisions (use attribution-window-advisor)."
---
# Privacy Compliance Checker

## Overview

This skill helps check and implement privacy-compliant Meta Ads setups, including GDPR compliance, iOS 14+ adjustments, consent management, and cookieless tracking strategies.

## Privacy Landscape 2025-2026

### Key Privacy Developments

```
┌─────────────────────────────────────────────────────────────────┐
│  PRIVACY TIMELINE                                               │
│                                                                 │
│  2021: iOS 14 ATT - App Tracking Transparency                   │
│  2022: Meta Conversions API mainstream                          │
│  2023: Google delays 3rd party cookie deprecation               │
│  2024: DSA (Digital Services Act) enforcement EU                │
│  2025: Chrome 3rd party cookie phase-out begins                 │
│  Jan 2026: Meta removes 7d_view and 28d_view attribution        │
│  2026: Fully cookieless advertising era / Andromeda engine      │
│                                                                 │
│  IMPACT ON META ADS:                                            │
│  ├── Signal loss: ~50% less tracking data                       │
│  ├── Attribution gaps: Conversions harder to measure            │
│  ├── Audience shrinkage: Retargeting pools smaller              │
│  └── Modeling: More reliant on AI/statistical modeling          │
└─────────────────────────────────────────────────────────────────┘
```

## GDPR Compliance Checklist

### Data Collection & Consent

```
GDPR COMPLIANCE CHECKLIST
=========================

□ LEGAL BASIS FOR TRACKING
├── Consent mechanism on website?
├── Cookie banner compliant (not pre-checked)?
├── Clear opt-in for marketing cookies?
├── Rejection possible without disadvantages?
└── Status: [OK / Fix needed]

□ PRIVACY POLICY
├── Meta/Facebook pixel mentioned?
├── Purpose of data collection explained?
├── Third-party sharing disclosed?
├── Retention periods stated?
└── Status: [OK / Fix needed]

□ DATA SUBJECT RIGHTS
├── Right of access facilitated?
├── Right to deletion possible?
├── Right to object respected?
├── Contact for privacy questions?
└── Status: [OK / Fix needed]

□ COOKIE CONSENT MANAGEMENT
├── CMP (Consent Management Platform) active?
├── Pixel fires only AFTER consent?
├── Consent signal sent to Meta?
├── Audit trail of consent?
└── Status: [OK / Fix needed]
```

### Consent Mode Implementation

```
CONSENT-BASED TRACKING SETUP
============================

OPTION 1: Meta Pixel with Consent Mode

// Only load pixel after consent
if (userHasConsented()) {
  // Load Facebook Pixel
  fbq('init', 'YOUR_PIXEL_ID');
  fbq('track', 'PageView');
} else {
  // Don't load pixel - no tracking
}

OPTION 2: Meta with Google Consent Mode v2

// Consent Mode v2 integration
gtag('consent', 'default', {
  'analytics_storage': 'denied',
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied'
});

// After consent update:
gtag('consent', 'update', {
  'analytics_storage': 'granted',
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted'
});
```

## ATT & Signal Loss (Baseline Since 2021)

### Current State

```
ATT IMPACT (standard operating conditions since iOS 14.5)
=========================================================

ATTRIBUTION CHANGES (updated Jan 2026):
├── Default attribution window: 7d click + 1d view
├── 7d view attribution: REMOVED (was available, now gone)
├── 28d view attribution: REMOVED
├── 28d click attribution: REMOVED
├── IMPORTANT: Historical data using old windows cannot be
│   compared with data from Jan 2026 onwards
├── Real-time reporting: Delayed (up to 72 hours)
└── Breakdown: Less granular

OPT-IN RATES (average):
├── Worldwide: ~25-35% opt-in
├── EU: ~20-30% opt-in
├── US: ~30-40% opt-in
└── App vs Web: Apps harder hit

SIGNAL RECOVERY STRATEGIES:
├── Conversions API implementation
├── Aggregated Event Measurement (AEM)
├── Value optimization (for high-value events)
└── Modeling (Meta's AI for gaps)
```

### Aggregated Event Measurement (AEM)

```
AEM SETUP CHECKLIST
===================

□ DOMAIN VERIFICATION
├── Domain verified in Business Settings?
├── DNS TXT record correct?
└── Status: [OK / Fix needed]

□ EVENT PRIORITIZATION (Max 8 events)
├── Top 8 events selected?
├── Priority order determined?
├── Highest priority = most important conversion?
└── Status: [OK / Fix needed]

RECOMMENDED PRIORITIZATION (E-commerce):
1. Purchase (highest)
2. InitiateCheckout
3. AddToCart
4. AddPaymentInfo
5. ViewContent
6. Lead
7. CompleteRegistration
8. PageView (lowest)

□ VALUE OPTIMIZATION
├── Value enabled for Purchase event?
├── Value ranges configured (4 buckets)?
└── Status: [OK / Fix needed]
```

## Conversions API Compliance

### CAPI Privacy Best Practices

```
CAPI PRIVACY SETUP
==================

□ DATA MINIMIZATION
├── Only send necessary parameters
├── No unnecessary PII
├── Hash all identifiable data
└── Document which data you send

□ HASHING REQUIREMENTS
├── Email: SHA256, lowercase, trimmed
├── Phone: SHA256, E.164 format
├── Names: SHA256, lowercase
├── Use Meta's hashing libraries
└── Status: [OK / Fix needed]

□ CONSENT FORWARDING
├── Send consent status with CAPI
├── Use opt_out parameter
├── Respect user preferences
└── Status: [OK / Fix needed]

□ DATA PROCESSING AGREEMENT
├── DPA with Meta signed?
├── DPA with CAPI partner (if applicable)?
└── Status: [OK / Fix needed]

CAPI EVENT EXAMPLE (Privacy-compliant):

{
  "event_name": "Purchase",
  "event_time": 1704067200,
  "user_data": {
    "em": ["SHA256_HASH_EMAIL"],
    "ph": ["SHA256_HASH_PHONE"],
    "fbc": "fb.1.1234567890.AbCdEf",
    "fbp": "fb.1.1234567890.1234567890",
    "client_ip_address": "123.45.67.89",
    "client_user_agent": "Mozilla/5.0..."
  },
  "custom_data": {
    "currency": "USD",
    "value": 99.00
  },
  "opt_out": false,
  "data_processing_options": [],
  "data_processing_options_country": 0,
  "data_processing_options_state": 0
}
```

## Cookieless Future Preparation

### First-Party Data Strategy

```
FIRST-PARTY DATA PRIORITIES
============================

1. EMAIL COLLECTION
├── Incentivize newsletter signups
├── Promote account creation
├── Post-purchase email capture
└── Use: Custom Audiences, Value-based LAL

2. PHONE NUMBER
├── SMS marketing opt-in
├── Checkout phone field
└── Use: High-match custom audiences

3. ZERO-PARTY DATA
├── Preference surveys
├── Quiz/configurator data
├── Explicit stated interests
└── Use: Segmentation, personalization

4. SERVER-SIDE TRACKING
├── CAPI implementation
├── Server-side GTM
├── Hybrid pixel + CAPI
└── Use: Signal recovery, accuracy

FIRST-PARTY DATA COLLECTION FRAMEWORK:

Touchpoint          │ Data to Collect        │ Consent
────────────────────┼────────────────────────┼──────────
Newsletter popup    │ Email, name            │ Explicit
Account creation    │ Email, phone, address  │ Explicit
Purchase            │ Full contact + purchase│ Implicit*
Quiz/Survey         │ Preferences, interests │ Explicit
Loyalty program     │ Purchase history       │ Explicit

*Check local regulations for legitimate interest
```

### Audience Building Without Cookies

```
COOKIELESS AUDIENCE STRATEGIES
===============================

1. CUSTOMER LIST UPLOADS
├── Upload hashed email/phone lists
├── Match rate: 50-70% typical
├── Refresh regularly (monthly)
└── Use for: Retargeting, Exclusions, LAL seed

2. ENGAGEMENT-BASED AUDIENCES
├── Video viewers (platform-native)
├── Page/Profile engagers
├── Ad engagers
├── Form engagers (Lead Ads)
└── No cookies needed - Meta platform data

3. WEBSITE CUSTOM AUDIENCES (with consent)
├── Implement with consent-first approach
├── Combine pixel + CAPI for accuracy
├── Shorter windows (consent decay)
└── Supplement with engagement audiences

4. BROAD TARGETING + AI
├── Let Meta's algorithm work
├── Advantage+ audiences
├── Less specific = more scale
└── Trust machine learning

RECOMMENDED AUDIENCE MIX 2025+:
├── 40% - First-party data (uploads, engagement)
├── 30% - Broad/Advantage+ (AI-optimized)
├── 20% - Website audiences (consent-based)
└── 10% - Interest targeting (declining utility)
```

## Compliance Audit Template

### Full Privacy Audit Checklist

```
PRIVACY COMPLIANCE AUDIT
========================

Audit Date: [DATE]
Account: [ACCOUNT]
Region: [EU/US/Other]

SECTION 1: WEBSITE COMPLIANCE
────────────────────────────
□ Cookie banner present
□ Opt-in (not pre-checked)
□ Easy reject option
□ Privacy policy link
□ Cookie policy detailed
Score: ___/5

SECTION 2: PIXEL IMPLEMENTATION
──────────────────────────────
□ Pixel loads after consent
□ Consent signal correct
□ No pre-consent tracking
□ Deduplication with CAPI
Score: ___/4

SECTION 3: CAPI COMPLIANCE
─────────────────────────
□ Data hashing correct
□ Minimal data principle
□ Consent forwarding
□ DPA in place
Score: ___/4

SECTION 4: iOS 14+ SETUP & ATTRIBUTION
──────────────────────────────────────
□ Domain verified
□ AEM configured
□ Event prioritization
□ Value optimization
□ Attribution window updated to 7d_click + 1d_view (28d/7d view removed Jan 2026)
□ Historical reports using old windows flagged/replaced
Score: ___/6

SECTION 5: AUDIENCE COMPLIANCE
─────────────────────────────
□ Consent for custom audiences
□ Customer list compliance
□ Retention policies
□ Data deletion process
Score: ___/4

TOTAL SCORE: ___/21

INTERPRETATION:
├── 19-21: Excellent compliance
├── 15-18: Good, minor fixes needed
├── 10-14: Fair, significant gaps
└── <10:   Poor, urgent action needed

ACTION ITEMS:
1. [Item]
2. [Item]
3. [Item]
```

## MCP Tool Integration

### Checking Signal Quality with Live Data

```
1. Verify CAPI event volumes and EMQ:
→ meta_get_insights(account_id="...", fields=["action_values","actions","cost_per_action_type"], date_preset="last_7d", level="account")

2. Check for attribution window configuration issues:
→ meta_get_insights(account_id="...", fields=["spend","purchase_roas","cost_per_action_type"], date_preset="last_7d", level="campaign")
   Note: Confirm results align with 7d_click + 1d_view default.
   Any reports showing anomalies vs history may reflect the Jan 2026 attribution change.
```

## Example Interaction

**User**: "I want to make sure my Meta Ads setup is GDPR-compliant. What should I check?"

**Claude response**:

"I'll help you with a GDPR compliance check for your Meta Ads. Here are the key points:

---

**QUICK GDPR CHECK (5 minutes):**

**1. Cookie Consent Banner:**
- [ ] Banner appears for ALL cookies?
- [ ] Reject button as prominent as Accept?
- [ ] No pre-checked boxes?
- [ ] Pixel does NOT load before consent?

**2. Privacy Policy:**
- [ ] Meta/Facebook pixel mentioned?
- [ ] Purpose of tracking explained?
- [ ] Contact for privacy requests?

**3. Technical Implementation:**
- [ ] Pixel conditional on consent?
- [ ] CAPI sends consent signal?

---

**TEST YOUR SETUP:**

1. **Open your website in incognito**
2. **Open browser DevTools → Network tab**
3. **Filter on 'facebook'**
4. **BEFORE you give consent:**
   - Do you see facebook requests? → Not compliant
   - No requests? → Good
5. **AFTER consent:**
   - Do you see pixel fire? → Correct

---

**RED FLAGS:**

- Cookie banner with only 'Accept' button
- Pre-checked consent boxes
- Pixel loads before consent
- No privacy policy
- No data deletion process

---

**RECOMMENDED TOOLS:**

- **CMP**: Cookiebot, OneTrust, Usercentrics
- **Testing**: Facebook Pixel Helper, Ghostery

Would you like me to dive deeper into a specific area?"
