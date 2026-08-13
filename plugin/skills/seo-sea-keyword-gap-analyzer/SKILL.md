---
name: seo-sea-keyword-gap-analyzer
description: "This skill should be used when the user asks to \"compare organic and paid keywords\", \"find SEO SEA cannibalization\", \"stop bidding on organic rankings\", mentions \"keyword overlap between GSC and Google Ads\", \"paid-only keyword dependencies\", or \"budget savings from organic\". Do NOT use for: general GSC performance analysis (use gsc-performance-analyzer), Google Ads campaign optimization (use Google Ads platform skills), or competitor keyword research (use competitor-analysis-toolkit)."
---
# SEO vs SEA Keyword Gap Analyzer

## Purpose

Help agencies and advertisers identify where organic and paid search overlap, where gaps exist, and how to optimize budget allocation between SEO and SEA. This analysis typically saves 10-30% of wasted ad spend by identifying keywords where organic rankings make paid ads unnecessary.

## When to Use This Skill

Invoke when user mentions:
- **Gap analysis:** "Compare my organic and paid keywords"
- **Cannibalization:** "Am I paying for clicks I'd get for free?"
- **Budget optimization:** "Where can I save on Google Ads?"
- **Content opportunities:** "What keywords convert via ads but have no content?"
- **SEO vs SEA:** "Should I bid on keywords where I rank #1?"
- **Organic/paid overlap:** "Which keywords appear in both GSC and Google Ads?"

## Required Tools

| Tool | Purpose |
|------|---------|
| `gsc_search_analytics` | Organic keyword data (queries, clicks, impressions, CTR, position) |
| `google_ads_run_gaql` | Paid keyword data via GAQL query (clicks, impressions, cost, conversions) |

---

## Part 1: Data Collection Framework

### Step 1: Organic Data (GSC)

```
gsc_search_analytics(
    site_url="<property>",
    dimensions=["query"],
    days=28,
    row_limit=5000
)
```

Key fields: `query`, `clicks`, `impressions`, `ctr`, `position`

### Step 2: Paid Data (Google Ads)

```
google_ads_run_gaql(
    customer_id="<account>",
    query="SELECT campaign.name, ad_group.name,
        ad_group_criterion.keyword.text,
        ad_group_criterion.keyword.match_type,
        metrics.impressions, metrics.clicks, metrics.ctr,
        metrics.average_cpc, metrics.cost_micros,
        metrics.conversions
    FROM keyword_view
    WHERE segments.date DURING LAST_30_DAYS
    ORDER BY metrics.impressions DESC LIMIT 500"
)
```

Key fields: `keyword.text`, `clicks`, `impressions`, `cost_micros` (÷ 1,000,000), `conversions`

---

## Part 2: Four-Quadrant Gap Classification

### The SEO-SEA Matrix

```
                        ORGANIC STRONG              ORGANIC WEAK
                     (Position ≤ 5)              (Position > 10 or absent)
                 ┌─────────────────────────┬──────────────────────────┐
  PAID ACTIVE    │  Q1: CANNIBALIZATION     │  Q2: PAID-ONLY           │
  (Running ads)  │  → Test pausing ads      │  → Content opportunity   │
                 │  → Potential savings      │  → Build organic content │
                 │  Priority: HIGH           │  Priority: MEDIUM        │
                 ├─────────────────────────┼──────────────────────────┤
  PAID INACTIVE  │  Q3: ORGANIC WINNERS     │  Q4: BLIND SPOTS         │
  (No ads)       │  → No action needed      │  → Assess search volume  │
                 │  → Monitor rankings      │  → Decide: SEO or SEA?   │
                 │  Priority: LOW            │  Priority: VARIES        │
                 └─────────────────────────┴──────────────────────────┘
```

### Classification Rules

| Quadrant | Organic Position | Paid Status | Action |
|----------|-----------------|-------------|--------|
| Q1: Cannibalization | ≤ 5 | Active + spending | Test pausing ads, monitor organic |
| Q2: Paid-Only | > 10 or absent | Active + spending | Create content to reduce CPC dependency |
| Q3: Organic Winners | ≤ 5 | Not bidding | No ads needed — free traffic |
| Q4: Blind Spots | > 10 or absent | Not bidding | Evaluate: worth SEO or SEA investment? |

### Position Thresholds

| Category | Position Range | Interpretation |
|----------|---------------|----------------|
| Strong organic | 1-3 | Dominant — ads rarely needed |
| Good organic | 4-5 | Solid — test reducing ads |
| Striking distance | 6-10 | Invest in SEO, keep ads |
| Weak organic | 11-20 | Ads needed, plan content |
| Not ranking | > 20 or absent | Fully dependent on ads |

---

## Part 3: Cannibalization Analysis (Q1)

### When to Pause Ads

