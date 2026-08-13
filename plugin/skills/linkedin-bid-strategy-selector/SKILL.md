---
name: linkedin-bid-strategy-selector
description: "This skill should be used when the user asks to \"optimize LinkedIn bid strategy\", \"choose between Maximum Delivery and Manual Bidding\", \"set up LinkedIn Cost Cap\", \"reduce LinkedIn CPC\", or mentions \"LinkedIn CPL too high\" or \"LinkedIn budget pacing\". Do NOT use for: LinkedIn benchmark lookups (use benchmark-database), LinkedIn lead gen form optimization (use linkedin-lead-gen-optimizer), LinkedIn performance troubleshooting (use linkedin-performance-troubleshooter)."
---
# LinkedIn Bid Strategy Selector

Advisor for selecting the optimal LinkedIn Ads bid strategy based on goals, budget, and account situation.

## Quick Selection Guide

```
WHAT IS YOUR PRIMARY GOAL?
|
+---> Maximum volume & reach
|   +---> MAXIMUM DELIVERY
|       (Let LinkedIn optimize)
|
+---> Keep CPL/CPA under control
|   +---> COST CAP
|       (Target cost with flexibility)
|
+---> Full control over costs
    +---> MANUAL BIDDING
        (Fixed max bid per result)
```

## Bid Strategy Overview

```
LINKEDIN BID STRATEGIES COMPARISON
====================================

Strategy         | Control | Risk | Best For            | Min. Budget
-----------------+---------+------+---------------------+------------
Maximum Delivery | None    | Low  | Beginners, volume   | $25/day
Cost Cap         | Target  | Med  | CPL constraints     | $50/day
Manual Bidding   | Exact   | High | Competitive auctions| $100/day

OBJECTIVE COMPATIBILITY:

                | Max Del | Cost Cap | Manual
----------------+---------+----------+--------
Brand Awareness |   Y     |    -     |   Y
Website Visits  |   Y     |    Y     |   Y
Engagement      |   Y     |    Y     |   Y
Video Views     |   Y     |    Y     |   Y
Lead Generation |   Y     |    Y     |   Y
Conversions     |   Y     |    Y     |   Y
Job Applicants  |   Y     |    -     |   Y
```

## Maximum Delivery (Automated Bidding)

### How It Works
LinkedIn automatically optimizes your bids to get as many results as possible within your budget. No control over CPC/CPL.

### When to Use
- New accounts with little benchmark data
- Brand awareness campaigns
- Fast learning phase completion
- Uncertain about realistic bid ranges
- Fully spending the budget is the priority

### When NOT to Use
- Strict CPL requirements
- Competitive niches where costs can explode
- When you already have benchmark data

### Setup
```
Campaign Settings:
+-- Objective: [Based on goal]
+-- Bid type: Maximum Delivery
+-- Daily budget: Minimum $25/day
+-- Schedule: Continuous or custom
+-- Pacing: Standard (recommended)

Expected Behavior:
+-- Day 1-3: Learning, CPC/CPL fluctuates
+-- Day 4-7: Stabilization
+-- Week 2+: Consistent delivery
+-- CPL: Typically 10-30% above market benchmark
```

### Expectations
```
MAXIMUM DELIVERY PERFORMANCE
============================

Positive:
+-- Budget is fully spent
+-- Maximum reach/impressions
+-- Fast data collection
+-- Little management needed

Negative:
+-- No CPL/CPC control
+-- Can be expensive in competitive niches
+-- CPA variation day-to-day
+-- Less suitable for strict ROI targets
```

## Cost Cap

### How It Works
Set a target CPL/CPA. LinkedIn tries to stay around this amount on average, but can temporarily go over/under.

### When to Use
- Known target CPL from historical data
- Lead generation with established lead value
- Scaling while monitoring efficiency
- B2B with predictable sales cycles

### When NOT to Use
- No benchmark CPL available
- Target too ambitious (delivery stops)
- New accounts without data

### Cost Cap Calculation

