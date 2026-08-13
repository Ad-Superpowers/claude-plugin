---
name: tiktok-attribution-guide
description: "This skill should be used when the user asks to \"understand TikTok attribution\", \"compare TikTok VTA vs CTA\", \"reconcile TikTok and GA4 conversions\", or mentions \"TikTok view-through attribution\", \"TikTok attribution windows\", or \"measure TikTok true impact\". Do NOT use for: TikTok app install attribution/MMP (use tiktok-app-performance-tracker), TikTok creative performance (use tiktok-video-performance-analyzer), or TikTok benchmark lookups (use tiktok-benchmark-database)."
---
# TikTok Attribution Guide

## Purpose

Understand and optimize TikTok's unique attribution model. TikTok's entertainment-first nature means **view-through attribution (VTA)** captures significantly more value than traditional click-based platforms. This skill helps advertisers measure TikTok's true impact and prove ROI.

## Why TikTok Attribution is Different

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TIKTOK vs TRADITIONAL PLATFORMS                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  TRADITIONAL (Google, Meta)              TIKTOK                             │
│  ──────────────────────────              ──────                             │
│                                                                              │
│  User Intent: HIGH                       User Intent: LOW (discovery)       │
│  ├─ Search-driven                        ├─ Entertainment-driven            │
│  ├─ Click-to-convert                     ├─ Watch → remember → convert      │
│  └─ CTR: 2-5%                            └─ CTR: 0.5-1.5%                   │
│                                                                              │
│  Attribution:                            Attribution:                        │
│  ├─ 70-80% click-through (CTA)           ├─ 40-60% click-through (CTA)      │
│  ├─ 20-30% view-through (VTA)            ├─ 40-60% view-through (VTA)       │
│  └─ VTA often ignored                    └─ VTA is CRITICAL                 │
│                                                                              │
│  If you only measure CTA on TikTok:                                         │
│  ══════════════════════════════════                                         │
│  You're missing 40-60% of TikTok's actual impact!                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## When to Use This Skill

Invoke when user mentions:
- **VTA questions:** "How many conversions come from ad views?"
- **Attribution comparison:** "What is the VTA/CTA ratio?"
- **Proving value:** "Does click-based attribution undercount TikTok?"
- **ROAS calculation:** "Should I include VTA in ROAS?"
- **Cross-platform:** "How do I compare TikTok with Google/Meta?"
- **Awareness measurement:** "How do I measure awareness campaigns?"
- **Landing page:** "How many people reach my LP?"

## View-Through vs Click-Through Attribution

### What Each Captures

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ATTRIBUTION MODEL COMPARISON                              │
└─────────────────────────────────────────────────────────────────────────────┘

CLICK-THROUGH ATTRIBUTION (CTA)
───────────────────────────────
User Journey: See Ad → Click → [optional: browse] → Convert

Conversion counted if:
├─ User clicked the ad
├─ Conversion within attribution window (default: 7 days)
└─ Conversion matches tracked event

TikTok metrics:
├─ cta_conversion: Total CTA conversions
├─ cta_purchase: Purchases from clicks
└─ cta_registration: Registrations from clicks


VIEW-THROUGH ATTRIBUTION (VTA)
──────────────────────────────
User Journey: See Ad → Watch (no click) → [leave TikTok] → Convert later

Conversion counted if:
├─ User viewed ad for 6+ seconds OR watched 100% (whichever first)
├─ User did NOT click
├─ Conversion within attribution window (default: 1 day)
└─ Conversion matches tracked event

TikTok metrics:
├─ vta_conversion: Total VTA conversions
├─ vta_purchase: Purchases from views
└─ vta_registration: Registrations from views


WHY VTA MATTERS ON TIKTOK
─────────────────────────
TikTok is an entertainment platform. Users:
├─ Scroll for entertainment, not to shop
├─ See compelling content → remember later
├─ Open browser/app later to search/purchase
└─ Never clicked - but ad drove the conversion

