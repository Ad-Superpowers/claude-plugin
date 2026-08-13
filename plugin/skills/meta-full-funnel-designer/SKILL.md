---
name: meta-full-funnel-designer
description: "This skill should be used when the user asks to \"design a full funnel\", \"allocate budget across funnel stages\", \"optimize TOFU/MOFU/BOFU\", or mentions \"full-funnel strategy\", \"customer journey campaigns\", or \"funnel budget split\". Do NOT use for: campaign structure details (use campaign-structure-advisor), audience overlap issues (use audience-overlap-detector), bid strategy selection (use bid-strategy-selector)."
---
# Full-Funnel Designer

## Overview

This skill helps design complete full-funnel advertising strategies for Meta Ads, including budget allocation, audience targeting per stage, and creative alignment with the customer journey.

## 2026 Context: ASC and Andromeda

> **Advantage+ Sales Campaigns (ASC):** For e-commerce advertisers, ASC (the new unified structure replacing "Advantage+ Shopping Campaigns") manages budget, audience, and placement automatically. For accounts spending >€5k/month on conversions, consider running ASC alongside or instead of manual TOFU/MOFU/BOFU segmentation — ASC often outperforms manual funnels at scale.

> **Andromeda Engine:** Meta's rebuilt ad retrieval system means creative quality is now the primary delivery signal. A full-funnel strategy with 15+ distinct creatives across stages outperforms one with only 4-6.

> **Attribution (Jan 2026 change):** 7-day view and 28-day view attribution windows have been removed. Default attribution is now 7-day click + 1-day view. Adjust BOFU ROAS targets accordingly — numbers will appear lower than historical comparisons.

## Funnel Framework

### The 3 Funnel Stages

```
┌─────────────────────────────────────────────────────────────────┐
│  TOFU (Top of Funnel) - AWARENESS                               │
│  ├── Goal: Reach & brand awareness                              │
│  ├── Budget: 20-30% of total                                    │
│  ├── Audiences: Broad, Lookalikes 3-10%, Interest-based         │
│  ├── Objectives: Reach, Video Views, Brand Awareness            │
│  ├── Creatives: Educational, entertaining, brand story          │
│  └── KPIs: CPM, Reach, Video ThruPlay, Frequency                │
├─────────────────────────────────────────────────────────────────┤
│  MOFU (Middle of Funnel) - CONSIDERATION                        │
│  ├── Goal: Engagement & interest building                       │
│  ├── Budget: 30-40% of total                                    │
│  ├── Audiences: Engagers, Video viewers, Website visitors       │
│  ├── Objectives: Traffic, Engagement, Lead Generation           │
│  ├── Creatives: Product demos, testimonials, comparisons        │
│  └── KPIs: CTR, CPC, Landing page views, Time on site           │
├─────────────────────────────────────────────────────────────────┤
│  BOFU (Bottom of Funnel) - CONVERSION                           │
│  ├── Goal: Conversions & sales                                  │
│  ├── Budget: 30-50% of total                                    │
│  ├── Audiences: Add to cart, High-intent visitors, Customers    │
│  ├── Objectives: Conversions, Sales (Advantage+ Catalog Ads)    │
│  ├── Creatives: Urgency, offers, social proof, retargeting      │
│  └── KPIs: CPA, ROAS, Conversion rate, AOV                      │
└─────────────────────────────────────────────────────────────────┘
```

## Budget Allocation Calculator

### Ask the user:

1. **What is your total monthly budget?**
2. **What is your current situation?**
   - New brand (low awareness) → More TOFU
   - Established brand (high traffic) → More BOFU
   - Growing brand (balance needed) → Balanced distribution

### Budget Distribution Models

#### Model A: New Brand / Awareness Focus
```
TOFU: 40% │████████████████████
MOFU: 35% │█████████████████▌
BOFU: 25% │████████████▌
```

#### Model B: Balanced / Growth Focus
```
TOFU: 25% │████████████▌
MOFU: 35% │█████████████████▌
BOFU: 40% │████████████████████
```

#### Model C: Established Brand / Performance Focus
```
TOFU: 15% │███████▌
MOFU: 25% │████████████▌
BOFU: 60% │██████████████████████████████
```

## Audience Mapping per Stage

### TOFU Audiences (Cold)

| Audience Type | Description | Expected CPM |
|---------------|-------------|--------------|
| Broad | Demographics + geo only | $3-8 |
| Interest Stacking | 3-5 related interests | $5-10 |
| Lookalike 6-10% | Broad lookalike of purchasers | $4-8 |
| Video Viewers LAL | Lookalike of 95% video viewers | $5-9 |

### MOFU Audiences (Warm)

| Audience Type | Description | Window |
|---------------|-------------|--------|
| Video Viewers | 50%, 75%, 95% watched | 30-60 days |
| Page Engagers | Likes, comments, shares | 30-90 days |
| Website Visitors | All visitors (excl. converters) | 30-60 days |
| Blog Readers | Specific content pages | 30-60 days |
| IG/FB Engagers | Profile visitors, post engagers | 30-90 days |

### BOFU Audiences (Hot)

| Audience Type | Description | Window |
|---------------|-------------|--------|
| Add to Cart | Product added, not purchased | 7-14 days |
| View Content | Product page viewed | 7-14 days |
| Initiate Checkout | Checkout started, not completed | 3-7 days |
| Past Purchasers | Cross-sell/upsell | 30-180 days |
| High-Value Customers | Top 20% LTV | 180-365 days |

## Creative Strategy per Stage

### TOFU Creative Formats

