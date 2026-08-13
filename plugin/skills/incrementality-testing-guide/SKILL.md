---
name: incrementality-testing-guide
description: "This skill should be used when the user asks to \"run an incrementality test\", \"measure true ad impact\", \"design a geo lift test\", mentions \"incremental ROAS\", \"holdout experiment\", or \"is my advertising actually working\". Do NOT use for: attribution discrepancy diagnosis (use attribution-reconciler), A/B testing landing pages (use landing-page-optimization-guide), or first-party data / tracking setup (use first-party-data-strategy)."
---
# Incrementality Testing Guide

## Purpose

Help advertisers understand and implement incrementality testing to measure the **true causal impact** of their advertising, beyond what traditional attribution can tell them.

## When to Use This Skill

Invoke when user mentions:
- **Incrementality:** "Is my advertising actually working?"
- **Testing:** "How do I run a geo lift test?"
- **Attribution skepticism:** "I don't trust platform reporting"
- **True ROAS:** "What's my incremental ROAS?"
- **Holdout tests:** "Should I run a holdout experiment?"
- **MMM/Econometrics:** "What is marketing mix modeling?"
- **Conversion lift:** "How do I set up a conversion lift study?"

---

## Part 1: Why Incrementality Testing Matters

### The Attribution Problem

Traditional attribution (last-click, platform-reported) has fundamental flaws:

| Attribution Type | What It Measures | What It Misses |
|-----------------|------------------|----------------|
| Last-click (GA4) | Final touchpoint | All assist interactions |
| Platform reporting | Platform's attributed conversions | Over-credits, includes organic |
| View-through | Ad view → conversion | Many would convert anyway |
| Multi-touch | Weighted path credit | Still doesn't prove causation |

**The Core Problem:** Attribution tells you WHO converted after seeing an ad, not WHETHER the ad caused the conversion.

### What Incrementality Testing Answers

**The Question:** "What additional conversions/revenue occurred BECAUSE of advertising that would NOT have happened without it?"

| Metric | Definition | Formula |
|--------|------------|---------|
| Incremental conversions | Conversions caused by ads | Test group - Control group |
| Incrementality rate | % of conversions caused by ads | (Test - Control) / Test |
| Incremental ROAS (iROAS) | True return on ad spend | Incremental Revenue / Ad Spend |

### Industry Benchmarks: Typical Incrementality Rates

| Channel/Tactic | Typical Incrementality | Notes |
|----------------|----------------------|-------|
| **Prospecting (cold audience)** | 70-90% | Reaching new users |
| **Generic search** | 75-95% | High intent, new customers |
| **Brand search** | 10-40% | Users already looking for you |
| **Retargeting (cart abandoners)** | 40-60% | Some would return anyway |
| **Retargeting (site visitors)** | 20-40% | Higher cannibalization |
| **Retargeting (past buyers)** | 15-30% | Lowest incrementality |
| **Social awareness** | 50-80% | Hard to measure directly |
| **Display prospecting** | 60-85% | Depends on targeting |

**Key Insight:** High ROAS channels often have LOW incrementality (brand search, retargeting), while lower ROAS channels (prospecting) often have HIGH incrementality.

---

## Part 2: Types of Incrementality Tests

### 1. Geo Lift Tests (Gold Standard)

**How it works:** Turn off advertising in some geographic regions while keeping it on in others.

| Aspect | Details |
|--------|---------|
| **Mechanism** | Compare sales in "ad on" vs "ad off" regions |
| **Best for** | Any channel, any business size |
| **Minimum spend** | €5,000/month |
| **Duration** | 4-8 weeks |
| **Confidence** | High (if properly designed) |

**Pros:**
- Works for any advertising channel
- Measures real-world impact
- Clean causal inference

**Cons:**
- Requires sufficient regional sales
- Lost revenue in control regions
- Geographic spillover possible

**Design Principles:**
1. Match test/control on historical sales (within 15%)
2. Account for regional differences (demographics, income)
3. Run for at least 4 weeks (full purchase cycles)
4. Document external factors during test

### 2. Conversion Lift (Meta/Google)

**How it works:** Platform creates test/holdout groups automatically.

| Platform | Name | Setup | Requirements |
|----------|------|-------|--------------|
| Meta | Conversion Lift | Experiments → Conversion Lift | €2K+/month spend |
| Google | Conversion Lift | Via Google rep | €5K+/month, rep assistance |

