---
name: google-ads-attribution-model-advisor
description: "This skill should be used when the user asks to \"choose an attribution model\", \"set up Data-Driven Attribution\", \"compare attribution models\", \"analyze conversion paths\", or mentions \"DDA\", \"cross-channel attribution\", or \"lookback window optimization\". Do NOT use for: bid strategy selection (use bid-strategy-selector), conversion tracking setup (use conversion-tracking-setup), or campaign performance diagnosis (use performance-troubleshooter)."
---
# Attribution Model Advisor

Complete guide for choosing, implementing, and evaluating Google Ads attribution models with focus on Data-Driven Attribution (DDA) and cross-channel measurement.

## 2026 Measurement Foundation: Consent Mode v2 + Enhanced Conversions

Attribution accuracy depends entirely on your measurement stack being compliant and complete. Check this first:

```
MEASUREMENT HEALTH CHECKLIST (2026)
════════════════════════════════════

1. CONSENT MODE V2 (Required for EEA since March 2024)
   ├── ad_storage + analytics_storage consent signals firing
   ├── ad_user_data + ad_personalization signals set
   ├── Google Tag Manager: Consent Initialization trigger configured
   └── Verify: gtag('consent', 'default', {...}) fires BEFORE any ad tags

2. ENHANCED CONVERSIONS (Name unchanged — still "Enhanced Conversions")
   ├── Hashes first-party user data (email, phone, address)
   ├── Recovers conversions lost to cookie rejection
   ├── Setup: Google Ads → Tools → Conversions → Enhanced Conversions
   └── Requires privacy policy update

3. ATTRIBUTION MODEL ORDER OF PREFERENCE (2026):
   Data-Driven (DDA) > Linear > Position-Based > Time Decay > Last Click
   ├── First Click: Only for pure awareness measurement
   └── Last Click: Legacy only — avoid for Smart Bidding campaigns
```

## Pull Conversion Action Settings via MCP

```
google_ads_run_gaql(query="
  SELECT conversion_action.name,
         conversion_action.attribution_model_settings.attribution_model,
         conversion_action.counting_type,
         conversion_action.include_in_conversions_metric,
         conversion_action.click_through_lookback_window_days,
         conversion_action.view_through_lookback_window_days,
         metrics.conversions, metrics.conversion_value
  FROM conversion_action
  WHERE conversion_action.status = 'ENABLED'
")
```

Use this to audit whether DDA is active and whether lookback windows match your sales cycle.



See [decision-trees.md](references/decision-trees.md) for details.



## Attribution Models Overview

### Model Comparison

```
ATTRIBUTION MODEL COMPARISON
═════════════════════════════

┌─────────────────────┬────────────┬────────────────────────────────────────┐
│ MODEL               │ DATA REQ   │ HOW IT WORKS                           │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Last Click          │ None       │ 100% credit to the last click          │
│                     │            │ (default, simple, but limited)         │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ First Click         │ None       │ 100% credit to the first click         │
│                     │            │ (good for measuring awareness)         │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Linear              │ Low        │ Equal distribution across all          │
│                     │            │ touchpoints (democratic, but no nuance)│
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Time Decay          │ Low        │ More credit to recent touchpoints      │
│                     │            │ (7-day half-life)                      │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Position Based      │ Medium     │ 40% first, 40% last, 20% middle       │
│                     │            │ (balanced awareness + conversion)      │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Data-Driven (DDA)   │ High       │ ML-based on your data                  │
│                     │ (600+/mo)  │ (most accurate, Google recommended)    │
└─────────────────────┴────────────┴────────────────────────────────────────┘
```

### Visual: How Credits Are Distributed

```
EXAMPLE: 4 TOUCHPOINTS BEFORE CONVERSION
═════════════════════════════════════════

Customer Journey:
Display Ad → Search (generic) → Search (brand) → Conversion
   [1]            [2]              [3]           [€100]

CREDIT DISTRIBUTION PER MODEL:

Last Click:
[1] €0 ────► [2] €0 ────► [3] €100 ────► Conversion
                              100%

First Click:
[1] €100 ───► [2] €0 ────► [3] €0 ────► Conversion
    100%

Linear:
[1] €33.33 ─► [2] €33.33 ─► [3] €33.33 ─► Conversion
    33.3%        33.3%         33.3%

Time Decay:
[1] €10.50 ─► [2] €24.50 ─► [3] €65 ────► Conversion
    10.5%        24.5%         65%

Position Based:
[1] €40 ────► [2] €20 ────► [3] €40 ────► Conversion
    40%          20%           40%

Data-Driven (example):
[1] €28 ────► [2] €35 ────► [3] €37 ────► Conversion
    28%          35%           37%
    (based on your account data)
```

## Data-Driven Attribution (DDA)

### How DDA Works

