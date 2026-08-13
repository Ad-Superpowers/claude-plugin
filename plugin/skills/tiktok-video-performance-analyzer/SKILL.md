---
name: tiktok-video-performance-analyzer
description: "This skill should be used when the user asks to \"improve TikTok video hooks\", \"optimize TikTok video length\", \"analyze TikTok video completion rates\", or mentions \"TikTok first 2 seconds\", \"UGC vs polished TikTok ads\", or \"when to use Spark Ads\". Do NOT use for: TikTok creative fatigue detection (use tiktok-creative-fatigue-tracker), TikTok benchmark lookups (use tiktok-benchmark-database), or TikTok attribution questions (use tiktok-attribution-guide)."
---
# TikTok Video Performance Analyzer

## Purpose

Analyze TikTok video ad performance with a focus on hook effectiveness (first 2 seconds), video length optimization, and engagement patterns. On TikTok, **70% of video retention is decided within the first 2 seconds** - making hook analysis critical for success.

## The Critical 2-Second Rule

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE 2-SECOND RULE ON TIKTOK                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  FIRST 2 SECONDS = 70% OF RETENTION DECISION                                 │
│                                                                              │
│  User Behavior:                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │ 0s         1s         2s         3s         4s         5s          │    │
│  │ │──────────│──────────│──────────│──────────│──────────│          │    │
│  │     ↑              ↑                                               │    │
│  │     │              │                                               │    │
│  │   SCROLL       DECISION                                            │    │
│  │   STOPS        POINT                                               │    │
│  │                "Watch or scroll?"                                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  If hook fails → 50%+ immediate scroll-away                                  │
│  If hook works → 3-5x more likely to complete video                         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## When to Use This Skill

Invoke when user mentions:
- **Hook optimization:** "How do I improve my TikTok video hook?"
- **Length questions:** "What's the optimal video length for TikTok?"
- **Completion issues:** "Why is my video completion rate low?"
- **Content strategy:** "Should I use UGC or polished content?"
- **Ad format:** "When should I use Spark Ads vs regular ads?"

## Hook Analysis Framework

### Effective Hook Types

| Hook Type | Description | Example | Best For |
|-----------|-------------|---------|----------|
| **Curiosity** | Open loop, question, surprising statement | "You won't believe what happened when..." | Awareness |
| **Emotional** | Surprise, humor, shock, fear | "This made me cry..." | Engagement |
| **Value Promise** | Clear benefit stated immediately | "3 ways to save $1000 on..." | Consideration |
| **Pattern Interrupt** | Unexpected visual or audio | Quick cut, loud sound, visual glitch | Stopping scroll |
| **Native Format** | Looks like organic content | "POV: When you discover..." | Authenticity |

### Hook Health Check

| Rating | 2s View Rate | Action |
|--------|--------------|--------|
| **Excellent** | >70% of plays | Hook is working well |
| **Good** | 50-70% of plays | Room for improvement |
| **Needs Work** | <50% of plays | Prioritize hook optimization |

### Diagnostic: Is My Hook Effective?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HOOK EFFECTIVENESS DIAGNOSIS                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
              Calculate 2s View Rate = (2s views / total plays) × 100
                                    │
            ┌───────────────────────┼───────────────────────────┐
            │                       │                           │
            ▼                       ▼                           ▼
         >70%                   50-70%                       <50%
    ─────────────            ─────────────               ─────────────
            │                       │                           │
            ▼                       ▼                           ▼
    HOOK WORKING             HOOK OKAY                   HOOK FAILING
    Check other              Consider testing            Prioritize
    performance              new hooks                   hook overhaul
    factors                        │                           │
                                   │                           │
                                   ▼                           ▼
                    ┌──────────────────────────────────────────────┐
                    │           HOOK IMPROVEMENT TACTICS            │
                    ├──────────────────────────────────────────────┤
                    │ 1. Start with action, not logo               │
                    │ 2. Add text overlay immediately              │
                    │ 3. Use pattern interrupt (sound, visual)     │
                    │ 4. Lead with benefit or curiosity            │
                    │ 5. Test trending sounds/music                │
                    └──────────────────────────────────────────────┘
