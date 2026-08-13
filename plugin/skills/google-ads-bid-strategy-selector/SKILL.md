---
name: google-ads-bid-strategy-selector
description: "This skill should be used when the user asks to \"choose a Google Ads bid strategy\", \"compare tCPA vs tROAS\", \"set up value-based bidding\", \"migrate from manual to Smart Bidding\", or mentions \"Portfolio Bidding\", \"Maximize Conversions\", or \"learning phase management\". Do NOT use for: Meta Ads bidding (use meta-bid-strategy-selector), LinkedIn bidding (use linkedin-bid-strategy-selector), keyword strategy (use keyword-strategy-planner)."
---
# Bid Strategy Selector

Complete guide for choosing and implementing the right Google Ads Smart Bidding strategy based on goals, data, and account situation. Current API: v23.2 (March 25, 2026).

## Quick Decision Tree

```
WHICH BID STRATEGY IS RIGHT FOR YOU?
│
├── NEW ACCOUNT / LOW DATA (<30 conversions/month)
│   └── MAXIMIZE CONVERSIONS (no target)
│       └── Goal: Collect data, complete learning phase
│
├── LEAD GENERATION with known lead value
│   ├── Consistent conversion volume (50+/month)?
│   │   └── YES → TARGET CPA
│   │   └── NO → MAXIMIZE CONVERSIONS
│   └── Variable lead values?
│       └── YES → MAXIMIZE CONVERSION VALUE + tROAS
│
├── E-COMMERCE with purchase tracking
│   ├── Focus on volume (market share)?
│   │   └── MAXIMIZE CONVERSION VALUE
│   ├── Focus on profitability?
│   │   └── TARGET ROAS
│   └── Balance both?
│       └── MAXIMIZE CONVERSION VALUE + tROAS target
│
└── MULTIPLE CAMPAIGNS with same goal
    └── PORTFOLIO BID STRATEGY
        └── Shared strategy across campaigns
```

## Smart Bidding Overview

```
SMART BIDDING COMPARISON
════════════════════════

┌─────────────────────────┬───────────┬───────────┬─────────────────────┐
│ STRATEGY                │ CONTROL   │ DATA REQ  │ BEST FOR            │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Maximize Conversions    │ None      │ Low       │ New accounts,       │
│ (without target)        │           │           │ data collection     │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Maximize Conversions    │ CPA cap   │ Medium    │ Lead gen with       │
│ + Target CPA            │           │ (50+/mo)  │ cost constraints    │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Maximize Conv. Value    │ None      │ Low       │ E-commerce volume,  │
│ (without target)        │           │           │ initial learning    │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Maximize Conv. Value    │ ROAS      │ Medium    │ E-commerce profit,  │
│ + Target ROAS           │ target    │ (50+/mo)  │ scaling             │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Manual CPC              │ Max CPC   │ None      │ Niche, B2B,         │
│ (Enhanced CPC opt.)     │ per kw    │           │ small accounts      │
└─────────────────────────┴───────────┴───────────┴─────────────────────┘
```

## Maximize Conversions

### How It Works

```
MAXIMIZE CONVERSIONS ENGINE
===========================

┌────────────────────────────────────────────────────────────────┐
│  GOOGLE AI OPTIMIZES FOR:                                      │
│  Maximum number of conversions within your daily budget        │
│                                                                │
│  SIGNALS USED:                                                 │
│  ├── Device, location, time of day                             │
│  ├── Browser, OS, demographics                                 │
│  ├── Search query and intent signals                           │
│  ├── Remarketing lists membership                              │
│  ├── Historical conversion patterns                            │
│  └── Real-time auction dynamics                                │
│                                                                │
│  YOU CONTROL:                                                  │
│  ├── Daily budget (spending limit)                             │
│  ├── Target CPA (optional, as constraint)                      │
│  └── Conversion actions (which ones to optimize for)           │
└────────────────────────────────────────────────────────────────┘
```

### When to Use Maximize Conversions

```
USE MAXIMIZE CONVERSIONS WHEN:
──────────────────────────────
• New account with little historical data
• First 2-4 weeks of a new campaign
• Lead generation focus (single conversion type)
• Budget is more important than CPA efficiency
• Collecting data for later tCPA transition

DO NOT USE WHEN:
────────────────
• Strict CPA requirements (use tCPA)
• E-commerce with purchase values (use Max Conv Value)
• Very low budget (<EUR20/day) - too few learnings
• Campaign with multiple conversion types without a primary one
```

