---
name: google-ads-learning-phase-tracker
description: "This skill should be used when the user asks to \"check learning phase status\", \"fix stuck learning phase\", \"accelerate Smart Bidding learning\", \"predict learning phase duration\", or mentions \"learning limited\", \"bid strategy learning\", or \"tCPA learning phase\". Do NOT use for: bid strategy selection (use bid-strategy-selector), campaign structure changes (use campaign-structure-advisor), or conversion tracking setup (use conversion-tracking-auditor)."
---
# Learning Phase Tracker

Complete guide for monitoring, understanding, and optimizing Google Ads Smart Bidding learning phases for faster and more stable performance.



See [decision-trees.md](references/decision-trees.md) for details.



## Learning Phase Fundamentals

### What Is Learning Phase?

```
LEARNING PHASE EXPLAINED
═════════════════════════

WHAT HAPPENS:
├── Google's AI collects data about your account
├── Analyzes which signals lead to conversions
├── Builds a prediction model
├── Bids are dynamically adjusted
└── Performance may fluctuate

WHY IT IS NECESSARY:
├── Every account is unique
├── AI must learn your specific patterns
├── Seasonality, audience, products vary
└── Generic models are suboptimal

LEARNING DURATION:
────────────────────────────────────────
Typical: 7-14 days (or ~50 conversions)

May take longer with:
├── Low conversion volume
├── Inconsistent tracking
├── Insufficient budget
├── Very niche targeting
└── New conversion actions

May be shorter with:
├── High volume accounts
├── Consistent historical pattern
├── Stable seasonality
└── Experience with similar campaigns
```

### Learning Phase Signals

```
SIGNALS SMART BIDDING USES
═══════════════════════════

REAL-TIME AUCTION SIGNALS:
├── Device (mobile, desktop, tablet)
├── Operating system
├── Browser
├── Location (geographic, granular)
├── Time of day
├── Day of week
├── Search query (exact + intent)
└── Ad format/placement

HISTORICAL SIGNALS:
├── User's past behavior
├── Conversion patterns
├── Seasonal trends
├── Time-of-day performance
└── Device performance history

AUDIENCE SIGNALS:
├── Remarketing list membership
├── Optimized Targeting signals
├── Customer Match segments
├── Demographics (age, gender, income)
└── Affinities & in-market

CONTEXTUAL SIGNALS:
├── Ad relevance
├── Landing page quality
├── Ad position factors
├── Competitive auction dynamics
└── Query-ad match quality

IMPORTANT:
The AI learns which COMBINATIONS of signals
lead to conversions in your specific situation.
```

## MCP Tool Integration

```
STEP 1: Check bid strategy status across all campaigns
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign.status,
    campaign.bidding_strategy_type,
    bidding_strategy.status,
    bidding_strategy.name,
    bidding_strategy.type,
    metrics.conversions,
    metrics.cost_micros,
    metrics.cost_per_conversion
  FROM campaign
  WHERE campaign.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")

STEP 2: Conversion volume per campaign (estimate learning progress)
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign.bidding_strategy_type,
    segments.date,
    metrics.conversions,
    metrics.cost_micros
  FROM campaign
  WHERE campaign.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY segments.date DESC
")

STEP 3: Check campaigns potentially stuck in learning
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign.bidding_strategy_type,
    campaign.start_date_time,
    metrics.conversions,
    metrics.cost_micros,
    metrics.search_impression_share
  FROM campaign
  WHERE campaign.status = 'ENABLED'
    AND campaign.bidding_strategy_type IN (
      'TARGET_CPA',
      'TARGET_ROAS',
      'MAXIMIZE_CONVERSIONS',
      'MAXIMIZE_CONVERSION_VALUE'
    )
    AND segments.date DURING LAST_30_DAYS
  ORDER BY campaign.start_date_time ASC
")
```

## Learning Phase Monitoring

### Checking Status

```
WHERE TO FIND LEARNING STATUS
══════════════════════════════

LOCATION 1: Campaign Level
─────────────────────────
Campaigns → Columns → Modify → Bid strategy
→ Add: "Bid strategy type" and "Bid strategy status"

LOCATION 2: Bid Strategy Report
──────────────────────────────
Tools → Shared Library → Bid strategies
→ See "Status" column per strategy

LOCATION 3: Recommendations Tab
──────────────────────────────
Recommendations → Scroll to "Bidding"
→ Alerts about learning issues

STATUS INTERPRETATION:
─────────────────────
┌─────────────────────┬─────────────────────────────────────────┐
│ Status              │ Meaning                                 │
├─────────────────────┼─────────────────────────────────────────┤
│ Learning            │ Actively learning (7-14 days)           │
├─────────────────────┼─────────────────────────────────────────┤
│ Learning (limited)  │ Insufficient data to learn              │
├─────────────────────┼─────────────────────────────────────────┤
│ Eligible            │ Learning complete, full                 │
│                     │ optimization active                     │
├─────────────────────┼─────────────────────────────────────────┤
│ Misconfigured       │ Setup issue (check conversion           │
│                     │ tracking)                               │
├─────────────────────┼─────────────────────────────────────────┤
│ Limited             │ Not learning-related (budget/bid)       │
└─────────────────────┴─────────────────────────────────────────┘
```

