---
name: tiktok-benchmark-database
description: "This skill should be used when the user asks to \"look up TikTok benchmarks\", \"compare TikTok CPM to industry average\", \"check TikTok Spark Ads benchmarks\", or mentions \"is my TikTok CTR good\", \"TikTok ROAS benchmark\", or \"TikTok Shop performance standards\". Do NOT use for: TikTok creative fatigue detection (use tiktok-creative-fatigue-tracker), TikTok video hook/length optimization (use tiktok-video-performance-analyzer), or TikTok attribution questions (use tiktok-attribution-guide)."
---
# TikTok Ads Benchmark Database

## Overview

This skill provides a comprehensive database of TikTok Ads benchmarks by industry, ad format, objective, and creative type, so you can assess how your metrics perform compared to market standards.

## Benchmark Disclaimer

```
IMPORTANT CONTEXT

These benchmarks are based on:
+-- Lebesgue "TikTok Ads Benchmarks for CTR, CR, and CPM" (Mar 2026)
+-- Tinuiti "Digital Ads Benchmark Report Q4 2025" (Jan 2026)
+-- Jonas Agency "2026 Paid Social and Video Media Benchmarks" (Feb 2026)
+-- TikTok Creative Best Practices Guide 2025
+-- Primarily focused on US/EU markets
+-- Focus on e-commerce & DTC brands

TikTok-Specific Factors:
+-- Creative fatigue is 4x faster than Meta
+-- Video quality impact is significant
+-- Hook performance (first 2 sec) is critical
+-- UGC often outperforms polished content
+-- Seasonal spikes are more extreme (TikTok Shop)
```

## CPM Benchmarks

```
COST PER MILLE (CPM) BY OBJECTIVE
=================================

Objective              │ Poor    │ Average │ Good    │ Excellent
───────────────────────┼─────────┼─────────┼─────────┼──────────
Reach                  │ >€8     │ €5-8    │ €3-5    │ <€3
Traffic                │ >€12    │ €7-12   │ €4-7    │ <€4
Video Views            │ >€6     │ €3-6    │ €1.50-3 │ <€1.50
App Install            │ >€18    │ €10-18  │ €6-10   │ <€6
Conversions            │ >€20    │ €12-20  │ €7-12   │ <€7
Catalog Sales          │ >€15    │ €10-15  │ €6-10   │ <€6

CPM BY INDUSTRY:
├── Fashion/Apparel: €6-12
├── Beauty/Cosmetics: €5-10
├── Food & Beverage: €4-8
├── Electronics: €10-18
├── Gaming: €3-8
├── Health & Fitness: €7-12
├── Home & Garden: €8-14
└── Finance/Insurance: €15-30
```

## CPC Benchmarks

```
COST PER CLICK (CPC) BY INDUSTRY
================================

Industry              │ Poor    │ Average │ Good    │ Excellent
──────────────────────┼─────────┼─────────┼─────────┼──────────
Fashion/Apparel       │ >€0.80  │ €0.40-0.80│€0.20-0.40│ <€0.20
Beauty/Cosmetics      │ >€0.70  │ €0.35-0.70│€0.18-0.35│ <€0.18
Food & Beverage       │ >€0.60  │ €0.30-0.60│€0.15-0.30│ <€0.15
Electronics           │ >€1.20  │ €0.60-1.20│€0.35-0.60│ <€0.35
Gaming                │ >€0.50  │ €0.25-0.50│€0.12-0.25│ <€0.12
Health & Fitness      │ >€0.90  │ €0.45-0.90│€0.25-0.45│ <€0.25
Home & Garden         │ >€1.00  │ €0.50-1.00│€0.30-0.50│ <€0.30
General E-commerce    │ >€0.85  │ €0.40-0.85│€0.22-0.40│ <€0.22

CPC BY AD FORMAT:
├── In-Feed Ads: €0.30-0.80
├── TopView: €0.50-1.50
├── Spark Ads: €0.25-0.60 (typically lower)
├── Collection Ads: €0.35-0.90
└── TikTok Shop: €0.20-0.50
```

## CTR Benchmarks