### Maximize Conversions + Target CPA

```
ADDING TARGET CPA
=================

WHEN:
├── 50+ conversions in the past 30 days
├── Stable performance (no major fluctuations)
├── Known target CPA (break-even or goal)
└── After successful pure Maximize Conversions phase

CALCULATING TARGET CPA:
───────────────────────
Break-even CPA (Lead Gen):
└── Lead Value x Conversion Rate to Sale

Example:
├── Lead value (as sale): EUR500
├── Close rate: 10%
├── Break-even CPA: EUR500 x 0.10 = EUR50

Starting Target CPA:
├── Week 1-2: 120% of break-even (EUR60)
├── Week 3-4: 110% of break-even (EUR55)
├── Week 5+: 100% or tighter if stable

WARNING: NEVER start BELOW your historical average CPA!
```

## Maximize Conversion Value

### How It Works

```
MAXIMIZE CONVERSION VALUE ENGINE
================================

┌────────────────────────────────────────────────────────────────┐
│  GOOGLE AI OPTIMIZES FOR:                                      │
│  Maximum total conversion value within your daily budget       │
│                                                                │
│  REQUIREMENTS:                                                 │
│  ├── Conversion tracking with VALUE (purchase value)           │
│  ├── Accurate revenue/value data                               │
│  └── Consistent value tracking                                 │
│                                                                │
│  AI PRIORITIZES:                                               │
│  ├── High-value transactions over low-value ones               │
│  ├── Users with high predicted value                           │
│  └── Queries that historically generate high values            │
└────────────────────────────────────────────────────────────────┘
```

### Maximize Conversion Value + Target ROAS

```
ADDING TARGET ROAS
==================

WHEN:
├── 50+ conversions with value in the past 30 days
├── Consistent value tracking (no gaps)
├── Known break-even or target ROAS
└── After successful pure Max Conv Value phase

CALCULATING TARGET ROAS:
────────────────────────
Break-even ROAS = 1 / Profit Margin

Example:
├── Profit margin: 40%
├── Break-even ROAS: 1 / 0.40 = 2.5 (250%)
├── Spending EUR100 means generating EUR250 in revenue is needed

Starting Target ROAS:
├── Week 1-2: 80% of break-even (200% if break-even is 250%)
├── Week 3-4: 90% of break-even (225%)
├── Week 5+: 100% or tighter if stable

WARNING: Too aggressive a ROAS target = no delivery!
```

## Portfolio Bid Strategies

### What Are Portfolio Strategies?

```
PORTFOLIO BID STRATEGY
======================

= One bid strategy shared across multiple campaigns

ADVANTAGES:
├── More data for learning → better optimization
├── Centralized bid management
├── Budget flexibility across campaigns
└── Better performance for small campaigns

LIMITATIONS:
├── All campaigns must share the same goal
├── Shared learning can be suboptimal per campaign
└── Less granular control
```

### Portfolio Strategy Setup

```
PORTFOLIO STRATEGY TYPES
========================

1. TARGET CPA PORTFOLIO
   └── Multiple Search/Display campaigns, same CPA goal
   └── Example: Brand + Non-brand Search

2. TARGET ROAS PORTFOLIO
   └── E-commerce campaigns with same margin target
   └── Example: Shopping + Search + PMax

3. MAXIMIZE CONVERSIONS PORTFOLIO
   └── Aggregate data for faster learning
   └── Example: Bundle new campaigns

4. TARGET IMPRESSION SHARE PORTFOLIO
   └── Brand visibility campaigns
   └── Example: Branded Search campaigns

SETUP LOCATION:
Tools & Settings → Shared Library → Bid Strategies
```

### When to Use Portfolio

```
PORTFOLIO DECISION MATRIX
=========================

USE PORTFOLIO WHEN:
├── Multiple campaigns with <50 conversions/month each
├── Campaigns have exactly the same KPI targets
├── A single point for bid management is desired
└── Small budgets spread across multiple campaigns

USE INDIVIDUAL WHEN:
├── Campaigns have different margin/CPA targets
├── Sufficient conversions per campaign (50+/month)
├── Different product types/audiences
└── Need for campaign-level bid adjustments
```

## Learning Phase Management

### Learning Phase Basics

