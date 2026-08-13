---
name: tiktok-app-performance-tracker
description: "This skill should be used when the user asks to \"optimize TikTok app install campaigns\", \"reconcile TikTok MMP data\", \"fix TikTok SKAN attribution\", or mentions \"TikTok cost per install\", \"TikTok AppsFlyer numbers don't match\", or \"TikTok app event tracking\". Do NOT use for: TikTok creative fatigue (use tiktok-creative-fatigue-tracker), TikTok video performance (use tiktok-video-performance-analyzer), or TikTok benchmark lookups (use tiktok-benchmark-database)."
---
# TikTok App Performance Tracker

## Purpose

Track, analyze, and optimize TikTok app install campaigns. This skill helps advertisers understand app event metrics, reconcile TikTok data with MMP (Mobile Measurement Partner) data, and navigate iOS 14+ SKAN attribution challenges.

## The Critical Landscape: TikTok App Advertising

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TIKTOK APP ATTRIBUTION ECOSYSTEM                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ANDROID (Clear attribution)          iOS (SKAN-based)                      │
│  ─────────────────────────            ────────────────                      │
│                                                                              │
│  TikTok tracking:                     TikTok tracking:                      │
│  ├─ Device-level attribution         ├─ SKAdNetwork only (post iOS 14.5)   │
│  ├─ Real-time data                   ├─ 24-48 hour delay                   │
│  └─ Full event stream                └─ Limited conversion values          │
│                                                                              │
│  MMP integration:                     MMP integration:                      │
│  ├─ Click + view attribution         ├─ Probabilistic modeling             │
│  ├─ Full user journey                ├─ Limited post-install events        │
│  └─ 100% match expected              └─ 40-60% typical match rate          │
│                                                                              │
│  Discrepancy: 5-15%                   Discrepancy: 20-50%                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## When to Use This Skill

Invoke when user mentions:
- **Install tracking:** "How many app installs am I getting?"
- **CPI analysis:** "What is my cost per install?"
- **MMP discrepancies:** "Why don't TikTok and AppsFlyer match?"
- **iOS tracking:** "How many iOS installs via SKAN?"
- **In-app events:** "How many registrations after install?"
- **Retention:** "What is my D2 retention?"
- **Gaming metrics:** "How many users complete the tutorial?"
- **Subscription apps:** "What is my cost per trial?"

## Key Metrics Explained

### App Install Funnel

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      APP INSTALL FUNNEL & METRICS                            │
└─────────────────────────────────────────────────────────────────────────────┘

  IMPRESSIONS → CLICKS → INSTALLS → REGISTRATION → IN-APP EVENTS → PURCHASE
       │           │          │            │               │            │
       ▼           ▼          ▼            ▼               ▼            ▼
     [CPM]      [CPC]      [CPI]       [CPR]         [CPA per        [ROAS]
                           [CVR]    [Install-to-     event]
                                    Reg Rate]

METRICS HIERARCHY:
─────────────────

Level 1: Acquisition
├─ app_install: Total attributed installs
├─ real_time_app_install: Today's installs (updates hourly)
├─ cost_per_install: Spend / installs
└─ install_rate: Installs / clicks × 100

Level 2: Activation
├─ registration: Sign-ups post-install
├─ install_to_registration_rate: Registrations / installs × 100
├─ complete_tutorial: Tutorial completions (gaming)
└─ start_trial: Trial starts (subscription apps)

Level 3: Engagement
├─ view_content: Product/content views
├─ add_to_cart: Cart additions
├─ add_to_wishlist: Wishlist additions
├─ achieve_level: Gaming progression
└─ day_2_retention: D2 return rate

Level 4: Monetization
├─ purchase: In-app purchases
├─ total_purchase_value: Revenue from purchases
├─ subscribe: Paid subscriptions
├─ spend_credit: In-app spending (gaming)
└─ checkout: Checkout completions
```

### SKAN (SKAdNetwork) Metrics - iOS Only

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SKAN ATTRIBUTION EXPLAINED                           │
└─────────────────────────────────────────────────────────────────────────────┘

WHAT IS SKAN?
─────────────
Apple's privacy-preserving attribution framework (standard since iOS 14.5, 2021).
NO device-level tracking. NO real-time data. Limited conversion values.

SKAN METRICS AVAILABLE:
───────────────────────
├─ skan_app_install: iOS installs via SKAdNetwork
├─ skan_conversion: Attributed conversions
├─ skan_purchase: Purchases (delayed)
├─ skan_registration: Registrations (delayed)
├─ skan_result: Combined results
└─ skan_cost_per_result: iOS CPA

KEY LIMITATIONS:
────────────────
┌──────────────────────────────────────────────────────────────────┐
│ Limitation              │ Impact                                 │
├─────────────────────────┼────────────────────────────────────────┤
│ 24-48 hour delay        │ No real-time optimization              │
│ Conversion values (0-63)│ Only 64 possible conversion buckets    │
│ One postback per user   │ Limited post-install event tracking    │
│ No view-through attr.   │ VTA not supported in SKAN              │
│ Campaign cap (100)      │ Max 100 campaigns per account          │
└──────────────────────────────────────────────────────────────────┘

SKAN DATA TIMELINE:
───────────────────
Day 0: User installs app (SKAN timer starts)
Day 0-24h: Conversion value can be updated
Day 1-2: Timer expires, postback sent to ad network
Day 2-3: Data appears in TikTok (24-48h delay after postback)

Total latency: 2-4 days from install to data visibility
```

