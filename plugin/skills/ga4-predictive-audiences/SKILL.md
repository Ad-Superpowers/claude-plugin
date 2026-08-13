---
name: ga4-predictive-audiences
description: "This skill should be used when the user asks to \"set up predictive audiences\", \"find likely buyers\", \"predict churn\", or mentions \"purchase probability\", \"at-risk customers\", or \"ML audiences in GA4\". Do NOT use for: building standard audiences (use ga4-audience-builder), audience exclusions (use ga4-audience-exclusions), or remarketing export setup (use ga4-remarketing-setup)."
---
# GA4 Predictive Audiences Guide

Complete guide for using GA4's machine learning predictive audiences for advanced remarketing and Smart Bidding optimization.

## Predictive Metrics Overview

```
GA4 PREDICTIVE METRICS
======================

┌──────────────────────┬──────────────────────────────────────────────────┐
│ Metric               │ Description                                      │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Purchase probability │ Probability that an active user will purchase    │
│                      │ within the next 7 days                          │
│                      │ Range: 0-100%                                    │
│                      │ Updates: daily                                   │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Churn probability    │ Probability that an active user will churn       │
│                      │ (no activity) within the next 7 days            │
│                      │ Range: 0-100%                                    │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Predicted revenue    │ Expected revenue from a user in the next 28     │
│                      │ days, based on historical behavior              │
│                      │ In property currency                             │
└──────────────────────┴──────────────────────────────────────────────────┘

HOW IT WORKS:
─────────────
├── Google's ML models analyze user behavior
├── Trained on your property data
├── Requires minimum data volume to work
├── Updates daily for all eligible users
└── No extra implementation needed (as long as purchase event is correct)
```

## Eligibility Requirements

```
REQUIREMENTS FOR PREDICTIVE AUDIENCES
======================================

CRITICAL REQUIREMENTS - All must be met:

1. PURCHASE EVENTS
──────────────────
┌────────────────────────────────────────────────────────────────────────┐
│ Requirement: Minimum 1,000 purchasers AND 1,000 non-purchasers       │
│ in 7 days                                                             │
│                                                                        │
│ This means:                                                            │
│ ├── Active e-commerce tracking with purchase event                    │
│ ├── Sufficient traffic (typically >10,000 users/week)                 │
│ ├── Purchase event must be correctly configured                       │
│ └── Consistent data over time (no gaps)                               │
└────────────────────────────────────────────────────────────────────────┘

2. CHURN PREDICTIONS
────────────────────
┌────────────────────────────────────────────────────────────────────────┐
│ Requirement: Minimum 1,000 churners AND 1,000 active users           │
│ in 7 days                                                             │
│                                                                        │
│ This means:                                                            │
│ ├── Sufficient returning users                                        │
│ ├── Clear churn definition (7 days no activity)                       │
│ └── Consistent engagement tracking                                    │
└────────────────────────────────────────────────────────────────────────┘

3. GENERAL REQUIREMENTS
───────────────────────
┌─────────────────────────┬──────────────────────────────────────────────┐
│ Requirement             │ Details                                      │
├─────────────────────────┼──────────────────────────────────────────────┤
│ Model quality           │ Sufficient predictive power                  │
│                         │ Google evaluates automatically               │
├─────────────────────────┼──────────────────────────────────────────────┤
│ Sustained data          │ Consistent volume over 28+ days              │
│                         │ No large gaps in data                        │
├─────────────────────────┼──────────────────────────────────────────────┤
│ Purchase event params   │ Correct value and currency parameters        │
│                         │ Transaction ID for deduplication             │
├─────────────────────────┼──────────────────────────────────────────────┤
│ User identification     │ Consistent user_id or client_id              │
│                         │ Cross-device tracking helps                  │
└─────────────────────────┴──────────────────────────────────────────────┘

CHECKING ELIGIBILITY:
────────────────────
Location: Admin → Audiences → New audience → Predictive
├── Green checkmark = Eligible
├── Yellow warning = Almost eligible
└── Grey = Not eligible (hover for reason)
```