```
LEARNING PHASE EXPLAINED
=========================

WHAT:
├── Period during which Smart Bidding collects data
├── Bids can fluctuate
├── Performance may temporarily worsen
└── DO NOT intervene during this phase

DURATION:
├── Typical: 7-14 days
├── Requirement: ~50 conversions (or actions)
├── Can take longer with low volume
└── Status visible in campaign UI

LEARNING PHASE STATUS:
├── "Learning" = Actively learning
├── "Learning (limited)" = Insufficient data
├── "Eligible" = Learning complete
└── "Limited" = Other issue (budget, etc.)
```

### What Resets the Learning Phase?

```
ACTIONS THAT RESET LEARNING
============================

AVOID THESE DURING LEARNING:
─────────────────────────────
• Changing bid strategy
• Adjusting Target CPA/ROAS (>20%)
• Changing conversion action
• Increasing or decreasing budget >20%
• Pausing campaign for >7 days

SAFE DURING LEARNING:
─────────────────────
• Adding or pausing ads
• Adding keywords (small batches)
• Adding negatives
• Budget changes <20%
• Ad copy adjustments
```

### Learning Phase Troubleshooting

```
LEARNING PHASE ISSUES
=====================

PROBLEM: "Learning (limited)" stays stuck
──────────────────────────────────────────
Cause: Insufficient conversions
Solutions:
├── Increase budget
├── Broader targeting (more volume)
├── Higher-funnel conversion action (temporarily)
└── Wait longer (sometimes needed)

PROBLEM: CPA spikes during learning
─────────────────────────────────────
This is normal! The AI is testing boundaries.
Actions:
├── DO NOT panic
├── Wait at least 7-10 days
├── Monitor the trend, not daily CPA
└── If >14 days poor: evaluate targeting/budget

PROBLEM: Learning takes >3 weeks
─────────────────────────────────
Possible causes:
├── Insufficient budget
├── Too niche targeting
├── Poor ad quality
└── Tracking issues
```

## Value-Based Bidding

### Value Rules (2025+)

```
VALUE RULES EXPLAINED
=====================

WHAT:
├── Dynamically adjust conversion values
├── Based on user/context signals
├── AI bids higher for high-value segments
└── Available for all Smart Bidding strategies

AVAILABLE SIGNALS:
├── Device (mobile, desktop, tablet)
├── Location (geographic)
├── Audience (Customer Match, remarketing)
└── Time (planned for future)

EXAMPLE SETUP:
──────────────
Value Rule 1: High-Value Customers
├── Condition: Customer Match list = "VIP Customers"
├── Adjustment: +50% value
└── Effect: EUR100 purchase → EUR150 for bidding

Value Rule 2: Low-Intent Location
├── Condition: Location = "Low converting region"
├── Adjustment: -30% value
└── Effect: EUR100 purchase → EUR70 for bidding
```

### New Customer Acquisition

```
NEW CUSTOMER BIDDING (2025+)
============================

LOCATION: Campaign Settings → Customer Acquisition

OPTIONS:
├── Bid higher for new customers: +X% bid adjustment
├── Only bid for new customers: Exclude existing
└── No differentiation (default)

SETUP REQUIREMENTS:
├── Customer Match list of existing customers
├── Conversion tracking active
└── Sufficient new vs returning data

RECOMMENDED START:
├── +20% for new customers
├── Monitor new vs returning ROAS
├── Adjust based on LTV data
└── E-commerce: Consider first-purchase margin
```

## Bid Strategy Migration

### From Manual to Smart Bidding

```
MANUAL → SMART BIDDING MIGRATION
================================

STEP 1: PREPARATION (Week -2 to -1)
────────────────────────────────────
□ Verify conversion tracking
□ Minimum 30 conversions/month
□ Document baseline metrics
□ Set budget (min EUR50/day)

STEP 2: INITIAL SETUP (Week 1)
──────────────────────────────
□ Start with Maximize Conversions (no target)
□ Expect fluctuations
□ DO NOT intervene

STEP 3: MONITORING (Week 2-3)
─────────────────────────────
□ Monitor learning phase
□ Compare with baseline
□ Still DO NOT intervene

STEP 4: OPTIMIZATION (Week 4+)
──────────────────────────────
□ Evaluate performance vs manual
□ Add target if stable
□ Start conservative (120% of achieved)
```

### Strategy Switch Checklist

```
BID STRATEGY SWITCH PROTOCOL
============================

□ PRE-SWITCH:
├── Document current performance (7-day average)
├── Calculate target (CPA/ROAS)
├── Choose switching moment (not during peak)
└── Prepare stakeholders (temporary fluctuations)

□ DURING SWITCH:
├── Implement new strategy
├── Conservative target (120% of current)
├── Screenshot for reference
└── Set calendar reminder for review

□ POST-SWITCH (Week 1-2):
├── Daily monitoring (but no changes)
├── Check learning phase status
├── Compare week-over-week (not day-over-day)
└── Note anomalies

□ POST-SWITCH (Week 3+):
├── Formal performance review
├── Tighten targets if stable (+10%)
├── Document learnings
└── Continue monitoring
```

