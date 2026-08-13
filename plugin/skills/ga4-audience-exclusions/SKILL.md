---
name: ga4-audience-exclusions
description: "This skill should be used when the user asks to \"exclude converters from campaigns\", \"set up audience exclusions\", \"prevent audience overlap\", or mentions \"frequency capping\", \"purchaser exclusions\", or \"budget waste from overlap\". Do NOT use for: building audiences (use ga4-audience-builder), predictive audiences (use ga4-predictive-audiences), or remarketing export setup (use ga4-remarketing-setup)."
---
# GA4 Audience Exclusions Guide

Complete guide for effectively excluding audiences and frequency capping to maximize advertising budget.

## Exclusion Types Overview

```
EXCLUSION STRATEGIES
=====================

┌─────────────────────┬────────────────────────────────────────────────────┐
│ Type                │ Description                                        │
├─────────────────────┼────────────────────────────────────────────────────┤
│ GA4 Built-in        │ "Exclude users when" in audience builder           │
│ Exclusion           │ Makes audience pre-filtered                        │
│                     │ └─► Best for: Remarketing audiences                │
├─────────────────────┼────────────────────────────────────────────────────┤
│ Google Ads          │ Separate exclusion audience added to               │
│ Campaign Exclusion  │ campaign settings                                  │
│                     │ └─► Best for: Prospecting campaigns                │
├─────────────────────┼────────────────────────────────────────────────────┤
│ Negative Audience   │ "Do not show ads to this audience"                 │
│ Targeting           │ Campaign-level or account-level                    │
│                     │ └─► Best for: Account-wide exclusions              │
├─────────────────────┼────────────────────────────────────────────────────┤
│ Frequency Capping   │ Soft exclusion via impression limits               │
│                     │ User sees max X ads per day/week                   │
│                     │ └─► Best for: Display/YouTube                      │
└─────────────────────┴────────────────────────────────────────────────────┘
```

## Core Exclusion Audiences

```
ESSENTIAL EXCLUSION AUDIENCES
===============================

1. RECENT PURCHASERS (MUST-HAVE)
─────────────────────────────────
Name: "Purchasers - Last 30 Days"
Condition: event_name = purchase (in last 30 days)
Duration: 30 days

Why exclude:
├── Prevent waste on recently converted users
├── Better user experience (no repetitive ads)
└── Focus acquisition budget on new customers

Exclude FROM:
├── All acquisition campaigns
├── Prospecting campaigns
└── Generic remarketing

Do NOT exclude from:
├── Cross-sell campaigns (different products)
├── Loyalty/VIP campaigns
└── Replenishment reminders (after X days)

2. ALL CONVERTERS (LIFETIME)
─────────────────────────────
Name: "All Purchasers - Lifetime"
Condition: event_name = purchase (any time)
Duration: 540 days (maximum)

Why:
├── Acquisition efficiency (focus on new customers)
├── Separate campaigns for existing vs new customers
└── Different messaging/offers per segment

Exclude FROM:
├── Pure acquisition campaigns
├── First-time buyer promos
└── New customer discounts

3. LEADS (RECENT SUBMITTERS)
─────────────────────────────
Name: "Leads - Last 14 Days"
Condition: event_name = generate_lead OR form_submit
Duration: 14 days

Why:
├── Already in sales funnel
├── Nurturing via email, not ads
└── Prevent over-exposure

Exclude FROM:
├── Lead generation campaigns
├── Demo request campaigns
└── Generic awareness

4. HIGH-VALUE CUSTOMERS (PROTECT)
──────────────────────────────────
Name: "VIP Customers - LTV 500+"
Condition: user_ltv > 500 OR purchase_count >= 5
Duration: 540 days

Why exclude from certain campaigns:
├── These customers return organically
├── No discount ads needed
├── Protect relationship

Exclude FROM:
├── Discount campaigns
├── Win-back with large discounts
└── Aggressive retargeting

5. CART ABANDONERS (ALREADY TARGETED)
──────────────────────────────────────
Name: "Active Cart Abandoners - 14d"
Condition: add_to_cart (last 14 days) EXCLUDE purchase
Duration: 14 days

Why exclude:
├── These already receive cart abandonment emails/ads
├── Prevent double exposure
└── Budget efficiency

Exclude FROM:
├── General product remarketing
├── Awareness campaigns
└── Top-of-funnel content

6. BOUNCED VISITORS (LOW VALUE)
────────────────────────────────
Name: "Bouncers - Single Page"
Condition: session_duration < 10s OR page_views = 1
Duration: 7 days

Why exclude:
├── Low intent, likely accidental traffic
├── Prevent waste on low-quality traffic
└── Better overall ROAS

Exclude FROM:
├── Remarketing campaigns
├── Consideration campaigns
└── High-intent targeting
```

## GA4 Exclusion Implementation

