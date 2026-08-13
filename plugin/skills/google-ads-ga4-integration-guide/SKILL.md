---
name: google-ads-ga4-integration-guide
description: "This skill should be used when the user asks to \"link Google Ads to GA4\", \"import GA4 conversions into Google Ads\", \"sync GA4 audiences\", \"align attribution models\", or mentions \"UTM tagging\", \"cross-platform tracking\", or \"data-driven attribution\". Do NOT use for: GA4 standalone reporting (use ga4 MCP tools directly), conversion tracking setup (use conversion-tracking-setup), enhanced conversions (use enhanced-conversions-setup)."
---
# GA4 Integration Guide

Complete guide for linking Google Ads with Google Analytics 4 for better audience targeting, conversion attribution, and cross-platform insights.



## GAQL: Verify GA4 Conversion Import + Attribution

Use `google_ads_run_gaql` to check which conversions are imported and how they are attributed:

```sql
SELECT conversion_action.name, conversion_action.status,
    conversion_action.type, conversion_action.category,
    conversion_action.attribution_model_settings.attribution_model,
    conversion_action.counting_type,
    metrics.conversions, metrics.all_conversions
FROM conversion_action
WHERE conversion_action.status = 'ENABLED'
ORDER BY metrics.all_conversions DESC
LIMIT 50
```

```sql
-- Campaign performance with GA4-imported conversions
SELECT campaign.name, campaign.advertising_channel_type,
    metrics.impressions, metrics.clicks, metrics.cost_micros,
    metrics.conversions, metrics.conversions_value,
    metrics.all_conversions
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
AND campaign.status = 'ENABLED'
ORDER BY metrics.conversions DESC
```

## Google Ads ↔ GA4 Linking

### Linking Setup

```
LINKING GOOGLE ADS AND GA4
══════════════════════════

REQUIREMENTS:
─────────────
□ Admin access in GA4 property
□ Admin access in Google Ads account
□ Same Google account (or linked accounts)

STEP 1: FROM GA4
─────────────────
1. GA4 → Admin → Product links → Google Ads links
2. Click "Link"
3. Select Google Ads account(s)
4. Configure settings:
   ├── Enable personalized advertising: ON
   ├── Enable auto-tagging: Recommended ON
   └── Click "Next" → "Submit"

STEP 2: VERIFY LINKING
───────────────────────
In GA4:
├── Admin → Google Ads links
└── Status: "Active"

In Google Ads:
├── Tools → Linked accounts → Google Analytics (GA4)
└── Status: "Linked"

WHAT THIS LINK ENABLES:
───────────────────────
┌─────────────────────────────────────────────────────────────────┐
│  FUNCTIONALITY                │ STATUS AFTER LINKING            │
├────────────────────────────────┼───────────────────────────────┤
│ Google Ads data in GA4         │ Automatic                     │
│ GA4 conversions → Google Ads   │ Manual import required        │
│ GA4 audiences → Google Ads     │ Manual enable required        │
│ Google Ads metrics in GA4      │ cost, clicks, impressions     │
│ Cross-platform attribution     │ Attribution settings          │
└────────────────────────────────┴───────────────────────────────┘

AUTO-TAGGING VS MANUAL TAGGING:
───────────────────────────────
AUTO-TAGGING (Recommended):
├── Google Ads adds gclid to URLs
├── GA4 recognizes automatically
├── Most accurate tracking
└── Enables: full Google Ads integration

MANUAL TAGGING (UTM):
├── You add UTM parameters yourself
├── More control over source/medium
├── Needed for: cross-domain, third-party tools
└── Can work alongside auto-tagging
```

### Attribution Model Alignment

