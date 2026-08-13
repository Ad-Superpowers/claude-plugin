---
name: ga4-audience-builder
description: "This skill should be used when the user asks to \"build GA4 audiences\", \"create custom segments\", \"set up audience targeting\", or mentions \"sequential audiences\", \"user segments\", or \"remarketing audiences in GA4\". Do NOT use for: audience exclusions (use ga4-audience-exclusions), predictive audiences (use ga4-predictive-audiences), or exporting audiences to Google Ads (use ga4-remarketing-setup)."
---
# GA4 Audience Builder Guide

Complete guide for building powerful custom audiences in Google Analytics 4 for remarketing and analysis.

## Quick Decision Tree

```
GA4 AUDIENCE BUILDER FLOW
│
├─► WHICH TYPE OF AUDIENCE?
│   ├─► Behavior-based
│   │   └─► Use events + parameters
│   │       └─► Example: "Users who viewed product but did not purchase"
│   │
│   ├─► User Property based
│   │   └─► Demographics, lifetime value, acquisition
│   │       └─► Example: "High-value customers (LTV > €500)"
│   │
│   ├─► Sequential (Journey)
│   │   └─► Steps in order
│   │       └─► Example: "Homepage → Category → Product → NO Purchase"
│   │
│   └─► Predictive (ML)
│       └─► See: ga4-predictive-audiences skill
│
├─► MEMBERSHIP DURATION?
│   ├─► Short (1-7 days)
│   │   └─► Cart abandoners, recent visitors
│   │
│   ├─► Medium (8-30 days)
│   │   └─► Product interest, engaged users
│   │
│   └─► Long (30-540 days)
│       └─► Customer loyalty, seasonal shoppers
│
└─► EXPORT NEEDED?
    ├─► Google Ads remarketing
    │   └─► See: ga4-remarketing-setup skill
    │
    └─► GA4 analysis only
        └─► No export configuration needed
```

## Audience Types Overview

```
GA4 AUDIENCE TYPES
===================

┌───────────────────┬────────────────────────────────────────────────────┐
│ Type              │ Use Case                                           │
├───────────────────┼────────────────────────────────────────────────────┤
│ Static Conditions │ Simple if/then rules                               │
│                   │ "Users with event X"                               │
├───────────────────┼────────────────────────────────────────────────────┤
│ Dynamic           │ Real-time membership updates                       │
│                   │ "Users who purchased last week"                    │
├───────────────────┼────────────────────────────────────────────────────┤
│ Sequential        │ Ordered steps (THEN/FOLLOWED BY)                   │
│                   │ "Viewed product → Added to cart → Did NOT buy"     │
├───────────────────┼────────────────────────────────────────────────────┤
│ Exclusion         │ Exclude certain users                              │
│                   │ "All visitors EXCEPT converters"                   │
├───────────────────┼────────────────────────────────────────────────────┤
│ Predictive        │ ML-based (purchase/churn probability)              │
│                   │ "Likely 7-day purchasers"                          │
└───────────────────┴────────────────────────────────────────────────────┘
```

## Creating an Audience: Step by Step

### Step 1: Navigate to Audience Builder

```
LOCATION: Admin → Property → Audiences → New audience

OPTIONS AT CREATION:
┌────────────────────────┬────────────────────────────────────────────┐
│ Option                 │ When to Use                                │
├────────────────────────┼────────────────────────────────────────────┤
│ Create a custom        │ Full control, custom conditions            │
│ audience               │ (Recommended for specific use cases)       │
├────────────────────────┼────────────────────────────────────────────┤
│ Use a reference        │ Start with GA4 template                   │
│ (Suggested audiences)  │ (Good for inspiration)                    │
├────────────────────────┼────────────────────────────────────────────┤
│ Create audience from   │ Start from existing Exploration           │
│ exploration            │ (Handy for analysis → action)             │
└────────────────────────┴────────────────────────────────────────────┘
```

### Step 2: Configure Conditions