### Method 1: Built-in Audience Exclusions

```
GA4 AUDIENCE BUILDER EXCLUSIONS
=================================

LOCATION: Admin → Audiences → New audience

SETUP:
──────
1. Build your "Include" conditions first
   ├── E.g.: event add_to_cart (last 7 days)

2. Click "Add new condition group"

3. Toggle to "Exclude users when"
   ├── E.g.: event purchase (last 7 days)

4. Result: Cart abandoners WITHOUT converters

EXAMPLE: CART ABANDONERS EXCL PURCHASE
───────────────────────────────────────
Include users when:
├── Event: add_to_cart
├── In last: 7 days

Exclude users when:
├── Event: purchase
├── In last: 7 days

Duration: 7 days

EXAMPLE: ENGAGED VISITORS EXCL CONVERTERS
──────────────────────────────────────────
Include users when:
├── session_duration > 120
├── AND page_views >= 3

Exclude users when:
├── Event: purchase
├── OR Event: generate_lead

Duration: 14 days
```

### Method 2: Dedicated Exclusion Audiences

```
STANDALONE EXCLUSION AUDIENCES
================================

WHY SEPARATE AUDIENCES:
├── Reusable across campaigns
├── Easier to manage centrally
├── Consistent access in Google Ads
└── More flexible for different exclusion windows

EXCLUSION AUDIENCE NAMING CONVENTION:
──────────────────────────────────────
[Segment]_Exclude_[Timeframe]

Examples:
├── Purchasers_Exclude_30d
├── Leads_Exclude_14d
├── VIP_Exclude_Discounts
├── Bouncers_Exclude_7d
└── Complainers_Exclude_90d

SETUP IN GA4:
─────────────
1. Create audience with ONLY the to-be-excluded condition
2. Give clear name (Exclude prefix)
3. Export to Google Ads
4. Add as exclusion in campaigns

EXAMPLE AUDIENCES TO CREATE:
─────────────────────────────
Audience 1: "Purchasers_Exclude_30d"
├── Include: event purchase (last 30 days)
├── Duration: 30 days
└── Export: Google Ads

Audience 2: "Purchasers_Exclude_7d"
├── Include: event purchase (last 7 days)
├── Duration: 7 days
└── Export: Google Ads

Audience 3: "All_Converters_Lifetime"
├── Include: event purchase (any time)
├── Duration: 540 days
└── Export: Google Ads
```

## Google Ads Exclusion Implementation

```
GOOGLE ADS EXCLUSION SETUP
============================

CAMPAIGN-LEVEL EXCLUSIONS:
───────────────────────────
1. Go to Campaign → Settings → Audiences
2. Scroll to "Audience exclusions"
3. Click "Edit audience exclusions"
4. Browse → Your data → Website visitors (GA4)
5. Select exclusion audiences
6. Save

AD GROUP-LEVEL EXCLUSIONS:
───────────────────────────
1. Go to Ad Group → Audiences
2. Click "Exclusions" tab
3. "+ Add exclusion"
4. Select GA4 audiences
5. Save

ACCOUNT-LEVEL EXCLUSIONS:
──────────────────────────
For exclusions that apply EVERYWHERE:

1. Tools & Settings → Shared Library → Audience Manager
2. Audience lists → Create exclusion list
3. Add GA4 audiences to list
4. Apply list to campaigns

WHEN TO USE EACH LEVEL:
┌─────────────────┬────────────────────────────────────────────────────────┐
│ Level           │ When to Use                                            │
├─────────────────┼────────────────────────────────────────────────────────┤
│ Account-level   │ Universal exclusions (all converters from acquisition) │
├─────────────────┼────────────────────────────────────────────────────────┤
│ Campaign-level  │ Campaign-specific logic                                │
│                 │ (exclude cart abandoners from awareness)               │
├─────────────────┼────────────────────────────────────────────────────────┤
│ Ad Group-level  │ Granular product/category exclusions                   │
│                 │ (exclude category X buyers from category X ads)        │
└─────────────────┴────────────────────────────────────────────────────────┘
```

## Frequency Capping Strategies

