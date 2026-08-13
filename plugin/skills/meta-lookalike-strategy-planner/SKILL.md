---
name: meta-lookalike-strategy-planner
description: "This skill should be used when the user asks to \"create lookalike audiences\", \"optimize LAL percentages\", \"choose source audiences\", or mentions \"lookalike strategy\", \"LAL underperforming\", or \"Advantage+ audience signals\". Do NOT use for: audience overlap issues (use audience-overlap-detector), full-funnel design (use full-funnel-designer), campaign structure (use campaign-structure-advisor)."
---
# Lookalike Strategy Planner

## Overview

This skill helps create high-quality Lookalike Audiences by selecting the right source audiences, choosing optimal percentages, and applying advanced strategies for maximum performance.

> **2026 Context:** Meta increasingly recommends Advantage+ Audience (broad targeting with audience suggestions) over manual Lookalikes for most campaign types. Lookalikes remain valuable as **audience suggestions** within Advantage+ campaigns, and for specific use cases where you need more targeting control. For Advantage+ Sales Campaigns (ASC), upload your Customer Match list as an audience signal instead of creating standalone LALs. Note: "Advantage+ Shopping Campaigns" branding was deprecated in API v25.0 — the unified product is now called **Advantage+ Sales Campaigns**.

## Lookalike Fundamentals

### How Meta Lookalikes Work

```
┌─────────────────────────────────────────────────────────────────┐
│  LOOKALIKE CREATION PROCESS                                     │
│                                                                 │
│  1. SOURCE AUDIENCE (your data)                                 │
│     └── Minimum 100 people (1,000+ recommended)                 │
│                                                                 │
│  2. META's ALGORITHM analyzes:                                  │
│     ├── Demographic data                                        │
│     ├── Interests & behavior                                    │
│     ├── Engagement patterns                                     │
│     ├── Purchase behavior                                       │
│     └── Cross-platform activity                                 │
│                                                                 │
│  3. LOOKALIKE OUTPUT                                            │
│     └── Top X% of people most similar to source                 │
│                                                                 │
│  Important: Source quality > Source size                         │
└─────────────────────────────────────────────────────────────────┘
```

## Source Audience Ranking

### Tier 1: Highest Quality (Recommended)

| Source Type | Min. Size | Why Effective |
|-------------|-----------|---------------|
| Purchasers (180d) | 500+ | Proven purchase intent |
| High-Value Customers (Top 20% LTV) | 200+ | Quality > quantity |
| Repeat Purchasers | 200+ | Loyalty signal |
| Subscribers (Email/SMS) | 1000+ | Active interest |

### Tier 2: Good Quality

| Source Type | Min. Size | Why Effective |
|-------------|-----------|---------------|
| Add to Cart (30d) | 500+ | High intent |
| Lead Form Completers | 300+ | Qualified interest |
| Checkout Initiators | 300+ | Near-purchasers |
| App Installers (Active) | 500+ | Engaged users |

### Tier 3: Usable but Less Specific

| Source Type | Min. Size | Why Effective |
|-------------|-----------|---------------|
| Website Visitors (30d) | 1000+ | Broad but relevant |
| Video Viewers 95% | 1000+ | High engagement |
| Page Engagers (90d) | 2000+ | Social interest |
| Content Viewers | 1000+ | Topic interest |

### Tier 4: Avoid as Source

```
DO NOT USE AS SOURCE:
├── All website visitors (too broad)
├── Video viewers <25% (low quality)
├── Page likes only (passive)
├── Very old data (>1 year)
└── Mixed audiences (purchasers + browsers)
```

## Percentage Selection Guide

### Percentage vs Reach Trade-off

