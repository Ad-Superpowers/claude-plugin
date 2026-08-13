---
name: technical-seo-monitor
description: "This skill should be used when the user asks to \"fix indexing problems\", \"check sitemap health\", \"diagnose crawl issues\", or mentions \"pages not appearing in Google\", \"canonical URL conflicts\", or \"technical SEO audit\". Do NOT use for: organic search performance analysis or CTR optimization (use gsc-performance-analyzer)."
---
# Technical SEO Monitor

## Purpose

Diagnose and resolve technical SEO issues using Google Search Console data. This skill covers indexing status, sitemap health, crawl diagnostics, canonical issues, and mobile usability — the foundational technical elements that determine whether Google can find, crawl, and index your pages.

## When to Use This Skill

Invoke when user mentions:
- **Indexing:** "Why isn't my page showing up in Google?"
- **Sitemaps:** "Is my sitemap working correctly?"
- **Crawl issues:** "Google can't access my pages"
- **Canonical problems:** "Google is indexing the wrong URL"
- **Mobile issues:** "Mobile usability errors in Search Console"
- **Rich results:** "My structured data isn't showing"
- **Technical audit:** "Check my site's technical SEO health"
- **Deindexing:** "Pages were removed from Google's index"

## Required Tools

| Tool | Purpose |
|------|---------|
| `gsc_manage_url(action="inspect")` | Per-page indexing status and crawl diagnostics |
| `gsc_list_sites(include_sitemaps=true)` | Property overview with sitemap health and status |
| `gsc_manage_url(action="submit_sitemap")` | Submit new or updated sitemaps |
| `gsc_search_analytics` | Identify pages with impressions but no clicks (indexed but poor) |
| `gsc_search_analytics(dimensions=["page"])` | Page-level performance for cross-referencing |

---

## Part 1: Indexing Status Interpretation

### URL Inspection Verdicts

| Verdict | Meaning | Action |
|---------|---------|--------|
| `PASS` | URL is indexed and eligible to appear in search | No action needed |
| `NEUTRAL` | URL found but not indexed (not an error) | May be low value or duplicate |
| `FAIL` | URL has critical issues preventing indexing | Immediate investigation needed |
| `VERDICT_UNSPECIFIED` | No data available | Page may not have been crawled yet |

### Coverage States

| State | Meaning | Priority |
|-------|---------|----------|
| `Submitted and indexed` | In sitemap and indexed | OK |
| `Indexed, not submitted in sitemap` | Found via crawling, indexed | Low — add to sitemap |
| `Crawled - currently not indexed` | Crawled but Google chose not to index | Medium — improve content quality |
| `Discovered - currently not indexed` | Known to Google but not yet crawled | Low — will be crawled eventually |
| `Excluded by 'noindex' tag` | Intentionally excluded | OK if intentional |
| `Blocked by robots.txt` | Cannot be crawled | High — fix if page should be indexed |
| `URL is unknown to Google` | Never discovered | High — submit sitemap or add internal links |
| `Redirect` | URL redirects elsewhere | OK if intentional |
| `Soft 404` | Page returns 200 but appears empty/low value | High — add content or return 404 |
| `Not found (404)` | Page doesn't exist | Medium — redirect or remove links |
| `Server error (5xx)` | Server failed to respond | Critical — fix server issues |
| `Duplicate without user-selected canonical` | Duplicate, Google chose canonical | Low — set canonical tag if preferred |
| `Duplicate, Google chose different canonical` | Your canonical differs from Google's | Medium — investigate canonical conflict |

### Diagnosis Decision Tree

