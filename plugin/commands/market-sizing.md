---
description: "Calculate Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM) for strategic budget planning and opportunity assessment. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# TAM/SAM/SOM Market Sizing Analysis

Calculate market opportunity for [specify company_name] in [specify industry].

## Overview

This workflow helps agencies and advertisers understand the true market opportunity for strategic budget planning. Combines research data with advertising platform estimates.

## Parameters
- Company: [specify company_name]
- Industry: [specify industry]
- Target Geography: Netherlands
- Target Market: [specify target_market_description]
- Product Category: Not specified
- Currency: EUR

---

## PHASE 1: Market Research

### Research Prompts

**Prompt 1 - Market Size Data:**
```
Research market size for [specify industry] in [specify target_geography]:
- Total market value ([specify currency]) 2024-2026
- Number of potential customers/businesses
- Market growth rate (CAGR)
- Key market segments
- Sources: Statista, IBISWorld, industry reports, government data
```

**Prompt 2 - Industry Benchmarks:**
```
Find advertising benchmarks for [specify industry] in [specify target_geography]:
- Average CPC/CPM by platform (Meta, Google, LinkedIn, TikTok)
- Average conversion rates
- Customer acquisition costs (CAC)
- Lifetime value benchmarks (LTV)
- Advertising spend as % of revenue (industry average)
```

**Prompt 3 - Competitor Ad Spend:**
```
Estimate competitor advertising spend in [specify industry]:
- Top 5 advertisers in the space
- Estimated monthly ad spend
- Primary advertising channels
- Share of voice estimates
```

---

## PHASE 2: Platform Audience Estimates

Use platform tools to get audience size estimates:

**Meta Ads (Reach Estimates):**
```
If Meta Ads connected, use Audience Manager reach estimates for:
- Demographics: [target demographics]
- Interests: [[specify industry]-related interests]
- Behaviors: [relevant behaviors]
- Geography: [specify target_geography]
```

**Google Ads (Keyword Planner):**
```
google_ads_run_keyword_planner(
    customer_id=customer_id,
    keywords=[[specify industry]-related keywords],
    page_url=""
)
```

**LinkedIn (Audience Estimates):**
```
For B2B, estimate LinkedIn audience:
- Job titles: [relevant titles]
- Industries: [[specify industry]]
- Company sizes: [target company sizes]
- Geography: [specify target_geography]
```

---

## PHASE 3: TAM/SAM/SOM Calculation

### Calculation Framework

```python
# TAM (Total Addressable Market)
# = Total market value if you captured 100%
# Method: Top-down (market reports) or Bottom-up (customers × value)

tam_topdown = market_report_value  # From research
tam_bottomup = total_potential_customers * average_customer_value

# SAM (Serviceable Addressable Market)
# = TAM filtered by your actual service capability
# Filters: Geography, segments you serve, channels you use

sam = tam * geographic_factor * segment_factor * channel_factor
# Example: €1B market × 10% (Netherlands) × 50% (SMB only) × 80% (digital) = €40M

# SOM (Serviceable Obtainable Market)
# = Realistic market share you can capture in 1-3 years
# Based on: Competition, resources, growth rate

som = sam * realistic_market_share
# New entrant: 1-5% of SAM
# Established player: 5-20% of SAM
# Market leader: 20-40% of SAM
```

### Advertising Budget Implications

```python
# Industry advertising benchmarks
ad_spend_to_revenue_ratio = industry_benchmark  # Typically 5-15% for growth

# Budget calculation from SOM
recommended_annual_budget = som * ad_spend_to_revenue_ratio
monthly_budget = recommended_annual_budget / 12

# CAC-based validation
max_cac = ltv * (1/3)  # LTV:CAC ratio of 3:1
conversions_needed = som / average_order_value
max_budget = conversions_needed * max_cac
```

---

## Output Format