```

## Video Length Optimization

### Recommended Length by Objective

| Objective | Recommended Length | Reason |
|-----------|-------------------|--------|
| **Awareness** | 15-20 seconds | Maximize reach and completion |
| **Consideration** | 10-15 seconds | Balance engagement and attention |
| **Conversion** | 6-10 seconds | Quick CTA, lowest cost per action |

### Creative Specs (In-Feed Video)

- **Format:** 9:16 vertical, 1080×1920px
- **Max length:** 60 seconds (recommended 9-15 sec for best performance)
- **Audio:** Required — 93% of TikTok users watch with sound on
- **Safe zones:** 150px top, 175px bottom (avoid placing text/CTAs here)

### Completion Rate Benchmarks by Length

| Video Length | Expected Completion Rate |
|--------------|-------------------------|
| Under 15s | 76.4% |
| 15-30s | 65% |
| 30-60s | 50% |
| Over 60s | <40% (also exceeds platform max for In-Feed ads) |

### Length Decision Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    VIDEO LENGTH DECISION                                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    What's your primary objective?
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
   AWARENESS                   CONSIDERATION               CONVERSION
   (Brand building)            (Education)                (Sales)
        │                           │                           │
        ▼                           ▼                           ▼
   15-20 seconds               10-15 seconds              6-10 seconds
        │                           │                           │
        ▼                           ▼                           ▼
   Focus on:                   Focus on:                  Focus on:
   - Reach                     - Key message              - Clear CTA
   - Completion                - Engagement               - Quick value prop
   - Brand recall              - Interest                 - Immediate action
```

## Content Type Analysis

### UGC vs Polished Content

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    UGC vs POLISHED COMPARISON                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  UGC (User-Generated Content)         POLISHED (Studio Quality)             │
│  ───────────────────────────          ─────────────────────────             │
│                                                                              │
│  CPM: -18% lower than polished        CPM: Higher baseline                  │
│  CTR: +12% higher                     CTR: Lower but consistent             │
│  Fatigue rate: 20-30% slower          Fatigue rate: 2-3 day lifespan        │
│                                                                              │
│  Best for:                            Best for:                             │
│  ├─ Prospecting                       ├─ Brand launches                     │
│  ├─ Awareness campaigns               ├─ Premium positioning                │
│  ├─ Gen Z audiences                   ├─ Product showcases                  │
│  └─ Authenticity-focused              └─ Controlled messaging               │
│                                                                              │
│  RECOMMENDATION:                                                             │
│  60-70% UGC, 20-30% Polished, 10% Lo-fi/Native                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Spark Ads vs Regular Ads

| Metric | Spark Ads | Regular Ads |
|--------|-----------|-------------|
| Engagement lift | +35% | Baseline |
| Completion lift | +134% | Baseline |
| 6s VTR lift | +157% | Baseline |
| CVR lift | +69% | Baseline |
| **Best for** | Awareness, mid-funnel, authenticity | Direct response, precise narratives |
| **Control** | Uses creator's post | Full brand control |

### When to Use Each

| Scenario | Recommendation |
|----------|----------------|
| Awareness campaign | Spark Ads (leverage organic engagement) |
| Direct response (conversions) | Regular Ads (control messaging) |
| Testing new angles | Regular Ads (faster iteration) |
| Building credibility | Spark Ads (social proof) |
| Precise brand messaging | Regular Ads (full control) |

## Performance Diagnosis

### Low Completion Rate

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LOW COMPLETION RATE DIAGNOSIS                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    Completion rate below 30%?
                                    │
            ┌───────────────────────┼───────────────────────────┐
            │                       │                           │
            ▼                       ▼                           ▼
      CHECK 1: HOOK           CHECK 2: LENGTH            CHECK 3: CONTENT
      2s view rate?           Video > 30s?              Relevance to audience?
            │                       │                           │
            ▼                       ▼                           ▼
       <50%?                    YES?                      Mismatch?
            │                       │                           │
            ▼                       ▼                           ▼
    STRENGTHEN HOOK          SHORTEN BY 30%           IMPROVE TARGETING
    - New opening            - Get to point faster    - Check audience match
    - Pattern interrupt      - Cut middle section     - Test different segments
    - Add text overlay       - Move CTA earlier       - Review demographics
