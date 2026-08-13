---
name: meta-creative-fatigue-analyzer
description: "This skill should be used when the user asks to \"detect creative fatigue\", \"analyze frequency vs CTR\", \"plan a creative refresh\", or mentions \"Meta ad fatigue\", \"declining CTR on Facebook\", or \"frequency thresholds\"."
---
# Meta Ads Creative Fatigue Analyzer

## Purpose

Detect and prevent creative fatigue on Meta Ads (Facebook/Instagram). Help advertisers understand when performance drops are due to creative fatigue vs other factors, and provide actionable recommendations for refresh timing and strategies.

## When to Use This Skill

Invoke when user mentions:
- **CTR questions:** "Is my CTR declining due to high frequency?"
- **Refresh timing:** "When should I refresh my Meta creatives?"
- **Frequency concerns:** "What frequency is too high for conversion campaigns?"
- **Audience vs creative:** "Should I expand my audience or refresh creatives?"
- **Prevention:** "How do I prevent Meta creative fatigue proactively?"
- **Diagnosis:** "Is my campaign fatigued or is there another issue?"

## Key Questions This Skill Answers

### Q1: Is my CTR dropping due to high frequency?

**Analysis Framework:**
1. Calculate CTR trend over time
2. Correlate with frequency increase
3. Check if CTR decline matches frequency curve

**Answer:** If frequency >3-4 for conversion campaigns AND CTR declining >10% week-over-week, creative fatigue is likely the cause.

### Q2: When should I refresh my creatives?

| Scenario | Refresh Every |
|----------|--------------|
| Standard budget, broad audience | 10-14 days |
| High budget, small audience | 5-7 days |
| High budget, large audience | 14-21 days |
| Low budget | 14-21 days |

### Q3: What frequency is too high?

| Campaign Type | Max Frequency/Week |
|--------------|-------------------|
| Conversion | 3-4/week |
| Consideration | 4-5/week |
| Awareness | 6-8/week |