**Pros:**
- Free to run
- Platform handles randomization
- Results in 2-4 weeks

**Cons:**
- Only tests that specific platform
- Relies on platform's measurement
- Some campaigns ineligible

### 3. Holdout Tests (For Retargeting)

**How it works:** Exclude a random % of your audience from seeing ads.

| Parameter | Recommendation |
|-----------|---------------|
| Holdout size | 10-20% of audience |
| Duration | 3-4 weeks minimum |
| Measurement | Compare conversion rates |

**Setup Steps:**
1. Create audience of all retargeting-eligible users
2. Randomly split (use user ID hash)
3. Exclude holdout group from all retargeting campaigns
4. Track conversions in both groups for 4+ weeks
5. Calculate: (Test CR - Control CR) / Test CR = Incrementality

### 4. Synthetic Control Methods

**How it works:** Use statistical modeling to create a "synthetic" control group.

**When to use:**
- Can't run true experiment
- Historical data available
- Need to analyze past campaigns

**Tools:**
- Google's CausalImpact (R/Python)
- Facebook's GeoLift (Python)
- Custom regression modeling

### 5. Marketing Mix Modeling (MMM)

**How it works:** Statistical analysis of all marketing inputs vs. business outcomes.

| Aspect | Details |
|--------|---------|
| **Data needed** | 2+ years, weekly granularity |
| **Cost** | €15,000-50,000 |
| **Time** | 8-12 weeks |
| **Confidence** | Highest (holistic view) |

**Best for:**
- Large advertisers (€100K+/month)
- Multi-channel marketing
- Strategic planning

**What MMM tells you:**
- Contribution of each channel to revenue
- Optimal budget allocation
- Diminishing returns curves
- Long-term brand effects

---

## Part 3: Designing a Good Incrementality Test

### Test Design Checklist

**Before Starting:**
- [ ] Define hypothesis clearly (e.g., "Meta retargeting drives 50%+ incremental conversions")
- [ ] Choose appropriate test type for budget/channel
- [ ] Calculate required sample size
- [ ] Set test duration (minimum 4 weeks)
- [ ] Document baseline metrics

**Test Structure:**

| Element | Requirement |
|---------|-------------|
| **Test/Control balance** | 50/50 for geo, 80/20 for holdout |
| **Sample matching** | Historical metrics within 15% |
| **Duration** | At least 1 full purchase cycle + 1 week |
| **Isolation** | No other major changes during test |
| **Documentation** | External factors logged daily |

### Statistical Power Calculation

**Minimum sample sizes for reliable results:**

| Desired Confidence | MDE (Minimum Detectable Effect) | Conversions Needed |
|-------------------|--------------------------------|-------------------|
| 80% | ±30% | ~200 per group |
| 80% | ±20% | ~400 per group |
| 90% | ±20% | ~600 per group |
| 95% | ±15% | ~1,000 per group |

**Formula for sample size:**
```
n = 2 × (Zα + Zβ)² × σ² / (μ1 - μ2)²

Where:
- Zα = 1.96 for 95% confidence
- Zβ = 0.84 for 80% power
- σ = standard deviation
- μ1 - μ2 = effect size to detect
```

### Avoiding Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| Test too short | Results not statistically significant | Minimum 4 weeks |
| Unmatched groups | Biased baseline comparison | Pre-match on historical KPIs |
| Contamination | Treatment leaks to control | Strict geographic separation |
| Multiple testing | False positives | Pre-register one primary metric |
| Optimizing during test | Changes invalidate results | Freeze all campaign settings |
| External factors | Noise masks signal | Document and adjust for events |

---

## Part 4: When to Test (and When Not To)

### Test Prioritization Framework

| Factor | Test Priority | Reason |
|--------|--------------|--------|
| Largest spend channel | HIGH | Highest potential impact |
| Channel with uncertain performance | HIGH | Clarify value |
| Retargeting | HIGH | Often over-attributed |
| Brand search | MEDIUM | Known low incrementality |
| New channel (testing) | LOW | Already in test mode |
| Proven channel | LOW | Retest every 12 months |

### When NOT to Test

- **<€5K/month spend:** Insufficient data for significance
- **<100 monthly conversions:** Sample too small
- **During promotional periods:** Too much noise
- **Q4 peak season:** Data too valuable to sacrifice
- **After major changes:** Need stable baseline first
- **When desperate:** Tests take 4-8 weeks

