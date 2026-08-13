---
name: tiktok-learning-phase-tracker
description: "This skill should be used when the user asks to \"manage TikTok learning phase\", \"fix TikTok learning limited status\", \"predict TikTok edit impact\", or mentions \"TikTok ad group stuck in learning\", \"TikTok 50 conversions requirement\", or \"when to edit TikTok campaigns\". Do NOT use for: TikTok creative fatigue detection (use tiktok-creative-fatigue-tracker), TikTok benchmark lookups (use tiktok-benchmark-database), or TikTok attribution questions (use tiktok-attribution-guide)."
---
# TikTok Learning Phase Tracker

Analyzer for TikTok Ads learning phase management. Predicts edit impact and advises on optimal timing for changes.

## Learning Phase Basics

### What Is TikTok's Learning Phase?

```
TIKTOK LEARNING PHASE EXPLAINED
================================

Period during which TikTok's algorithm collects data about:
+-- Which users are most relevant
+-- Optimal bid prices per auction
+-- Best times and placements
+-- Creative performance patterns

STATUS INDICATORS:
+-- "Learning": Algorithm is collecting data
+-- "Active": Exited, stable optimization
+-- "Learning Limited": Not enough conversions
+-- "Not Delivering": Budget/bid issues
```

### Exit Criteria

```
TIKTOK EXIT REQUIREMENTS
========================

MINIMUM REQUIREMENTS:
+-- 50 conversion events per week per ad group
+-- 72-hour initial learning window
+-- Sufficient budget for target CPA
+-- Stable creative performance

FORMULA FOR MINIMUM BUDGET:
Daily Budget = (Target CPA x 50) / 7

EXAMPLE:
+-- Target CPA: EUR20
+-- Minimum weekly: EUR20 x 50 = EUR1,000
+-- Minimum daily: EUR1,000 / 7 = EUR143/day
+-- With buffer (1.5x): EUR215/day recommended

72-HOUR RULE:
+-- First 72 hours: Make NO changes
+-- Algorithm learns fundamental patterns
+-- Edits during this period = reset learning
+-- Avoid even small changes
```

### Learning Phase Statuses

```
STATUS INTERPRETATION
=====================

STATUS: Learning (Normal)
+-- Duration: 0-7 days
+-- Meaning: Algorithm is actively learning
+-- Action: WAIT, do not change
+-- Expectation: CPA fluctuates 30-50%
+-- Exit: After 50+ conversions/week

STATUS: Learning Limited
+-- Duration: >7 days without exit
+-- Causes:
|   +-- Budget too low
|   +-- Audience too small (<100k)
|   +-- Bid too low
|   +-- Event too rare
+-- Action: Intervene (see Exit Strategies)
+-- Urgency: High

STATUS: Active
+-- Meaning: Learning complete
+-- CPA: Stabilized
+-- Action: Optimize, scale
+-- Edits: Careful, can re-trigger

STATUS: Not Delivering
+-- Causes:
|   +-- Budget exhausted
|   +-- Bid too low for auction
|   +-- Creative rejected
|   +-- Audience exhausted
+-- Action: Diagnose and fix
+-- Urgency: Critical
```

## Smart+ Campaigns & Learning Phase