### Learning Duration Tracker

```
HOW LONG DOES LEARNING TAKE?
════════════════════════════

BASELINE EXPECTATIONS:
──────────────────────
New account/campaign:
├── Minimum: 7 days
├── Typical: 10-14 days
├── Max (normal): 21 days
└── Guideline: ~50 conversions needed

Existing account (change):
├── Bid strategy switch: 7-14 days
├── Target adjustment >20%: 7 days
├── Small target change <10%: 3-5 days
└── New conversion action: 14+ days

LEARNING DURATION CALCULATOR:
─────────────────────────────
Estimated duration = 50 / (conversions per day)

Example:
├── 10 conv/day → ~5 days (fast!)
├── 3 conv/day → ~17 days (average)
├── 1 conv/day → ~50 days (long)
└── 0.5 conv/day → 100+ days (too long)

If >21 days in learning:
├── Evaluate conversion volume
├── Check budget allocation
├── Consider higher-funnel conversion
└── Or different bid strategy type
```

## What Resets Learning Phase?

### Major Resets (Full Restart)

```
ACTIONS THAT FULLY RESET LEARNING
═════════════════════════════════

AVOID THESE DURING LEARNING:
─────────────────────────────

1. CHANGING BID STRATEGY
   └── From tCPA to Max Conversions = RESET
   └── From tROAS to tCPA = RESET
   └── Portfolio to individual = RESET

2. LARGE TARGET ADJUSTMENT (>20%)
   └── tCPA from $50 to $40 = RESET
   └── tROAS from 400% to 300% = RESET
   └── Exception: Adding first target

3. CHANGING CONVERSION ACTION
   └── Different primary conversion = RESET
   └── Changing conversion value = RESET
   └── Linking new conversion action = RESET

4. PAUSING CAMPAIGN >7 DAYS
   └── Longer pause = learning data becomes stale
   └── Reopening = essentially a fresh start

5. DRASTIC BUDGET CHANGE (>50%)
   └── Halving budget = RESET
   └── Doubling budget = Partial reset
```

### Minor Changes (No Reset)

```
SAFE ACTIONS DURING LEARNING
═══════════════════════════

THESE ACTIONS ARE SAFE:
───────────────────────

TARGETING:
├── Adding keywords (small batches)
├── Adding negative keywords
├── Expanding locations
├── Device bid adjustments
└── Adding audiences (observation)

ADS:
├── Adding new ads
├── Pausing ads
├── Changing RSA headlines/descriptions
├── Adding/changing extensions
└── Optimizing ad copy

BUDGET:
├── Budget increase <20%
├── Budget decrease <10%
└── Small shared budget adjustments

LANDING PAGES:
├── Changing landing page URL
├── Content updates
└── A/B test URL variants

GENERAL RULE:
Small, incremental changes = OK
Large, structural changes = RESET
```

### Gray Zone Actions

```
ACTIONS WITH POTENTIAL IMPACT
═══════════════════════════

HANDLE WITH CAUTION:
──────────────────────

1. BUDGET CHANGE 20-30%
   └── May slow down learning
   └── Usually not a full reset
   └── Monitor closely

2. TARGET CHANGE 10-20%
   └── May cause short "re-calibration"
   └── Not always a full reset
   └── Wait-and-see approach

3. ADDING MANY KEYWORDS AT ONCE
   └── >50 keywords = may disrupt learning
   └── Better: batches of 10-20
   └── Monitor impression share

4. ADDING NEW AD GROUPS
   └── 1-2 ad groups = no problem
   └── Large-scale restructure = problematic
   └── Test small first

5. CHANGING AUDIENCE TARGETING
   └── Observation to targeting = impact
   └── Adding new audiences = OK
   └── Removing audiences = minor impact
```



See [decision-trees.md](references/decision-trees.md) for details.



## Learning Phase Best Practices

### Pre-Launch Checklist

```
BEFORE LAUNCHING SMART BIDDING
══════════════════════════════

□ CONVERSION TRACKING VERIFIED
├── Test conversions fired
├── Correct attribution window
├── Values correct (if used)
└── No duplicate conversions

□ HISTORICAL DATA PRESENT
├── Minimum 30 days of data
├── Preferably 50+ conversions in history
├── Consistent tracking throughout the period
└── No large gaps in data

□ ADEQUATE BUDGET
├── Minimum: 10x target CPA per day
├── Recommended: 20x target CPA per day
├── Buffer for learning fluctuations
└── 30-day budget commitment

□ REALISTIC TARGET SET
├── Target CPA: Historical average + 20%
├── Target ROAS: Historical average - 20%
├── DO NOT start too aggressively
└── Room to learn

□ STAKEHOLDERS INFORMED
├── Expect fluctuations in first 2 weeks
├── No panic on CPA spikes
├── Focus on trend, not daily numbers
└── Review after 4 weeks, not earlier
```

