---
name: google-ads-scaling-calculator
description: "This skill should be used when the user asks to \"scale Google Ads budget\", \"calculate incremental ROAS\", \"analyze diminishing returns\", \"plan a scaling roadmap\", or mentions \"iROAS\", \"break-even calculation\", or \"profit maximization model\". Do NOT use for: initial campaign setup (use search-campaign-builder), bid strategy selection (use learning-phase-tracker)."
---
# Scaling Calculator

Complete guide for calculating and implementing Google Ads budget scaling strategies with focus on profitability and incremental ROAS.

## Pull Scaling Baseline Data via MCP

```
google_ads_run_gaql(query="
  SELECT campaign.name, campaign.bidding_strategy_type,
         metrics.search_impression_share,
         metrics.search_budget_lost_impression_share,
         metrics.search_rank_lost_impression_share,
         metrics.cost_micros, metrics.conversions,
         metrics.cost_per_conversion,
         metrics.conversions_value,
         campaign.target_roas.target_roas,
         campaign.target_cpa.target_cpa_micros
  FROM campaign
  WHERE segments.date DURING LAST_30_DAYS
    AND campaign.status = 'ENABLED'
  ORDER BY metrics.cost_micros DESC
  LIMIT 20
")
```

Interpret:
- `search_budget_lost_impression_share` > 15% → budget is the scaling bottleneck
- `search_rank_lost_impression_share` > 20% → bids/QS limit reach — fix first
- Both low → market saturation; try horizontal scaling or Demand Gen / PMax

## Scaling Fundamentals

More budget does not mean linearly more results. Diminishing returns occur because best audiences and search terms trigger first, more budget means broader (less relevant) reach, and competition forces higher bids.

## Break-Even Calculations

### ROAS Break-Even

```
Formula: Break-Even ROAS = 1 / Gross Margin %
Target ROAS = 1 / (Gross Margin - Desired Net Margin)

Quick reference:
├── 30% margin → Break-even 3.33x, Target (10% profit) 3.70x
├── 40% margin → Break-even 2.50x, Target (10% profit) 2.78x
├── 50% margin → Break-even 2.00x, Target (10% profit) 2.22x
```

### CPA Break-Even

```
E-commerce: Break-Even CPA = AOV x Gross Margin %
Lead Gen:   Break-Even CPL = Customer Value x Close Rate x Margin

Examples:
├── AOV $100, Margin 40%: Break-even CPA = $40
├── Customer Value $2000, Close Rate 10%, Margin 30%: Break-even CPL = $60
```

> Full ROAS and CPA break-even tables by margin level in [references/detailed-reference.md](references/detailed-reference.md).

## Incremental ROAS (iROAS)

**iROAS = Additional Revenue / Additional Ad Spend** — measures the true value of additional spend, unlike blended ROAS which overstates value (some conversions would happen without ads).

**Example:** Budget $10k → $15k (+$5k). Revenue $50k → $65k (+$15k). Blended ROAS drops 5.0x → 4.3x, but iROAS = $15k/$5k = 3.0x. If break-even is 2.5x, scaling is profitable despite lower blended ROAS.

**Typical incrementality:** Brand 30-60%, Non-brand Search 60-80%, Shopping 50-70%, PMax 60-80%, Remarketing 20-50%.

> Detailed iROAS calculation methods (geo experiment, budget step test, holdout) in [references/detailed-reference.md](references/detailed-reference.md).

## Scaling Strategies

### Conservative Scaling (Default)

**Rule: Maximum 15-20% budget increase per week.**

- Week 0: Baseline ($1,000, ROAS 4.5x)
- Week 1: +15% ($1,150), monitor iROAS and CPA trend
- Week 2: +15% if stable ($1,322), monitor QS and auction insights
- Week 3: +15% if stable ($1,520)
- Week 4: Evaluate — compare to Week 0, calculate true iROAS

**Stop scaling when:** iROAS < break-even, ROAS drops >25% WoW, CPA increases >30% vs baseline, learning phase doesn't complete.

### Aggressive Scaling (Proven Winners Only)

Only when campaign is profitable >3 months, Smart Bidding stable, iROAS proven, sufficient margin above break-even.

Method: +20% → +25% → +20% → +15% over 4 weeks = ~2x budget. Monitor daily (spend pacing), every 3 days (conversion-lag adjusted ROAS), weekly (full review).

### Horizontal vs Vertical

**Vertical (more budget, same campaigns):** Easy, quick impact, but diminishing returns and limited by audience size.

**Horizontal (new campaigns, audiences):** New potential (YouTube, Demand Gen, new geos), but new learning phases and uncertain performance.

**Optimal: Hybrid** — 70% existing top performers, 20% expansion of proven concepts, 10% experimental.

## Profit Maximization

### MER (Marketing Efficiency Ratio)

MER = Total Revenue / Total Marketing Spend. Unlike ROAS (single channel), MER measures holistic efficiency including cross-channel and brand halo effects.

Benchmarks: Startup/Growth 3-5x, Mature E-commerce 5-8x, Market Leader 8-15x.

### Profit Curve

Optimal spend is where Marginal Cost = Marginal Revenue (iCPA = Break-Even CPA, iROAS = Break-Even ROAS).

Practical approach: Start profitable → increase in steps → track iROAS per step → stop when iROAS < break-even → optimal = step before that point.

> MER analysis example and Google Ads Script for automated scaling monitoring in [references/detailed-reference.md](references/detailed-reference.md).

## Scaling Roadmap Template

```markdown
# Scaling Roadmap

## Current State
- **Monthly Spend:** [X] | **ROAS:** [X.X]x | **Break-Even:** [X.X]x
- **Impression Share:** [X]% (room: [X]%)
- **Budget Limited Days:** [X]/month
- **Top Performers:** [Campaign names]

## Scaling Plan

### Phase 1: Preparation (Week 1-2)
- [ ] Calculate break-even ROAS for all campaigns
- [ ] Identify top 3 scalable campaigns
- [ ] Set up incrementality tracking
- [ ] Document baseline metrics

### Phase 2: Conservative Scaling (Week 3-6)
| Week | Campaign | Budget Change | Target ROAS |
|------|----------|---------------|-------------|
| 3 | [Top 1] | +15% | >[X]x |
| 4 | [Top 1] | +15% | >[X]x |
| 5 | [Top 2] | +15% | >[X]x |

### Phase 3: Evaluation (Week 7-8)
- [ ] Calculate true iROAS per campaign
- [ ] Compare MER before/after
- [ ] Identify diminishing returns point

## Budget Projection
| Month | Spend | Expected Revenue | Target ROAS |
|-------|-------|------------------|-------------|
| Current | $X | $X | X.Xx |
| +1 Month | $X (+X%) | $X | X.Xx |

## Rollback Triggers
- iROAS below [X.X]x for 2 consecutive weeks
- CPA increases >30% vs baseline
- Quality Score drops significantly
```
