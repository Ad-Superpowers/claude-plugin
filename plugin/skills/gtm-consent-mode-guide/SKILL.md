---
name: gtm-consent-mode-guide
description: "This skill should be used when the user asks to \"implement Consent Mode v2\", \"integrate a CMP with GTM\", \"recover data lost to cookie consent\", \"set up consent_default and consent_update\", or mentions \"TCF 2.2\", \"behavioral modeling\", or \"Enhanced Conversions for consent\". Do NOT use for: GTM tag/trigger setup (use gtm-conversion-setup-guide), server-side tagging (use gtm-server-side-tagging-guide), or strategic tracking planning (use tracking-plan-builder)."
---

# GTM Consent Mode v2 Guide

Since March 2024, Google requires Consent Mode v2 for any advertiser serving users in the European Economic Area (EEA). Without it, Google Ads, GA4, and other Google products cannot use remarketing or behavioral modeling for those users. This skill covers everything you need to implement consent correctly, integrate a CMP, and recover the data you lose to cookie consent refusals.

## Why Consent Mode v2 Exists

### Regulatory Background

| Regulation | Scope | Key Requirement |
|---|---|---|
| GDPR (2018) | EU/EEA residents | Explicit consent before storing cookies or processing personal data |
| ePrivacy Directive | EU/EEA | Consent before setting non-essential cookies |
| Digital Markets Act (2024) | Large platforms (Google, Meta, etc.) | Platforms must verify consent before using data for ads |
| TDDDG (Germany) | Germany | Stricter interpretation of ePrivacy |
| nFADP (Switzerland) | Switzerland | GDPR-equivalent since Sept 2023 |

### What Changed in v2 (March 2024)

Consent Mode v1 had two consent types: `ad_storage` and `analytics_storage`. v2 adds two more:

| Consent Type | Purpose | Required Since |
|---|---|---|
| `ad_storage` | Cookies for advertising (Google Ads, remarketing) | v1 (2020) |
| `analytics_storage` | Cookies for analytics (GA4, GA) | v1 (2020) |
| `ad_user_data` | **NEW in v2.** Sending user data to Google for advertising | March 2024 |
| `ad_personalization` | **NEW in v2.** Using data for ad personalization/remarketing | March 2024 |

**If you do not implement v2:** Google Ads cannot use remarketing audiences, conversion modeling is disabled, and your campaigns lose optimization signal for EEA users.

## How Consent Mode Works

### The Two-Step Consent Flow

```
Step 1: consent_default (on page load, BEFORE any tags fire)
  |
  Set all consent types to 'denied' for EEA users
  |
  GTM loads tags in RESTRICTED mode:
  - GA4: sends cookieless pings (no user identification)
  - Google Ads: no conversion tracking, no remarketing
  - Meta: pixel does not fire
  |
Step 2: consent_update (when user interacts with consent banner)
  |
  +-- User ACCEPTS all --> Update all to 'granted'
  |   GTM reloads tags in FULL mode
  |   Cookies are set, full tracking resumes
  |
  +-- User ACCEPTS analytics only --> Update analytics_storage to 'granted'
  |   GA4 sets cookies, ads remain restricted
  |
  +-- User REJECTS all --> No update (stays 'denied')
      Cookieless pings continue, no cookies set
```

### consent_default Configuration

This must fire BEFORE any Google tags. Implement via a tag in GTM that fires on "Consent Initialization - All Pages" trigger (built-in trigger type).

```javascript
// gtag consent default (implemented via GTM tag or CMP integration)
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'wait_for_update': 500  // Wait 500ms for CMP to load
});
```

**The `wait_for_update` parameter** tells Google tags to wait up to 500ms for a consent update before firing in restricted mode. This gives your CMP time to check for a returning visitor's stored consent choice.

### consent_update Configuration

This fires when the user makes a consent choice in the CMP banner.

```javascript
// User accepts all cookies
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted'
});
```

