---
name: experiment-design-framework
description: "This skill should be used when the user asks to \"design an A/B test for ads\", \"calculate sample size for an experiment\", \"measure incrementality\", \"run a geo lift study\", or mentions \"statistical significance\", \"holdout test\", or \"test duration\". Do NOT use for: creative fatigue analysis (use creative-fatigue-analyzer), general campaign performance review (use platform-specific troubleshooters), or audience strategy (use buyer-persona-framework)."
---

# Advertising Experiment Design Framework

## Purpose

Provide a rigorous, practical framework for designing and interpreting advertising experiments. Move from "I think this works" to "I know this works, and here's the data." Most ad optimization is observational — experiments let you prove causation.

## When to Use This Skill

Invoke when user mentions:
- **A/B testing:** "How do I A/B test my ads?"
- **Statistical significance:** "Is this result significant?"
- **Sample size:** "How many conversions do I need?"
- **Test duration:** "How long should I run this test?"
- **Incrementality:** "Is this channel actually driving sales?"
- **Holdout test:** "What would happen if I turned off this campaign?"
- **Geo lift:** "How do I test a campaign's true impact?"
- **Multi-variate:** "Can I test multiple things at once?"
- **Learning phase:** "How do I test without wasting budget?"

---

## Part 1: Experiment Types

### Overview Matrix

| Experiment Type | Complexity | Cost | Statistical Rigor | Best For |
|----------------|-----------|------|-------------------|----------|
| **A/B Test (Split Test)** | Low | Low | Medium-High | Creative, copy, landing pages |
| **Multi-Variate Test (MVT)** | Medium | Medium | Medium | Multiple creative elements simultaneously |
| **Holdout Test** | Low | Low-Medium | High | Measuring incrementality of a campaign |
| **Geo Lift Test** | High | High | Highest | Measuring true channel contribution |
| **Pre/Post Test** | Low | Low | Low | Rough directional signal only |
| **Conversion Lift (Meta/Google)** | Medium | Medium | High | Platform-provided incrementality |

### When to Use Each Type

```
QUESTION: What are you trying to learn?

├── "Which creative/copy/CTA works better?"
│   └── A/B Test (or MVT if testing multiple elements)
│
├── "Is this campaign actually driving incremental sales?"
│   └── Holdout Test (simplest) or Conversion Lift Study
│
├── "What's the true ROI of this channel?"
│   └── Geo Lift Test (gold standard) or Holdout Test
│
├── "Should I change my bid strategy?"
│   └── A/B Test with Campaign Budget Optimization
│       (run both strategies simultaneously, same audience split)
│
├── "Which audience performs better?"
│   └── A/B Test with audience splitting
│       (Meta: split test feature; Google: experiments)
│
└── "What's the best combination of headline + image + CTA?"
    └── Multi-Variate Test (need high traffic volume)
```

---

## Part 2: A/B Test Design

### The 5 Requirements of a Valid A/B Test

| Requirement | What It Means | Common Violation |
|------------|--------------|-----------------|
| **1. Single variable** | Change ONE thing between variants | Testing new image AND new copy simultaneously |
| **2. Random assignment** | Audience randomly split, not self-selected | Showing variant A to one audience, B to another |
| **3. Sufficient sample size** | Enough data to detect the expected effect | Declaring a winner after 50 conversions |
| **4. Adequate duration** | Run long enough to capture weekly patterns | Stopping after 3 days because one variant "looks better" |
| **5. Pre-defined success metric** | Decide what "winning" means before launch | Switching metric to "engagement" when conversion results are flat |

### What to Test (Testing Hierarchy)

**Test big bets first, then refine.** Impact ranking:

| Priority | What to Test | Expected Impact | Minimum Budget |
|----------|-------------|----------------|----------------|
| **1 (Highest)** | Offer/Pricing | 50-200% conversion lift | €500 |
| **2** | Audience/Targeting | 30-100% efficiency gain | €1,000 |
| **3** | Landing page | 20-80% conversion lift | €500 |
| **4** | Ad format (video vs image vs carousel) | 20-50% CTR change | €500 |
| **5** | Creative concept (visual theme) | 15-40% CTR change | €300 |
| **6** | Headline/Copy | 10-25% CTR change | €300 |
| **7** | CTA button | 5-15% CTR change | €200 |
| **8** | Color/font/minor design | 2-10% CTR change | €200 |
| **9 (Lowest)** | Bid strategy | 5-20% CPA change | €1,000 |

