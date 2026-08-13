---
name: meta-ab-test-planner
description: "This skill should be used when the user asks to \"plan an A/B test\", \"calculate sample size\", \"analyze test results\", or mentions \"Meta split test\", \"statistical significance\", or \"testing roadmap\". Do NOT use for: creative brainstorming (use creative-diversification-generator), ad copy writing (use ad-copy-generator), campaign structure (use campaign-structure-advisor)."
---
# A/B Test Planner

## Overview

This skill helps set up statistically sound A/B tests in Meta Ads, including hypothesis formulation, test structure, sample size calculations, and result interpretation for reliable optimization decisions.

## A/B Testing Fundamentals

### Why A/B Test in Meta Ads?

```
┌─────────────────────────────────────────────────────────────────┐
│  A/B TESTING vs "JUST RUNNING"                                  │
│                                                                 │
│  Without A/B test:                                              │
│  ├── Algorithm picks "winner" based on early signals            │
│  ├── No statistical certainty                                   │
│  ├── Seasonal/timing effects confuse results                    │
│  └── Learnings not reproducible                                 │
│                                                                 │
│  With A/B test:                                                 │
│  ├── Equal conditions for both variants                         │
│  ├── Statistical significance (95%+ confidence)                 │
│  ├── Isolated variable = clear learning                         │
│  └── Reproducible results                                       │
└─────────────────────────────────────────────────────────────────┘
```

### Meta's Native A/B Test Tool

```
LOCATION: Ads Manager → Experiments → A/B Test

BENEFITS:
├── Automatic audience split (no overlap)
├── Statistical significance calculation
├── Controlled test environment
└── Clear winner declaration

WHEN TO USE:
├── Creative testing (image A vs B)
├── Audience testing (LAL vs Interest)
├── Placement testing (Auto vs Manual)
└── Optimization goal testing
```

## Hypothesis Framework

### Formulating a SMART Hypothesis

```
HYPOTHESIS STRUCTURE:
"If we change [VARIABLE] from [A] to [B],
then we expect [METRIC] to improve by [X%],
because [RATIONALE]."

EXAMPLE:
"If we change the video hook from 'product-first' to
'problem-first', then we expect View Rate (3 sec)
to improve by 15%, because people first recognize their
problem before they're interested in the solution."
```

### Good vs Bad Hypotheses

| Bad | Good |
|-----|------|
| "I think version B works better" | "Version B (with social proof) increases CTR by 10% vs version A (without)" |
| "We're testing new creative" | "UGC-style creative lowers CPA by 15% vs studio creative" |
| "Let's compare audiences" | "LAL 1% purchasers has 20% lower CPA than Interest targeting" |

## Test Prioritization Framework

### ICE Score Method

```
PRIORITIZATION FORMULA:
ICE Score = (Impact + Confidence + Ease) / 3

IMPACT (1-10):
├── How much influence on results?
├── 10 = Core element (hook, offer)
└── 1 = Minor detail (button color)

CONFIDENCE (1-10):
├── How sure are you of improvement?
├── 10 = Supported by data/research
└── 1 = Pure guess

EASE (1-10):
├── How easy to execute?
├── 10 = Copy change
└── 1 = Remake entire video
```

### Test Priority Matrix

```
PRIORITY    │ WHAT TO TEST                  │ ICE
────────────┼───────────────────────────────┼─────
HIGH        │ Video hook (first 3 sec)      │ 9.0
HIGH        │ Headline                       │ 8.5
HIGH        │ Offer/promotion               │ 8.5
MEDIUM      │ Primary text length           │ 7.0
MEDIUM      │ CTA button                    │ 6.5
MEDIUM      │ Image style                   │ 6.5
LOW         │ Description text              │ 5.0
LOW         │ Emoji usage                   │ 4.5
SKIP        │ Button color                  │ 2.0
```

## Test Types & Setup

### Type 1: Creative Test