## Campaign Type Specific Recommendations

### Search Campaigns

```
SEARCH BID STRATEGY GUIDE
=========================

BRAND SEARCH:
├── Strategy: Maximize Conversions or Manual CPC
├── Reason: High CTR, low competition
├── Target: Impression Share >90%
└── Note: Don't overbid — brand terms win anyway

NON-BRAND SEARCH:
├── New: Maximize Conversions (2-3 weeks)
├── Then: Target CPA/ROAS
├── Reason: Competitive, need efficiency
├── Note: Broad match + Smart Bidding = Google's recommended combo
└── AI Max: Enable AI Max for Search to unlock Search Term Matching,
    URL Expansion, and Text Customization within existing Search campaigns
    (Campaign.ai_max_setting.enable_ai_max)

DSA (Dynamic Search Ads):
├── Strategy: Maximize Conversions
├── Reason: Discovery, volume focus
├── Transition to tCPA once winning queries are known
└── Note: Negative keywords management
```

### Shopping & PMax

```
SHOPPING / PMAX BID STRATEGY
============================

STANDARD SHOPPING (if still used):
├── Start: Maximize Clicks (data collection)
├── Transition: Target ROAS after 50+ purchases
├── Note: Product-level bidding via priorities

PERFORMANCE MAX:
├── E-commerce: Maximize Conversion Value + tROAS
├── Lead Gen: Maximize Conversions + tCPA
├── New: Without target (2-3 weeks)
└── Note: PMax needs more data than Search

ROAS TARGETS FOR PMAX:
├── Conservative start: 200-300%
├── Moderate: 300-500%
├── Aggressive: 500%+
└── Adjust based on margin and goals
```

### Display & Video

```
DISPLAY / VIDEO BID STRATEGY
============================

DISPLAY CAMPAIGNS:
├── Remarketing: Maximize Conversions + tCPA
├── Prospecting: Maximize Conversions (volume focus)
├── Brand: Target CPM (if available)
└── Note: Longer learning due to lower volume

VIDEO CAMPAIGNS:
├── Awareness: Target CPM or Maximize Impressions
├── Consideration: Target CPV (Cost-per-View)
├── Conversion: Maximize Conversions
└── Note: Video ads convert indirectly

DEMAND GEN (replaced Discovery in 2025):
├── Strategy: Maximize Conversions or tCPA
├── Target CPC: Also available for Demand Gen (v22 addition)
├── Reason: Hybrid awareness/conversion
└── Note: Factor in view-through conversions
```

## Smart Bidding Exploration (v21+)

```
SMART BIDDING EXPLORATION
=========================

WHAT:
├── Google's feature to test bid variations beyond your tROAS target
├── API field: target_roas_tolerance_percent_millis
├── Lets the algorithm explore auctions outside the strict target
└── Goal: Find incremental volume while staying near your target

WHEN TO ENABLE:
├── Campaign hitting tROAS target but with limited volume
├── Goal is to test scale without fully loosening the target
├── Available for tROAS campaigns with sufficient conversion data (30+/mo)

HOW TO CHECK:
──────────────
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign.maximize_conversion_value.target_roas,
    campaign.maximize_conversion_value.target_roas_tolerance_percent_millis
  FROM campaign
  WHERE campaign.advertising_channel_type = 'SEARCH'
    AND campaign.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
")
```

## Performance Monitoring Script

