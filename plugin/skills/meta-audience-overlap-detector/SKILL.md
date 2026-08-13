---
name: meta-audience-overlap-detector
description: "This skill should be used when the user asks to \"detect audience overlap\", \"consolidate audiences\", \"set up exclusion strategies\", or mentions \"audience overlap\", \"self-bidding\", or \"internal auction competition\". Do NOT use for: campaign structure advice (use campaign-structure-advisor), lookalike strategy (use lookalike-strategy-planner), full-funnel design (use full-funnel-designer)."
---
# Audience Overlap Detector

## Overview

This skill helps identify audience overlap in Meta Ads accounts, which leads to internal competition (self-bidding), higher costs, and inconsistent delivery. It provides frameworks for overlap analysis and solution strategies.

## Why Overlap Is Problematic

```
┌─────────────────────────────────────────────────────────────────┐
│  AUCTION DYNAMICS WITH OVERLAP                                   │
│                                                                 │
│  User "Anna" is in:                                             │
│  ├── Ad Set A: Interest "Fitness"                               │
│  ├── Ad Set B: Lookalike 1% Purchasers                          │
│  └── Ad Set C: Website Visitors 30d                             │
│                                                                 │
│  Result:                                                        │
│  ├── You bid 3x against yourself for the same impression        │
│  ├── CPM rises artificially                                     │
│  ├── Budget is distributed inefficiently                        │
│  └── Learning phase takes longer (split data)                   │
└─────────────────────────────────────────────────────────────────┘
```

## Overlap Check Method

### Step 1: Audience Overlap Tool (Meta)

```
Location: Ads Manager → Audiences → Select 2+ audiences →
          Actions → Show Audience Overlap

Interpretation:
├── <10% overlap: Acceptable, no action needed
├── 10-30% overlap: Monitor, consider exclusions
├── 30-50% overlap: Problematic, consolidate or exclude
└── >50% overlap: Critical, merge audiences
```

### Step 2: Create Overlap Matrix

Ask the user to share their audiences, and create a matrix:

```
AUDIENCE OVERLAP MATRIX
=======================

              │ Broad │ LAL 1% │ LAL 3% │ Interest │ Retarg │
──────────────┼───────┼────────┼────────┼──────────┼────────┤
Broad         │   -   │  15%   │  25%   │   35%    │   5%   │
LAL 1%        │  15%  │   -    │  70%   │   20%    │  10%   │
LAL 3%        │  25%  │  70%   │   -    │   30%    │  15%   │
Interest      │  35%  │  20%   │  30%   │    -     │   8%   │
Retargeting   │   5%  │  10%   │  15%   │    8%    │   -    │

Critical: LAL 1% <> LAL 3% = 70% overlap
Warning: Broad <> Interest = 35% overlap
```

## Overlap Scenarios & Solutions

### Scenario 1: Lookalike Overlap

**Problem**: LAL 1%, LAL 2%, LAL 3% running simultaneously

```
CURRENT SITUATION:
├── Ad Set 1: LAL 1% Purchasers
├── Ad Set 2: LAL 2% Purchasers
└── Ad Set 3: LAL 3% Purchasers

OVERLAP: 60-80% between adjacent percentages

SOLUTION A - Layered Lookalikes:
├── Ad Set 1: LAL 0-1%
├── Ad Set 2: LAL 1-3% (exclude 0-1%)
└── Ad Set 3: LAL 3-5% (exclude 0-3%)

SOLUTION B - Consolidation:
└── Ad Set 1: LAL 0-3% (single audience)

SOLUTION C - Source Differentiation:
├── Ad Set 1: LAL 1% from Purchasers
├── Ad Set 2: LAL 1% from High-Value Customers
└── Ad Set 3: LAL 1% from Email Subscribers
```

### Scenario 2: Interest vs Lookalike Overlap

**Problem**: Interest audiences overlap with lookalikes

```
CURRENT SITUATION:
├── Ad Set 1: Interest "Luxury Fashion"
└── Ad Set 2: LAL 2% Purchasers (luxury items)

OVERLAP: 25-40% typical

SOLUTION A - Interest Exclusion:
├── Ad Set 1: Interest "Luxury Fashion"
│   └── EXCLUDE: LAL 2% Purchasers
└── Ad Set 2: LAL 2% Purchasers

SOLUTION B - Broad Audience:
└── Ad Set 1: Advantage+ Audience
    └── Suggestion: Interest "Luxury Fashion"
    (Let algorithm optimize)
```

### Scenario 3: Retargeting Overlap

**Problem**: Multiple retargeting audiences overlap

```
CURRENT SITUATION:
├── Ad Set 1: All Website Visitors (30d)
├── Ad Set 2: Product Page Viewers (30d)
└── Ad Set 3: Add to Cart (14d)

OVERLAP: Product viewers AND ATC are also in "All visitors"

SOLUTION - Funnel Exclusions:
├── Ad Set 1: All Visitors (30d)
│   └── EXCLUDE: Product Viewers + ATC
├── Ad Set 2: Product Viewers (30d)
│   └── EXCLUDE: ATC
└── Ad Set 3: Add to Cart (14d)
    └── EXCLUDE: Purchasers (7d)
```

## Exclusion Strategy Framework

### Vertical Exclusions (Funnel-based)

