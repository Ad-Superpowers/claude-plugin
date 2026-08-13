---
name: meta-automated-rules-builder
description: "This skill should be used when the user asks to \"create automated rules\", \"set up budget protection\", \"build performance rules\", or mentions \"Meta automated rules\", \"rule-based optimization\", or \"auto-pause rules\". Do NOT use for: bid strategy selection (use bid-strategy-selector), workflow process optimization (use workflow-optimizer), campaign structure (use campaign-structure-advisor)."
---
# Automated Rules Builder

## Overview

This skill helps set up automated rules in Meta Ads Manager that continuously monitor your campaigns and automatically take actions based on performance metrics, saving time and enabling fast responses to changes.

## Automated Rules Fundamentals

### What Are Automated Rules?

```
┌─────────────────────────────────────────────────────────────────┐
│  HOW AUTOMATED RULES WORK                                       │
│                                                                 │
│  1. TRIGGER: When does Meta check the rule?                     │
│     └── Every 30 min, daily, or custom interval                 │
│                                                                 │
│  2. CONDITION: Which criteria must be met?                      │
│     └── E.g.: CPA > $25 AND Impressions > 1000                 │
│                                                                 │
│  3. ACTION: What happens when the condition is true?            │
│     └── Pause, change budget, adjust bid, notification          │
│                                                                 │
│  4. SCOPE: Which items does the rule apply to?                  │
│     └── Campaigns, Ad Sets, or Ads                              │
└─────────────────────────────────────────────────────────────────┘
```

### Rules Location in Meta

```
NAVIGATION:
Ads Manager → Rules → Create Rule
OR
Ads Manager → Select items → Rules → Create New Rule

RULE TYPES:
├── Reduce Audience Overlap
├── Reduce Auction Overlap
├── Optimize Ad Creative
└── Custom Rule (most flexible)
```

## Rule Categories & Use Cases

### Category 1: Budget Protection Rules

```
GOAL: Prevent budget waste on poor performance

RULE: CPA Limit Pause
├── Apply to: Ad Sets (active)
├── Action: Turn off ad set
├── Conditions:
│   ├── Cost per Result > $[MAX CPA]
│   └── Impressions > 1000 (wait for data)
├── Time Range: Last 3 days
├── Schedule: Continuously
└── Notification: On

RULE: ROAS Minimum Guard
├── Apply to: Campaigns
├── Action: Turn off campaign
├── Conditions:
│   ├── Purchase ROAS < [MIN ROAS]
│   └── Amount Spent > $100
├── Time Range: Last 7 days
├── Schedule: Continuously
└── Notification: On
```

### Category 2: Scale Rules

```
GOAL: Automatically scale up on good performance

RULE: Increase Budget on Low CPA
├── Apply to: Ad Sets
├── Action: Increase daily budget by 20%
├── Conditions:
│   ├── Cost per Result < $[TARGET CPA - 20%]
│   └── Results > 10
├── Time Range: Last 3 days
├── Schedule: Daily at 06:00
├── Max Budget Cap: $[MAX DAILY BUDGET]
└── Notification: On

RULE: Decrease Budget on High CPA
├── Apply to: Ad Sets
├── Action: Decrease daily budget by 15%
├── Conditions:
│   ├── Cost per Result > $[TARGET CPA + 20%]
│   └── Amount Spent > $50
├── Time Range: Last 3 days
├── Schedule: Daily at 06:00
├── Min Budget Floor: $[MIN DAILY BUDGET]
└── Notification: On
```

### Category 3: Creative Management Rules

```
GOAL: Automatically pause underperforming ads

RULE: Pause Low CTR Ad
├── Apply to: Ads
├── Action: Turn off ad
├── Conditions:
│   ├── CTR (link) < 0.5%
│   └── Impressions > 3000
├── Time Range: Last 7 days
├── Schedule: Daily at 00:00
└── Notification: On

RULE: High Frequency Warning
├── Apply to: Ad Sets
├── Action: Send notification only
├── Conditions:
│   └── Frequency > 3.0
├── Time Range: Last 7 days
├── Schedule: Daily at 09:00
└── Notification: On
```

### Category 4: Learning Phase Rules

```
GOAL: Protect learning phase and prevent premature decisions

RULE: Learning Phase Budget Lock
├── Apply to: Ad Sets
├── Action: Send notification only (!)
├── Conditions:
│   ├── Delivery is "Learning"
│   └── Results < 50
├── Time Range: Last 7 days
├── Schedule: Daily
└── Notification: On
Warning: Do NOT auto-pause during learning!

RULE: Post-Learning Performance Check
├── Apply to: Ad Sets
├── Action: Turn off ad set
├── Conditions:
│   ├── Delivery is NOT "Learning"
│   ├── Cost per Result > $[TARGET CPA x 1.5]
│   └── Amount Spent > $[CPA TARGET x 50]
├── Time Range: Last 7 days
├── Schedule: Daily
└── Notification: On
```

