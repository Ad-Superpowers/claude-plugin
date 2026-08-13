---
description: "Analyze lead quality across platforms with LinkedIn-specific benchmarks. Compare CPL by industry, MQL/SQL rates, Lead Gen Forms vs Landing Pages, and LTV:CAC framework for B2B. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# B2B Lead Quality Analyzer

Deep analysis of B2B lead generation with **LinkedIn-specific benchmarks** and quality metrics. LinkedIn CPC is 3-5x higher than Meta/Google, but B2B audience quality often compensates — this workflow measures whether it actually does.

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### LEAD FUNNEL OVERVIEW
| Stage | Volume | Rate | Benchmark | Status |
|-------|--------|------|-----------|--------|
| Total Leads | XXX | - | - | - |
| MQLs | XX | XX% | 31% | OK/Above/Below |
| SQLs | XX | XX% of MQL | 20-35% | OK/Above/Below |
| Opportunities | XX | XX% of SQL | 35-50% | OK/Above/Below |

B2B sales cycle context: Avg LinkedIn-sourced cycle 200+ days. Multi-touch attribution: 6-12 touches average. Do not judge CPL without SQL rate data.

### LINKEDIN-SPECIFIC METRICS
| Metric | Your Value | Industry Benchmark | Status |
|--------|------------|-------------------|--------|
| CPL | EUR XX | EUR [industry avg] | OK/Above/Below |
| CPC | EUR XX | EUR 4-7 (B2B avg) | OK/Above/Below |
| CTR | X.XX% | 0.35-0.55% (Sponsored Content) | OK/Above/Below |
| Form CVR | XX% | 6-10% (Lead Gen Forms) | OK/Above/Below |
| SQL Rate | XX% | 10-20% (average) | OK/Above/Below |
| Cost/SQL | EUR XXX | CPL / SQL rate | OK/Above/Below |

### LEAD GEN FORMS vs LANDING PAGES
| Source | Leads | CPL | SQL Rate | Cost/SQL | Recommendation |
|--------|-------|-----|----------|----------|----------------|
| Lead Gen Forms | XX | EUR XX | XX% | EUR XXX | Volume or Quality call |
| Landing Pages | XX | EUR XX | XX% | EUR XXX | Volume or Quality call |

When to use which: Lead Gen Forms for volume, TOFU/MOFU content, mobile. Landing Pages for quality, BOFU demos, complex qualification.

### PLATFORM QUALITY COMPARISON
| Platform | Leads | CPL | SQL Rate | Cost/SQL | Quality Score (1-10) |
|----------|-------|-----|----------|----------|---------------------|
| LinkedIn | XX | EUR XX | XX% | EUR XXX | X |
| Google | XX | EUR XX | XX% | EUR XXX | X |
| Meta | XX | EUR XX | XX% | EUR XXX | X |

### LTV:CAC ANALYSIS
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Avg Contract Value | EUR XX,XXX | - | - |
| Customer Lifespan | X years | - | - |
| Estimated LTV | EUR XX,XXX | - | - |
| CAC (from ads) | EUR X,XXX | - | - |
| LTV:CAC Ratio | X:1 | 3:1 - 5:1 | OK/Above/Below |

Interpretation: <1:1 loss-making | 1-3:1 break-even to marginal | 3-5:1 healthy target | 5-7:1 excellent | >7:1 potentially under-investing.

### RECOMMENDATIONS
**Budget Reallocation:**
- LinkedIn: Increase/Decrease/Maintain — reason based on SQL rate
- Google: Increase/Decrease/Maintain — reason
- Meta: Increase/Decrease/Maintain — reason

**Quality Improvements:**
1. [Lead Gen Form field changes if SQL rate <15%]
2. [Landing Page test for BOFU campaigns if quality is priority]
3. [Speed-to-lead: respond <1hr for 53% conv rate vs 17% at 24hr+]

**Lead Gen Form Optimization:**
- Current fields: X
- Recommendation: Add/Remove field to improve SQL rate
- Expected impact: +X% SQL rate or +X% volume

## EXECUTION STEPS

### Step 1: Discover Accounts
- `meta_list_ad_accounts()`
- `google_ads_list_accounts()`
- `linkedin_list_ad_accounts()`

### Step 2: Gather Lead Data