```
LOOKALIKE PERCENTAGE SPECTRUM
=============================

1%  ████                    ~200K-500K people
    └── Most similar to source
    └── Best for: High-value products, limited budget

2%  ████████                ~400K-1M people
    └── Good balance of quality/reach
    └── Best for: General prospecting

3%  ████████████            ~600K-1.5M people
    └── Broader reach, still relevant
    └── Best for: Scalable campaigns

5%  ████████████████████    ~1M-2.5M people
    └── Large reach, more variation
    └── Best for: Awareness, large budgets

10% ████████████████████████████████████████  ~2M-5M people
    └── Very broad, limited similarity
    └── Best for: Maximum reach needed
```

### Percentage Selection Decision Tree

```
START: Which percentage should I choose?
│
├─► Question 1: What is your daily budget per ad set?
│   ├── <$20/day → Use 1-2%
│   ├── $20-50/day → Use 2-3%
│   ├── $50-100/day → Use 3-5%
│   └── >$100/day → Use 5-10%
│
├─► Question 2: What is your product type?
│   ├── High-ticket (>$200) → Use 1-2%
│   ├── Mid-range ($50-200) → Use 2-4%
│   └── Low-ticket (<$50) → Use 3-6%
│
├─► Question 3: What is your campaign goal?
│   ├── Pure performance/ROAS → Use 1-2%
│   ├── Balanced growth → Use 2-4%
│   └── Scale/volume → Use 4-6%
│
└─► RESULT: Choose percentage based on overlap
```

## Advanced Lookalike Strategies

### Strategy 1: Value-Based Lookalikes

```
STEPS:
1. Create Custom Audience of purchasers
2. During creation: "Include LTV" or purchase value
3. Meta optimizes for high-value matches

SETUP IN META:
├── Audiences → Create Audience → Custom Audience
├── Website → Purchase event
├── "Sort by value" or "Include value"
└── Create Lookalike from this audience

RESULT: LAL finds people who resemble your BEST customers
```

### Strategy 2: Layered Lookalikes

```
GOAL: Maximum reach without overlap

SETUP:
├── Ad Set 1: LAL 0-1% (most valuable)
│   └── Budget: 40% of LAL budget
│
├── Ad Set 2: LAL 1-3%
│   └── Exclude: LAL 0-1%
│   └── Budget: 35% of LAL budget
│
└── Ad Set 3: LAL 3-5%
    └── Exclude: LAL 0-3%
    └── Budget: 25% of LAL budget

BENEFIT: Test which layer performs best
```

### Strategy 3: Multi-Source Lookalikes

```
GOAL: Reach different customer segments

SETUP:
├── LAL 2%: Purchasers (all buyers)
├── LAL 2%: High-AOV Customers (>$150 orders)
├── LAL 2%: Repeat Purchasers (2+ orders)
├── LAL 2%: Email Engagers (opens/clicks)
└── LAL 2%: Video Completers (95% viewed)

IMPORTANT: Check overlap between these LALs!
Often 20-40% overlap, use exclusions if needed
```

### Strategy 4: Stacked Lookalikes

```
GOAL: Combine multiple high-intent sources

SETUP:
1. Create Super Source Audience:
   ├── Purchasers (180d) +
   ├── Repeat Purchasers +
   ├── High-Value Customers +
   └── Active Email Subscribers

2. Create LAL from combined audience

BENEFIT: Larger source = more data for algorithm
DRAWBACK: Can "dilute" signal if sources are too diverse
```

## Lookalike Troubleshooting

### Problem: LAL performs worse than Interest audiences

```
POSSIBLE CAUSES:
├── Source audience too small (<500)
├── Source audience too old (>180 days)
├── Source contains low-quality users
├── LAL percentage too broad for budget
└── Learning phase not completed

SOLUTIONS:
├── Upgrade to Tier 1 source (purchasers)
├── Refresh source with recent data
├── Filter source to high-value only
├── Lower percentage (e.g., 3% → 1%)
└── Increase budget or consolidate ad sets
```

### Problem: LAL has insufficient reach