```
GOAL: Which creative performs better?
VARIABLE: Image, video, or carousel

SETUP IN META:
├── Campaign: [Existing campaign]
├── Test Type: Creative
├── Variants: 2-5 creatives
├── Metric: CTR, CPA, or ROAS
├── Budget Split: Equal (50/50 for 2 variants)
└── Duration: Min. 7 days

EXAMPLE:
├── Variant A: Product lifestyle photo
├── Variant B: Product on white background
├── Variant C: UGC-style photo
└── Primary Metric: CTR (or Purchase CPA)
```

### Type 2: Audience Test

```
GOAL: Which audience has best CPA/ROAS?
VARIABLE: Targeting

SETUP IN META:
├── Campaign: New test campaign
├── Test Type: Audience
├── Variants: 2 audiences
├── Creative: SAME for both (!)
├── Budget: Equal per variant
└── Duration: Min. 14 days (more data needed)

EXAMPLE:
├── Variant A: LAL 1% Purchasers
├── Variant B: Interest Stack "Fitness"
├── Control: Same creative set
└── Primary Metric: CPA or ROAS
```

### Type 3: Placement Test

```
GOAL: Auto placements vs Manual?
VARIABLE: Where ads are shown

SETUP IN META:
├── Campaign: Test campaign
├── Test Type: Placement
├── Variants:
│   ├── A: Advantage+ Placements (auto)
│   └── B: Manual (e.g., Feed + Stories only)
├── Creative: Same
└── Duration: 14 days

WHEN RELEVANT:
├── You suspect Meta Audience Network wastes budget
├── You want to isolate Stories performance
├── You want to test Threads as a standalone placement
└── New account without placement data
```

## Sample Size & Duration Calculator

### Minimum Test Duration

```
RULE OF THUMB:
├── Minimum 7 days (to cover day-of-week variation)
├── Minimum 100 conversions per variant
├── Or minimum 1,000 clicks per variant (for CTR tests)
└── Statistical significance >90% reached

CALCULATOR INPUTS:
├── Baseline conversion rate: [X%]
├── Minimum detectable effect: [Y%]
├── Statistical significance: 95%
├── Power: 80%
└── Daily traffic/conversions: [Z]
```

### Quick Reference Table

| Test Type | Min. per Variant | Recommended Duration |
|-----------|------------------|----------------------|
| CTR Test | 1,000 clicks | 7-10 days |
| Conversion Test | 100 conversions | 14-21 days |
| ROAS Test | 100 purchases | 14-28 days |
| Audience Test | 200 conversions | 21-30 days |

### When to End a Test?

```
END IF:
├── 95%+ statistical significance reached
├── Both variants have >100 conversions
├── Test has run for minimum 7 days
└── No major external factors (holidays, etc.)

DO NOT END IF:
├── <90% significance (unless budget exhausted)
├── <50 conversions per variant
├── <7 days run time
└── During abnormal period (Black Friday, etc.)
```

## Test Structure Templates

### Single Variable Test Template

```
A/B TEST PLAN
=============

TEST INFO:
├── Test Name: [Descriptive name]
├── Hypothesis: [SMART hypothesis]
├── Start Date: [Date]
└── Expected End Date: [Date]

TEST DETAILS:
├── Type: [Creative / Audience / Placement]
├── Variable: [What are we testing]
├── Primary Metric: [CPA / CTR / ROAS]
└── Secondary Metrics: [CTR, Frequency, etc.]

VARIANTS:
├── Variant A (Control): [Description]
└── Variant B (Test): [Description]

BUDGET:
├── Total Test Budget: €[X]
├── Per Variant: €[X/2]
└── Daily Budget per Variant: €[X]

DURATION & SAMPLE SIZE:
├── Minimum Duration: [X] days
├── Target Conversions per Variant: [X]
└── Stop Criterion: 95% significance OR [date]

SUCCESS CRITERIA:
├── Winner if: [Metric] difference >10%
├── With: >95% statistical significance
└── Decision: [What do we do with the winner?]
```

## Result Analysis Framework

### Interpretation Guide