```javascript
// User accepts analytics only
gtag('consent', 'update', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'granted'
});
```

### What Each Consent Type Controls

| Consent Type | When Granted | When Denied |
|---|---|---|
| `ad_storage` | Google Ads cookies set (_gcl_aw, _gcl_dc) | No ad cookies. Cookieless pings sent. |
| `analytics_storage` | GA4 cookies set (_ga, _ga_XXXXX) | No analytics cookies. Cookieless pings sent. |
| `ad_user_data` | User data (email, phone) sent to Google for ads | User data NOT sent to Google for ad purposes |
| `ad_personalization` | Remarketing audiences built, personalized ads served | No remarketing, no personalized ads |

### Consent Type Dependencies

```
To use Google Ads remarketing:
  ad_storage = granted AND ad_personalization = granted

To use Enhanced Conversions:
  ad_storage = granted AND ad_user_data = granted

To use GA4 with full user tracking:
  analytics_storage = granted

To use GA4 with behavioral modeling:
  analytics_storage = denied is OK (modeling fills the gap)
  BUT analytics_storage must be denied via Consent Mode (not by blocking GA4 entirely)
```

## CMP Integration in GTM

A Consent Management Platform (CMP) shows the cookie banner and manages user consent choices. It must integrate with GTM to send `consent_update` commands.

### CMP Selection Guide

| CMP | Free Tier | GTM Template | TCF 2.2 | Best For |
|---|---|---|---|---|
| **Cookiebot** | Up to 1 domain, 50 pages | Yes (official) | Yes | Small-medium sites |
| **CookieYes** | Up to 100 pages | Yes (community) | Yes | Budget-conscious |
| **Usercentrics** | No free tier | Yes (official) | Yes | Enterprise, German market |
| **OneTrust** | No free tier | Yes (official) | Yes | Enterprise, global |
| **Complianz** | WordPress only | Via plugin | Yes | WordPress sites |
| **Iubenda** | Limited free | Yes (community) | Yes | Multi-language EU sites |
| **Consentmanager** | Up to 10k views/mo | Yes (official) | Yes | EU-focused, competitive pricing |

### CMP Integration Pattern (Generic)

Regardless of which CMP you use, the integration follows the same pattern in GTM:

```
1. Add CMP's GTM template (from Community Template Gallery)
   OR add CMP script via Custom HTML tag

2. Create "Consent Initialization - All Pages" trigger
   (Built-in trigger type in GTM)

3. Configure CMP tag to fire on Consent Initialization trigger
   This fires BEFORE any other tags

4. CMP tag:
   a. Sets consent_default (all denied for EEA)
   b. Checks for stored consent (returning visitor)
   c. If stored consent exists: fires consent_update immediately
   d. If there is no prior consent choice: shows banner, fires consent_update on interaction

5. All Google tags use Built-in Consent Checks:
   - GA4 tags: require analytics_storage
   - Google Ads tags: require ad_storage + ad_user_data
   - Remarketing tags: require ad_storage + ad_personalization
```

### Cookiebot Integration (Step by Step)

1. **Create Cookiebot account** at cookiebot.com, add your domain
2. **Get your Cookiebot ID** (CBID) from the dashboard
3. **In GTM:** Templates > Search Gallery > "Cookiebot CMP"
4. **Create tag:** Cookiebot CMP template
   - Cookiebot ID: `your-cbid-here`
   - Consent Mode: Enable
   - Default consent: Deny all
5. **Set trigger:** Consent Initialization - All Pages
6. **Configure tag consent:**
   - For each Google tag, go to Advanced Settings > Consent Settings
   - Set "Require additional consent for tag to fire"
   - Add appropriate consent types (see table below)

### Tag Consent Settings in GTM

For each tag, configure which consent types it requires:

