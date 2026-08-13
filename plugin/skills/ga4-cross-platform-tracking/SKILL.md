---
name: ga4-cross-platform-tracking
description: "This skill should be used when the user asks to \"set up UTM parameters\", \"track Meta ads in GA4\", \"implement cross-platform tracking\", or mentions \"auto-tagging vs UTM\", \"campaign naming conventions\", or \"LinkedIn/TikTok attribution in GA4\". Do NOT use for: channel grouping configuration (use ga4-channel-groupings), attribution model selection (use ga4-attribution-advisor)."
---
# GA4 Cross-Platform Tracking Guide

Complete guide for consistent tracking of all advertising platforms in Google Analytics 4 with UTM parameters and platform integrations.

## UTM Parameters Basics

```
UTM PARAMETERS OVERVIEW
========================

THE 5 UTM PARAMETERS:
┌─────────────────┬───────────┬────────────────────────────────────┐
│ Parameter       │ Required? │ Purpose                            │
├─────────────────┼───────────┼────────────────────────────────────┤
│ utm_source      │ YES       │ Platform/source (facebook, linkedin)│
├─────────────────┼───────────┼────────────────────────────────────┤
│ utm_medium      │ YES       │ Marketing medium (cpc, social)     │
├─────────────────┼───────────┼────────────────────────────────────┤
│ utm_campaign    │ YES       │ Campaign name/ID                   │
├─────────────────┼───────────┼────────────────────────────────────┤
│ utm_content     │ Optional  │ Ad creative/variant                │
├─────────────────┼───────────┼────────────────────────────────────┤
│ utm_term        │ Optional  │ Keyword or targeting               │
└─────────────────┴───────────┴────────────────────────────────────┘

UTM URL STRUCTURE:
https://example.com/landing-page
  ?utm_source=facebook
  &utm_medium=paid-social
  &utm_campaign=summer-sale-2024
  &utm_content=video-ad-1
  &utm_term=lookalike-purchasers

IMPORTANT RULES:
├── Always use lowercase (GA4 is case-sensitive)
├── No spaces (use - or _)
├── Stay consistent across entire team
├── Never use UTM on internal links (pollutes data)
└── Test URLs before deployment
```

## Naming Convention Standard

```
NAMING CONVENTION FRAMEWORK
=============================

UTM_SOURCE (platform name):
┌─────────────────┬────────────────────────────────────┐
│ Platform        │ Standard source                    │
├─────────────────┼────────────────────────────────────┤
│ Facebook        │ facebook                           │
│ Instagram       │ instagram (or facebook if combined)│
│ LinkedIn        │ linkedin                           │
│ TikTok          │ tiktok                             │
│ Pinterest       │ pinterest                          │
│ Twitter/X       │ twitter                            │
│ Google Ads      │ google (auto-tagged)               │
│ Microsoft Ads   │ bing                               │
│ Email           │ newsletter / email                 │
└─────────────────┴────────────────────────────────────┘

UTM_MEDIUM (traffic type):
┌─────────────────┬────────────────────────────────────┐
│ Type            │ Standard medium                    │
├─────────────────┼────────────────────────────────────┤
│ Paid click      │ cpc                                │
│ Paid social     │ paid-social                        │
│ Organic social  │ organic-social                     │
│ Display ads     │ display                            │
│ Video ads       │ video                              │
│ Email           │ email                              │
│ Affiliate       │ affiliate                          │
│ Referral        │ referral                           │
│ Retargeting     │ retargeting                        │
└─────────────────┴────────────────────────────────────┘

UTM_CAMPAIGN (campaign identification):
Format: [year]-[month]-[type]-[description]

Examples:
├── 2024-06-promo-summer-sale
├── 2024-q3-brand-awareness
├── 2024-08-retargeting-cart-abandonment
├── 2024-ongoing-lead-gen-whitepaper
└── 2024-07-launch-new-product

UTM_CONTENT (ad creative):
Format: [format]-[variant]-[identifier]

Examples:
├── video-15s-product-demo
├── carousel-3img-testimonials
├── static-square-discount
├── story-fullscreen-v2
└── lead-form-short

UTM_TERM (targeting):
Format: [audience-type]-[detail]

Examples:
├── lookalike-purchasers-1pct
├── interest-marketing-professionals
├── retargeting-30d-visitors
├── custom-email-list
└── broad-age25-44
```

