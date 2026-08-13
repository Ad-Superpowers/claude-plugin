---
name: meta-attribution-window-advisor
description: "This skill should be used when the user asks to \"choose an attribution window\", \"compare click vs view-through attribution\", \"set up incremental attribution\", or mentions \"Meta attribution settings\", \"iOS 14 attribution\", or \"attribution window configuration\". Do NOT use for: cross-platform attribution reconciliation (use cross-platform-attribution-reconciler), CAPI setup (use capi-implementation-guide), EMQ optimization (use emq-optimizer)."
---
# Attribution Window Advisor

Advisor for choosing the optimal Meta Ads attribution configuration based on product, buying cycle, and goals.

> **January 2026 Attribution Change:** Meta removed 7-day view and 28-day view attribution windows. The new default is **7-day click + 1-day view**. Unique reach counts now have a **13-month retention limit**. If your reports compare to periods before January 2026, expect metric discontinuities for view-based attribution.

## Attribution Basics

### What Is Attribution?

Attribution determines which ads receive credit for conversions and how long after interaction a conversion is still attributed.

```
Attribution Types:
├── Click-Through: Conversion after clicking an ad
├── View-Through: Conversion after seeing an ad (no click)
└── Engaged-View: Conversion after 10+ sec video view
```

### Available Windows (Current)

| Window Type | Options | Default |
|-------------|---------|---------|
| **Click-Through** | 1-day, 7-day | 7-day |
| **View-Through** | 1-day, None | 1-day |
| **Engaged-View** | 1-day, None | 1-day (if VT=1-day) |

**Removed (no longer available):**
- 28-day click
- 28-day view
- 7-day view

## Attribution Window Selection

### Decision Tree

```
WHAT IS YOUR PRODUCT/SERVICE?
│
├─► Impulse Purchases (<€50, quick decision)
│   └─► 1-day click, 1-day view
│   └─► Examples: Fast fashion, accessories, digital products
│
├─► Standard E-commerce (€50-200)
│   └─► 7-day click, 1-day view (DEFAULT)
│   └─► Examples: Clothing, electronics, home goods
│
├─► Considered Purchases (€200+, research phase)
│   └─► 7-day click, 1-day view
│   └─► Examples: Furniture, luxury items, tech
│
├─► Lead Generation (B2B/Services)
│   └─► 7-day click, 1-day view
│   └─► Long sales cycle = 7-day click minimum
│
└─► High-Ticket / Long Sales Cycle
    └─► 7-day click, 1-day view
    └─► Supplement with external attribution tools
```

### Recommendation Matrix

| Scenario | Click Window | View Window | Rationale |
|----------|--------------|-------------|-----------|
| **Default (most cases)** | 7-day | 1-day | Balanced data collection |
| **Impulse/Flash sales** | 1-day | 1-day | Short decision cycle |
| **Brand awareness** | 7-day | 1-day | Capture delayed action |
| **Retargeting** | 7-day | 1-day | Users already familiar |
| **Strict ROAS targets** | 7-day | None | Minimize inflated metrics |
| **High-consideration B2B** | 7-day | 1-day | Research-heavy buying |

## Click-Through vs View-Through

### Understanding the Difference

```
CLICK-THROUGH ATTRIBUTION:
├── User clicks ad
├── User converts within window
├── Conversion credited to ad
└── Stronger causation signal

VIEW-THROUGH ATTRIBUTION:
├── User sees ad (no click)
├── User converts within window (different path)
├── Conversion credited to ad
└── Measures awareness/influence

ENGAGED-VIEW (Video only):
├── User watches 10+ seconds (or 97% if <10 sec)
├── User converts within 1 day
├── Requires View-Through = 1-day
└── Middle ground between click and view
```

### When to Use View-Through

```
ENABLE VIEW-THROUGH (1-day) WHEN:
├── Brand awareness is important
├── Want to measure full ad impact
├── Video ads prominent in mix
├── Upper-funnel campaigns
└── Budget for incremental reach

DISABLE VIEW-THROUGH (None) WHEN:
├── Strict ROAS accountability
├── Comparison with other channels
├── Minimizing attribution overlap
├── Focus on direct response only
└── Incremental measurement priority
```

### View-Through Impact

