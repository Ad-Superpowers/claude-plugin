---
description: "Monitor your website's technical SEO health using Google Search Console. Checks sitemap status, indexing coverage, and inspects key pages for crawl issues, canonical conflicts, mobile usability problems, and rich results eligibility. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** google_search_console
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Technical SEO Health Check

Monitor technical SEO health via Google Search Console: sitemaps, indexing, crawl status, and page inspections.

- Site: [specify site_url]
- Pages to inspect: auto
- Check sitemaps: true

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### Overall Health: [HEALTHY / NEEDS ATTENTION / CRITICAL]

Score bands: HEALTHY = 0 critical issues, <=2 warnings. NEEDS ATTENTION = 1-2 critical or 3+ warnings. CRITICAL = 3+ critical issues.

### Sitemap Status
| Sitemap URL | URLs Submitted | Status | Last Downloaded | Errors | Warnings |
|-------------|---------------|--------|-----------------|--------|----------|
Flag: status != "Success", errors > 0, or last downloaded > 7 days ago.

### Indexing Estimate
| Metric | Value |
|--------|-------|
| Pages in sitemaps | X |
| Pages with impressions (confirmed indexed) | Y |
| Estimated index rate | Y/X % |

### Page Inspections
| Page | Indexed? | Last Crawl | Canonical OK? | Mobile OK? | Rich Results |
|------|----------|------------|--------------|------------|-------------|
Canonical OK = Google canonical matches user-declared canonical. Mobile OK = no usability issues.

### Critical Issues (fix now)
- [Issue description with affected page/sitemap and specific fix]

### Warnings
- [Warning description with affected page/sitemap and recommendation]

### Recommendations
1. [Most impactful fix]
2. [Second priority]
3. [Third priority]

## EXECUTION STEPS

### Step 1: Get site info and sitemaps
```
gsc_list_sites(include_sitemaps=true)
```
Find "[specify site_url]" in the results. Extract:
- Site verification status
- All sitemaps with their processing status, URL counts, errors, warnings, last downloaded date

> Conditional: if check_sitemaps

For each sitemap, flag:
- Processing errors or warnings > 0
- Last downloaded > 7 days ago (stale)
- URL count = 0 (empty sitemap)

### Step 2: Estimate indexing coverage
```
gsc_search_analytics(
    site_url="[specify site_url]",
    dimensions=["page"],
    days=28,
    row_limit=200
)
```
Count distinct pages with impressions = confirmed indexed and ranking pages.
Compare this count to the total URLs submitted in sitemaps to estimate index rate.

### Step 3: Identify top pages for inspection
```
gsc_search_analytics(
    site_url="[specify site_url]",
    dimensions=["page"],
    days=7,
    row_limit=10
)
```

> Conditional: if pages_to_inspect == "auto"

Auto-select pages to inspect (max 5 to stay within quota):
1. Homepage (derive from site_url)
2. Top 3 pages by clicks from the query above
3. A page from the sitemap that has 0 impressions (if identifiable)

> Otherwise

Inspect these specific pages: [specify pages_to_inspect]

### Step 4: Inspect key pages
For each selected page (max 5), run:
```
gsc_manage_url(
    action="inspect",
    site_url="[specify site_url]",
    url="PAGE_URL"
)
```
For each inspected page, extract:
- **Index status**: indexed / not indexed (+ reason if not indexed)
- **Last crawl date**: flag if > 30 days ago
- **Canonical URL**: compare Google-selected vs user-declared. Flag conflicts.
- **Mobile usability**: PASS or list issues
- **Rich results**: types detected or none
- **Page fetch status**: success / error
- **Robots.txt**: allowed / blocked

### Step 5: Classify issues
**CRITICAL** (fix now):
- Pages that should be indexed but are not
- Canonical conflicts (Google canonical != user canonical)
- Page fetch failures (server errors, redirects)
- Robots.txt blocking important pages

**WARNING** (fix soon):
- Mobile usability issues
- Stale sitemaps (last downloaded > 14 days)
- Sitemap errors > 0
- Last crawl > 30 days ago on important pages
- Low index rate (< 50% of sitemap URLs have impressions)

### Step 6: Compile report
Assign overall health status based on issue counts. Generate prioritized recommendations.

## EDGE CASES
- **No sitemaps found**: Note absence. Recommend creating and submitting an XML sitemap. Skip sitemap-related analysis but continue with page inspections.
- **URL Inspection API quota**: Limit is 2,000/day per property. Inspect max 5 pages. If user requests more, warn about quota and prioritize highest-traffic pages.
- **Domain property vs URL-prefix property**: `sc-domain:example.com` covers all subdomains; `https://www.example.com/` only covers that prefix. Note which type in the report.
- **Site not verified**: gsc_list_sites will not include it. Advise user to verify ownership in Google Search Console.
- **New site with no data**: Sitemaps may exist but no impressions yet. Focus on sitemap health and page inspection; skip indexing rate comparison.
- **Large site (>10K pages)**: Index rate estimate from 200-row sample will be rough. Note this limitation.