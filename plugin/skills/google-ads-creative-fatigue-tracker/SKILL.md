---
name: google-ads-creative-fatigue-tracker
description: "This skill should be used when the user asks to \"detect Google Ads creative fatigue\", \"check asset performance decay\", \"find when to refresh Google Ads creatives\", or mentions \"PMax asset group fatigue\", \"Display ad burnout\", \"YouTube creative fatigue\", or \"asset rating decline\"."
---
# Google Ads Creative Fatigue Tracker

## Purpose

Detect and prevent creative fatigue on Google Ads across Display, Performance Max, and YouTube campaigns. Google Ads has **fundamentally different fatigue patterns** than Meta or TikTok - using asset ratings instead of frequency, with longer cycles (4-8 weeks vs 3-14 days).

## The Critical Difference: Google Ads vs Other Platforms

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  CREATIVE FATIGUE: PLATFORM COMPARISON                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  GOOGLE ADS                TIKTOK ADS               META ADS                 │
│  ──────────                ──────────               ─────────                │
│                                                                              │
│  Fatigue onset: 4-8 weeks  Fatigue onset: 3-7 days  Fatigue onset: ~14 days │
│  Indicator: Ad Strength    Indicator: Frequency     Indicator: Frequency    │
│  (PMax); Asset Labels      (Display still uses                               │
│  (Display/RDA only)        performance labels)                               │
│  CTR decline: Very gradual CTR decline: Cliff       CTR decline: Gradual    │
│  (~0.5%/week)              (-20-25%/day)            (~2%/day)               │
│                                                                              │
│  ┌──────────────────────┐  ┌──────────────────────┐ ┌─────────────────────┐ │
│  │ Week 1-2: Learning   │  │ Day 1-2: Learning    │ │ Day 1-7: Learning   │ │
│  │ Week 3-4: Evaluating │  │ Day 2-4: Peak        │ │ Day 7-10: Peak      │ │
│  │ Week 5-6: Optimize   │  │ Day 4-7: Decline     │ │ Day 10-14: Decline  │ │
│  │ Week 7-8: Refresh    │  │ Day 7+: Severe       │ │ Day 14+: Fatigue    │ │
│  └──────────────────────┘  └──────────────────────┘ └─────────────────────┘ │
│                                                                              │
│  Refresh: Every 4-8 weeks  Refresh: Every 3-5 days  Refresh: Every 7-14 days│
│  Asset minimum: 15+        Creatives needed: 8-12   Creatives needed: 4-6   │
│                                                                              │
│  ⚠️ Google Ads fatigues 4x SLOWER than Meta, 8x SLOWER than TikTok!          │
└─────────────────────────────────────────────────────────────────────────────┘
```

## When to Use This Skill

Invoke when user mentions:
- **Performance questions:** "My Google Ads CTR is declining slowly"
- **Asset questions:** "What do PMax asset ratings mean?"
- **Timing questions:** "When should I refresh my Google Ads creatives?"
- **PMax specific:** "My asset group performance is degrading"
- **Display specific:** "My RDA performance is dropping"
- **YouTube specific:** "My video ad is getting fewer views"

## Google Ads Fatigue Detection: Asset Ratings

### Understanding Asset Ratings (Primary Indicator for Display/RDA — Removed for PMax)

Google Ads uses **asset performance ratings** for Display (RDA) campaigns. Note the critical API change:

```
GOOGLE ADS ASSET RATING SYSTEM
══════════════════════════════

⚠️ CRITICAL API CHANGE (v22, 2025):
   Asset performance labels (Best/Good/Low/Pending) were REMOVED for
   Performance Max campaigns in API v22. They are still available for
   Display (RDA) campaigns.

   For PMax fatigue detection, use PERFORMANCE TRENDS instead of asset labels.
   See "PMax Fatigue Detection" section below.

RATING MEANINGS (Display/RDA only):
─────────────────────────────────────
┌─────────────┬─────────────────────────────────────────────────────────────┐
│ Rating      │ What It Means                                               │
├─────────────┼─────────────────────────────────────────────────────────────┤
│ Best        │ Outperforms other assets - KEEP and create variations       │
│ Good        │ Average or above - KEEP, monitor for changes                │
│ Low         │ Underperforms vs others - REPLACE after 30+ days of "Low"   │
│ Pending     │ Insufficient data - WAIT (needs 2-4 weeks minimum)          │
└─────────────┴─────────────────────────────────────────────────────────────┘

