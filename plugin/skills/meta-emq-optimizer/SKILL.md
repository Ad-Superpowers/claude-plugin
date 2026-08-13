---
name: meta-emq-optimizer
description: "This skill should be used when the user asks to \"improve EMQ score\", \"optimize event match quality\", \"configure Advanced Matching\", or mentions \"EMQ\", \"Customer Information Parameters\", or \"match quality diagnostics\". Do NOT use for: CAPI implementation (use capi-implementation-guide), attribution window configuration (use attribution-window-advisor), pixel installation issues (use performance-troubleshooter)."
---
# EMQ Optimizer

Optimizer for Meta's Event Match Quality (EMQ) score to improve user matching and attribution.

## What Is EMQ?

Event Match Quality measures how well Meta can match conversion events to Facebook/Instagram users.

```
EMQ Score Scale: 0-10

Score Interpretation:
├── 0-3: Poor - Many missed matches
├── 4-5: OK - Basic matching, improvement needed
├── 6-7: Good - Good match rate
├── 8-10: Great - Optimal matching
└── Target: 7+ for Purchase events
```

## Why EMQ Is Crucial

```
Higher EMQ = Better:
├── More accurate attribution
├── Better algorithm optimization
├── Higher reported ROAS
├── Better audience building
└── More effective retargeting

Low EMQ Impact:
├── Missed conversions in reporting
├── Algorithm optimizes on incomplete data
├── Underreported ROAS
├── Weaker lookalike audiences
└── Less effective retargeting
```

## EMQ Check Workflow

```
STEP 1: Check current EMQ
└── Events Manager → Pixel → Event → Details → Match Quality

STEP 2: Identify gaps
└── Which parameters are missing?

STEP 3: Implement improvements
└── Add missing parameters

STEP 4: Monitor results
└── EMQ update takes 24-72 hours
```

## Customer Information Parameters (CIPs)

### Parameter Impact Ranking

| Parameter | Code | Impact | Description |
|-----------|------|--------|-------------|
| **Email** | em | Very High | Most important matcher |
| **Phone** | ph | Very High | Almost as important as email |
| **First Name** | fn | High | Strengthens other matches |
| **Last Name** | ln | High | Strengthens other matches |
| **External ID** | external_id | High | Persistent user identifier |
| **City** | ct | Medium | Location matching |
| **State** | st | Medium | Location matching |
| **Zip Code** | zp | Medium | Location matching |
| **Country** | country | Medium | Location matching |
| **Date of Birth** | db | Medium | Extra identifier |
| **Gender** | ge | Medium | Extra identifier |
| **Client IP** | client_ip_address | Basic | Required for server events |
| **User Agent** | client_user_agent | Basic | Required for server events |
| **Click ID** | fbc | High | Facebook click identifier |
| **Browser ID** | fbp | High | Facebook browser identifier |

### Implementation Priority Order

```
PHASE 1 - Essentials (Expected EMQ: 5-6)
├── Email (em)
├── Client IP Address
├── User Agent
├── fbc (Facebook Click ID - from URL)
└── fbp (Facebook Browser ID - from cookie)

PHASE 2 - High Impact (Expected EMQ: 7-8)
├── Phone Number (ph)
├── First Name (fn)
├── Last Name (ln)
└── External ID (customer ID)

PHASE 3 - Optimization (Expected EMQ: 8-10)
├── City (ct)
├── State (st)
├── Zip Code (zp)
├── Country (country)
├── Date of Birth (db)
└── Gender (ge)
```

## Advanced Matching Setup

### Automatic Advanced Matching (AAM)

```
What it does:
Meta automatically reads form fields and matches data

Setup (2 minutes):
1. Events Manager → Data Sources → Pixel
2. Settings → Advanced Matching
3. Toggle "Automatic Advanced Matching" ON
4. Review detected fields
5. Done

Automatically detects:
├── Email fields
├── Phone fields
├── Name fields
├── Address fields
└── Form submissions
```

### Manual Advanced Matching