```
CLICK-THROUGH RATE (CTR) BY FORMAT
==================================

Ad Format               │ Poor    │ Average │ Good    │ Excellent
────────────────────────┼─────────┼─────────┼─────────┼──────────
In-Feed Ads             │ <0.5%   │ 0.5-1.5%│ 1.5-2.5%│ >2.5%
Spark Ads               │ <1.0%   │ 1.0-2.0%│ 2.0-3.5%│ >3.5%
TopView                 │ <1.5%   │ 1.5-3.0%│ 3.0-5.0%│ >5.0%
Collection Ads          │ <1.2%   │ 1.2-2.2%│ 2.2-3.5%│ >3.5%
Branded Effects         │ <0.5%   │ 0.5-1.0%│ 1.0-2.0%│ >2.0%
TikTok Shop Ads         │ <1.5%   │ 1.5-3.0%│ 3.0-5.0%│ >5.0%

CTR BY OBJECTIVE:
+-- Awareness (Reach): 0.5-1.5%
+-- Traffic: 1.0-2.5%
+-- Video Views: 0.3-1.0% (focus on view rate)
+-- Conversions: 1.5-3.5%
+-- Catalog Sales: 1.2-3.0%
```

## Conversion Rate Benchmarks

```
CONVERSION RATE BY INDUSTRY
===========================

Industry              │ Poor    │ Average │ Good    │ Excellent
──────────────────────┼─────────┼─────────┼─────────┼──────────
Fashion/Apparel       │ <1.5%   │ 1.5-3%  │ 3-5%    │ >5%
Beauty/Cosmetics      │ <2%     │ 2-4%    │ 4-7%    │ >7%
Food & Beverage       │ <1%     │ 1-2.5%  │ 2.5-4%  │ >4%
Electronics           │ <0.8%   │ 0.8-2%  │ 2-3.5%  │ >3.5%
Gaming (App Install)  │ <5%     │ 5-12%   │ 12-20%  │ >20%
Health & Fitness      │ <1.2%   │ 1.2-2.5%│ 2.5-4%  │ >4%
Home & Garden         │ <1%     │ 1-2%    │ 2-3.5%  │ >3.5%

TIKTOK SHOP CONVERSION RATES:
├── Shop Tab browsing to purchase: 4-8%
├── Live Shopping CVR: 5-12%
├── Video Shopping Ads: 3-6%
├── Product Links: 2-4%
└── Shop Ads (in-feed): 4-10%

CONTEXT: TikTok Shop CVR 25% higher vs external site
```

## CPA/CPL Benchmarks

```
COST PER ACQUISITION/LEAD BY VERTICAL
=====================================

E-commerce (Purchase):
├── Fashion: €12-25 CPA
├── Beauty: €10-22 CPA
├── Electronics: €25-50 CPA
├── Home: €20-40 CPA
└── General DTC: €15-35 CPA

Lead Generation:
├── Education: €15-35 CPL
├── Finance: €30-70 CPL
├── B2B/SaaS: €50-120 CPL
├── Services: €20-45 CPL
└── Real Estate: €25-60 CPL

App Installs:
├── Gaming: €1.50-4.00 CPI
├── Utility: €2.50-6.00 CPI
├── E-commerce App: €3.00-8.00 CPI
├── Social: €2.00-5.00 CPI
└── Finance App: €5.00-15.00 CPI

TikTok Shop vs External Site:
├── Shop Ads CPA: 25% lower typically
├── External Site CPA: Higher but more control
└── Decision: Low-AOV → Shop, High-AOV → External
```

## ROAS Benchmarks

```
RETURN ON AD SPEND (ROAS) BY CATEGORY
=====================================

Category              │ Poor    │ Average │ Good    │ Excellent
──────────────────────┼─────────┼─────────┼─────────┼──────────
Fashion (Low AOV)     │ <1.5x   │ 1.5-2.5x│ 2.5-4x  │ >4x
Fashion (High AOV)    │ <2x     │ 2-3.5x  │ 3.5-5x  │ >5x
Beauty                │ <2x     │ 2-3.5x  │ 3.5-6x  │ >6x
Electronics           │ <1.2x   │ 1.2-2x  │ 2-3x    │ >3x
Food & Beverage       │ <1.5x   │ 1.5-3x  │ 3-5x    │ >5x
Health & Fitness      │ <1.8x   │ 1.8-3x  │ 3-5x    │ >5x
Home & Garden         │ <1.5x   │ 1.5-2.5x│ 2.5-4x  │ >4x

TIKTOK-SPECIFIC ROAS NOTES:
├── First 72 hours: ROAS may be lower (learning)
├── Week 2-4: Optimal ROAS window
├── After 30 days: Expect 10-20% decline (fatigue)
└── TikTok Shop: Generally higher ROAS vs external
```

