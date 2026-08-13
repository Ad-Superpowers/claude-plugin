---
name: meta-learning-phase-tracker
description: "This skill should be used when the user asks to \"check learning phase status\", \"predict edit impact\", \"exit learning phase faster\", or mentions \"learning phase\", \"significant edit reset\", or \"ad set health check\". Do NOT use for: campaign structure decisions (use campaign-structure-advisor), performance troubleshooting (use performance-troubleshooter), bid strategy selection (use bid-strategy-selector)."
---
# Learning Phase Tracker

Analyzer for Meta Ads learning phase management. Predicts edit impact and advises on optimal timing for changes.

## Learning Phase Basics

### What Is Learning Phase?

A period during which Meta's algorithm learns who to target and how to bid. Ad sets show "Learning" status until sufficient data has been collected.

### Exit Criteria (2026 Update)

```
Traditional rule: 50 optimization events per ad set per week

2026 Update: Some accounts see 10 conversions over 3 days
as the new threshold (Meta continues to refine this).
With ASC campaigns (unified structure since v25.0), the
algorithm has more flexibility — combined ad sets learn faster.

Practical rule of thumb: Plan for 50/week, but monitor
whether faster exit is possible.
```

### Learning Phase Statuses

| Status | Meaning | Action |
|--------|---------|--------|
| **Learning** | Algorithm is collecting data | Don't change, wait |
| **Active** | Exited, optimization is stable | Monitor and optimize |
| **Learning Limited** | Insufficient events | Increase budget or use broader targeting |

## Edit Impact Matrix

### Significant Edits (Trigger Learning Reset)

| Edit Type | Impact | Learning Reset? |
|-----------|--------|-----------------|
| Budget >20% increase | High | Usually yes |
| Budget >20% decrease | High | Usually yes |
| Audience change | High | Yes |
| New creative | High | Yes |
| Optimization goal change | High | Yes |
| Bid strategy change | High | Yes |
| Placement change | Medium | Often yes |

### Non-Significant Edits (Usually Safe)

| Edit Type | Impact | Learning Reset? |
|-----------|--------|-----------------|
| Budget <20% change | Low | Usually no |
| Ad name change | None | No |
| Campaign name change | None | No |
| Adding new ad (2026) | Variable | Sometimes not anymore |
| Minor copy tweak | Low | Usually no |

### 2026 Updates

Meta now shows messages like:
> "You can increase your budget to €[X] without restarting learning"

This provides specific safe thresholds per ad set.

## Budget Change Impact Calculator

### Safe Budget Increase Zones

```
Current Daily Budget: €[X]
Learning Phase Status: [Learning/Active/Limited]

SAFE ZONE (No Reset):
├── Increase: Up to 20% (€[X x 1.2])
└── Decrease: Up to 20% (€[X x 0.8])

YELLOW ZONE (Possible Reset):
├── Increase: 20-50% (€[X x 1.2] - €[X x 1.5])
└── Decrease: 20-50%
└── Recommendation: Do in 2 steps over 3-4 days

RED ZONE (Likely Reset):
├── Increase: >50%
└── Decrease: >50%
└── Recommendation: Duplicate ad set with new budget
```

### Budget Change Decision Tree

```
Want to increase budget?
│
├─► <20% increase
│   └─► Safe, implement directly
│
├─► 20-50% increase
│   ├─► Ad set in Learning?
│   │   └─► Wait until Active, then increase
│   └─► Ad set Active?
│       └─► Do in 2 steps (10% + 10%)
│
└─► >50% increase
    └─► Duplicate ad set with new budget
        └─► Keep original running as backup
```

## Learning Phase Exit Strategies

### Quick Exit Tactics

```
Tactic 1: Budget Boost
├── Increase budget to 3x CPA x 50 / 7 days
├── Example: CPA €20 → Budget €429/week = €61/day
└── After exit: Scale back to desired level

Tactic 2: Broader Targeting
├── Use Advantage+ Audience
├── Remove interest restrictions
├── Expand age ranges
└── More conversion opportunities = faster learning

Tactic 3: Higher-Funnel Event
├── Temporarily optimize for AddToCart instead of Purchase
├── More events = faster learning
├── After exit: Switch back to Purchase
└── Note: May affect traffic quality

Tactic 4: Consolidation
├── Merge small ad sets
├── Combine budgets
├── One strong ad set > multiple weak ones
└── Aggregated data = faster learning
```

### Learning Limited Solutions

```
Diagnosis: Why Learning Limited?
│
├─► Budget too low
│   └─► Increase to €[CPA x 50 / 7] per day
│
├─► Audience too small
│   └─► Broader targeting or merge audiences
│
├─► Too few creatives
│   └─► Add more ads (not just 1 ad per ad set)
│
├─► Event too rare
│   └─► Switch to higher-funnel event
│
└─► Competition too high
    └─► Increase budget or adjust bid strategy
```

## Edit Timing Best Practices

### When to Make Changes