```
DETERMINING YOUR COST CAP
================

Step 1: Determine your Lead Value
+-- Enterprise SaaS: Lead Value = ACV x Close Rate x 0.5
|   Example: $50k x 5% x 0.5 = $1,250 lead value
|
+-- SMB SaaS: Lead Value = ACV x Close Rate
|   Example: $5k x 10% = $500 lead value
|
+-- Services: Lead Value = Avg Deal x Close Rate
    Example: $10k x 15% = $1,500 lead value

Step 2: Calculate Break-Even CPL
+-- Formula: Lead Value x Target CAC Efficiency
+-- Efficiency factor: 0.10-0.20 (aggressive) to 0.30-0.40 (conservative)
|
+-- Example Enterprise:
|   $1,250 x 0.20 = $250 break-even CPL
|
+-- Example SMB:
    $500 x 0.15 = $75 break-even CPL

Step 3: Set Cost Cap
+-- Start: 1.2x break-even CPL (learning room)
+-- Week 2: Tighten to 1.1x
+-- Week 3+: Target break-even
+-- Never: Start below historical average
```

### Setup Best Practices

```
Cost Cap Implementation:
+-- Calculate break-even CPL: $[X]
+-- Start Cost Cap: $[X x 1.2]
+-- Daily Budget: Minimum $50/day
+-- Audience Size: >50,000 recommended
+-- Creative Rotation: 3-5 variants

Optimization Timeline:
+-- Week 1: Monitor, don't adjust
+-- Week 2: Tighten cap 10% if CPL stable
+-- Week 3: Fine-tune based on SQL rate
+-- Ongoing: Adjust seasonally
```

### Troubleshooting

```
COST CAP ISSUES
===============

Issue: No/Low Delivery
+-- Cause: Cap too low
+-- Check: Compare with benchmark CPL
+-- Fix: Increase cap 15-25%
+-- Alternative: Switch to Maximum Delivery temporarily

Issue: CPL above Cap
+-- Cause: Learning phase or high competition
+-- Check: Is it consistent or incidental?
+-- Fix: Wait 5-7 days, increase cap 10%
+-- Alternative: Expand audience size

Issue: Inconsistent Delivery
+-- Cause: Audience too small or cap too tight
+-- Check: Audience size (>50k?)
+-- Fix: Broaden targeting or loosen cap
+-- Alternative: Split into multiple campaigns
```

## Manual Bidding

### How It Works
You set an exact maximum bid per click/impression/lead. LinkedIn never bids more, even if this costs delivery.

### When to Use
- Competitive niches (Finance, SaaS, Enterprise)
- Experienced advertisers with lots of data
- Strict margin requirements
- Auction dynamics well understood
- A/B testing different bid levels

### When NOT to Use
- Beginners
- Low conversion volume
- Unknown bid ranges

### Determining Manual Bids

```
MANUAL BID STRATEGY
====================

For CPC Campaigns:
+-- Research: Check LinkedIn suggested bid range
+-- Start: Mid-range of suggestions
+-- Test: Run 3 ad sets with low/mid/high bids
+-- Evaluate: After 1000+ impressions per variant
+-- Optimize: Focus budget on best performing bid

Suggested Bid Interpretation:
+-- "$5.00 - $8.00" = Low competition
+-- "$8.00 - $12.00" = Medium competition
+-- "$12.00 - $20.00" = High competition
+-- ">$20.00" = Very competitive (Finance, C-suite)

Bid Positioning Strategy:
+-- Volume focus: Bid in top 25% of range
+-- Efficiency focus: Bid in bottom 50% of range
+-- Balanced: Bid at median
+-- Testing: Run parallel at different levels
```

### Bid Optimization Process

```
MANUAL BID OPTIMIZATION WORKFLOW
================================

Week 1: Discovery
+-- Set 3 bid levels: -20%, baseline, +20%
+-- Equal budget across ad sets
+-- Track: Impressions, clicks, conversions
+-- Minimum: 1000 impressions per variant

Week 2: Analysis
+-- Compare CPC, CTR, conversion rate
+-- Calculate effective CPL per bid level
+-- Identify sweet spot
+-- Document: Bid vs Performance curve

Week 3: Optimization
+-- Consolidate budget to winning bid level
+-- Fine-tune: Test +/-10% variations
+-- Scale: Increase budget 20%
+-- Monitor: Daily performance checks

Ongoing:
+-- Adjust for seasonality
+-- React to competition changes
+-- Refresh bids monthly
+-- Test new ranges quarterly
```

## Bid Strategy by Campaign Objective

### Lead Generation Campaigns