## Video Performance Benchmarks

```
VIDEO VIEW METRICS
==================

Metric                  │ Poor    │ Average │ Good    │ Excellent
────────────────────────┼─────────┼─────────┼─────────┼──────────
2-Second View Rate      │ <30%    │ 30-50%  │ 50-70%  │ >70%
6-Second View Rate      │ <20%    │ 20-35%  │ 35-50%  │ >50%
ThruPlay (15s+)         │ <8%     │ 8-15%   │ 15-25%  │ >25%
25% View Rate           │ <25%    │ 25-40%  │ 40-55%  │ >55%
50% View Rate           │ <12%    │ 12-22%  │ 22-35%  │ >35%
75% View Rate           │ <6%     │ 6-12%   │ 12-20%  │ >20%
100% Completion         │ <3%     │ 3-8%    │ 8-15%   │ >15%

HOOK PERFORMANCE (First 2 Seconds):
+-- Critical metric for TikTok success
+-- Target: >50% 2-second view rate
+-- <30% = Hook is failing, creative refresh needed
+-- >70% = Excellent hook, scale this creative

OPTIMAL VIDEO LENGTH BY OBJECTIVE:
├── Awareness: 15-20 seconds
├── Consideration: 10-15 seconds
├── Conversion: 6-10 seconds (clear CTA)
└── TikTok Shop: 9-15 seconds
```

## Spark Ads vs Regular Ads

```
SPARK ADS BENCHMARK COMPARISON
==============================

Metric          │ Regular Ads │ Spark Ads │ Spark Advantage
────────────────┼─────────────┼───────────┼────────────────
CTR             │ 1.0-1.8%    │ 1.5-3.0%  │ +50-70%
Engagement Rate │ 2-4%        │ 4-8%      │ +100%
Video Completion│ 8-12%       │ 15-25%    │ +80-110%
CVR             │ 2-3.5%      │ 3.5-6%    │ +65-70%
CPM             │ €8-15       │ €6-12     │ -15-25%
CPC             │ €0.50-1.00  │ €0.30-0.70│ -30-40%

WHEN TO USE SPARK ADS:
├── Brand building + performance
├── Creator/influencer content
├── Social proof needed
├── TOFU/MOFU campaigns
└── When authenticity matters

WHEN TO USE REGULAR ADS:
├── Strict brand guidelines
├── Product launches (controlled messaging)
├── Retargeting (branded content)
└── Direct response BOFU
```

## UGC vs Polished Content

```
UGC VS POLISHED CREATIVE BENCHMARKS
===================================

Metric          │ Polished    │ UGC        │ UGC Advantage
────────────────┼─────────────┼────────────┼───────────────
CPM             │ €10-18      │ €6-12      │ -18% average
CTR             │ 0.8-1.5%    │ 1.2-2.5%   │ +12% average
Engagement      │ 2-4%        │ 5-10%      │ +150%
Conversion Rate │ 2-3%        │ 2.5-4%     │ +25%
Creative Lifespan│ 2-5 days   │ 5-10 days  │ UGC lasts ~2x longer

UGC BEST PRACTICES:
├── Authentic, phone-recorded look
├── Real people, relatable scenarios
├── First-person POV performs well
├── Text overlays + native TikTok fonts
└── Trending sounds/audio

POLISHED CONTENT USE CASES:
├── Brand launches/announcements
├── High-end luxury products
├── Corporate/B2B messaging
└── Product demonstrations requiring clarity
```

## TikTok Shop Specific Benchmarks

```
TIKTOK SHOP PERFORMANCE METRICS
===============================

Shop Ads Performance:
├── CTR: 1.5-4.0%
├── CVR: 4-10%
├── CPA: 25% lower vs external
├── ROAS: 20-40% higher vs external
└── AOV: 15-20% lower (impulse buys)

Live Shopping Metrics:
├── Viewer to Buyer CVR: 5-12%
├── Average Watch Time: 8-15 minutes
├── Peak Hours: 6-9 PM local
├── Best Days: Weekend evenings
└── GMV per Live: Highly variable

Product Feed Optimization:
├── Title click rate impact: +15-25%
├── Image quality impact: +10-20% CVR
├── Price visibility: +20% consideration
└── Review ratings: +30% trust signal

GMV MAX CAMPAIGN BENCHMARKS:
├── Learning period: 5+ days
├── Minimum conversions: 30/week
├── Expected CPA improvement: 10-20%
└── Best for: High-volume SKUs
```