## Creating Predictive Audiences

### Step 1: Verify Eligibility

```
ELIGIBILITY CHECK
=================

LOCATION: Admin → Audiences → New audience → Predictive

WHAT YOU SEE:
┌──────────────────────────────────────────────────────────────────────┐
│ Predictive audiences                                                 │
│                                                                      │
│ ✅ Likely 7-day purchasers                    [Create audience]     │
│    Users with >X% probability to purchase                           │
│                                                                      │
│ ✅ Likely 7-day churners                      [Create audience]     │
│    Users with >X% probability to churn                              │
│                                                                      │
│ ⚠️ Predicted revenue                          [Not yet available]   │
│    Need more purchase data with value                               │
└──────────────────────────────────────────────────────────────────────┘

NOT ELIGIBLE? CHECK:
────────────────────
├── Reports → Monetization → Ecommerce purchases
│   └─► Are there purchase events?
│
├── Admin → Events → purchase event parameters
│   └─► Does purchase have a value parameter?
│
├── Realtime report → Events
│   └─► Are purchases being tracked?
│
└── Explore → Free form → Users with purchase
    └─► Minimum 1,000 in the last 28 days?
```

### Step 2: Configure Audience

```
PREDICTIVE AUDIENCE CONFIGURATION
==================================

OPTION A: SUGGESTED PREDICTIVE AUDIENCES
─────────────────────────────────────────
Google offers ready-made options:

1. Likely 7-day purchasers
   ├── Users with high purchase probability
   ├── Threshold automatically determined
   └── Ideal for conversion campaigns

2. Likely 7-day churners
   ├── Users with high churn probability
   ├── Still recently active, but at-risk
   └── Ideal for retention campaigns

3. Predicted high spenders
   ├── Users with high predicted revenue
   ├── Based on 28-day forecast
   └── Ideal for VIP targeting

OPTION B: CUSTOM PREDICTIVE AUDIENCE
─────────────────────────────────────
Combine predictive metrics with other conditions:

Example: "High-Value Likely Purchasers"
├── Include: Purchase probability > 70%
├── AND: LTV > $200
└── Duration: 7 days

Example: "At-Risk VIP Customers"
├── Include: Churn probability > 50%
├── AND: Previous purchases >= 3
└── Duration: 14 days

Example: "High Predicted Revenue + Cart Abandon"
├── Include: Predicted revenue > $100
├── AND: event add_to_cart (last 7 days)
├── Exclude: event purchase
└── Duration: 7 days
```

### Step 3: Set Thresholds

```
PROBABILITY THRESHOLDS
======================

PURCHASE PROBABILITY TIERS:
┌─────────────────┬──────────────┬───────────────────────────────────────┐
│ Tier            │ Probability  │ Use Case                              │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Top tier        │ >90%         │ Near-certain buyers                   │
│                 │              │ └─► Minimal incentive needed          │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ High            │ 70-90%       │ Likely buyers                         │
│                 │              │ └─► Light push campaigns              │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Medium          │ 50-70%       │ Potential buyers                      │
│                 │              │ └─► Stronger incentives               │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Low-Medium      │ 30-50%       │ Need nurturing                        │
│                 │              │ └─► Awareness + consideration         │
└─────────────────┴──────────────┴───────────────────────────────────────┘

CHURN PROBABILITY TIERS:
┌─────────────────┬──────────────┬───────────────────────────────────────┐
│ Tier            │ Probability  │ Use Case                              │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ High risk       │ >80%         │ Almost gone                           │
│                 │              │ └─► Aggressive win-back               │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Medium risk     │ 50-80%       │ At-risk                               │
│                 │              │ └─► Re-engagement campaigns           │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Low risk        │ <50%         │ Likely to stay                        │
│                 │              │ └─► Standard nurturing                │
└─────────────────┴──────────────┴───────────────────────────────────────┘

PREDICTED REVENUE TIERS:
┌─────────────────┬──────────────┬───────────────────────────────────────┐
│ Tier            │ Revenue      │ Use Case                              │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ High value      │ >$200        │ VIP treatment                         │
│                 │              │ └─► Premium ad spend                  │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Medium value    │ $50-200      │ Standard valuable                     │
│                 │              │ └─► Normal campaign inclusion         │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Low value       │ <$50         │ Lower priority                        │
│                 │              │ └─► Efficiency focus                  │
└─────────────────┴──────────────┴───────────────────────────────────────┘
```