```
================================================================================
                    MARKET SIZING ANALYSIS
                    [specify company_name] | [specify industry]
                    Geography: [specify target_geography]
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The [specify industry] market in [specify target_geography] represents a [size] opportunity.
[specify company_name]'s realistic addressable market (SOM) is estimated at [specify currency][X]M
annually, suggesting an optimal advertising budget of [specify currency][X]K-[X]K/month.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 MARKET SIZE PYRAMID
─────────────────────

┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                         TAM                                     │
│              Total Addressable Market                           │
│                 [specify currency] [X.X]B                           │
│        (Everyone who could possibly buy)                        │
│                                                                 │
│    ┌───────────────────────────────────────────────┐            │
│    │                    SAM                        │            │
│    │       Serviceable Addressable Market          │            │
│    │            [specify currency] [XXX]M              │            │
│    │     (Market you can actually reach)           │            │
│    │                                               │            │
│    │    ┌────────────────────────────────┐         │            │
│    │    │            SOM                 │         │            │
│    │    │  Serviceable Obtainable Market │         │            │
│    │    │      [specify currency] [XX]M      │         │            │
│    │    │   (Realistic 1-3 year target)  │         │            │
│    │    └────────────────────────────────┘         │            │
│    └───────────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────────────┘

📈 DETAILED BREAKDOWN
─────────────────────

### TAM (Total Addressable Market)

| Calculation Method | Value | Source |
|-------------------|-------|--------|
| Top-Down (Market Reports) | [specify currency] [X.X]B | [Source] |
| Bottom-Up (Customers × Value) | [specify currency] [X.X]B | Calculated |
| **Selected TAM** | [specify currency] [X.X]B | [Method used] |

TAM Assumptions:
- Total potential customers: [X,XXX,XXX]
- Average customer value: [specify currency] [XXX]
- Geographic scope: [Global/Regional/National]

### SAM (Serviceable Addressable Market)

| Filter Applied | Factor | Calculation |
|---------------|--------|-------------|
| Starting TAM | 100% | [specify currency] [X.X]B |
| Geographic filter ([specify target_geography]) | [X]% | [specify currency] [XXX]M |
| Segment filter ([target segments]) | [X]% | [specify currency] [XXX]M |
| Channel filter (digital-reachable) | [X]% | [specify currency] [XXX]M |
| **Final SAM** | [X.X]% of TAM | [specify currency] [XXX]M |

SAM Assumptions:
- Serviceable geography: [specify target_geography]
- Target segments: [specify target_market_description]
- Digital penetration: [X]%

### SOM (Serviceable Obtainable Market)

| Scenario | Market Share | Value | Timeline |
|----------|-------------|-------|----------|
| Conservative | [X]% of SAM | [specify currency] [X]M | Year 1 |
| Realistic | [X]% of SAM | [specify currency] [XX]M | Year 2 |
| Optimistic | [X]% of SAM | [specify currency] [XX]M | Year 3 |
| **Selected SOM** | [X]% of SAM | [specify currency] [XX]M | [Timeframe] |

SOM Assumptions:
- Current market position: [New entrant/Established/Leader]
- Competitive intensity: [High/Medium/Low]
- Growth trajectory: [X]% year-over-year

🎯 ADVERTISING AUDIENCE ESTIMATES
─────────────────────────────────

| Platform | Reachable Audience | Monthly Reach (est.) | CPM Range |
|----------|-------------------|---------------------|-----------|
| Meta (FB/IG) | [X.X]M | [X]M | [specify currency] [X-X] |
| Google (Search) | [XXX]K searches/mo | N/A | [specify currency] [X-X] CPC |
| Google (Display) | [X.X]M | [X]M | [specify currency] [X-X] |
| LinkedIn | [XXX]K | [XX]K | [specify currency] [XX-XX] |
| TikTok | [X.X]M | [XXX]K | [specify currency] [X-X] |

💰 BUDGET RECOMMENDATIONS
─────────────────────────

### Method 1: Percentage of SOM
| Metric | Value |
|--------|-------|
| SOM Value | [specify currency] [XX]M |
| Industry ad spend ratio | [X-X]% |
| **Recommended Annual Budget** | [specify currency] [X]M - [specify currency] [X]M |
| **Monthly Budget Range** | [specify currency] [XX]K - [specify currency] [XXX]K |

### Method 2: CAC-Based Budget
| Metric | Value |
|--------|-------|
| Target LTV | [specify currency] [X,XXX] |
| Target LTV:CAC Ratio | 3:1 |
| Max CAC | [specify currency] [XXX] |
| Target New Customers (Year 1) | [X,XXX] |
| **Max Annual Budget** | [specify currency] [X]M |
| **Monthly Budget** | [specify currency] [XX]K |

### Method 3: Platform-Based Minimum Viability
| Platform | Min. Monthly Budget | Expected Results |
|----------|--------------------|--------------------|
| Meta | [specify currency] [X]K | [XXX] reach/day, [XX] conversions |
| Google Search | [specify currency] [X]K | [XXX] clicks, [XX] conversions |
| LinkedIn | [specify currency] [X]K | [XX] leads |
| TikTok | [specify currency] [X]K | [XXX]K impressions |
| **Minimum Viable Total** | [specify currency] [XX]K/month |

📊 RECOMMENDED BUDGET ALLOCATION
────────────────────────────────

Based on [specify industry] benchmarks and market analysis:

| Platform | Allocation | Monthly Budget | Primary Objective |
|----------|------------|----------------|-------------------|
| Meta Ads | [XX]% | [specify currency] [X]K | [Awareness/Conversion] |
| Google Ads | [XX]% | [specify currency] [X]K | [Intent capture] |
| LinkedIn | [XX]% | [specify currency] [X]K | [B2B leads] |
| TikTok | [XX]% | [specify currency] [X]K | [Awareness/younger demo] |
| **Total** | 100% | [specify currency] [XX]K |

⚠️ CONFIDENCE LEVELS & CAVEATS
──────────────────────────────

| Estimate | Confidence | Data Quality | Notes |
|----------|------------|--------------|-------|
| TAM | [High/Medium/Low] | [Source quality] | [Caveats] |
| SAM | [High/Medium/Low] | [Assumptions] | [Caveats] |
| SOM | [High/Medium/Low] | [Based on] | [Caveats] |
| Budget Rec. | [High/Medium/Low] | [Methodology] | [Caveats] |

Key Uncertainties:
1. [Uncertainty 1 and impact]
2. [Uncertainty 2 and impact]
3. [Uncertainty 3 and impact]

📋 SOURCES & METHODOLOGY
────────────────────────
- Market data: [Sources used]
- Audience estimates: [Platforms used]
- Benchmarks: [Sources]
- Calculation methodology: [Top-down/Bottom-up/Hybrid]

📅 RECOMMENDED REVIEW CADENCE
─────────────────────────────
- Quarterly: Review SOM assumptions based on actual performance
- Annually: Full market sizing refresh
- Trigger: Major market shift or new competitor entry
```

---

## Methodology Notes

### Top-Down vs Bottom-Up

**Top-Down (Use when):**
- Market reports available
- Quick estimation needed
- High-level planning

**Bottom-Up (Use when):**
- Specific customer segments known
- Platform audience data available
- Detailed planning needed

### Industry Ad Spend Benchmarks

| Industry | Ad Spend as % Revenue |
|----------|----------------------|
| E-commerce | 10-15% |
| SaaS | 20-40% (growth stage) |
| Professional Services | 5-10% |
| Retail | 3-5% |
| Finance | 5-8% |
| Healthcare | 3-6% |
| Travel | 8-12% |

Adjust based on:
- Growth stage (higher for growth, lower for mature)
- Competitive intensity (higher in competitive markets)
- Margin structure (higher margins = more ad budget room)