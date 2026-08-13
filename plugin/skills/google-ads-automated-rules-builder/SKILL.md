---
name: google-ads-automated-rules-builder
description: "This skill should be used when the user asks to \"create automated rules in Google Ads\", \"set up budget management automation\", \"configure bid adjustment rules\", \"build performance alerts\", or mentions \"scheduling automation\", \"scripts vs rules\", or \"Google Ads automation\". Do NOT use for: Meta Ads rules (use meta-automated-rules-builder), Google Ads Scripts only (use google-ads-scripts-library), or bid strategy selection (use bid-strategy-selector)."
---
# Automated Rules Builder

Complete guide to Google Ads automated rules — from budget management to performance alerts and bid optimization.



See [decision-trees.md](references/decision-trees.md) for details.



## MCP Tool Integration

```
Use these queries to identify which campaigns/keywords need rules before building them.

STEP 1: Find campaigns exceeding CPA thresholds (candidates for rules)
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign.status,
    campaign.bidding_strategy_type,
    metrics.cost_micros,
    metrics.conversions,
    metrics.cost_per_conversion,
    metrics.search_budget_lost_impression_share
  FROM campaign
  WHERE campaign.status = 'ENABLED'
    AND segments.date DURING LAST_7_DAYS
  ORDER BY metrics.cost_per_conversion DESC
  LIMIT 50
")

STEP 2: Find keywords with high spend and zero conversions (auto-pause candidates)
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    ad_group.name,
    ad_group_criterion.keyword.text,
    ad_group_criterion.keyword.match_type,
    metrics.cost_micros,
    metrics.conversions,
    metrics.clicks
  FROM keyword_view
  WHERE campaign.status = 'ENABLED'
    AND ad_group.status = 'ENABLED'
    AND ad_group_criterion.status = 'ENABLED'
    AND metrics.conversions < 1
    AND metrics.cost_micros > 10000000
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
  LIMIT 50
")

STEP 3: Budget pacing check (find campaigns near daily cap)
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign_budget.amount_micros,
    metrics.cost_micros,
    metrics.impressions,
    metrics.search_budget_lost_impression_share
  FROM campaign
  WHERE campaign.status = 'ENABLED'
    AND segments.date DURING LAST_7_DAYS
  ORDER BY metrics.search_budget_lost_impression_share DESC
  LIMIT 25
")
```

## Automated Rules Overview

### What Are Automated Rules?

```
GOOGLE ADS AUTOMATED RULES
═══════════════════════════

DEFINITION:
───────────
Automated rules are IF-THEN statements that Google Ads
executes automatically based on performance data.

IF [condition is true] THEN [execute action]

ADVANTAGES:
───────────
✓ No technical knowledge required
✓ UI-based configuration
✓ Reliable execution
✓ Email notifications
✓ Audit trail

LIMITATIONS:
────────────
✗ Limited condition combinations
✗ No custom calculations
✗ No external data sources
✗ Max 1 action per rule
✗ No real-time execution

WHERE TO FIND:
──────────────
Google Ads → Tools & Settings → Bulk Actions → Rules

RULE COMPONENTS:
────────────────
┌────────────────────────────────────────────────────────────┐
│ 1. APPLY TO: What gets affected?                           │
│    ├── Campaigns                                           │
│    ├── Ad Groups                                           │
│    ├── Keywords                                            │
│    ├── Ads                                                 │
│    └── Extensions                                          │
├────────────────────────────────────────────────────────────┤
│ 2. ACTION: What should happen?                             │
│    ├── Enable / Pause                                      │
│    ├── Change budget                                       │
│    ├── Change bid                                          │
│    ├── Send email                                          │
│    └── Change labels                                       │
├────────────────────────────────────────────────────────────┤
│ 3. CONDITIONS: When should it happen?                      │
│    ├── Performance metrics (CPA, CTR, etc.)                │
│    ├── Status conditions                                   │
│    ├── Label conditions                                    │
│    └── Budget conditions                                   │
├────────────────────────────────────────────────────────────┤
│ 4. FREQUENCY: How often to check?                          │
│    ├── Hourly                                              │
│    ├── Daily                                               │
│    ├── Weekly                                              │
│    └── Monthly                                             │
└────────────────────────────────────────────────────────────┘
```

## Essential Automated Rules

### Budget Management Rules

