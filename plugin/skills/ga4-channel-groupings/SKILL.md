---
name: ga4-channel-groupings
description: "This skill should be used when the user asks to \"configure channel groupings\", \"create custom channel groups\", \"fix source/medium mapping\", or mentions \"branded vs non-branded traffic\", \"default channel groups\", or \"affiliate tracking channels\". Do NOT use for: UTM parameter setup (use ga4-cross-platform-tracking), attribution model selection (use ga4-attribution-advisor)."
---
# GA4 Channel Groupings Guide

Complete guide for configuring and optimizing channel groupings in Google Analytics 4 for accurate traffic categorization.

## Default Channel Groups

```
GA4 DEFAULT CHANNEL GROUPS
===========================

NOTE: GA4 introduced the "Primary Channel Group" concept in March 2024.
This is now the default grouping shown in Acquisition reports. The ~20
default channels below are unchanged. Custom channel groups are still
available under Admin → Data display → Custom channel groups.

THE ~20 STANDARD CHANNELS:
┌─────────────────────┬───────────────────────────────────────────┐
│ Channel             │ When triggered                            │
├─────────────────────┼───────────────────────────────────────────┤
│ Direct              │ Source = (direct) AND medium = (none/not  │
│                     │ set)                                      │
├─────────────────────┼───────────────────────────────────────────┤
│ Organic Search      │ Source = search engine AND medium =       │
│                     │ organic (google, bing, yahoo, etc.)       │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Search         │ Source = search engine AND medium =       │
│                     │ cpc/ppc/paid AND campaign != shopping     │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Shopping       │ (Source = shopping sites) OR              │
│                     │ (campaign contains shop/shopping)         │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Social         │ Source = social network AND medium =      │
│                     │ cpc/ppc/paid/paid-social                  │
├─────────────────────┼───────────────────────────────────────────┤
│ Organic Social      │ Source = social network AND medium =      │
│                     │ social/organic-social OR referral         │
├─────────────────────┼───────────────────────────────────────────┤
│ Email               │ Medium = email                            │
├─────────────────────┼───────────────────────────────────────────┤
│ Affiliates          │ Medium = affiliate                        │
├─────────────────────┼───────────────────────────────────────────┤
│ Referral            │ Medium = referral (and not social)        │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Video          │ Source = video platform AND medium = cpc  │
│                     │ (youtube, vimeo, etc.)                    │
├─────────────────────┼───────────────────────────────────────────┤
│ Organic Video       │ Source = video platform AND medium =      │
│                     │ organic/referral                          │
├─────────────────────┼───────────────────────────────────────────┤
│ Display             │ Medium = display/banner/cpm               │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Other          │ Medium = cpc/ppc/paid (not matched        │
│                     │ elsewhere)                                │
├─────────────────────┼───────────────────────────────────────────┤
│ Organic Shopping    │ Source = shopping AND medium != paid      │
├─────────────────────┼───────────────────────────────────────────┤
│ Audio               │ Medium = audio                            │
├─────────────────────┼───────────────────────────────────────────┤
│ SMS                 │ Medium = sms                              │
├─────────────────────┼───────────────────────────────────────────┤
│ Mobile Push         │ Medium = push/mobile/notification         │
├─────────────────────┼───────────────────────────────────────────┤
│ Unassigned          │ None of the above rules match             │
└─────────────────────┴───────────────────────────────────────────┘

ORDER MATTERS:
├── GA4 evaluates channels from top to bottom
├── First match wins
├── Therefore: specific rules first, general rules later
└── "Unassigned" is always the last fallback
```

## Channel Group Configuration