```
View-Through Effect on Metrics:
├── ROAS: Typically 10-30% higher with VT enabled
├── Conversions: 15-40% more reported
└── CPA: Appears lower (more conversions attributed)

Note:
- VT conversions are NOT fake
- They measure brand influence
- But they are less "incremental"
- Always compare apples-to-apples
```

## ATT Attribution Constraints

### Current State (Since iOS 14.5)

```
App Tracking Transparency (ATT) — standard since 2021:
├── ~75-85% of iOS users opt out of tracking
├── Limited conversion visibility for opted-out users
├── Up to 72 hour delay for iOS conversions
├── Aggregated Event Measurement (AEM) for opted-out users
└── Meta uses modeled conversions to fill gaps

Practical Impact:
├── Reported conversions ~15-25% below actual
├── Data delay for iOS traffic
├── Cross-device attribution limited
└── View-through less reliable for iOS
```

### Aggregated Event Measurement (AEM)

```
What AEM Does:
├── Aggregates iOS conversion data
├── Privacy-compliant measurement
├── Removes device identifiers
├── Applies modeling and noise

2025 Update:
├── 8-event limit REMOVED
├── Manual prioritization no longer needed
├── AEM now automatic for eligible events
└── Advanced Mobile Measurement (AMM) enabled
```

### iOS Attribution Strategy

```
RECOMMENDED SETUP:

1. Event Configuration:
   ├── Focus on high-value events (Purchase)
   ├── CAPI implementation essential
   ├── Enable Aggregated Event Measurement
   └── No manual event ranking needed (2025+)

2. Attribution Expectations:
   ├── Accept 20-30% underreporting
   ├── Use modeled conversions
   ├── Supplement with post-purchase surveys
   └── Cross-reference with platform data

3. Optimization Approach:
   ├── Trust Meta's modeled data
   ├── Focus on trends, not absolute numbers
   ├── Compare period-over-period
   └── Use multiple measurement sources
```

## Incremental Attribution (2025)

### What Is Incremental Attribution?

```
Traditional Attribution:
├── Counts all conversions after ad exposure
├── Including conversions that would have happened anyway
└── Can cause overclaiming

Incremental Attribution:
├── Measures ONLY conversions CAUSED BY the ad
├── Excludes organic conversions
├── Holdout-based measurement
└── True ad effectiveness
```

### Meta's Incremental Attribution Setting

```
How to Enable:
1. Campaign settings
2. Attribution section
3. Enable "Incremental Attribution"
4. Select conversion event

Impact:
├── Reported conversions LOWER (only incremental)
├── ROAS more accurate (true ad value)
├── Algorithm optimizes for incremental lift
└── Early adopters: 20%+ improvement in true ROI
```

### When to Use Incremental Attribution

```
USE INCREMENTAL WHEN:
├── High retargeting spend
├── Strong organic conversion base
├── Need true incrementality measurement
├── Budget optimization priority
└── Advanced measurement maturity

STICK TO STANDARD WHEN:
├── Low conversion volume
├── New accounts/campaigns
├── Primarily prospecting
├── Need learning phase data
└── Simple measurement needs
```

## Attribution Comparison Framework

### Meta vs Google Attribution

```
COMPARISON NOTES:
├── Different attribution models
├── Different tracking methods
├── Overlap in conversions
└── Don't add together!

Meta Attribution:
├── People-based (logged-in users)
├── Cross-device by default
├── View-through included
└── Click: 7-day, View: 1-day

Google Ads:
├── Cookie/click-based
├── Last-click default (changing)
├── No view-through for search
└── Data-driven attribution available

RECONCILIATION:
├── Accept 20-40% overlap
├── Use holistic measurement (MMM)
├── Post-purchase surveys for truth
└── Don't optimize for one at expense of other
```

### Multi-Touch Attribution Considerations

```
META'S APPROACH:
├── Single-touch (last-touch within window)
├── Full credit to last Meta touchpoint
├── No native multi-touch

FOR MULTI-TOUCH:
├── Use third-party tools (Triple Whale, Northbeam)
├── Implement Marketing Mix Modeling
├── Post-purchase surveys
└── Platform-agnostic measurement
```

## Attribution Configuration Guide

### Setup Checklist