```
RESULT SCENARIOS:

SCENARIO 1: Clear winner (>95% sig, >15% difference)
├── Action: Implement winner
├── Learning: Document why it worked
└── Next: Test the next variable

SCENARIO 2: Marginal winner (90-95% sig, 5-15% difference)
├── Action: Consider collecting more data
├── Learning: Difference may be real but small
└── Next: Implement or retest with larger budget

SCENARIO 3: No winner (<90% sig)
├── Action: Make no changes
├── Learning: Variable makes no difference
└── Next: Test a larger/different change

SCENARIO 4: Surprising loser (your favorite version loses)
├── Action: Implement the winner (data > gut feeling!)
├── Learning: Document the difference
└── Next: Investigate WHY your expectation was wrong
```

### Post-Test Documentation

```
TEST RESULTS REPORT
====================

TEST: [Name]
Period: [Start] - [End]

RESULTS:

Metric          │ Variant A │ Variant B │ Difference
────────────────┼───────────┼───────────┼──────────
Impressions     │  50,000   │  50,000   │    0%
Clicks          │   2,500   │   3,000   │  +20%
CTR             │   5.0%    │   6.0%    │  +20%
Conversions     │    125    │    150    │  +20%
CPA             │  €20.00   │  €16.67   │  -17%
ROAS            │   2.5x    │   3.0x    │  +20%

STATISTICAL SIGNIFICANCE: [X%]

WINNER: Variant [A/B]

KEY LEARNINGS:
├── [Learning 1]
├── [Learning 2]
└── [Learning 3]

NEXT STEPS:
├── [Action 1]
├── [Action 2]
└── [Next test]
```

## Testing Roadmap Template

### Quarterly Testing Calendar

```
Q[X] TESTING ROADMAP
====================

MONTH 1:
├── Week 1-2: Creative Test - Hook variations
├── Week 3-4: Creative Test - Format (video vs static)
└── Apply learnings

MONTH 2:
├── Week 1-2: Audience Test - LAL vs Interest
├── Week 3-4: Copy Test - Long vs short
└── Apply learnings

MONTH 3:
├── Week 1-2: Offer Test - % discount vs € discount
├── Week 3-4: Winning combo test
└── Quarter review & planning

PRIORITY ORDER:
1. Hook/first impression (highest impact)
2. Offer/value proposition
3. Audience targeting
4. Copy elements
5. Technical optimizations
```

## Example Interaction

**User**: "I want to test whether UGC-style videos work better than my current studio content. What's the best way to set this up?"

**Claude response**:

"Great test! Here's your A/B test plan:

---

**A/B TEST PLAN: UGC vs Studio Content**

**HYPOTHESIS:**
'If we use UGC-style videos instead of studio content, we expect CPA to decrease by 20%, because UGC feels more authentic and better fits social media behavior.'

**TEST SETUP:**

| Element | Details |
|---------|---------|
| Type | Creative Test |
| Platform | Meta Ads A/B Test tool |
| Variable | Video style |
| Control (A) | Current studio video |
| Test (B) | UGC-style video |

**IMPORTANT: Keep constant:**
- Same message/script direction
- Same offer/CTA
- Same audience
- Same budget split

**BUDGET & DURATION:**
- Minimum €500 per variant (€1,000 total)
- Minimum 14 days
- Goal: 100+ conversions per variant

**METRICS:**
- Primary: CPA (Cost per Acquisition)
- Secondary: CTR, Hook Rate (3 sec views), ThruPlay Rate

**SUCCESS CRITERIA:**
- Winner at >95% significance
- Minimum 15% CPA difference
- Both >100 conversions

---

**Would you like me to also write a UGC script you can test?**"

## MCP Tool Usage

### Pull current creative performance before setting up a test:

```python
# Get performance data to establish your baseline metrics
meta_get_insights(
    account_id="act_XXXXXXXXX",
    level="ad",
    date_preset="last_30d",
    fields=["impressions", "clicks", "ctr", "cpc", "spend", "actions", "cost_per_action_type"]
)
```

Use this to identify which creatives to test against and what your current CTR/CPA baseline is before writing your hypothesis.