### During Learning Protocol

```
DURING LEARNING PHASE
══════════════════════

WEEK 1: HANDS-OFF
─────────────────
□ Daily monitoring (no action)
□ Log performance in spreadsheet
□ Expect: Higher CPA, volatility
□ DO NOT: Change budget, adjust targets

WEEK 2: OBSERVE PATTERNS
────────────────────────
□ Analyze day-of-week trends
□ Check device performance
□ Note metrics becoming stable
□ Still: No major changes

WEEK 3: FIRST EVALUATION
────────────────────────
□ Compare with pre-learning baseline
□ Check learning status in UI
□ If "Eligible": Small optimization OK
□ If "Learning": Keep waiting

WEEK 4: FORMAL REVIEW
──────────────────────
□ Full performance analysis
□ Learning complete? → Optimize
□ Still learning? → Evaluate cause
□ Document learnings

MONITORING DASHBOARD:
─────────────────────
┌───────────────────────────────────────────────────────────┐
│ Metric          │ Pre-Learning │ Week 1 │ Week 2 │ Week 3│
├─────────────────┼──────────────┼────────┼────────┼───────┤
│ Conversions     │ baseline     │ -20%?  │ stable │ +10%? │
│ CPA             │ baseline     │ +30%?  │ -10%?  │ target│
│ Conv Rate       │ baseline     │ varies │ stable │ stable│
│ Impression Share│ baseline     │ varies │ varies │ stable│
└─────────────────┴──────────────┴────────┴────────┴───────┘
```

### Learning Acceleration Tactics

```
HOW TO ACCELERATE LEARNING
══════════════════════════

TACTIC 1: CONSERVATIVE TARGETS
───────────────────────────────
Start with more relaxed targets:
├── tCPA: +30% of desired target
├── tROAS: -30% of desired target
├── More auctions = more data = faster learning
└── Tighten after learning is complete

TACTIC 2: ADEQUATE BUDGET
──────────────────────────
Budget formula:
├── Daily budget >= 15x target CPA
├── Or: Enough for 15+ conversions/day
├── More spend = faster learnings
└── Investment in the learning period

TACTIC 3: PORTFOLIO STRATEGIES
───────────────────────────────
Bundle campaigns:
├── Same conversion goal
├── Shared learnings
├── Aggregated data
└── Faster optimization

TACTIC 4: BROAD MATCH + SMART BIDDING
──────────────────────────────────────
During learning only:
├── Broad match = more impressions
├── Smart bidding selects the best
├── More data for AI
└── Later: Add negatives

TACTIC 5: SEASONALITY ADJUSTMENTS
──────────────────────────────────
For known seasonal events:
├── Tools → Bid strategies → Advanced
├── Add seasonality adjustment
├── Informs AI about expected change
└── Prevents unnecessary "re-learning"
```



See [detailed-reference.md](references/detailed-reference.md) for details.



## Output: Learning Phase Status Template

```markdown
# Learning Phase Status Report

## Campaign Overview
- **Campaign name:** [Name]
- **Bid strategy:** [tCPA/tROAS/Max Conv/etc.]
- **Learning status:** [Learning/Limited/Eligible]
- **Days in learning:** [X]

## Current Performance
| Metric | Baseline | Week 1 | Week 2 | Current |
|--------|----------|--------|--------|---------|
| Conversions | [X] | [X] | [X] | [X] |
| CPA | $[X] | $[X] | $[X] | $[X] |
| Conv Rate | [X]% | [X]% | [X]% | [X]% |
| Spend | $[X] | $[X] | $[X] | $[X] |

## Learning Analysis

### Data Volume Check
- Conversions past 30 days: [X] (needed: 50+)
- Average per day: [X]
- Estimated time to eligible: [X] days

### Blocking Factors
- [ ] Budget too low
- [ ] Target too restrictive
- [ ] Conversion tracking issues
- [ ] Insufficient impressions

## Recommendations

### If Status = "Learning"
- [ ] Wait at least [X] days
- [ ] No major changes
- [ ] Daily monitoring

### If Status = "Learning (Limited)"
**Priority action:** [Describe solution]

Options:
1. [Option 1 - e.g., increase budget]
2. [Option 2 - e.g., relax target]
3. [Option 3 - e.g., consolidate]

### If Status = "Eligible"
- [ ] Evaluate performance vs targets
- [ ] Consider target tightening (max 10%)
- [ ] Begin optimization cycle

## Next Steps
1. [Action 1 + deadline]
2. [Action 2 + deadline]
3. [Action 3 + deadline]

## Review Schedule
- Daily check: [Time]
- Weekly deep-dive: [Day]
- Formal evaluation: [Date]
```
</output>