### Q4: Should I expand audience or refresh creative?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUDIENCE vs CREATIVE DECISION                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    What's happening with your metrics?
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
FREQUENCY HIGH              FREQUENCY NORMAL            REACH EXHAUSTED
+ CTR DECLINING             + CTR DECLINING             (can't reach more)
        │                           │                           │
        ▼                           ▼                           ▼
REFRESH CREATIVE            TEST NEW AUDIENCE          EXPAND AUDIENCE
(Primary issue)             (Targeting issue)          (Audience issue)
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    │
                                    ▼
                          BOTH ISSUES?
                    Refresh creative + expand audience
```

## Fatigue Detection Algorithm

### Step 1: Pull Creative Performance Data

```
→ meta_get_creatives(account_id="act_XXXXXXXXX", scope="account", date_preset="last_14d", sort_by="spend")
```
This returns creative-level performance with text content. Identify ads with highest spend + longest runtime.

### Step 2: Pull Daily Frequency & CTR Trends

```
→ meta_get_insights(account_id="act_XXXXXXXXX", level="ad", date_preset="last_14d", time_increment="1", fields=["impressions", "reach", "frequency", "ctr", "cpm", "spend", "actions"])
```
Daily `time_increment="1"` is essential — plot CTR over time and correlate with frequency curve. This is the core fatigue detection signal.

### Step 3: Score Against Thresholds

| Signal | Warning | Critical |
|--------|---------|----------|
| **CTR decline** | >10-15% over 7 days | >20% over 7 days |
| **CPM rise** | >20-30% over 14 days | >40% over 14 days |
| **Frequency** | >3/week (conversion) | >5/week (any type) |
| **Days active** | >10 days | >14 days |
| **Platform alert** | "Creative Limited" | "Creative Fatigue" warning |

### Step 4: Check Creative Depth (Andromeda Threshold)

From the Step 1 results, count active creatives per campaign:

```
Count distinct ads with status=ACTIVE from meta_get_creatives output.
Group by campaign_id to get creatives-per-campaign.
```

| Creative Depth | Status | Action |
|---------------|--------|--------|
| **15+ active** | Healthy | Andromeda has enough material to rotate |
| **8-14 active** | Warning | Schedule 3-5 new creatives this week |
| **<8 active** | Critical | Fatigue will hit fast — add creatives immediately |

Low creative depth is the #1 predictor of premature fatigue under Andromeda. More variations = slower fatigue onset.

### Combined Signal (Critical)

When you see ALL THREE:
- Frequency high
- CTR declining
- CPM rising

**Action:** Refresh immediately - fatigue confirmed.

### Fatigue Timeline (Meta)

| Phase | Days | What's Happening | Action |
|-------|------|------------------|--------|
| **Learning** | 1-7 | Algorithm optimizing | Don't touch |
| **Peak** | 7-10 | Best performance window | Monitor closely |
| **Early decline** | 10-14 | Fatigue signs appearing | Prepare refresh |
| **Fatigue** | 14+ | Performance degrading | Refresh or kill |

### CTR & CPM Patterns

```
META ADS FATIGUE PATTERNS
──────────────────────────

CTR Pattern: Linear, gradual descent
├─ Daily decline after day 7: ~2%
├─ Predictable curve
└─ Watch for acceleration

CPM Pattern: Gradual incline
├─ Daily increase over days 10-14: +1-3%
├─ Slower than TikTok
└─ May spike suddenly at fatigue point
```

## Fatigue Detection Decision Tree

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IS MY META CREATIVE FATIGUED?                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                         Check Platform Alerts
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
           "CREATIVE LIMITED"               NO PLATFORM ALERT
           or "CREATIVE FATIGUE"                    │
                    │                               │
                    ▼                               ▼
           FATIGUE CONFIRMED              Check Frequency by Campaign Type
           Refresh immediately                      │
                                    ┌───────────────┼───────────────┐
                                    ▼               ▼               ▼
                               CONVERSION       CONSIDER.       AWARENESS
                               >3-4/week?       >4-5/week?      >6-8/week?
                                    │               │               │
                                    ▼               ▼               ▼
                               ┌────┴────┐     ┌────┴────┐     ┌────┴────┐
                               YES    NO       YES    NO       YES    NO
                                │      │        │      │        │      │
                                ▼      ▼        ▼      ▼        ▼      ▼
                            Check   Likely   Check   Likely   Check   Likely
                            CTR    not      CTR    not       CTR    not
                            trend  fatigue  trend  fatigue   trend  fatigue
```

## Refresh vs Kill Decision Framework

### Refresh Actions (Minor Tweaks)

When CTR declines 10-15% or CPM rises 15-20%:

1. **Change headline or primary text** - quick win
2. **Swap CTA button** - Learn More vs Shop Now
3. **Adjust image cropping** - new focal point
4. **Add text overlay** - reinforces message
5. **Change color scheme** - fresh look, same concept

### Kill Criteria (Pause Immediately)

- CTR falls >30% below campaign average
- CPA >2x baseline for 48 hours
- "Creative Limited" status in Ads Manager
- Negative feedback score increasing

## Prevention Strategies

### Creative Rotation Schedule

| Scenario | Refresh Every | Creatives Needed |
|----------|--------------|------------------|
| Standard budget, broad audience | 10-14 days | 4-6 per ad set |
| High budget, small audience | 5-7 days | 6-8 per ad set |
| High budget, large audience | 14-21 days | 4-6 per ad set |
| Low budget | 14-21 days | 3-4 per ad set |

### Content Mix for Longevity

```
META CREATIVE MIX (RECOMMENDED)
──────────────────────────────────

UGC Content: 40%
├─ Fatigues 10-15% slower than polished
├─ +3-4 days extended lifespan
├─ 17-18 day average lifespan
└─ Best for: Authenticity, social proof

Polished Content: 40%
├─ 10-12 day typical lifespan
├─ Brand consistency
├─ Professional look
└─ Best for: Brand campaigns, premium products

Dynamic Creative: 20%
├─ Auto-rotates elements (images, headlines, CTAs)
├─ Extends total lifespan
├─ Best when you have 3+ images/headlines/CTAs
└─ Use for testing and optimization
```

### Andromeda Engine & Minimum Creative Depth (2026)

Meta's Andromeda ad retrieval engine (rolled out 2025-2026) fundamentally changed how ads are matched to users. Creative quality is now the primary ranking signal — not audience targeting.

```
ANDROMEDA IMPLICATIONS FOR FATIGUE MANAGEMENT:
├── Creative quality drives matching — weak creative = less delivery
├── Minimum 15+ DISTINCT creative variations recommended per campaign
├── Fewer variations = faster fatigue and higher CPMs
├── Advantage+ Audience + high creative volume = best results
└── Andromeda rewards variety: different angles, formats, hooks

CREATIVE DEPTH TARGET:
├── Minimum: 8-10 active creatives per ad set
├── Recommended: 15+ distinct variations
├── Include: Different hooks, formats (video/static/carousel), angles
└── Refresh: Rotate 2-3 new creatives weekly on high-spend campaigns
```

### Variation Types to Prepare (4-6 per ad set)

1. **Different headline angles** (benefit, feature, social proof)
2. **Different imagery** (lifestyle, product, UGC)
3. **Different formats** (single image, carousel, video)
4. **Different CTAs** (Learn More, Shop Now, Get Started)

## Platform Signals (Meta-Specific)

### Understanding Meta's Alerts

| Signal | What It Means | Action |
|--------|--------------|--------|
| **Creative Limited** | Meta has flagged potential fatigue | Refresh immediately |
| **Creative Fatigue** | Cost per result doubled past benchmarks | Refresh or pause within 24-48h |
| **Learning Limited** | Not enough data to optimize | Different issue - consolidate or raise budget |

### Quality Ranking Components

Monitor these for early fatigue signals:
- **Quality Ranking:** Below/Average/Above average
- **Engagement Rate Ranking:** User interaction vs competitors
- **Conversion Rate Ranking:** Conversion performance vs competitors

## Recovery Playbook

### When Creative is Fatigued

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    META FATIGUE RECOVERY                                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                First: Try NEW CREATIVE
                (Most effective lever - 15-25% CTR lift)
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
            WORKS (+15-25% CTR)           DOESN'T WORK
                    │                               │
                    ▼                               ▼
             Continue with                Second: AUDIENCE EXPANSION
             new creative                 (Add 10-20% new audience)
                                                   │
                                    ┌───────────────┴───────────────┐
                                    │                               │
                                    ▼                               ▼
                            WORKS                           STILL STRUGGLING
                            (Extends 7-14 days)                    │
                                    │                               ▼
                                    ▼                  Third: COMBINED APPROACH
                             Scale up               New creative + 10-20% audience
                                                    + budget reallocation
```

### Budget Reallocation Strategy

**Meta-Specific Approach:**
- When creative ages >14 days: Shift 20-30% to new ad sets
- Reserve 20% for evergreen performers
- Test 10% on new creative concepts weekly

## Benchmarks

### Frequency Thresholds by Campaign Type

| Campaign Type | Safe | Warning | Critical |
|--------------|------|---------|----------|
| Conversion | <3/week | 3-4/week | >4/week |
| Consideration | <4/week | 4-5/week | >5/week |
| Awareness | <6/week | 6-8/week | >8/week |

### CTR & CPM Warning Signs

| Metric | Warning Threshold | Critical Threshold |
|--------|-------------------|-------------------|
| CTR decline | >10% week-over-week | >20% week-over-week |
| CPM rise | >20% over 14 days | >40% over 14 days |

### Creative Lifespan by Type

| Creative Type | Average Lifespan |
|--------------|------------------|
| Standard (polished) | 10-12 days |
| UGC | 17-18 days |
| High budget, small audience | 5-7 days |
| Low budget | 14-21 days |

## Differentiating Fatigue from Other Issues

### Not Fatigue - Different Problems

| Symptom | Likely Cause | Solution |
|---------|-------------|----------|
| "Learning Limited" | Budget too low or audience too narrow | Consolidate ad sets or raise budget |
| CTR normal but conversions down | Landing page or tracking issue | Check LP and pixel |
| Sudden performance drop (1 day) | External factor or algorithm change | Wait 24-48h before acting |
| High CPM but stable CTR | Competition increased | Accept or improve bid |

### Is It Fatigue? Checklist

- [ ] Frequency exceeds threshold for campaign type
- [ ] CTR declining over 7+ days (not just 1-2 days)
- [ ] CPM rising gradually (not sudden spike)
- [ ] Days active approaching or exceeding 14
- [ ] No recent significant changes to campaign
- [ ] No external factors (seasonality, competition)

## Output Template

When diagnosing Meta creative fatigue, provide:

```
## Meta Creative Fatigue Analysis

### Fatigue Score: X/10
(10 = severe fatigue)

**Components:**
- Frequency: [score] - [current] vs [threshold for campaign type]
- CTR trend: [score] - [% change over 7 days]
- CPM trend: [score] - [% change over 14 days]
- Days active: [score] - [days] vs 14 day threshold

### Status: [Healthy / Warning / Critical]

### Platform Signals
- Creative Limited: [Yes/No]
- Creative Fatigue Warning: [Yes/No]
- Learning Limited: [Yes/No - if yes, different issue]

### Diagnosis
- Fatigue detected: [Yes/No/Likely]
- Primary indicator: [which metric is driving diagnosis]
- Days until refresh needed: [estimate]

### Recommendations

**Refresh or Continue:** [decision]

**If Refresh:**
1. [Specific action 1]
2. [Specific action 2]

**Creative Suggestions:**
- [Based on current creative type]

**Audience Recommendation:**
- [Expand/Maintain/Test new]

**Testing Ideas:**
- [A/B test suggestion]
```

## Monitoring Checklist

### Daily Checks (High-Spend Campaigns)
- [ ] Frequency by ad set
- [ ] CTR trend (last 3 days)
- [ ] CPM trend (last 3 days)
- [ ] Platform alerts (Creative Limited, etc.)

### Weekly Checks
- [ ] Calculate fatigue score per creative
- [ ] Identify refresh candidates
- [ ] Review creative library depth (need 4-6)
- [ ] Plan next week's refreshes
- [ ] Compare UGC vs polished performance

### Bi-Weekly Review
- [ ] Average creative lifespan analysis
- [ ] Frequency threshold validation
- [ ] Budget allocation vs creative performance
- [ ] Learnings documentation

---

*Sources: Alison.ai "Creative Fatigue Report Q3 2025" (Sep 2025), Sovran Meta Ads benchmarks (Q1 2026), Meta Business Help Center. Meta creative fatigue is more gradual than TikTok — plan for 2-week refresh cycles with monitoring. With Andromeda, maintaining 15+ creative variations is the most effective fatigue prevention strategy.*