⚠️ Ratings are RELATIVE within your asset group
   "Low" doesn't mean bad in absolute terms - just worse than others

⚠️ Minimum assets needed for meaningful ratings: 3-5 per type
   Without enough assets, ratings can't be calculated properly
```

### Fatigue Detection by Campaign Type

#### Performance Max Asset Groups

```
PMAX CREATIVE FATIGUE DETECTION
═══════════════════════════════

⚠️ NOTE: Asset performance labels (Best/Good/Low) were REMOVED for PMax
   in API v22. For PMax, rely on performance trends and search term data.

SIGNAL 1: PERFORMANCE TRENDS (Primary for PMax)
────────────────────────────────────────────────
Weekly tracking:
├── CTR decline: >10% week-over-week for 2+ weeks
├── Conv Rate decline: >15% from baseline
├── CPM rise: >20% without competition changes
└── ROAS decline: >15% sustained over 2+ weeks

google_ads_run_gaql(query="
  SELECT
    campaign.name,
    segments.week,
    metrics.impressions,
    metrics.clicks,
    metrics.ctr,
    metrics.cost_micros,
    metrics.conversions,
    metrics.conversions_value
  FROM campaign
  WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY campaign.name, segments.week ASC
")

SIGNAL 2: SEARCH TERM QUALITY (v21+ PMax feature)
────────────────────────────────────────────────────
Declining search query quality = early creative/signal fatigue signal:

google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign_search_term_view.search_term,
    metrics.impressions,
    metrics.clicks,
    metrics.cost_micros,
    metrics.conversions
  FROM campaign_search_term_view
  WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
    AND segments.date DURING LAST_14_DAYS
    AND metrics.cost_micros > 0
  ORDER BY metrics.cost_micros DESC
  LIMIT 100
")
→ Surge in irrelevant search terms + declining conv rate = creative/audience signal fatigue

SIGNAL 3: ASSET GROUP PERFORMANCE
─────────────────────────────────
Compare asset groups:
├── Declining vs stable asset groups
├── Watch for consistent underperformers
└── Budget share shifting away automatically

FATIGUE TIMELINE (PMAX):
────────────────────────
┌─────────────────────────────────────────────────────────────────────────────┐
│ WEEK 1-2: LEARNING PHASE                                                     │
│ ├── Asset ratings: "Pending"                                                │
│ ├── No changes - let system learn                                           │
│ └── Monitor delivery and basics only                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ WEEK 3-4: EVALUATION PHASE                                                   │
│ ├── First ratings appear (may be unstable)                                  │
│ ├── Note initial performers                                                 │
│ └── Still too early for optimization                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ WEEK 5-6: FIRST OPTIMIZATION                                                 │
│ ├── Ratings stabilize                                                       │
│ ├── Replace consistently "Low" assets                                       │
│ ├── Add variations of "Best" performers                                     │
│ └── This is your baseline performance                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ WEEK 7-8+: ONGOING OPTIMIZATION / FATIGUE WATCH                              │
│ ├── Monthly 20-30% asset refresh                                            │
│ ├── Watch for Best→Good→Low transitions                                     │
│ ├── Seasonal/promotional updates                                            │
│ └── Fatigue signs typically appear here                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Display Campaigns (RDA)

```
DISPLAY / RDA CREATIVE FATIGUE DETECTION
════════════════════════════════════════

SIGNAL 1: ASSET PERFORMANCE LABELS (Still available for Display/RDA)
──────────────────────────────────────────────────────────────────────
Rating system for Display (RDA) — unlike PMax, still active for Display:
├── Best/Good/Low/Pending
├── Check Ads → Assets → View asset details
└── Replace "Low" after 30+ days consistent

google_ads_run_gaql(query="
  SELECT
    ad_group.name,
    campaign.name,
    ad_group_ad.ad.type,
    metrics.impressions,
    metrics.ctr,
    metrics.cost_micros,
    metrics.conversions
  FROM ad_group_ad
  WHERE campaign.advertising_channel_type = 'DISPLAY'
    AND ad_group_ad.ad.type = 'RESPONSIVE_DISPLAY_AD'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")
# Note: RDA asset performance labels are not available via GAQL —
# check in Google Ads UI: Ads → Assets → View asset details.

SIGNAL 2: AD PERFORMANCE METRICS
────────────────────────────────
┌─────────────────┬──────────────┬──────────────┬────────────────────────────┐
│ Metric          │ Healthy      │ Warning      │ Critical (Fatigue Likely)  │
├─────────────────┼──────────────┼──────────────┼────────────────────────────┤
│ CTR             │ >0.3%        │ 0.1-0.3%     │ <0.1% sustained            │
│ CTR decline     │ <5%/month    │ 5-10%/month  │ >10%/month                 │
│ Conv Rate       │ >1%          │ 0.5-1%       │ <0.5% declining            │
│ CPA increase    │ <10%         │ 10-25%       │ >25% from baseline         │
└─────────────────┴──────────────┴──────────────┴────────────────────────────┘

SIGNAL 3: PLACEMENT FATIGUE
───────────────────────────
High-performing placements declining:
├── Check per-placement performance
├── Top sites showing CTR decline
└── May indicate audience saturation on those sites

DISPLAY FATIGUE TIMELINE:
────────────────────────
├── Week 1-2: Learning (don't touch)
├── Week 3-4: First optimization opportunity
├── Week 5-8: Monitor for decline patterns
├── Week 8+: Plan refresh if decline detected
└── Monthly: 20-30% creative refresh recommended
```

#### YouTube Campaigns

```
YOUTUBE VIDEO AD FATIGUE DETECTION
══════════════════════════════════

SIGNAL 1: VIEW-THROUGH RATE (VTR) DECLINE
─────────────────────────────────────────
Skippable in-stream ads:
├── Healthy: >25-30% VTR
├── Warning: 20-25% VTR (declining)
├── Fatigue: <20% VTR or >15% decline from peak
└── Severe: <15% VTR

SIGNAL 2: WATCH TIME METRICS
────────────────────────────
├── Average % viewed declining
├── Drop-off points shifting earlier
├── "Skip" behavior increasing
└── Engagement (likes/comments) declining

SIGNAL 3: CPV TRENDS
────────────────────
├── Healthy: Stable or declining CPV
├── Warning: +10-20% CPV increase
├── Fatigue: +30%+ CPV increase
└── Combined with VTR decline = confirmed fatigue

YOUTUBE FATIGUE TIMELINE:
─────────────────────────
├── Week 1-2: Learning (delivery ramp-up)
├── Week 3-4: Peak performance
├── Week 5-8: Stable performance expected
├── Week 8-12: Watch for fatigue signs
├── Week 12+: Most videos show some fatigue
└── Typical video lifespan: 8-16 weeks
```



See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.



## Prevention Strategies

### Asset Library Requirements

```
GOOGLE ADS CREATIVE REQUIREMENTS
════════════════════════════════

PERFORMANCE MAX:
───────────────
Per Asset Group (for healthy rotation):
├── Headlines: 5-15 (aim for 10+)
├── Long Headlines: 3-5
├── Descriptions: 4-5
├── Images (landscape): 5-10
├── Images (square): 5-10
├── Images (portrait): 3-5
├── Logos: 2-3
├── Videos: 2-5 (highly recommended)
└── TOTAL: 40+ assets per asset group

DISPLAY (RDA):
──────────────
├── Landscape Images: 5
├── Square Images: 5
├── Short Headlines: 5
├── Long Headline: 1
├── Descriptions: 5
├── Logos: 2
├── Videos: 1-5 (optional but recommended)
└── TOTAL: 25+ assets per ad

YOUTUBE:
────────
├── Video variants: 3-5 per campaign
├── Different lengths: 6s, 15s, 30s, 60s+
├── Different hooks: Test first 5 seconds
├── Different CTAs: Various call-to-actions
└── Companion banners: Match video style
```

### Refresh Schedule

```
GOOGLE ADS CREATIVE REFRESH SCHEDULE
════════════════════════════════════

WEEKLY CHECKS:
──────────────
□ Asset ratings changes
□ Major metric shifts (>10% any direction)
□ Disapproved ads
□ "Limited" warnings

BI-WEEKLY ACTIONS:
──────────────────
□ Replace any asset consistently "Low" for 30+ days
□ Add 1-2 new image variations
□ Test new headline angles
□ Review video performance

MONTHLY REFRESH (CRITICAL):
───────────────────────────
□ Replace 20-30% of assets
□ Add seasonal/promotional content
□ New image concepts
□ Fresh headline/description copy
□ Review and update audience signals (PMax)

QUARTERLY OVERHAUL:
──────────────────
□ Full creative strategy review
□ New photoshoot/video production
□ Brand guideline updates
□ Competitive creative analysis
□ Test new formats (if available)

SEASONAL CALENDAR:
──────────────────
├── 3-4 weeks before peak: Upload seasonal assets
├── During peak: Monitor performance daily
├── After peak: Return to evergreen content
└── Always maintain evergreen baseline

REFRESH VOLUME BY SCENARIO:
───────────────────────────
┌─────────────────┬───────────────────┬────────────────────────────────────┐
│ Scenario        │ Refresh Frequency │ Volume                             │
├─────────────────┼───────────────────┼────────────────────────────────────┤
│ Stable perform  │ Monthly           │ 20% of assets                      │
│ Slight decline  │ Bi-weekly         │ 30% of assets                      │
│ Clear fatigue   │ Weekly            │ 50% of assets over 2 weeks         │
│ Severe fatigue  │ Immediate         │ 100% (full refresh)                │
│ Seasonal peak   │ Pre-peak          │ Add 30-50% new seasonal assets     │
└─────────────────┴───────────────────┴────────────────────────────────────┘
```

### Content Mix for Longevity

```
GOOGLE ADS CREATIVE MIX (RECOMMENDED)
═════════════════════════════════════

IMAGE MIX:
──────────
Product shots: 40%
├── Clean product imagery
├── Multiple angles
├── White/neutral backgrounds
└── Typical lifespan: 8-12 weeks

Lifestyle images: 40%
├── Products in context
├── People using products
├── Emotional appeal
└── Typical lifespan: 6-10 weeks

Promotional/Seasonal: 20%
├── Sale imagery
├── Holiday themes
├── Limited time offers
└── Typical lifespan: Campaign duration

HEADLINE MIX:
─────────────
Brand headlines: 20%
├── "[Brand] Official"
├── "Shop [Brand] Online"
└── Long lifespan (rarely fatigue)

Benefit headlines: 30%
├── "Free Shipping"
├── "30-Day Returns"
└── Medium lifespan

Action headlines: 30%
├── "Shop Now"
├── "Get Yours Today"
└── Medium lifespan

Promotional headlines: 20%
├── "Up to 50% Off"
├── "New Arrivals"
└── Short lifespan (rotate frequently)

VIDEO MIX (For PMax/YouTube):
─────────────────────────────
Product demos: 30%
├── How it works
├── Feature showcase
└── Lifespan: 12-16 weeks

Testimonials: 30%
├── Customer reviews
├── Social proof
└── Lifespan: 8-12 weeks

Brand story: 20%
├── Company values
├── Behind the scenes
└── Lifespan: 16+ weeks

Short-form (6-15s): 20%
├── Quick promos
├── Bumper ads
└── Lifespan: 6-10 weeks
```

## Recovery Playbook

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GOOGLE ADS FATIGUE RECOVERY                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                First: REPLACE LOW-PERFORMING ASSETS
                (Most important action)
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
            WORKS                           DOESN'T WORK
            (Ratings improve,                      │
            metrics stabilize)                     │
                    │                               ▼
                    ▼                  Second: ADD NEW CREATIVE CONCEPTS
             Monitor &                  (Not just variations - new angles)
             Continue                              │
                                    ┌───────────────┴───────────────┐
                                    │                               │
                                    ▼                               ▼
                            WORKS                           STILL STRUGGLING
                                    │                               │
                                    ▼                               ▼
                             Scale up              Third: REVIEW TARGETING/AUDIENCE
                                                   (PMax audience signals,
                                                    Display audiences)
                                                              │
                                                              ▼
                                                   Fourth: CAMPAIGN RESTRUCTURE
                                                   (New asset groups, fresh start)
```

### Budget Reallocation During Recovery

```
BUDGET STRATEGY DURING FATIGUE
══════════════════════════════

HEALTHY STATE:
──────────────
├── Continue normal budget
├── 10% allocated to creative testing
└── Standard optimization cadence

WARNING STATE:
──────────────
├── Maintain budget (don't reduce)
├── Increase testing budget to 20%
├── Accelerate creative production
└── Daily monitoring

CRITICAL STATE:
───────────────
├── Reduce budget 20-30% temporarily
├── Reallocate to fresh creatives/campaigns
├── Aggressive creative refresh
├── Consider pausing worst performers
└── Plan full campaign rebuild if needed
```

## Benchmarks

### Healthy Performance Metrics

```
GOOGLE ADS CREATIVE HEALTH BENCHMARKS
═════════════════════════════════════

PERFORMANCE MAX:
───────────────
┌─────────────────┬──────────────┬──────────────┬──────────────┐
│ Metric          │ Healthy      │ Warning      │ Critical     │
├─────────────────┼──────────────┼──────────────┼──────────────┤
│ "Best" assets   │ 20-30%       │ 10-20%       │ <10%         │
│ "Low" assets    │ <20%         │ 20-40%       │ >40%         │
│ CTR trend       │ Stable/up    │ -5-10%/month │ >-10%/month  │
│ ROAS trend      │ Stable/up    │ -10-15%      │ >-15%        │
│ Conv Rate       │ Stable/up    │ -10-20%      │ >-20%        │
└─────────────────┴──────────────┴──────────────┴──────────────┘

DISPLAY (RDA):
──────────────
┌─────────────────┬──────────────┬──────────────┬──────────────┐
│ Metric          │ Healthy      │ Warning      │ Critical     │
├─────────────────┼──────────────┼──────────────┼──────────────┤
│ CTR             │ >0.3%        │ 0.15-0.3%    │ <0.15%       │
│ Conv Rate       │ >1%          │ 0.5-1%       │ <0.5%        │
│ CPA trend       │ Stable       │ +10-25%      │ >+25%        │
│ Asset ratings   │ Mixed B/G    │ Many "Low"   │ Mostly "Low" │
└─────────────────┴──────────────┴──────────────┴──────────────┘

YOUTUBE:
────────
┌─────────────────┬──────────────┬──────────────┬──────────────┐
│ Metric          │ Healthy      │ Warning      │ Critical     │
├─────────────────┼──────────────┼──────────────┼──────────────┤
│ VTR (skippable) │ >30%         │ 20-30%       │ <20%         │
│ CPV trend       │ Stable/down  │ +10-30%      │ >+30%        │
│ Avg % viewed    │ >40%         │ 25-40%       │ <25%         │
│ Engagement      │ Stable/up    │ Declining    │ Dropped >50% │
└─────────────────┴──────────────┴──────────────┴──────────────┘
```

### Platform Comparison

```
CREATIVE FATIGUE: GOOGLE ADS vs OTHERS
══════════════════════════════════════

┌─────────────────────┬─────────────┬─────────────┬─────────────┐
│ Factor              │ Google Ads  │ Meta        │ TikTok      │
├─────────────────────┼─────────────┼─────────────┼─────────────┤
│ Fatigue onset       │ 4-8 weeks   │ ~14 days    │ 3-7 days    │
│ Primary indicator   │ Ad Strength │ Frequency   │ Frequency   │
│                     │ (PMax v22+) │             │             │
│                     │ Asset Label │             │             │
│                     │ (Display)   │             │             │
│ Decline pattern     │ Very gradual│ Gradual     │ Cliff/sudden│
│ Refresh frequency   │ Monthly     │ Bi-weekly   │ Every 3-5d  │
│ Assets needed       │ 15+ per AG  │ 4-6 per set │ 8-12 per    │
│ Learning phase      │ 2-4 weeks   │ ~7 days     │ 1-2 days    │
│ Video importance    │ High (PMax) │ Medium      │ Critical    │
│ Seasonality impact  │ High        │ Medium      │ Lower       │
└─────────────────────┴─────────────┴─────────────┴─────────────┘
```

## Output Template

When diagnosing Google Ads creative fatigue, provide:

```


See [detailed-reference.md](references/detailed-reference.md) for details.



## Monitoring Checklist

### Weekly Checks
- [ ] Asset ratings in PMax/Display
- [ ] CTR trend (last 7 days vs previous 7)
- [ ] Any "Limited" or warning flags
- [ ] Top/bottom performing assets

### Bi-Weekly Checks
- [ ] Overall performance trend (2-week window)
- [ ] Identify consistently "Low" assets (30+ days)
- [ ] Plan asset replacements
- [ ] Review competitive landscape

### Monthly Review
- [ ] Full asset audit (all ratings)
- [ ] Execute 20-30% refresh
- [ ] Compare to previous month
- [ ] Update seasonal content
- [ ] Document learnings

### Quarterly Review
- [ ] Creative strategy assessment
- [ ] Asset performance analysis
- [ ] Production planning for next quarter
- [ ] Test new formats/approaches
- [ ] Budget vs creative performance

---

*Based on 2025-2026 Google Ads research. Google Ads creative fatigue is fundamentally different from Meta/TikTok - longer cycles, asset ratings vs frequency, and gradual decline patterns. Plan for 4-8 week refresh cycles.*
