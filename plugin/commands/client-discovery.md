---
description: Comprehensive client research combining deep research with optional ad account analysis. Gathers company intel, competitive landscape, and advertising history in one structured workflow. (requires Pro subscription)
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Client Discovery & Intelligence Gathering

Conduct comprehensive client research to build a complete profile for [specify company_name]. Combines external research with optional ad platform data. Works with or without connected ad accounts.

## Parameters
- Company: [specify company_name]
- Website: Not provided
- Industry: To be determined
- Research Depth: standard (quick = overview only, standard = full research + platform data, comprehensive = deep analysis + 5+ competitors + trends)

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### Executive Summary

2-3 sentences summarizing the company, its market position, and key advertising opportunity areas. Write as if briefing a new account manager.

### Company Snapshot

| Attribute | Details |
|-----------|---------|
| Industry | [Industry/vertical] |
| Business Model | [B2B/B2C/D2C/Marketplace/SaaS/etc.] |
| Company Size | [Employees] |
| Revenue | [If public/available] |
| Founded | [Year] |
| Headquarters | [Location] |
| Website | [URL] |

### Target Market

**Primary Audience:**
- Demographics: [Age, gender, location]
- Psychographics: [Interests, values, lifestyle]
- B2B specifics (if applicable): [Industry, company size, job titles]

**Secondary Audiences:**
1. [Audience segment 1]
2. [Audience segment 2]

### Products & Services

| Offering | Price Point | Target Segment |
|----------|-------------|----------------|
| [Product 1] | [X] | [Segment] |
| [Product 2] | [X] | [Segment] |

Estimated AOV: [X] | Estimated CLV: [X]

### Competitive Landscape

| Competitor | Strength | Weakness | Ad Activity |
|------------|----------|----------|-------------|
| [Competitor 1] | [Key strength] | [Key weakness] | [High/Med/Low] |
| [Competitor 2] | [Key strength] | [Key weakness] | [High/Med/Low] |
| [Competitor 3] | [Key strength] | [Key weakness] | [High/Med/Low] |

Competitive position: [How [specify company_name] differentiates]
Opportunity gaps: [Underserved areas competitors miss]

### Digital Presence Score

| Channel | Score (1-10) | Notes | Opportunity |
|---------|-------------|-------|-------------|
| Website | [X] | [Notes] | [High/Med/Low] |
| SEO | [X] | [Notes] | [High/Med/Low] |
| Social (Meta) | [X] | [X followers] | [High/Med/Low] |
| Social (LinkedIn) | [X] | [X followers] | [High/Med/Low] |
| Social (TikTok) | [X] | [X followers] | [High/Med/Low] |
| Content/Blog | [X] | [Notes] | [High/Med/Low] |
| Email Marketing | [X] | [Notes] | [High/Med/Low] |

Overall Digital Maturity: [Beginner / Developing / Established / Advanced]

### Advertising History (if platform data available)

| Platform | 90-Day Spend | Key Metrics | Status |
|----------|-------------|-------------|--------|
| Meta Ads | [X] | ROAS: X.X, CPA: [X] | [Active/Paused] |
| Google Ads | [X] | Conv: XXX, CPA: [X] | [Active/Paused] |
| LinkedIn | [X] | Leads: XX, CPL: [X] | [Active/Paused] |
| TikTok | [X] | ROAS: X.X | [Active/Paused] |

Best performing platform: [Platform] (why)
Highest potential platform: [Platform] (why)

### Key Insights & Opportunities

1. **[Insight 1 Title]**: [Observation with data] — Opportunity: [Specific action]
2. **[Insight 2 Title]**: [Observation with data] — Opportunity: [Specific action]
3. **[Insight 3 Title]**: [Observation with data] — Opportunity: [Specific action]

### Risks & Considerations

- [Risk 1]: [Description and mitigation]
- [Risk 2]: [Description and mitigation]

### Recommended Next Steps

1. **Immediate**: [First priority action]
2. **This Week**: [Second priority action]
3. **This Month**: [Longer-term action]

### Suggested Workflows to Run Next

- [ ] Market Sizing (if budget planning needed)
- [ ] Buyer Persona Builder (if audience unclear)
- [ ] Landing Page Analyzer (if conversion focus)
- [ ] Competitive Landscape Analyzer (if competitive intel needed)

## EXECUTION STEPS

### Step 1: Research the Company

Use web search and crawling tools to gather company intelligence:
- Business model, revenue streams, products/services
- Target market and customer segments
- Company size, founding date, leadership, recent news
- Funding history (if startup/private)

Crawl [specify company_website] to extract:
- Value proposition (homepage hero)
- Products/services structure
- Target audience signals (language, imagery)
- Trust signals (testimonials, certifications, press)
- Conversion points (CTAs, forms, pricing)


### Step 2: Analyze Digital Presence

Research [specify company_name]'s digital footprint:
- Website traffic estimates
- Social media presence and follower counts
- Content marketing strategy and SEO visibility
- Tech stack signals
- Customer reviews and sentiment

### Step 3: Map Competitive Landscape

Identify [specify company_name]'s competitors:
- Top 3-5 direct competitors (5+ if comprehensive depth)
- Market positioning and pricing comparison
- Unique value propositions
- Competitive advantages and weaknesses

### Step 4: Gather Platform Data (if connected)

{% if research_depth in ["standard", "comprehensive"] %}For each connected platform, gather 90-day performance:

**Meta Ads:**
- `meta_get_insights(account_id=account_id, date_preset="last_90d", level="account", fields=["spend", "impressions", "clicks", "actions", "action_values", "purchase_roas"])`
- `meta_query(account_id=account_id, entity_type="campaigns", effective_status=["ACTIVE", "PAUSED"])`

**Google Ads:**
- `google_ads_run_gaql(customer_id=customer_id, query="SELECT campaign.id, campaign.name, campaign.status, metrics.impressions, metrics.clicks, metrics.ctr, metrics.average_cpc, metrics.cost_micros, metrics.conversions, metrics.conversions_value FROM campaign WHERE segments.date DURING LAST_90_DAYS ORDER BY metrics.cost_micros DESC")`

**LinkedIn Ads:**
- `linkedin_get_analytics(account_id=account_id, date_range="last 90 days", time_granularity="MONTHLY")`

**TikTok Ads:**
- `tiktok_get_report(date_range="last 90 days", level="campaign")`

**GA4 (traffic context):**
- `ga4_run_report(property_id=property_id, metrics=["sessions", "totalUsers", "newUsers"], dimensions=["sessionDefaultChannelGrouping"], start_date="90daysAgo", end_date="today")`


### Step 5: Synthesize Findings

Combine research and platform data into the output format above. Cross-reference external research with actual platform performance. Highlight discrepancies (e.g., strong brand but weak ad performance). Prioritize insights by actionability.

## EDGE CASES

- **No ad accounts connected**: Produce a research-only report. Skip the Advertising History section and note that platform data will enrich the profile once accounts are connected.
- **Private company (limited data)**: Rely on website analysis, social signals, job postings, and press mentions. Note confidence level as "Low — limited public data" in the executive summary.
- **New company (<1 year old)**: Focus on founding team background, initial traction signals, and market opportunity rather than historical performance. Flag that benchmarks may not apply.
- **No website provided**: Use web search to find the website. If none exists, flag this as a critical gap and adjust Digital Presence Score accordingly.
- **Non-English market**: Note the primary market language. Adjust competitor research to include local players. Flag if ad platform tools may return limited data for non-English keywords.