| Tag | Required Consent (Additional) | Built-in Consent |
|---|---|---|
| Google Tag (GA4 Config) | `analytics_storage` | Built-in (automatic) |
| GA4 Event tags | `analytics_storage` | Built-in (automatic) |
| Google Ads Conversion | `ad_storage`, `ad_user_data` | Built-in (automatic) |
| Google Ads Remarketing | `ad_storage`, `ad_personalization` | Built-in (automatic) |
| Conversion Linker | `ad_storage` | Built-in (automatic) |
| Meta Pixel (Custom HTML) | `ad_storage` | NOT automatic -- must configure |
| LinkedIn Insight (Custom HTML) | `ad_storage` | NOT automatic -- must configure |
| TikTok Pixel (Custom HTML) | `ad_storage` | NOT automatic -- must configure |

**Critical:** Google tags (GA4, Google Ads) have built-in Consent Mode support and automatically adjust their behavior when consent is denied. Non-Google tags (Meta, LinkedIn, TikTok) do NOT have built-in support. You must either:
- Set "Additional Consent" in the tag's consent settings to block them when consent is denied, OR
- Use trigger conditions that check consent state before firing

### Non-Google Tags: Consent Gating

For Meta, LinkedIn, and TikTok tags that do not natively support Consent Mode:

**Option A: GTM Consent Settings (Recommended)**

1. Open the Meta/LinkedIn/TikTok tag
2. Advanced Settings > Consent Settings
3. Select "Require additional consent for tag to fire"
4. Add: `ad_storage`
5. The tag will only fire when `ad_storage` is granted

**Option B: Trigger Condition**

Create a custom trigger that checks consent state:

| Setting | Value |
|---|---|
| Trigger Type | Custom Event |
| Event Name | `purchase` (or whatever event) |
| Condition | `{{Consent - ad_storage}}` equals `granted` |

Where `{{Consent - ad_storage}}` is a Custom JavaScript variable:

```javascript
function() {
  try {
    return window.google_tag_data && 
           window.google_tag_data.ics && 
           window.google_tag_data.ics.entries && 
           window.google_tag_data.ics.entries.ad_storage && 
           window.google_tag_data.ics.entries.ad_storage.update === 'granted' 
           ? 'granted' : 'denied';
  } catch(e) {
    return 'denied';
  }
}
```

## Impact on Conversion Tracking

### Data Loss Estimation

When users deny consent, you lose their conversion data. The percentage varies by country and industry.

| Country / Region | Typical Consent Rate | Data Loss |
|---|---|---|
| Germany | 40-55% | 45-60% |
| France | 45-60% | 40-55% |
| Netherlands | 50-65% | 35-50% |
| Belgium | 45-60% | 40-55% |
| Nordics (Sweden, Denmark, Norway) | 55-70% | 30-45% |
| UK | 60-75% | 25-40% |
| Southern Europe (Spain, Italy) | 55-70% | 30-45% |
| US (if consent applied) | 75-90% | 10-25% |
| US (no consent required) | 100% | 0% |

**Industry Variation:**

| Audience Type | Consent Rate Modifier | Reason |
|---|---|---|
| Tech-savvy (developers, IT) | -15% | More privacy-aware |
| B2B enterprise | -10% | Corporate privacy policies |
| E-commerce (general) | Baseline | Average behavior |
| Healthcare / Finance | -10% | Privacy-sensitive users |
| Gaming / Entertainment | +10% | Younger, less privacy-concerned |

### What You Lose Without Consent

| Feature | With Consent | Without Consent (but Consent Mode active) | Without Consent Mode at all |
|---|---|---|---|
| GA4 page views | Full tracking | Cookieless pings (modeled) | Nothing |
| GA4 user count | Accurate | Modeled (+/- 15%) | Missing |
| GA4 conversions | Full tracking | Modeled | Missing |
| Google Ads conversions | Full tracking | Modeled (up to 70% recovery) | Missing |
| Google Ads remarketing | Full audiences | No audiences | No audiences |
| Meta Pixel events | Full tracking | Blocked entirely | Blocked entirely |
| LinkedIn events | Full tracking | Blocked entirely | Blocked entirely |
| TikTok events | Full tracking | Blocked entirely | Blocked entirely |