```
AUDIENCE CONDITIONS
====================

CONDITION TYPES:
────────────────
├── Include users when: (AND/OR logic)
│   ├── Event (event_name = X)
│   ├── Event parameter (event_param = Y)
│   ├── User property (user_property = Z)
│   ├── First user (acquisition source/medium)
│   └── Device/Geo (platform, country, city)
│
└── Exclude users when: (Filter OUT)
    └── Same options as include

AVAILABLE OPERATORS:
┌─────────────────────┬────────────────────────────────────────────────┐
│ Operator            │ Example                                        │
├─────────────────────┼────────────────────────────────────────────────┤
│ equals              │ event_name = purchase                          │
├─────────────────────┼────────────────────────────────────────────────┤
│ does not equal      │ page_location != /thank-you                    │
├─────────────────────┼────────────────────────────────────────────────┤
│ contains            │ page_title contains "Product"                  │
├─────────────────────┼────────────────────────────────────────────────┤
│ begins with         │ page_path begins with /shop/                   │
├─────────────────────┼────────────────────────────────────────────────┤
│ ends with           │ page_path ends with /checkout                  │
├─────────────────────┼────────────────────────────────────────────────┤
│ matches regex       │ page_path matches regex ^/product/[0-9]+$      │
├─────────────────────┼────────────────────────────────────────────────┤
│ > / < / >= / <=     │ ltv > 100 (for numeric values)                 │
├─────────────────────┼────────────────────────────────────────────────┤
│ in list             │ country in list [NL, BE, DE]                   │
└─────────────────────┴────────────────────────────────────────────────┘
```

### Step 3: Configure Scoping

```
AUDIENCE SCOPING
=================

WHAT IS SCOPING:
├── Determines at which level conditions are evaluated
├── Critical for correct audience definition
└── Wrong scoping = wrong users in audience

SCOPE LEVELS:
┌─────────────────┬────────────────────────────────────────────────────┐
│ Scope           │ Meaning                                            │
├─────────────────┼────────────────────────────────────────────────────┤
│ Across all      │ Condition ever true within membership window       │
│ sessions        │ "User did this at any point in the last X days"    │
│                 │ └─► MOST COMMONLY USED scope                       │
├─────────────────┼────────────────────────────────────────────────────┤
│ Within same     │ Condition true within a single session             │
│ session         │ "User did this in the same session"                │
│                 │ └─► For session-specific journeys                  │
├─────────────────┼────────────────────────────────────────────────────┤
│ Within same     │ Condition true within a single event               │
│ event           │ "This event had these parameters"                  │
│                 │ └─► For specific event combinations                │
└─────────────────┴────────────────────────────────────────────────────┘

EXAMPLE OF THE DIFFERENCE:
───────────────────────────
"User viewed product AND added to cart"

Across all sessions:
└─► User who ever viewed a product AND ever added something
    (Could be different products!)

Within same session:
└─► User who viewed a product AND added to cart in the SAME session
    (More relevant for cart abandonment)

Within same event:
└─► Not logical for this example (2 events)
```

### Step 4: Membership Duration

```
MEMBERSHIP DURATION SETTINGS
==============================

WHAT IT IS:
├── How long user stays in audience after last qualifying action
├── Max 540 days (Google Ads limit)
└── Choose based on customer journey and campaign goal

RECOMMENDATIONS PER USE CASE:
┌─────────────────────────┬────────────┬─────────────────────────────────┐
│ Use Case                │ Duration   │ Reason                          │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Cart abandonment        │ 7-14 days  │ Short purchase intent window    │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Product viewers         │ 14-30 days │ Medium interest window          │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Recent customers        │ 30-90 days │ Cross-sell/upsell window        │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ All customers           │ 180-540 d  │ Longer loyalty period           │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Seasonal shoppers       │ 365 days   │ Seasonal re-activation          │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ High-value customers    │ 540 days   │ Maximum retention for VIPs      │
└─────────────────────────┴────────────┴─────────────────────────────────┘

IMPORTANT:
├── Shorter duration = more relevant targeting
├── Longer duration = larger audience size
├── Google Ads has max 540 days
└── Choose based on average sales cycle
```

## Sequential Audiences

