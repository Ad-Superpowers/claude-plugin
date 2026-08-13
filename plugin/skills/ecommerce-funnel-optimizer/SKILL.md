---
name: ecommerce-funnel-optimizer
description: "This skill should be used when the user asks to \"build an e-commerce ad funnel\", \"optimize retargeting windows\", \"set ROAS targets by funnel stage\", \"recover abandoned carts with ads\", or mentions \"dynamic product ads\", \"Advantage+ Catalog Ads\", or \"seasonal ad strategy\". Do NOT use for: single-platform campaign structure (use platform-specific skills), attribution discrepancies (use attribution-reconciler), or creative fatigue diagnosis (use creative-fatigue-analyzer)."
---

# E-Commerce Funnel Optimizer

## Purpose

Guide advertisers through building, analyzing, and optimizing a full-funnel e-commerce advertising strategy across multiple platforms. Move from single-channel ROAS chasing to a system where each platform and campaign tier has a defined role, target, and measurement approach.

## When to Use This Skill

Invoke when user mentions:
- **Funnel design:** "How do I structure my e-commerce funnel?"
- **Retargeting:** "What retargeting windows should I use?"
- **Catalog Ads:** "How do I set up Advantage+ Catalog Ads / dynamic product ads?"
- **ROAS targets:** "What ROAS should I target for prospecting vs retargeting?"
- **Cart abandonment:** "How do I recover abandoned carts with ads?"
- **Product-level analysis:** "Which products should I push in ads?"
- **Seasonal strategy:** "How do I adjust my funnel for Black Friday / Q4?"
- **AOV optimization:** "How do I increase average order value through ads?"

---

## Part 1: Full Funnel Architecture

### The E-Commerce Ad Funnel

```
STAGE 1: DISCOVERY (Top of Funnel)
│  Goal: Introduce products to new audiences
│  Platforms: TikTok, Meta (Broad/Lookalike), YouTube
│  KPIs: CPM, Reach, Thumbstop Rate, CTR
│  Budget: 30-40% of total
│
STAGE 2: CONSIDERATION (Middle of Funnel)
│  Goal: Educate, build desire, showcase product range
│  Platforms: Meta (Interest/Engagement), Google Shopping, Pinterest
│  KPIs: CTR, Add to Cart Rate, Cost per Add to Cart
│  Budget: 15-25% of total
│
STAGE 3: CART & PURCHASE (Bottom of Funnel)
│  Goal: Convert intent into transactions
│  Platforms: Google Search (Brand + Product), Meta Advantage+ Catalog Ads, Google Shopping
│  KPIs: ROAS, CPA, Conversion Rate
│  Budget: 25-35% of total
│
STAGE 4: RETENTION & UPSELL (Post-Purchase)
│  Goal: Repeat purchases, cross-sell, increase LTV
│  Platforms: Meta Custom Audiences, Google RLSA, Email
│  KPIs: Repeat Purchase Rate, LTV, ROAS on existing customers
│  Budget: 10-15% of total
```

### Platform Roles in the Funnel

| Platform | Primary Role | Secondary Role | Best For |
|----------|-------------|---------------|----------|
| **TikTok** | Discovery | Consideration | Impulse buys, visual products, <35 audience |
| **Meta (FB/IG)** | Discovery + Retargeting | Full funnel | Broad targeting + precise retargeting |
| **Google Search** | Purchase intent | Consideration | High-intent keywords, brand defense |
| **Google Shopping** | Consideration + Purchase | Discovery (PMax) | Product comparison, price-sensitive buyers |
| **Google PMax** | Full funnel (automated) | Discovery | Broad e-commerce with catalog feed |
| **YouTube** | Discovery | Consideration | Product demos, unboxing, storytelling |
| **LinkedIn** | N/A for most e-commerce | B2B e-commerce only | SaaS tools, office supplies, B2B wholesale |

---

## Part 2: Retargeting Windows & Audience Strategy

### Retargeting Audience Tiers

| Tier | Audience | Window | Platform | Priority |
|------|----------|--------|----------|----------|
| **Tier 1** | Cart abandoners | 1-14 days | Meta Advantage+ Catalog Ads, Google RLSA | Highest |
| **Tier 2** | Product viewers (no cart) | 1-30 days | Meta Advantage+ Catalog Ads, Google Shopping | High |
| **Tier 3** | Category browsers | 1-30 days | Meta, Google Display | Medium |
| **Tier 4** | All website visitors | 1-180 days | Meta, Google Display | Lower |
| **Tier 5** | Past purchasers (cross-sell) | 30-365 days | Meta Custom Audience | Medium-High |
| **Tier 6** | Lapsed customers | 90-365 days | Meta, Google, Email | Medium |

### Window Duration Decision Framework