**Browser-side (Pixel):**

```javascript
// Init with user data
fbq('init', 'PIXEL_ID', {
  em: 'john@example.com',          // Email (auto-hashed)
  fn: 'john',                       // First name
  ln: 'doe',                        // Last name
  ph: '31612345678',               // Phone (with country code, no +)
  external_id: 'customer_12345',    // Your customer ID
  ge: 'm',                          // Gender: m/f
  db: '19900115',                   // DOB: YYYYMMDD
  ct: 'amsterdam',                  // City (lowercase)
  st: 'nh',                         // State/Province
  zp: '1012',                       // Zip code
  country: 'nl'                     // Country (ISO 2-letter)
});
```

**Server-side (CAPI):**

```json
{
  "user_data": {
    "em": ["ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"],
    "ph": ["ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"],
    "fn": ["ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"],
    "ln": ["ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"],
    "external_id": ["customer_12345"],
    "client_ip_address": "192.168.1.1",
    "client_user_agent": "Mozilla/5.0...",
    "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
    "fbp": "fb.1.1558571054389.1098115397"
  }
}
```

## Hashing Requirements

### Correct Hashing (CAPI)

```
HASHING RULES:
1. Use SHA256
2. Lowercase everything BEFORE hashing
3. Trim whitespace
4. Remove special characters (phone)
5. Hash each parameter separately

EXAMPLE PYTHON:
import hashlib

def hash_parameter(value):
    if not value:
        return None
    # Lowercase, trim, encode
    normalized = str(value).lower().strip()
    # SHA256 hash
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

# Correct:
email = "John.Doe@Example.com"
hashed = hash_parameter(email)  # Hash of "john.doe@example.com"

# Phone normalization:
phone = "+31 6 12345678"
normalized_phone = ''.join(filter(str.isdigit, phone))  # "31612345678"
hashed_phone = hash_parameter(normalized_phone)
```

### Pixel Hashing

```
PIXEL HASHING (Automatic):
- fbq() hashes automatically when raw values are sent
- Pre-hashed values are also accepted

Sending pre-hashed:
fbq('init', 'PIXEL_ID', {
  em: 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
});

Or raw (auto-hashed):
fbq('init', 'PIXEL_ID', {
  em: 'john@example.com'  // Meta hashes this automatically
});
```

## fbc and fbp Parameters

### Facebook Click ID (fbc)

```
What it is:
Tracking parameter Meta adds to URLs after ad click

Where to find:
URL: https://yoursite.com/?fbclid=AbCdEfGhIjKlMnOp...

How to use:
1. Capture fbclid from URL
2. Store in first-party cookie
3. Send as fbc parameter

Format:
fbc = fb.{version}.{creation_time}.{fbclid}
Example: fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz
```

### Facebook Browser ID (fbp)

```
What it is:
First-party cookie that Pixel automatically sets

Where to find:
Cookie: _fbp

How to use:
1. Read _fbp cookie
2. Send with CAPI events

Format:
fbp = fb.{version}.{creation_time}.{random_number}
Example: fb.1.1558571054389.1098115397
```

### Implementation

```javascript
// JavaScript helper
function getFacebookParams() {
  const cookies = document.cookie.split(';');
  let fbp = null;
  let fbc = null;

  cookies.forEach(cookie => {
    const [name, value] = cookie.trim().split('=');
    if (name === '_fbp') fbp = value;
    if (name === '_fbc') fbc = value;
  });

  // If fbc not in cookie, check URL
  if (!fbc) {
    const urlParams = new URLSearchParams(window.location.search);
    const fbclid = urlParams.get('fbclid');
    if (fbclid) {
      fbc = `fb.1.${Date.now()}.${fbclid}`;
    }
  }

  return { fbp, fbc };
}
```

## EMQ Diagnostic Framework

### Score Analysis