```
Page not appearing in Google?
│
├─► Run gsc_manage_url(site_url, action="inspect", url=page_url)
│   │
│   ├─► Verdict: PASS → Page IS indexed
│   │   └─► Check: Is it ranking for the right queries?
│   │       Use gsc_search_analytics with page_filter
│   │
│   ├─► Verdict: FAIL
│   │   ├─► robots.txt blocking? → Fix robots.txt
│   │   ├─► noindex tag? → Remove if page should be indexed
│   │   ├─► Server error? → Fix backend issues
│   │   └─► Soft 404? → Add meaningful content
│   │
│   ├─► Verdict: NEUTRAL (crawled, not indexed)
│   │   ├─► Thin content? → Expand to 300+ words
│   │   ├─► Duplicate? → Set canonical or consolidate
│   │   ├─► Low authority? → Add internal links
│   │   └─► Recently published? → Wait 1-2 weeks
│   │
│   └─► No data → Page never discovered
│       ├─► In sitemap? → Check gsc_list_sites(include_sitemaps=true)
│       ├─► Internal links? → Add links from indexed pages
│       └─► Submit sitemap with gsc_manage_url(action="submit_sitemap")
```

---

## Part 2: Sitemap Health Check

### Sitemap Status Indicators

| Status | Meaning | Action |
|--------|---------|--------|
| `Success` | Sitemap processed without errors | Healthy |
| `Pending` | Submitted but not yet processed | Wait (usually < 24h) |
| `Has errors` | Sitemap has parsing or URL errors | Fix errors |
| Warnings > 0 | Non-critical issues found | Review and fix |
| Errors > 0 | Critical issues found | Immediate fix needed |

### Sitemap Health Checklist

| Check | Good | Warning | Critical |
|-------|------|---------|----------|
| Processing status | Success | Pending > 48h | Has errors |
| URL count | Matches expected pages | Differs by > 20% | 0 URLs or missing |
| Last downloaded | < 7 days ago | 7-30 days ago | > 30 days ago |
| Errors | 0 | 1-5 | > 5 |
| Warnings | 0 | 1-10 | > 10 |
| URLs in index vs sitemap | > 80% indexed | 50-80% indexed | < 50% indexed |

### Common Sitemap Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| 0 URLs discovered | XML parsing error | Validate XML, check encoding |
| Not downloaded recently | robots.txt blocks sitemap | Add `Sitemap:` directive to robots.txt |
| Many URLs not indexed | Low quality or duplicate pages | Clean up sitemap, only include indexable URLs |
| Sitemap too large | > 50,000 URLs or > 50MB | Split into sitemap index with child sitemaps |
| Wrong URL format | HTTP vs HTTPS mismatch | Ensure all URLs match property URL scheme |

---

## Part 3: Canonical URL Diagnostics

### Canonical Conflicts

When `gsc_manage_url(action="inspect")` returns different `google_canonical` vs `user_canonical`:

| Scenario | Cause | Fix |
|----------|-------|-----|
| Google chose HTTPS, you set HTTP | HTTPS migration incomplete | Update canonicals to HTTPS |
| Google chose www, you set non-www | Mixed signals | Standardize + redirect |
| Google chose different page | Content overlap/duplication | Consolidate or differentiate content |
| Google ignoring your canonical | Canonical contradicts signals | Check: hreflang, internal links, sitemap consistency |
| No user canonical set | Missing `<link rel="canonical">` | Add canonical tags to all pages |

### Canonical Best Practices

1. Every page should have a self-referencing canonical tag
2. Canonical URL must be accessible (not 404, not redirect, not noindex)
3. Canonical should match the URL in sitemap
4. All internal links should point to the canonical version
5. Canonical must use the correct protocol (HTTPS) and domain (www vs non-www)

---

## Part 4: Core Web Vitals & Mobile Usability

### Core Web Vitals (as of 2024-2026)

Google uses Core Web Vitals as a ranking signal. The three active metrics are:

| Metric | What It Measures | Good | Needs Improvement | Poor |
|--------|-----------------|------|------------------|------|
| **LCP** (Largest Contentful Paint) | Loading speed of main content | < 2.5s | 2.5-4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | Responsiveness to user input | < 200ms | 200-500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | Visual stability | < 0.1 | 0.1-0.25 | > 0.25 |

> **INP replaced FID (First Input Delay) in March 2024.** INP measures the full interaction latency (from input to next frame paint), not just the initial response delay. If you have old references to FID in your performance reports, those are outdated. Focus on INP.