```
How long is your typical consideration cycle?

Impulse products (fashion, beauty, gadgets):
  Cart abandoners: 1-7 days (urgency-driven)
  Product viewers: 1-14 days
  All visitors: 1-30 days

Considered purchases (furniture, electronics, luxury):
  Cart abandoners: 1-14 days
  Product viewers: 1-30 days
  All visitors: 1-60 days

High-ticket items (€500+):
  Cart abandoners: 1-21 days
  Product viewers: 1-45 days
  All visitors: 1-90 days
```

### Retargeting Frequency Caps

| Audience Tier | Daily Cap | Weekly Cap | Rationale |
|--------------|-----------|------------|-----------|
| Cart abandoners (1-3d) | 3-4 | 15-20 | High intent, time-sensitive |
| Cart abandoners (4-14d) | 1-2 | 7-10 | Still warm, reduce pressure |
| Product viewers | 1-2 | 5-7 | Nurture without annoying |
| All visitors | 1 | 3-5 | Light touch, brand reminder |
| Past purchasers | 1 | 3-4 | Relationship maintenance |

### Audience Exclusion Strategy (Critical)

Always exclude to prevent wasted spend and bad experience:

| Campaign Type | Exclude |
|--------------|---------|
| Prospecting (TOF) | All website visitors (30d), all purchasers (180d) |
| Product viewer retargeting | Cart abandoners, recent purchasers (14d) |
| Cart abandoner retargeting | Recent purchasers (7d) |
| Cross-sell campaigns | Recent purchasers of same product (90d) |
| Win-back campaigns | Active customers (purchased in last 60d) |

---

## Part 3: Advantage+ Catalog Ads Setup

### Meta Advantage+ Catalog Ads Configuration

**Prerequisites:**
1. Product catalog uploaded to Meta Commerce Manager
2. Meta Pixel with standard e-commerce events (ViewContent, AddToCart, Purchase)
3. Conversions API (CAPI) — mandatory for reliable signal matching

**Campaign Structure:**
```
Campaign: Catalog_Retargeting (Advantage+ Catalog Ads)
├── Ad Set: Cart Abandoners (1-14 days)
│   ├── Audience: AddToCart but NOT Purchase (14 days)
│   ├── Product Set: All products
│   └── Creative: Carousel with "Still interested?" overlay
├── Ad Set: Product Viewers (1-30 days)
│   ├── Audience: ViewContent but NOT AddToCart (30 days)
│   ├── Product Set: Viewed products + similar
│   └── Creative: Carousel with social proof overlay
└── Ad Set: Broad Retargeting (1-180 days)
    ├── Audience: All visitors excluding above
    ├── Product Set: Best sellers
    └── Creative: Collection ad with lifestyle imagery
```

**Use `meta_get_insights` to monitor Advantage+ Catalog Ads performance:**
```
Breakdowns: product_id, placement
Metrics: spend, purchases, purchase_roas, cost_per_purchase
Date range: last 14 days for retargeting optimization
```

### Google Shopping & PMax Dynamic Ads

**Google Merchant Center Requirements:**
1. Product feed with required attributes (id, title, description, price, image_link, availability)
2. Feed updated minimum daily (ideally every 6 hours for price/stock changes)
3. Enhanced conversions enabled for better matching

**GAQL for product-level performance:**
```sql
SELECT
  segments.product_item_id,
  segments.product_title,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_micros
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.conversions_value DESC
```

### TikTok Dynamic Showcase Ads Setup

**Requirements:**
1. TikTok Pixel with e-commerce events
2. Product catalog synced (via Shopify integration or manual feed)
3. Minimum 100 products recommended

**Use `tiktok_get_report` for product performance:**
```
Report type: auction
Dimensions: ad_id
Metrics: spend, conversion, cost_per_conversion, conversion_rate
```

---

## Part 4: ROAS Targets by Funnel Stage

### Target ROAS Framework

| Funnel Stage | Target ROAS | Acceptable Range | Why |
|-------------|-------------|-----------------|-----|
| **Discovery/Prospecting** | 0.5x - 2x | Break-even is a win | Investing in new customer acquisition |
| **Consideration** | 2x - 4x | Growing awareness into intent | Warming cold traffic |
| **Cart/Purchase (Retargeting)** | 4x - 10x | High intent = high return | Converting existing demand |
| **Cart Abandonment** | 8x - 15x+ | Highest intent segment | Recovery of nearly-lost sales |
| **Cross-sell/Upsell** | 5x - 12x | Known customers, lower risk | Leveraging existing relationship |
| **Win-back** | 3x - 6x | Re-engaging lapsed buyers | Moderate intent, known value |

### ROAS Target Calibration by Margin