```
CUSTOMIZING PRIMARY CHANNEL GROUP
===================================

LOCATION: Admin → Data display → Default channel group

WHAT YOU CAN CUSTOMIZE:
├── Channel order (priority)
├── Channel rules (source/medium matching)
├── Add new channels
└── Rename existing channels

STEP-BY-STEP CUSTOMIZATION:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Go to Admin → Data display → Default channel group        │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click the channel you want to customize                   │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Review the current rules                                  │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Click "Add new condition" for extra rules                 │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Define source/medium/campaign matching                    │
├────┼────────────────────────────────────────────────────────────┤
│ 6  │ Save changes                                              │
└────┴────────────────────────────────────────────────────────────┘

ADDING A NEW CHANNEL:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Scroll to bottom of channel list                          │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click "Add new channel"                                   │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Give the channel a name                                   │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Define matching rules                                     │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Drag channel to correct position (order matters!)         │
├────┼────────────────────────────────────────────────────────────┤
│ 6  │ Save                                                      │
└────┴────────────────────────────────────────────────────────────┘

IMPORTANT:
├── Changes are NOT retroactive
├── Only future data is affected
├── Test first with exploration report
└── Document all changes for team
```

## Custom Channel Rules

```
CHANNEL RULE SYNTAX
===================

AVAILABLE CONDITIONS:
┌─────────────────────┬────────────────────────────────────────────┐
│ Dimension           │ Examples                                   │
├─────────────────────┼────────────────────────────────────────────┤
│ Source              │ google, facebook, linkedin, affiliate-name │
├─────────────────────┼────────────────────────────────────────────┤
│ Medium              │ cpc, organic, referral, email, affiliate   │
├─────────────────────┼────────────────────────────────────────────┤
│ Campaign            │ Campaign name or ID                        │
├─────────────────────┼────────────────────────────────────────────┤
│ Source platform     │ Advertising platform (Google Ads, etc.)    │
└─────────────────────┴────────────────────────────────────────────┘

MATCHING OPERATORS:
┌─────────────────────┬────────────────────────────────────────────┐
│ Operator            │ Usage                                      │
├─────────────────────┼────────────────────────────────────────────┤
│ exactly matches     │ Exact string match (case insensitive)      │
├─────────────────────┼────────────────────────────────────────────┤
│ contains            │ Substring anywhere in value                │
├─────────────────────┼────────────────────────────────────────────┤
│ begins with         │ String starts with value                   │
├─────────────────────┼────────────────────────────────────────────┤
│ ends with           │ String ends with value                     │
├─────────────────────┼────────────────────────────────────────────┤
│ matches regex       │ Regular expression match                   │
├─────────────────────┼────────────────────────────────────────────┤
│ is one of           │ Match against list of values               │
└─────────────────────┴────────────────────────────────────────────┘

EXAMPLE RULES:

Channel: "Affiliate"
├── Rule 1: Medium exactly matches "affiliate"
├── Rule 2: Source contains "partner"
└── Rule 3: Campaign begins with "aff-"
→ Matches if ANY of the above is true

Channel: "Paid Brand Search"
├── Rule 1: Medium is one of [cpc, ppc, paid]
├── AND
├── Rule 2: Source exactly matches "google"
├── AND
├── Rule 3: Campaign contains "brand"
→ Matches if ALL of the above are true

COMBINING RULES (AND vs OR):
─────────────────────────────
Within one rule: AND (all conditions must match)
Between rules: OR (one of the rules must match)

Example "Paid Social" channel:
├── Rule 1: Source=facebook AND Medium=paid-social
├── OR
├── Rule 2: Source=instagram AND Medium=paid-social
├── OR
├── Rule 3: Source=linkedin AND Medium=paid-social
└── → Traffic becomes "Paid Social" if ANY rule matches
```

## Common Custom Channels