```
FREQUENCY CAPPING GUIDE
=========================

WHAT IS FREQUENCY CAPPING:
├── Limit on how often a user sees your ads
├── Per day, week, or month
├── Only for Display, Video, Discovery
└── NOT available for Search

WHY CAPPING:
├── Prevent ad fatigue
├── Avoid negative brand perception
├── Better overall ROI
├── Respect user experience

FREQUENCY CAP SETTINGS:
┌─────────────────────┬─────────────────┬─────────────────────────────────┐
│ Audience Type       │ Recommended Cap │ Rationale                       │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ Cart abandoners     │ 5-7/day         │ High intent, reminder needed    │
│                     │ 15-20/week      │ But not overkill                │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ Product viewers     │ 3-5/day         │ Medium intent                   │
│                     │ 10-15/week      │ Gentle consideration nudge      │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ All visitors        │ 2-3/day         │ Lower intent                    │
│                     │ 7-10/week       │ Brand presence, not pushy       │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ YouTube remarketing │ 2-3/day         │ Video is intrusive              │
│                     │ 5-7/week        │ Quality over quantity           │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ Display prospecting │ 3-5/day         │ New users need exposure         │
│                     │ 15-20/week      │ But not bombardment             │
└─────────────────────┴─────────────────┴─────────────────────────────────┘

FREQUENCY CAP SETUP (GOOGLE ADS):
──────────────────────────────────
1. Campaign Settings → Additional settings
2. Frequency capping
3. Set: "Cap impressions at X per [day/week/month]"
4. Apply to: Campaign or Ad group

VIEWABLE FREQUENCY CAP:
────────────────────────
├── Cap on viewable impressions (50% pixels, 1+ second)
├── Better metric than total impressions
└── Available for Display campaigns

SEQUENTIAL MESSAGING WITH FREQUENCY:
──────────────────────────────────────
Combine frequency capping with sequential ads:

Day 1-2: Awareness creative (3x)
Day 3-5: Consideration creative (3x)
Day 6-7: Conversion creative (3x)

Setup via:
├── Separate ad groups with their own frequency caps
├── Exclude users after X days in each phase
└── Or: Campaign-level sequencing tools
```

## Audience Overlap Management

```
PREVENTING AUDIENCE OVERLAP
==============================

WHY OVERLAP IS PROBLEMATIC:
├── Same user sees ads from multiple campaigns
├── Budget competition with yourself
├── Inconsistent messaging
├── Higher than needed frequency
└── Difficult attribution analysis

OVERLAP DETECTION (GOOGLE ADS):
────────────────────────────────
1. Tools → Shared Library → Audience Manager
2. Audience insights → Overlap
3. Review which audiences overlap
4. Percentage overlap per audience pair

OVERLAP SOLUTIONS:

METHOD 1: HIERARCHICAL EXCLUSIONS
───────────────────────────────────
Prioritize audiences and exclude higher from lower:

Priority 1: Converters
├── No exclusions needed

Priority 2: Cart abandoners
├── Exclude: Converters

Priority 3: Product viewers
├── Exclude: Converters
├── Exclude: Cart abandoners

Priority 4: All visitors
├── Exclude: Converters
├── Exclude: Cart abandoners
├── Exclude: Product viewers

METHOD 2: MUTUALLY EXCLUSIVE AUDIENCES
────────────────────────────────────────
Build audiences that by definition do not overlap:

Audience A: "Purchasers only"
├── purchase = true

Audience B: "Cart abandon, no purchase"
├── add_to_cart = true
├── EXCLUDE: purchase = true

Audience C: "Product view only"
├── view_item = true
├── EXCLUDE: add_to_cart = true
├── EXCLUDE: purchase = true

METHOD 3: CAMPAIGN STRUCTURE
─────────────────────────────
Separate campaigns per funnel stage:

Campaign 1: "Acquisition" (new users)
├── Target: Optimized Targeting (expands from seed list)
├── Exclude: All site visitors

Campaign 2: "Consideration" (browsers)
├── Target: All visitors
├── Exclude: Cart abandoners + Converters

Campaign 3: "Conversion" (high intent)
├── Target: Cart abandoners
├── Exclude: Converters

Campaign 4: "Retention" (customers)
├── Target: All converters
├── Exclude: Recent converters (7d)
```

## Timing-Based Exclusions

```
TIMED EXCLUSION STRATEGIES
============================

WHY TIMED EXCLUSIONS:
├── Cross-sell after the right period
├── Replenishment reminders
├── Seasonal re-engagement
└── Prevent over-targeting after conversion

EXCLUSION WINDOWS PER USE CASE:
┌─────────────────────────┬───────────────┬─────────────────────────────────┐
│ Use Case                │ Exclude For   │ Then Include In                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ Recent purchase         │ 7-14 days     │ Cross-sell campaigns            │
│ (post-purchase glow)    │               │                                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ Subscription/membership │ Billing cycle │ Renewal reminders               │
│                         │ (30-60 days)  │                                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ High-ticket items       │ 30-90 days    │ Accessory/service campaigns     │
│                         │               │                                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ Consumables             │ Avg usage     │ Replenishment campaigns         │
│ (skincare, vitamins)    │ (30-60 days)  │                                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ Seasonal products       │ 330-365 days  │ Next season campaigns           │
│                         │               │                                 │
└─────────────────────────┴───────────────┴─────────────────────────────────┘

IMPLEMENTATION EXAMPLE:
────────────────────────

"Recent Buyers - Exclude 14d, Include After"

Audience 1: "Purchasers_Exclude_14d" (for exclusion)
├── purchase (last 14 days)
├── Duration: 14 days
└── Use as exclusion

Audience 2: "Purchasers_14d_to_90d" (for targeting)
├── purchase (last 90 days)
├── EXCLUDE: purchase (last 14 days)
├── Duration: 90 days
└── Use for cross-sell targeting
```