```
Your break-even ROAS = 1 / Gross Margin %

Examples:
  80% margin (digital products, SaaS): Break-even = 1.25x
  60% margin (beauty, supplements): Break-even = 1.67x
  40% margin (fashion, home goods): Break-even = 2.5x
  25% margin (electronics, commodity): Break-even = 4.0x
  15% margin (grocery, low-margin): Break-even = 6.67x

Target ROAS should be at least 1.5x your break-even for healthy profit.
```

### Blended vs Stage-Level ROAS

**Common mistake:** Judging every campaign by blended ROAS target.

**Correct approach:** Weight ROAS expectations by funnel position.

| Scenario | TOF Budget | TOF ROAS | BOF Budget | BOF ROAS | Blended ROAS |
|----------|-----------|----------|-----------|----------|-------------|
| Aggressive growth | 50% | 1.5x | 50% | 8x | 4.75x |
| Balanced | 35% | 1.5x | 65% | 6x | 4.43x |
| Profit-focused | 20% | 2x | 80% | 6x | 5.2x |

---

## Part 5: Product-Level ROAS Analysis

### Product Performance Segmentation

Use `google_ads_run_gaql` and `meta_get_insights` to categorize products:

| Quadrant | Revenue | ROAS | Action |
|----------|---------|------|--------|
| **Stars** | High | High | Scale spend, expand to new platforms |
| **Cash Cows** | High | Medium | Maintain, optimize for efficiency |
| **Question Marks** | Low | High | Test scaling, may be limited audience |
| **Dogs** | Low | Low | Reduce spend, exclude from catalog ads if persistent |

### Product Feed Optimization Checklist

| Element | Impact | Action |
|---------|--------|--------|
| Title optimization | High | Include brand + product type + key attribute (size/color) |
| Image quality | High | White background for Shopping, lifestyle for catalog ads |
| Price competitiveness | High | Monitor competitor pricing, use sale_price when applicable |
| Availability | Medium | Remove out-of-stock immediately, update feed hourly |
| Product type | Medium | Use Google's taxonomy for better matching |
| Custom labels | Medium | Tag by margin, seasonality, best-seller status |
| GTIN/MPN | Low-Medium | Required for brand searches, improves matching |

### Custom Labels Strategy for Feed Segmentation

| Label | Values | Use Case |
|-------|--------|----------|
| `custom_label_0` | high_margin, medium_margin, low_margin | Bid by profitability |
| `custom_label_1` | best_seller, new_arrival, clearance | Campaign segmentation |
| `custom_label_2` | seasonal_q4, evergreen | Seasonal bid adjustments |
| `custom_label_3` | price_tier_1, price_tier_2, price_tier_3 | Bid by AOV range |
| `custom_label_4` | high_stock, low_stock | Prevent promoting nearly OOS |

---

## Part 6: AOV Optimization Through Ads

### Upsell & Cross-Sell Ad Strategies

| Strategy | Implementation | Expected AOV Lift |
|----------|---------------|------------------|
| **Bundle ads** | Show product bundles in catalog ad carousel | +15-30% |
| **Threshold offers** | "Free shipping over €75" in ad copy | +10-20% |
| **Cross-sell catalog ads** | Show complementary products post-purchase | +10-25% |
| **Tiered discounts** | "10% off €50, 15% off €100" | +20-35% |
| **Premium variants** | Lead with higher-priced product in carousel | +5-15% |

### Cross-Sell Timing Windows

| Trigger | Timing | Message | Platform |
|---------|--------|---------|----------|
| First purchase | 3-7 days post | Complementary products | Meta Catalog Ads, Email |
| Repeat purchase | 14-30 days post | Replenishment or upgrade | Meta, Google RLSA |
| High AOV purchase | 7-14 days post | Accessories, add-ons | Meta Catalog Ads |
| Category purchase | 7-21 days post | Adjacent categories | Meta, Google Shopping |

---

## Part 7: Seasonal & Sale Period Strategy

### Seasonal Funnel Adjustments

| Period | TOF Budget | BOF Budget | Key Actions |
|--------|-----------|-----------|-------------|
| **Pre-season (6-8 weeks before)** | 50-60% | 40-50% | Build audiences, test creatives |
| **Ramp-up (2-4 weeks before)** | 40% | 60% | Increase retargeting pools, warm audiences |
| **Peak (sale event)** | 20-30% | 70-80% | Maximize conversion of built audiences |
| **Post-peak (1-2 weeks after)** | 30% | 70% | Gift card/returns retargeting, clearance |
| **Off-season** | 40-50% | 50-60% | Return to balanced growth mode |

### Black Friday / Cyber Monday Playbook

**8 Weeks Before:**
- Increase prospecting spend 20% to grow retargeting pools
- Launch "sneak peek" content for email/social
- Set up all sale product feeds with `sale_price`

