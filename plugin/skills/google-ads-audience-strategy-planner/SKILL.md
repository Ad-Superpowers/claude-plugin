---
name: google-ads-audience-strategy-planner
description: "This skill should be used when the user asks to \"plan Google Ads audience strategy\", \"set up Customer Match\", \"configure Optimized Targeting\", \"build audience layering\", or mentions \"In-market audiences\", \"first-party data strategy\", \"B2B targeting\", or \"custom segments\". Do NOT use for: remarketing list creation (use remarketing-list-builder), GA4 audience export (use ga4-integration-guide), bid strategy selection (use bid-strategy-selector)."
---
# Audience Strategy Planner

Complete guide for setting up an effective Google Ads audience strategy with first-party data, Google audiences, and layering strategies for lead generation.

> Quick decision guide for choosing audience strategy in [references/decision-trees.md](references/decision-trees.md).

## GAQL: Check Audience Performance

```sql
-- Audience observation data from Search campaigns
SELECT campaign.name, ad_group.name,
    ad_group_criterion.user_list.user_list,
    ad_group_criterion.bid_modifier,
    metrics.impressions, metrics.clicks, metrics.cost_micros,
    metrics.conversions, metrics.conversions_value
FROM ad_group_audience_view
WHERE segments.date DURING LAST_30_DAYS
AND campaign.advertising_channel_type = 'SEARCH'
ORDER BY metrics.impressions DESC
LIMIT 100
```

```sql
-- All Customer Match + remarketing lists
SELECT user_list.name, user_list.size_for_search,
    user_list.size_for_display, user_list.membership_life_span,
    user_list.type, user_list.eligible_for_search
FROM user_list
ORDER BY user_list.size_for_search DESC
LIMIT 50
```

## Audience Types Overview

| Type | Description | Use Case |
|------|-------------|----------|
| **First-Party Data** | | |
| Customer Match | Your customer lists (email, phone, address) | Upsell, loyalty, exclusion |
| Website Visitors | Remarketing lists (RLSA) | Re-engage, cart recovery |
| YouTube Users | Video interactions | Video remarketing |
| GA4 Audiences | Behavioral segments | Complex targeting |
| **Google-Provided** | | |
| In-market | Actively researching products | High-intent prospecting |
| Affinity | Long-term interests & lifestyle | Brand awareness |
| Life Events | Major life changes (moving, wedding) | Timely targeting |
| Detailed Demographics | Age, gender, income, parental | Demographic targeting |
| Optimized Targeting | Google expands beyond selections | Scale acquisition |
| Custom Segments | Keywords, URLs, app interests | Custom intent targeting |

Optimized Targeting replaced Similar Audiences (deprecated May 2023). Enabled by default in Display, YouTube, and Demand Gen.

### Audience Sizing

| Network | Minimum Size |
|---------|-------------|
| Search (RLSA) | 1,000 users |
| Display / Gmail | 100 users |
| YouTube | 1,000 users |
| Customer Match | 1,000 matched users |

Optimal size: 10,000-100,000 for stable data. Recommended membership durations: All Visitors 30-90d, Cart Abandoners 7-14d, Converters 180-365d (for exclusion).

## Customer Match Setup

**Requirements:** $50,000+ lifetime spend, 90+ days account history, good compliance.

**Data types:** Email, phone (with country code), mailing address, mobile device IDs.

| Data Combination | Expected Match Rate |
|---|---|
| Email only | 30-50% |
| Email + Phone | 45-65% |
| Email + Phone + Name | 55-75% |
| All fields | 60-80% |

**Setup:** Tools → Audience Manager → Segments → "+ Segment" → "Customer list". Upload CSV or automate via API. Processing takes 24-48 hours.

### Customer Match Strategies

| Strategy | Segment | Targeting | Bid Adjustment |
|----------|---------|-----------|----------------|
| Upsell/Cross-sell | Active customers, last purchase >30d | Observation or Targeting | +20-50% |
| Win-back | Churned customers (90+ days) | Targeting | +10-30% |
| Exclusion (acquisition) | All customers | Exclude | N/A |
| Optimized Targeting | Best customers as signal | Signal for Display/YouTube/Demand Gen | N/A |
| PMax Signals | Customer list | Audience signal (not direct targeting) | N/A |

Segment by: purchase value, recency, product category, or LTV tier.

## Audience Layering Strategies

**AND Logic (narrowing):** In-market: Business Services AND Affinity: Business Professionals AND Age 25-54 → smaller, more qualified audience.

**OR Logic (expanding):** In-market: CRM Software OR Cloud Storage OR Cybersecurity → larger audience, related interests.

**Exclusion Logic:** Target all website visitors MINUS converters MINUS Customer Match → prospecting only.

### B2B Lead Gen Layering Example
- Layer 1 (Intent): In-market for Enterprise Software + Cloud Services
- Layer 2 (Decision maker): Affinity for Business Professionals + Income Top 10%
- Layer 3 (Exclusion): Exclude current customers + recent converters

### B2B Targeting Solutions

Google Ads lacks job title / company size targeting. Workarounds:
1. **In-market + Affinity layering** for decision makers
2. **Customer Match** segmented by firmographics (enterprise/mid-market/SMB)
3. **Custom Segments** with competitor/tool keywords and review site URLs (g2.com, capterra.com)
4. **LinkedIn → Google Ads workflow:** Generate leads on LinkedIn → export to Customer Match → use as PMax signal → Display remarketing via Google

## Full-Funnel Audience Framework

| Funnel Stage | Audiences | Campaigns | Budget |
|---|---|---|---|
| Awareness | Affinity, Optimized Targeting, Life Events | Display, YouTube, Demand Gen | 15-25% |
| Consideration | In-market, Website visitors, Custom intent | Display, YouTube, Search (broad) | 30-40% |
| Decision | RLSA (high-intent), Form abandoners, Return visitors | Search, Remarketing Display | 35-45% |
| Loyalty | Customer Match, Recent converters | Display remarketing, YouTube | 5-10% |

> Detailed In-market/Affinity category lists, Custom Segments setup guide, and Google Ads Script for audience analysis in [references/detailed-reference.md](references/detailed-reference.md).

## Output: Audience Strategy Template

```markdown
# Audience Strategy Plan

## Business Context
- **Type:** [B2B/B2C/Local] | **Deal value:** $[X] | **Sales cycle:** [X days]

## First-Party Data
| Data Type | Size | Match Rate | Status |
|-----------|------|------------|--------|
| Customer emails | [X] | [X%] | [Status] |
| Website visitors | [X] | N/A | [Tag status] |
| GA4 audiences | [X] | N/A | [Linked] |

## Audience Layering per Campaign
Layer 1 (Intent): [Audiences]
Layer 2 (Qualification): [Audiences + Demographics]
Layer 3 (Exclusions): [Exclusion lists]

## Bid Adjustments
| Audience | Adjustment | Rationale |
|----------|------------|-----------|
| [Audience] | +20% | High performer |
| [Audience] | -15% | Lower quality |

## Implementation Checklist
- [ ] Customer Match lists uploaded
- [ ] In-market audiences added (observation)
- [ ] Custom segments created
- [ ] Exclusion lists configured
- [ ] GA4 audiences linked
- [ ] Bid adjustments set
```
