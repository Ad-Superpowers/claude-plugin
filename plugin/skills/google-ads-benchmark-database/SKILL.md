---
name: google-ads-benchmark-database
description: "This skill should be used when the user asks to \"compare performance to industry benchmarks\", \"set KPI targets for a new account\", \"estimate CPA or ROAS by industry\", or mentions \"Google Ads benchmarks\", \"seasonal CPC trends\", or \"industry averages\". Do NOT use for: real-time performance troubleshooting (use performance-troubleshooter), Quality Score optimization (use quality-score-optimizer), or campaign structure decisions (use campaign-structure-advisor)."
---
# Benchmark Database

Complete database with Google Ads KPI benchmarks per industry, campaign type, and region for performance comparison and goal setting.

## How to Pull Live Account Data First

Before applying benchmarks, pull actual account data via MCP to ground the comparison:

```
google_ads_run_gaql(query="
  SELECT campaign.name, campaign.advertising_channel_type,
         metrics.clicks, metrics.impressions, metrics.ctr,
         metrics.average_cpc, metrics.conversions,
         metrics.cost_per_conversion, metrics.conversions_value,
         metrics.cost_micros
  FROM campaign
  WHERE segments.date DURING LAST_30_DAYS
    AND campaign.status = 'ENABLED'
  ORDER BY metrics.cost_micros DESC
  LIMIT 20
")
```

Compare the output against the benchmarks below to identify gaps.

## Disclaimer

```
BENCHMARK DISCLAIMER
════════════════════

These benchmarks are compiled from:
├── WordStream/LOCALiQ "Google Ads Benchmarks 2025" (Sep 2025, ~16K campaigns)
├── LOCALiQ "Search Advertising Benchmarks for 2025" (updated Feb 2026)
├── WordStream "Conversion Rate Benchmarks" (updated Nov 2025)
├── Tinuiti "Digital Ads Benchmark Report Q4 2025" (Jan 2026)
└── Agency experience and case studies

IMPORTANT NUANCES:
├── Benchmarks are AVERAGES
├── Top 10% performers do 2-3x better
├── Bottom 10% performers do 2-3x worse
├── Your results depend on:
│   ├── Landing page quality
│   ├── Brand awareness
│   ├── Product/market fit
│   ├── Competition in your niche
│   └── Account history

USE FOR:
├── Initial target setting (new account)
├── Performance check (significant deviations)
├── Budget planning (CPA estimates)
└── Client benchmarking

DO NOT USE AS:
├── Absolute truth
├── Guarantee of results
└── Direct comparison without context
```

## Search Campaign Benchmarks

### CTR Benchmarks per Industry

```
SEARCH CTR BENCHMARKS (2025/2026)
═════════════════════════════════

┌────────────────────────────┬─────────┬─────────┬─────────┐
│ INDUSTRY                   │ AVG CTR │ TOP 25% │ TOP 10% │
├────────────────────────────┼─────────┼─────────┼─────────┤
│ Dating & Personals         │ 6.05%   │ 8.5%    │ 11%+    │
│ Travel & Hospitality       │ 4.68%   │ 6.5%    │ 9%+     │
│ Advocacy                   │ 4.41%   │ 6.0%    │ 8%+     │
│ Auto                       │ 4.00%   │ 5.5%    │ 7%+     │
│ Education                  │ 3.78%   │ 5.2%    │ 7%+     │
│ Real Estate                │ 3.71%   │ 5.0%    │ 7%+     │
│ Health & Medical           │ 3.27%   │ 4.5%    │ 6%+     │
│ Employment Services        │ 2.42%   │ 3.5%    │ 5%+     │
│ Finance & Insurance        │ 2.91%   │ 4.0%    │ 5%+     │
│ E-Commerce (Retail)        │ 2.69%   │ 4.0%    │ 5%+     │
│ Consumer Services          │ 2.41%   │ 3.5%    │ 5%+     │
│ Industrial Services        │ 2.61%   │ 3.5%    │ 5%+     │
│ Home Goods                 │ 2.44%   │ 3.5%    │ 5%+     │
│ Legal                      │ 2.93%   │ 4.0%    │ 5%+     │
│ Technology                 │ 2.09%   │ 3.0%    │ 4%+     │
│ B2B                        │ 2.41%   │ 3.5%    │ 5%+     │
└────────────────────────────┴─────────┴─────────┴─────────┘

OVERALL SEARCH AVERAGE: 6.66% (LOCALiQ/WordStream 2025 report)
Note: significant increase vs prior years due to PMax, branded queries, and methodology shift
```