**Rule of thumb:** Don't A/B test CTA button colors when you haven't tested whether video outperforms images.

### A/B Test Setup by Platform

**Meta Ads:**
- Use the built-in A/B Test feature (Experiments tab)
- Meta handles randomization and statistical analysis
- Choose split: audience (default), placement, or delivery optimization
- Run at ad set level for audience tests, ad level for creative tests
- Monitor with `meta_get_insights` using ad-level breakdowns

**Google Ads:**
- Use Campaign Experiments for bid strategy / targeting tests
- Use Ad Variations for copy / headline tests
- Experiments split traffic automatically (customizable %)
- RSA testing: pin different headlines to positions and compare
- Monitor with `google_ads_run_gaql`:

```sql
SELECT
  ad_group_ad.ad.id,
  ad_group_ad.ad.name,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.cost_micros,
  metrics.conversions_value
FROM ad_group_ad
WHERE campaign.id = {campaign_id}
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.conversions DESC
```

---

## Part 3: Sample Size & Duration

### Sample Size Calculation

**The formula (simplified):**
```
Required conversions per variant ≈ 16 × (1/MDE²)

Where MDE = Minimum Detectable Effect (as decimal)
```

| MDE (Minimum Effect You Want to Detect) | Conversions Needed Per Variant | Total Conversions (2 variants) |
|----------------------------------------|-------------------------------|-------------------------------|
| 50% improvement | ~64 | ~128 |
| 30% improvement | ~178 | ~356 |
| 20% improvement | ~400 | ~800 |
| 15% improvement | ~711 | ~1,422 |
| 10% improvement | ~1,600 | ~3,200 |
| 5% improvement | ~6,400 | ~12,800 |

**Key insight:** The smaller the improvement you want to detect, the more data you need. Most ad tests should target detecting a 20-30% improvement — smaller effects usually aren't worth optimizing for.

### Duration Guidelines

| Factor | Minimum | Recommended | Maximum |
|--------|---------|------------|---------|
| **Calendar time** | 7 days | 14-21 days | 28 days |
| **Full business cycles** | 1 week | 2 weeks | 4 weeks |
| **Conversions per variant** | 50 (directional) | 100+ (reliable) | No max |
| **Confidence level** | 90% (directional) | 95% (standard) | 99% (high-stakes) |

### Duration Calculator

```
Estimated duration = Required conversions per variant / Daily conversion rate per variant

Example:
  Current daily conversions: 20/day (total campaign)
  Split 50/50: 10/day per variant
  Need 400 conversions per variant (20% MDE)
  Duration = 400 / 10 = 40 days

  That's too long. Options:
  a) Accept higher MDE (30% → 178 conversions → 18 days) ✓
  b) Increase budget to get more daily conversions ✓
  c) Use a higher-volume metric (clicks instead of purchases) ⚠️ (less meaningful)
```

### When You Don't Have Enough Volume

| Daily Conversions | Recommended Approach |
|------------------|---------------------|
| > 50/day | Full A/B test, 95% significance, 2-week minimum |
| 20-50/day | A/B test, 90% significance, 3-week minimum |
| 5-20/day | A/B test, 90% significance, accept higher MDE (30%+) |
| 1-5/day | Sequential testing (run A for 2 weeks, then B for 2 weeks) |
| < 1/day | Don't A/B test conversions. Test higher-funnel metric (CTR, Add to Cart) |

---

## Part 4: Statistical Significance

### What It Means

```
"95% statistical significance" means:

There is a ≤5% probability that the observed difference between
variants occurred by random chance alone.

It does NOT mean:
- "95% chance that variant B is better" (common misinterpretation)
- "Variant B will always outperform A by this margin"
- "The test is 95% accurate"
```

### Interpreting Results