```
LEAD GEN BID STRATEGY SELECTION
===============================

Budget <$50/day
+---> Maximum Delivery
    +-- Reason: Need volume for learning
    +-- Expectation: CPL will be higher

Budget $50-150/day
+---> Cost Cap (recommended)
    +-- Start: Benchmark CPL x 1.2
    +-- Target: Benchmark CPL
    +-- Reason: Balance volume & efficiency

Budget >$150/day
+---> Manual Bidding OR Cost Cap
    +-- Manual: If competitive niche
    +-- Cost Cap: If stable market
    +-- Test: Run both parallel

Lead Gen Forms vs Website Conversions:
+-- Forms: Typically 20-30% lower CPL
+-- Website: Higher quality, higher CPL
+-- Bid: Adjust expectations accordingly
```

### Website Visits / Traffic

```
TRAFFIC CAMPAIGN BIDDING
========================

Goal: Maximum Clicks
+---> Maximum Delivery + CPC billing
    +-- Benefit: Optimize for clicks
    +-- Risk: Quality may vary

Goal: Quality Traffic
+---> Manual CPC Bidding
    +-- Set: Target CPC x 0.9
    +-- Benefit: Cost control
    +-- Risk: Lower volume

Recommended CPC Ranges by Industry:
+-- Technology: $4-8
+-- Finance: $6-12
+-- Healthcare: $4-8
+-- Education: $3-6
+-- Professional Services: $4-7
+-- General B2B: $3-6
```

### Brand Awareness / Video Views

```
AWARENESS CAMPAIGN BIDDING
==========================

Objective: Reach
+---> Maximum Delivery
    +-- Billing: CPM
    +-- Benefit: Maximum exposure
    +-- Target CPM: $30-60

Objective: Video Views
+---> Manual CPV OR Maximum Delivery
    +-- CPV target: $0.05-0.15
    +-- View threshold: 50%+ completion
    +-- Benchmark: 25% view rate = good
```

## Budget & Pacing Strategy

### Budget Allocation Framework

```
LINKEDIN BUDGET ALLOCATION
==========================

Total Monthly Budget: $[X]
|
+-- Lead Generation: 50-60%
|   +-- Lead Gen Forms: 60%
|   +-- Website Conversions: 40%
|
+-- Retargeting: 20-30%
|   +-- Website visitors: 50%
|   +-- Video viewers: 25%
|   +-- Form abandoners: 25%
|
+-- Brand Awareness: 10-20%
|   +-- Thought leadership: 60%
|   +-- Video content: 40%
|
+-- Testing: 5-10%
    +-- New creatives & audiences
```

### Pacing Options

```
PACING STRATEGY
===============

Standard Pacing (Recommended):
+-- Budget spread evenly across day
+-- Benefit: Consistent delivery
+-- Best for: Lead gen, conversions
+-- Use when: You want steady performance

Accelerated Pacing:
+-- Spend budget as fast as possible
+-- Benefit: Quick results, testing
+-- Risk: May exhaust budget early
+-- Use when: Time-sensitive campaigns

Budget Flight Recommendations:
+-- Short campaigns (<7 days): Accelerated
+-- Standard campaigns (7-30 days): Standard
+-- Always-on: Standard
+-- Peak periods: Increase budget, keep standard pacing
```

### Scaling Protocols

```
SCALING LINKEDIN CAMPAIGNS
==========================

Safe Scaling Rules:
+-- Maximum increase: 25% per 5-7 days
+-- Never: >50% at once (triggers learning)
+-- Monitor: CPL after each increase
+-- Trigger: CPL stable + SQL rate acceptable
+-- Stop: If CPL rises >25% after increase

Scaling Example:
+-- Week 1: $100/day (baseline)
+-- Week 2: $125/day (+25%)
+-- Week 3: $156/day (+25%)
+-- Week 4: $195/day (+25%)
+-- Week 5: $244/day (+25%)
+-- Result: 2.5x scale in 5 weeks

Horizontal Scaling:
+-- Duplicate winning campaign
+-- Change one variable:
|   +-- New audience segment
|   +-- New creative set
|   +-- New geography
+-- Run parallel
+-- Consolidate after 14 days
```

## High CPL Diagnosis & Resolution