```
BUDGET PROTECTION RULES
═══════════════════════

RULE 1: PAUSE CAMPAIGN ON BUDGET OVERRUN
─────────────────────────────────────────
Goal: Prevent overspend at campaign level

Apply to: All enabled campaigns
Action: PAUSE campaign
Condition: Cost > [Maximum daily budget]
           Date range: Same day
Frequency: Hourly

Example:
├── Max budget: €500/day
├── Condition: Cost > €475 (build in margin)
└── Alert: Email on every execution


RULE 2: INCREASE BUDGET FOR GOOD PERFORMANCE
─────────────────────────────────────────────
Goal: Scale winning campaigns automatically

Apply to: Enabled campaigns with label "Auto-Scale"
Action: INCREASE budget by 15%
Conditions:
├── CPA < €30 (your target CPA)
├── Conversions >= 5
├── Cost > €100 (significant spend)
Date range: Previous 7 days
Frequency: Weekly (Monday 8:00)
Max budget: €500/day (set a cap)

Preview first! Check which campaigns are affected.


RULE 3: DECREASE BUDGET FOR POOR PERFORMANCE
─────────────────────────────────────────────
Goal: Limit spend on underperformers

Apply to: Enabled campaigns with label "Auto-Scale"
Action: DECREASE budget by 20%
Conditions:
├── CPA > €50 (above target)
├── Cost > €100
├── Conversions > 0 (there is data)
Date range: Previous 7 days
Frequency: Weekly (Monday 8:00)
Min budget: €20/day (don't go too low)


RULE 4: MONTHLY BUDGET PACING
──────────────────────────────
Goal: Prevent monthly overspend

Apply to: All enabled campaigns
Action: Send email notification
Conditions:
├── Cost > [Monthly budget * (day/days_in_month) * 1.1]
Date range: This month
Frequency: Daily (9:00)

Note: Calculate the expected spend ratio manually per day.
```

### Bid Management Rules

```
BID ADJUSTMENT RULES
════════════════════

RULE 5: INCREASE BID FOR TOP PERFORMERS
────────────────────────────────────────
Goal: More volume for winning keywords

Apply to: Keywords with label "Auto-Bid"
Action: INCREASE bid by 10%
Conditions:
├── Status: Enabled
├── CPA < €25 (below target)
├── Impressions > 100
├── Clicks >= 5
├── Avg Position < 3 (optional: top position check)
Date range: Previous 14 days
Frequency: Weekly
Max CPC: €5.00 (set a cap)


RULE 6: DECREASE BID FOR UNDERPERFORMERS
─────────────────────────────────────────
Goal: Reduce spend on poor keywords

Apply to: Keywords with label "Auto-Bid"
Action: DECREASE bid by 15%
Conditions:
├── Status: Enabled
├── CPA > €40 (above target)
├── Cost > €50
├── Conversions < 2
Date range: Previous 14 days
Frequency: Weekly
Min CPC: €0.50 (don't go too low for visibility)


RULE 7: PAUSE KEYWORDS WITHOUT CONVERSIONS
───────────────────────────────────────────
Goal: Stop spend on non-converters

Apply to: All enabled keywords
Action: PAUSE keyword
Conditions:
├── Cost > €100
├── Conversions = 0
Date range: Previous 30 days
Frequency: Weekly

WARNING: Always preview first!
Check that no valuable awareness keywords get paused.


RULE 8: REACTIVATE PAUSED KEYWORDS (Seasonal)
──────────────────────────────────────────────
Goal: Reactivate keywords for seasonal periods

Apply to: Paused keywords with label "Seasonal-Q4"
Action: ENABLE keyword
Conditions: None (activate all with label)
Frequency: One time / Manual trigger

Tip: Use labels for seasonal items:
├── "Seasonal-Q4" for holiday season
├── "Seasonal-Summer" for summer
└── "Seasonal-BTS" for back to school
```

### Performance Alert Rules

```
MONITORING & ALERT RULES
═════════════════════════

RULE 9: CPA SPIKE ALERT
────────────────────────
Goal: Immediate notification on CPA increase

Apply to: All enabled campaigns
Action: Send email notification
Conditions:
├── CPA > €50 (your max acceptable CPA)
├── Conversions >= 3 (enough data)
├── Cost > €100
Date range: Previous 3 days
Frequency: Daily (9:00)


RULE 10: CTR DROP ALERT
────────────────────────
Goal: Detect possible ad fatigue or issues

Apply to: All enabled ad groups
Action: Send email notification
Conditions:
├── CTR < 1% (below benchmark)
├── Impressions > 500
Date range: Previous 7 days
Frequency: Weekly


RULE 11: QUALITY SCORE DROP ALERT
──────────────────────────────────
Goal: Monitor Quality Score declines

Apply to: Keywords with label "Monitor-QS"
Action: Send email notification
Conditions:
├── Quality Score < 5
├── Status: Enabled
├── Impressions > 100
Date range: Previous 30 days
Frequency: Weekly


RULE 12: ZERO IMPRESSIONS ALERT
────────────────────────────────
Goal: Detect campaigns without delivery

Apply to: All enabled campaigns
Action: Send email notification
Conditions:
├── Impressions = 0
├── Budget > €10
Date range: Yesterday
Frequency: Daily (10:00)


RULE 13: CONVERSION TRACKING ISSUE ALERT
─────────────────────────────────────────
Goal: Detect possible tracking problems

Apply to: All enabled campaigns
Action: Send email notification
Conditions:
├── Clicks > 100
├── Conversions = 0
├── Historical conversion rate > 1% (conversions expected)
Date range: Yesterday
Frequency: Daily
```