Example:
┌──────────────────────────────────────────────────────────────────┐
│ 7:00 PM: User sees your shoe ad while scrolling TikTok          │
│ 7:00 PM: User keeps scrolling (no click)                        │
│ 9:00 PM: User remembers the shoes while browsing                │
│ 9:00 PM: User Googles "brand name shoes" → purchases            │
│                                                                   │
│ CTA attribution: ❌ Not counted (no click)                       │
│ VTA attribution: ✅ Counted (viewed ad < 1 day ago)              │
│ Without VTA: TikTok gets zero credit for this conversion        │
└──────────────────────────────────────────────────────────────────┘
```

### TikTok Default Attribution Windows

| Window Type | Default | Options | Recommendation |
|-------------|---------|---------|----------------|
| **Click-through** | 7 days | 1, 7, 14, 28 days | 7 days (standard) |
| **View-through** | 1 day | Off, 1 day | 1 day (always enable!) |

**Critical:** Never turn off VTA on TikTok. You'll undercount conversions by 40-60%.

## VTA/CTA Ratio Benchmarks

### What's Healthy?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         VTA/CTA RATIO BENCHMARKS                             │
└─────────────────────────────────────────────────────────────────────────────┘

RATIO = VTA Conversions / CTA Conversions

HEALTHY RANGE BY CAMPAIGN TYPE:
───────────────────────────────

Conversion Campaigns (Purchase/Lead)
├─ Expected ratio: 0.5 - 1.5 (50-150% as many VTA as CTA)
├─ High VTA (>1.5): Normal for awareness-heavy creative
└─ Low VTA (<0.3): Check if VTA enabled, or creative isn't memorable

Traffic Campaigns
├─ Expected ratio: 0.2 - 0.5
├─ Lower ratio expected (clicks are the goal)
└─ If >0.8: You're driving delayed traffic (good for brand)

Awareness/Video View Campaigns
├─ Expected ratio: 1.0 - 3.0
├─ High VTA is the POINT
└─ If <0.5: Creative may not be memorable

BY VERTICAL:
────────────
E-commerce:        0.6 - 1.2 (impulse vs research purchases)
Gaming (mobile):   0.3 - 0.8 (more direct install behavior)
Subscription:      0.8 - 1.5 (consideration period)
Lead Gen:          0.7 - 1.3 (form fills often delayed)
Travel:            1.0 - 2.0 (high research intent)
Luxury/Fashion:    1.2 - 2.5 (heavy consideration)
```

### Interpreting Your Ratio

| Ratio | Interpretation | Action |
|-------|----------------|--------|
| <0.3 | Very low VTA | Check: VTA enabled? Creative memorable? |
| 0.3-0.5 | Low, but normal for some verticals | Monitor, especially for conversion campaigns |
| 0.5-1.0 | Healthy balance | Good - TikTok working as expected |
| 1.0-1.5 | High VTA | Strong brand impact, normal for awareness |
| 1.5-2.0 | Very high VTA | Creative is memorable, consider brand campaigns |
| >2.0 | Extremely high | Verify tracking, or creative driving delayed intent |

## Attribution Window Recommendations

### Choosing the Right Windows

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ATTRIBUTION WINDOW DECISION TREE                          │
└─────────────────────────────────────────────────────────────────────────────┘

What's your average purchase consideration time?

LOW CONSIDERATION (<24h)                    HIGH CONSIDERATION (>24h)
├─ Fast fashion                             ├─ B2B
├─ Food delivery                            ├─ Travel
├─ Mobile gaming                            ├─ Luxury goods
├─ Low-cost items (<€50)                    ├─ High-cost items (>€200)
│                                           │
▼                                           ▼
CTA: 7 days                                 CTA: 14-28 days
VTA: 1 day                                  VTA: 1 day (TikTok max)

WHY VTA IS CAPPED AT 1 DAY:
───────────────────────────
TikTok limits VTA to 1 day to prevent over-attribution.
This is actually conservative - many platforms allow 7-day VTA.