```
ALIGNING ATTRIBUTION MODELS
════════════════════════════

PROBLEM: GA4 AND GOOGLE ADS SHOW DIFFERENT CONVERSIONS
──────────────────────────────────────────────────────

Causes:
├── Different attribution models
├── Different lookback windows
├── Conversion counting (one vs every)
└── Cross-device handling

ATTRIBUTION MODEL OPTIONS:
──────────────────────────

┌──────────────────────────────────────────────────────────────────┐
│ Model                │ Description            │ Use Case         │
├──────────────────────┼────────────────────────┼──────────────────┤
│ Data-driven          │ AI-based, adapts to    │ Recommended     │
│                      │ your data              │ (default 2024+)  │
├──────────────────────┼────────────────────────┼──────────────────┤
│ Last Click           │ 100% to last           │ Simple funnel    │
│                      │ (non-direct) click     │ comparison       │
├──────────────────────┼────────────────────────┼──────────────────┤
│ First Click          │ 100% to first click    │ Awareness focus  │
├──────────────────────┼────────────────────────┼──────────────────┤
│ Linear               │ Equally distributed    │ All touchpoints  │
│                      │                        │ equally important│
├──────────────────────┼────────────────────────┼──────────────────┤
│ Position-based       │ 40% first, 40% last    │ Balance awareness│
│                      │ 20% middle             │ + conversion     │
├──────────────────────┼────────────────────────┼──────────────────┤
│ Time decay           │ More to recent         │ Short sales      │
│                      │                        │ cycles           │
└──────────────────────┴────────────────────────┴──────────────────┘

RECOMMENDED ALIGNMENT:
──────────────────────
1. GA4: Admin → Attribution settings
   └── Reporting attribution model: Data-driven

2. Google Ads: Tools → Conversions → [Conversion] → Settings
   └── Attribution model: Data-driven

3. Align lookback windows:
   ├── GA4: 30, 60, or 90 days
   └── Google Ads: Match with GA4 setting

WARNING — DATA-DRIVEN REQUIRES:
├── Minimum 300 conversions in 30 days
├── Minimum 3000 ad interactions
└── Otherwise: fallback to last-click
```

## Importing GA4 Conversions

### Conversion Import Setup

```
IMPORTING GA4 CONVERSIONS TO GOOGLE ADS
═══════════════════════════════════════

WHY IMPORT GA4 CONVERSIONS?
───────────────────────────
□ Single source of truth
□ Better cross-device tracking
□ Includes modeled conversions
□ Less duplicate tracking
□ Consistent with web analytics

WHICH CONVERSIONS TO IMPORT:
────────────────────────────
Yes: Purchase (e-commerce)
Yes: Form submissions (lead gen)
Yes: Sign ups
No:  Page views (not suitable)
No:  Scroll depth (not suitable)
No:  Engagement events (use GA4 audiences instead)

STEP 1: MARK GA4 CONVERSION
────────────────────────────
1. GA4 → Admin → Events
2. Find or create event (e.g. "generate_lead")
3. Toggle "Mark as conversion" ON

OR via custom event:
gtag('event', 'generate_lead', {
  'currency': 'EUR',
  'value': 50
});

STEP 2: IMPORT IN GOOGLE ADS
─────────────────────────────
1. Google Ads → Tools → Conversions
2. "+ New conversion action"
3. "Import" → "Google Analytics 4 properties"
4. Select linked GA4 property
5. Check conversions you want to import
6. Configure:
   ├── Conversion name (optionally adjust)
   ├── Goal category: Lead, Purchase, etc.
   ├── Value: Use value from GA4 / Fixed value
   ├── Count: One (leads) / Every (sales)
   └── Attribution model: Data-driven

STEP 3: PRIMARY VS SECONDARY
─────────────────────────────
□ Primary: Used for bidding optimization
□ Secondary: Only for observation

TIP: Start with secondary, promote to primary
     after validation (1-2 weeks of data)

SYNC TIMING:
────────────
□ Conversions sync every 4-6 hours
□ Up to 24 hours delay possible
□ Historical data: not retroactive
```



## GA4 Audiences to Google Ads

### Audience Export Setup

