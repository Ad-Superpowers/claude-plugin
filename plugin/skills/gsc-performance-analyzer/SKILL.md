---
name: gsc-performance-analyzer
description: "This skill should be used when the user asks to \"analyze GSC performance\", \"optimize organic CTR\", \"check keyword rankings\", or mentions \"position tracking\", \"seasonal SEO trends\", or \"Google Discover performance\". Do NOT use for: indexing problems or technical SEO issues (use technical-seo-monitor)."
---
# GSC Performance Analyzer

## Purpose

Provide expert-level interpretation of Google Search Console data. Transform raw metrics (clicks, impressions, CTR, position) into actionable SEO insights with proper context for benchmarks, seasonality, and data quality.

## When to Use This Skill

Invoke when user mentions:
- **Performance analysis:** "How is my organic search doing?"
- **CTR optimization:** "My CTR is low, what should I do?"
- **Position tracking:** "Am I ranking well for this keyword?"
- **Trends:** "Why did my traffic drop last week?"
- **Search appearances:** "What are rich results?"
- **Discover/News:** "How is my content doing in Google Discover?"
- **Data quality:** "Is my GSC data accurate?"

## Required Tools

| Tool | Purpose |
|------|---------|
| `gsc_search_analytics` | All organic search data queries |
| `gsc_list_sites` | Property discovery |
| `gsc_manage_url(action="inspect")` | Page-level indexing diagnostics |
| `gsc_search_analytics(dimensions=["page"])` | Page-level performance overview |

---

## Part 1: CTR Benchmarks by Position

### Expected CTR by Average Position (Web Search, 2024-2026 data)

> **AI Overviews impact:** Google AI Overviews (formerly SGE) are shown for a large portion of informational queries. For queries where an AI Overview appears, CTR for positions 1-3 can drop 20-60% compared to the benchmarks below. The effect is strongest on "what is", "how to", and definition queries. Navigational, commercial, and brand queries are less affected.

| Position | Expected CTR | Range | Interpretation |
|----------|-------------|-------|----------------|
| 1 | 27-32% | 22-39% | #1 should capture ~30% of clicks — lower if AI Overview shown |
| 2 | 15-18% | 12-22% | Strong second position |
| 3 | 10-13% | 8-16% | Still above the fold |
| 4 | 7-9% | 5-11% | Often below ads on mobile |
| 5 | 5-7% | 3-9% | Bottom of first visible results |
| 6-7 | 3-5% | 2-6% | Requires scrolling on mobile |
| 8-10 | 2-3% | 1-4% | Bottom of page 1 |
| 11-20 | 0.5-1.5% | 0.2-2% | Page 2 — very few clicks |

### CTR Modifiers

| Factor | CTR Impact | Notes |
|--------|-----------|-------|
| AI Overview present | -20-60% | Informational queries most affected; answer shown inline |
| Rich snippets (FAQ, How-to) | +20-50% | Higher visibility, more SERP real estate |
| Sitelinks | +15-30% | Authority signal, more click targets |
| Featured snippet (position 0) | +40-80% | Dominates SERP, but may reduce position 1 CTR |
| Brand query | +50-100% | Users specifically looking for you |
| Long-tail (4+ words) | +10-20% | Higher intent, less competition |
| SERP features (maps, shopping) | -10-30% | Competing visual elements push organic down |
| Ads above organic | -15-25% | Especially on mobile, ads push organic below fold |

### CTR Diagnosis Framework

```
IF actual_ctr > expected_ctr × 1.3:
    → Excellent! Strong titles/meta descriptions
    → Consider: Are you getting enough impressions?

IF actual_ctr is within ±30% of expected:
    → Normal performance for this position
    → Focus on improving position rather than CTR

IF actual_ctr < expected_ctr × 0.7:
    → Below expected — investigate:
    1. Title tag: Is it compelling? Under 60 chars?
    2. Meta description: Does it include a CTA? Under 155 chars?
    3. SERP features: Are rich results/ads pushing you down?
    4. Search intent mismatch: Does your page match what searchers want?
    5. Competing sitelinks: Does a competitor have expanded sitelinks?
```

---

## Part 2: Performance Patterns

### Seasonal Analysis

To detect seasonality, query with `dimensions=["date"]` over 90+ days:

| Pattern | Detection | Action |
|---------|-----------|--------|
| Weekly cycle | Compare Mon-Sun averages | B2B: weekday peaks; B2C: weekend peaks |
| Monthly cycle | Compare week-over-week | E-commerce: paycheck cycles, month-end |
| Seasonal | Compare month-over-month | Holiday, weather, industry events |
| Trend | 3-month moving average | Gradual decline = content aging; rise = growing authority |

### Common Traffic Drop Causes