### Scheduling Rules

```
SCHEDULING AUTOMATION
═════════════════════

RULE 14: WEEKDAY ONLY CAMPAIGNS
────────────────────────────────
Goal: Pause campaigns on weekends

RULE A - Pause Friday evening:
Apply to: Campaigns with label "Weekdays-Only"
Action: PAUSE campaign
Frequency: Weekly, Friday at 22:00

RULE B - Enable Monday morning:
Apply to: Paused campaigns with label "Weekdays-Only"
Action: ENABLE campaign
Frequency: Weekly, Monday at 06:00


RULE 15: BUSINESS HOURS ONLY
─────────────────────────────
Goal: Only advertise during business hours

RULE A - Enable morning:
Apply to: Campaigns with label "Business-Hours"
Action: ENABLE campaign
Frequency: Daily (Weekdays), at 08:00

RULE B - Pause evening:
Apply to: Campaigns with label "Business-Hours"
Action: PAUSE campaign
Frequency: Daily (Weekdays), at 18:00


RULE 16: SEASONAL CAMPAIGN ACTIVATION
──────────────────────────────────────
Goal: Automatic activation for promotional periods

Enable Rule:
Apply to: Campaigns with label "BlackFriday2025"
Action: ENABLE campaign
Frequency: One time, specific date (e.g., Nov 20 09:00)

Pause Rule:
Apply to: Campaigns with label "BlackFriday2025"
Action: PAUSE campaign
Frequency: One time, specific date (e.g., Dec 2 23:00)


RULE 17: PAYDAY BUDGET BOOST
─────────────────────────────
Goal: Increase budget around paydays (25th-5th)

Apply to: Campaigns with label "Payday-Boost"
Action: INCREASE budget by 30%
Frequency: Monthly, 24th at 06:00

Reset Rule:
Apply to: Campaigns with label "Payday-Boost"
Action: Set budget to [original value]
Frequency: Monthly, 6th at 06:00

Tip: Note original budgets before the reset.
```

## Advanced Rule Strategies

### Rule Combinations

```
LAYERED AUTOMATION STRATEGY
════════════════════════════

TIER 1: PROTECTION RULES (Highest priority)
────────────────────────────────────────────
├── Budget overrun prevention
├── Zero conversion pauses (after €100+ spend)
└── Anomaly detection alerts

TIER 2: OPTIMIZATION RULES
───────────────────────────
├── Bid adjustments (weekly)
├── Budget scaling (weekly)
└── Performance-based pauses

TIER 3: SCHEDULING RULES
─────────────────────────
├── Time-based enables/pauses
├── Day-of-week adjustments
└── Seasonal activations

TIER 4: MONITORING RULES
─────────────────────────
├── Performance alerts
├── Tracking issue detection
└── Competitive alerts

EXECUTION ORDER:
────────────────
Protection > Optimization > Scheduling > Monitoring

Run protection rules first (hourly) so they can
override other rules if needed.
```

### Labels for Rule Management

```
LABEL STRATEGY FOR AUTOMATED RULES
═══════════════════════════════════

LABEL NAMING CONVENTION:
────────────────────────
[Category]-[Specific]

Categories:
├── Auto- : Automated rule target
├── Exclude- : Exclude from automation
├── Monitor- : Monitoring only
├── Seasonal- : Seasonal items
└── Test- : A/B test items

EXAMPLES:
─────────
├── Auto-Scale         → Budget scaling rules
├── Auto-Bid           → Bid adjustment rules
├── Auto-Pause         → Auto-pause candidates
├── Exclude-Rules      → Never auto-modify
├── Monitor-QS         → Quality Score monitoring
├── Monitor-CPA        → CPA threshold monitoring
├── Seasonal-Q4        → Q4 / Holiday campaigns
├── Seasonal-Summer    → Summer campaigns
├── Test-Creative      → Creative testing
└── Test-Bid           → Bid experiment

LABEL APPLICATION:
──────────────────
Google Ads → Campaigns/Ad Groups/Keywords
→ Select items → Apply labels

Tip: Create labels before creating rules.
     Rules can only target existing labels.
```



See [decision-trees.md](references/decision-trees.md) for details.



## Rule Management Best Practices

### Setup Checklist