### CPC Benchmarks per Industry

```
SEARCH CPC BENCHMARKS (EUR, 2025/2026)
══════════════════════════════════════

┌────────────────────────────┬──────────┬──────────┬──────────┐
│ INDUSTRY                   │ AVG CPC  │ LOW END  │ HIGH END │
├────────────────────────────┼──────────┼──────────┼──────────┤
│ Legal                      │ €7.80    │ €4.00    │ €15.00   │
│ Consumer Services          │ €5.66    │ €3.00    │ €12.00   │
│ Finance & Insurance        │ €3.44    │ €1.50    │ €8.00    │
│ B2B                        │ €3.33    │ €1.50    │ €7.00    │
│ Technology                 │ €3.80    │ €1.50    │ €8.00    │
│ Employment Services        │ €2.04    │ €1.00    │ €5.00    │
│ Real Estate                │ €2.37    │ €1.00    │ €5.00    │
│ Industrial Services        │ €2.56    │ €1.00    │ €5.00    │
│ Home Goods                 │ €2.94    │ €1.00    │ €6.00    │
│ Health & Medical           │ €2.62    │ €1.00    │ €6.00    │
│ Education                  │ €2.40    │ €0.80    │ €5.00    │
│ Advocacy                   │ €1.43    │ €0.50    │ €3.00    │
│ E-Commerce (Retail)        │ €1.16    │ €0.40    │ €3.00    │
│ Travel & Hospitality       │ €1.53    │ €0.50    │ €4.00    │
│ Dating & Personals         │ €2.78    │ €1.00    │ €5.00    │
│ Auto                       │ €2.46    │ €1.00    │ €5.00    │
└────────────────────────────┴──────────┴──────────┴──────────┘

CPCs vary significantly by:
├── Geo (Randstad vs rest)
├── Device (Mobile often cheaper)
├── Time of day
└── Seasonality
```

### Conversion Rate Benchmarks

```
SEARCH CONVERSION RATE BENCHMARKS (2025/2026)
═════════════════════════════════════════════

┌────────────────────────────┬──────────┬──────────┬──────────┐
│ INDUSTRY                   │ AVG CVR  │ TOP 25%  │ TOP 10%  │
├────────────────────────────┼──────────┼──────────┼──────────┤
│ Dating & Personals         │ 9.64%    │ 12%      │ 15%+     │
│ Legal                      │ 5.10%    │ 8%       │ 12%+     │
│ Consumer Services          │ 6.64%    │ 9%       │ 12%+     │
│ Auto                       │ 6.03%    │ 8%       │ 11%+     │
│ Employment Services        │ 5.13%    │ 7%       │ 10%+     │
│ Finance & Insurance        │ 5.10%    │ 7%       │ 10%+     │
│ Health & Medical           │ 3.36%    │ 5%       │ 8%+      │
│ Industrial Services        │ 3.37%    │ 5%       │ 7%+      │
│ Education                  │ 3.39%    │ 5%       │ 7%+      │
│ Travel & Hospitality       │ 3.55%    │ 5%       │ 7%+      │
│ Real Estate                │ 2.47%    │ 4%       │ 6%+      │
│ Home Goods                 │ 2.70%    │ 4%       │ 6%+      │
│ Technology                 │ 2.92%    │ 4%       │ 6%+      │
│ Advocacy                   │ 1.96%    │ 3%       │ 5%+      │
│ E-Commerce (Retail)        │ 2.81%    │ 4%       │ 6%+      │
│ B2B                        │ 3.04%    │ 4%       │ 6%+      │
└────────────────────────────┴──────────┴──────────┴──────────┘

CONVERSION TYPES:
├── E-commerce: Purchase
├── Lead Gen: Form submit, Phone call
├── SaaS: Free trial, Demo request
└── Local: Store visit, Call
```

