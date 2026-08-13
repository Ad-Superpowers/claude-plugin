---
name: google-ads-remarketing-list-builder
description: "This skill should be used when the user asks to \"build remarketing lists\", \"set up RLSA\", \"implement dynamic remarketing\", \"create cart abandonment audiences\", or mentions \"sequential remarketing\", \"cross-device retargeting\", or \"display remarketing campaigns\". Do NOT use for: audience strategy planning (use audience-strategy-planner), GA4 audience export (use ga4-integration-guide), bid strategy selection (use bid-strategy-selector)."
---
# Remarketing List Builder

Complete guide for setting up effective remarketing lists and RLSA strategies for lead generation with advanced segmentation and messaging sequences.

## GAQL: Check Remarketing List Sizes + RLSA Coverage

Use `google_ads_run_gaql` to audit remarketing list health and RLSA coverage:

```sql
-- All remarketing/customer match lists with sizes
SELECT user_list.name, user_list.type,
    user_list.size_for_search, user_list.size_for_display,
    user_list.membership_life_span, user_list.eligible_for_search,
    user_list.eligible_for_display
FROM user_list
ORDER BY user_list.size_for_search DESC
LIMIT 50
```

```sql
-- RLSA audiences active in Search campaigns (observation + targeting)
SELECT campaign.name, ad_group.name,
    ad_group_criterion.user_list.user_list,
    ad_group_criterion.type, ad_group_criterion.bid_modifier,
    metrics.impressions, metrics.clicks, metrics.conversions
FROM ad_group_audience_view
WHERE campaign.advertising_channel_type = 'SEARCH'
AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
LIMIT 100
```

> Quick decision guide for choosing remarketing type in [references/decision-trees.md](references/decision-trees.md).

## Essential Remarketing Lists

```
LIST HIERARCHY:
┌──────────────────────────────────────────────────────────────┐
│                    ALL VISITORS (30d, min 1000 Search)        │
│    ┌────────────────────────────────────────────────────┐    │
│    │         SERVICE/PRODUCT PAGE VISITORS (30d)         │    │
│    │    ┌────────────────────────────────────────────┐   │    │
│    │    │         HIGH INTENT VISITORS (14d)          │   │    │
│    │    │    ┌────────────────────────────────────┐  │   │    │
│    │    │    │         CONVERTERS (180d)           │  │   │    │
│    │    │    └────────────────────────────────────┘  │   │    │
│    │    └────────────────────────────────────────────┘   │    │
│    └────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

**Setup each list:** Audience Manager → Segments → "+" → Website visitors. Use URL rules (contains "/services/", "/contact", "/thank-you", etc.) with appropriate membership durations.

## Advanced Segmentation

**Engagement-based:** Bounce (don't target), Engaged (2+ pages, soft CTA), High Engagement (180s+ session, strong CTA).

**Recency-based:**
- Hot Leads (1-3 days): highest bids, aggressive messaging
- Warm Leads (4-14 days): medium bids, reminder messaging
- Cold Leads (15-30 days): lower bids, value proposition refresh
- Dormant (31-90 days): lowest bids, special offer/incentive

**Funnel-based:** Blog readers (lead magnet) → Service explorers (case studies) → Form starters (simplified form/phone CTA).

**Form abandonment:** Requires GA4 events (form_start without form_submit, 7-day window). Strategy: "Still have a question?", direct contact options.

## RLSA (Remarketing Lists for Search Ads)

### Implementation Modes

**Observation (Bid Only):** Everyone sees ads, RLSA users get bid boost. Use when testing RLSA value or broad campaign goal. Setup: Campaign → Audiences → Add → "Observation" → Set bid adjustment.

**Targeting (Target Only):** Only RLSA users see ads. Use for competitor bidding (return visitors only), broader keywords with known users. Setup: Campaign → Audiences → Add → "Targeting".

### RLSA Bid Adjustments

| Audience Segment | Recommended Bid Adjustment |
|---|---|
| All visitors (30d) | +10% to +20% |
| High-intent pages | +30% to +50% |
| Cart/form abandoners | +40% to +70% |
| Past converters (upsell) | +20% to +40% |
| Converters (exclude) | -100% (exclusion) |

### Recommended RLSA Structure (Hybrid)

- **Campaign 1:** General Search (all users) with RLSA as Observation, bid adjustments per segment, exclude converters
- **Campaign 2:** RLSA High-Intent (RLSA only) — broader keywords OK, more aggressive bids, personalized messaging
- **Campaign 3:** RLSA Win-Back (RLSA only) — 30-90 day old visitors, competitor keywords, re-engagement messaging

## Display Remarketing

### Campaign Setup

1. New Campaign → Leads → Display → Standard display
2. Add remarketing lists with "Targeting" (not Observation)
3. Exclude converters, recent contacts, branded traffic
4. Bidding: Target CPA or Maximize Conversions
5. Responsive Display Ads: 5 headlines, 1 long headline, 5 descriptions, landscape (1200x628) + square (1200x1200) images

**Ad copy by segment:**
- General visitors: "Still looking for [service]?" / "Discover why 1000+ customers chose us"
- High-intent: "Ready to get started?" / "Contact us for a no-obligation quote"
- Form abandoners: "We haven't received your request yet" / "Still have questions?"

### Sequential Remarketing

Show different messages based on time since visit:

| Day Range | Theme | CTA | Audience Setup |
|---|---|---|---|
| 1-3 | Awareness recall | "Learn More" | Target 3d list |
| 4-7 | Education / social proof | "View Case Study" | Target 7d, Exclude 3d + Converters |
| 8-14 | Differentiation | "Compare Options" | Target 14d, Exclude 7d + Converters |
| 15-30 | Conversion push / urgency | "Start Now" | Target 30d, Exclude 14d + Converters |

> Dynamic remarketing setup (e-commerce + services), cross-device remarketing strategy, and Google Ads Script for list health monitoring in [references/detailed-reference.md](references/detailed-reference.md).

## Output: Remarketing Strategy Template

```markdown
# Remarketing Strategy Plan

## Account Context
- **Business type:** [B2B/B2C/Local Service]
- **Monthly website visitors:** [X]
- **Current conversion rate:** [X%]
- **Average time to conversion:** [X days]

## Remarketing Lists Inventory
| List Name | Definition | Duration | Min Size | Priority |
|-----------|------------|----------|----------|----------|
| All Visitors | URL: / | 30 days | 1,000 | High |
| Service Pages | URL: /services/* | 30 days | 500 | High |
| High Intent | URL: /contact OR /pricing | 14 days | 200 | Critical |
| Form Abandoners | form_start NOT form_submit | 7 days | 100 | Critical |
| Converters | URL: /thank-you | 180 days | N/A | Exclusion |

## RLSA Strategy
| Campaign | Audience | Mode | Bid Adjustment |
|----------|----------|------|----------------|
| Brand | All Visitors | Observation | +20% |
| Non-Brand | High Intent | Observation | +40% |
| Non-Brand | Converters | Observation | -100% |
| RLSA-Only | All Visitors | Targeting | N/A |

## Implementation Checklist
- [ ] Remarketing tag implemented (all pages)
- [ ] Event tracking for key interactions
- [ ] All required lists created
- [ ] RLSA audiences added to Search campaigns
- [ ] Display remarketing campaign created
- [ ] Frequency cap set (3-5 per day)
- [ ] Sequential messaging configured
```
