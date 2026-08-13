---
name: meta-account-auditor
description: "This skill should be used when the user asks to \"audit a Meta Ads account\", \"take over a new account\", \"run a health check\", or mentions \"account audit\", \"periodic review\", or \"Meta account health score\". Do NOT use for: campaign structure advice (use campaign-structure-advisor), performance troubleshooting (use performance-troubleshooter), benchmark comparisons only (use benchmark-database)."
---
# Account Auditor

## Overview

This skill provides a systematic framework for performing complete Meta Ads account audits, including health scoring, issue identification, and prioritized recommendations for optimization.

## Audit Framework

### Audit Scope Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  META ADS ACCOUNT AUDIT AREAS                                   │
│                                                                 │
│  1. TRACKING & DATA QUALITY                                     │
│     └── Pixel, CAPI, Events, Attribution                        │
│                                                                 │
│  2. ACCOUNT STRUCTURE                                           │
│     └── Campaigns, Ad Sets, Ads, Naming                         │
│                                                                 │
│  3. AUDIENCE STRATEGY                                           │
│     └── Custom, Lookalike, Targeting, Exclusions                │
│                                                                 │
│  4. CREATIVE PERFORMANCE                                        │
│     └── Formats, Fatigue, Testing, Diversity                    │
│                                                                 │
│  5. BUDGET & BIDDING                                            │
│     └── Allocation, Strategy, Efficiency                        │
│                                                                 │
│  6. PERFORMANCE METRICS                                         │
│     └── KPIs, Trends, Benchmarks                                │
│                                                                 │
│  7. COMPLIANCE & SETTINGS                                       │
│     └── Policies, Settings, Access                              │
└─────────────────────────────────────────────────────────────────┘
```

## Complete Audit Checklist

### Section 1: Tracking & Data Quality

```
TRACKING AUDIT
==============

□ PIXEL STATUS
├── Is the pixel installed and active?
├── Pixel ID correct on all relevant domains?
├── Test events in Events Manager
└── Score: [green OK / yellow Issues / red Critical]

□ CONVERSIONS API (CAPI)
├── Is CAPI implemented?
├── Event Match Quality score (goal: >6.0)
├── Deduplication correctly configured?
├── Which parameters are being sent?
└── Score: [green OK / yellow Issues / red Critical]

□ EVENT TRACKING
├── Which events are active?
├── Are events firing correctly? (test conversions)
├── Are custom events needed?
├── Value tracking for purchases?
└── Score: [green OK / yellow Issues / red Critical]

□ DOMAIN VERIFICATION
├── Is the domain verified?
├── Aggregated Event Measurement (AEM) configured?
├── Event prioritization correct?
└── Score: [green OK / yellow Issues / red Critical]

□ ATTRIBUTION WINDOW (Critical — Jan 2026 change)
├── Are reports using the correct default? (7d click + 1d view)
├── Note: 7d view and 28d view attribution REMOVED by Meta (Jan 2026)
├── Historical data using old windows cannot be compared to current data
├── Any reports or rules referencing 28d attribution must be updated
└── Score: [green OK / yellow Issues / red Critical]

TRACKING SCORE: ___/50 points
```

### Section 2: Account Structure

```
STRUCTURE AUDIT
===============

□ CAMPAIGN ORGANIZATION
├── How many active campaigns? (Ideal: 3-8)
├── Clear funnel segmentation? (TOFU/MOFU/BOFU)
├── Logical campaign objectives?
├── No duplicate campaigns?
└── Score: [green OK / yellow Issues / red Critical]

□ AD SET STRUCTURE
├── Number of ad sets per campaign (Ideal: 2-5)
├── Sufficient budget per ad set for learning?
├── No overlapping audiences?
├── Logical audience segmentation?
└── Score: [green OK / yellow Issues / red Critical]

□ ADS ORGANIZATION
├── Number of ads per ad set (Ideal: 3-6, Andromeda engine recommends 15+ distinct creatives per account)
├── Creative diversity present?
├── No duplicate ads?
├── Advantage+ Creative (formerly DCO) correctly configured?
└── Score: [green OK / yellow Issues / red Critical]

□ NAMING CONVENTIONS
├── Consistent naming system?
├── Campaign includes: objective, funnel, date?
├── Ad set includes: audience type?
├── Ad includes: creative type, version?
└── Score: [green OK / yellow Issues / red Critical]

STRUCTURE SCORE: ___/40 points
```

### Section 3: Audience Strategy

```
AUDIENCE AUDIT
==============

