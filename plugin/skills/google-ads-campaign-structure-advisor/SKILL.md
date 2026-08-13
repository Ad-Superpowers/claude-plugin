---
name: google-ads-campaign-structure-advisor
description: "This skill should be used when the user asks to \"restructure Google Ads account\", \"consolidate campaigns\", \"organize ad groups\", \"migrate from SKAGs\", or mentions \"campaign type selection\", \"account structure optimization\", or \"Smart Bidding-friendly structure\". Do NOT use for: bid strategy selection (use bid-strategy-selector), keyword strategy (use keyword-strategy-planner), or performance diagnosis (use performance-troubleshooter)."
---
# Campaign Structure Advisor

Complete guide for structuring and optimizing Google Ads accounts with focus on modern, Smart Bidding-optimized architectures.

> Quick decision guide for choosing structure type in [references/decision-trees.md](references/decision-trees.md).

## 2026 Campaign Type Reference

| Type | Purpose | Key Notes |
|------|---------|-----------|
| Search | Text ads on Google Search | AI Max subtype (2026) for broad query coverage |
| Performance Max | All-channel automation | Negative keywords (v20+), search terms (v21+), network breakdown (v22+) |
| Demand Gen | Visual prospecting (YouTube, Discover, Gmail) | Replaced Discovery (Aug 2023), supports TargetCPC (v22+) |
| Display | Banner/image ads on GDN | |
| Shopping | Product listing ads (feed-based) | |
| Video | YouTube video campaigns | |
| App | App install/engagement | |

Removed: Discovery (→ Demand Gen), Similar Audiences (→ Optimized Targeting).

## Pull Current Account Structure via MCP

```
google_ads_run_gaql(query="
  SELECT campaign.name, campaign.advertising_channel_type,
         campaign.advertising_channel_sub_type,
         campaign.bidding_strategy_type,
         campaign.status,
         metrics.conversions, metrics.cost_micros,
         metrics.cost_per_conversion
  FROM campaign
  WHERE segments.date DURING LAST_30_DAYS
    AND campaign.status = 'ENABLED'
  ORDER BY metrics.cost_micros DESC
  LIMIT 25
")
```

Use to audit campaign types, identify consolidation candidates (<30 conv/month), and spot legacy structures.

## Modern Structure Principles

1. **Consolidation over fragmentation:** Fewer campaigns with more conversions = faster Smart Bidding learning
2. **Machine learning first:** Smart Bidding + broad match, not manual bids + exact match
3. **Theme-based ad groups (STAG):** Same-intent keywords grouped (10-20 per group), replacing SKAGs
4. **Budget = business constraint:** Separate campaigns only for different budgets, geos, business units, or performance targets

## Recommended Account Architectures

### E-Commerce
| Campaign | Budget % | Bidding | Purpose |
|----------|----------|---------|---------|
| Brand Search | 10-15% | Max Conv or tCPA | Capture branded intent |
| Performance Max | 40-50% | Max Conv Value + tROAS | Full-funnel automation |
| Non-Brand Search | 30-40% | tCPA or tROAS | High-intent traffic |
| Demand Gen | 5-10% | tCPA or tCPC (v22+) | Prospecting, visual products |
| Display Remarketing | 5-10% | tCPA | Re-engage visitors |

### Lead Gen
| Campaign | Budget % | Purpose |
|----------|----------|---------|
| Brand Search | 10-15% | Low CPA, high conversion rate |
| High-Intent Non-Brand | 50-60% | Qualified leads ([service] + action terms) |
| Consideration/Research | 20-25% | Top-funnel leads ([service] + question terms) |
| Performance Max (optional) | 10-15% | Broader reach |

### Ad Group Best Practices (STAG)
- 10-20 keywords per ad group, all same intent/theme
- Same landing page, 2-3 RSAs per group
- Match type strategy: Broad 40-60% + Phrase 30-40% + Exact 10-20% (with Smart Bidding)
- Negatives are crucial with broad match: account-level list, campaign-level, weekly search term review

## Campaign Consolidation

### When to Consolidate
- <50 conversions per campaign per month (Smart Bidding "Learning Limited")
- Overlapping keywords across campaigns
- Same CPA/ROAS targets with no reason for separation
- Fragmented budgets across many small campaigns

### Keep Separate When
- Different budget pools or business units
- Different geographic/language targets
- Significantly different performance targets (brand vs non-brand)
- Compliance/organizational requirements

### Consolidation Process

**Phase 1 (Week 1):** Export data, identify candidates, map keyword overlap, plan new structure.

**Phase 2 (Week 2):** Build new consolidated campaigns, reorganize keywords, write RSAs, configure bid strategy.

**Phase 3 (Week 3):** Soft transition — reduce old budgets 50%, enable new with 50%, shift gradually over 7-14 days.

**Phase 4 (Week 4+):** Monitor Learning Phase, adjust targets, optimize negatives, review search terms.

### Portfolio Bid Strategies

One bid strategy across multiple campaigns — useful when individual campaigns have too little data.

- Target CPA Portfolio: Multiple lead gen campaigns, same CPA target
- Target ROAS Portfolio: Multiple e-commerce campaigns, same margin target
- Maximize Conversions Portfolio: New/small campaigns needing aggregated data

## SKAG to Modern Migration

SKAGs (Single Keyword Ad Groups) no longer work because Smart Bidding needs data volume, close variants make exact match imprecise, and broad match + Smart Bidding outperforms.

**Migration steps:**
1. Export all SKAGs, group keywords by theme/intent
2. Define new structure: 500 SKAGs → 30-50 themed ad groups in 3-5 campaigns
3. Consolidate ad copy: 2-3 RSAs per group using best performers as base
4. Gradual transition over 4 weeks (20% → 50% → 80% → 100% new structure)
5. Post-migration: monitor Learning Phase (2-4 weeks), expand with broad match gradually

> Enterprise account architecture (multi-product/region), budget hierarchies, and Google Ads Script for structure analysis in [references/detailed-reference.md](references/detailed-reference.md).

## Output: Structure Recommendation Template

```markdown
# Account Structure Recommendation

## Current State
- **Campaigns:** [X] | **Ad Groups:** [X] | **Keywords:** [X]
- **Avg conversions/campaign/month:** [X]
- **SKAGs detected:** [X]

## Assessment
| Aspect | Current | Best Practice | Status |
|--------|---------|---------------|--------|
| Campaign count | [X] | [Based on budget] | [OK/Issue] |
| Ad groups/campaign | [X] | 5-15 | [OK/Issue] |
| Keywords/ad group | [X] | 10-20 | [OK/Issue] |
| Conv/campaign | [X] | 50+ | [OK/Issue] |

## Proposed Architecture
├── Campaign 1: [Name] — Budget: [X]/day — Bidding: [Strategy]
├── Campaign 2: [Name] — ...
└── Campaign N: [Name] — ...

## Consolidation Plan
| Old Campaigns | New Campaign | Reason |
|---------------|--------------|--------|
| [List] | [New name] | [Low volume/overlap] |

## Migration Timeline
- Week 1: Preparation (export data, design structure)
- Week 2-3: Migration (gradual budget shift)
- Week 4: Consolidation (100% new structure)

## Expected Outcomes
- Faster learning phase
- Improved Smart Bidding performance
- Reduced management overhead
```