| Symptom | Likely Cause | Diagnosis |
|---------|-------------|-----------|
| All queries drop equally | Algorithm update | Check Google Search Status dashboard |
| Specific page drops | Lost ranking for key terms | Check position changes for that page |
| Impressions stable, clicks drop, position stable | AI Overviews absorbing clicks | Check if query type is informational; AI Overview is answering the question in SERP |
| Impressions up, clicks down | Position dropped below fold OR AI Overview | CTR decline with impression growth; check query types |
| Impressions down, CTR stable | Lost rankings broadly | Compare positions period-over-period |
| Single-day cliff | Technical issue | Check `gsc_manage_url(action="inspect")` for crawl errors |
| Gradual decline over weeks | Content freshness decay or AI Overview rollout | Content needs updating; check if informational queries are affected |
| Mobile-only drop | Mobile usability issue | Check mobile-specific metrics |

---

## Part 3: Search Type Analysis

### Web (Default)

Standard organic search results. Primary metric for most sites.

### Google Discover

```
gsc_search_analytics(site_url="...", search_type="discover", days=28)
```

| Metric | Good | Average | Poor |
|--------|------|---------|------|
| CTR | > 8% | 4-8% | < 4% |
| Impressions/article | > 5,000 | 1,000-5,000 | < 1,000 |

Discover optimization:
- Large, high-quality images (min 1200px wide)
- Compelling, non-clickbait titles
- E-E-A-T signals (author bios, expertise)
- Fresh, timely content
- Topics the user has shown interest in (personalized)

### Google News

```
gsc_search_analytics(site_url="...", search_type="news", days=28)
```

News-specific considerations:
- Timeliness is critical (24-72 hour window)
- Headline quality directly impacts CTR
- Structured data (NewsArticle schema) improves visibility

### Image Search

```
gsc_search_analytics(site_url="...", search_type="image", days=28)
```

Image optimization:
- Descriptive alt text
- Relevant file names
- Proper image sitemaps
- WebP format for speed

---

## Part 4: Data Quality Guide

### Data Freshness

| Data State | Availability | Accuracy |
|------------|-------------|----------|
| `final` (default) | 3-4 days delay | High — confirmed data |
| `all` | 1-2 days delay | Medium — may be revised |

### Known Limitations

| Limitation | Impact | Workaround |
|-----------|--------|------------|
| Max 16 months history | Can't compare YoY beyond 16 months | Export monthly for long-term tracking |
| 25,000 row limit per query | Large sites may miss long-tail data | Use filters to segment queries |
| Position is average | Position 5.3 could be 1 sometimes, 10 others | Add date dimension for daily positions |
| Anonymized queries | Very low-volume queries hidden | ~10-20% of impressions may be anonymized |
| Click/impression counting | Deduplicated per query per day per user | Lower than raw pageview counts |
| Fresh data revisions | "all" data may change after finalization | Use "final" for reporting |

### Sampling

GSC does NOT sample data (unlike GA4). All reported metrics are based on actual data. However:
- Very rare queries may be anonymized (privacy threshold)
- Position is an average — a query at position 1 and position 20 shows as 10.5

---

## Part 5: Output Format

```
================================================================================
                     ORGANIC SEARCH PERFORMANCE ANALYSIS
                     Property: [site_url]
                     Period: [start_date] to [end_date]
================================================================================

EXECUTIVE SUMMARY
─────────────────
Total clicks: [X] ([+/-Y%] vs previous period)
Total impressions: [X] ([+/-Y%])
Average CTR: [X%] (benchmark: [Y%] for avg position [Z])
Average position: [X] ([improved/declined] by [Y])

HEALTH ASSESSMENT: [STRONG / STABLE / DECLINING / NEEDS ATTENTION]

TOP PERFORMING QUERIES (by clicks)
───────────────────────────────────
| Query | Clicks | Impressions | CTR | Position | CTR vs Benchmark |
|-------|--------|-------------|-----|----------|-----------------|
| [kw]  | 450    | 12,000      | 3.8%| 4.2      | Normal ✓        |
| [kw]  | 320    | 8,500       | 3.8%| 2.1      | LOW ⚠️ (expect 15-18%) |

CTR OPTIMIZATION OPPORTUNITIES
──────────────────────────────
Keywords where CTR is significantly below benchmark for their position:

| Query | Position | Actual CTR | Expected CTR | Gap | Fix |
|-------|----------|-----------|-------------|-----|-----|
| [kw]  | 1.5      | 12%       | 28-32%      | -16% | Improve title tag — OR check if AI Overview present |
| [kw]  | 3.2      | 4%        | 10-13%      | -6%  | Add rich snippets |

Note: If an AI Overview is shown for an informational query, low CTR at positions 1-3 is expected and may not be fixable via on-page optimization. The strategic response is to target commercial/navigational queries where AI Overviews are less prevalent, or to optimize content to be cited within the AI Overview itself (structured data, E-E-A-T).

TREND ANALYSIS
──────────────
[Week-over-week or day-over-day trend observations]

SEARCH TYPE BREAKDOWN
─────────────────────
| Type | Clicks | Impressions | CTR | Trend |
|------|--------|-------------|-----|-------|
| Web | [X] | [Y] | [Z%] | [↑↓→] |
| Discover | [X] | [Y] | [Z%] | [↑↓→] |
| Image | [X] | [Y] | [Z%] | [↑↓→] |

RECOMMENDATIONS
───────────────
1. [Highest-impact recommendation]
2. [Second recommendation]
3. [Third recommendation]
```
