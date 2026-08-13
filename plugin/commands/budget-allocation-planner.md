---
description: "Forward-looking budget planning with scenario modeling (conservative/realistic/aggressive). Integrates market sizing data, competitive share of voice analysis, and platform-specific budget thresholds. Outputs optimal budget distribution across channels with confidence levels and expected ROI ranges. Different from budget-pacing-monitor which tracks actual spend vs. budget. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Strategic Budget Planning & Scenario Modeling

Develop a budget allocation plan for [specify company_name] ([specify industry]) with three-scenario analysis.

**Planning Period:** Q1 2026
**Total Budget:** EUR30,000
**Objective:** growth

> Conditional: if historical_roas
**Historical ROAS:** [specify historical_roas]x

> Conditional: if target_cpa
**Target CPA:** EUR[specify target_cpa]

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### EXECUTIVE SUMMARY
**Recommended Scenario:** [Conservative/Realistic/Aggressive]

### SCENARIO COMPARISON
| Metric | Conservative (70%) | Realistic (100%) | Aggressive (130%) |
|--------|-------------------|------------------|-------------------|
| Quarterly Budget | [amount] | [amount] | [amount] |
| Expected ROAS | X.Xx | X.Xx | X.Xx |
| Expected Conversions | XXX | XXX | XXX |
| Market Share Impact | +X% | +X% | +X% |
| Risk Level | Low | Medium | High |
| Confidence | 85% | 70% | 55% |

### RECOMMENDED CHANNEL ALLOCATION (selected scenario)
| Channel | % | Monthly Budget | Role | Target KPI |
|---------|---|---------------|------|-----------|
| [Channel] | XX% | [amount] | [Conversion/Prospecting/Awareness] | [CPA/ROAS] |
| **Total** | 100% | **[amount]** | - | **Blended: [metric]** |

### MONTHLY PHASING
| Month | Total | Google | Meta | Other | Focus |
|-------|-------|--------|------|-------|-------|
| M1 (30%) | [amount] | [amount] | [amount] | [amount] | Testing & baseline |
| M2 (35%) | [amount] | [amount] | [amount] | [amount] | Optimize & scale |
| M3 (35%) | [amount] | [amount] | [amount] | [amount] | Full scale |

### REALLOCATION TRIGGERS
| Trigger | Action |
|---------|--------|
| ROAS > 150% target for 2 weeks | +20% to that channel from underperformers |
| ROAS < 50% target for 2 weeks | -30% from that channel, redistribute |
| Seasonal peak approaching | +20-30% overall during peak |

### NEXT STEPS
1. Approve scenario
2. Set up tracking and attribution
3. Create campaign structures
4. Schedule weekly budget reviews

## EXECUTION STEPS

### Step 1: Discover Accounts & Current Performance
- `meta_list_ad_accounts()` then `meta_get_insights(account_id="...", date_preset="last_30d", level="account")`
- `google_ads_list_accounts()` then `google_ads_run_gaql(customer_id="...", query="SELECT metrics.cost_micros, metrics.conversions, metrics.conversions_value FROM customer WHERE segments.date DURING LAST_30_DAYS")`
- `linkedin_list_ad_accounts()` then `linkedin_get_analytics(account_id="...", start_date="30_DAYS_AGO", end_date="TODAY")`
- `tiktok_get_advertiser_info()` then `tiktok_get_report(start_date="30_DAYS_AGO", end_date="TODAY", level="account")`
- `ga4_list_properties()` then `ga4_run_report(property_id="...", start_date="30daysAgo", end_date="yesterday", metrics=["sessions","conversions","totalRevenue"], dimensions=["sessionDefaultChannelGroup"])`

### Step 2: Budget Classification & Constraints

**Budget levels and channel limits:**
| Monthly Budget | Max Channels | Strategy |
|---------------|-------------|----------|
| <3K | 1 channel | Single-channel focus, validate PMF |
| 3-5K | 2 channels | Core + retargeting only |
| 5-10K | 2-3 channels | Primary 50%, secondary 30%, testing 20% |
| 10K+ | 3-4 channels | Full multi-channel viable |

**Platform minimum viable budgets:**
| Channel | Minimum/mo | Why | Sweet Spot |
|---------|-----------|-----|-----------|
| Google Search | 500 | Algorithm learning volume | 2-5K |
| Meta | 1,000 | Learning phase needs ~50 conv/week | 3-8K |
| LinkedIn | 2,000 | High CPCs require scale | 5-10K |
| TikTok | 1,000 | Creative testing needs budget | 3-8K |

### Step 3: Build Three Scenarios

**Conservative (70% budget):** Bottom-funnel only. Google Search (50%) + Meta retargeting (30%) + brand protection (20%). No new channel testing.

**Realistic (100% budget):** Balanced prospecting/retargeting (70/30). Core channels + selective testing. For growth/conversion: Google Search 35% + Meta 30% + Shopping/PMax 20% + testing 15%. For awareness: Meta 40% + TikTok 25% + YouTube 20% + Search 15%.

**Aggressive (130% budget):** Heavy prospecting (80/20). Multi-channel: Meta 30% + Google 25% + TikTok 20% + LinkedIn 15% + YouTube 10%. Warning: ROAS may temporarily drop as you invest in upper-funnel.

### Step 4: SOV & Market Context

**SOV-SOM Rule (Ehrenberg-Bass):**
- Maintain share: SOV = SOM
- Grow share: SOV should exceed SOM by 5-15pp
- Each 10pp ESOV = ~0.5% market share growth/year

**Expected KPIs by channel:**
| Channel | CPM | CPC | CTR | CVR | CPL (B2B) | ROAS (E-com) |
|---------|-----|-----|-----|-----|-----------|-------------|
| Meta | 8-15 | 0.50-2 | 1-2% | 2-5% | 30-80 | 3-6x |
| Google Search | 15-40 | 1-5 | 2-5% | 3-8% | 40-100 | 4-8x |
| LinkedIn | 30-60 | 3-8 | 0.4-0.8% | 2-6% | 50-150 | N/A |
| TikTok | 5-12 | 0.30-1.50 | 1-3% | 1-3% | 40-100 | 2-5x |

Seasonality: Q4/Black Friday CPMs +30-100%. Q1 CPMs -10-20%. Summer -5-15%.

### Step 5: Present Results
Follow OUTPUT FORMAT above. Recommend one scenario with rationale based on company context, risk tolerance, and growth goals.

## EDGE CASES
- No ad accounts connected: Base recommendations on industry, objective, and budget benchmarks only
- Only 1 platform connected: Recommend as primary, suggest others to connect
- Budget below all minimums (<500/mo): Recommend organic-first strategy, state minimum to start paid
- All historical metrics are 0: Flag tracking issue, use benchmark-based recommendations
- API error on a platform: Skip it, note the error, recommend based on remaining data