**LinkedIn:** `linkedin_get_analytics(account_id="FROM_STEP_1", start_date="YYYY-MM-DD", end_date="YYYY-MM-DD", fields=["impressions","clicks","costInLocalCurrency","externalWebsiteConversions","leadGenerationMailContactInfoShares"])`

**Google Ads:** `google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT campaign.id, campaign.name, campaign.status, metrics.impressions, metrics.clicks, metrics.ctr, metrics.average_cpc, metrics.cost_micros, metrics.conversions, metrics.conversions_value FROM campaign WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC")`

Filter Google campaigns to lead-focused ones (search for "lead", "demo", "contact", "sign up" in conversion actions).

**Meta:** `meta_get_insights(account_id="FROM_STEP_1", date_preset="last_30d", level="campaign", fields=["campaign_name","spend","impressions","clicks","actions","cost_per_action_type","cpc","ctr","cpm"])`

Filter Meta campaigns to those with lead-type actions (lead, complete_registration, contact).

### Step 3: Apply LinkedIn Benchmarks

**CPL Benchmarks by Industry:**
| Industry | Poor | Average | Good | Excellent |
|----------|------|---------|------|-----------|
| Finance & Insurance | >EUR 120 | EUR 90-120 | EUR 60-90 | <EUR 60 |
| SaaS / Software | >EUR 120 | EUR 80-120 | EUR 50-80 | <EUR 50 |
| Professional Services | >EUR 100 | EUR 70-100 | EUR 45-70 | <EUR 45 |
| Healthcare | >EUR 150 | EUR 100-150 | EUR 70-100 | <EUR 70 |
| Manufacturing | >EUR 130 | EUR 90-130 | EUR 60-90 | <EUR 60 |
| Education | >EUR 80 | EUR 60-80 | EUR 40-60 | <EUR 40 |
| Marketing / Agencies | >EUR 120 | EUR 80-120 | EUR 50-80 | <EUR 50 |

**CPL context by deal size:**
- Enterprise (EUR 50k+ ACV): CPL EUR 150-300+ acceptable
- Mid-market (EUR 10-50k ACV): CPL EUR 80-150 target
- SMB (EUR 5k ACV): CPL <EUR 50 target
- Freemium SaaS: CPL <EUR 30 ideal

**Lead Quality Benchmarks (LinkedIn-specific):**
| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| MQL to SQL Rate | <10% | 10-20% | 20-35% | >35% |
| SQL to Opportunity | <20% | 20-35% | 35-50% | >50% |
| Opportunity to Close | <15% | 15-25% | 25-40% | >40% |
| Lead Gen Form SQL Rate | <8% | 8-15% | 15-25% | >25% |
| Landing Page SQL Rate | <15% | 15-30% | 30-45% | >45% |

**Lead Gen Forms vs Landing Pages (expected performance):**
| Metric | Lead Gen Forms | Landing Pages |
|--------|----------------|---------------|
| Conversion Rate | 10-13% | 4-6% |
| Cost per Lead | 15-25% lower | Higher |
| SQL Rate (quality) | 20-40% lower | Higher |
| Mobile Experience | Excellent | Variable |

### Step 4: Calculate Quality Metrics

```
Quality-adjusted CPL = total_spend / mql_count (cost per MQL, not just CPL)
Platform efficiency = sql_rate * (1 / quality_cpl) — higher = better
LTV = avg_contract_value * customer_lifespan_years * gross_margin
CAC = total_spend / customers_acquired
LTV:CAC ratio = LTV / CAC — target 3:1 to 5:1
```

If CRM data is unavailable, score on platform data only: use CPL, CTR, and conversion rate benchmarks.

### Step 5: Present Results
Follow OUTPUT FORMAT above EXACTLY. Use SaaS / Software benchmarks. Flag any metric more than 1 tier below benchmark.

## EDGE CASES
- No LinkedIn account connected: Analyze Google + Meta only, note LinkedIn is recommended for B2B
- No CRM data available: Score on platform metrics only (CPL, CTR, CVR vs benchmarks), skip MQL/SQL funnel and LTV:CAC
- All leads from one platform: Full analysis for that platform, recommend testing a second channel
- Zero conversions: Flag as tracking issue or insufficient budget, recommend minimum EUR 2k/mo for LinkedIn B2B
- B2C account detected (ecommerce/ROAS focus): Redirect to ecommerce-roas-optimizer workflow instead
- Very low volume (<20 leads): Note statistical insignificance, recommend extending date range to 90 days
- API error on one platform: Note the error, continue with remaining platforms