## Platform-Specific Setup

### Meta (Facebook & Instagram)

```
META ADS UTM CONFIGURATION
============================

WHERE TO CONFIGURE:
├── Ad Level → Destination → URL Parameters
├── Or: Campaign/Ad Set Level → Tracking → URL Parameters

RECOMMENDED TEMPLATE:
utm_source=facebook
&utm_medium=paid-social
&utm_campaign={{campaign.name}}
&utm_content={{ad.name}}
&utm_term={{adset.name}}

DYNAMIC PARAMETERS META:
┌─────────────────────────┬────────────────────────────────────┐
│ Parameter               │ What it contains                   │
├─────────────────────────┼────────────────────────────────────┤
│ {{campaign.name}}       │ Campaign name                      │
│ {{campaign.id}}         │ Campaign ID                        │
│ {{adset.name}}          │ Ad set name                        │
│ {{adset.id}}            │ Ad set ID                          │
│ {{ad.name}}             │ Ad name                            │
│ {{ad.id}}               │ Ad ID                              │
│ {{placement}}           │ Placement (feed, stories, etc.)    │
│ {{site_source_name}}    │ Platform (fb, ig, an, msg)         │
└─────────────────────────┴────────────────────────────────────┘

ADVANCED TEMPLATE (with placement):
utm_source={{site_source_name}}
&utm_medium=paid-social
&utm_campaign={{campaign.name}}
&utm_content={{ad.name}}_{{placement}}
&utm_term={{adset.name}}

NOTE:
├── fbclid is automatically added by Meta
├── GA4 does NOT recognize fbclid for attribution
├── UTM is essential for GA4 tracking
├── Test in Events Manager for parameter validation
└── Meta Pixel is still needed for Meta Attribution
```

### LinkedIn Ads

```
LINKEDIN ADS UTM CONFIGURATION
================================

WHERE TO CONFIGURE:
├── Campaign Manager → Campaign → Ad → Destination URL
├── Or: Bulk upload via campaign CSV

RECOMMENDED TEMPLATE:
utm_source=linkedin
&utm_medium=paid-social
&utm_campaign={{CAMPAIGN_NAME}}
&utm_content={{CREATIVE_NAME}}
&utm_term={{CAMPAIGN_GROUP_NAME}}

DYNAMIC PARAMETERS LINKEDIN:
┌─────────────────────────┬────────────────────────────────────┐
│ Parameter               │ What it contains                   │
├─────────────────────────┼────────────────────────────────────┤
│ {{CAMPAIGN_NAME}}       │ Campaign name                      │
│ {{CAMPAIGN_ID}}         │ Campaign ID                        │
│ {{CAMPAIGN_GROUP_NAME}} │ Campaign group name                │
│ {{CAMPAIGN_GROUP_ID}}   │ Campaign group ID                  │
│ {{CREATIVE_NAME}}       │ Creative/ad name                   │
│ {{CREATIVE_ID}}         │ Creative ID                        │
│ {{MEMBER_ID}}           │ LinkedIn member ID (hashed)        │
└─────────────────────────┴────────────────────────────────────┘

LINKEDIN INSIGHT TAG:
─────────────────────
In addition to UTM, install LinkedIn Insight Tag:
├── Required for LinkedIn Attribution
├── Required for LinkedIn Audiences
├── Required for Conversion Tracking
└── Implement via GTM or directly

<!-- LinkedIn Insight Tag (in GTM or head) -->
<script type="text/javascript">
_linkedin_partner_id = "XXXXXX";
// ... rest of Insight Tag code
</script>

NOTE:
├── LinkedIn adds li_fat_id (for first-party tracking)
├── This is NOT sufficient for GA4
├── UTM is essential for GA4 attribution
└── B2B: consider longer attribution windows
```

