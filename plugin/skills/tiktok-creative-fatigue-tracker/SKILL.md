---
name: tiktok-creative-fatigue-tracker
description: "This skill should be used when the user asks to \"detect TikTok creative fatigue\", \"refresh TikTok ad creatives\", \"plan TikTok creative rotation\", or mentions \"TikTok CTR declining\", \"TikTok CPM spiking\", or \"how many creatives for TikTok\". Do NOT use for: TikTok video hook/length optimization (use tiktok-video-performance-analyzer), TikTok benchmark lookups (use tiktok-benchmark-database), or TikTok learning phase questions (use tiktok-learning-phase-tracker)."
---
# TikTok Creative Fatigue Tracker

## Purpose

Detect and prevent creative fatigue on TikTok Ads. TikTok's novelty-driven algorithm causes ads to fatigue **4x faster** than Meta (3-7 days vs 14 days). This skill helps identify early warning signs and provides actionable refresh strategies.

## The Critical Difference: TikTok vs Meta

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     CREATIVE FATIGUE: TIKTOK vs META                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  TIKTOK ADS                              META ADS                            │
│  ──────────                              ─────────                           │
│                                                                              │
│  Fatigue onset: ~3-7 days                Fatigue onset: ~14 days            │
│  CTR decline: Cliff (-20-25%/day)        CTR decline: Gradual (-2%/day)     │
│  CPM rise: Sudden (+5-10%/day)           CPM rise: Slow (+1-3%/day)         │
│                                                                              │
│  ┌──────────────────────┐                ┌──────────────────────┐           │
│  │ DAY 1-2: Learning    │                │ DAY 1-7: Learning    │           │
│  │ DAY 2-4: Peak        │                │ DAY 7-10: Peak       │           │
│  │ DAY 4-7: Decline     │                │ DAY 10-14: Decline   │           │
│  │ DAY 7+: Severe       │                │ DAY 14+: Fatigue     │           │
│  └──────────────────────┘                └──────────────────────┘           │
│                                                                              │
│  Refresh: Every 3-5 days                 Refresh: Every 7-14 days           │
│  Creatives needed: 8-12 per campaign     Creatives needed: 4-6 per ad set   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## When to Use This Skill

Invoke when user mentions:
- **Fatigue questions:** "Is my TikTok ad fatiguing?"
- **Timing questions:** "When should I refresh my TikTok creatives?"
- **Performance drops:** "Why did my TikTok CPM spike suddenly?"
- **Creative planning:** "How many creatives do I need for TikTok?"
- **Prevention:** "How do I prevent TikTok creative fatigue?"

## Fatigue Detection Algorithm

### Step 1: Pull Ad-Level Performance Trends

```
→ tiktok_get_report(start_date="YYYY-MM-DD", end_date="YYYY-MM-DD", level="ad", metrics=["ctr", "cpm", "frequency", "spend", "impressions", "clicks"])
```
Pull 14 days of daily data. TikTok fatigue is fast — look for cliff patterns starting day 4-5.

### Step 2: Identify Active Campaigns & Creatives

```
→ tiktok_query(entity_type="campaigns")
```
Cross-reference campaign launch dates with performance curves. Creatives older than 5 days are fatigue candidates.

### Step 3: Score Against Thresholds

| Signal | Warning | Critical | Severity |
|--------|---------|----------|----------|
| **CTR decline** | >15% decline within 3 days | >30% decline within 3 days | Warning → Critical |
| **CPM spike** | >20% increase over baseline | >40% increase over baseline | Warning → Critical |
| **CPA rise** | >20% increase (no budget/audience change) | >50% increase | Warning → Critical |
| **Frequency** | >4/week prospecting | >2/day OR >6-10/week | Warning → Urgent |
| **Days active** | >5 days | >7 days | Warning → Critical |

### Fatigue Detection Decision Tree

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IS MY TIKTOK CREATIVE FATIGUED?                           │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                         Check Frequency
                                    │
            ┌───────────────────────┼───────────────────────────┐
            │                       │                           │
            ▼                       ▼                           ▼
    FREQUENCY LOW            FREQUENCY MODERATE          FREQUENCY HIGH
    (<4/week)                (4-6/week)                  (>6/week or >2/day)
            │                       │                           │
            ▼                       ▼                           ▼
    Check CTR trend          Check CTR trend             FATIGUE LIKELY
            │                       │                    Confirm with CTR
            │               ┌───────┴───────┐                   │
            │               ▼               ▼                   │
            │         CTR STABLE      CTR DECLINING             │
            │         (±10%)          (>15% in 3 days)          │
            │               │               │                   │
            │               ▼               ▼                   │
            │         Not fatigued    Check CPM trend           │
            │         (rare for TikTok)     │                   │
            │                       ┌───────┴───────┐           │
            │                       ▼               ▼           │
            │                   CPM STABLE     CPM RISING       │
            │                       │          (>20%)           │
            │                       ▼               ▼           │
            │                   Audience      FATIGUE           │
            │                   issue         CONFIRMED ────────┘
            │                                      │
            └──────────────────────────────────────┘
                                    │
                                    ▼
                         ACTION: REFRESH OR KILL