## E-Commerce Specific Benchmarks

### ROAS Benchmarks per Vertical

```
E-COMMERCE ROAS BENCHMARKS (2025/2026)
══════════════════════════════════════

┌─────────────────────────┬──────────┬──────────┬─────────────┐
│ VERTICAL                │ AVG ROAS │ GOOD     │ EXCELLENT   │
├─────────────────────────┼──────────┼──────────┼─────────────┤
│ Fashion & Apparel       │ 3.5x     │ 4-5x     │ 6x+         │
│ Beauty & Cosmetics      │ 4.0x     │ 5-6x     │ 7x+         │
│ Electronics             │ 2.5x     │ 3-4x     │ 5x+         │
│ Home & Garden           │ 3.0x     │ 4-5x     │ 6x+         │
│ Sports & Outdoor        │ 3.5x     │ 4-5x     │ 6x+         │
│ Food & Beverage         │ 3.0x     │ 4-5x     │ 6x+         │
│ Health & Wellness       │ 3.5x     │ 5-6x     │ 7x+         │
│ Jewelry & Accessories   │ 4.0x     │ 5-7x     │ 8x+         │
│ Pet Supplies            │ 3.5x     │ 4-5x     │ 6x+         │
│ Toys & Games            │ 3.0x     │ 4-5x     │ 6x+         │
│ Office & Business       │ 2.5x     │ 3-4x     │ 5x+         │
│ Automotive Parts        │ 3.0x     │ 4-5x     │ 6x+         │
└─────────────────────────┴──────────┴──────────┴─────────────┘

ROAS CONTEXT:
─────────────
Break-even ROAS = 1 / Profit Margin

Example:
├── 30% margin → Break-even ROAS = 3.33x
├── 40% margin → Break-even ROAS = 2.50x
├── 50% margin → Break-even ROAS = 2.00x
└── 60% margin → Break-even ROAS = 1.67x

Target ROAS = Break-even x (1 + Desired Profit %)
```

### Average Order Value per Category

```
AVERAGE ORDER VALUE BENCHMARKS (EUR)
════════════════════════════════════

┌─────────────────────────┬──────────┬─────────────┬─────────────┐
│ CATEGORY                │ AVG AOV  │ RANGE LOW   │ RANGE HIGH  │
├─────────────────────────┼──────────┼─────────────┼─────────────┤
│ Jewelry & Watches       │ €180     │ €80         │ €500+       │
│ Electronics             │ €150     │ €50         │ €400+       │
│ Furniture               │ €250     │ €100        │ €800+       │
│ Fashion & Apparel       │ €85      │ €40         │ €150        │
│ Beauty & Cosmetics      │ €55      │ €30         │ €100        │
│ Sports & Outdoor        │ €95      │ €40         │ €200        │
│ Health & Supplements    │ €65      │ €30         │ €120        │
│ Pet Supplies            │ €50      │ €25         │ €100        │
│ Food & Beverage         │ €45      │ €20         │ €80         │
│ Home & Garden           │ €75      │ €30         │ €200        │
│ Books & Media           │ €30      │ €15         │ €60         │
│ Baby & Kids             │ €65      │ €30         │ €120        │
└─────────────────────────┴──────────┴─────────────┴─────────────┘

AOV INCREASE STRATEGIES:
├── Cross-sell & upsell (+15-30%)
├── Bundle offers (+20-40%)
├── Free shipping threshold (+10-20%)
└── Quantity discounts (+10-25%)
```