```
DATA-DRIVEN ATTRIBUTION ENGINE
══════════════════════════════

MACHINE LEARNING APPROACH:
├── Analyzes all conversion paths
├── Compares converting vs non-converting journeys
├── Calculates incremental value per touchpoint
└── Dynamically adjusts based on new data

SIGNALS DDA USES:
├── Ad interactions (clicks, impressions)
├── Device type and cross-device behaviour
├── Time between interactions
├── Ad format and placement
├── Search query types
└── Customer segment signals

WHEN CREDITS ARE DISTRIBUTED:
├── Real-time with each conversion
├── Lookback window: 30-90 days (configurable)
├── Including view-through conversions (if enabled)
└── Cross-channel when linked (GA4)
```

### DDA Requirements & Setup

```
DDA REQUIREMENTS CHECKLIST
══════════════════════════

MINIMUM REQUIREMENTS:
□ 600+ conversions per month (per conversion action)
□ 15,000+ clicks per month
□ 30 days of history at these volumes
□ Conversion tracking correctly implemented

RECOMMENDED FOR OPTIMAL DDA:
□ 1000+ conversions per month
□ Consistent tracking (no gaps)
□ Cross-device tracking enabled
□ Enhanced Conversions active (recovers consent-rejected data)
□ Consent Mode v2 correctly configured (required EEA, Mar 2024+)

ACTIVATING DDA:
1. Tools & Settings → Measurement → Conversions
2. Select conversion action
3. Attribution model → "Data-driven"
4. Save

⚠️ IMPORTANT:
├── DDA is set per conversion action
├── Not all actions need to use DDA
├── Evaluate after 2-4 weeks whether data is stable
└── Fall back to Linear if data is insufficient
```

### Analyzing DDA Impact

```
DDA vs LAST CLICK COMPARISON
═════════════════════════════

WHERE TO FIND:
Tools → Attribution → Model comparison

WHAT YOU SEE:
┌─────────────────────────────────────────────────────────────┐
│ Campaign       │ Last Click │ Data-Driven │ Difference      │
├────────────────┼────────────┼─────────────┼─────────────────┤
│ Brand Search   │ 150 conv   │ 120 conv    │ -20% (↓)        │
│ Generic Search │ 80 conv    │ 95 conv     │ +19% (↑)        │
│ Display        │ 20 conv    │ 45 conv     │ +125% (↑)       │
│ YouTube        │ 10 conv    │ 35 conv     │ +250% (↑)       │
│ Shopping       │ 100 conv   │ 105 conv    │ +5%             │
└────────────────┴────────────┴─────────────┴─────────────────┘

HOW TO INTERPRET:
─────────────────
↑ Campaign receives MORE credit with DDA
  → Undervaluation in Last Click
  → Consider budget increase

↓ Campaign receives LESS credit with DDA
  → Overvaluation in Last Click
  → Reconsider budget allocation

ACTION FOR SIGNIFICANT DIFFERENCES (>20%):
├── Analyze conversion paths for those campaigns
├── Check assisted conversions
├── Adjust budget allocation based on DDA values
└── Monitor for 2-4 weeks after changes
```

## Cross-Channel Attribution

### Google Ads + GA4 Integration

```
CROSS-CHANNEL ATTRIBUTION SETUP
════════════════════════════════

WHY CROSS-CHANNEL:
├── Google Ads only sees Google touchpoints
├── GA4 sees all channels (organic, social, email, etc.)
├── Better full-funnel attribution
└── More accurate budget allocation

SETUP STEPS:
─────────────
1. LINK GOOGLE ADS TO GA4
   □ GA4 → Admin → Product Links → Google Ads
   □ Enable auto-tagging in Google Ads
   □ Import conversions to Google Ads (optional)

2. CONFIGURE ATTRIBUTION IN GA4
   □ Admin → Attribution Settings
   □ Reporting attribution model: Data-driven
   □ Lookback window: 90 days (or as needed)
   □ Enable "Include Google signals data"

3. ANALYZE CROSS-CHANNEL PATHS
   □ GA4 → Advertising → Attribution → Conversion paths
   □ Filter by different channel groupings
   □ Compare paid vs organic touchpoints

4. IMPORT GA4 CONVERSIONS (optional)
   □ Tools → Measurement → Conversions → Import
   □ Select GA4 property
   □ Choose conversion events
   □ Note: Different attribution possible than native GA conversions
```

### Conversion Path Analysis