```
BEFORE CONFIGURING:

□ Define conversion events
  └── What actions matter most?

□ Understand buying cycle
  └── How long from awareness to purchase?

□ Set measurement goals
  └── Volume vs. incrementality?

□ Establish baselines
  └── Current performance benchmarks

CONFIGURATION:

□ Campaign level settings
  └── Ads Manager → Campaign → Settings → Attribution

□ Consistent across campaigns
  └── Use same windows for comparison

□ Document choices
  └── Why this configuration?
```

### Attribution Settings by Campaign Type

| Campaign Type | Recommended Window | View-Through | Notes |
|--------------|-------------------|--------------|-------|
| **Prospecting** | 7-day click | 1-day | Capture delayed conversions |
| **Retargeting** | 7-day click | 1-day or None | Consider incrementality |
| **Brand Awareness** | 7-day click | 1-day | Measure full impact |
| **Advantage+ Catalog Ads** | 7-day click | 1-day | Standard e-commerce (formerly DPA) |
| **Lead Gen** | 7-day click | 1-day | Research-heavy decision |
| **App Install** | 7-day click | 1-day | Standard mobile |

## Attribution Analysis

### Comparing Attribution Windows

```
HOW TO ANALYZE IMPACT:

1. Run comparison:
   ├── Export data with 1-day click
   ├── Export data with 7-day click
   └── Compare conversion difference

2. Calculate "extended window lift":
   ├── (7-day conversions - 1-day conversions) / 1-day conversions
   └── Shows delayed conversion rate

3. Interpret:
   ├── >50% lift: Long consideration, use 7-day
   ├── 20-50% lift: Normal, 7-day appropriate
   └── <20% lift: Quick decisions, 1-day sufficient
```

### View-Through Impact Analysis

```
MEASURING VT CONTRIBUTION:

1. Compare periods:
   ├── Period A: VT enabled
   ├── Period B: VT disabled
   └── Measure conversion difference

2. Calculate VT percentage:
   ├── (VT conversions) / (Total conversions)
   └── Shows VT contribution to reported results

3. Evaluate:
   ├── >30% VT: Significant brand influence
   ├── 10-30% VT: Normal awareness contribution
   └── <10% VT: Minimal impact, consider disabling
```

## Troubleshooting Attribution

### Common Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Conversion delay | Sales missing, appear later | Normal for iOS, wait 72hr |
| Over-attribution | More conversions than orders | Check deduplication, VT impact |
| Under-attribution | Fewer conversions than expected | Check pixel/CAPI, attribution window |
| Inconsistent data | Different numbers in reports | Verify date ranges, attribution settings |
| GA4 mismatch | Meta shows more conversions | Different models, VT inclusion |

### Attribution Audit Template

```markdown
# Attribution Audit

## Current Configuration
- Click window: [1-day / 7-day]
- View window: [None / 1-day]
- Incremental: [Yes / No]

## Conversion Analysis
- Reported conversions: [X]
- Platform transactions: [Y]
- Difference: [Z]%

## Attribution Window Analysis
| Window | Conversions | % of Total |
|--------|-------------|------------|
| 1-day click | [X] | [X]% |
| 2-7 day click | [Y] | [Y]% |
| 1-day view | [Z] | [Z]% |

## Recommendations
1. [Recommendation based on analysis]
2. [Additional recommendation]

## Action Items
□ [Action 1]
□ [Action 2]
```

## MCP: Analyze Attribution Impact

```python
# Pull conversions broken down by attribution window to understand click vs view contribution
meta_get_insights(account_id="act_XXXXX", level="campaign", fields=["spend","actions","website_purchase_roas"], date_preset="last_30d")

# Compare attribution at ad set level for the same period
meta_get_insights(account_id="act_XXXXX", level="adset", fields=["actions","cost_per_action_type","spend"], date_preset="last_7d")
```

## Best Practices

```
DO:
├── Keep attribution consistent across campaigns
├── Document your attribution choices
├── Compare trends, not absolute numbers
├── Use multiple measurement sources
├── Accept some measurement uncertainty

DON'T:
├── Change attribution mid-campaign
├── Compare campaigns with different windows
├── Obsess over exact conversion counts
├── Ignore iOS measurement limitations
├── Add Meta + Google conversions together
```