### Testing Calendar Template

| Quarter | Test Focus | Why |
|---------|-----------|-----|
| Q1 (Jan-Mar) | Prospecting channels | Post-holiday baseline |
| Q2 (Apr-Jun) | Retargeting | Pre-summer assessment |
| Q3 (Jul-Sep) | Brand campaigns | Before Q4 planning |
| Q4 (Oct-Dec) | NO TESTING | Peak revenue period |

---

## Part 5: Interpreting Results

### Understanding Your Results

| Incrementality Rate | Interpretation | Action |
|--------------------|----------------|--------|
| **85-100%** | Highly incremental | Scale confidently |
| **65-85%** | Mostly incremental | Maintain, optimize |
| **45-65%** | Partially incremental | Review targeting, reduce waste |
| **25-45%** | Low incrementality | Significant optimization needed |
| **<25%** | Mostly cannibalistic | Consider pausing |

### Calculating True Performance

**Adjusted Metrics:**

```
Reported ROAS: 5.0x
Measured Incrementality: 60%
Incremental ROAS: 5.0x × 60% = 3.0x

This channel's TRUE return is 3.0x, not 5.0x
```

**Budget Reallocation Logic:**

| If iROAS is... | And target ROAS is... | Then... |
|---------------|----------------------|---------|
| Above target | - | Scale spending |
| At target | - | Maintain |
| Below target but positive | Above breakeven | Optimize before scaling |
| Negative/minimal | Any | Reduce or pause |

### Statistical Significance Check

**Your result is statistically significant if:**
- p-value < 0.05 (95% confidence)
- Confidence interval doesn't cross zero
- Effect size is > minimum detectable effect

**If not significant:**
- Extend test duration
- Increase sample size
- Accept wider confidence interval
- Combine with other data sources

---

## Part 6: Quick Reference Tables

### Test Type Selection Matrix

| Situation | Recommended Test | Why |
|-----------|-----------------|-----|
| Single platform, €5K+/month | Geo lift | Most reliable |
| Meta only, any budget | Meta Conversion Lift | Free, easy |
| Retargeting specifically | Holdout test | Direct measurement |
| Historical analysis | Synthetic control | No experiment needed |
| €100K+/month, multi-channel | Full MMM | Comprehensive view |

### Platform-Specific Notes

| Platform | Built-in Testing | Notes |
|----------|-----------------|-------|
| **Meta** | Conversion Lift, Brand Lift | In Experiments tab |
| **Google** | Conversion Lift (via rep) | Requires Google contact |
| **TikTok** | Conversion Lift (limited) | Check current availability |
| **LinkedIn** | Brand Lift | Limited conversion lift |

### Cost of Not Testing

| Annual Spend | If 20% Non-Incremental | If 30% Non-Incremental |
|-------------|----------------------|----------------------|
| €50K | €10K wasted | €15K wasted |
| €100K | €20K wasted | €30K wasted |
| €500K | €100K wasted | €150K wasted |
| €1M | €200K wasted | €300K wasted |

---

## Part 7: Next Steps After Testing

### Post-Test Action Framework

1. **Document findings:** Create permanent record of methodology, results, confidence
2. **Share with stakeholders:** Translate to business impact
3. **Adjust budgets:** Reallocate based on iROAS
4. **Update reporting:** Add incrementality context to dashboards
5. **Plan next test:** Incrementality changes over time - retest in 6-12 months

### Building a Measurement Culture

| Level | Practice |
|-------|----------|
| **Starter** | One test per year on largest channel |
| **Developing** | Quarterly tests on different channels |
| **Advanced** | Continuous testing calendar, synthetic control |
| **Mature** | Full MMM with regular lift studies |

---

## Optional: Enrich with Live Data

If the user has connected their GA4 account, pull baseline metrics before the test starts to establish the pre-test period benchmark:

```python
# Capture pre-test baseline: conversions, sessions, revenue by channel
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="30daysAgo",
    end_date="today",
    metrics=["keyEvents", "sessions", "purchaseRevenue"],
    dimensions=["date", "sessionDefaultChannelGroup"]
)
```

Document this baseline before the test begins. Post-test, run the same query for the test period and compare. The difference (adjusted for seasonality) is your incrementality signal. Store both outputs to calculate iROAS accurately.

*Last updated: February 2026*
*Based on industry best practices and academic research in causal inference*