□ CUSTOM AUDIENCES
├── Which custom audiences exist?
├── Are they up-to-date (recent data)?
├── Minimum size reached? (>1000)
├── Source quality assessment
└── Score: [green OK / yellow Issues / red Critical]

□ LOOKALIKE AUDIENCES
├── Which LALs are active?
├── Source audience quality?
├── Percentage selection appropriate?
├── Are value-based LALs being used?
├── Note: Lookalikes deprioritized in 2026 — Advantage+ Audience is now Meta's recommended approach
└── Score: [green OK / yellow Issues / red Critical]

□ INTEREST/BEHAVIOR TARGETING
├── Relevance of selected interests?
├── Audience size not too broad/narrow?
├── Are Advantage+ Audiences active on prospecting campaigns? (Recommended over manual interests in 2026)
├── Testing of new interests?
└── Score: [green OK / yellow Issues / red Critical]

□ EXCLUSIONS
├── Are buyers excluded where needed?
├── Funnel-based exclusions active?
├── Audience overlap minimized?
├── No conflicting exclusions?
└── Score: [green OK / yellow Issues / red Critical]

AUDIENCE SCORE: ___/40 points
```

### Section 4: Creative Performance

```
CREATIVE AUDIT
==============

□ FORMAT DIVERSITY
├── Mix of video, static, carousel?
├── Different aspect ratios (1:1, 4:5, 9:16)?
├── UGC vs produced content balance?
├── Stories/Reels-specific creative?
└── Score: [green OK / yellow Issues / red Critical]

□ CREATIVE HEALTH
├── Average age of active creatives?
├── CTR trend (rising/falling)?
├── Frequency per creative?
├── Creative fatigue signals?
└── Score: [green OK / yellow Issues / red Critical]

□ MESSAGING & COPY
├── Clear value proposition?
├── Strong hooks (first 3 sec)?
├── Variation in copy angles?
├── CTAs clear and consistent?
└── Score: [green OK / yellow Issues / red Critical]

□ TESTING CADENCE
├── Are new creatives being tested?
├── A/B testing active?
├── Clear test hypotheses?
├── Learnings documented?
└── Score: [green OK / yellow Issues / red Critical]

CREATIVE SCORE: ___/40 points
```

### Section 5: Budget & Bidding

```
BUDGET AUDIT
============

□ BUDGET ALLOCATION
├── Budget distribution across funnel?
├── No ad sets under minimum budget?
├── Budget aligned with goals?
├── Pacing correct (daily vs lifetime)?
└── Score: [green OK / yellow Issues / red Critical]

□ BID STRATEGY
├── Which bid strategies in use?
├── Appropriate for campaign objectives?
├── Cost caps realistic?
├── ROAS targets achievable?
└── Score: [green OK / yellow Issues / red Critical]

□ BUDGET EFFICIENCY
├── Spend vs budget ratio?
├── Are budgets fully spending?
├── ROI per campaign/funnel stage?
├── Identification of budget waste?
└── Score: [green OK / yellow Issues / red Critical]

□ SCALING POTENTIAL
├── Winning ad sets with room to scale?
├── Headroom in audiences?
├── Budget increase history successful?
└── Score: [green OK / yellow Issues / red Critical]

BUDGET SCORE: ___/40 points
```

### Section 6: Performance Review

```
PERFORMANCE AUDIT
=================

□ KEY METRICS (vs benchmarks)
├── CPA: $___ (benchmark: $___)
├── ROAS: ___ (benchmark: ___)
├── CTR: ___% (benchmark: ___%)
├── CPM: $___ (benchmark: $___)
└── Score: [green OK / yellow Issues / red Critical]

□ TREND ANALYSIS (Last 30 days)
├── CPA trend: [up / flat / down]
├── ROAS trend: [up / flat / down]
├── Volume trend: [up / flat / down]
├── Efficiency trend: [up / flat / down]
└── Score: [green OK / yellow Issues / red Critical]

□ FUNNEL METRICS
├── TOFU: Reach, CPM, Video Views
├── MOFU: CTR, CPC, Engagement
├── BOFU: CPA, ROAS, Conv Rate
└── Score: [green OK / yellow Issues / red Critical]

□ LEARNING PHASE STATUS
├── % ad sets in learning?
├── Average time in learning?
├── Learning phase success rate?
└── Score: [green OK / yellow Issues / red Critical]

PERFORMANCE SCORE: ___/40 points
```

### Section 7: Unused Feature Detection

```
UNUSED FEATURES AUDIT
=====================
This section identifies money left on the table - features that are
available but not being used, representing optimization opportunities.