```
POPULAR CUSTOM CHANNEL CONFIGURATIONS
=======================================

1. BRANDED VS NON-BRANDED SEARCH
─────────────────────────────────

Channel: "Paid Search - Brand"
┌─────────────────────┬────────────────────────────────────────────┐
│ Condition           │ Setting                                    │
├─────────────────────┼────────────────────────────────────────────┤
│ Medium              │ is one of: cpc, ppc, paid                  │
│ AND Source          │ is one of: google, bing                    │
│ AND Campaign        │ contains: brand (or your brand name)       │
└─────────────────────┴────────────────────────────────────────────┘

Channel: "Paid Search - Non-Brand"
┌─────────────────────┬────────────────────────────────────────────┐
│ Condition           │ Setting                                    │
├─────────────────────┼────────────────────────────────────────────┤
│ Medium              │ is one of: cpc, ppc, paid                  │
│ AND Source          │ is one of: google, bing                    │
│ AND Campaign        │ does not contain: brand                    │
└─────────────────────┴────────────────────────────────────────────┘

Place "Paid Search - Brand" ABOVE "Paid Search - Non-Brand"

2. AFFILIATE MARKETING
──────────────────────

Channel: "Affiliate"
┌─────────────────────┬────────────────────────────────────────────┐
│ Rule 1              │ Medium exactly matches: affiliate          │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 2           │ Source contains: affiliate                 │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 3           │ Campaign begins with: aff_                 │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 4           │ Source is one of: [affiliate-partner-1,    │
│                     │ affiliate-partner-2, etc.]                 │
└─────────────────────┴────────────────────────────────────────────┘

3. INFLUENCER MARKETING
───────────────────────

Channel: "Influencer"
┌─────────────────────┬────────────────────────────────────────────┐
│ Rule 1              │ Medium exactly matches: influencer         │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 2           │ Campaign contains: influencer              │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 3           │ Campaign begins with: inf_                 │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 4           │ Source contains: creator                   │
└─────────────────────┴────────────────────────────────────────────┘

4. PARTNER/RESELLER TRAFFIC
────────────────────────────

Channel: "Partner"
┌─────────────────────┬────────────────────────────────────────────┐
│ Rule 1              │ Medium exactly matches: partner            │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 2           │ Source is one of: [partner-1.com,          │
│                     │ partner-2.com, reseller.com]               │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 3           │ Campaign begins with: partner_             │
└─────────────────────┴────────────────────────────────────────────┘

5. RETARGETING SEPARATE
────────────────────────

Channel: "Retargeting"
┌─────────────────────┬────────────────────────────────────────────┐
│ Rule 1              │ Medium exactly matches: retargeting        │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 2           │ Campaign contains: retargeting             │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 3           │ Campaign contains: remarketing             │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 4           │ Medium exactly matches: remarketing        │
└─────────────────────┴────────────────────────────────────────────┘

Place "Retargeting" ABOVE "Paid Social" and "Paid Search"
Otherwise retargeting traffic gets categorized in those channels
```

## Channel Order Optimization

```
DETERMINING CHANNEL PRIORITY
==============================

RECOMMENDED ORDER:
┌────┬────────────────────────┬────────────────────────────────────┐
│ #  │ Channel                │ Rationale                          │
├────┼────────────────────────┼────────────────────────────────────┤
│ 1  │ Retargeting            │ Most specific paid traffic         │
├────┼────────────────────────┼────────────────────────────────────┤
│ 2  │ Paid Search - Brand    │ Specific search subset             │
├────┼────────────────────────┼────────────────────────────────────┤
│ 3  │ Paid Shopping          │ Shopping-specific campaigns        │
├────┼────────────────────────┼────────────────────────────────────┤
│ 4  │ Paid Search            │ General paid search                │
├────┼────────────────────────┼────────────────────────────────────┤
│ 5  │ Paid Social            │ Social advertising                 │
├────┼────────────────────────┼────────────────────────────────────┤
│ 6  │ Display                │ Display/banner ads                 │
├────┼────────────────────────┼────────────────────────────────────┤
│ 7  │ Paid Video             │ YouTube/video ads                  │
├────┼────────────────────────┼────────────────────────────────────┤
│ 8  │ Paid Other             │ Other paid traffic                 │
├────┼────────────────────────┼────────────────────────────────────┤
│ 9  │ Affiliate              │ Affiliate partners                 │
├────┼────────────────────────┼────────────────────────────────────┤
│ 10 │ Influencer             │ Influencer collaborations          │
├────┼────────────────────────┼────────────────────────────────────┤
│ 11 │ Partner                │ Business partners                  │
├────┼────────────────────────┼────────────────────────────────────┤
│ 12 │ Email                  │ Email marketing                    │
├────┼────────────────────────┼────────────────────────────────────┤
│ 13 │ SMS                    │ SMS campaigns                      │
├────┼────────────────────────┼────────────────────────────────────┤
│ 14 │ Push Notifications     │ Mobile push                        │
├────┼────────────────────────┼────────────────────────────────────┤
│ 15 │ Organic Search         │ SEO traffic                        │
├────┼────────────────────────┼────────────────────────────────────┤
│ 16 │ Organic Social         │ Unpaid social                      │
├────┼────────────────────────┼────────────────────────────────────┤
│ 17 │ Organic Video          │ YouTube organic                    │
├────┼────────────────────────┼────────────────────────────────────┤
│ 18 │ Referral               │ Website referrals                  │
├────┼────────────────────────┼────────────────────────────────────┤
│ 19 │ Direct                 │ Direct traffic                     │
├────┼────────────────────────┼────────────────────────────────────┤
│ 20 │ Unassigned             │ Catch-all (always last)            │
└────┴────────────────────────┴────────────────────────────────────┘

PRINCIPLE:
├── Most specific rules first
├── Paid traffic before organic
├── Custom channels before default channels
├── Direct and Unassigned always last
└── Test order with sample data
```