**Smart+ Campaigns** (TikTok's automated type, like Meta Advantage+) have a modified learning phase:

| Smart+ Type | Learning Requirement | Notes |
|-------------|---------------------|-------|
| Smart+ Web | 30-50 conversions/week | Similar to manual; algorithm also learns audiences |
| Smart+ App | 50 installs/week | Standard app learning applies |
| Smart+ Lead Gen | 30-50 leads/week | Form-fill based |
| **GMV Max** | 30 purchases/week | Shop-specific; 5+ day learning period |

**Key difference:** Smart+ learns both creative and audience simultaneously — you need a larger creative pool at launch (5-8 assets) to prevent learning from stalling due to creative exhaustion.

## TikTok vs Meta Learning Phase

```
PLATFORM COMPARISON
===================

Feature                | TikTok           | Meta
-----------------------+------------------+-----------------
Exit threshold         | 50/week/ad group | 50/week/ad set
Initial learning       | 72 hours strict  | 3-7 days flex
Edit sensitivity       | HIGH             | Medium
Recovery time          | 3-5 days         | 3-7 days
Consolidation impact   | Very positive    | Positive
Creative refresh impact| 4x faster fatigue| 2-3 weeks
Budget change tolerance| 20% safe         | 20% safe

KEY DIFFERENCE:
+-- TikTok = stricter 72-hour window
+-- TikTok = faster creative fatigue
+-- TikTok = more frequent consolidation needed
+-- TikTok = higher edit sensitivity
```

## Edit Impact Matrix

### Significant Edits (Trigger Learning Reset)

```
SIGNIFICANT EDITS - AVOID DURING LEARNING
==========================================

Edit Type                | Impact | Reset Risk | Recovery
-------------------------+--------+------------+----------
Budget change >20%       | High   | 90%        | 3-5 days
Audience change          | High   | 95%        | 3-7 days
Optimization goal change | High   | 100%       | 3-7 days
Bid/bid strategy change  | High   | 85%        | 3-5 days
New creative addition    | Med    | 60%        | 2-4 days
Geographic change        | High   | 90%        | 3-5 days
Schedule change          | Med    | 50%        | 2-3 days
Placement change         | Med    | 70%        | 2-4 days

WARNING - IN FIRST 72 HOURS:
+-- ALL edits trigger reset
+-- Even "minor" edits
+-- Wait until window is complete
+-- Plan changes in advance
```

### Non-Significant Edits (Usually Safe)

```
SAFE EDITS
==========

Edit Type                | Impact | Reset Risk | Notes
-------------------------+--------+------------+------------
Ad group name change     | None   | 0%         | Always safe
Campaign name change     | None   | 0%         | Always safe
Budget <20% change       | Low    | 10%        | Incremental OK
Ad creative pause        | Low    | 20%        | If others active
Bid adjustment <10%      | Low    | 15%        | Minor tweaks OK
Ad copy minor tweak      | Low    | 25%        | Text only
```

## Budget Change Impact Calculator

### Safe Budget Zones

```
BUDGET CHANGE IMPACT
====================

Current Budget: EUR[X]/day
Learning Status: [Learning/Active/Limited]

SAFE ZONE (No Reset):
+-- Maximum increase: +20% (EUR[X x 1.2])
+-- Maximum decrease: -20% (EUR[X x 0.8])
+-- Frequency: 1x per 3 days
+-- Example: EUR100 --> EUR120 is safe

YELLOW ZONE (Possible Reset):
+-- Increase: 20-40%
+-- Decrease: 20-40%
+-- Recommendation: Split into 2 steps
+-- Example: EUR100 --> EUR140 do via EUR100 --> EUR120 --> EUR140

RED ZONE (Likely Reset):
+-- Increase: >40%
+-- Decrease: >40%
+-- Recommendation: Duplicate ad group
+-- Example: EUR100 --> EUR200 = create new ad group
```

### Budget Change Decision Tree

```
WANT TO INCREASE BUDGET?
|
+--> <20% increase
|    +--> Status: Active --> Apply directly
|    +--> Status: Learning --> Wait until Active
|
+--> 20-40% increase
|    +--> Split into 2 steps (10-20% each)
|    +--> Wait 3 days between steps
|    +--> Monitor CPA after each step
|
+--> >40% increase
     +--> DO NOT change (triggers reset)
     +--> Duplicate ad group with new budget
     +--> Let original run in parallel
     +--> Evaluate after 7 days
```

## Learning Phase Exit Strategies

### Fast Exit Tactics

```
TACTIC 1: BUDGET BOOST
======================
When: Learning Limited due to budget
How:
+-- Calculate: Target CPA x 50 / 7 x 1.5
+-- Increase budget to this level
+-- Wait 72 hours
+-- After exit: Scale back to desired level (gradually)

Example:
+-- Target CPA: EUR25
+-- Minimum: EUR25 x 50 / 7 = EUR179/day
+-- With buffer: EUR179 x 1.5 = EUR268/day
+-- After exit: Scale down 20%/3 days


TACTIC 2: CONSOLIDATION
========================
When: Multiple ad groups with low volume
How:
+-- Identify 2-3 similar ad groups
+-- Create new ad group with:
|   +-- Combined budget
|   +-- Best creatives from all groups
|   +-- Broader audience (union)
+-- Pause originals
+-- Monitor new ad group

Benefit:
+-- Aggregated data = faster learning
+-- More efficient budget usage
+-- Less fragmentation
+-- TikTok prefers consolidated structure


TACTIC 3: HIGHER-FUNNEL EVENT
=============================
When: Conversion event is too rare
How:
+-- Temporarily optimize for:
|   +-- AddToCart instead of Purchase
|   +-- InitiateCheckout instead of Purchase
|   +-- ViewContent instead of Lead
+-- More events = faster learning
+-- After exit: Switch back to lower-funnel
+-- Note: Traffic quality may change

When NOT to use:
+-- You already have enough volume
+-- Budget is the problem (not event frequency)
+-- Quality/fraud concerns


TACTIC 4: BROADER TARGETING
===========================
When: Audience too small (<100k)
How:
+-- Remove narrowing restrictions
+-- Expand age ranges
+-- Add similar interests
+-- Test Auto-Targeting mode
+-- Let lookalike algorithm work

TikTok Specific:
+-- Auto-Targeting often better than manual
+-- Algorithm is strong in discovery
+-- Start broad, narrow later
+-- Minimum audience: 100k+ recommended
```

### Learning Limited Solutions

```
DIAGNOSIS: WHY LEARNING LIMITED?
=================================

Check 1: Budget vs CPA
+-- Current budget: EUR[X]/day
+-- Achieved CPA: EUR[Y]
+-- Conversions/week: [Z]
+-- Minimum budget: EUR Y x 50 / 7
+-- Problem? Budget < Minimum

Check 2: Audience Size
+-- Current audience: [X]
+-- Minimum recommended: 100,000
+-- Optimal: 500k-2M
+-- Problem? Audience < 100k

Check 3: Bid Competitiveness
+-- Current bid/cap: EUR[X]
+-- Suggested range: EUR[Y-Z]
+-- Winning auctions: [X]%
+-- Problem? Bid < suggested range

Check 4: Event Frequency
+-- Events/week: [X]
+-- Required: 50/week
+-- Event type: [specified]
+-- Problem? Events < 50

SOLUTION MATRIX:
|
+-- Budget issue --> Tactic 1 (Budget Boost)
+-- Audience issue --> Tactic 4 (Broader Targeting)
+-- Bid issue --> Raise bid/switch to auto
+-- Event issue --> Tactic 3 (Higher-Funnel)
```

## 72-Hour Rule Management

```
72-HOUR LEARNING WINDOW PROTOCOL
================================

HOUR 0-24:
├── Status: Initial data collection
├── CPA: Highly volatile (±50-100%)
├── Volume: Inconsistent
├── Action: ZERO edits
└── Monitoring: Observe only

HOUR 24-48:
├── Status: Pattern formation
├── CPA: Still volatile (±30-50%)
├── Volume: Stabilizing
├── Action: ZERO edits
└── Monitoring: Note trends

HOUR 48-72:
├── Status: Final learning phase
├── CPA: Narrowing range (±20-30%)
├── Volume: More consistent
├── Action: ZERO edits
└── Monitoring: Prepare optimization plan

HOUR 72+:
├── Status: Safe to optimize
├── Check: 50+ conversions achieved?
│   ├── Yes → Active status, can optimize
│   └── No → Learning continues, wait more
├── Action: Minor optimizations allowed
└── Caution: Still avoid significant edits
```

### Pre-Launch Checklist

```
PRE-LAUNCH CHECKLIST
====================

[ ] Budget sufficient?
    +-- Minimum: CPA target x 50 / 7
    +-- Recommended: 1.5x minimum

[ ] Audience >100k?
    +-- Check audience size estimator
    +-- Broader is better for learning

[ ] Multiple creatives?
    +-- Minimum: 3-5 ads per ad group
    +-- Mix: Different hooks, formats

[ ] Tracking correct?
    +-- Pixel events firing
    +-- Conversions registering

[ ] No changes planned?
    +-- Plan 72+ hours hands-off
    +-- Block calendar if needed

[ ] Monitoring setup?
    +-- Alerts for anomalies
    +-- Daily check-in scheduled
```

## Edit Timing Best Practices

### When to Make Changes

```
BEST TIMING FOR EDITS
=====================

IDEAL:
+-- After 72-hour window complete
+-- After 50+ conversions reached
+-- Beginning of the week (Monday/Tuesday)
+-- After stable 5-7 days of performance
+-- During daytime (avoid late-night deploys)

AVOID:
+-- First 72 hours (CRITICAL)
+-- During learning phase
+-- Weekend (less data)
+-- Peak shopping periods
+-- Directly after previous change (<3 days)
+-- During TikTok Shop mega events
+-- Late evening (monitoring difficult)
```

### Batch vs Sequential Edits

```
NEED MULTIPLE EDITS?
|
+--> Option 1: Batch All Edits
|    +-- When: Major refresh/restructure
|    +-- Advantage: Single learning reset
|    +-- Disadvantage: No isolation of impact
|    +-- Timing: Beginning of the week
|
+--> Option 2: Sequential Edits
     +-- When: Testing hypotheses
     +-- Advantage: Isolate impact per change
     +-- Disadvantage: Multiple potential resets
     +-- Spacing: 5-7 days between edits
     +-- Priority: Biggest impact first
```

## Ad Group Health Check

### Quick Health Assessment

```
AD GROUP HEALTH CHECK
=====================

[ ] Learning Status: [Learning/Active/Limited]
[ ] Days in status: [X] days
[ ] Conversions L7D: [X]
[ ] Daily budget: EUR[X]
[ ] Current CPA: EUR[X]
[ ] Target CPA: EUR[X]
[ ] Frequency L7D: [X]
[ ] CTR: [X]%
[ ] 2-sec View Rate: [X]%

HEALTH SCORE:
+-- HEALTHY: Active + 50+ conv/week + CPA <=1.2x target
+-- WARNING: Learning >7d OR 25-50 conv/week OR CPA 1.2-1.5x target
+-- CRITICAL: Limited OR <25 conv/week OR CPA >1.5x target
+-- DEAD: Not Delivering >24 hours
```

### Recommended Actions by Status

```
ACTION PER STATUS
=================

HEALTHY (Active, Performing)
+-- Action: Gentle optimization
+-- Scale: +20% budget per 3-4 days
+-- Creative: Add new (don't replace)
+-- Monitor: Weekly review
+-- Goal: Maintain momentum

WARNING (Learning Extended / Moderate Issues)
+-- Diagnose: Budget? Audience? Creative?
+-- Priority 1: Fix root cause
+-- Priority 2: Consider consolidation
+-- Avoid: Multiple changes at once
+-- Timeline: Fix within 7 days

CRITICAL (Learning Limited / Poor Performance)
+-- Diagnose: Use Learning Limited checklist
+-- Immediate: Implement exit tactic
+-- Option A: Budget boost (if budget issue)
+-- Option B: Consolidate (if fragmented)
+-- Option C: Rebuild (if fundamentally broken)
+-- Timeline: Act within 48 hours

DEAD (Not Delivering)
+-- Check 1: Budget exhausted?
+-- Check 2: Bid too low?
+-- Check 3: Creative rejected?
+-- Check 4: Audience exhausted?
+-- Immediate: Identify blocker
+-- Timeline: Fix within 24 hours
```

## Common Scenarios

### Scenario 1: Stuck in Learning (>7 days)

```
SITUATION:
+-- Ad group: 10 days in Learning
+-- Budget: EUR75/day
+-- Conversions L7D: 18
+-- CPA: EUR28
+-- Target CPA: EUR25

DIAGNOSIS:
+-- Required budget: EUR25 x 50 / 7 = EUR179/day
+-- Current budget: EUR75/day (42% of requirement)
+-- Root cause: BUDGET TOO LOW

SOLUTION:
1. Increase budget to EUR200/day (with buffer)
2. Wait for new 72-hour window
3. After learning exit: Scale back to EUR150/day
4. Achieve sustainable 50+ conv/week

ALTERNATIVE:
+-- Consolidate with other ad groups
+-- Aggregate budget = faster learning
```

### Scenario 2: Creative Refresh Needed

```
SITUATION:
+-- Ad group: Active (4 weeks)
+-- CTR: Declined from 2.1% to 1.2%
+-- CPM: Increased from EUR8 to EUR12
+-- Diagnosis: Creative fatigue (TikTok = 3-7 days!)

APPROACH:
1. DO NOT replace all creatives (triggers reset)
2. ADD new creatives to existing ad group
3. Let algorithm test new vs old
4. After 5-7 days: Pause underperformers
5. Repeat cycle with new additions

BEST PRACTICE:
+-- Add 2-3 new creatives per week
+-- Maintain 5-8 active creatives
+-- Remove bottom 20% performers
+-- Never full creative swap
```

### Scenario 3: Doubling Budget

```
SITUATION:
+-- Ad group: Active, performing well
+-- Current budget: EUR100/day
+-- Target: EUR200/day
+-- Risk: >40% increase = reset

SOLUTION A: Gradual
+-- Week 1: EUR100 --> EUR120 (+20%)
+-- Week 2: EUR120 --> EUR145 (+20%)
+-- Week 3: EUR145 --> EUR175 (+20%)
+-- Week 4: EUR175 --> EUR200 (+14%)
+-- Total: 4 weeks for 2x scale (safe)

SOLUTION B: Duplication
+-- Duplicate ad group with EUR200/day budget
+-- Let original run at EUR100/day
+-- After 7-10 days: Compare performance
+-- Scale winner, pause loser
+-- Total: 2 weeks but parallel spend
```

### Scenario 4: Post-Edit Recovery

```
SITUATION:
+-- Accidentally made significant edit
+-- Learning phase triggered
+-- CPA spiked 40%

RECOVERY PROTOCOL:
1. NO FURTHER EDITS (makes it worse)
2. Monitor 72 hours without action
3. If no stabilization after 72 hours:
   +-- Check if edit was correct
   +-- Consider rollback (new reset)
   +-- Or: Accept and wait for re-learning
4. Plan buffer for future edits
5. Document for future reference

EXPECTED RECOVERY:
+-- Day 1-3: High volatility (normal)
+-- Day 4-5: Stabilizing
+-- Day 6-7: Near baseline
+-- Week 2: Fully recovered
```

## Output Templates

### Edit Impact Analysis

```markdown
# Edit Impact Analysis

## Proposed Change
- Ad Group: [name]
- Change Type: [budget/audience/creative/bid]
- Change Details: [specifics]
- Current Status: [Learning/Active/Limited]

## Risk Assessment
- Learning Reset Risk: [Low/Medium/High] ([X]%)
- Recovery Time: [X-Y] days
- Performance Impact: [Minimal/Moderate/Significant]

## Recommendation
**[PROCEED / PROCEED WITH CAUTION / DELAY / ALTERNATIVE APPROACH]**

### If Proceeding:
1. Best timing: [day/time]
2. Monitor: [specific metrics]
3. Rollback trigger: [criteria]

### Alternative Approach:
[Safer alternative if applicable]

### Post-Change Protocol:
- Hour 1-24: [actions]
- Day 2-3: [evaluation]
- Day 4-7: [optimization]
```

### Weekly Health Report

```markdown
# Ad Group Health Report - Week [X]

## Overview
| Ad Group | Status | Conv L7D | CPA | vs Target | Health |
|----------|--------|----------|-----|-----------|--------|
| [name]   | Active | [X]      | €[Y]| [+/-Z%]   | 🟢     |
| [name]   | Learning| [X]     | €[Y]| [+/-Z%]   | 🟡     |

## Actions Required
- 🔴 [Critical action]
- 🟡 [Warning action]

## Recommendations
1. [Recommendation 1]
2. [Recommendation 2]

## Next Week Plan
- [ ] [Planned optimization]
- [ ] [Creative refresh]
```

## Example Interaction

**User**: "My TikTok ad group has been in learning for 10 days with €80/day budget and 22 conversions per week. Target CPA is €30. What should I do?"

**Claude response**:

"Your ad group is in **Learning Limited** - let me run the diagnosis:

---

**DIAGNOSIS:**

| Check | Your Situation | Required | Status |
|-------|---------------|----------|--------|
| Budget | €80/day | €214/day* | 🔴 37% too low |
| Conversions | 22/week | 50/week | 🔴 56% too low |
| CPA | ~€25.45** | €30 target | 🟢 Below target |

*Calculation: €30 × 50 / 7 = €214/day minimum
**Calculation: €80 × 7 / 22 = €25.45 effective CPA

**Root Cause: Budget too low for required conversion volume**

---

**RECOMMENDED ACTION: Budget Boost (Tactic 1)**

1. **Increase budget to €250/day** (€214 + buffer)
   - This gives the algorithm enough room for 50+ conv/week

2. **Wait 72 hours** after the change (don't touch it!)

3. **After learning exit (Active status):**
   - If CPA ≤€30: Maintain €250/day budget
   - If CPA >€30: Scale back to €200/day

---

**ALTERNATIVE (if budget is limited):**

Consolidate with other ad groups to get a combined budget that can generate 50+ conversions.

---

**TIMING:**

- Implement at the start of the week (Monday/Tuesday)
- Expected recovery: 5-7 days
- Check-in: Day 4 and Day 7

Would you like me to run the budget change impact calculation for your specific situation?"

## MCP Tool Examples

Pull learning phase status and conversion volume:

```
# Check ad group status and conversion counts
tiktok_get_report(
  start_date="2026-03-28",
  end_date="2026-04-04",
  level="adgroup",
  metrics=["conversions", "cost_per_conversion", "spend", "ctr", "cpm"]
)

# List campaigns to identify which are in learning
tiktok_query(entity_type="campaigns")
```