| Scenario | Significance | Confidence Interval | Interpretation | Action |
|----------|-------------|-------------------|---------------|--------|
| A: 2.1% CVR, B: 2.8% CVR | p = 0.02 (sig.) | B is +20% to +50% better | Clear winner | Implement B |
| A: 2.1% CVR, B: 2.4% CVR | p = 0.15 (not sig.) | B is -5% to +30% better | Inconclusive | Need more data or accept ambiguity |
| A: 2.1% CVR, B: 2.2% CVR | p = 0.45 (not sig.) | B is -12% to +18% better | No difference | Either variant works, choose based on other factors |
| A: 2.1% CVR, B: 1.6% CVR | p = 0.01 (sig.) | B is -15% to -35% worse | Clear loser | Do NOT implement B |

### Common Statistical Mistakes

| Mistake | Why It's Wrong | What to Do Instead |
|---------|---------------|-------------------|
| **Peeking and stopping early** | Significance fluctuates early; stopping on a "good day" inflates false positives | Set duration upfront, only check at end (or use sequential testing) |
| **Running until significant** | If you keep running, random fluctuations will eventually reach 95% | Pre-define sample size and duration |
| **Ignoring negative results** | "The test didn't work, let's try something else" loses the learning | Document learnings: what does this tell you about your audience? |
| **Testing too many variants** | 5 variants = 10 pairwise comparisons = much higher false positive rate | Maximum 3-4 variants; apply Bonferroni correction for multiple comparisons |
| **Wrong success metric** | Optimizing for clicks when you care about purchases | Define primary metric before launch, ideally closest to revenue |
| **Novelty effect** | New variant gets initial engagement boost that fades | Run test for 2+ weeks to see past novelty |
| **Segment cherry-picking** | "It didn't win overall, but it won with women 25-34!" | Only analyze pre-defined segments, not post-hoc discoveries |

---

## Part 5: Incrementality Testing

### What Is Incrementality?

```
Incrementality = Sales with ads - Sales that would have happened anyway (without ads)

Example:
  With retargeting campaign: 100 purchases/week
  Without retargeting (holdout): 75 purchases/week
  Incremental sales: 25/week
  Incrementality rate: 25% (only 25 of 100 sales were truly driven by the ads)
  True ROAS: Reported ROAS × 0.25
```

### Holdout Test Design

**The simplest incrementality test:**

1. Take your retargeting audience
2. Randomly split: 90% see ads (treatment), 10% see no ads (holdout)
3. Run for 2-4 weeks
4. Compare purchase rate: treatment group vs holdout group
5. The difference = incremental impact

**Meta implementation:**
- Create a Conversion Lift study in Experiments
- Meta handles the random split and measurement
- Minimum spend: ~€5,000 over the test period
- Results in 2-4 weeks

**Google Ads implementation:**
- Use Campaign Experiments with a holdout
- Or use Google's Conversion Lift measurement (for larger accounts)

### Typical Incrementality by Campaign Type

| Campaign Type | Typical Incrementality | What This Means |
|--------------|----------------------|----------------|
| Brand search (own brand) | 10-30% | Most would have found you anyway |
| Non-brand search (generic terms) | 40-70% | Capturing real intent |
| Google Shopping | 30-60% | Price comparison, some would buy anyway |
| Meta prospecting (broad) | 60-85% | Genuine new demand creation |
| Meta retargeting (all visitors) | 15-35% | Many would have returned anyway |
| Meta retargeting (cart abandoners) | 20-45% | Some would have completed purchase |
| TikTok prospecting | 50-80% | Discovery-driven, high incrementality |
| Google Display | 5-25% | View-through, often low incrementality |

**Implication:** Channels that look "efficient" (low CPA, high ROAS) often have low incrementality. Brand search has the best ROAS but the lowest incrementality — those customers were already coming.

### Geo Lift Test Design

**The gold standard for channel-level incrementality:**

1. **Select matched markets:** Pair cities/regions with similar demographics, market size, and baseline sales
2. **Treatment vs control:** Run ads in treatment markets, no ads (or standard spend) in control
3. **Duration:** 4-8 weeks minimum (longer for lower frequency categories)
4. **Measurement:** Compare sales difference between treatment and control, adjusted for baseline

**Market Matching Criteria:**