```
SEQUENTIAL AUDIENCES
=====================

WHAT IT IS:
├── Audiences based on order of actions
├── Use "is followed by" or "is indirectly followed by"
└── Perfect for customer journey targeting

SYNTAX:
────────
Step 1: [First condition]
        │
        ├─► is followed by (directly next action)
        │   └─► "Immediately after"
        │
        └─► is indirectly followed by (somewhere later)
            └─► "At some point after"
        │
Step 2: [Second condition]
        │
        ├─► (repeat for more steps)
        │
Step N: [Final condition]

EXAMPLE: CART ABANDONERS (SEQUENTIAL)
──────────────────────────────────────
Step 1: event_name = view_item
        is indirectly followed by
Step 2: event_name = add_to_cart
        AND EXCLUDE
Step 3: event_name = purchase

Meaning: "Users who viewed a product, then added to cart,
         but did NOT purchase"

EXAMPLE: CHECKOUT ABANDONERS
─────────────────────────────
Step 1: event_name = begin_checkout
        is indirectly followed by
Step 2: event_name = add_payment_info
        AND EXCLUDE
Step 3: event_name = purchase

Meaning: "Users who started checkout, entered payment info,
         but did not complete"

TIME CONSTRAINTS:
─────────────────
├── "within X time" - Step must follow within X time
│   └─► Example: add_to_cart within 30 minutes of view_item
│
└── Without constraint - Anytime in membership window
```

## Practical Audience Templates

```
AUDIENCE TEMPLATES FOR ADVERTISERS
====================================

1. HIGH-INTENT NON-CONVERTERS
─────────────────────────────
Name: "High Intent - No Purchase"
Conditions:
├── Include: event_name = add_to_cart (count >= 2)
├── Include: session_duration > 180 (3+ minutes)
└── Exclude: event_name = purchase
Duration: 14 days
Use case: High purchase intent, needs extra push

2. RECENT CUSTOMERS (CROSS-SELL)
────────────────────────────────
Name: "Recent Buyers - 30 Days"
Conditions:
├── Include: event_name = purchase
└── Timeframe: Last 30 days
Duration: 30 days
Use case: Cross-sell campaigns

3. HIGH-VALUE CUSTOMERS
────────────────────────
Name: "VIP Customers LTV 500+"
Conditions:
├── Include: LTV (user property) > 500
└── Or: purchase value sum > 500
Duration: 540 days
Use case: VIP treatment, loyalty campaigns

4. ENGAGED NON-CONVERTERS
──────────────────────────
Name: "Engaged Visitors - No Purchase"
Conditions:
├── Include: session_count >= 3
├── Include: page_views >= 10
└── Exclude: event_name = purchase
Duration: 30 days
Use case: Retargeting engaged browsers

5. CATEGORY INTEREST
─────────────────────
Name: "[Category] Viewers"
Conditions:
├── Include: page_path contains /category/[name]/
├── Or: item_category = [name]
└── Exclude: event_name = purchase (optional)
Duration: 14 days
Use case: Category-specific remarketing

6. LAPSED CUSTOMERS
────────────────────
Name: "Lapsed Customers 90+ Days"
Conditions:
├── Include: event_name = purchase
├── Timeframe: 90-365 days ago (NOT last 90 days)
└── Exclude: purchase in last 90 days
Duration: 275 days
Use case: Win-back campaigns

7. EMAIL SUBSCRIBERS NON-BUYERS
────────────────────────────────
Name: "Newsletter - No Purchase"
Conditions:
├── Include: event_name = sign_up OR newsletter_subscribe
└── Exclude: event_name = purchase
Duration: 90 days
Use case: Email subscriber conversion
```

## Best Practices

```
DO's ✅
═══════
├── Use clear, descriptive audience names
│   └─► "Cart_Abandon_14d_ExclPurchase" vs "Audience 1"
│
├── Document audience logic in description
│   └─► Add explanation of why these conditions
│
├── Start with broader audiences, narrow down later
│   └─► Too specific = too few users
│
├── Test audience size before activation
│   └─► <1000 users = possibly too small for Google Ads
│
├── Use exclusions to prevent overlap
│   └─► Exclude converters from prospecting audiences
│
├── Combine with Predictive Audiences
│   └─► "Likely Purchasers" + "Cart Abandoners" = High priority
│
└── Review audiences monthly
    └─► Remove inactive/small audiences

DON'Ts
═══════
├── Create too many audiences (>50 becomes unmanageable)
│   └─► Focus on 10-20 core audiences
│
├── Create audiences without a clear campaign goal
│   └─► First: what do I want to achieve? Then: which audience?
│
├── Forget to add exclusions
│   └─► Retargeting converters with prospecting ads
│
├── Set too short membership duration for long sales cycles
│   └─► B2B: 30-90 days, not 7 days
│
├── Build on only one data point
│   └─► Combine multiple signals for better targeting
│
└── Never review audiences on performance
    └─► Poor ROAS? Adjust or pause audience
```