```
Recommended formats:
├── Video (15-30 sec) - Hook within 3 seconds
├── Carousel - Storytelling or educational
├── Reels - Native, entertaining content
└── Collection - Brand discovery

Content types:
├── Educational ("Did you know...")
├── Entertainment (Relatable content)
├── Brand story (Values, mission)
└── User generated (Authentic)
```

### MOFU Creative Formats

```
Recommended formats:
├── Video (30-60 sec) - Product demos
├── Carousel - Feature highlights
├── Lead ads - Gated content
└── Instant Experience - Immersive storytelling

Content types:
├── Product demonstrations
├── Customer testimonials
├── How-to guides
├── Comparison content
└── Behind the scenes
```

### BOFU Creative Formats

```
Recommended formats:
├── Advantage+ Catalog Ads (Dynamic Product Ads)
├── Carousel - Retargeting viewed products
├── Single image - Strong CTA
└── Collection - Product catalog

Content types:
├── Urgency ("Last chance", "Almost sold out")
├── Social proof (Reviews, ratings)
├── Special offers (Discount, free shipping)
├── Abandoned cart reminders
└── Limited time deals
```

## Full-Funnel Campaign Template

### When the user asks to set up a funnel:

```
CAMPAIGN STRUCTURE TEMPLATE
===========================

Budget: [TOTAL BUDGET]

TOFU CAMPAIGN - Awareness
   ├── Name: [BRAND]_TOFU_Awareness_[MONTH]
   ├── Objective: Reach / Video Views
   ├── Budget: [X]% = $[AMOUNT]
   ├── Audiences:
   │   ├── Ad Set 1: Broad (18-65, [COUNTRY])
   │   ├── Ad Set 2: Interest Stack ([INTERESTS])
   │   └── Ad Set 3: LAL 6-10% Purchasers
   └── Creatives:
       ├── Video 1: Brand story (15 sec)
       ├── Video 2: Educational hook
       └── Carousel: Value proposition

MOFU CAMPAIGN - Consideration
   ├── Name: [BRAND]_MOFU_Consideration_[MONTH]
   ├── Objective: Traffic / Engagement
   ├── Budget: [X]% = $[AMOUNT]
   ├── Audiences:
   │   ├── Ad Set 1: Video Viewers 50%+ (30d)
   │   ├── Ad Set 2: Page Engagers (60d)
   │   └── Ad Set 3: Website Visitors (30d)
   └── Creatives:
       ├── Video 1: Product demo
       ├── Carousel: Features & benefits
       └── Testimonial: Customer story

BOFU CAMPAIGN - Conversion
   ├── Name: [BRAND]_BOFU_Conversion_[MONTH]
   ├── Objective: Conversions / Sales
   ├── Budget: [X]% = $[AMOUNT]
   ├── Audiences:
   │   ├── Ad Set 1: Add to Cart (14d)
   │   ├── Ad Set 2: View Content (7d)
   │   └── Ad Set 3: Past Purchasers (90d)
   └── Creatives:
       ├── Advantage+ Catalog Ads: Viewed products
       ├── Single image: Urgency offer
       └── Carousel: Social proof
```

## Frequency & Overlap Management

### Frequency Guidelines per Stage

| Stage | Max Frequency/Week | Action When Exceeded |
|-------|---------------------|----------------------|
| TOFU | 2-3x | Expand audience |
| MOFU | 3-4x | Refresh creatives |
| BOFU | 5-7x | Add exclusions |

### Audience Exclusions Setup

```
TOFU exclusions:
└── Exclude: MOFU + BOFU audiences

MOFU exclusions:
├── Exclude: Purchasers (30d)
└── Exclude: Add to Cart (7d)

BOFU exclusions:
└── Exclude: Purchasers (7d) or converters
```

## Funnel Diagnosis Framework

### When the funnel is underperforming:

```
PROBLEM: Low awareness/reach
├── Check: Is TOFU budget sufficient? (min 20%)
├── Check: Are audiences too narrow?
└── Action: Target broader, more video content

PROBLEM: High TOFU metrics, low MOFU engagement
├── Check: Does MOFU content align with TOFU messaging?
├── Check: Are retargeting windows correct?
└── Action: Align content, extend windows

PROBLEM: Good engagement, few conversions
├── Check: Is the landing page optimized?
├── Check: Are BOFU offers compelling enough?
└── Action: A/B test offers, add urgency

PROBLEM: High CPA in BOFU
├── Check: Is the audience too small (audience exhaustion)?
├── Check: Is frequency too high?
└── Action: Strengthen TOFU/MOFU, refresh creatives
```

## Example Interaction

**User**: "I want to set up a full funnel for my e-commerce store. Budget is $5,000/month."

**Claude response**:

"I'll help you with a complete full-funnel strategy. First, a few questions:

1. **What do you sell?** (product category)
2. **Is your brand already established or are you starting fresh?**
3. **Do you have existing pixel data/audiences?**
4. **What is your average order value (AOV)?**

Based on $5,000/month and an average scenario, I'd suggest:

| Stage | Budget | Goal |
|-------|--------|------|
| TOFU | $1,250 (25%) | Reach new people |
| MOFU | $1,750 (35%) | Build interest |
| BOFU | $2,000 (40%) | Drive conversions |

Would you like me to build out the complete campaign structure with audiences and creative suggestions?"

## MCP Tool Usage

### Audit an existing funnel before designing a new one:

```python
# Get campaign-level performance split by objective to map current funnel state
meta_get_insights(
    account_id="act_XXXXXXXXX",
    level="campaign",
    date_preset="last_30d",
    fields=["impressions", "reach", "spend", "actions", "cost_per_action_type"]
)
```

This shows budget distribution across objectives (Awareness / Traffic / Conversions) and helps identify which funnel stage is underfunded or over-invested before recommending changes.