```javascript
/**
 * Bid Strategy Performance Monitor
 *
 * Monitors Smart Bidding performance and learning phase status.
 *
 * Setup:
 * 1. Update EMAIL
 * 2. Schedule daily at 9:00
 */

var CONFIG = {
  EMAIL: 'you@example.com',
  CPA_THRESHOLD: 0.25,     // Alert on 25% CPA increase
  ROAS_THRESHOLD: 0.20,    // Alert on 20% ROAS decline
  LEARNING_DAYS_ALERT: 14  // Alert if learning >14 days
};

function main() {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var alerts = [];
  var learningCampaigns = [];

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var bidStrategy = campaign.getBiddingStrategyType();

    // Check learning phase (via status indicators)
    var status = checkCampaignStatus(campaign);
    if (status.isLearning) {
      learningCampaigns.push({
        name: campaign.getName(),
        strategy: bidStrategy,
        days: status.learningDays
      });
    }

    // Check performance changes
    var perfAlerts = checkPerformance(campaign);
    alerts = alerts.concat(perfAlerts);
  }

  // Send summary
  if (alerts.length > 0 || learningCampaigns.length > 0) {
    sendSummaryEmail(alerts, learningCampaigns);
  }

  Logger.log('Monitor complete. Alerts: ' + alerts.length);
  Logger.log('Campaigns in learning: ' + learningCampaigns.length);
}

function checkCampaignStatus(campaign) {
  // Note: Learning phase status not directly available via API
  // This is a proxy check
  var stats7d = campaign.getStatsFor('LAST_7_DAYS');
  var stats14d = campaign.getStatsFor('LAST_14_DAYS');

  var conv7d = stats7d.getConversions();
  var conv14d = stats14d.getConversions();

  // If <50 conversions in 14 days, likely still learning
  return {
    isLearning: conv14d < 50,
    learningDays: conv14d < 50 ? 14 : 0
  };
}

function checkPerformance(campaign) {
  var alerts = [];
  var name = campaign.getName();

  var currentStats = campaign.getStatsFor('LAST_7_DAYS');
  var previousStats = campaign.getStatsFor('LAST_14_DAYS');

  var currentCPA = currentStats.getConversions() > 0 ?
    currentStats.getCost() / currentStats.getConversions() : 0;

  // Calculate previous period CPA
  var prevConv = previousStats.getConversions() - currentStats.getConversions();
  var prevCost = previousStats.getCost() - currentStats.getCost();
  var previousCPA = prevConv > 0 ? prevCost / prevConv : 0;

  if (previousCPA > 0 && currentCPA > 0) {
    var change = (currentCPA - previousCPA) / previousCPA;
    if (change > CONFIG.CPA_THRESHOLD) {
      alerts.push({
        campaign: name,
        metric: 'CPA',
        previous: previousCPA.toFixed(2),
        current: currentCPA.toFixed(2),
        change: (change * 100).toFixed(1) + '%'
      });
    }
  }

  return alerts;
}

function sendSummaryEmail(alerts, learningCampaigns) {
  var subject = 'Smart Bidding Status - ' + AdsApp.currentAccount().getName();
  var body = 'Smart Bidding Daily Report\n';
  body += '===========================\n\n';

  if (learningCampaigns.length > 0) {
    body += 'CAMPAIGNS IN LEARNING:\n';
    for (var i = 0; i < learningCampaigns.length; i++) {
      var lc = learningCampaigns[i];
      body += '- ' + lc.name + ' (' + lc.strategy + ')\n';
    }
    body += '\n';
  }

  if (alerts.length > 0) {
    body += 'PERFORMANCE ALERTS:\n';
    for (var j = 0; j < alerts.length; j++) {
      var alert = alerts[j];
      body += '- ' + alert.campaign + ': ' + alert.metric + ' changed ';
      body += alert.previous + ' -> ' + alert.current + ' (' + alert.change + ')\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Output: Bid Strategy Recommendation Template

```markdown
# Bid Strategy Recommendation

## Account Situation
- **Account type:** [E-commerce / Lead Gen / Hybrid]
- **Monthly budget:** EUR[X]
- **Current conversions/month:** [X]
- **Current CPA/ROAS:** EUR[X] / [X]%
- **Primary goal:** [Volume / Efficiency / Profitability]

## Recommended Strategy
**[STRATEGY NAME]**

### Why This Strategy
1. [Reason 1 - based on account situation]
2. [Reason 2 - based on goals]
3. [Reason 3 - based on data availability]

### Implementation Plan

**Week 1-2: Setup & Learning**
- Switch to [strategy]
- Target: [None / EURX / X%] (conservative)
- Budget: EUR[X]/day
- Action: Monitor only, no changes

**Week 3-4: Evaluation**
- Learning phase check
- Performance vs baseline
- Target adjustment: [Specify]

**Week 5+: Optimization**
- Tighten target to [X]
- Continue monitoring
- Evaluate scale opportunities

### Targets
- Primary: [CPA EURX / ROAS X%]
- Secondary: [Conversions, Value, etc.]

### Expected Results
- CPA change: [+/- X%]
- Volume change: [+/- X%]
- Learning phase duration: [X weeks]

### Risks & Mitigation
- Risk: [Describe]
- Mitigation: [Plan]
```