**Common INP issues:**
- Heavy JavaScript executing during user interactions
- Long tasks blocking the main thread
- React/Vue re-renders triggered by click handlers
- Third-party scripts (chat widgets, analytics) delaying response

### Mobile Verdicts from URL Inspection

| Issue | Impact | Fix |
|-------|--------|-----|
| Text too small to read | Poor mobile UX | Use min 16px font, responsive typography |
| Clickable elements too close | Accidental taps | Min 48px touch targets, 8px spacing |
| Content wider than screen | Horizontal scrolling | Set viewport meta, use responsive CSS |
| Viewport not set | Page not mobile-optimized | Add `<meta name="viewport" content="width=device-width, initial-scale=1">` |

---

## Part 5: Output Format

```
================================================================================
                     TECHNICAL SEO HEALTH CHECK
                     Property: [site_url]
                     Date: [YYYY-MM-DD]
================================================================================

OVERALL HEALTH: [HEALTHY / NEEDS ATTENTION / CRITICAL]

SITEMAP STATUS
──────────────
| Sitemap | URLs | Status | Last Downloaded | Errors | Warnings |
|---------|------|--------|-----------------|--------|----------|
| /sitemap.xml | 1,240 | Success | 2 days ago | 0 | 0 |
| /blog-sitemap.xml | 380 | Has errors | 5 days ago | 3 | 2 |

INDEXING SUMMARY (sampled pages)
────────────────────────────────
| Status | Count | % | Action |
|--------|-------|---|--------|
| Indexed | [X] | [Y%] | Monitor |
| Crawled, not indexed | [X] | [Y%] | Improve content quality |
| Discovered, not indexed | [X] | [Y%] | Wait or add internal links |
| Blocked/Excluded | [X] | [Y%] | Review if intentional |
| Errors | [X] | [Y%] | Fix immediately |

CRITICAL ISSUES (Fix Now)
─────────────────────────
1. [Issue description + affected URL + fix]
2. [Issue description + affected URL + fix]

WARNINGS (Plan to Fix)
──────────────────────
1. [Warning description + affected URL + fix]

CANONICAL ISSUES
────────────────
| Page | Your Canonical | Google's Canonical | Issue |
|------|---------------|-------------------|-------|
| [url] | [url] | [different url] | Google chose different page |

RECOMMENDATIONS
───────────────
1. CRITICAL: [Most important fix]
2. HIGH: [Second priority]
3. MEDIUM: [Third priority]
```

---

## Part 6: Monitoring Cadence

| Check | Frequency | Tool |
|-------|-----------|------|
| Sitemap status | Weekly | `gsc_list_sites(include_sitemaps=true)` |
| Key page indexing | Weekly | `gsc_manage_url(action="inspect")` (sample 10-20 pages) |
| Overall impressions trend | Weekly | `gsc_search_analytics` with `dimensions=["date"]` |
| New page indexing | Within 48h of publish | `gsc_manage_url(action="inspect")` |
| After technical changes | Immediately | `gsc_manage_url(action="inspect")` + `gsc_list_sites(include_sitemaps=true)` |
| Full technical audit | Monthly | All GSC tools combined |

### AI Overviews: Technical SEO Implications

Google AI Overviews (launched broadly 2024) directly affect organic performance. From a technical SEO perspective:

- **Structured data matters more:** Pages with well-implemented schema (FAQ, HowTo, Article) are more likely to be cited in AI Overviews
- **E-E-A-T signals:** Author markup, About pages, and expertise signals help Google trust your content for AI sourcing
- **Indexing is still required:** Pages must be indexed to appear in AI Overviews
- **Monitor CTR separately:** Impressions may remain stable while clicks drop — this is often AI Overviews, not an indexing problem

```
gsc_search_analytics(site_url="...", dimensions=["query"], days=90)
```

Compare CTR trends against position trends. If position is stable but CTR is declining on informational queries, AI Overviews are likely the cause — not a technical issue.