```

### Fatigue Timeline

| Phase | Days | What's Happening | Action |
|-------|------|------------------|--------|
| **Learning** | 1-2 | Metrics stabilizing | Don't touch |
| **Peak** | 2-4 | Best performance window | Monitor daily |
| **Early decline** | 4-5 | Fatigue signs appearing | Prepare refresh |
| **Fatigue** | 5-7 | Performance degrading | Refresh immediately |
| **Severe** | 7+ | Significant fatigue | Kill and replace |

## Refresh vs Kill Decision Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    REFRESH vs KILL DECISION                                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                    How severe is the decline?
                                    │
            ┌───────────────────────┼───────────────────────────┐
            │                       │                           │
            ▼                       ▼                           ▼
      MODERATE                  SEVERE                    CRITICAL
   CTR -10-15%               CTR -15-30%                CTR >30% below
   CPM +15-20%               CPM +20-40%                average for 48h
            │                       │                           │
            ▼                       ▼                           ▼
       REFRESH                   TEST                        KILL
   Minor tweaks:              New version:               Pause immediately
   - New hook                 - Different angle          Do not revive
   - Different music          - New format               Replace completely
   - Add text overlay         - UGC version
   - Change thumbnail
```

### Refresh Actions (Minor Tweaks)

When CTR declines 10-15% or CPM rises 15-20%:

1. **New hook** (first 2 seconds) - highest impact
2. **Different music/sound** - TikTok-specific lever
3. **Add text overlay** - reinforces message
4. **Change thumbnail** - improves click-through
5. **Speed up pacing** - maintains attention

### Kill Criteria (Pause Immediately)

- CTR falls >30% below campaign average
- CPA >2x baseline for 48 hours
- Negative comments/feedback rising
- Policy violation risk

**Do NOT attempt to revive severely fatigued creative.**

## Prevention Strategies

### Creative Rotation Schedule

| Scenario | Refresh Every | Creatives Needed |
|----------|--------------|------------------|
| Standard | 5-7 days | 8-12 per campaign |
| High budget | 3-4 days | 12-15 per campaign |
| Exploration phase | Weekly (1-2 assets) | 8-10 active |
| Scaling phase | Biweekly (2-3 assets) | 10-12 active |

### Content Mix for Longevity

```
TIKTOK CREATIVE MIX (RECOMMENDED)
──────────────────────────────────

UGC Content: 60-70%
├─ Fatigues 20-30% slower than polished
├─ +1-2 days extended lifespan
├─ Best for: Prospecting, awareness, Gen Z
└─ Use: Creator partnerships, customer testimonials

Polished Content: 20-30%
├─ 2-3 day typical lifespan
├─ Use sparingly
├─ Best for: Brand launches, premium positioning
└─ Rotate most frequently

Lo-fi/Native Content: 10%
├─ Looks organic (not "ad-like")
├─ Often best CTR
├─ Best for: Authenticity, scroll-stopping
└─ POV videos, behind-the-scenes
```

### Variation Types to Prepare (8-12 per campaign)

1. **Different hooks** (question, shocking stat, POV, pattern interrupt)
2. **Different creators/faces** (diversity extends reach)
3. **Different video lengths** (6s, 15s, 30s — max 60s for In-Feed)
4. **Different music/sounds** (trending vs custom)
5. **Different editing styles** (fast cuts, continuous, split screen)
6. **Spark Ads vs regular ads** (organic boost vs controlled)

### Smart+ Campaigns & Fatigue