```
CONVERSION PATH ANALYSIS
════════════════════════

WHERE TO FIND (GA4):
Advertising → Attribution → Conversion paths

WHAT TO ANALYZE:
────────────────

1. TOP CONVERTING PATHS
   Paid Search → Organic → Direct → Conversion
   Display → Paid Search → Paid Search → Conversion

   → Identify typical customer journeys
   → Understand the role of each channel

2. PATH LENGTH DISTRIBUTION
   ┌────────────────────────────────────────┐
   │ Touchpoints │ % Conversions │ Trend    │
   ├─────────────┼───────────────┼──────────┤
   │ 1           │ 35%           │ Direct   │
   │ 2-3         │ 40%           │ Short    │
   │ 4-6         │ 18%           │ Medium   │
   │ 7+          │ 7%            │ Complex  │
   └─────────────┴───────────────┴──────────┘

   → Longer paths = more assisted value
   → Short paths = strong bottom-funnel

3. TIME TO CONVERSION
   ┌────────────────────────────────────────┐
   │ Days        │ % Conversions │ Type     │
   ├─────────────┼───────────────┼──────────┤
   │ Day 0       │ 45%           │ Impulse  │
   │ 1-7 days    │ 30%           │ Short    │
   │ 8-30 days   │ 20%           │ Medium   │
   │ 30+ days    │ 5%            │ Long     │
   └─────────────┴───────────────┴──────────┘

   → Determines lookback window choice
   → Influences remarketing strategy

4. ASSISTED VS LAST CLICK
   Per campaign/channel:
   ├── Assisted conversions (in path, not last)
   ├── Last click conversions (final touch)
   └── Assisted/Last ratio

   Ratio > 1: Channel is "assister" (top-funnel)
   Ratio < 1: Channel is "closer" (bottom-funnel)
```



See [decision-trees.md](references/decision-trees.md) for details.



## Multi-Touch Attribution Strategy

### Assisted Conversions Analysis

```
ANALYZING ASSISTED CONVERSIONS
══════════════════════════════

WHAT ARE ASSISTED CONVERSIONS:
├── Touchpoints in the conversion path that are NOT the last
├── Show the "supporting" role of campaigns
├── Crucial for full-funnel budget allocation
└── Often undervalued in Last Click

WHERE TO FIND:
Tools → Attribution → Top paths
Tools → Attribution → Assisted conversions

HOW TO USE:
───────────

1. IDENTIFY "HIDDEN GEMS"
   Campaigns with:
   ├── Few last-click conversions
   ├── Many assisted conversions
   └── High assisted/last ratio

   → These campaigns are top-funnel initiators
   → They support other campaigns
   → Don't judge them on direct conversions

2. CALCULATE FULL VALUE
   Total Value = Last Click Conv × Avg Value
                 + Assisted Conv × (Avg Value × Weight)

   Weight suggestion:
   ├── 0.3-0.5 for awareness (Display, Video)
   ├── 0.5-0.7 for consideration (Generic Search)
   └── 0.8-1.0 for high-intent assisted

3. BUDGET ALLOCATION
   ┌────────────────────────────────────────────────────┐
   │ Campaign Type    │ Eval Metric      │ Budget Role  │
   ├──────────────────┼──────────────────┼──────────────┤
   │ Display/Video    │ Assisted Conv    │ Top-funnel   │
   │ Generic Search   │ Assisted + Last  │ Mid-funnel   │
   │ Brand Search     │ Last Click       │ Bottom       │
   │ Shopping/PMax    │ Total Conv       │ Full-funnel  │
   └──────────────────┴──────────────────┴──────────────┘
```

### Attribution Windows

```
LOOKBACK WINDOW OPTIMIZATION
═════════════════════════════

WHAT IS A LOOKBACK WINDOW:
├── Period during which touchpoints are counted
├── Click-through: 30 days default (1-90 possible)
├── View-through: 1 day default (1-30 possible)
└── Engaged-view: 3 days default (video)

HOW TO DETERMINE THE RIGHT WINDOW:
───────────────────────────────────

STEP 1: Analyze Time to Conversion
GA4 → Advertising → Attribution → Conversion paths → Time to conversion

STEP 2: Determine Optimal Window
┌─────────────────────────────────────────────────────────┐
│ If 90%+ conversions within X days → Window = X + buffer │
└─────────────────────────────────────────────────────────┘

TYPICAL WINDOWS PER INDUSTRY:
─────────────────────────────
E-commerce (impulse):
├── Click-through: 7-14 days
├── View-through: 1 day
└── Reason: Short decision cycle

E-commerce (high-value):
├── Click-through: 30 days
├── View-through: 7 days
└── Reason: More research needed

B2B Lead Gen:
├── Click-through: 60-90 days
├── View-through: 7-14 days
└── Reason: Long sales cycle

Travel/Finance:
├── Click-through: 30-60 days
├── View-through: 7 days
└── Reason: Comparison shopping

HOW TO SET:
Tools → Measurement → Conversions → [Action] →
Edit settings → Lookback window
```



See [detailed-reference.md](references/detailed-reference.md) for details.



## Output: Attribution Model Recommendation Template

```markdown
# Attribution Model Recommendation

## Account Analysis
- **Monthly conversions:** [X]
- **Conversion types:** [Lead/Purchase/Multiple]
- **Current attribution model:** [Last Click/DDA/etc.]
- **Average path length:** [X touchpoints]
- **Average time to conversion:** [X days]



See [detailed-reference.md](references/detailed-reference.md) for details.