```
POSSIBLE CAUSES:
├── Percentage too low for market
├── Too many exclusions active
├── Geographic targeting too narrow
└── Source too specific

SOLUTIONS:
├── Increase percentage (e.g., 1% → 3%)
├── Review and reduce exclusions
├── Expand geo targeting
└── Combine multiple sources
```

### Problem: LAL audience not growing

```
LOOKALIKE REFRESH CYCLE:
├── Meta updates LALs automatically every 3-7 days
├── Source audience must keep growing
└── Stagnation = source audience is stagnating

ACTION:
├── Check if source audience is still receiving events
├── Verify pixel/CAPI is working correctly
└── Consider a broader event as source
```

## Lookalike Creation Template

### When user asks for a LAL strategy:

```
LOOKALIKE STRATEGY TEMPLATE
============================

ACCOUNT INFO:
├── Monthly budget: [AMOUNT]
├── Current purchasers: [COUNT]
├── Product type: [TYPE]
└── Average order value: [AOV]

RECOMMENDED LOOKALIKES:

PRIMARY LAL (best chance of conversion):
├── Source: [Purchasers 180d / High-Value]
├── Percentage: [1-2%]
├── Estimated size: [XXX,XXX]
└── Budget allocation: 40-50%

SECONDARY LAL (scale potential):
├── Source: [Add to Cart / Leads]
├── Percentage: [2-3%]
├── Estimated size: [XXX,XXX]
└── Budget allocation: 30-35%

TERTIARY LAL (reach/awareness):
├── Source: [Engagers / Video Viewers]
├── Percentage: [3-5%]
├── Estimated size: [XXX,XXX]
└── Budget allocation: 15-25%

EXCLUSIONS SETUP:
├── All LALs: Exclude purchasers (30d)
├── Secondary: Exclude Primary LAL
└── Tertiary: Exclude Primary + Secondary
```

## Source Audience Optimization

### Checklist for Best Source Quality

```
SOURCE AUDIENCE CHECKLIST:

□ Minimum 1,000 people in source (ideal 5,000+)
□ Data is recent (last 180 days)
□ Based on conversion events (not pageviews)
□ Geographically relevant to target market
□ Contains no test/spam accounts
□ Value-based if available
□ Single intent (not mixed)
```

## Example Interaction

**User**: "I want to set up lookalike audiences but don't know which source to use. I have about 2,000 purchasers in the last 6 months."

**Claude response**:

"With 2,000 purchasers in 6 months, you have an excellent foundation for lookalikes! Here is my recommended strategy:

**Primary Lookalike (highest priority):**
- Source: Purchasers (180 days)
- Percentage: 1-2%
- Why: You have enough data for a strong signal

**Also consider a Value-Based LAL:**
- Source: Top 20% customers by order value
- Percentage: 1%
- Why: Finds people who resemble your BEST customers

**Questions to optimize further:**
1. Do you have access to order value data in your pixel events?
2. How many repeat purchasers do you have (2+ orders)?
3. What is your daily budget for prospecting?

With that info I can fine-tune the percentages and build out a layered strategy!"

## MCP Tool Usage

### Pull existing custom audiences to select the best LAL source:

```python
# List custom audiences to identify your highest-quality source options
meta_query(
    account_id="act_XXXXXXXXX",
    entity_type="adsets",
    effective_status=["ACTIVE"],
    fields=["id", "name", "targeting", "optimization_goal"]
)
# Note: Custom audience listing is not directly available via MCP tools.
# Use Ads Manager → Audiences to view custom audience details (subtype, size, last updated).
# The adsets query above shows which audiences are in use via targeting.custom_audiences.
```

Look for audiences with `approximate_count` > 1,000 and recent `time_updated`. Purchaser audiences (OFFLINE_CONVERSION or WEBSITE with Purchase event) in the 500–10,000 range are ideal LAL sources. Avoid audiences with counts below 300 or last updated more than 180 days ago.