## CPI Benchmarks by Vertical

| Vertical | Android CPI | iOS CPI (SKAN) | Install-to-Reg Rate |
|----------|-------------|----------------|---------------------|
| **Gaming - Casual** | €0.50 - €1.50 | €1.00 - €3.00 | 25-40% |
| **Gaming - Midcore** | €1.50 - €4.00 | €3.00 - €8.00 | 15-25% |
| **Gaming - Hardcore** | €3.00 - €10.00 | €6.00 - €15.00 | 10-20% |
| **E-commerce** | €0.80 - €2.50 | €1.50 - €4.00 | 30-50% |
| **Fintech** | €2.00 - €6.00 | €4.00 - €12.00 | 20-35% |
| **Food Delivery** | €1.00 - €3.00 | €2.00 - €5.00 | 40-60% |
| **Dating** | €1.50 - €4.00 | €3.00 - €7.00 | 35-50% |
| **Streaming** | €0.80 - €2.00 | €1.50 - €4.00 | 40-55% |
| **Utilities** | €0.30 - €1.00 | €0.60 - €2.00 | 45-65% |

**Regional Multipliers:**
- Western Europe: 1.0x (baseline)
- North America: 1.2x - 1.5x
- UK: 1.1x - 1.3x
- Eastern Europe: 0.6x - 0.8x
- Southeast Asia: 0.3x - 0.5x
- LATAM: 0.4x - 0.6x

## MMP Integration & Discrepancy Troubleshooting

### Supported MMPs

| MMP | Integration | Typical Match Rate |
|-----|-------------|-------------------|
| **AppsFlyer** | Full (OneLink) | 85-95% Android, 50-70% iOS |
| **Adjust** | Full | 85-95% Android, 50-70% iOS |
| **Singular** | Full | 85-95% Android, 50-70% iOS |
| **Branch** | Full | 80-90% Android, 45-65% iOS |
| **Kochava** | Full | 80-90% Android, 45-65% iOS |

### Why TikTok and MMP Data Don't Match

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DISCREPANCY DIAGNOSIS FLOWCHART                           │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    "TikTok shows more installs than MMP"
                                    │
                                    ▼
                         Check time zone settings
                                    │
            ┌───────────────────────┼───────────────────────────┐
            │                       │                           │
            ▼                       ▼                           ▼
      DIFFERENT TZ             SAME TZ                    NOT THE ISSUE
    (Common cause!)        Check attribution window              │
            │                       │                           ▼
            ▼                       ▼                  Check iOS vs Android
      Align to UTC         Compare windows                      │
      in both systems              │               ┌────────────┼────────────┐
                                   │               │                         │
                    ┌──────────────┼──────────────┐│                         │
                    │              │              ││                         │
                    ▼              ▼              ▼▼                         ▼
             TT: 7d click     TT: 1d VTA    MMP has         iOS HEAVY        ANDROID
             MMP: 7d click    MMP: 1d VTA   different       (SKAN issue)     (Should match)
                    │              │        windows                │              │
                    ▼              ▼            │                  ▼              ▼
             Should match    Should match   Align!          Expected gap     Debug:
             (debug further) (debug further)                (20-50% normal)  - Click tracking
                                                                             - Deep links
                                                                             - Postback delays
