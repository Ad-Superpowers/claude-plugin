---
description: "Design rigorous incrementality tests to measure true advertising impact. Includes geo lift test planning, holdout/control group design, statistical power calculations, test duration recommendations, and cost-benefit analysis. Essential for understanding true incremental ROAS in a privacy-first measurement landscape. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Incrementality Test Designer

Design a rigorous incrementality test for your platform. In a privacy-first world (40-60% iOS signal loss, 50-65% modeled conversions), incrementality testing answers the only question that matters: "What revenue did this advertising create that wouldn't have happened anyway?"

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### TEST RECOMMENDATION
| Factor | Value |
|--------|-------|
| Recommended Test Type | [Geo Lift / Conversion Lift / Holdout / Ghost Bids / MMM] |
| Why This Test | [2-3 bullet reasons based on spend, platform, geography] |
| Estimated Duration | [X weeks total incl. baseline + cooldown] |
| Confidence Level | [High / Medium-High / Medium] |

**Test Type Selection Reference:**

| Test Type | Best For | Min Budget | Min Duration | Confidence |
|-----------|----------|-----------|--------------|------------|
| Geo Lift | Any channel, any size | 5K/mo | 4-6 weeks | High |
| Conversion Lift (Meta) | Meta only | 2K/mo | 2-4 weeks | Medium-High |
| Brand Lift (Google) | Brand awareness | 5K+ | 2 weeks | High |
| Holdout Test | Retargeting | 3K/mo | 3-4 weeks | Medium |
| Ghost Bids | Display/Video | 10K/mo | 4 weeks | High |
| Full MMM | All channels | 100K+/mo | 8-12 weeks | Highest |

### GEO SPLIT DESIGN
| Factor | Test Regions | Control Regions |
|--------|-------------|-----------------|
| Population | [50% of target] | [50% of target] |
| Historical similarity | Must match within 15% | Baseline |
| Suggested regions | [List 3-5] | [List 3-5] |

**Pre-built geo splits (use if applicable):**

Netherlands:
| Option | Test | Control | Balance |
|--------|------|---------|---------|
| North/South | Noord-Holland, Zuid-Holland, Utrecht | Noord-Brabant, Gelderland, Limburg | 85% |
| Randstad/Rest | Amsterdam, Rotterdam, Den Haag | All other provinces | 72% |

Germany:
| Option | Test | Control | Balance |
|--------|------|---------|---------|
| North/South | NRW, Niedersachsen, Hamburg | Bavaria, Baden-Wuerttemberg, Hessen | 88% |

### POWER ANALYSIS
| Metric | Your Value | Required (80% Power) | Gap |
|--------|-----------|---------------------|-----|
| Monthly conversions | [from data] | 400 (200/group) | [+/-X] |
| Monthly revenue | [from data] | - | - |
| Current ROAS | [calculated] | - | - |
| MDE at 80% confidence | +/-30% | ~200/group | - |
| MDE at 90% confidence | +/-20% | ~400/group | - |
| MDE at 95% confidence | +/-15% | ~800/group | - |
| Test duration needed | [calculated] | [X weeks] | - |

Data sufficiency: [Sufficient (400+/mo) | Marginal (extend duration) | Insufficient (use platform lift instead)]

### SCHEDULE
| Phase | Duration | Activities |
|-------|----------|------------|
| Pre-test baseline | 2 weeks | Measure both regions, confirm <15% variance |
| Test period | 4-6 weeks | Ads ON in test, OFF in control |
| Post-test cooldown | 1 week | Measure lag conversions |
| Analysis | 1 week | Statistical analysis, significance testing |

### COST-BENEFIT ANALYSIS
| Cost Type | Amount |
|-----------|--------|
| Lost revenue (control group) | [est. 50% of normal in control] |
| Media spend (unchanged) | [X] |
| Analysis time | [X hours] |
| **Total Test Cost** | **[X]** |

| Savings Scenario | Annual Impact |
|------------------|---------------|
| 20% of spend non-incremental | Save [X]/year |
| 30% of spend non-incremental | Save [X]/year |
| 80%+ incremental | Validate/increase budget |

ROI breakeven: [X weeks] of optimized spend

### HOLDOUT DESIGN (if retargeting test)
| Group | Size | Treatment |
|-------|------|-----------|
| Control (Holdout) | 10-20% | No retargeting ads |
| Test | 80-90% | Normal retargeting |

**Retargeting incrementality benchmarks:**

| Type | Expected Incrementality |
|------|------------------------|
| Cart abandoners (1-3 days) | 40-60% |
| Cart abandoners (7+ days) | 60-80% |
| Website visitors (generic) | 20-40% |
| Past purchasers | 15-30% |
| Dynamic product ads | 35-55% |

### RESULTS INTERPRETATION
| Incrementality Rate | Meaning | Action |
|--------------------|---------|--------|
| 80-100% | Highly incremental | Scale aggressively |
| 60-80% | Mostly incremental | Maintain/optimize |
| 40-60% | Partially incremental | Review targeting, creative |
| 20-40% | Low incrementality | Reduce spend, shift budget |
| <20% | Mostly cannibalization | Pause or restructure |

iROAS formula: Reported ROAS x Incrementality% = True incremental ROAS

### EXECUTION CHECKLIST
**Pre-test:** Define regions/audiences, set up tracking, document baselines, ensure <15% group variance, create suppression lists
**During test:** Monitor daily (don't optimize!), document external factors, keep other marketing consistent, flag contamination
**Post-test:** 7-day cooldown, calculate lift = (Test - Control) / Control, check p < 0.05, document learnings

### NEXT STEPS
1. Run Cross-Platform Comparison for baseline
2. After test: update budget allocation based on iROAS
3. Retest every 6-12 months (incrementality changes over time)

## EXECUTION STEPS

### Step 1: Gather Baseline Data
- **Meta:** `meta_get_insights(account_id, date_preset="last_90d", level="campaign")`
- **Google Ads:** `google_ads_run_gaql(customer_id=customer_id, query="SELECT campaign.id, campaign.name, metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions, metrics.conversions_value FROM campaign WHERE segments.date DURING LAST_90_DAYS ORDER BY metrics.cost_micros DESC")`
- **GA4:** `ga4_run_report(property_id, start_date="90daysAgo", end_date="today", metrics=["conversions","totalRevenue"], dimensions=["source","medium"])`

### Step 2: Determine Test Type
Based on platform, spend level, geography, and conversion volume, select from the test type table. If <200 monthly conversions, prefer platform-native lift studies.

### Step 3: Design Geo/Holdout Structure
Match test and control groups on historical performance (<15% variance). For geo tests, use pre-built splits or create custom ones based on regional similarity.

### Step 4: Calculate Power
Use conversion volume and spend data to determine MDE and required test duration. If insufficient data, recommend extending duration or using a less granular test.

### Step 5: Run Cost-Benefit Analysis
Estimate test cost (lost control revenue + analysis time) vs potential annual savings from budget reallocation. Test ROI should break even within 1-2 months.

### Step 6: Present Results
Follow OUTPUT FORMAT above EXACTLY. Fill all tables with real data from steps 1-5.

## EDGE CASES
- **Low budget (<5K/mo):** Use platform-native conversion lift instead of geo test
- **Low conversions (<100/mo):** Extend test to 8+ weeks or use revenue as primary metric
- **Peak season:** Defer testing - data too noisy (avoid Nov-Dec, major promos)
- **Recent major changes:** Wait 4+ weeks for stable baseline before testing
- **Multiple platforms:** Test one platform at a time to isolate effects
- **Small geography:** Not enough regions for geo split - use audience holdout instead