Implication: Even with 1-day VTA, TikTok captures significant delayed conversions.
With longer VTA, numbers would be much higher (but less reliable).
```

### Cross-Platform Window Alignment

For fair comparison across platforms:

| Platform | CTA Window | VTA Window | Notes |
|----------|------------|------------|-------|
| **TikTok** | 7 days | 1 day | VTA max is 1 day |
| **Meta** | 7 days | 1 day | Align with TikTok |
| **Google Ads** | 30 days | 1 day (Display) | Longer CTA is standard |
| **Snapchat** | 28 days | 1 day | Similar to TikTok |
| **Pinterest** | 30 days | 1 day | Consideration platform |

## Landing Page Analysis

### Click-to-Landing Page Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LANDING PAGE VIEW FUNNEL                                │
└─────────────────────────────────────────────────────────────────────────────┘

     CLICKS → LANDING PAGE VIEWS → CONVERSIONS

     100        80 (80% LP view rate)    8 (10% LP CVR)
      │          │                        │
      │          │                        │
      ▼          ▼                        ▼
   You pay    Actually     Actually
   for these  reached LP   converted

METRICS:
─────────
├─ total_landing_page_view: Users who reached your LP
├─ landing_page_view_rate: LP views / clicks × 100
├─ cost_per_landing_page_view: Spend / LP views
└─ complete_payment_roas: Revenue / spend (from LP conversions)

BENCHMARKS:
───────────
| LP View Rate | Status | Likely Cause |
|--------------|--------|--------------|
| >80% | Excellent | Fast page, good experience |
| 60-80% | Acceptable | Some drop-off, normal |
| 40-60% | Concerning | Slow page or bot traffic |
| <40% | Critical | Major page speed/tracking issue |

DIAGNOSE LOW LP VIEW RATE:
──────────────────────────
1. Page speed (test with PageSpeed Insights)
   └─ TikTok users expect instant loads (<2 seconds)
2. Mobile optimization (most TikTok = mobile)
   └─ Non-mobile friendly pages = immediate bounce
3. Redirect chains (track time from click to LP)
   └─ Each redirect loses users
4. Click fraud/bot traffic
   └─ Check audience insights for anomalies
```

## Proving TikTok's Incremental Value

### The Attribution Challenge

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    "TIKTOK ISN'T WORKING" - OR IS IT?                        │
└─────────────────────────────────────────────────────────────────────────────┘

COMMON SCENARIO:
────────────────
CMO: "TikTok CPA is €30, Google CPA is €15. TikTok isn't working."

REALITY CHECK:
──────────────
                              TikTok                Google
                              ──────                ──────
CTA Conversions:              100                   200
VTA Conversions:              80                    20
─────────────────────────────────────────────────────────────
Total Attributed:             180                   220
Spend:                        €5,400                €3,300
─────────────────────────────────────────────────────────────
CTA-only CPA:                 €54                   €16.50
FULL CPA (CTA+VTA):           €30                   €15

But wait...
───────────
Many of Google's "conversions" were users who:
1. Saw TikTok ad → remembered brand
2. Googled brand name → clicked Google ad
3. Converted → Google gets credit

TikTok ASSISTED but Google CLOSED. Both deserve credit.
```

### Incremental Value Framework

```
METHOD 1: INCREMENTALITY TESTING (Gold Standard)
────────────────────────────────────────────────
├─ Geo holdout test: Run TikTok in some regions, not others
├─ Compare conversion lift between test/control
├─ Measures TRUE incremental value
└─ Requires: 4+ weeks, significant budget, clean geos

METHOD 2: VTA WEIGHTED ANALYSIS
───────────────────────────────
├─ Count VTA at 50% weight (conservative)
├─ Total value = CTA + (VTA × 0.5)
├─ Compare weighted CPA across platforms
└─ Quick approximation of incrementality

METHOD 3: BRAND SEARCH LIFT
───────────────────────────
├─ Monitor brand search volume before/during TikTok
├─ Correlate TikTok spend with search volume
├─ Attribute % of brand search conversions to TikTok
└─ Requires: Clean data, no other major campaigns