## Frequency & Fatigue Benchmarks

```
FREQUENCY CAPS & FATIGUE THRESHOLDS
===================================

Frequency Guidelines:
├── Prospecting: 4-5 impressions/user/week
├── Retargeting: 6-8 impressions/user/week
├── TikTok Shop: 5-7/week (higher tolerance)
└── Brand Awareness: 3-4/week

CREATIVE FATIGUE SIGNALS:
│
├── CTR drop >15% week-over-week → REFRESH
├── CPM increase >20% without budget change → FATIGUE
├── CVR drop >20% with stable traffic → CREATIVE ISSUE
├── Frequency >7/week → BURNOUT RISK
└── Engagement rate halved → IMMEDIATE ACTION

FATIGUE TIMELINE (TikTok vs Meta):
├── TikTok onset: 3-7 days
├── Meta onset: 14-21 days
├── TikTok = 4x faster fatigue
└── Creative rotation: Weekly for TikTok
```

## Seasonal Adjustment Factors

```
SEASONAL VARIATIONS
====================

Periode              │ CPM Factor │ CPA Factor │ Notes
─────────────────────┼────────────┼────────────┼──────────────
January              │   0.75     │   0.85     │ Post-holiday dip
February             │   0.85     │   0.90     │ Valentine's spike
March-April          │   0.90     │   0.95     │ Spring baseline
May-June             │   0.95     │   1.00     │ Summer prep
July-August          │   0.85     │   0.95     │ Summer lull
September            │   1.00     │   1.00     │ Back-to-school
October              │   1.15     │   1.05     │ Q4 ramp
November             │   1.50     │   1.30     │ Black Friday/Mega
December 1-20        │   1.60     │   1.35     │ Holiday peak
December 21-31       │   1.20     │   1.15     │ Post-Christmas

TIKTOK-SPECIFIC EVENTS:
├── Chinese New Year: +30-50% for relevant audiences
├── TikTok Shop Mega Sales: +40-60% CPM spikes
├── Prime Day equivalent: +25-35%
└── Singles Day (11.11): +50-80% (APAC focus)
```

## Attribution Considerations

```
TIKTOK ATTRIBUTION VS OTHER PLATFORMS
=====================================

Default Attribution Windows:
├── Click-through: 7 days
├── View-through: 1 day
├── TikTok Shop: 28 days (extended)

ATTRIBUTION DISCREPANCIES:

TikTok vs GA4:
├── Expected gap: 15-25%
├── TikTok reports 30% more via VTA
├── GA4 undercounts view-through
└── Solution: Use UTMs + lift tests

TikTok vs Meta:
├── Different attribution models
├── TikTok VTA more aggressive
├── Compare click-only for apples-to-apples
└── Run incrementality tests

BEST PRACTICE:
├── Use TikTok data for TikTok optimization
├── Use GA4/MMM for cross-channel decisions
├── Accept 15-25% variance as normal
└── Focus on relative trends, not absolute numbers
```

## Search Ads Benchmarks (Launched Sep 2025)

```
TIKTOK SEARCH ADS (KEYWORD-TARGETED)
=====================================

Available since September 2025 — runs in TikTok search results.
Recommended allocation: 20-30% of total TikTok budget.

Metric              │ Average     │ Good        │ Notes
────────────────────┼─────────────┼─────────────┼──────────────────
CTR                 │ 1.5-3.0%    │ >3.0%       │ Higher intent = higher CTR
CPC                 │ €0.30-0.80  │ <€0.30      │ Comparable to Google Display
Conversion Rate     │ 2-5%        │ >5%         │ Higher intent than In-Feed
Creative Fatigue    │ 14-21 days  │ —           │ Much slower than In-Feed
Best Objective      │ Traffic, Conversions, Lead Gen

KEY DIFFERENCES vs IN-FEED:
├── Higher user intent (actively searching)
├── Keyword-based targeting (not interest/behavior)
├── Lower creative fatigue (search behavior = repeated exposure expected)
└── Works well alongside Google Search for branded + generic queries
```

## Smart+ Campaign Benchmarks