### Cart Abandonment Benchmarks

```
CART ABANDONMENT RATES (2025/2026)
══════════════════════════════════

┌─────────────────────────┬────────────────┬────────────────┐
│ INDUSTRY                │ CART ABANDON   │ CHECKOUT ABAND │
├─────────────────────────┼────────────────┼────────────────┤
│ Finance                 │ 83.6%          │ 75.0%          │
│ Non-Profit              │ 83.1%          │ 74.0%          │
│ Travel                  │ 81.7%          │ 72.0%          │
│ Retail/E-commerce       │ 72.8%          │ 63.0%          │
│ Fashion & Apparel       │ 68.3%          │ 59.0%          │
│ Gaming                  │ 64.2%          │ 55.0%          │
│ Food & Grocery          │ 52.0%          │ 44.0%          │
└─────────────────────────┴────────────────┴────────────────┘

TOP REASONS FOR ABANDONMENT:
├── 48% Extra costs (shipping, tax)
├── 24% Account creation required
├── 18% Shipping too slow
├── 17% Checkout too complex
├── 15% Trust issues
└── 12% Payment options
```

## Campaign Type Benchmarks

### Shopping Campaign Benchmarks

```
SHOPPING CAMPAIGN BENCHMARKS (2025/2026)
════════════════════════════════════════

OVERALL BENCHMARKS:
───────────────────
├── CTR: 0.86% (range: 0.5% - 2.0%)
├── CPC: €0.38 (range: €0.15 - €1.00)
├── CVR: 1.91% (range: 1.0% - 4.0%)
├── ROAS: 4.0x (range: 2.5x - 8.0x)
└── Impression Share: 40% (target: 60%+)

PER VERTICAL:
─────────────
┌─────────────────────┬───────┬───────┬───────┬───────┐
│ VERTICAL            │ CTR   │ CPC   │ CVR   │ ROAS  │
├─────────────────────┼───────┼───────┼───────┼───────┤
│ Fashion & Apparel   │ 1.2%  │ €0.32 │ 2.1%  │ 4.5x  │
│ Electronics         │ 0.7%  │ €0.45 │ 1.5%  │ 3.0x  │
│ Beauty & Cosmetics  │ 1.1%  │ €0.28 │ 2.5%  │ 5.0x  │
│ Home & Garden       │ 0.9%  │ €0.35 │ 1.8%  │ 3.5x  │
│ Sports & Outdoor    │ 1.0%  │ €0.30 │ 2.0%  │ 4.0x  │
│ Food & Beverage     │ 0.8%  │ €0.25 │ 2.2%  │ 4.5x  │
│ Toys & Games        │ 1.3%  │ €0.28 │ 2.3%  │ 4.0x  │
└─────────────────────┴───────┴───────┴───────┴───────┘
```

### Performance Max Benchmarks