## Troubleshooting

```
TROUBLESHOOTING GUIDE
======================

PROBLEM: Audience size = 0
───────────────────────────
Causes:
├── Conditions too restrictive
├── Event does not exist or is misspelled
├── Timeframe too short
├── Data not yet processed
└── Wrong scoping

Solution:
├── Check event/parameter names in DebugView
├── Broaden conditions (fewer AND, more OR)
├── Wait 24-48 hours for data processing
├── Use Exploration to count users first
└── Test each condition separately

PROBLEM: Audience not available in Google Ads
──────────────────────────────────────────────
Causes:
├── Google Ads link not active
├── "Enable personalized ads" not on
├── Audience too small (<1000 users)
├── Not yet synchronized (24-48 hours)
└── Policy violation (sensitive categories)

Solution:
├── Check Admin → Product Links → Google Ads
├── Verify "Personalized advertising" toggle
├── Wait for sufficient audience volume
├── Check Google Ads policy compliance
└── Verify Google Signals is enabled

PROBLEM: Audience is not growing
─────────────────────────────────
Causes:
├── Events are not being triggered
├── Filters too restrictive
├── Consent mode blocking users
└── Membership duration too short

Solution:
├── Verify event tracking in DebugView
├── Review and broaden conditions
├── Check consent rates
├── Extend membership duration

PROBLEM: Too much overlap between audiences
────────────────────────────────────────────
Causes:
├── No exclusions configured
├── Conditions not mutually exclusive
└── Audience hierarchy not thought through

Solution:
├── Create exclusion audiences
├── Use "AND NOT" conditions
├── Design audience architecture with tiers
└── Prioritize: converters → high-intent → general
```

## Output: Audience Builder Recommendation Template

```markdown
# GA4 Audience Recommendation

## Audience Overview
- **Name:** [Audience name]
- **Goal:** [Remarketing/Analysis/Export]
- **Expected size:** [Estimate]
- **Membership duration:** [X days]

## Audience Configuration

### Include Conditions
| # | Type | Condition | Scope |
|---|------|-----------|-------|
| 1 | Event | [event_name = X] | [Across all sessions] |
| 2 | Parameter | [param = Y] | [Within same event] |
| 3 | User Property | [property = Z] | [Across all sessions] |

### Exclude Conditions
| # | Type | Condition | Reason |
|---|------|-----------|--------|
| 1 | Event | [event_name = purchase] | Exclude converters |

### Sequential Steps (if applicable)
```
Step 1: [First action]
        │ is indirectly followed by
Step 2: [Second action]
        │ AND EXCLUDE
Step 3: [Action to exclude]
```

## Export Configuration
- **Google Ads:** [Yes/No]
- **Display & Video 360:** [Yes/No]
- **Search Ads 360:** [Yes/No]

## Campaign Use Cases
1. [First campaign type - description]
2. [Second campaign type - description]
3. [Third campaign type - description]

## Monitoring
- **Review frequency:** [Weekly/Monthly]
- **KPIs:** [Audience size, Conversion rate, ROAS]
- **Alerts:** [If size <X or >Y]

## Notes
[Any additional remarks or context]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, pull segment sizes to validate audience eligibility before building:

```python
# Check user counts per key segment to estimate audience sizes
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["totalUsers", "sessions"],
    dimensions=["sessionDefaultChannelGroup"],
    start_date="30daysAgo",
    end_date="today"
)
```

Use this to check if there are enough users in each segment to meet platform minimums (Google Ads: 1,000 users, Meta: 100). Small segments need broader definitions or longer lookback windows.