## Strategic Audience Combinations

```
PREDICTIVE + BEHAVIORAL COMBINATIONS
=====================================

1. HIGH-VALUE CART ABANDONERS
─────────────────────────────
Conditions:
├── Predicted revenue > $100
├── AND: event add_to_cart (last 3 days)
└── EXCLUDE: event purchase

Strategy: Premium retargeting, higher bids
Expected ROAS: High

2. LIKELY PURCHASERS + CATEGORY INTEREST
────────────────────────────────────────
Conditions:
├── Purchase probability > 60%
├── AND: page_path contains /category/[name]/

Strategy: Category-specific ads for high-intent users
Use: Product-specific campaigns

3. AT-RISK LOYAL CUSTOMERS
──────────────────────────
Conditions:
├── Churn probability > 60%
├── AND: total purchases >= 3
├── AND: LTV > $200

Strategy: VIP win-back with exclusive offers
Priority: High (valuable to retain)

4. LIKELY CHURNERS - RECENT BROWSERS
────────────────────────────────────
Conditions:
├── Churn probability > 70%
├── AND: session (last 7 days)
└── EXCLUDE: purchase (last 30 days)

Strategy: Re-engagement with new products
Timing: Act fast

5. HIGH PREDICTED REVENUE - NEW VISITORS
────────────────────────────────────────
Conditions:
├── Predicted revenue > $150
├── AND: session_number = 1 or 2

Strategy: Fast-track to conversion
Focus: Reduce friction, clear CTA

6. LOW PURCHASE PROB + HIGH ENGAGEMENT
──────────────────────────────────────
Conditions:
├── Purchase probability < 30%
├── AND: session_duration > 300s
├── AND: page_views > 5

Strategy: Research phase - nurture content
Goal: Move up the probability ladder
```

## Google Ads Integration

```
PREDICTIVE AUDIENCES IN GOOGLE ADS
==================================

AUTOMATIC SYNC:
─────────────────
├── Eligible predictive audiences sync automatically
├── Requires: Google Ads link + Personalized ads enabled
├── Sync time: 24-48 hours after audience creation
└── Updates: Daily (real-time probability updates)

SMART BIDDING OPTIMIZATION:
──────────────────────────
Predictive audiences are ideal for:

┌────────────────────────┬─────────────────────────────────────────────────┐
│ Bid Strategy           │ How Predictive Helps                            │
├────────────────────────┼─────────────────────────────────────────────────┤
│ Target ROAS            │ Focus budget on high predicted revenue users    │
│                        │ Bid higher for high purchase probability        │
├────────────────────────┼─────────────────────────────────────────────────┤
│ Target CPA             │ Optimize toward users with high purchase chance │
│                        │ Avoid spend on low probability                  │
├────────────────────────┼─────────────────────────────────────────────────┤
│ Maximize Conversions   │ Prioritize likely purchasers                    │
│                        │ More efficient spend allocation                 │
├────────────────────────┼─────────────────────────────────────────────────┤
│ Value-Based Bidding    │ Predicted revenue as value signal               │
│                        │ Higher bids for higher predicted value          │
└────────────────────────┴─────────────────────────────────────────────────┘

CAMPAIGN SETUP TIPS:
───────────────────
├── Create separate ad groups for probability tiers
├── Adjust creative messaging per tier
├── Monitor performance per probability segment
└── A/B test predictive vs. behavior-only targeting
```