```
PERFORMANCE MAX BENCHMARKS (2025/2026)
══════════════════════════════════════

E-COMMERCE PMAX:
────────────────
├── ROAS: 3.5-5.0x (vs Shopping 4.0x)
├── CPA: Often 10-20% lower than Search alone
├── CVR: 2.0-3.5%
├── Learning phase: 2-4 weeks
└── Impression share: N/A (multi-channel)

2025+ PMAX IMPROVEMENTS (v20-v23):
───────────────────────────────────
├── Campaign-level negative keywords (v20+) — control brand safety
├── Search term insights reporting (v21+) — visible in Insights tab
├── ad_network_type breakdown in GAQL (v22+) — split Search/Display/etc
├── First-party audience exclusions — exclude existing customers
├── Demographic reporting — age/gender breakdown available
└── Budget forecasting — project spend/conversion outcomes

LEAD GEN PMAX:
──────────────
├── CPL: Often 15-25% lower than Search
├── CVR: 3.0-6.0%
├── Lead Quality: Monitor closely (varies)
├── Learning phase: 2-3 weeks
└── Best for: 50+ conversions/month goal

PMAX VS STANDARD SHOPPING:
──────────────────────────
┌───────────────┬──────────────┬──────────────┐
│ METRIC        │ PMAX         │ STD SHOPPING │
├───────────────┼──────────────┼──────────────┤
│ ROAS          │ +10-20%      │ Baseline     │
│ Reach         │ +40-60%      │ Baseline     │
│ CPA           │ -10-20%      │ Baseline     │
│ Control       │ Lower        │ Higher       │
│ Transparency  │ Lower (but   │ Higher       │
│               │ improving!)  │              │
└───────────────┴──────────────┴──────────────┘

PULL PMAX SEARCH TERM INSIGHTS VIA GAQL (v22+):
────────────────────────────────────────────────
google_ads_run_gaql(query="
  SELECT search_term_view.search_term, metrics.clicks,
         metrics.conversions, metrics.cost_micros
  FROM search_term_view
  WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.conversions DESC
  LIMIT 50
")
```

### Display & Video Benchmarks

```
DISPLAY CAMPAIGN BENCHMARKS
═══════════════════════════

┌─────────────────────────┬───────┬───────┬───────┐
│ TYPE                    │ CTR   │ CPM   │ CVR   │
├─────────────────────────┼───────┼───────┼───────┤
│ Remarketing - Website   │ 0.7%  │ €2.50 │ 0.8%  │
│ Remarketing - Cart      │ 1.2%  │ €3.50 │ 1.5%  │
│ In-Market Audiences     │ 0.4%  │ €1.80 │ 0.3%  │
│ Custom Intent           │ 0.5%  │ €2.00 │ 0.4%  │
│ Optimized Targeting     │ 0.3%  │ €1.50 │ 0.2%  │
│ Affinity Audiences      │ 0.2%  │ €1.20 │ 0.1%  │
└─────────────────────────┴───────┴───────┴───────┘

VIDEO/YOUTUBE BENCHMARKS:
─────────────────────────
├── View Rate: 25-35%
├── CPV: €0.02 - €0.06
├── CTR (to website): 0.5-2.0%
├── View-through CVR: 0.5-1.5%
└── Completion rate: 40-60%

DEMAND GEN BENCHMARKS:
──────────────────────
├── CTR: 0.8-1.5%
├── CPC: €0.50-1.50
├── CVR: 1.0-3.0%
├── Best for: Visual products, brand consideration
└── Note: Replaced Discovery campaigns (Aug 2023+)
    Demand Gen supports TargetCPC bidding (v22+)
```

## Lead Generation Benchmarks

### CPL Benchmarks per Industry

```
COST PER LEAD BENCHMARKS (EUR, 2025/2026)
═════════════════════════════════════════

┌────────────────────────────┬──────────┬──────────┬──────────┐
│ INDUSTRY                   │ AVG CPL  │ LOW      │ HIGH     │
├────────────────────────────┼──────────┼──────────┼──────────┤
│ Technology/SaaS            │ €75      │ €30      │ €200     │
│ Financial Services         │ €80      │ €40      │ €250     │
│ Insurance                  │ €60      │ €25      │ €150     │
│ Legal Services             │ €110     │ €50      │ €300     │
│ Healthcare                 │ €70      │ €30      │ €180     │
│ Education                  │ €45      │ €20      │ €100     │
│ Real Estate                │ €50      │ €20      │ €120     │
│ Home Services              │ €40      │ €15      │ €100     │
│ B2B Services               │ €90      │ €40      │ €250     │
│ Marketing/Advertising      │ €55      │ €25      │ €150     │
│ Recruitment                │ €65      │ €30      │ €180     │
│ Consulting                 │ €85      │ €40      │ €220     │
│ Manufacturing              │ €95      │ €45      │ €250     │
└────────────────────────────┴──────────┴──────────┴──────────┘

LEAD QUALITY CONTEXT:
─────────────────────
├── MQL CPL = Avg CPL x 2-3
├── SQL CPL = MQL CPL x 2-3
├── Opportunity CPL = SQL CPL x 2-4
└── Customer Acquisition Cost = Opportunity x Close Rate
```