□ ADVANTAGE+ FEATURES (Underutilized?)
├── Advantage+ Sales Campaigns
│   └── E-commerce account with $5k+/month? Not using Advantage+ Sales?
│       → Potential: 10-20% ROAS improvement
├── Advantage+ Placements
│   └── Manual placements only? Missing reach opportunities
│       → Potential: 15-30% more reach at same cost
├── Advantage Detailed Targeting
│   └── Disabled? AI audience expansion not working
│       → Potential: 10-15% more conversions
├── Advantage+ Creative
│   └── Not using? Missing creative optimization
│       → Potential: 5-10% CTR improvement
└── Score: [green Using / yellow Partially / red Not Using]

□ CONVERSIONS API (CAPI) - Enabled but Low Volume?
├── CAPI enabled but <50% of events from server?
│   └── Missing: Better attribution, lower CPM
├── Only PageView sent? Missing Add-to-Cart, Purchase?
│   └── Missing: Conversion signal strength
├── Event Match Quality <6.0?
│   └── Missing: Full CAPI value (poor matching)
└── Score: [green OK / yellow Partial / red Not Optimized]

□ AUDIENCE ASSETS (Created but Not Used?)
├── Custom Audiences uploaded but not in active ad sets?
│   └── Wasted asset: Customer data not being leveraged
├── Lookalike Audiences created but inactive?
│   └── Wasted asset: Expansion opportunities unused
├── Value-based Lookalikes available but not used?
│   └── Missing: Higher-value customer targeting
├── Website remarketing lists exist but no retargeting campaigns?
│   └── Wasted: Warm audiences not being targeted
└── Score: [green Using All / yellow Partially / red Many Unused]

□ CATALOG & SHOPPING FEATURES (E-commerce)
├── Catalog connected but no Dynamic Ads?
│   └── Missing: Personalized product recommendations
├── Advantage+ Catalog Ads not enabled?
│   └── Missing: Automated creative optimization
├── Collection Ads not tested?
│   └── Missing: Mobile shopping experience
├── Collaborative Ads available (retailer) but not used?
│   └── Missing: Partner reach
└── Score: [green OK / yellow Partial / red Underutilized]

□ AUTOMATION & RULES (Not Configured?)
├── No automated rules for budget/bid management?
│   └── Missing: Proactive management, less manual work
├── No Advantage Campaign Budget enabled?
│   └── Missing: Automated budget allocation across ad sets
├── No cost caps or bid caps when needed?
│   └── Risk: Uncontrolled spending
├── No scheduled ad set rules (day/time)?
│   └── Missing: Performance optimization by schedule
└── Score: [green Using / yellow Basic / red None]

□ MEASUREMENT & ATTRIBUTION (Not Set Up?)
├── Conversion Lift studies available but not run?
│   └── Missing: True incrementality data
├── Brand Lift studies available but not used?
│   └── Missing: Brand impact measurement
├── A/B testing (Experiments) not used?
│   └── Missing: Statistical testing framework
├── Attribution comparison report not reviewed?
│   └── Missing: Understanding of attribution impact
└── Score: [green Using / yellow Basic / red None]

UNUSED FEATURES SCORE: ___/60 points

OPPORTUNITY COST ESTIMATE:
├── Each unused Advantage+ feature: ~$500-2,000/month missed
├── Low CAPI adoption: ~15-25% higher CPMs
├── Unused audiences: ~20-30% efficiency loss
├── No automation: ~2-5 hours/week manual work
└── TOTAL ESTIMATED OPPORTUNITY: $___/month
```

## Health Score Calculator

### Score Interpretation

```
ACCOUNT HEALTH SCORE
====================

SECTION               │ MAX POINTS │ YOUR SCORE
─────────────────────┼────────────┼───────────
Tracking & Data      │     40     │    ___
Account Structure    │     40     │    ___
Audience Strategy    │     40     │    ___
Creative Performance │     40     │    ___
Budget & Bidding     │     40     │    ___
Performance Metrics  │     40     │    ___
Unused Features      │     60     │    ___
─────────────────────┼────────────┼───────────
TOTAL                │    300     │    ___

SCORE INTERPRETATION:
├── 250-300: Excellent - Minor optimizations
├── 200-249: Good - Several improvements needed
├── 150-199: Fair - Significant work required
└── <150:    Poor - Major restructuring needed
```

## Issue Prioritization Matrix

### Categorize found issues:

```
ISSUE PRIORITIZATION
====================

CRITICAL (Fix within 24 hours):
├── Tracking not working
├── No conversions being tracked
├── Budget completely stopped
├── Policy violations
└── Major data discrepancies