## Best Practices

```
DO's
═══════
├── Combine predictive with behavioral signals
│   └─► "Likely purchasers" + "Cart abandoners" = Super high intent
│
├── Segment by probability tiers
│   └─► >70%, 50-70%, <50% treated as separate audiences
│
├── Use for Smart Bidding optimization
│   └─► Target ROAS with predicted revenue signals
│
├── Monitor model quality over time
│   └─► Seasonal shifts can affect model accuracy
│
├── Start with Google's suggested audiences
│   └─► Then customize with your own conditions
│
├── Combine with exclusions
│   └─► "Likely purchasers" EXCLUDE "Recent purchasers"
│
└── Track ROAS per probability tier
    └─► Validate that high probability = high ROAS

DON'Ts
════════
├── Rely solely on predictive
│   └─► Combine with first-party data
│
├── Ignore ineligibility
│   └─► Fix tracking first, then use predictive
│
├── Expect predictive to work instantly
│   └─► Model needs 28+ days of data
│
├── Put all users in one predictive audience
│   └─► Segment by tiers for better performance
│
├── Blindly trust the model
│   └─► Validate with actual conversion data
│
└── Forget to review audiences
    └─► Predictive updates daily, review performance
```

## Output: Predictive Audience Recommendation Template

```markdown
# GA4 Predictive Audience Recommendation

## Eligibility Status
- **Purchase probability:** [Eligible / Not yet / Not eligible]
- **Churn probability:** [Eligible / Not yet / Not eligible]
- **Predicted revenue:** [Eligible / Not yet / Not eligible]

## Eligibility Metrics
| Metric | Required | Current | Status |
|--------|----------|---------|--------|
| Weekly purchasers | >1,000 | [X] | [Pass/Fail] |
| Weekly non-purchasers | >1,000 | [X] | [Pass/Fail] |
| Data consistency | 28+ days | [X days] | [Pass/Fail] |
| Purchase value param | Yes | [Yes/No] | [Pass/Fail] |

## Recommended Predictive Audiences

### Audience 1: [Name]
- **Type:** [Purchase/Churn/Revenue] probability
- **Threshold:** >[X]%
- **Combined with:** [Additional conditions]
- **Expected size:** [X users]
- **Use case:** [Campaign type]

### Audience 2: [Name]
- **Type:** [Type]
- **Threshold:** >[X]%
- **Combined with:** [Conditions]
- **Expected size:** [X users]
- **Use case:** [Campaign type]

## Google Ads Strategy

### Bid Adjustments per Tier
| Probability Tier | Bid Adjustment | Rationale |
|-----------------|----------------|-----------|
| >80% | +[X]% | Highest intent |
| 50-80% | +[X]% | Medium intent |
| <50% | -[X]% | Lower intent |

### Campaign Recommendations
1. **[Campaign type]:** Target [audience] with [strategy]
2. **[Campaign type]:** Target [audience] with [strategy]

## Monitoring Plan
- **Review frequency:** [Weekly]
- **Key metrics:** [Prediction accuracy, ROAS per tier, Size trends]
- **Alerts:** [If accuracy <X% or size drop >Y%]

## Action Items (if not eligible)
1. [ ] [First step to reach eligibility]
2. [ ] [Second step]
3. [ ] [Third step]

## Notes
[Specific recommendations or context for this property]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, check whether predictive metrics are available and what the underlying purchase event volume looks like:

```python
# Check purchase event volume — need ≥1k purchasers in last 28 days for predictive eligibility
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["eventCount", "totalUsers"],
    dimensions=["eventName"],
    start_date="28daysAgo",
    end_date="today"
)
```

If `eventCount` is below 1,000 purchases, predictive audiences are not yet available. Focus on growing purchase volume before revisiting predictive segments.
</output>
