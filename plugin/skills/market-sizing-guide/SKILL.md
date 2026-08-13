---
name: market-sizing-guide
description: "This skill should be used when the user asks to \"calculate TAM SAM SOM\", \"size my market for ad budget\", \"plan budget for a new market\", mentions \"how much should I spend on ads\", \"addressable audience sizing\", or \"market opportunity assessment\". Do NOT use for: channel-level budget allocation (use channel-selection-framework), competitor spend estimation (use competitor-analysis-toolkit), or cross-platform attribution (use attribution-reconciler)."
---
# Market Sizing Guide for Advertising Budget Planning

## Purpose

Help advertisers and agencies calculate realistic market opportunity to inform strategic budget decisions. Moves beyond "what can we afford" to "what should we invest based on market size."

## When to Use This Skill

Invoke when user mentions:
- **Market sizing:** "How big is the market for X?"
- **Budget planning:** "How much should we spend on ads?"
- **TAM/SAM/SOM:** Any reference to these terms
- **New market entry:** "We're launching in a new country/segment"
- **Opportunity assessment:** "Is this market worth pursuing?"
- **Strategic planning:** Budget allocation across markets

---

## Core Framework: TAM → SAM → SOM

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                               TAM                                           │
│                    Total Addressable Market                                 │
│            "If we captured 100% of everyone who could buy"                  │
│                                                                             │
│         ┌─────────────────────────────────────────────────────┐             │
│         │                      SAM                            │             │
│         │           Serviceable Addressable Market            │             │
│         │   "Market we can actually reach with our product"   │             │
│         │                                                     │             │
│         │      ┌─────────────────────────────────────┐        │             │
│         │      │              SOM                    │        │             │
│         │      │    Serviceable Obtainable Market    │        │             │
│         │      │  "Realistic share we can capture"   │        │             │
│         │      │         (1-3 year horizon)          │        │             │
│         │      └─────────────────────────────────────┘        │             │
│         └─────────────────────────────────────────────────────┘             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Definitions

| Term | Definition | Example |
|------|------------|---------|
| **TAM** | Total market demand for a product/service globally or in largest scope | All e-commerce sales in Europe |
| **SAM** | Portion of TAM that your business model can serve | E-commerce in Netherlands that shops online |
| **SOM** | Realistic market share you can capture in 1-3 years | Your realistic sales given competition, resources |

---

## Calculation Methods

### Method 1: Top-Down (Market Reports)

```
TAM = Market research report value
SAM = TAM × Geographic filter × Segment filter × Channel filter
SOM = SAM × Realistic market share %
```

**Best for:**
- Quick estimates
- Well-researched industries
- Investor presentations

**Sources:**
- Statista, IBISWorld, Euromonitor
- Industry associations
- Government statistics (CBS, Eurostat)
- Analyst reports

**Example:**
```
TAM: Dutch e-commerce market = €35B (Statista 2025)
SAM: Fashion segment = €5.3B (15% of e-commerce)
     × Online-first shoppers = €3.7B (70%)
     × Target demographic (25-45) = €1.85B (50%)
SOM: New brand, year 1 = €18.5M (1% market share)
```

### Method 2: Bottom-Up (Customer Calculation)

```
TAM = Total potential customers × Average transaction value × Purchase frequency
SAM = TAM filtered by serviceable segments
SOM = SAM × Capture rate
```

**Best for:**
- Niche markets
- New categories
- When market reports don't exist

**Example:**
```
TAM:
  - Dutch SMBs: 1.2M businesses
  - Need marketing software: 40% = 480,000
  - Average spend: €2,400/year
  - TAM = 480,000 × €2,400 = €1.15B

SAM:
  - Digital-first SMBs: 60% = 288,000
  - Can afford €200+/mo: 50% = 144,000
  - SAM = 144,000 × €2,400 = €345M

SOM:
  - Year 1 realistic: 0.5% = 720 customers
  - SOM = 720 × €2,400 = €1.73M
```

### Method 3: Hybrid (Recommended for Advertising)

Combine top-down market data with bottom-up platform audience data.

```
Step 1: Get top-down market size (€ value)
Step 2: Get platform audience sizes (Meta, Google, LinkedIn)
Step 3: Cross-validate and triangulate
Step 4: Apply advertising-specific filters
```

---

## Advertising-Specific Calculations

### Platform Audience Estimates

| Platform | Best For | Audience Data Available |
|----------|----------|------------------------|
| Meta Ads Manager | B2C, broad reach | Reach estimates by demographics, interests |
| Google Keyword Planner | Search intent | Monthly search volume |
| LinkedIn Campaign Manager | B2B | Professional demographics |
| TikTok Ads Manager | Younger demographics | Interest-based reach |

