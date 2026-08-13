---
name: google-ads-pmax-asset-group-optimizer
description: "This skill should be used when the user asks to \"optimize PMax asset groups\", \"analyze asset group performance\", \"configure listing groups\", \"set up search themes\", or mentions \"audience signals optimization\", \"creative testing in PMax\", or \"asset group structure\". Do NOT use for: standard Search/Display campaign setup (use search-campaign-builder), bid strategy selection (use learning-phase-tracker)."
---
# Performance Max Asset Group Optimizer

Complete guide for optimizing Performance Max asset groups — from structure and audience signals to creative testing and feed optimization.

> Asset group count decision guide in [references/decision-trees.md](references/decision-trees.md).

## MCP Tool Integration

```
STEP 1: PMax campaign performance overview
google_ads_run_gaql(query="
  SELECT campaign.name, campaign.status,
    metrics.cost_micros, metrics.conversions,
    metrics.cost_per_conversion, metrics.conversions_value
  FROM campaign
  WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
    AND campaign.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")

STEP 2: Asset group performance
google_ads_run_gaql(query="
  SELECT campaign.name, asset_group.name, asset_group.status,
    metrics.impressions, metrics.clicks, metrics.conversions,
    metrics.cost_micros, metrics.cost_per_conversion
  FROM asset_group
  WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")

STEP 3: Search terms (v21+)
google_ads_run_gaql(query="
  SELECT campaign.name, search_term_view.search_term,
    metrics.impressions, metrics.clicks,
    metrics.conversions, metrics.cost_micros
  FROM search_term_view
  WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
  LIMIT 100
")

STEP 4: Ad network type breakdown (v22+)
google_ads_run_gaql(query="
  SELECT campaign.name, segments.ad_network_type,
    metrics.impressions, metrics.clicks,
    metrics.conversions, metrics.cost_micros
  FROM campaign
  WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
    AND segments.date DURING LAST_30_DAYS
")
```

## Asset Group Structure

### Structuring Options

| Option | Best for | Example |
|--------|----------|---------|
| Category-based | Most common | Women's / Men's / Accessories |
| Margin-based | Profit focus | High / Standard / Clearance |
| Funnel-based | Customer journey | Prospecting / Retargeting / Cross-sell |
| Performance-based | Data-driven | Top Performers / Testing / Long Tail |
| **Hybrid (recommended)** | Best of all | Bestsellers + Category A/B/C + Sale |

### Asset Requirements

| Asset Type | Min | Recommended | Max | Specs |
|------------|-----|-------------|-----|-------|
| Headlines | 3 | 5-15 | 15 | Max 30 chars |
| Long Headlines | 1 | 3-5 | 5 | Max 90 chars |
| Descriptions | 2 | 4-5 | 5 | Max 90 chars |
| Images | 2 | 6-10 | 20 | 1200x628, 1200x1200, 960x1200 |
| Logos | 1 | 2 | 5 | 1200x1200 (square), 1200x300 (landscape) |
| Videos | 0 | 1-3 | 5 | 15-30 sec, 16:9 + 1:1 + 9:16 |

No video upload = Google auto-creates video from images (often less effective).

> Detailed asset variation strategy (headline/image/video types) in [references/detailed-reference.md](references/detailed-reference.md).

### Asset Performance Ratings

Per-asset ratings (Best/Good/Low/Pending) removed from API in v22 — check in Google Ads UI only (Campaign → Asset Groups → Asset Performance).

**Optimization cycle:**
- Week 1-2: Learning phase — upload all assets, make no changes
- Week 3-4: First analysis — identify "Low" performers, note trends
- Week 5-6: First optimization — replace consistently "Low" assets, add "Best" variations
- Monthly: Full review, replace 20-30% of assets, seasonal updates

**Replacement rules:** Low >30 days → Replace. Low <30 days → Monitor. Good → Keep, test variations. Best → Keep, create similar. Pending → Wait.

## Audience Signals Optimization

Audience Signals = HINTS for Google AI, NOT targeting restrictions. Google will advertise beyond your signals.

**Signal priority (strongest to weakest):**
1. Your Data: Customer Match (converters)
2. Your Data: Website remarketing (high intent)
3. Custom Segments: Keywords (competitor/product)
4. Custom Segments: URLs (competitor sites)
5. In-Market Audiences
6. Affinity Audiences
7. Demographics

**Example configuration — Bestsellers AG:**
- Your Data: All Purchasers, Product Viewers (90d), Cart Abandoners (30d)
- Custom Segments: top product names, competitor product pages
- Interests: relevant In-Market + Affinity categories

> Audience signal troubleshooting (ignored signals, too broad/narrow) in [references/decision-trees.md](references/decision-trees.md).

## Search Themes

Keywords you give PMax to understand relevant search queries (hints for AI, not exact targeting).

- Recommended: 3-7 per asset group (max 25)
- Types: Branded, Generic Product, Long-tail, Problem-solving
- Update monthly: check Search Terms report, add high-performers, remove non-performers

> Per-category search theme examples in [references/detailed-reference.md](references/detailed-reference.md).

## Listing Groups (E-commerce)

Listing Groups determine which products belong to which Asset Group.

**Segmentation attributes:** Category, Brand, Condition, Item ID, Product Type, Custom Labels (0-4).

**Custom Labels strategy:**
- Label 0: Margin Level (High/Medium/Low)
- Label 1: Performance Tier (Bestseller/Rising Star/Long Tail)
- Label 2: Seasonal (Spring/Summer/Fall/Winter)
- Label 3: Promo Status (Full Price/On Sale/Clearance)

**Optimization:** Identify top 20% products (own asset group, premium signals) and bottom 20% (exclude or improve feed quality). Exclude out-of-stock, below-breakeven margin, seasonally irrelevant products.

## PMax New Capabilities (2025-2026)

- **Campaign-level negative keywords (v20):** Add via UI or API. Protect specific queries for separate Search campaigns.
- **Search terms reporting (v21):** PMax search term data now in API. Use to find negatives and new keyword opportunities.
- **First-party audience exclusions (Mar 2026):** Exclude existing customers for pure prospecting.
- **Ad network type breakdown (v22):** See which network (Search, Display, YouTube) drives PMax performance.
- **Demographic reporting (Mar 2026):** Age/gender breakdowns for budget efficiency analysis.

> Creative testing approaches (sequential, split AG, experiments) and asset refresh cadence in [references/detailed-reference.md](references/detailed-reference.md).

## Output: Asset Group Optimization Template

```markdown
# Asset Group Optimization Plan

## Campaign Overview
- **Campaign:** [Name] | **Account:** [Name] | **Period:** [Date range]

## Asset Group Structure
| Asset Group | Products/Focus | Budget % | ROAS | Status |
|-------------|---------------|----------|------|--------|
| [AG 1] | [Products] | [%] | [X]x | [Status] |

## Asset Performance Review
| Asset Type | Rating | Action |
|------------|--------|--------|
| [Headline/Image/Video] | [Best/Good/Low] | [Keep/Replace/Add variation] |

## Audience Signals Review
| Signal Type | Signal | Performance |
|-------------|--------|-------------|
| Your Data | [Signal] | [Performance] |
| Custom | [Signal] | [Performance] |

## Action Items
- Immediate: [This week actions]
- Short-term: [Next 2 weeks]
- Long-term: [Next month]

## Success Metrics
| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| ROAS | [X]x | [Y]x | [Date] |
| CPA | $[X] | $[Y] | [Date] |
```