```
EXPORTING GA4 AUDIENCES TO GOOGLE ADS
══════════════════════════════════════

ADVANTAGES:
───────────
□ Based on site behavior (not just ad clicks)
□ Complex conditions (sequences, exclusions)
□ Predictive audiences (likely to purchase)
□ Automatic sync

STEP 1: CREATE AUDIENCE IN GA4
───────────────────────────────
1. GA4 → Admin → Audiences → "New audience"
2. Choose template or "Create custom audience"

AUDIENCE EXAMPLES:

HIGH-VALUE USERS:
├── Condition: transaction_value > $100
├── In last: 30 days
└── Use: High-value remarketing

CART ABANDONERS:
├── Condition 1: add_to_cart (include)
├── Condition 2: purchase (exclude)
├── In last: 7 days
└── Use: Cart recovery campaigns

ENGAGED USERS (NO CONVERSION):
├── Condition 1: session_duration > 120s
├── Condition 2: page_view count > 3
├── Condition 3: form_submit (exclude)
├── In last: 30 days
└── Use: Consideration remarketing

PREDICTIVE AUDIENCE:
├── Template: "Likely 7-day purchasers"
├── Google ML-based
├── Requires: 1000+ purchases, 1000+ non-purchases
└── Use: Acquisition lookalike

STEP 2: ENABLE GOOGLE ADS EXPORT
─────────────────────────────────
During audience creation:
□ "Enable personalized advertising" = ON

This enables automatic sync to Google Ads

STEP 3: VERIFICATION IN GOOGLE ADS
───────────────────────────────────
1. Google Ads → Tools → Audience Manager
2. Filter: "GA4" or "[GA4 property name]"
3. Check:
   ├── List size (must be >1000 for targeting)
   ├── Status: "Active"
   └── Last updated: Recent

AUDIENCE SIZING:
────────────────
┌─────────────────────────────────────────────────────────────────┐
│ Audience Size │ Search Remarketing │ Display/YouTube             │
├───────────────┼────────────────────┼───────────────────────────┤
│ <100          │ Too small          │ Too small                  │
│ 100-1,000     │ Usable             │ Too small                  │
│ 1,000-10,000  │ Good               │ Usable                    │
│ 10,000+       │ Excellent          │ Good                      │
│ 100,000+      │ Excellent          │ Excellent                 │
└───────────────┴────────────────────┴───────────────────────────┘

WARNING: Audiences smaller than minimums will not populate
```

### Predictive Audiences

```
GA4 PREDICTIVE AUDIENCES
════════════════════════

AVAILABLE PREDICTIVE AUDIENCES:
───────────────────────────────

1. LIKELY TO PURCHASE (7-DAY)
   ├── Users likely to purchase within 7 days
   ├── Requires: 1000+ purchases in 28 days
   ├── Use: Bid boost, aggressive targeting
   └── Combine with: cart abandoners, high-intent

2. LIKELY TO CHURN
   ├── Users likely not to return
   ├── Requires: 1000+ active + 1000+ churned users
   ├── Use: Retention campaigns, win-back
   └── Combine with: high-value customers

3. PREDICTED REVENUE (Top X%)
   ├── Highest predicted revenue users
   ├── Requires: Revenue data, sufficient volume
   ├── Use: VIP targeting, premium campaigns
   └── Combine with: cross-sell audiences

SETUP:
──────
1. GA4 → Admin → Audiences
2. "New audience" → "Predictive"
3. Choose predictive metric
4. Set threshold (e.g. top 20%)
5. Enable Google Ads export

BEST PRACTICES:
───────────────
□ Combine predictive + behavioral
  E.g.: "Likely to purchase" + "Viewed product page"

□ Exclude converters
  Predictive audiences may contain recent buyers

□ Adjust bids based on score
  Higher predicted value = higher bid

□ Monitor performance separately
  Predictive vs non-predictive segments
```

## Campaign URL Tagging

### UTM Parameter Strategy