### From Market Size to Ad Budget

```python
# Method 1: Percentage of Revenue Method
advertising_budget = target_revenue × industry_ad_ratio

# Method 2: CAC-Based Method
max_budget = target_customers × max_allowable_CAC

# Method 3: Market Share Method
required_share_of_voice = target_market_share × 1.5  # Rule of thumb
budget = market_total_ad_spend × required_share_of_voice
```

### Industry Advertising Ratios

| Industry | Ad Spend as % of Revenue | Notes |
|----------|-------------------------|-------|
| E-commerce (growth) | 10-20% | Higher for new brands |
| E-commerce (mature) | 5-10% | Established brands |
| SaaS (growth stage) | 20-40% | Very high for growth |
| SaaS (mature) | 10-15% | More efficient |
| Professional Services | 5-10% | Relationship-driven |
| Retail (traditional) | 3-5% | Lower margins |
| Finance/Insurance | 5-8% | Regulated, longer cycles |
| Healthcare | 3-6% | Regulated |
| Travel/Hospitality | 8-12% | Seasonal, competitive |
| Consumer Goods | 8-15% | Brand-dependent |
| Education | 5-10% | Cyclical |

### Share of Voice (SOV) Rule

**Ehrenberg-Bass Institute finding:** To grow market share, your share of voice (SOV) must exceed your current share of market (SOM).

```
Excess Share of Voice (ESOV) = SOV - SOM

For each 10 points of ESOV, expect ~0.5% market share growth per year

Example:
- Current market share: 5%
- Target market share: 8% in 3 years
- Required ESOV: (8-5) / 0.5 / 10 × 3 ≈ 20 points
- Required SOV: 5% + 20% = 25% of category ad spend
```

---

## SAM Filtering Factors

### Geographic Filters

| Region | Typical % of Global | Notes |
|--------|-------------------|-------|
| North America | 25-35% | Highest spend per capita |
| Europe (Western) | 20-25% | Strong digital adoption |
| Netherlands | 1-2% of Europe | ~€1T GDP |
| UK | 15-20% of Europe | Largest EU market (was) |
| DACH | 25-30% of Europe | Germany dominates |
| Nordics | 5-8% of Europe | High digital maturity |

### Segment Filters

| Filter Type | Example Factors |
|-------------|-----------------|
| B2B vs B2C | 30% of market is B2B |
| Age demographics | 25-44 age group = 35% of adults |
| Income level | High income = top 20% |
| Tech adoption | Digitally active = 70-80% |
| Purchase intent | Active shoppers = 10-20% of aware |

### Channel Filters

| Factor | Description | Typical % |
|--------|-------------|-----------|
| Digital reachable | Can be reached via digital ads | 70-90% |
| Platform presence | On specific platform (e.g., LinkedIn for B2B) | 30-60% |
| Mobile vs desktop | Mobile-first audience | 60-70% |

---

## SOM Estimation Guidelines

### Market Share by Company Stage

| Company Stage | Typical SOM (% of SAM) | Factors |
|---------------|----------------------|---------|
| New entrant (Year 1) | 0.1-1% | Brand awareness, resources |
| Growing (Year 2-3) | 1-5% | Proven product-market fit |
| Established | 5-15% | Known brand, loyal customers |
| Market leader | 20-40% | Category dominance |
| Monopoly/duopoly | 40-70% | Few viable alternatives |

### SOM Adjustment Factors

Increase SOM estimate if:
- Unique value proposition (+0.5-2%)
- First mover in niche (+1-3%)
- Strong brand recognition (+1-2%)
- Superior product/service (+0.5-1%)
- Aggressive pricing (+0.5-1%)
- Strong distribution (+0.5-1%)

Decrease SOM estimate if:
- Entering established market (-1-2%)
- Strong incumbent competition (-0.5-1%)
- Limited differentiation (-0.5-1%)
- Resource constraints (-0.5-1%)
- Regulatory barriers (-0.5-2%)

---

## Advertising Budget Frameworks

### Framework 1: Objective-Based Budget

```
Budget = Target Conversions × Expected CPA

Where:
- Target Conversions = SOM / Average Order Value
- Expected CPA = Industry benchmark × (1 + new brand premium)
```

**New brand CPA premiums:**
- Brand new: +50-100%
- Some awareness: +20-50%
- Established: 0%
- Market leader: -10-20%

### Framework 2: Growth Equation