## Rule Builder Templates

### Template 1: Complete Budget Protection Set

```
RULE SET: BUDGET PROTECTION
============================

RULE 1: Emergency Stop
├── Name: [ACCOUNT]_Emergency_Stop_High_CPA
├── Apply to: All active ad sets
├── Action: Turn off
├── Conditions:
│   ├── Cost per Purchase > $[CPA TARGET x 2]
│   └── Purchases = 0
│   └── Amount Spent > $[CPA TARGET]
├── Time Range: Today
├── Schedule: Every 30 minutes
└── Why: Stop bleeding on clearly losing ads

RULE 2: CPA Limit Daily
├── Name: [ACCOUNT]_CPA_Limit_Daily
├── Apply to: All active ad sets
├── Action: Turn off
├── Conditions:
│   ├── Cost per Purchase > $[CPA TARGET x 1.3]
│   └── Purchases > 3
├── Time Range: Last 3 days
├── Schedule: Continuously
└── Why: Pause on persistently high CPA

RULE 3: No Conversions Alert
├── Name: [ACCOUNT]_No_Conv_Alert
├── Apply to: All active ad sets
├── Action: Notification only
├── Conditions:
│   ├── Purchases = 0
│   └── Amount Spent > $[CPA TARGET x 2]
├── Time Range: Last 3 days
├── Schedule: Daily at 09:00
└── Why: Early warning on zero conversions
```

### Template 2: Auto-Scaling Rule Set

```
RULE SET: AUTO-SCALING
======================

RULE 1: Scale Up Winners
├── Name: [ACCOUNT]_Scale_Up_Winners
├── Apply to: All active ad sets
├── Action: Increase daily budget by 20%
├── Conditions:
│   ├── Cost per Purchase < $[CPA TARGET x 0.8]
│   └── Purchases > 5
│   └── Daily Budget < $[MAX BUDGET]
├── Time Range: Last 3 days
├── Schedule: Daily at 06:00
├── Budget Cap: $[MAX DAILY BUDGET]
└── Why: Allocate budget to winners

RULE 2: Scale Down Losers
├── Name: [ACCOUNT]_Scale_Down_Losers
├── Apply to: All active ad sets
├── Action: Decrease daily budget by 20%
├── Conditions:
│   ├── Cost per Purchase > $[CPA TARGET x 1.2]
│   └── Purchases > 3
│   └── Daily Budget > $[MIN BUDGET]
├── Time Range: Last 3 days
├── Schedule: Daily at 06:00
├── Budget Floor: $[MIN DAILY BUDGET]
└── Why: Automatically reduce losers

RULE 3: Weekend Budget Boost
├── Name: [ACCOUNT]_Weekend_Boost
├── Apply to: All active campaigns
├── Action: Increase daily budget by 30%
├── Conditions:
│   └── Current day is Saturday OR Sunday
├── Schedule: Custom (Fri 18:00)
└── Why: Extra budget for weekend traffic
```

### Template 3: Creative Rotation Rules

```
RULE SET: CREATIVE MANAGEMENT
=============================

RULE 1: Kill Low Performers
├── Name: [ACCOUNT]_Kill_Low_CTR
├── Apply to: All active ads
├── Action: Turn off ad
├── Conditions:
│   ├── CTR (link click-through rate) < 0.5%
│   └── Impressions > 5000
├── Time Range: Last 7 days
├── Schedule: Daily at 00:00
└── Why: Stop budget going to bad ads

RULE 2: High Frequency Warning
├── Name: [ACCOUNT]_Frequency_Alert
├── Apply to: All active ad sets
├── Action: Send notification only
├── Conditions:
│   └── Frequency > 3.5
├── Time Range: Last 7 days
├── Schedule: Daily at 09:00
└── Why: Signal for creative refresh

RULE 3: Cost per ThruPlay Alert
├── Name: [ACCOUNT]_Video_Cost_Alert
├── Apply to: Video ads
├── Action: Turn off ad
├── Conditions:
│   ├── Cost per ThruPlay > $0.15
│   └── ThruPlays > 500
├── Time Range: Last 7 days
├── Schedule: Daily
└── Why: Pause expensive video ads
```

## Condition Builder Guide

### Available Metrics

```
PERFORMANCE METRICS:
├── Results (conversions of choice)
├── Cost per Result
├── Impressions
├── Reach
├── Frequency
├── CPM (cost per 1000 impressions)
├── CPC (cost per click)
├── CTR (click-through rate)
├── Amount Spent

CONVERSION METRICS:
├── Purchases
├── Cost per Purchase
├── Purchase ROAS
├── Leads
├── Cost per Lead
├── Add to Carts
├── Checkouts Initiated

VIDEO METRICS:
├── Video Plays
├── ThruPlays
├── Cost per ThruPlay
├── Video Average Play Time
├── Video Plays at 25%, 50%, 75%, 100%

STATUS METRICS:
├── Delivery (Learning, Active, etc.)
├── Current Day (Mon, Tue, etc.)
├── Current Time
```