```
UTM TAGGING STRATEGY
═════════════════════

WHEN TO USE UTM:
────────────────
□ Alongside auto-tagging (for GA4 custom reports)
□ Cross-platform tracking (Meta, LinkedIn, etc.)
□ Email campaigns
□ Organic social posts
□ Partner/affiliate links

UTM PARAMETERS:
───────────────
┌───────────────────┬────────────────────────────────────────────┐
│ Parameter         │ Description                                │
├───────────────────┼────────────────────────────────────────────┤
│ utm_source        │ Platform (google, facebook, newsletter)    │
│ utm_medium        │ Type (cpc, display, email, social)        │
│ utm_campaign      │ Campaign name                              │
│ utm_term          │ Keyword (auto-filled by Google Ads)       │
│ utm_content       │ Ad variant (for A/B testing)              │
└───────────────────┴────────────────────────────────────────────┘

GOOGLE ADS UTM TEMPLATE (Account Level):
────────────────────────────────────────
Settings → Account settings → Tracking → Final URL suffix

{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={_campaign}&utm_content={_adgroupname}&utm_term={keyword}

OR with ValueTrack parameters:
{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={creative}&utm_term={keyword}

VALUETRACK PARAMETERS REFERENCE:
────────────────────────────────
{campaignid}    - Campaign ID
{campaign}      - Campaign name (use {_campaign} for custom)
{adgroupid}     - Ad group ID
{creative}      - Ad ID
{keyword}       - Triggered keyword
{device}        - Device (m, t, c)
{matchtype}     - Match type (e, p, b)
{network}       - Network (g=Search, s=Search partner, d=Display)
{placement}     - Display placement URL
{loc_physical}  - Physical location ID
{loc_interest}  - Location of interest ID

NAMING CONVENTIONS:
───────────────────
Campaign names (consistent format):
├── [Platform]_[Type]_[Target]_[Date]
├── Example: Google_Search_US_LeadGen_2025Q1
└── No spaces, use underscores

utm_content for A/B testing:
├── v1, v2, v3
├── headline-a, headline-b
└── image-product, image-lifestyle
```

### Cross-Platform Tracking

```
CROSS-PLATFORM TRACKING WITH GA4
═════════════════════════════════

ALL TRAFFIC TO GA4:
───────────────────

GOOGLE ADS:
├── Auto-tagging: gclid captured
├── Plus UTM: for custom reports
└── Linked: conversions sync back

META ADS:
├── UTM tagging required
├── utm_source=facebook or meta
├── utm_medium=paid_social
└── Optional: capture fbclid parameter

LINKEDIN ADS:
├── UTM tagging required
├── utm_source=linkedin
├── utm_medium=paid_social
└── LinkedIn insight tag for conversions

MICROSOFT ADS:
├── Auto-tagging possible (msclkid)
├── Plus UTM: for GA4
└── Link: Microsoft Ads ↔ GA4 also possible

EMAIL:
├── utm_source=newsletter or [email_name]
├── utm_medium=email
├── utm_campaign=[campaign_name]
└── utm_content=[variant]

UNIFIED REPORTING IN GA4:
─────────────────────────
1. Reports → Acquisition → Traffic acquisition
2. Dimension: Session source/medium
3. Filter: Medium = cpc, paid_social, email

CREATE CROSS-PLATFORM REPORT:
─────────────────────────────
1. Explore → Free form
2. Rows: Session source, Session medium
3. Values: Sessions, Conversions, Revenue
4. Filter: Paid channels only

ATTRIBUTION COMPARISON:
───────────────────────
1. Advertising → Attribution paths
2. Compare: First click vs Last click vs Data-driven
3. See: How channels work together
```

## GA4 Reports for Google Ads

### Custom Reports Setup

```
GA4 REPORTS FOR GOOGLE ADS PERFORMANCE
═══════════════════════════════════════

REPORT 1: GOOGLE ADS CAMPAIGN PERFORMANCE
──────────────────────────────────────────
Location: Reports → Acquisition → Google Ads campaigns

Metrics available:
├── Sessions
├── Engaged sessions
├── Users
├── Conversions
├── Revenue
└── Engagement rate

Customize:
1. Click "Customize report" (pencil icon)
2. Add metrics: Avg engagement time, Bounce rate
3. Add dimensions: Landing page, Device category

REPORT 2: GOOGLE ADS KEYWORDS
──────────────────────────────
Location: Reports → Acquisition → Google Ads keywords

Shows: Search query data (with keyword matching)

REPORT 3: CUSTOM EXPLORATION - FUNNEL
──────────────────────────────────────
1. Explore → Funnel exploration
2. Steps:
   ├── Step 1: session_start (from: google/cpc)
   ├── Step 2: product_view OR page_view
   ├── Step 3: add_to_cart
   └── Step 4: purchase
3. Segment: Google Ads campaigns

REPORT 4: CUSTOM EXPLORATION - PATH
────────────────────────────────────
1. Explore → Path exploration
2. Starting point: google/cpc session
3. See: User journey after ad click
4. Identify: Drop-off points, key pages

REPORT 5: LANDING PAGE PERFORMANCE
───────────────────────────────────
1. Reports → Engagement → Pages and screens
2. Filter: Session source = google
3. Metrics: Engagement rate, Conversions
4. Identify: Best/worst performing landing pages
```