| Factor | How to Match | Data Source |
|--------|-------------|-------------|
| Population size | Within 20% of each other | Census data |
| Baseline sales | Similar weekly revenue | Shopify/GA4 |
| Seasonality pattern | Same seasonal trends | Historical sales |
| Competitive landscape | Similar competitors present | Market research |
| Media landscape | Similar media costs | Platform data |

**Example Design:**
```
Treatment markets: Amsterdam, Rotterdam, Utrecht
Control markets: Den Haag, Eindhoven, Groningen

Run Meta prospecting campaigns ONLY in treatment markets for 6 weeks.
Compare sales growth in treatment vs control.

Treatment sales growth: +18%
Control sales growth: +3% (organic trend)
Incremental lift: +15%
```

---

## Part 6: Platform-Specific Testing Features

### Meta Experiments

| Feature | Use Case | Minimum Budget | Duration |
|---------|---------|---------------|----------|
| A/B Test | Creative, audience, placement | €500/variant | 7-28 days |
| Conversion Lift | Campaign incrementality | €5,000+ | 14-28 days |
| Brand Lift | Awareness/recall measurement | €10,000+ | 14-28 days |
| Advantage+ Tests | Automated creative optimization | €1,000+ | 14 days |

**Use `meta_get_insights` to monitor tests:**
- Compare ad-level performance across variants
- Track primary metric (conversions) AND secondary metrics (CTR, CPC)
- Check `frequency` to ensure adequate exposure

### Google Ads Experiments

| Feature | Use Case | Setup |
|---------|---------|-------|
| Campaign Experiments | Bid strategy, targeting changes | Draft → Experiment (set traffic split) |
| Ad Variations | Headline, description, URL changes | Find & Replace or custom rules |
| Video Experiments | YouTube creative testing | Brand Lift integration |

**Use `google_ads_run_gaql` to compare experiments:**
```sql
SELECT
  campaign.name,
  campaign.experiment_type,
  metrics.conversions,
  metrics.cost_micros,
  metrics.conversions_value,
  metrics.search_impression_share
FROM campaign
WHERE campaign.experiment_type != 'UNSPECIFIED'
  AND segments.date DURING LAST_30_DAYS
```

---

## Part 7: Testing Calendar & Cadence

### Recommended Testing Cadence

| Business Size | Monthly Ad Spend | Tests per Month | Focus |
|--------------|-----------------|----------------|-------|
| Small (<€5K/mo) | €1-5K | 1 test | Creative or audience |
| Medium (€5-25K/mo) | €5-25K | 2-3 tests | Creative, audience, bid strategy |
| Large (€25-100K/mo) | €25-100K | 4-6 tests | Full program across platforms |
| Enterprise (>€100K/mo) | €100K+ | 8-12 tests | Continuous optimization program |

### Annual Testing Roadmap

| Quarter | Testing Focus | Rationale |
|---------|--------------|-----------|
| **Q1 (Jan-Mar)** | Audience & targeting tests | Low CPMs, good for testing |
| **Q2 (Apr-Jun)** | Creative format tests | Prepare winners for H2 |
| **Q3 (Jul-Sep)** | Landing page & offer tests | Optimize conversion ahead of Q4 |
| **Q4 (Oct-Dec)** | Minimize testing, run winners | Peak season, don't experiment with high stakes |

### Test Documentation Template

For every experiment, document:

```
Test Name: [Descriptive name]
Hypothesis: "If we [change X], then [metric Y] will [improve/decrease] by [Z%]
            because [reason/insight]."
Primary Metric: [Conversion rate / ROAS / CPA / CTR]
Secondary Metrics: [Other metrics to watch]
Platform: [Meta / Google / TikTok]
Audience: [Who sees the test]
Variants:
  - Control (A): [Description]
  - Treatment (B): [Description]
Expected MDE: [%]
Required Sample: [N conversions per variant]
Estimated Duration: [Days]
Budget: [€ per variant]
Start Date: [Date]
End Date: [Date]
Results: [Fill in after test completes]
Learning: [What did we learn, regardless of outcome?]
Next Action: [What do we do with this result?]
```

---

## Part 8: Common Testing Mistakes & Fixes