**4 Weeks Before:**
- Build lookalike audiences from last year's BFCM purchasers
- Create and test all sale creatives (urgency, countdown, deal-focused)
- Pre-approve all ads (review delays increase during BFCM)

**Sale Week:**
- Shift 70-80% of budget to retargeting
- Enable all cart abandonment sequences (1-hour, 4-hour, 24-hour)
- Increase daily budgets 2-3x (Meta/Google can handle spikes)
- Monitor hourly and adjust bids for top performers

**Post-BFCM (2 Weeks After):**
- Retarget BFCM browsers who didn't purchase
- Cross-sell to BFCM purchasers
- Win-back campaigns for lapsed customers who missed the sale

### CPM Seasonality Benchmarks (Approximate, EUR)

| Month | Meta CPM | Google CPC | TikTok CPM | Notes |
|-------|----------|-----------|------------|-------|
| Jan-Feb | €6-10 | €0.40-0.80 | €4-7 | Post-holiday dip, good for testing |
| Mar-Apr | €8-12 | €0.50-0.90 | €5-8 | Spring ramp-up |
| May-Jun | €8-12 | €0.50-0.90 | €5-8 | Stable, pre-summer |
| Jul-Aug | €7-11 | €0.40-0.80 | €4-7 | Summer dip in many verticals |
| Sep-Oct | €10-15 | €0.60-1.00 | €6-10 | Q4 ramp begins |
| Nov | €15-25 | €0.80-1.50 | €8-15 | BFCM competition peak |
| Dec | €12-20 | €0.70-1.20 | €7-12 | Christmas, then sharp drop Dec 26+ |

---

## Part 8: MCP Tool Usage for Funnel Analysis

### Discovery Stage Analysis

**Meta prospecting performance:**
Use `meta_get_insights` with:
- `level`: campaign
- `fields`: reach, impressions, frequency, cpm, ctr, actions (landing_page_views)
- `filtering`: campaigns with "prospecting" or "TOF" in name
- `date_range`: last 30 days

**TikTok discovery performance:**
Use `tiktok_get_report` with:
- Metrics: reach, impressions, cpm, ctr, video_views_p75
- Date range: last 30 days

### Conversion Stage Analysis

**Google Ads Shopping/Search ROAS:**
Use `google_ads_run_gaql`:
```sql
SELECT
  campaign.name,
  campaign.advertising_channel_type,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_micros,
  metrics.all_conversions_value
FROM campaign
WHERE campaign.advertising_channel_type IN ('SHOPPING', 'SEARCH')
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.conversions_value DESC
```

### Cross-Platform Funnel View

**GA4 for unified funnel metrics:**
Use `ga4_run_report` with:
- Dimensions: sessionDefaultChannelGroup, sessionSourceMedium
- Metrics: sessions, addToCarts, ecommercePurchases, purchaseRevenue
- Date range: last 30 days

This gives the cross-platform view of how each channel contributes to each funnel stage, independent of platform-reported attribution.

---

## Part 9: Funnel Health Diagnostic Checklist

### Weekly Review Checklist

| Check | Metric | Warning Threshold | Tool |
|-------|--------|-------------------|------|
| TOF reach sufficient? | Weekly reach / target audience | < 10% of TAM | `meta_get_insights` |
| MOF engagement healthy? | CTR on consideration campaigns | < 1% Meta, < 2% Google | `meta_get_insights`, `google_ads_run_gaql` |
| Cart abandonment rate? | Carts / Purchases | > 75% for most categories | `ga4_run_report` |
| Retargeting pool size? | Active retargeting audience size | < 1,000 people | Meta Audiences, Google Audiences |
| Frequency creep? | Average frequency on retargeting | > 8x/week | `meta_get_insights` |
| BOF ROAS on target? | Retargeting ROAS | Below stage target | `meta_get_insights`, `google_ads_run_gaql` |
| New vs returning ratio? | % revenue from new customers | < 30% (growth stalling) | `ga4_run_report` |

### Common Funnel Problems & Fixes

| Problem | Symptom | Root Cause | Fix |
|---------|---------|-----------|-----|
| High TOF spend, low conversions | Blended ROAS dropping | Insufficient MOF/BOF | Increase retargeting budget allocation |
| Retargeting pool shrinking | BOF impressions declining | TOF prospecting underfunded | Increase prospecting 20-30% |
| Cart abandonment spiking | Cart rate up, purchase rate flat | Price shock, shipping costs, friction | Test threshold free shipping, simplify checkout |
| Frequency fatigue | CTR dropping on retargeting | Same creative too long | Refresh creatives every 2-3 weeks |
| Cannibalization | Multiple platforms claiming same sale | Overlapping audiences | Use exclusion audiences, check incrementality |
| ROAS declining at scale | Efficiency drops as spend increases | Audience saturation | Expand to new platforms, broaden targeting |