```
AUTOMATED RULES SETUP CHECKLIST
════════════════════════════════

FOR EACH RULE:
──────────────
□ Clear name (describes action + condition)
□ Preview executed and checked
□ Email notification enabled
□ Correct date range selected
□ Appropriate frequency chosen
□ Labels applied where needed

NAMING CONVENTION:
──────────────────
[Action]-[Object]-[Condition]-[Frequency]

Examples:
├── PAUSE-Keywords-NoConv100Spend-Weekly
├── ALERT-Campaigns-CPAOver50-Daily
├── BUDGET-Increase15-LowCPA-Weekly
├── ENABLE-Seasonal-BlackFriday-OneTime
└── BID-Decrease10-HighCPA-Weekly

DOCUMENTATION:
──────────────
Create a Google Sheet with:
├── Rule name
├── Purpose
├── Conditions
├── Action
├── Frequency
├── Last reviewed date
├── Owner

TESTING:
────────
1. Always PREVIEW before activation
2. Start with ALERT ONLY (no action)
3. Monitor for 1-2 weeks
4. Activate action after validation
5. Review monthly
```

### Common Mistakes

```
COMMON MISTAKES TO AVOID
═════════════════════════

MISTAKE 1: Overly aggressive thresholds
────────────────────────────────────────
✗ Pause on first day without conversions
✓ Wait for sufficient data (€100+ spend)

MISTAKE 2: No maximum/minimum limits
─────────────────────────────────────
✗ Increase bid 10% every week (unlimited)
✓ Set Max CPC at €5.00

MISTAKE 3: Wrong date range
────────────────────────────
✗ CPA check on "same day" (too little data)
✓ Use 7-14 days for reliable metrics

MISTAKE 4: No preview before activation
────────────────────────────────────────
✗ Activate without checking which items are affected
✓ Always preview, screenshot results

MISTAKE 5: Conflicting rules
─────────────────────────────
✗ Rule A: Pause if CPA > 50
  Rule B: Enable if CPA < 60
  (Campaigns flip on/off continuously)
✓ Use labels to prevent conflicts
✓ Ensure clear, non-overlapping conditions

MISTAKE 6: No recovery mechanism
─────────────────────────────────
✗ Auto-pause without re-enable logic
✓ Create complementary enable rules
✓ Use labels for tracking

MISTAKE 7: Over-automation
──────────────────────────
✗ Rules for everything, no human review
✓ Balance: Automation + periodic manual review
```

### Monitoring & Maintenance

```
RULE MAINTENANCE SCHEDULE
═════════════════════════

DAILY:
──────
□ Check email alerts
□ Review unexpected actions
□ Validate rule execution log

WEEKLY:
───────
□ Review rule results
├── How many items affected?
├── Expected outcomes?
└── Any edge cases?

□ Check for conflicts
□ Adjust thresholds if needed

MONTHLY:
────────
□ Full rule audit
├── Are all rules still relevant?
├── Thresholds up to date?
└── Business goals changed?

□ Performance review
├── Impact on account performance
├── Time saved vs manual
└── Optimization opportunities

QUARTERLY:
──────────
□ Strategic review
├── New automation opportunities
├── Rules that can be removed
└── Script vs rule evaluation

RULE AUDIT LOG:
───────────────
Google Ads → Tools → Change History
Filter: Automated rules
├── When executed
├── Which items affected
└── What was the action
```

## Output: Automated Rules Template

```markdown
# Automated Rules Configuration Document

## Account Details
- **Account:** [Account name]
- **Account ID:** [XXX-XXX-XXXX]
- **Rules Owner:** [Name]
- **Last Review:** [Date]



See [detailed-reference.md](references/detailed-reference.md) for details.



## Labels in Use
| Label | Purpose | Applied To |
|-------|---------|-----------|
| Auto-Scale | Budget/bid automation | Campaigns |
| Auto-Bid | Bid adjustment automation | Keywords |
| Exclude-Rules | Never auto-modify | Various |
| Monitor-QS | QS monitoring | Keywords |

## Rule Dependencies
```
┌─────────────────────────────────────────┐
│ Protection Rules (Hourly)               │
│ ↓ Block optimization if budget cap hit │
├─────────────────────────────────────────┤
│ Optimization Rules (Weekly)             │
│ ↓ Adjust bids/budgets                  │
├─────────────────────────────────────────┤
│ Scheduling Rules (As scheduled)         │
│ ↓ Time-based enable/pause              │
├─────────────────────────────────────────┤
│ Alert Rules (Daily/Weekly)              │
│ → Notifications only                   │
└─────────────────────────────────────────┘
```

## Change Log
| Date | Rule | Change | Reason | By |
|------|------|--------|--------|-----|
| [Date] | [Rule name] | [What changed] | [Why] | [Name] |

## Notes
[Additional notes about the automation setup]
```