### Lead Form Conversion Benchmarks

```
FORM CONVERSION RATES
═════════════════════

BY FORM LENGTH:
───────────────
├── 1-3 fields: 25-30% conversion
├── 4-6 fields: 15-20% conversion
├── 7-10 fields: 10-15% conversion
└── 11+ fields: 5-10% conversion

BY FORM TYPE:
─────────────
├── Contact form: 12-18%
├── Quote request: 8-15%
├── Demo request: 5-12%
├── Newsletter: 20-35%
├── Whitepaper download: 15-25%
└── Free trial: 8-15%

GOOGLE LEAD FORM EXTENSIONS:
────────────────────────────
├── CVR: 5-15%
├── CPL: Often 20-40% lower than LP forms
├── Quality: Usually lower (convenience leads)
└── Best for: High-volume, qualification funnel
```

## Seasonal Benchmarks

### Seasonal CPC Trends

```
SEASONAL CPC FLUCTUATIONS
═════════════════════════

┌───────────────┬────────────┬─────────────────────────────────┐
│ PERIOD        │ CPC CHANGE │ NOTES                           │
├───────────────┼────────────┼─────────────────────────────────┤
│ Jan           │ -15%       │ Post-holiday lull               │
│ Feb           │ -10%       │ Valentine's spike (certain)     │
│ Mar           │ Baseline   │ Spring season start             │
│ Apr           │ +5%        │ Easter, spring shopping         │
│ May           │ +10%       │ Mother's Day, pre-summer        │
│ Jun           │ +5%        │ Summer sales start              │
│ Jul-Aug       │ -5%        │ Summer lull (varies by industry)│
│ Sep           │ +10%       │ Back-to-school, fall season     │
│ Oct           │ +15%       │ Pre-holiday buildup             │
│ Nov           │ +30-50%    │ Black Friday, Cyber Monday      │
│ Dec           │ +40-60%    │ Holiday shopping peak           │
└───────────────┴────────────┴─────────────────────────────────┘

BLACK FRIDAY / CYBER MONDAY BENCHMARKS:
───────────────────────────────────────
├── CPC increase: +40-80%
├── CTR increase: +20-40%
├── CVR increase: +25-50%
├── ROAS impact: Often neutral (higher CPC, higher CVR)
└── Recommendation: Increase budgets 2-3x
```

### Industry-Specific Seasonality

```
INDUSTRY SEASONAL PATTERNS
══════════════════════════

E-COMMERCE / RETAIL:
────────────────────
Peak: Nov-Dec (holiday), June (sales)
Low: Jan-Feb, Jul-Aug
Strategy: Scale budgets 50-100% for peaks

TRAVEL:
───────
Peak: Jan (booking), Jun-Aug (travel)
Low: Oct-Nov
Strategy: Early year booking campaigns

EDUCATION:
──────────
Peak: Aug-Sep (back-to-school), Jan (new year)
Low: Jun-Jul
Strategy: Lead gen before decision periods

B2B / SAAS:
───────────
Peak: Jan (budget season), Sep-Oct (Q4 push)
Low: Jul-Aug, Dec (holidays)
Strategy: Reduce bids during holidays

HOME SERVICES:
──────────────
Peak: Mar-Jun (spring projects), Sep (pre-winter)
Low: Dec-Feb
Strategy: Weather-dependent bid adjustments
```

## Geographic Benchmarks (Benelux Focus)

### Regional CPC Differences