```
CPL TOO HIGH - DIAGNOSIS
======================

Check 1: Benchmark Alignment
+-- Compare to industry benchmark
+-- Finance CPL $90-120 is normal
+-- SaaS CPL $80-120 is normal
+-- If within range: Expectations issue

Check 2: Audience Size
+-- <20,000: Significantly higher CPL expected
+-- 20-50,000: Moderately higher CPL
+-- 50-200,000: Optimal range
+-- >200,000: May be too broad

Check 3: Targeting Precision
+-- Too narrow: High CPM, high CPL
+-- Too broad: Low relevance, high CPL
+-- Sweet spot: Qualified audience, reasonable size

Check 4: Creative Performance
+-- CTR <0.4%: Creative issue
+-- CTR 0.4-0.6%: Normal
+-- CTR >0.6%: Strong creative
+-- Low CTR = High CPC = High CPL

Check 5: Form Friction
+-- Many fields (>5): Lower CVR, higher CPL
+-- Custom questions: May filter but increase CPL
+-- Test: Reduce fields, measure SQL impact

RESOLUTION MATRIX:

If CPL High + CTR Low -> Creative refresh needed
If CPL High + CTR Good -> Audience/targeting issue
If CPL High + CVR Low -> Form optimization needed
If CPL High + All Good -> Market rate, accept or narrow targeting
```

## Scenario-Based Recommendations

### Scenario 1: New Account Launch

```
NEW ACCOUNT - 4 WEEK PLAN
=========================

Week 1-2:
+-- Strategy: Maximum Delivery
+-- Budget: $50-75/day
+-- Goal: 30+ conversions for learning
+-- Focus: Gather benchmark data
+-- Expected CPL: 20-30% above market

Week 3:
+-- Strategy: Transition to Cost Cap
+-- Cost Cap: Achieved CPL x 1.1
+-- Budget: Maintain $50-75/day
+-- Goal: Validate efficiency
+-- Monitor: Delivery consistency

Week 4+:
+-- Strategy: Cost Cap (tightened)
+-- Cost Cap: Target benchmark
+-- Budget: Scale if CPL stable
+-- Goal: Sustainable acquisition
+-- Optimize: Creative testing
```

### Scenario 2: Scaling Profitable Campaign

```
SCALING SCENARIO
================

Current State:
+-- Spend: $75/day
+-- CPL: $85 (target: $100)
+-- SQL Rate: 22% (good)
+-- Goal: Scale to $200/day

Scaling Plan:
+-- Week 1: $75 -> $95 (+27%)
|   +-- Monitor: CPL should stay <$95
|
+-- Week 2: $95 -> $120 (+26%)
|   +-- Monitor: Add new creative variants
|
+-- Week 3: $120 -> $150 (+25%)
|   +-- Monitor: Test audience expansion
|
+-- Week 4: $150 -> $200 (+33%)
|   +-- Monitor: Review SQL rate stability
|
+-- Contingency:
    +-- If CPL >$100: Pause scaling
    +-- If CPL >$110: Reduce budget 15%
    +-- If SQL rate drops: Tighten targeting
```

### Scenario 3: High-Competition Niche (Finance/Enterprise SaaS)

```
COMPETITIVE NICHE STRATEGY
==========================

Strategy: Manual Bidding + Premium Positioning

Setup:
+-- Research: Check suggested bid range
+-- Bid: Top 30% of range (win auctions)
+-- Budget: $100+/day (sufficient volume)
+-- Audience: Tight, qualified targeting
+-- Creative: Premium, thought leadership

Bid Strategy:
+-- Start: $12-15 CPC (Finance)
+-- Week 1: Evaluate win rate
+-- Adjust: If <60% impression share, increase bid
+-- Optimize: Test bid levels +/-20%
+-- Target: 70%+ impression share on target audience

Cost Management:
+-- Accept higher CPC for better audience
+-- Focus on: SQL rate, not just CPL
+-- Calculate: Cost per SQL, not just cost per lead
+-- Expectation: CPL $100-150 acceptable if SQL rate >25%
```

## Ad Format Considerations by Bid Strategy

Different ad formats have distinct bidding dynamics. New formats available in 2025-2026:

| Format | Best Bid Strategy | Notes |
|--------|-------------------|-------|
| Single Image (Sponsored Content) | Cost Cap or Max Delivery | Standard workhorse |
| Video Ads | Max Delivery (CPV) | Optimize for view rate |
| Carousel Ads | Cost Cap | Higher engagement, worth bidding for |
| Document Ads | Cost Cap | Strong engagement for content offers; content is viewed in-feed |
| Thought Leader Ads | Max Delivery | Boost employee posts; lower CPM than brand ads, no CPC control |
| Message Ads / Conversation Ads | Manual CPC | Limited volume; bid on open rate |
| CTV / Connected TV Ads | CPM only | Awareness only, no direct response bidding |
| Dynamic Ads | Manual CPC | Personalized but smaller scale |
| Lead Gen Forms (any format) | Cost Cap | Target CPL-based cap recommended |

**Thought Leader Ads note:** These are boosted employee posts. Bidding works via Max Delivery only — you cannot set manual CPC. They typically achieve 20-40% lower CPM than standard brand Sponsored Content.

**Document Ads note:** Users swipe through the document in-feed without leaving LinkedIn. Very high dwell time. Use Cost Cap with a CPL target; document downloads typically convert at 8-12%.

## MCP Tool Usage

To pull current bid and cost data for analysis:

```
# Get campaign performance including cost and delivery metrics
linkedin_get_analytics(
  account_id="YOUR_ACCOUNT_ID",
  start_date="YYYY-MM-DD",
  end_date="YYYY-MM-DD",
  level="campaign",
  fields=["costInLocalCurrency", "clicks", "impressions", "leads"]
)

# Get campaign details including bid strategy settings
linkedin_query(
  account_id="YOUR_ACCOUNT_ID",
  entity_type="campaigns"
)
```

Use these to compare actual CPL vs bid caps, identify under-delivery (budget not spent), and spot bid strategy mismatches.

## Output: Strategy Recommendation Template

```markdown
# LinkedIn Bid Strategy Recommendation

## Current Situation
- Daily/Monthly budget: $[X]
- Industry: [sector]
- Target audience size: [X]
- Current CPL/CPC: [metric] (if available)
- Primary goal: [volume/efficiency/quality]

## Recommended Strategy
**[Maximum Delivery / Cost Cap / Manual Bidding]**

### Why This Strategy
- [Reason 1 based on budget]
- [Reason 2 based on goal]
- [Reason 3 based on experience level]

### Implementation
1. Campaign Setup: [specifics]
2. Bid Configuration: [details]
3. Budget Allocation: [breakdown]

### Targets
- Primary: CPL $[X] / CPC $[Y]
- Secondary: CTR [X]%, CVR [Y]%
- Quality: SQL Rate [X]%

### Timeline
- Week 1: [Learning/baseline]
- Week 2: [Optimization]
- Week 3+: [Scaling/maintenance]

### Success Criteria
- CPL within [X]% of target
- Delivery consistent (>90% budget spend)
- SQL rate maintains [X]%+
```

## Example Interaction

**User**: "I have a $100/day budget for LinkedIn lead gen in the SaaS sector. What's the best bidding strategy?"

**Claude response**:

"For your situation ($100/day, SaaS, lead generation) I recommend:

**Recommended Strategy: Cost Cap**

### Why Cost Cap?

1. **Budget is sufficient** - $100/day gives LinkedIn enough room to optimize
2. **SaaS has benchmark data** - We can determine a realistic target CPL
3. **Balance volume & efficiency** - Cost Cap prevents runaway costs

### Implementation

**Step 1: Determine your Cost Cap**
```
SaaS Benchmark CPL: $80-120
Start Cost Cap: $120 (1.2x industry baseline)
Week 2 target: $100
Week 3+ target: $85-90
```

**Step 2: Campaign Setup**
- Objective: Lead Generation
- Bid type: Cost Cap
- Cost Cap: $120
- Daily budget: $100
- Audience: >50,000 people

**Step 3: Optimization Timeline**
| Week | Action | Target CPL |
|------|--------|------------|
| 1 | Monitor, don't touch | $120 |
| 2 | Tighten cap 15% | $100 |
| 3 | Fine-tune based on SQL | $90 |
| 4+ | Scale if stable | $85-90 |

### Expected Results
- Leads per week: ~8-12 (depending on niche)
- Expected CPL: $85-100 after optimization
- SQL rate target: 15-25%

### Red Flags to Monitor
- Delivery <80% budget? -> Increase cap
- CPL >$140 after week 2? -> Check creative/targeting
- CTR <0.4%? -> Refresh creatives

Would you like me to validate your Cost Cap calculation based on your specific deal size and close rate?"