```

**Common Fixes for Low Completion:**
1. Strengthen first 2 seconds
2. Shorten video by 30% (max 60 sec; target 9-15 sec)
3. Add captions (7% watch without sound — but captions improve retention for all)
4. Test trending sounds (93% watch with sound — audio is a primary engagement lever)

### Low CTR Despite Views

**Diagnostic Questions:**
- Is the CTA clear?
- Is the CTA placed too late?
- Is the offer relevant to the audience?

**Common Fixes:**
1. Move CTA earlier in video
2. Add text overlay CTA
3. Use stronger action verb
4. Test "Shop Now" vs "Learn More"

### Low Conversion Despite Clicks

**Diagnostic Questions:**
- Does landing page match video?
- Is LP mobile-optimized?
- What's the load speed?

**Common Fixes:**
1. Ensure video-to-LP continuity
2. Simplify checkout/form
3. Use TikTok Shop for lower friction

## Optimization Recommendations

### Quick Wins (Implement Today)

1. Add text overlay in first 2 seconds
2. Test trending sounds/music
3. Add captions for sound-off viewing
4. Start with action, not logo

### Creative Tests to Run

| Test | Hypothesis | Metrics to Track |
|------|------------|------------------|
| Hook A vs Hook B (same content) | Different hooks affect retention | 2s view rate, completion |
| UGC vs polished version | UGC performs better | CTR, CPM, fatigue rate |
| 6s vs 15s vs 30s lengths | Shorter = higher completion | Completion rate, CPA |
| Spark Ad vs regular boost | Spark = higher engagement | Engagement rate, CVR |

### Campaign Type Considerations

| Campaign Type | Video Approach | Notes |
|---------------|---------------|-------|
| **Standard auction** | Any length ≤60s; hook critical | Manual control |
| **Smart+ Campaigns** | 9-15s recommended; algorithm selects best | Auto-optimization across audiences (like Meta Advantage+) |
| **Search Ads** (Sep 2025) | 9-15s; clear value prop in first 2s | Keyword-targeted; higher intent audience |
| **Spark Ads** | Matches original organic post length | Must feel native |
| **GMV Max / TikTok Shop** | 9-15s product demo; CTA = "Shop Now" | Automated Shop campaign |

### Advanced Optimization

1. Analyze top-performing organic for hooks
2. Use Creative Center for inspiration
3. Test creator collaborations
4. Implement Smart Creative for auto-optimization
5. For Smart+ Campaigns: let the algorithm test hooks — provide 3-5 variations at launch

## Benchmarks

### View Rate Benchmarks

| Metric | Excellent | Good | Needs Work |
|--------|-----------|------|------------|
| 2s view rate | >70% | 50-70% | <50% |
| 6s view rate | >50% | 30-50% | <30% |

### Completion Rate Benchmarks

| Rating | Completion Rate |
|--------|-----------------|
| Excellent | >50% |
| Good | 30-50% |
| Needs Work | <30% |

### Engagement Rate Benchmarks

| Rating | Engagement Rate |
|--------|-----------------|
| Excellent | >3% |
| Good | 1-3% |
| Needs Work | <1% |

## Output Template

When analyzing TikTok video performance, provide:

```
## TikTok Video Performance Analysis

### Video Health Score: X/10
(Components: Hook, Length, Completion, Engagement)

### Hook Effectiveness
- 2s view rate: X% ([Excellent/Good/Needs Work])
- 6s view rate: X% ([Excellent/Good/Needs Work])
- Hook type: [identified hook type]
- Assessment: [analysis]

### Length Optimization
- Current length: Xs
- Objective: [Awareness/Consideration/Conversion]
- Optimal length: Xs
- Match: [Good/Needs adjustment]

### Completion Funnel
| Stage | Rate | Benchmark | Status |
|-------|------|-----------|--------|
| 25% | X% | - | - |
| 50% | X% | - | - |
| 75% | X% | - | - |
| 100% | X% | >30% | [status] |

### Content Type Recommendation
- Current: [UGC/Polished/Mix]
- Recommended: [recommendation based on analysis]
- Spark Ads opportunity: [Yes/No with reasoning]

### Recommendations

**Immediate Hook Improvements:**
1. [Specific action]
2. [Specific action]

**Optimal Length for Goal:**
- Recommended: Xs for [objective]

**Content Format Suggestion:**
- [UGC/Polished/Spark Ads recommendation]

**A/B Tests to Run:**
1. [Test with hypothesis]
2. [Test with hypothesis]
```

## Monitoring Checklist

### Daily Checks
- [ ] 2s and 6s view rates
- [ ] Completion rate by creative
- [ ] CTR trends
- [ ] CPA by creative

### Weekly Checks
- [ ] Compare hook effectiveness across creatives
- [ ] Analyze length vs completion correlation
- [ ] Review UGC vs polished performance
- [ ] Identify Spark Ads opportunities

### Monthly Review
- [ ] Hook style performance analysis
- [ ] Optimal length validation
- [ ] Content mix optimization
- [ ] Creator collaboration ROI

## MCP Tool Examples

Pull video performance data directly:

```
# Get creative-level performance (hook rates, completion, CTR)
tiktok_get_report(
  start_date="2026-03-01",
  end_date="2026-04-04",
  level="ad",
  metrics=["video_play_actions", "video_watched_2s", "video_watched_6s",
           "video_views_p25", "video_views_p50", "video_views_p100",
           "ctr", "cpc", "spend"]
)

# Get asset info for a specific creative
tiktok_get_asset_info(
  asset_type="video",
  asset_ids=["<video_id>"]
)

# List campaigns to find which use which ad formats
tiktok_query(entity_type="campaigns")
```

---

*Based on 2025-2026 TikTok Ads research. The first 2 seconds determine 70% of video performance - prioritize hook optimization above all else. In-Feed video max is 60 sec; target 9-15 sec for best results.*