```
BENELUX CPC DIFFERENCES (vs NL Average)
═══════════════════════════════════════

NETHERLANDS:
────────────
├── Randstad (AMS, RTD, UTR): +20-30%
├── Noord-Holland (other): Baseline
├── Zuid-Holland (other): +5-10%
├── Noord-Brabant: -5-10%
├── Limburg: -10-15%
├── Other regions: -15-25%

BELGIUM:
────────
├── Brussels: +10-20% vs NL average
├── Flanders: -5-15% vs NL average
├── Wallonia: -15-25% vs NL average

GERMANY (if targeting):
───────────────────────
├── Munich, Frankfurt: +30-50% vs NL
├── Berlin, Hamburg: +20-30% vs NL
├── Other: Comparable to NL
└── Overall: German market 2-3x larger, similar CPCs

RECOMMENDATION:
───────────────
├── Budget allocation: Match to population/purchasing power
├── Bid adjustments: -10% to -20% for lower-value regions
├── Separate campaigns: If significant budget differences
└── Language: NL/DE/FR separate campaigns
```

## Quick Reference Tables

### Universal Benchmark Cheat Sheet

```
QUICK REFERENCE - ALL CAMPAIGN TYPES
════════════════════════════════════

                    │ POOR      │ AVERAGE   │ GOOD      │ EXCELLENT
────────────────────┼───────────┼───────────┼───────────┼───────────
SEARCH CTR          │ <2%       │ 2-4%      │ 4-6%      │ >6%
SEARCH CVR          │ <2%       │ 2-4%      │ 4-6%      │ >6%
SEARCH CPA          │ >€100     │ €50-100   │ €25-50    │ <€25
────────────────────┼───────────┼───────────┼───────────┼───────────
SHOPPING CTR        │ <0.5%     │ 0.5-1%    │ 1-2%      │ >2%
SHOPPING CVR        │ <1%       │ 1-2%      │ 2-3%      │ >3%
SHOPPING ROAS       │ <2x       │ 2-4x      │ 4-6x      │ >6x
────────────────────┼───────────┼───────────┼───────────┼───────────
PMAX CVR            │ <1.5%     │ 1.5-3%    │ 3-5%      │ >5%
PMAX ROAS           │ <2.5x     │ 2.5-4x    │ 4-6x      │ >6x
────────────────────┼───────────┼───────────┼───────────┼───────────
DISPLAY CTR         │ <0.2%     │ 0.2-0.5%  │ 0.5-1%    │ >1%
DISPLAY CVR         │ <0.2%     │ 0.2-0.5%  │ 0.5-1%    │ >1%
────────────────────┼───────────┼───────────┼───────────┼───────────
VIDEO VIEW RATE     │ <20%      │ 20-30%    │ 30-40%    │ >40%
VIDEO CTR           │ <0.5%     │ 0.5-1%    │ 1-2%      │ >2%
────────────────────┼───────────┼───────────┼───────────┼───────────
QUALITY SCORE       │ 1-4       │ 5-6       │ 7-8       │ 9-10
```

## Output: Benchmark Comparison Report

```markdown
# Benchmark Comparison Report

## Account Overview
- **Account:** [Account Name]
- **Industry:** [Industry]
- **Report Period:** [Date Range]
- **Compared Against:** Industry Benchmarks 2025/2026



See [benchmarks.md](references/benchmarks.md) for details.



## Priority Improvements

### High Priority (Below Average)
1. [Metric]: Currently X.XX%, target X.XX%
   - Recommended action: [Action]

### Medium Priority (At Average)
1. [Metric]: Currently X.XX%, opportunity to reach X.XX%
   - Recommended action: [Action]

## Seasonal Outlook
- Current month benchmark adjustments: [+/-X%]
- Upcoming opportunities: [Holidays, seasons]
- Recommended budget changes: [Increase/maintain]

## Next Steps
1. [ ] Address high-priority gaps
2. [ ] A/B test improvements
3. [ ] Re-benchmark in [X weeks]
```
