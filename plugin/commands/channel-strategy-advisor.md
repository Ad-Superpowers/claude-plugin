---
description: "AI-powered channel selection advisor that matches campaign objectives with optimal platform mix. Analyzes audience fit, platform strengths, funnel stage requirements, and budget constraints to recommend the ideal channel strategy. Includes budget allocation suggestions and expected performance benchmarks per channel. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Channel Strategy Advisor

Recommend the optimal advertising channel mix for [specify company_name] ([specify industry]) with objective **[specify primary_objective]** and EUR10,000/month budget. Geography: Netherlands / Europe.
> Conditional: if target_audience
 Audience: [specify target_audience].
> Conditional: if product_type
 Product type: [specify product_type].
> Conditional: if existing_channels
 Current channels: [specify existing_channels].
> Conditional: if sales_cycle
 Sales cycle: [specify sales_cycle].

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

| Channel | Priority | Allocation % | Monthly Budget | Role | Expected KPI |
|---------|----------|-------------|----------------|------|-------------|
| [Channel] | 1 | XX% | XXXX | [Conversion/Prospecting/Awareness] | [CPA XX / ROAS Xx / CPM XX] |
| [Channel] | 2 | XX% | XXXX | ... | ... |
| [Channel] | 3 | XX% | XXXX | ... | ... |
| **Total** | - | 100% | **XXXX** | - | **Blended: [metric]** |

For each recommended channel, include:
- Why it fits this objective + audience
- Campaign types to run
- Expected results range
- Success criteria / KPI targets

Also include:
- Channels NOT recommended and why
- Implementation roadmap (Week 1-2: Launch, Week 3-4: Optimize, Month 2: Scale)

## EXECUTION STEPS

### Step 1: Discover Connected Accounts
- `meta_list_ad_accounts()` -- check Meta availability
- `google_ads_list_accounts()` -- check Google Ads availability
- `linkedin_list_ad_accounts()` -- check LinkedIn availability
- `tiktok_get_advertiser_info()` -- check TikTok availability
- `ga4_list_properties()` -- check GA4 availability

### Step 2: Gather Current Performance (if accounts exist)
Pull last 30 days from each connected platform to understand current channel performance:

**Meta:** `meta_get_insights(account_id="FROM_STEP_1", date_preset="last_30d", level="account")`
**Google Ads:** `google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT metrics.cost_micros, metrics.conversions, metrics.conversions_value, metrics.impressions, metrics.clicks FROM customer WHERE segments.date DURING LAST_30_DAYS")`
**LinkedIn:** `linkedin_get_analytics(account_id="FROM_STEP_1", start_date="30_DAYS_AGO", end_date="TODAY")`
**TikTok:** `tiktok_get_report(start_date="30_DAYS_AGO", end_date="TODAY", level="account")`

### Step 3: Analyze and Recommend

**3a. Objective-Channel Fit:**
- Awareness: Meta (broad reach, CPM 8-15), TikTok (viral, CPM 5-12), YouTube/Display
- Consideration: Meta (engagement), Google Search (intent), LinkedIn (B2B research)
- Conversion/Lead Gen: Google Search (highest intent), Meta (retargeting + lookalikes), LinkedIn (B2B leads, CPL 50-150)
- App Install: Meta + TikTok app campaigns, Google App Campaigns

**3b. Audience-Channel Fit:**
- B2B: LinkedIn primary (job title targeting), Google Search (research intent), Meta for retargeting
- D2C/E-commerce: Meta + Google Shopping primary, TikTok for discovery
- Local: Google Search/Maps primary, Meta for local awareness
- Age <35: TikTok strongest; Age 35+: Meta + Google strongest

**3c. Budget Constraints (minimum viable monthly budgets):**
- Meta: min 1,000 (learning phase needs ~50 conv/week)
- Google Search: min 500 (2,000+ for competitive verticals)
- LinkedIn: min 2,000 (high CPCs)
- TikTok: min 1,000 (creative fatigue 4x faster than Meta)

If total budget <3,000: focus on 1 channel only.
If 3,000-5,000: max 2 channels.
If 5,000-10,000: 2-3 channels.
If 10,000+: full multi-channel viable.

**3d. Industry Benchmarks (use for expected KPIs):**

| Metric | Meta | Google Search | LinkedIn | TikTok |
|--------|------|--------------|----------|--------|
| CPM | 8-15 | 15-40 | 30-60 | 5-12 |
| CPC | 0.50-2.00 | 1.00-5.00 | 3.00-8.00 | 0.30-1.50 |
| CTR | 1.0-2.0% | 2.0-5.0% | 0.4-0.8% | 1.0-3.0% |
| CVR | 2-5% | 3-8% | 2-6% | 1-3% |
| CPL (B2B) | 30-80 | 40-100 | 50-150 | 40-100 |
| ROAS (E-com) | 3-6x | 4-8x | N/A | 2-5x |

**3e. Seasonality (adjust if relevant):**
Q4/Black Friday: CPMs +30-100%. Q1: CPMs -10-20%. Summer: CPMs -5-15%.

### Step 4: Present Results
Follow the OUTPUT FORMAT section above EXACTLY. Include the prioritized channel table, per-channel rationale, excluded channels, and implementation roadmap.

## EDGE CASES
- If no ad accounts connected: Base recommendations on industry, objective, audience, and budget only. Use benchmarks above.
- If only 1 platform connected: Recommend it as primary if it fits. Suggest others to connect.
- If budget is below all channel minimums (<500/mo): Recommend organic-first strategy. Suggest minimum budget to start paid.
- If API error on a platform: Skip it, note the error, recommend based on remaining data.
- If all metrics are 0: Flag as potential tracking issue, recommend based on benchmarks.