## Best Practices

```
DO's ✅
═══════
├── Start with core exclusions (purchasers, leads)
│   └─► This alone significantly improves ROAS
│
├── Use hierarchical exclusions
│   └─► Prevents overlap and budget waste
│
├── Maintain naming convention
│   └─► [Segment]_Exclude_[Timeframe] format
│
├── Review exclusion lists monthly
│   └─► Business changes require updates
│
├── Combine frequency caps with exclusions
│   └─► Belt-and-suspenders approach
│
├── Test exclusion impact
│   └─► Compare ROAS before/after
│
└── Document your exclusion strategy
    └─► Prevents confusion in team

DON'Ts
═══════
├── Exclude all converters permanently
│   └─► Missing cross-sell and retention opportunities
│
├── Exclude too aggressively
│   └─► Can limit reach too much
│
├── Forget to export exclusion audiences
│   └─► GA4 → Google Ads export needed
│
├── Only exclude at GA4 level
│   └─► Google Ads campaign exclusions also needed
│
├── Set frequency cap at 1/day
│   └─► Too low for effective remarketing
│
└── Never review exclusions
    └─► Outdated exclusions cost opportunities
```

## Output: Audience Exclusion Strategy Template

```markdown
# GA4 Audience Exclusion Strategy

## Exclusion Audiences Overview

### Core Exclusions (Must-Have)
| Audience Name | Condition | Duration | Export Status |
|---------------|----------|----------|---------------|
| Purchasers_Exclude_30d | purchase (30d) | 30 days | [✅/--] |
| Purchasers_Exclude_7d | purchase (7d) | 7 days | [✅/--] |
| All_Converters_Lifetime | purchase (all) | 540 days | [✅/--] |
| Leads_Exclude_14d | generate_lead (14d) | 14 days | [✅/--] |

### Secondary Exclusions
| Audience Name | Condition | Duration | Use Case |
|---------------|----------|----------|----------|
| [Name] | [Condition] | [X days] | [Use case] |
| [Name] | [Condition] | [X days] | [Use case] |

## Campaign Exclusion Matrix

| Campaign Type | Exclusions Applied |
|---------------|-------------------|
| Acquisition/Prospecting | All_Converters_Lifetime, Cart_Abandoners_14d |
| Consideration/Remarketing | Purchasers_Exclude_7d |
| Cart Recovery | Purchasers_Exclude_7d |
| Cross-sell | Purchasers_Exclude_7d (include older purchasers) |
| Retention/Loyalty | Non-purchasers excluded |

## Frequency Capping Strategy

| Audience | Daily Cap | Weekly Cap | Rationale |
|----------|-----------|------------|-----------|
| Cart abandoners | [X] | [X] | [Reason] |
| Product viewers | [X] | [X] | [Reason] |
| All visitors | [X] | [X] | [Reason] |
| YouTube remarketing | [X] | [X] | [Reason] |

## Overlap Prevention

### Audience Hierarchy
```
1. Converters (highest priority)
   └─ No exclusions
2. Cart Abandoners
   └─ Exclude: Converters
3. Product Viewers
   └─ Exclude: Converters, Cart Abandoners
4. Engaged Visitors
   └─ Exclude: All above
5. All Visitors
   └─ Exclude: All above
```

## Timed Exclusion Schedule

| Segment | Exclude For | Then Target With |
|---------|-------------|------------------|
| Recent purchasers | [X days] | [Campaign type] |
| [Segment] | [X days] | [Campaign type] |

## Implementation Checklist

### GA4
- [ ] Core exclusion audiences created
- [ ] All audiences exported to Google Ads
- [ ] Naming convention consistent

### Google Ads
- [ ] Campaign-level exclusions applied
- [ ] Account-level exclusion list created
- [ ] Frequency caps set
- [ ] Exclusion audiences verified in Audience Manager

## Monitoring

- **Review frequency:** [Weekly/Monthly]
- **Key metrics:** Overlap %, Reach impact, ROAS change
- **Alerts:** [When action needed]

## Notes
[Specific considerations or context]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, check exclusion audience sizes before applying them to campaigns:

```python
# Get converters and recent purchasers volume to size exclusion lists
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["totalUsers"],
    dimensions=["date"],
    start_date="30daysAgo",
    end_date="today"
)
```

If exclusion audience size is very small (<500 users), the impact on reach will be negligible — you can safely apply it. If it's large (>10% of total users), review whether exclusions are too aggressive and might be cutting into valid remarketing pool.