### Key Insight: Consent Mode vs. No Consent Mode

Even when consent is denied, Consent Mode sends cookieless pings to Google. These pings allow Google to model the missing conversions. Without Consent Mode, those conversions are simply gone.

```
Scenario: 1,000 actual conversions, 50% consent rate

WITHOUT Consent Mode:
  Reported: 500 conversions (50% loss)
  Modeled: 0
  Total visible: 500

WITH Consent Mode:
  Reported: 500 conversions (consented users)
  Modeled: ~350 conversions (70% of denied users recovered)
  Total visible: 850 (only 15% loss)
```

## Recovery Strategies

### Strategy 1: Google Consent Mode Behavioral Modeling

**How it works:** Google uses the observed behavior of consented users to model the likely conversions of non-consented users. The model considers factors like device type, geography, time of day, and the consented conversion rate.

**Requirements:**
- Consent Mode v2 properly implemented
- Minimum 1,000 ad-click events per day (for the property)
- Minimum 7 consecutive days of data
- If thresholds not met, modeling is partial or unavailable

**What you get:** Modeled conversions appear in GA4 and Google Ads reports with a "modeled" label. Smart Bidding strategies (tCPA, tROAS) can use modeled data for optimization.

### Strategy 2: Enhanced Conversions

Enhanced Conversions use first-party data (hashed email, phone, address) to attribute conversions without relying on cookies.

**Google Ads Enhanced Conversions:**
- Send hashed user data with conversion events
- Google matches against signed-in Google users
- Works even when `ad_storage` is denied, IF `ad_user_data` is granted
- Recovers 5-15% additional conversions

**Implementation (via GTM):**

See the gtm-conversion-setup-guide skill for detailed Enhanced Conversions tag setup.

**Important consent requirement:** Enhanced Conversions still require `ad_user_data` consent. If the user denies all consent, Enhanced Conversions cannot fire.

### Strategy 3: Server-Side Tagging (for Meta, LinkedIn, TikTok)

For non-Google platforms, Consent Mode behavioral modeling does not help. Server-side tagging is the primary recovery strategy.

**How it helps:**
- Server-side requests are not blocked by browser ad blockers
- Meta CAPI can send conversion data server-side (with user consent)
- First-party cookie domain extends cookie lifetime
- Recovers 10-25% of events lost to ad blockers (separate from consent loss)

**Limitation:** Server-side tagging does NOT bypass consent requirements. If the user denies consent, you must not send their data to ad platforms, even server-side.

See the gtm-server-side-tagging-guide skill for implementation details.

### Strategy 4: Conversion Import / Offline Conversions

For high-value conversions (B2B leads becoming customers, offline purchases):

| Platform | Feature | How |
|---|---|---|
| Google Ads | Offline Conversion Import | Upload CRM data with GCLID |
| Meta | Offline Conversions | Upload customer lists with purchase data |
| LinkedIn | Offline Conversions | Upload CRM data via Campaign Manager |
| TikTok | Offline Events | Upload via Events API |

This bypasses consent issues entirely because the data comes from your CRM (first-party), not from browser cookies.

### Strategy 5: Consent Banner Optimization

Improve your consent rate by optimizing the banner itself:

| Optimization | Typical Impact | Notes |
|---|---|---|
| "Accept All" button is visually prominent | +10-20% consent rate | Larger, colored, left-positioned |
| Reduce number of choices | +5-10% | Two buttons beats five categories |
| Explain value exchange | +5-10% | "Accept cookies for personalized offers" |
| Don't use dark patterns | Required by law | But also builds trust |
| Load banner quickly | +3-5% | Slow banners get dismissed |
| Remember choice (don't ask again) | N/A | Required and reduces friction |
| Position: bottom bar vs. modal | Varies | Test both; modals force a choice |

### Recovery Strategy Decision Matrix

| Strategy | Platforms | Consent Required | Recovery | Effort |
|---|---|---|---|---|
| Consent Mode modeling | Google only | No (works on denied) | 50-70% of lost Google data | Low |
| Enhanced Conversions | Google only | `ad_user_data` | 5-15% additional | Medium |
| Server-side tagging | All | Yes (for sending data) | 10-25% (ad blocker recovery) | High |
| Offline conversion import | All | No (CRM data) | Varies (depends on CRM match) | Medium |
| Banner optimization | All (indirect) | N/A | 5-20% more consented users | Low |

## TCF 2.2 Compliance

The Transparency and Consent Framework (TCF) 2.2, managed by the IAB, is the technical standard most CMPs use to communicate consent to ad tech vendors.

### TCF 2.2 and Google

Google is a registered TCF vendor. When your CMP supports TCF 2.2:

- The CMP sets a `__tcfapi` function and `euconsent-v2` cookie
- Google tags read TCF consent signals automatically
- You do NOT need to manually map TCF purposes to Consent Mode types
- Google handles the mapping: TCF Purpose 1 maps to analytics/ad storage, etc.

### TCF Purpose Mapping

| TCF Purpose | Maps To | Description |
|---|---|---|
| Purpose 1: Store/access information | `analytics_storage`, `ad_storage` | Basic cookie consent |
| Purpose 2: Select basic ads | `ad_personalization` | Basic ad targeting |
| Purpose 3: Create personalized ads profile | `ad_personalization` | Behavioral profiling |
| Purpose 4: Select personalized ads | `ad_personalization` | Serve personalized ads |
| Purpose 7: Measure ad performance | `ad_storage`, `ad_user_data` | Conversion tracking |
| Purpose 8: Measure content performance | `analytics_storage` | Content analytics |
| Purpose 9: Market research | `analytics_storage` | Audience insights |
| Purpose 10: Develop and improve products | `analytics_storage` | Product improvement |

### CMP TCF Configuration Checklist

- [ ] CMP is IAB-registered and TCF 2.2 certified
- [ ] Google LLC (Vendor ID 755) is in the vendor list
- [ ] All relevant TCF purposes are presented to the user
- [ ] Legitimate Interest is not used as legal basis for Purpose 1 (must be consent)
- [ ] `euconsent-v2` cookie is set correctly after user interaction
- [ ] `__tcfapi` JavaScript function is available on page
- [ ] GTM reads TCF signals (automatic for Google tags)

## Regional Consent Strategies

Not all visitors need the same consent experience. Use geo-targeting to show consent banners only where required.

### Strategy: Strict EU, Permissive Rest of World

```javascript
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'region': ['AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR',
             'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL',
             'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'IS', 'LI', 'NO',
             'CH', 'GB'],
  'wait_for_update': 500
});

// Rest of world: granted by default (no banner needed)
gtag('consent', 'default', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted'
});
```

### Regional Strategy Decision Table

| Region | Consent Required | Approach |
|---|---|---|
| EU/EEA (27 countries) | Yes, strict | Deny all by default, show banner |
| UK | Yes | Deny all by default, show banner |
| Switzerland | Yes (nFADP) | Deny all by default, show banner |
| US - California | Yes (CCPA) | Granted by default, show opt-out link |
| US - Other states with laws | Varies | Check state-specific requirements |
| US - No state law | No | Granted by default |
| Canada | Yes (PIPEDA) | Implied consent OK, show notice |
| Brazil | Yes (LGPD) | Similar to GDPR, show banner |
| Rest of world | Varies | Granted by default (assess per market) |

### US State Privacy Laws (as of 2026)

| State | Law | Effective | Approach |
|---|---|---|---|
| California | CCPA/CPRA | Active | Opt-out model (Do Not Sell) |
| Virginia | VCDPA | Active | Opt-out model |
| Colorado | CPA | Active | Opt-out model |
| Connecticut | CTDPA | Active | Opt-out model |
| Utah | UCPA | Active | Opt-out model |
| Texas | TDPSA | Active | Opt-out model |
| Oregon | OCPA | Active | Opt-out model |
| Montana | MCDPA | Active | Opt-out model |
| Additional states | Various | 2025-2026 | Check current status |

For US states: the opt-out model means you can set consent to `granted` by default but must provide a "Do Not Sell My Personal Information" mechanism.

## Testing Consent Implementation

### Pre-Launch Testing Checklist

- [ ] Banner appears on first visit (no prior consent stored)
- [ ] Banner does NOT appear on return visit (consent stored)
- [ ] "Accept All" sets all consent types to granted
- [ ] "Reject All" keeps all consent types denied
- [ ] Partial consent (analytics only) works correctly
- [ ] Google tags fire in restricted mode before consent
- [ ] Google tags fire in full mode after consent granted
- [ ] Non-Google tags (Meta, LinkedIn, TikTok) do NOT fire when consent denied
- [ ] Non-Google tags fire after consent granted
- [ ] `consent_default` fires BEFORE any tags (check GTM Preview)
- [ ] `consent_update` fires at correct time (after user interaction)
- [ ] Cookies are only set after consent granted
- [ ] Regional targeting works (EU gets banner, US does not)
- [ ] `wait_for_update` is set (returning visitors don't see banner flash)

### Testing Tools

| Tool | Purpose |
|---|---|
| GTM Preview Mode | Verify consent_default and consent_update timing |
| Chrome DevTools > Application > Cookies | Verify no cookies set before consent |
| Google Tag Assistant | Verify consent state per tag |
| GA4 DebugView | Verify events arrive with correct consent state |
| CMP scanner (e.g., cookiebot.com/scanner) | Verify all cookies are categorized |
| Browser private/incognito mode | Test first-visit experience |
| VPN to different countries | Test regional consent strategies |

### Debugging Consent Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| Banner does not appear | CMP script not loading | Check tag fires on Consent Initialization |
| Tags fire before consent | consent_default missing or late | Ensure Consent Initialization trigger is used |
| All consent shows "granted" for EU | Regional settings wrong | Check region list in consent_default |
| GA4 shows 0 users for EU | Consent Mode not enabled | Verify consent_default fires, check DebugView |
| Meta Pixel fires on denied | No consent gating on Meta tag | Add consent setting to Meta tag |
| Modeled data not appearing | Below traffic threshold | Need 1,000+ ad clicks/day for modeling |
| Banner appears every visit | Consent cookie not persisting | Check CMP cookie settings and domain |

## MCP Tools for Consent Auditing

### Audit Consent Implementation

Use **`gtm_audit`** to verify consent configuration in your GTM container:

```
gtm_audit(container_path="accounts/123456/containers/789012")

Check for:
- CMP tag present and fires on Consent Initialization
- consent_default configured (all denied for EU regions)
- Google tags have built-in consent checks enabled
- Non-Google tags have Additional Consent settings
- No tags fire on "All Pages" without consent gating
```

### Manage Consent Tags

Use **`gtm_manage`** to update consent settings across multiple tags:

```
gtm_manage(
  container_path="accounts/123456/containers/789012",
  action="update_tag",
  ...
)

Common updates:
- Add consent settings to non-Google tags
- Update CMP configuration parameters
- Add/remove regions from consent_default
```

### Verify Data Impact

After implementing consent, use GA4 reports to measure the impact:

```
Before consent implementation:
  ga4_run_report(dimensions=["country"], metrics=["activeUsers", "keyEvents"])

After consent implementation (2 weeks later):
  ga4_run_report(dimensions=["country"], metrics=["activeUsers", "keyEvents"])

Compare EU vs non-EU metrics to quantify consent impact.
Expected: 30-60% drop in EU tracked users, partially recovered by modeling.
```

Note: GA4 renamed "Conversions" to "Key Events" in the UI (2023). The Data API metric `keyEvents` reflects this; the older `conversions` metric name is deprecated. Always use `keyEvents` in API calls.