### The 10 Most Costly Mistakes

| # | Mistake | Cost | Fix |
|---|---------|------|-----|
| 1 | **Not testing at all** | Missing 20-50% efficiency gains | Start with 1 test per month |
| 2 | **Peeking daily and stopping early** | 30%+ false positive rate | Pre-commit to end date |
| 3 | **Testing too many things at once** | Can't attribute results | One variable per test |
| 4 | **Not enough budget per variant** | Inconclusive results, wasted time | Minimum €300-500/variant |
| 5 | **Running during promotions** | Promotion effect masks test effect | Test during normal periods |
| 6 | **Ignoring learning phase** | First 3-5 days data is unreliable | Exclude first 3 days from analysis |
| 7 | **Winner takes all mentality** | Missing nuance in results | Check: does winner work for all segments? |
| 8 | **Not documenting results** | Repeating failed tests, losing learnings | Maintain a test log (spreadsheet) |
| 9 | **Testing during seasonality shifts** | Confounding variables | Test within stable periods |
| 10 | **Copying competitor tests** | Different audience, different results | Test based on your own data and hypotheses |

---

## Part 9: Interpreting & Acting on Results

### Result Interpretation Matrix

| Statistical Sig. | Effect Size | Confidence Interval | Verdict | Action |
|------------------|------------|-------------------|---------|--------|
| p < 0.05 | Large (>20%) | Narrow, above zero | Strong winner | Implement immediately |
| p < 0.05 | Small (5-10%) | Narrow, above zero | Marginal winner | Implement if no downside |
| p = 0.05-0.10 | Any | Crosses zero | Inconclusive | Extend test or accept ambiguity |
| p > 0.10 | Near zero | Wide, centered on zero | No difference | Either option works |
| p < 0.05 | Negative | Below zero | Clear loser | Reject the change |

### What To Do After Every Test

```
1. DOCUMENT the result (see template above)
2. SHARE with team (even negative results have value)
3. DECIDE: Implement, iterate, or reject
4. GENERATE next hypothesis based on what you learned
5. QUEUE the next test
```

### Building a Testing Culture

**The compound effect of testing:**
```
1 test/month × 12 months = 12 experiments/year
Assume 30% have a clear winner with 15% average improvement
= ~4 winning changes per year
Compound improvement: 1.15^4 = 1.75x (75% cumulative improvement)

This is why companies that test systematically outperform those that optimize by intuition.
```

---

## Part 10: Advanced — Multi-Touch Incrementality

### Beyond Single-Channel Testing

When you run ads on Meta, Google, and TikTok simultaneously, turning off one channel affects the others. Advanced incrementality testing accounts for this:

**Media Mix Modeling (MMM):**
- Statistical model using 2+ years of spend and revenue data
- Accounts for seasonality, promotions, organic trends
- Outputs: marginal ROAS per channel, optimal budget allocation
- Tools: Meta Robyn (open source), Google Meridian (open source), or commercial platforms
- Best for: €50K+/month spend, 2+ years of data

**Multi-Cell Lift Studies:**
- Split audience into multiple cells: see all ads, see only Meta, see only Google, see no ads
- Compare conversion rates across cells
- Shows interaction effects between channels
- Requires large audiences (100K+ per cell)

**Practical Alternative for Smaller Budgets:**
```
Month 1: Run all channels normally (baseline)
Month 2: Turn off Channel X (measure impact)
Month 3: Restore Channel X (confirm recovery)

Impact of Channel X = Baseline revenue - Month 2 revenue
(Adjusted for seasonality and organic trends)

This is crude but directional. Better than no incrementality data.
```

### MCP Tools for Experiment Monitoring

**Pre-test baseline (all platforms):**
Use `meta_get_insights`, `google_ads_run_gaql`, `tiktok_get_report` to establish 30-day baseline metrics before any experiment begins.

**During test:**
Use same tools weekly to monitor both variants. Watch for:
- Sample size accumulation (on track?)
- Any extreme outliers (data quality issue?)
- External factors (competitor promotion, PR event?)

**Post-test analysis:**
Pull final metrics from both variants using platform tools, calculate significance, document results.