```
SMART+ CAMPAIGN PERFORMANCE (TikTok's Automated Campaign Type)
=============================================================
Launched/expanded Jan 2026. Sub-types: Smart+ Web, Smart+ App, Smart+ Lead Gen, GMV Max.

Metric              │ Smart+      │ Manual      │ Difference
────────────────────┼─────────────┼─────────────┼──────────────────
Setup Time          │ Minutes     │ Hours       │ Automated targeting
CPA (steady state)  │ -10-20%     │ Baseline    │ Algorithm advantage
Learning Phase      │ 5-7 days    │ 3-7 days    │ Similar
Creative Rotation   │ Auto        │ Manual      │ Needs 5-8 assets
Audience Control    │ Low         │ High        │ Tradeoff

WHEN TO USE SMART+:
├── New accounts with limited data
├── Scaling proven campaigns
├── Shop campaigns (GMV Max)
└── When you want hands-off optimization

WHEN TO USE MANUAL:
├── Brand safety requirements
├── Specific audience exclusions needed
├── Testing messaging hypotheses
└── Retargeting campaigns
```

## Benchmark Comparison Template

```
METRIC EVALUATION - [ACCOUNT]
==============================

YOUR METRICS vs BENCHMARKS

Metric      | Your Value  | Benchmark | Difference | Status
------------+-------------+-----------+------------+--------
CPM         │   €[X]      │   €[Y]    │  [+/-Z%] │ [🟢🟡🔴]
CPC         │   €[X]      │   €[Y]    │  [+/-Z%] │ [🟢🟡🔴]
CTR         │   [X]%      │   [Y]%    │  [+/-Z%] │ [🟢🟡🔴]
CVR         │   [X]%      │   [Y]%    │  [+/-Z%] │ [🟢🟡🔴]
CPA         │   €[X]      │   €[Y]    │  [+/-Z%] │ [🟢🟡🔴]
ROAS        │   [X]x      │   [Y]x    │  [+/-Z%] │ [🟢🟡🔴]
2s View     │   [X]%      │   [Y]%    │  [+/-Z%] │ [🟢🟡🔴]

INTERPRETATION:
Green: Above benchmark (>10% better)
Yellow: At benchmark (+/-10%)
Red: Below benchmark (>10% worse)

CREATIVE HEALTH:
+-- Hook Performance: [Strong/Weak]
+-- Fatigue Status: [Fresh/Warning/Fatigued]
+-- Format: [UGC/Polished/Spark]
+-- Age: [X] days

RECOMMENDATIONS:
+-- [Priority 1]
+-- [Priority 2]
+-- [Priority 3]
```

## Example Interaction

**User**: "My TikTok beauty campaign has a CTR of 1.8%, CVR of 3.5%, and CPM of EUR9. Is that good?"

**Claude response**:

"Let me compare your metrics with beauty/cosmetics benchmarks:

---

**BENCHMARK COMPARISON - Beauty/Cosmetics:**

| Metric | Your Value | Benchmark Range | Status |
|--------|------------|-----------------|--------|
| CTR | 1.8% | 0.8-1.5% (average) | Excellent |
| CVR | 3.5% | 2-4% (average) | Good |
| CPM | EUR9 | EUR5-10 (average) | OK |

**Calculated Metrics:**
- CPC: EUR9 / (1.8% x 10) = EUR0.50 --> Good for beauty
- CPA: EUR9 / (1.8% x 3.5% / 100) = EUR14.29 --> Excellent

---

**INTERPRETATION:**

**CTR (1.8%)** - 20% above average. Your creative/hook is working well.

**CVR (3.5%)** - Exactly in the average range. Room for improvement on the landing page or product page.

**CPM (EUR9)** - Normal for beauty. Not too high, not exceptionally low.

---

**RECOMMENDATIONS:**

1. **Keep your creative strategy** - CTR is strong, your hook is working

2. **Focus on CVR improvement**:
   - Test landing page optimizations
   - Try TikTok Shop (often +25% CVR)
   - Add reviews/social proof

3. **Monitor creative fatigue**:
   - On TikTok: refresh after 7-10 days
   - If CTR drops >15% --> new creative needed

4. **Scale potential**: With CPA of EUR14.29 and beauty benchmark EUR10-22, you can safely increase budget.

Would you like me to analyze your hook performance (2-second view rate) for more insight?"

## MCP Tool Examples

Pull benchmark data for comparison:

```
# Get account-wide metrics to compare against benchmarks
tiktok_get_report(
  start_date="2026-03-01",
  end_date="2026-04-04",
  level="campaign",
  metrics=["cpm", "cpc", "ctr", "conversion_rate", "cost_per_conversion",
           "video_watched_2s", "video_views_p100", "spend"]
)

# List campaigns with objective to filter benchmark table
tiktok_query(entity_type="campaigns")
```