### Condition Combinations

```
AND vs OR LOGIC:

AND (all conditions must be true):
├── CPA > $20 AND Impressions > 1000
└── Both must be true for action

OR (one condition is enough):
├── CPA > $30 OR CTR < 0.3%
└── Either one triggers action

COMPLEX EXAMPLE:
(CPA > $25 AND Purchases > 5) OR (CTR < 0.5% AND Impressions > 5000)
```

## Best Practices & Warnings

### Do's

```
RECOMMENDED:
├── Always add "AND Impressions > X"
│   └── Prevents decisions on insufficient data
├── Use 3-7 day time ranges
│   └── Balance between responsiveness and reliability
├── Set budget caps/floors on scaling rules
│   └── Prevents runaway budgets
├── Test rules on a small subset first
│   └── Validate before broad rollout
├── Document your rules
│   └── Know why you set something up
└── Check rules weekly
    └── Adjust thresholds as metrics change
```

### Don'ts

```
AVOID:
├── Auto-pausing during Learning Phase
│   └── Let learning phase complete (50 conv)
├── Too short time ranges (Today/Yesterday)
│   └── Too volatile, unreliable data
├── Too low impression thresholds
│   └── Minimum 1,000+ for reliable CTR
├── Conflicting rules
│   └── Rule A increases, Rule B decreases simultaneously
├── Forgotten rules still running
│   └── Audit monthly
└── No notifications enabled
    └── Always know what's happening
```

## Rule Audit Checklist

### Monthly Review

```
RULE AUDIT CHECKLIST
====================

□ INVENTORY
├── How many rules are active?
├── Which rules haven't triggered in >30 days?
└── Are there conflicting rules?

□ THRESHOLDS
├── Do CPA targets still match current performance?
├── Are budget caps/floors still relevant?
└── Are impression minimums sufficient?

□ PERFORMANCE
├── Which rules have triggered most often?
├── Have auto-actions had the expected effect?
└── Are there false positives/negatives?

□ CLEANUP
├── Remove inactive rules
├── Update naming conventions
└── Document changes
```

## MCP Tool Integration

### Pulling Live Data Before Setting Thresholds

Before building rules, always check current account performance to set realistic thresholds:

```
STEP 1: Get recent CPA baseline
→ meta_get_insights(account_id="...", fields=["cost_per_action_type","spend","actions"], date_preset="last_7d", level="adset")

STEP 2: Check frequency levels
→ meta_get_insights(account_id="...", fields=["frequency","impressions"], date_preset="last_7d", level="adset")

STEP 3: Review current learning phase status
→ meta_get_insights(account_id="...", fields=["spend","impressions","actions"], date_preset="last_3d", level="adset")
```

Use the actual CPA from `meta_query` results to set rule thresholds — never guess.

## Example Interaction

**User**: "I want to set up rules so my ads automatically stop if the CPA gets too high. My target CPA is $15."

**Claude response**:

"Let me first check your current account performance to set accurate thresholds.

```
meta_get_insights(account_id="...", fields=["cost_per_action_type","impressions","spend"], date_preset="last_7d", level="adset")
```

Based on those results, I'll build a complete rule set for CPA protection. With a target CPA of $15, I'd suggest the following:

---

**RULE SET: CPA Protection (Target: $15)**

**Rule 1: Emergency Stop**
```
Name: CPA_Emergency_Stop
Apply to: All active ad sets
Action: Turn OFF ad set
Conditions:
├── Cost per Purchase > $30 (2x target)
└── Impressions > 500
Time Range: Today
Schedule: Every 30 minutes
```
*Stops immediately on extreme CPA*

---

**Rule 2: CPA Limit**
```
Name: CPA_Limit_Pause
Apply to: All active ad sets
Action: Turn OFF ad set
Conditions:
├── Cost per Purchase > $19.50 (1.3x target)
└── Purchases > 3
Time Range: Last 3 days
Schedule: Continuously
```
*Pauses on persistently high CPA*

---

**Rule 3: No Conversion Alert**
```
Name: No_Conv_Warning
Apply to: All active ad sets
Action: Send notification only
Conditions:
├── Purchases = 0
└── Amount Spent > $30 (2x target)
Time Range: Last 3 days
Schedule: Daily at 09:00
```
*Warning on zero conversions*

---

**Important:**
- Do NOT set an auto-pause rule during learning phase
- Wait until you've had at least 50 conversions
- Check after 1 week whether the thresholds are working well

After rules are live, monitor via:
```
meta_get_insights(account_id="...", fields=["cost_per_action_type","spend","impressions"], date_preset="last_3d", level="adset")
```

Would you like me to also add scaling rules for when CPA is below target?"