```
TOFU CAMPAIGN
├── Target: Broad/Cold audiences
└── Exclude: All warm + hot audiences

MOFU CAMPAIGN
├── Target: Engagers, video viewers
└── Exclude: High-intent (ATC, IC) + purchasers

BOFU CAMPAIGN
├── Target: ATC, View Content, IC
└── Exclude: Recent purchasers (7-14d)
```

### Horizontal Exclusions (Within the same stage)

```
When you have multiple ad sets in one campaign:

Ad Set A: Interest Stack 1
└── Exclude: Custom Audience from Interest Stack 2

Ad Set B: Interest Stack 2
└── Exclude: Custom Audience from Interest Stack 1

OR use Advantage Campaign Budget (API field: campaign_budget_optimization)
to let Meta automatically distribute budget without overlap issues.

NOTE (2026): With Advantage+ Audience enabled, Meta's Andromeda engine
handles much of the overlap routing automatically. Manual exclusions
are still recommended for funnel separation (TOFU/MOFU/BOFU).
```

## Account Audit Checklist

### Ask the user for this info:

```
OVERLAP AUDIT QUESTIONNAIRE
============================

1. AUDIENCE INVENTORY
   □ How many active audiences do you have?
   □ Which types? (LAL, Interest, Custom, Saved)
   □ Which windows do you use for retargeting?

2. CAMPAIGN STRUCTURE
   □ How many campaigns are running simultaneously?
   □ Do multiple campaigns use the same audiences?
   □ Do you have exclusions set up?

3. SIGNS OF OVERLAP
   □ Fluctuating delivery between ad sets?
   □ Unexpectedly high CPMs?
   □ Ad sets stuck in learning phase?
   □ Inconsistent results with equal budgets?
```

## Overlap Diagnosis Decision Tree

```
START: Suspected overlap
│
├─► Check 1: Are you using LAL 1%, 2%, 3% simultaneously?
│   ├── YES → Consolidate or layer with exclusions
│   └── NO → Go to Check 2
│
├─► Check 2: Are interest + LAL audiences running simultaneously?
│   ├── YES → Check overlap %, exclude if >20%
│   └── NO → Go to Check 3
│
├─► Check 3: Do you have retargeting audiences without exclusions?
│   ├── YES → Implement funnel-based exclusions
│   └── NO → Go to Check 4
│
├─► Check 4: Are multiple campaigns running on the same audiences?
│   ├── YES → Consolidate campaigns or split audiences
│   └── NO → Overlap is probably not the problem
│
└─► RESULT: Implement recommended exclusion strategy
```

## Audience Consolidation Guide

### When to Consolidate?

| Situation | Action |
|----------|--------|
| 2+ ad sets with >50% overlap | Merge into 1 ad set |
| LAL 1% + LAL 2% + LAL 3% | Use LAL 0-3% or layer |
| 5+ interest ad sets | Consolidate to 2-3 stacks |
| Multiple retargeting windows | Use longest window + exclusions |

### Consolidation Template

```
FROM (fragmented):
├── Campaign 1
│   ├── Ad Set: LAL 1% - €20/day
│   ├── Ad Set: LAL 2% - €20/day
│   └── Ad Set: LAL 3% - €20/day
└── Total: €60/day, lots of overlap

TO (consolidated):
├── Campaign 1
│   ├── Ad Set: LAL 0-2% - €40/day
│   └── Ad Set: LAL 2-5% - €20/day (exclude 0-2%)
└── Total: €60/day, minimal overlap
```

## Performance Impact Monitoring

### Metrics to track after overlap fix:

```
BEFORE/AFTER COMPARISON
========================

Metric              │ Before Fix │ After Fix │ Goal
────────────────────┼────────────┼───────────┼─────────
CPM                 │   €12.50   │   €9.80   │ ↓ 15-25%
Frequency (7d)      │    4.2     │    2.8    │ ↓ to <3
Delivery Stability  │  Volatile  │  Stable   │ Consistent
Learning Phase Exit │   Slow     │  Faster   │ <7 days
Budget Spend Rate   │  Uneven    │   Even    │ Consistent
```

## Example Interaction

**User**: "My CPMs have risen enormously in recent weeks and some ad sets are barely getting delivery. Could it be overlap?"

**Claude response**:

"That does sound like possible audience overlap. Let's check:

**Can you tell me:**
1. Which audiences are currently running?
2. Have you recently added new ad sets?
3. Are you using multiple Lookalike percentages (1%, 2%, 3%)?
4. Do you have exclusions set up between your ad sets?

**Typical signs of overlap:**
- Rising CPMs without external reason
- Some ad sets getting no delivery
- Ad sets stuck in learning phase for a long time
- Inconsistent costs between similar ad sets

Share your account ID and I'll check the overlap directly!"

## MCP Tool Usage

### Step 1: List custom audiences to find IDs

```python
meta_query(
    account_id="act_XXXXXXXXX",
    entity_type="customaudiences"
)
```

### Step 2: Get overlap between any 2+ audiences

```python
meta_query(
    account_id="act_XXXXXXXXX",
    entity_type="audienceoverlap",
    entity_id="AUDIENCE_ID_1,AUDIENCE_ID_2"
)
```

### Step 3: List active ad sets to see which audiences are in use

```python
meta_query(
    account_id="act_XXXXXXXXX",
    entity_type="adsets",
    effective_status=["ACTIVE"],
    fields=["name", "targeting", "status", "daily_budget"]
)
```

Cross-reference the audience IDs in `targeting.custom_audiences` across ad sets to spot duplicates, then use the overlap data from Step 2 to quantify the issue.