```
BEST TIMING:
├── Beginning of the week (Monday/Tuesday)
│   └─► Gives algorithm weekdays to learn
│
├── After stable 5-7 days of performance
│   └─► Baseline data available for comparison
│
└── NOT during:
    ├── Learning phase (wait for exit)
    ├── Weekend (less data)
    ├── Peak periods (Black Friday, etc.)
    └── Right after previous change (<3 days)
```

### Batch Edits Strategy

```
Multiple edits needed?
│
├─► Option 1: Batch all edits together
│   ├── Advantage: One learning reset instead of multiple
│   └─► Use when: Major refresh/overhaul
│
└─► Option 2: Staggered edits
    ├── Advantage: Isolate impact per change
    ├── Wait 3-5 days between edits
    └─► Use when: Testing hypotheses
```

## Ad Set Health Check

### Quick Health Assessment

```
AD SET HEALTH CHECK

□ Learning Phase Status: [Learning/Active/Limited]
□ Days in current status: [X]
□ Conversions last 7 days: [X]
□ Daily budget: €[X]
□ Estimated CPA: €[X]
□ Frequency: [X]
□ CTR: [X]%
□ Delivery status: [Active/Limited/Off]

HEALTH SCORE:
├── Green (Healthy): Active + 50+ conv/week + Frequency <4
├── Yellow (Watch): Learning >7 days OR 25-50 conv/week
└── Red (Action needed): Limited OR <25 conv/week OR Frequency >5
```

### Recommended Actions by Status

```
STATUS: Learning (Normal)
├── Days in learning: <7
├── Action: Wait, don't make changes
└── Check again: After 7 days

STATUS: Learning (Extended)
├── Days in learning: >7
├── Action: Evaluate budget/audience/event
└── Consider: Tactic 1-4 from Exit Strategies

STATUS: Learning Limited
├── Action: Immediate intervention
├── Primary: Increase budget
├── Secondary: Broader audience
└── Tertiary: Higher-funnel event

STATUS: Active (Healthy)
├── Action: Monitor, no changes needed
├── Optimize: Test new creatives (add, don't replace)
└── Scale: 20% budget increase if performance is stable

STATUS: Active (Declining)
├── Symptoms: Rising CPA, falling ROAS
├── Diagnose: Creative fatigue? Audience saturation?
├── Action: Refresh creatives, expand audience
└── Avoid: Major restructuring (resets learning)
```

## Edit Impact Simulator

### Input Template

```
CURRENT AD SET:
- Daily budget: €[X]
- Learning status: [Learning/Active/Limited]
- Days in status: [X]
- Conv. last 7 days: [X]
- Current CPA: €[X]

PROPOSED CHANGE:
- Change type: [budget/audience/creative/bid/event]
- Change details: [specifics]
```

### Output Template

```
EDIT IMPACT ANALYSIS

Proposed Change: [description]

RISK ASSESSMENT:
├── Learning Reset Risk: [Low/Medium/High]
├── Performance Impact: [Minimal/Moderate/Significant]
└── Recovery Time: [X] days

RECOMMENDATION:
[Proceed/Proceed with caution/Delay/Alternative approach]

ALTERNATIVE APPROACH (if risky):
[Safer alternative to achieve same goal]

TIMING ADVICE:
[When to implement if proceeding]

POST-CHANGE MONITORING:
- Day 1-3: [what to monitor]
- Day 4-7: [evaluation criteria]
- Action triggers: [when to intervene]
```

## MCP: Check Learning Phase Status

```python
# Get learning phase status for all active ad sets
meta_query(account_id="act_XXXXX", entity_type="adsets", effective_status=["ACTIVE"], fields=["id","name","status","daily_budget","optimization_goal","bid_strategy"])
```

## Common Scenarios

### Scenario 1: Doubling Budget

```
Situation: Ad set performing well, want to 2x budget
Risk: High (>50% increase)

Recommendation:
1. Duplicate ad set with 2x budget
2. Keep original running on current budget
3. After 7 days: Evaluate which performs better
4. Pause the underperformer
```

### Scenario 2: Creative Refresh

```
Situation: CTR declining, want to replace all ads
Risk: High (triggers reset)

Recommendation:
1. Add new ads to existing ad set (don't replace)
2. Let algorithm test new vs old
3. Pause underperformers after 5-7 days
4. Avoid full creative swap
```

### Scenario 3: Audience Change

```
Situation: Want to add interest targeting
Risk: High (audience change = reset)

Recommendation:
1. Create new ad set with new audience
2. Keep original running in parallel
3. Compare performance after 7-14 days
4. Scale winner, pause loser
```

### Scenario 4: Stuck in Learning

```
Situation: 14 days in Learning, no progress
Diagnosis: Budget €30/day, CPA €25, 8 conv/week

Recommendation:
1. Increase budget to €90/day (€25 CPA x 50 / 7 x 0.5 buffer)
2. OR switch to AddToCart event temporarily
3. OR merge with other ad sets
4. After exit: Optimize back to desired setup
```