Pause ads on keywords where ALL of these are true:
1. Organic position ≤ 3
2. Organic CTR > 20%
3. The keyword is **not** a branded competitor term
4. Not in a highly competitive auction (CPC < €2 or below industry average)

### Incremental Lift Test

Before pausing, estimate incremental value:
- **Rule of thumb:** When organic is #1, paid ads add 10-20% incremental clicks
- **High-competition verticals:** Paid may add 30-50% incremental
- **Branded terms:** Organic captures 80-90% without ads

### Savings Estimation

```
potential_savings = sum(
    keyword.monthly_cost
    for keyword in q1_keywords
    if keyword.organic_position <= 3
    and keyword.organic_ctr > 0.20
    and keyword.is_branded == False
)
```

---

## Part 4: Content Gap Opportunities (Q2)

### Prioritization Framework

Score each paid-only keyword:

| Factor | Weight | Scoring |
|--------|--------|---------|
| Monthly conversions | 30% | High (>10): 3, Medium (3-10): 2, Low (<3): 1 |
| CPC | 25% | High (>€3): 3, Medium (€1-3): 2, Low (<€1): 1 |
| Monthly cost | 25% | High (>€500): 3, Medium (€100-500): 2, Low (<€100): 1 |
| Content feasibility | 20% | Easy (informational): 3, Medium (commercial): 2, Hard (transactional): 1 |

### Content ROI Estimate

```
monthly_organic_potential = keyword.paid_clicks × 0.6  # Assume 60% capture rate
time_to_rank = 3-6 months (informational) / 6-12 months (commercial)
content_cost = €200-500 per article
break_even_months = content_cost / (keyword.cpc × monthly_organic_potential)
```

Keywords with break-even < 6 months are high-priority content opportunities.

---

## Part 5: Output Format

```
================================================================================
                   SEO vs SEA KEYWORD GAP ANALYSIS
                   Property: [site_url]
                   Google Ads: [customer_id]
                   Period: Last 28 days
================================================================================

EXECUTIVE SUMMARY
─────────────────
Total organic keywords analyzed: [X]
Total paid keywords analyzed: [Y]
Overlap: [Z] keywords ([%])

POTENTIAL MONTHLY SAVINGS: €[amount]
CONTENT OPPORTUNITIES: [N] keywords worth €[monthly CPC] in ads

QUADRANT BREAKDOWN:
| Quadrant | Keywords | Monthly Spend | Action |
|----------|----------|--------------|--------|
| Q1: Cannibalization | [N] | €[X] | Test pausing |
| Q2: Paid-Only | [N] | €[X] | Create content |
| Q3: Organic Winners | [N] | €0 | Monitor |
| Q4: Blind Spots | [N] | €0 | Evaluate |

─────────────────────────────────────────────────────────
Q1: CANNIBALIZATION — Test Pausing These Ads
─────────────────────────────────────────────────────────
| Keyword | Org Pos | Org CTR | Paid Cost/mo | Paid Conv | Action |
|---------|---------|---------|-------------|-----------|--------|
| [kw]    | 1.2     | 28%     | €450        | 12        | Pause  |
| [kw]    | 2.5     | 22%     | €280        | 8         | Test   |

─────────────────────────────────────────────────────────
Q2: CONTENT OPPORTUNITIES — Write Content for These
─────────────────────────────────────────────────────────
| Keyword | CPC | Paid Cost/mo | Conversions | Content Priority |
|---------|-----|-------------|-------------|-----------------|
| [kw]    | €4.20 | €890      | 22          | HIGH            |
| [kw]    | €2.80 | €560      | 15          | HIGH            |

─────────────────────────────────────────────────────────
RECOMMENDATIONS
─────────────────────────────────────────────────────────
1. IMMEDIATE: Pause ads on [N] cannibalized keywords → Save ~€[X]/month
2. SHORT-TERM: Create content for top [N] paid-only keywords → Reduce CPC dependency
3. ONGOING: Monitor Q3 organic winners for ranking drops
```

---

## Part 6: Industry Benchmarks

### Expected Organic vs Paid Distribution

| Industry | % Organic Traffic | % Paid Traffic | Overlap Rate |
|----------|------------------|---------------|-------------|
| E-commerce | 35-45% | 55-65% | 20-30% |
| SaaS/B2B | 50-65% | 35-50% | 15-25% |
| Local Services | 40-55% | 45-60% | 25-35% |
| Finance | 30-40% | 60-70% | 30-40% |
| Health | 45-60% | 40-55% | 20-30% |
| Education | 55-70% | 30-45% | 10-20% |

### Healthy Cannibalization Rates

- **< 15% overlap:** Good balance — organic and paid target different terms
- **15-30% overlap:** Normal — review highest-spend overlaps
- **> 30% overlap:** High — significant savings opportunity