METHOD 4: MMM (Marketing Mix Modeling)
──────────────────────────────────────
├─ Statistical model across all channels
├─ Shows marginal impact of each channel
├─ Best for mature advertisers with history
└─ Requires: Data science resources, 12+ months data
```

### Quick Heuristics for TikTok Value

| Signal | Interpretation |
|--------|----------------|
| Brand search ↑ after TikTok launch | TikTok driving awareness |
| High VTA on TikTok | Platform influence extends beyond click |
| Google brand CPA drops | TikTok warming audiences |
| Direct traffic ↑ | Brand recall from TikTok exposure |
| Social mentions ↑ | TikTok creative resonating |

## GA4 Integration for TikTok

### Tracking TikTok in GA4

```
UTM STRUCTURE FOR TIKTOK:
─────────────────────────

utm_source=tiktok
utm_medium=paid_social (or cpc)
utm_campaign={{campaign_name}}
utm_content={{ad_name}}
utm_term={{adgroup_name}}

TikTok macros available:
├─ __CAMPAIGN_NAME__
├─ __AID__ (ad ID)
├─ __CID__ (creative ID)
└─ __PLACEMENT__


GA4 ATTRIBUTION COMPARISON:
───────────────────────────

TikTok Ads Manager:              GA4:
├─ Uses TikTok pixel             ├─ Uses GA4 events
├─ 7-day CTA + 1-day VTA         ├─ Data-driven or last-click
├─ Counts VTA                    ├─ No VTA (click-based only)
└─ Platform-centric              └─ Cross-channel view

EXPECTED DISCREPANCY:
─────────────────────
GA4 will show 30-50% FEWER conversions than TikTok because:
1. GA4 doesn't track view-through
2. GA4 may attribute to another channel (last-click)
3. Cross-device tracking differs

This is NORMAL. Use both:
├─ TikTok data: Platform optimization
└─ GA4 data: Cross-channel comparison
```

## Cross-Platform Attribution Comparison

### Aligning Metrics Across Platforms

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CROSS-PLATFORM ATTRIBUTION MAP                            │
└─────────────────────────────────────────────────────────────────────────────┘

                TikTok          Meta            Google          LinkedIn
                ──────          ────            ──────          ────────
Click-through   cta_conversion  click_conv      conversions     conversions
View-through    vta_conversion  view_conv       (Display only)  (not separate)
Combined        conversion      conversions     -               -

Default CTA     7 days          7 days          30 days         90 days
Default VTA     1 day           1 day           1 day (Display) N/A

FAIR COMPARISON APPROACH:
─────────────────────────
1. Align windows: 7-day CTA, 1-day VTA everywhere
2. Compare CTA conversions only (conservative)
3. OR: Include VTA at consistent weight (50%)
4. Account for platform role (top/mid/bottom funnel)

PLATFORM ROLE CONSIDERATIONS:
─────────────────────────────
TikTok: Top-of-funnel discovery → expect higher VTA
Meta: Mid-funnel consideration → balanced VTA/CTA
Google Search: Bottom-funnel intent → mostly CTA
LinkedIn: B2B consideration → long cycles, VTA important
```

## Output Template

When analyzing TikTok attribution, provide:

```
## TikTok Attribution Analysis

### Attribution Breakdown
| Type | Conversions | % of Total | Cost Per |
|------|-------------|------------|----------|
| Click-through (CTA) | X | X% | €X.XX |
| View-through (VTA) | X | X% | €X.XX |
| **Total** | **X** | **100%** | **€X.XX** |

### VTA/CTA Ratio: X.XX
**Interpretation:** [Healthy / Low / High - explanation]

### Attribution Windows
| Window | Current | Recommendation |
|--------|---------|----------------|
| CTA | X days | [recommendation] |
| VTA | X day | [recommendation] |

### Landing Page Performance
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| LP View Rate | X% | >80% | [status] |
| Cost per LP View | €X.XX | - | - |
| LP → Conversion Rate | X% | varies by vertical | - |

### Cross-Platform Context (if applicable)
| Platform | CTA Conv | VTA Conv | Total CPA |
|----------|----------|----------|-----------|
| TikTok | X | X | €X.XX |
| Meta | X | X | €X.XX |
| Google | X | - | €X.XX |

### Key Findings
1. [Finding about VTA importance]
2. [Finding about platform comparison]
3. [Finding about optimization opportunity]

### Recommendations

**Attribution Setup:**
- [ ] Ensure VTA is enabled (1-day window)
- [ ] Align windows with other platforms for comparison
- [ ] [Specific recommendation]

**Optimization Actions:**
1. [Action based on VTA/CTA ratio]
2. [Action based on LP performance]
3. [Action for proving incremental value]

### Proving TikTok's Value
[Summary of how to demonstrate TikTok's contribution to overall marketing mix]
```

## Campaign Type Attribution Notes

| Campaign Type | Attribution Behavior |
|---------------|---------------------|
| **Standard In-Feed** | Default 7-day CTA + 1-day VTA |
| **Smart+ Campaigns** | Same windows; algorithm optimizes toward attributed events — VTA is a key signal |
| **Search Ads (Sep 2025)** | Primarily CTA (users have explicit intent); VTA is lower; attribution behaves more like Google Search |
| **TikTok Shop / GMV Max** | Extended 28-day CTA window; higher VTA due to product discovery behavior |
| **Spark Ads** | VTA particularly important — organic engagement drives delayed conversions |

**Search Ads tip:** For campaigns using TikTok Search Ads, expect a lower VTA/CTA ratio (0.1-0.4 is normal) since search-intent users click rather than passively view.

## Common Questions Answered

### "Should I include VTA in my ROAS calculation?"

**Yes, but communicate clearly:**
- Internal reporting: Include VTA (it's real impact)
- Finance reporting: May need CTA-only for conservative view
- Recommendation: Show both, explain the difference

### "Why does GA4 show fewer TikTok conversions?"

**GA4 is click-based only:**
- No view-through tracking in GA4
- May attribute to different channel (last-click)
- Cross-device tracking differs
- Expect 30-50% fewer in GA4 - this is normal

### "Is TikTok cannibalizing my Google conversions?"

**Possible, but more likely TikTok is ASSISTING:**
- TikTok creates awareness
- Users search brand on Google
- Google gets last-click credit
- Test: Pause TikTok, watch if Google brand conversions drop

### "What's a good VTA/CTA ratio?"

**Depends on campaign type:**
- Conversion campaigns: 0.5 - 1.5
- Traffic campaigns: 0.2 - 0.5
- Awareness campaigns: 1.0 - 3.0

## Monitoring Checklist

### Weekly Attribution Review
- [ ] VTA/CTA ratio by campaign
- [ ] LP view rate trend
- [ ] Cross-platform CPA comparison (aligned windows)
- [ ] Brand search volume correlation

### Monthly Deep Dive
- [ ] Full funnel attribution analysis
- [ ] Incrementality indicators (brand lift, search lift)
- [ ] Window setting optimization
- [ ] Platform role assessment

### Quarterly Strategy
- [ ] Incrementality test planning
- [ ] Attribution model refinement
- [ ] Cross-channel budget allocation review
- [ ] Stakeholder education on VTA importance

## MCP Tool Examples

Pull CTA vs VTA breakdowns:

```
# Get attribution split by campaign
tiktok_get_report(
  start_date="2026-03-01",
  end_date="2026-04-04",
  level="campaign",
  metrics=["cta_conversion", "vta_conversion", "cta_purchase", "vta_purchase",
           "total_landing_page_view", "spend", "impressions"]
)

# Get campaign list to understand campaign type and attribution context
tiktok_query(entity_type="campaigns")
```

---

*Based on 2025-2026 TikTok Ads attribution research. View-through attribution is not "soft" attribution - it captures TikTok's real impact on the discovery-to-conversion journey.*