```
CURRENT EMQ: [score]

SCORE < 4 (Poor):
├── Check: Is CAPI active?
├── Check: Are basic parameters present? (IP, UA)
├── Check: Is email/phone being sent?
└── Action: Implement Phase 1 parameters

SCORE 4-5 (OK):
├── Check: Missing email OR phone?
├── Check: Are fbc/fbp being sent?
├── Check: Hashing correct?
└── Action: Add missing high-impact params

SCORE 6-7 (Good):
├── Check: All Phase 1+2 parameters present?
├── Check: Advanced Matching enabled?
├── Check: Multiple parameters per event?
└── Action: Add Phase 3 parameters

SCORE 8-10 (Great):
├── Maintain current setup
├── Monitor for degradation
└── Document configuration
```

### Common EMQ Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Email not hashed | EMQ low despite email | Verify hashing (SHA256, lowercase) |
| Phone format wrong | Phone parameter ignored | Remove +, spaces, use digits only |
| fbc/fbp missing | EMQ 1-2 points lower | Capture and send along |
| CAPI only | EMQ mediocre | Enable Pixel + AAM too |
| Parameters null | Events without user data | Check data layer population |

### Troubleshooting Checklist

```
□ Events Manager → Diagnostics → Match Quality
  └── Shows which parameters are being received

□ Test Events tool
  └── Send test event, check parameters

□ Browser Developer Tools
  └── Network tab → Check pixel requests

□ CAPI Response Logging
  └── Log API responses, check errors

□ Parameter Verification
  └── Per event: which params are populated?
```

## MCP: Check Current EMQ and Event Volume

```python
# Cross-check ROAS — low EMQ typically shows as underreported ROAS
meta_get_insights(account_id="act_XXXXX", level="campaign", date_preset="last_7d", fields=["spend","website_purchase_roas","actions"])

# Check pixel health via Events Manager UI (pixel diagnostics are not exposed via meta_query)
# Events Manager → Data Sources → Pixel → Diagnostics → Match Quality tab
# This shows EMQ per event and which Customer Information Parameters are received
```

> **EMQ Minimum Bar:** Meta's own CAPI guidance sets 6.0 as the minimum acceptable EMQ for production campaigns. Below 6.0, algorithm optimization quality degrades measurably. Target 7+ for Purchase events.

## EMQ Improvement Plan Template

```markdown
# EMQ Improvement Plan

## Current State
- EMQ Score: [score]
- Event: [event name]
- Current parameters: [list]

## Gap Analysis
| Parameter | Available? | In Data Layer? | Being Sent? |
|-----------|------------|----------------|-------------|
| Email | [yes/no] | [yes/no] | [yes/no] |
| Phone | [yes/no] | [yes/no] | [yes/no] |
| ... | ... | ... | ... |

## Improvement Actions

### Quick Wins (Week 1)
1. Enable Automatic Advanced Matching
2. Add fbc/fbp to CAPI events
3. [other quick wins]

### Implementation (Week 2-3)
1. Add missing parameters to data layer
2. Update CAPI payload
3. Verify hashing
4. Test deduplication

### Expected Result
- Current EMQ: [X]
- Target EMQ: [Y]
- Timeline: [2-4 weeks]

## Verification
□ Test event with all parameters
□ Events Manager shows parameters
□ EMQ score improved (24-72 hours)
□ Attribution improvement visible
```

## Platform-Specific Tips

### Shopify

```
Native integration:
- AAM automatically enabled with "Maximum" data sharing
- Customer info automatically sent
- Verify in Events Manager

Extra improvement:
- Ensure checkout forms are complete
- Use logged-in customer data
- Check app settings for advanced options
```

### WooCommerce

```
With plugin:
- Enable "Advanced Matching" in plugin settings
- Configure which fields to send
- Check user profile data population

Extra improvement:
- Ensure account creation at checkout
- Capture phone number (often optional)
- Add birthday field if relevant
```

### Custom Implementation

```
Data layer requirements:
- Populate user object on all relevant pages
- Include in checkout/conversion events
- Persist customer ID across sessions

CAPI checklist:
- Hash all PII correctly
- Include fbc/fbp
- Log and verify payload
```