## GA4 Channel Groupings Impact

```
UTM → GA4 CHANNEL GROUPING MAPPING
====================================

HOW GA4 DETERMINES CHANNELS:
GA4 looks at source/medium combination:

┌─────────────────────────────────┬─────────────────────────────┐
│ Source/Medium                   │ GA4 Default Channel         │
├─────────────────────────────────┼─────────────────────────────┤
│ facebook / paid-social          │ Paid Social                 │
│ facebook / cpc                  │ Paid Social (cpc matched)   │
│ linkedin / paid-social          │ Paid Social                 │
│ tiktok / paid-social            │ Paid Social                 │
│ facebook / organic-social       │ Organic Social              │
│ google / cpc                    │ Paid Search                 │
│ google / organic                │ Organic Search              │
│ newsletter / email              │ Email                       │
│ (direct) / (none)               │ Direct                      │
│ example.com / referral          │ Referral                    │
└─────────────────────────────────┴─────────────────────────────┘

COMMON MISTAKES:
────────────────
WRONG: utm_medium=social
   → GA4 sees this as "Organic Social" instead of "Paid Social"

CORRECT: utm_medium=paid-social
   → GA4 puts in "Paid Social" channel

WRONG: utm_medium=Facebook
   → Case mismatch, inconsistent data

CORRECT: utm_medium=paid-social
   → Consistent with naming convention

MEDIUM VALUES THAT TRIGGER PAID SOCIAL:
├── paid-social
├── paidsocial
├── paid_social
├── cpc (if source is a social platform)
├── ppc (if source is a social platform)
└── cpm (if source is a social platform)

CHECK YOUR CHANNEL MAPPING:
LOCATION: GA4 → Admin → Data display → Default channel group
Here you can see which rules GA4 applies
```

## Tracking Verification

```
UTM TRACKING VERIFICATION STEPS
=================================

STEP 1: URL VALIDATION (before launch)
───────────────────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Use Campaign URL Builder tool                             │
│    │ https://ga-dev-tools.google/campaign-url-builder/         │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Test URL in browser - does page load correctly?           │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Check special characters are encoded                      │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Verify no spaces or uppercase                             │
└────┴────────────────────────────────────────────────────────────┘

STEP 2: GA4 DEBUGVIEW TEST
───────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Open GA4 → Configure → DebugView                          │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Activate debug mode (GA Debugger extension)               │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click your test UTM URL                                   │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Check in DebugView:                                       │
│    │ - page_view event appears                                 │
│    │ - campaign, source, medium parameters correct             │
└────┴────────────────────────────────────────────────────────────┘

STEP 3: REALTIME VERIFICATION
──────────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ GA4 → Reports → Realtime                                  │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Look at "Traffic source" card                             │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Verify source/medium/campaign correct                     │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Check that channel grouping is correct                    │
└────┴────────────────────────────────────────────────────────────┘

STEP 4: REPORTING VERIFICATION (24-48 hours later)
───────────────────────────────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ GA4 → Reports → Acquisition → Traffic acquisition         │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Filter on your test campaign                              │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Verify sessions and events appear                         │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Check channel grouping is correct                         │
└────┴────────────────────────────────────────────────────────────┘

TEST CHECKLIST:
[ ] URL loads correctly with parameters
[ ] Page_view appears in DebugView
[ ] Source parameter correct
[ ] Medium parameter correct
[ ] Campaign parameter correct
[ ] Content parameter correct (if used)
[ ] Term parameter correct (if used)
[ ] Default channel grouping is correct
[ ] No (not set) or (other) values
```

## 2026: Cross-Channel Budgeting in GA4