HIGH (Fix within 1 week):
├── Poor EMQ score (<5)
├── High audience overlap (>50%)
├── Creative fatigue (CTR <0.5%)
├── CPA >50% above target
└── Learning phase failures

MEDIUM (Fix within 2 weeks):
├── Naming conventions inconsistent
├── Ad set consolidation needed
├── Audience refresh needed
├── Budget reallocation needed
└── Missing exclusions

LOW (Fix within 1 month):
├── Nice-to-have optimizations
├── Testing opportunities
├── Documentation updates
└── Minor structural changes
```

## Audit Report Template

### When the user asks for an account audit:

```
ACCOUNT AUDIT REPORT
=====================

Audit Date: [DATE]
Account: [ACCOUNT NAME]
Auditor: Claude AI

EXECUTIVE SUMMARY
────────────────────
Account Health Score: [X]/300 ([STATUS])

Top 3 Strengths:
1. [Strength]
2. [Strength]
3. [Strength]

Top 3 Areas for Improvement:
1. [Area]
2. [Area]
3. [Area]

DETAILED FINDINGS
─────────────────────────────

1. TRACKING & DATA
   Status: [green/yellow/red]
   Issues: [List]
   Recommendations: [List]

2. ACCOUNT STRUCTURE
   Status: [green/yellow/red]
   Issues: [List]
   Recommendations: [List]

[...etc for all sections...]

ACTION PLAN (Prioritized)
────────────────────────────

WEEK 1 (Critical):
□ [Action 1]
□ [Action 2]

WEEK 2-3 (High):
□ [Action 3]
□ [Action 4]

MONTH 1 (Medium):
□ [Action 5]
□ [Action 6]

EXPECTED IMPACT
───────────────
After implementation we expect:
├── CPA: [X%] improvement
├── ROAS: [X%] improvement
└── Efficiency: [X%] improvement
```

## Quick Audit Checklist

### For a fast health check:

```
QUICK AUDIT (15 minutes)
========================

□ Pixel active? (Events Manager → Test Events)
□ Conversions last 7 days? (yes/no/how many)
□ Learning phase issues? (% in learning)
□ CPA vs target? (under/on/over)
□ Frequency <3? (yes/no)
□ CTR >1%? (yes/no)
□ Active creatives >3 per ad set? (yes/no)
□ Budget fully spending? (yes/no)

QUICK SCORE: ___/8
└── 7-8: Healthy account
└── 5-6: Attention needed
└── <5: In-depth audit needed
```

## MCP Tool Integration

### Running an Audit with Live Data

Use these MCP calls to pull actual account data before scoring each section:

```
1. Campaign structure overview:
→ meta_query(account_id="...", entity_type="campaigns", effective_status=["ACTIVE"], fields=["id","name","objective","status","daily_budget","lifetime_budget"])

2. Ad set performance + delivery:
→ meta_get_insights(account_id="...", level="adset", date_preset="last_7d", fields=["cost_per_action_type","spend","frequency","impressions"])

3. Ad-level creative health:
→ meta_get_creatives(account_id="...", scope="account", date_preset="last_7d")

4. Top/bottom performers (last 30 days):
→ meta_get_insights(account_id="...", level="campaign", date_preset="last_30d", fields=["spend","actions","cost_per_action_type","impressions"])
```

Feed results directly into the audit sections above to score each area objectively.

## Example Interaction

**User**: "I just took over a new account. Can you help me with an audit?"

**Claude response**:

"I'll help you with a systematic account audit. Let me pull the live data first:

```
meta_get_insights(account_id="...", level="campaign", date_preset="last_7d", fields=["spend","cost_per_action_type","frequency","impressions"])
```

```
meta_get_insights(account_id="...", level="adset", date_preset="last_7d", fields=["cost_per_action_type","spend","frequency"])
```

While that runs, I also need a few things:

---

**STEP 1: Gather Basic Info**

Can you tell me the following:
1. What is the industry/vertical?
2. What is the monthly ad budget?
3. What are the current KPI targets (CPA/ROAS)?
4. How long has the account been running?

---

**STEP 2: Key Things I'll Check From the Data**

**Tracking Check:**
- Pixel active + EMQ score for Purchase event (target: 6.0+)
- Attribution window: confirm reports use 7d click + 1d view (28d view removed Jan 2026)

**Structure Check:**
- Number of active campaigns (ideal: 3-8)
- Ad sets per campaign (ideal: 2-5)
- Creative count and diversity

**Performance Check (Last 7 days):**
- CPA vs target
- ROAS vs target
- Learning phase % (should be <20% of budget)

---

Share the account ID and I'll generate a complete audit with health score and action plan!"