```

### Common Discrepancy Causes & Solutions

| Cause | Impact | Solution |
|-------|--------|----------|
| **Time zone mismatch** | 5-20% variance | Align both to UTC or same TZ |
| **Attribution window** | 10-30% variance | Match windows in both systems |
| **VTA attribution** | TikTok higher | MMP may not track all VTA |
| **SKAN delays** | iOS 24-48h lag | Compare same date range after lag |
| **Click URL issues** | Missing installs in MMP | Test deep link setup |
| **Postback failures** | MMP missing events | Check MMP postback logs |
| **Organic vs paid** | Attribution overlap | Review MMP deduplication rules |
| **Re-engagement** | Counted differently | Align re-attribution windows |

### Acceptable Discrepancy Ranges

| Platform | Acceptable | Investigate | Critical |
|----------|------------|-------------|----------|
| Android | <10% | 10-20% | >20% |
| iOS (SKAN) | <30% | 30-50% | >50% |

## iOS SKAN Best Practices

### SKAN Optimization Strategy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      iOS CAMPAIGN OPTIMIZATION                               │
└─────────────────────────────────────────────────────────────────────────────┘

CONVERSION VALUE SCHEMA (64 buckets: 0-63)
──────────────────────────────────────────

For E-commerce/Revenue Apps:
┌────────────────────────────────────────────────┐
│ Value │ Meaning                                │
├───────┼────────────────────────────────────────┤
│ 0     │ Install only (no post-install event)  │
│ 1-10  │ Registration / Sign-up                │
│ 11-20 │ Add to Cart / Content View            │
│ 21-40 │ Purchase (€0-€50)                     │
│ 41-55 │ Purchase (€50-€200)                   │
│ 56-63 │ High-value purchase (€200+)           │
└────────────────────────────────────────────────┘

For Gaming Apps:
┌────────────────────────────────────────────────┐
│ Value │ Meaning                                │
├───────┼────────────────────────────────────────┤
│ 0     │ Install only                          │
│ 1-5   │ Tutorial start                        │
│ 6-15  │ Tutorial complete                     │
│ 16-30 │ Level 5 achieved                      │
│ 31-45 │ First purchase (IAP)                  │
│ 46-63 │ High-value IAP / Subscription         │
└────────────────────────────────────────────────┘

For Subscription Apps:
┌────────────────────────────────────────────────┐
│ Value │ Meaning                                │
├───────┼────────────────────────────────────────┤
│ 0     │ Install only                          │
│ 1-10  │ Registration                          │
│ 11-25 │ Trial started                         │
│ 26-40 │ Paywall viewed                        │
│ 41-55 │ Trial converted (monthly)             │
│ 56-63 │ Trial converted (annual)              │
└────────────────────────────────────────────────┘
```

### iOS Campaign Setup Recommendations

1. **Consolidate campaigns** - Max 100 SKAN campaigns per account
2. **Higher budgets** - Minimum €50/day per ad group for learning
3. **Broader targeting** - SKAN works better with larger audiences
4. **Patience with data** - Wait 3-4 days before optimization decisions
5. **Use SKAN + MMP together** - SKAN for attribution, MMP for incrementality

## In-App Event Tracking Setup

### Standard Events by App Type

```
E-COMMERCE APP                      GAMING APP
──────────────                      ──────────
□ app_install                       □ app_install
□ registration                      □ registration
□ view_content                      □ complete_tutorial
□ add_to_cart                       □ achieve_level
□ add_to_wishlist                   □ spend_credit (IAP)
□ checkout                          □ subscribe
□ purchase                          □ purchase (IAP)
□ add_payment_info                  □ day_2_retention

SUBSCRIPTION APP                    FINTECH APP
────────────────                    ───────────
□ app_install                       □ app_install
□ registration                      □ registration
□ start_trial                       □ view_content
□ subscribe                         □ add_payment_info
□ purchase                          □ purchase (deposit)
□ day_2_retention                   □ checkout (KYC complete)
                                    □ subscribe (premium)
```

### Event Value Tracking Best Practices

| Event | Track Value? | Why |
|-------|--------------|-----|
| purchase | YES | ROAS calculation |
| subscribe | YES | LTV prediction |
| add_to_cart | Optional | Funnel analysis |
| spend_credit | YES | Gaming revenue |
| registration | No | Boolean event |
| view_content | No | Volume metric |

## Campaign Optimization Framework

### Learning Phase for App Campaigns

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      APP CAMPAIGN LEARNING PHASE                             │
└─────────────────────────────────────────────────────────────────────────────┘

REQUIREMENT: 50 conversions in 7 days per ad group

For app installs (CPI €1.50):
├─ Minimum budget: 50 × €1.50 / 7 = €10.71/day
├─ Recommended: €50/day (safety margin)
└─ Conservative: €30-40/day

For in-app events (CPA €15):
├─ Minimum budget: 50 × €15 / 7 = €107/day
├─ Recommended: €150/day
└─ Consider: Start with install optimization, switch after data