## MCP Tool: Analyze Channel Distribution

```python
# Check traffic and conversions by channel group
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["sessions", "keyEvents", "totalRevenue", "sessionKeyEventRate"],
    dimensions=["sessionDefaultChannelGroup"],
    start_date="30daysAgo",
    end_date="yesterday"
)

# Find "Unassigned" traffic to diagnose missing UTMs
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="30daysAgo",
    end_date="yesterday",
    metrics=["sessions"],
    dimensions=["sessionDefaultChannelGroup", "sessionSourceMedium"]
)
# Filter for "Unassigned" in the results to diagnose missing UTMs
```

## Output: Channel Configuration Template

```markdown
# GA4 Channel Grouping Configuration

## Property Information
- **GA4 Property:** [Property name]
- **Measurement ID:** G-XXXXXXXXXX
- **Configuration date:** [Date]
- **Last modified:** [Date]

## UTM Requirements per Channel

| Channel | Required UTM | Example |
|---------|--------------|---------|
| Paid Social | medium=paid-social | utm_medium=paid-social |
| Affiliate | medium=affiliate | utm_medium=affiliate |
| Influencer | medium=influencer | utm_medium=influencer |
| Partner | medium=partner | utm_medium=partner |
| Retargeting | campaign contains "retargeting" | utm_campaign=fb-retargeting-cart |

## Testing & Verification

### Test Cases
| Test URL | Expected Channel | Actual Channel | Status |
|----------|------------------|----------------|--------|
| ?utm_source=facebook&utm_medium=paid-social | Paid Social | [Result] | ✅/❌ |
| ?utm_source=google&utm_medium=cpc&utm_campaign=brand | Paid Search - Brand | [Result] | ✅/❌ |
| ?utm_source=partner-x&utm_medium=affiliate | Affiliate | [Result] | ✅/❌ |
| ?utm_source=influencer-y&utm_medium=influencer | Influencer | [Result] | ✅/❌ |

## Traffic Distribution Analysis

### Current Distribution (Last 30 Days)
| Channel | Sessions | % of Total | Conversions |
|---------|----------|------------|-------------|
| Paid Search | [X] | [X]% | [X] |
| Paid Social | [X] | [X]% | [X] |
| Organic Search | [X] | [X]% | [X] |
| Direct | [X] | [X]% | [X] |
| Referral | [X] | [X]% | [X] |
| Unassigned | [X] | [X]% | [X] |

### Target: Unassigned < 5%
Current Unassigned: [X]% - Action needed: On target / Review UTMs

## Issues & Resolutions Log

| Date | Issue | Resolution |
|------|-------|------------|
| [Date] | [Issue description] | [How resolved] |

## Next Steps
1. [ ] [Action 1]
2. [ ] [Action 2]
3. [ ] [Action 3]

## Notes
[Additional observations, exceptions, or special situations]
```