```
GA4 CROSS-CHANNEL BUDGETING (BETA, 2026)
==========================================

WHAT IT IS:
├── A budget planning tool inside GA4 that combines data from multiple ad platforms
├── Supported platforms: Google Ads (native), Meta, LinkedIn, TikTok, Snapchat (import)
├── Location: GA4 → Advertising → Cross-channel budgeting
└── Uses GA4's data-driven attribution as the single source of truth

WHY IT MATTERS FOR TRACKING SETUP:
├── Consistent UTMs are critical for this feature to work correctly
├── Meta, LinkedIn, TikTok data must be connected via GA4 product links
├── Platform performance is compared using GA4 attributed conversions (Key Events)
└── Accurate channel groupings are prerequisite (Paid Social must not fall into Unassigned)

SETUP REQUIREMENTS:
├── All paid platforms must have UTMs on every ad
├── Channel groupings must be clean (Unassigned < 5%)
└── Key Events must be correctly configured with values

MCP TOOL - Check cross-channel attribution:
```
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["keyEvents", "totalRevenue"],
    dimensions=["sessionDefaultChannelGroup", "sessionCampaignName"],
    start_date="30daysAgo",
    end_date="yesterday"
)
```
```

## Output: Cross-Platform Tracking Template

```markdown
# Cross-Platform Tracking Configuration

## Account Overview
- **GA4 Property:** [Property name]
- **Measurement ID:** G-XXXXXXXXXX
- **Active platforms:** [Meta, LinkedIn, TikTok, Google Ads]

## Platform Configuration Status

### Google Ads
| Setting | Status | Details |
|---------|--------|---------|
| Auto-tagging | ✅/❌ | [Enabled/Disabled] |
| GA4 Link | ✅/❌ | [Account ID] |
| UTM (optional) | N/A | Not needed with auto-tagging |

### Meta Ads
| Setting | Status | Details |
|---------|--------|---------|
| UTM Template | ✅/❌ | [Template description] |
| Dynamic params | ✅/❌ | [{{campaign.name}} etc.] |
| Pixel installed | ✅/❌ | [Pixel ID] |

### LinkedIn Ads
| Setting | Status | Details |
|---------|--------|---------|
| UTM Template | ✅/❌ | [Template description] |
| Dynamic params | ✅/❌ | [{{CAMPAIGN_NAME}} etc.] |
| Insight Tag | ✅/❌ | [Partner ID] |

### TikTok Ads
| Setting | Status | Details |
|---------|--------|---------|
| UTM Template | ✅/❌ | [Template description] |
| Dynamic params | ✅/❌ | [__CAMPAIGN_NAME__ etc.] |
| Pixel installed | ✅/❌ | [Pixel ID] |

## UTM Naming Convention

### Approved Values
| Parameter | Format | Examples |
|-----------|--------|----------|
| utm_source | [platform-name] | facebook, linkedin, tiktok |
| utm_medium | [traffic-type] | paid-social, cpc, email |
| utm_campaign | [year]-[month]-[type]-[description] | 2024-06-promo-summer |
| utm_content | [format]-[variant] | video-15s-product |
| utm_term | [audience]-[detail] | lookalike-purchasers |

## Platform URL Templates

### Meta Ads Template
```
?utm_source=facebook&utm_medium=paid-social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}
```

### LinkedIn Ads Template
```
?utm_source=linkedin&utm_medium=paid-social&utm_campaign={{CAMPAIGN_NAME}}&utm_content={{CREATIVE_NAME}}&utm_term={{CAMPAIGN_GROUP_NAME}}
```

### TikTok Ads Template
```
?utm_source=tiktok&utm_medium=paid-social&utm_campaign=__CAMPAIGN_NAME__&utm_content=__AID_NAME__&utm_term=__ADGROUP_NAME__
```

## Verification Checklist
| Platform | URL Test | DebugView | Realtime | Reports |
|----------|----------|-----------|----------|---------|
| Meta | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| LinkedIn | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| TikTok | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Google Ads | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |

## Expected Data Discrepancies
| Platform | vs GA4 | Reason |
|----------|--------|--------|
| Meta | +/-20-30% | View-through, cross-device |
| LinkedIn | +/-15-25% | B2B longer cycles |
| TikTok | +/-20-30% | Mobile app attribution |
| Google Ads | +/-5-10% | Best accuracy with auto-tag |

## Next Steps
1. [ ] [Action 1]
2. [ ] [Action 2]
3. [ ] [Action 3]

## Notes
[Additional remarks, exceptions, or special configurations]
```