### Linking Google Ads Cost Data

```
COST DATA IN GA4
════════════════

WHAT IS AUTOMATICALLY AVAILABLE:
─────────────────────────────────
After linking, GA4 shows:
├── Google Ads clicks
├── Google Ads impressions
├── Google Ads cost
└── Google Ads conversions (e.g. clicks to GA4 conversions)

WHERE TO FIND:
──────────────
1. Reports → Acquisition → Acquisition overview
2. Card: "Google Ads campaigns"
3. Metrics: Cost, Clicks, Impressions

COST DATA IMPORT FOR OTHER PLATFORMS:
─────────────────────────────────────
GA4 also supports cost data import for:
├── Meta Ads
├── Microsoft Ads
├── Display & Video 360
└── Search Ads 360

Setup:
1. Admin → Data import
2. "+ Create data source"
3. "Cost data"
4. Upload CSV or connect API

CSV FORMAT:
───────────
date,utm_source,utm_medium,utm_campaign,impressions,clicks,cost
2025-01-15,facebook,paid_social,spring_sale,10000,250,125.00

CALCULATED METRICS:
───────────────────
After cost import you can calculate:
├── CPA = Cost / Conversions
├── ROAS = Revenue / Cost
└── CPM = (Cost / Impressions) * 1000
```






## Output: GA4 Integration Checklist

```markdown
# GA4 Integration Implementation Checklist

## Account Information
- **Google Ads Account ID:** [ID]
- **GA4 Property ID:** [ID]
- **Website:** [URL]

## Phase 1: Basic Linking
- [ ] Admin access to both GA4 and Google Ads
- [ ] Accounts linked (GA4 → Google Ads links)
- [ ] Auto-tagging enabled in Google Ads
- [ ] Verify link shows "Active" in both platforms

## Phase 2: Conversion Import
- [ ] Key events marked as conversions in GA4
- [ ] Conversions imported to Google Ads
- [ ] Conversion counting configured (One/Every)
- [ ] Attribution model set to Data-driven
- [ ] Primary/Secondary status set correctly
- [ ] Test conversion tracked successfully

### Conversions to Import:
| GA4 Event | Google Ads Name | Goal Category | Count |
|-----------|-----------------|---------------|-------|
| [event]   | [name]          | [category]    | One   |

## Phase 3: Audience Setup
- [ ] Remarketing audiences created in GA4
- [ ] Audiences enabled for Google Ads export
- [ ] Audiences visible in Google Ads Audience Manager
- [ ] Audience size meets minimums (1000+ for Search)

### Audiences to Create:
| Audience Name | Definition | Expected Size |
|---------------|------------|---------------|
| All Visitors 30d | All users, 30 days | [size] |
| Converters | purchase event | [size] |
| Cart Abandoners | add_to_cart excl purchase | [size] |

## Phase 4: UTM Strategy
- [ ] UTM template set at account level
- [ ] ValueTrack parameters configured
- [ ] Naming conventions documented
- [ ] Test URLs verified

## Phase 5: Reporting Setup
- [ ] Google Ads campaign report customized
- [ ] Landing page performance exploration created
- [ ] Funnel exploration for ad traffic created
- [ ] Cost data displaying correctly

## Validation Checklist
- [ ] Conversions match within 15% between platforms
- [ ] Audiences populating as expected
- [ ] No "unassigned" traffic from Google Ads
- [ ] Attribution model consistent

## Troubleshooting Reference
- Conversion discrepancy >20%: Check attribution models
- Audience not syncing: Verify personalized advertising enabled
- Missing Google Ads data: Check linking status
```