```
Revenue Growth = Ad Spend × ROAS

Target Spend = Target Revenue Growth / Target ROAS

Example:
- Current revenue: €1M
- Target growth: €500K (50% growth)
- Target ROAS: 4x
- Required ad spend: €500K / 4 = €125K
```

### Framework 3: LTV:CAC Ratio

```
Maximum CAC = LTV × (1/3)  # For healthy 3:1 ratio
Budget = Target New Customers × Maximum CAC

Example:
- LTV: €1,200
- Maximum CAC: €400 (3:1 ratio)
- Target new customers: 500
- Maximum budget: €200,000
```

### Framework 4: Competitive Parity

```
Required Budget = Total Market Ad Spend × Target SOV

Example:
- Market total ad spend: €50M/year
- Current market share: 5%
- Target SOV: 10% (2x market share)
- Required budget: €5M/year
```

---

## Confidence Levels & Caveats

### Data Quality Indicators

| Source Type | Confidence | Notes |
|-------------|------------|-------|
| Government statistics | High | Reliable but often lagging |
| Paid research reports | Medium-High | Quality varies |
| Platform estimates | Medium | Often inflated |
| Industry associations | Medium | May have bias |
| Competitor estimates | Low-Medium | Often guesswork |
| Your own calculations | Variable | Depends on assumptions |

### Common Mistakes to Avoid

1. **TAM inflation** - Using unrealistic total market
2. **Forgetting filters** - Not narrowing to SAM properly
3. **Optimistic SOM** - Overestimating capture rate
4. **Ignoring competition** - Not accounting for SOV requirements
5. **Static thinking** - Not accounting for market changes

### Uncertainty Ranges

Always present ranges, not point estimates:

```
Conservative: TAM × 0.7 → SAM × 0.7 → SOM × 0.7
Realistic:    TAM × 1.0 → SAM × 1.0 → SOM × 1.0
Optimistic:   TAM × 1.2 → SAM × 1.2 → SOM × 1.3
```

---

## Output Template

When calculating market size, provide:

```
## Market Sizing Analysis: [Company/Product]

### TAM (Total Addressable Market)
- **Value:** €[X]B (Source: [Source])
- **Methodology:** [Top-down/Bottom-up/Hybrid]
- **Assumptions:** [List key assumptions]
- **Confidence:** [High/Medium/Low]

### SAM (Serviceable Addressable Market)
- **Value:** €[X]M ([X]% of TAM)
- **Filters Applied:**
  1. Geographic: [Filter] → [X]%
  2. Segment: [Filter] → [X]%
  3. Channel: [Filter] → [X]%
- **Confidence:** [High/Medium/Low]

### SOM (Serviceable Obtainable Market)
- **Value:** €[X]M ([X]% of SAM)
- **Timeline:** [X] years
- **Rationale:** [Why this market share is achievable]
- **Confidence:** [High/Medium/Low]

### Advertising Budget Implications

| Method | Recommended Budget | Calculation |
|--------|-------------------|-------------|
| % of SOM | €[X]/year | SOM × [X]% ad ratio |
| CAC-based | €[X]/year | [X] customers × €[X] CAC |
| SOV-based | €[X]/year | Market spend × [X]% SOV |
| **Recommended** | €[X]/month | [Rationale] |

### Caveats
- [Caveat 1]
- [Caveat 2]
- [Caveat 3]
```

---

## Quick Reference: Netherlands Market Data (2025)

| Metric | Value | Source |
|--------|-------|--------|
| Population | 17.9M | CBS |
| GDP | ~€1T | CBS |
| Internet users | 97% | Eurostat |
| E-commerce market | €35B | Ecommerce Europe |
| Digital ad spend | €3.5B | IAB NL |
| Mobile ad share | 65% | IAB NL |
| SMB count | 1.2M | KVK |
| B2B market size | €350B | Estimate |

---

## Optional: Enrich with Live Data

If the user has connected a Google Ads account, use keyword volume as a demand-side proxy to validate market size estimates:

```python
# Pull impression data for core category keywords as a market demand signal
google_ads_run_gaql(
    customer_id="YOUR_CUSTOMER_ID",
    query="SELECT search_term_view.search_term, metrics.impressions, metrics.clicks FROM search_term_view WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.impressions DESC LIMIT 30"
)
```

High impression volume with low competition (low CPCs) = under-served market. High volume with high CPCs = competitive market where you need strong differentiation. Use this to sense-check the TAM/SAM estimates in the framework above.

*Last updated: February 2026*
*Sources: Statista, Euromonitor, IAB, CBS Netherlands, Ecommerce Europe*