**Smart+ Campaigns** (TikTok's automated type, like Meta Advantage+) handle some rotation automatically — but fatigue still occurs:

| Smart+ Type | Fatigue Behavior | Recommendation |
|-------------|-----------------|----------------|
| Smart+ Web | Auto-rotates best creative | Still refresh every 7-10 days |
| Smart+ App | Algorithm-driven | Supply 5+ variants at launch |
| Smart+ Lead Gen | Auto-optimize | Monitor CTR for cliff signals |
| GMV Max (Shop) | Auto for Shop SKUs | Refresh product visuals |

**Note:** Smart+ reduces manual rotation work but doesn't eliminate fatigue. Provide a large creative pool (8-12 assets) at campaign launch so the algorithm has material to rotate.

### Search Ads (Launched Sep 2025)

Search Ads run in TikTok's search results (keyword-targeted). Fatigue pattern differs:
- **Lower fatigue rate** than In-Feed (users have active intent)
- Recommended 20-30% of total TikTok budget
- Creative still benefits from refreshes every 14-21 days (closer to Google Search cadence)

### Frequency Caps

| Campaign Type | Recommended Cap | Action |
|--------------|-----------------|--------|
| Prospecting | 4-5 impressions/user/week | Use TikTok automated rules |
| Retargeting | 6-8 impressions/user/week | Monitor daily |
| Awareness | Can go higher | Watch for CTR decline |

## Recovery Playbook

### When Creative is Fatigued

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TIKTOK FATIGUE RECOVERY                                   │
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
             Continue with                Second: Try NEW AUDIENCE
             new creative                 (10-20% expansion)
                                                   │
                                    ┌───────────────┴───────────────┐
                                    │                               │
                                    ▼                               ▼
                            WORKS                           STILL STRUGGLING
                            (Extends 3-5 days)                     │
                                    │                               ▼
                                    ▼                  Third: COMBINED APPROACH
                             Scale up               New creative + new audience
                                                    + budget reallocation
```

### Budget Reallocation Strategy

**TikTok-Specific Approach:**
- Reallocate 30-50% weekly to new creative experiments
- Reserve 20% for proven high performers (evergreen reserve)
- Rotate aggressively - TikTok rewards freshness

### Recovery Impact by Tactic

| Tactic | Expected Impact | Best Use Case |
|--------|-----------------|---------------|
| New creative | +15-25% CTR lift immediately | Always try first |
| Audience expansion | Extends reach 3-5 days | When creative is strong |
| Combined approach | Best for scaling | Broad budgets |
| Budget reallocation | Sustained performance | Ongoing optimization |

## Benchmarks

### Healthy Metrics

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| CTR | >1.5% | 1.0-1.5% declining | <1.0% |
| CPM | Platform avg for vertical | +10-20% above baseline | +30%+ above baseline |
| Frequency | <4/week prospecting | 4-6/week | >6/week |
| CPA | At or below target | +10-20% above target | +50%+ above target |

### Platform Comparison

| Metric | TikTok | Meta |
|--------|--------|------|
| Fatigue onset | 3-7 days | 14 days |
| CTR pattern | Convex (plateau then cliff) | Linear (gradual descent) |
| CTR daily decline after peak | 20-25% | ~2% |
| CPM daily increase post-fatigue | +5-10% | +1-3% |
| Creatives needed | 8-12 | 4-6 |

## Output Template

When diagnosing TikTok creative fatigue, provide:

```
## TikTok Creative Fatigue Analysis

### Fatigue Score: X/10
(10 = severe fatigue)

**Components:**
- CTR trend: [score] - [detail]
- CPM trend: [score] - [detail]
- Frequency: [score] - [detail]
- Days active: [score] - [detail]

### Status: [Healthy / Warning / Critical]

### Current Metrics vs Benchmarks
| Metric | Current | Benchmark | Status |
|--------|---------|-----------|--------|
| CTR | X% | >1.5% | [status] |
| CPM | $X | $X avg | [status] |
| Frequency | X/week | <4/week | [status] |
| Days active | X days | <5 days | [status] |

### Recommendation: [Refresh / Kill / Continue]

**Immediate Actions:**
1. [Action 1]
2. [Action 2]

**Creative Suggestions:**
- [Specific refresh idea based on analysis]
- [Alternative approach]

**Rotation Schedule:**
- Next refresh: [date/timing]
- Creatives needed in pipeline: [number]
```

## Monitoring Checklist

### Daily Checks
- [ ] CTR trend (last 3 days)
- [ ] CPM trend (last 3 days)
- [ ] Frequency by creative
- [ ] Days since creative launch
- [ ] CPA trend

### Weekly Checks
- [ ] Calculate fatigue score per creative
- [ ] Identify refresh candidates
- [ ] Review creative library depth (need 8-12)
- [ ] Plan next week's refreshes
- [ ] Analyze top/bottom performers

### Monthly Review
- [ ] Average creative lifespan analysis
- [ ] UGC vs polished performance comparison
- [ ] Rotation cadence effectiveness
- [ ] Budget allocation vs creative performance

---

*Sources: TikTok Creative Best Practices Guide 2025, Lebesgue "TikTok Ads Benchmarks" (Mar 2026), Alison.ai "Creative Fatigue Report Q3 2025" (Sep 2025). TikTok creative fatigue is fundamentally different from other platforms — plan for 4x faster refresh cycles.*