LEARNING PHASE STATUS:
─────────────────────
✅ Active: Getting conversions, still learning
⚠️ Limited: Not enough conversions (<50/week)
❌ Not Learning: Stuck - change targeting or bid
✅ Completed: Ready to scale
```

### Campaign Type Selection

| Campaign Type | Best For | Notes |
|---------------|----------|-------|
| **Standard App Install** | Testing, control | Manual targeting and bidding |
| **Smart+ App** | Scaling, automation | TikTok's automated campaign (like Meta Advantage+); algorithm handles audience + creative rotation; needs 5+ ad variants |
| **Value-Based Optimization** | ROAS-focused | Requires in-app purchase events |

**Smart+ App campaigns** (part of TikTok's Smart+ suite, expanded Jan 2026) are recommended once you have 50+ installs/week of history. They reduce manual audience management and typically improve CPI by 10-20% after the learning phase.

### Bid Strategy Selection

| Objective | Strategy | When to Use |
|-----------|----------|-------------|
| **Maximize installs** | Lowest Cost (auto) | Starting out, broad testing |
| **Target CPI** | Cost Cap | Know your target CPI, want control |
| **Value optimization** | Value-Based | Have purchase data, optimize ROAS |
| **iOS campaigns** | Lowest Cost | SKAN works best with volume |
| **Smart+ App** | Auto (algorithm-managed) | Let TikTok optimize bids automatically |

### Scaling Decision Tree

```
                         Is CPI below target?
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
            YES             MARGINAL              NO
         (>20% below)       (±10%)            (>10% above)
              │                 │                 │
              ▼                 ▼                 ▼
        Scale up           Hold steady      Troubleshoot:
        (+20-30% budget)   Monitor 3-5 days ├─ Creative fatigue?
              │                 │            ├─ Audience saturation?
              ▼                 ▼            ├─ Competition?
        Check install-     Check retention  └─ Seasonality?
        to-registration         │
        rate                    │
              │                 │
              ▼                 ▼
        Good (>30%)?       Good (>20% D2)?
              │                 │
        YES → Continue     YES → Continue optimizing
        NO → Check LP/app  NO → Check app quality/UX
```

## Output Template

When analyzing TikTok app performance, provide:

```
## TikTok App Performance Analysis

### Campaign Overview
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Total Installs | X | - | - |
| CPI | €X.XX | €X.XX (vertical avg) | [✅/⚠️/❌] |
| Install Rate | X% | >2% | [status] |
| Real-time Installs (today) | X | - | - |

### Funnel Analysis
| Stage | Count | Rate | Benchmark |
|-------|-------|------|-----------|
| Installs | X | - | - |
| Registrations | X | X% of installs | >30% |
| Add to Cart | X | X% of registrations | >20% |
| Purchase | X | X% of installs | >5% |

### iOS (SKAN) Status
| Metric | Value | Note |
|--------|-------|------|
| SKAN Installs | X | Delayed 24-48h |
| SKAN CPA | €X.XX | - |
| Data Freshness | X days ago | - |

### MMP Reconciliation (if applicable)
| Source | Installs | Variance | Status |
|--------|----------|----------|--------|
| TikTok | X | - | - |
| MMP (AppsFlyer/Adjust) | X | X% | [Acceptable/Investigate] |

**Variance Analysis:**
- [Explanation of any discrepancy]
- [Root cause if identified]

### Recommendations

**Immediate Actions:**
1. [Action based on data]
2. [Action based on benchmarks]

**Optimization Opportunities:**
- [Creative refresh if needed]
- [Targeting adjustments]
- [Bid strategy changes]

### Learning Phase Status
- Status: [Active/Limited/Completed]
- Conversions this week: X/50 required
- Budget recommendation: €X/day
```

## Monitoring Checklist

### Daily Checks
- [ ] Real-time installs trending vs yesterday
- [ ] CPI within acceptable range
- [ ] Install rate stable (>2%)
- [ ] SKAN data arriving (iOS)
- [ ] MMP postback status (if applicable)

### Weekly Checks
- [ ] Install-to-registration rate
- [ ] D2 retention rate
- [ ] Purchase/revenue metrics
- [ ] TikTok vs MMP reconciliation
- [ ] Learning phase status per ad group
- [ ] SKAN conversion value distribution

### Monthly Review
- [ ] CPI trends by vertical/geo
- [ ] LTV:CAC ratio analysis
- [ ] iOS vs Android performance split
- [ ] Creative performance by install rate
- [ ] Seasonal patterns identification

## MCP Tool Examples

Pull app install and funnel metrics:

```
# Get install counts and funnel events
tiktok_get_report(
  start_date="2026-03-28",
  end_date="2026-04-04",
  level="campaign",
  metrics=["app_install", "real_time_app_install", "cost_per_install",
           "registration", "purchase", "spend",
           "skan_app_install", "skan_cost_per_result"]
)

# List campaigns to identify app install campaigns
tiktok_query(entity_type="campaigns")
```

---

*Based on 2025-2026 TikTok Ads and MMP integration research. iOS attribution via SKAN requires patience - data delays are normal, not errors.*
