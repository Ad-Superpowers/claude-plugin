---
description: "Comprehensive landing page analysis combining page crawling, GA4 performance data, and CRO best practices. Identifies conversion opportunities and provides actionable recommendations. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# CRO & Landing Page Quality Assessment

Analyze [specify landing_page_url] for conversion optimization.

**Objective:** [specify campaign_objective]
**Audience:** Not specified
**Industry:** General

> Conditional: if ad_copy
**Ad Copy:** [specify ad_copy]

> Conditional: if ga4_property_id
**GA4 Property:** [specify ga4_property_id]

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### OVERALL SCORE: [XX]/100
[2-3 sentence summary of conversion potential]

### CONVERSION SCORECARD
| Category | Score | Status | Priority Fix |
|----------|-------|--------|-------------|
| Message Match | [X]/20 | [Good/Needs Work/Critical] | [Yes/No] |
| Value Proposition | [X]/20 | ... | ... |
| Trust & Credibility | [X]/15 | ... | ... |
| CTA Effectiveness | [X]/15 | ... | ... |
| Form Optimization | [X]/10 | ... | ... |
| Mobile Experience | [X]/10 | ... | ... |
| Technical Performance | [X]/10 | ... | ... |
| **TOTAL** | **[XX]/100** | | |

80-100: Excellent | 60-79: Good | 40-59: Needs work | <40: Major overhaul

### TOP 3 ISSUES
1. [Critical issue] - Est. impact: +[X]% conversion rate
2. [Important issue] - Est. impact: +[X]% conversion rate
3. [Secondary issue] - Est. impact: +[X]% conversion rate

### QUICK WINS (< 1 hour)
- [Quick fix 1]
- [Quick fix 2]

### A/B TEST SUGGESTIONS
| Test | Hypothesis | Priority | Expected Lift |
|------|-----------|----------|--------------|
| [Test 1] | If [change], then [outcome] because [reason] | High | +[X]% |

### PROJECTED IMPACT
| Metric | Current | Projected | Improvement |
|--------|---------|-----------|------------|
| Conversion Rate | [X]% | [X]% | +[X]% |
| CPA | [amount] | [amount] | -[X]% |
| Monthly Conversions | [X] | [X] | +[X] |

## EXECUTION STEPS

### Step 1: Crawl the Page

Extract from [specify landing_page_url]:
- **Hero section:** H1 headline, subheadline, hero image/video, primary CTA
- **Value proposition:** Benefits listed, USPs, problem/solution framing
- **Trust signals:** Logos, testimonials, reviews, certifications, press mentions, guarantees
- **Conversion elements:** CTA buttons (text, placement, count), forms (fields, length), pricing, risk reducers
- **Technical:** Meta title/description, mobile responsiveness, tracking pixels

If no crawl tools available, visit the page manually and document these elements.

### Step 2: GA4 Performance Data (if available)

**Page performance:**
`ga4_run_report(property_id="[specify ga4_property_id]", start_date="30daysAgo", end_date="yesterday", metrics=["sessions","conversions","bounceRate","averageSessionDuration"], dimensions=["landingPage"])`

**Traffic sources:**
`ga4_run_report(property_id="[specify ga4_property_id]", start_date="30daysAgo", end_date="yesterday", metrics=["sessions","conversions"], dimensions=["sessionSource","sessionMedium"])`

**Device breakdown:**
`ga4_run_report(property_id="[specify ga4_property_id]", start_date="30daysAgo", end_date="yesterday", metrics=["sessions","conversions","bounceRate"], dimensions=["deviceCategory"])`

### Step 3: Score Each Category

**Message Match (20 pts):**
- Headline matches ad promise: 0-8 pts
- Visual continuity from ad: 0-6 pts
- Offer consistency: 0-6 pts

**Value Proposition (20 pts):**
- Clear within 5 seconds: 0-8 pts
- Unique vs competitors: 0-6 pts
- Benefit-focused (not feature-focused): 0-6 pts

**Trust & Credibility (15 pts):**
- Testimonials/reviews: 0-4 pts
- Logos/social proof: 0-4 pts
- Certifications/guarantees: 0-4 pts
- Contact info visible: 0-3 pts

**CTA Effectiveness (15 pts):**
- Clear action verb: 0-4 pts
- Visible above fold: 0-4 pts
- Value-focused text (not "Submit"): 0-4 pts
- Contrasting color: 0-3 pts

**Form Optimization (10 pts):**
- Appropriate field count: 0-4 pts (Lead Gen: 3-5, Signup: 2-3, Download: 2-3)
- Clear labels: 0-3 pts
- Error handling: 0-3 pts

**Mobile Experience (10 pts):**
- Responsive layout: 0-4 pts
- Touch-friendly CTAs (min 44x44px): 0-3 pts
- Readable text (min 16px): 0-3 pts

**Technical Performance (10 pts):**
- Load speed (<3s): 0-4 pts
- Tracking pixels (Meta/Google/LinkedIn/TikTok): 0-3 pts
- No broken elements, SSL: 0-3 pts

### Step 4: Benchmark Against Industry

| Objective | Poor | Average | Good | Excellent |
|-----------|------|---------|------|-----------|
| Lead Gen (B2B) | <2% | 2-5% | 5-10% | >10% |
| Lead Gen (B2C) | <3% | 3-8% | 8-15% | >15% |
| E-commerce | <1% | 1-3% | 3-5% | >5% |
| SaaS Signup | <2% | 2-5% | 5-10% | >10% |

Bounce rate: Landing page <40% = good, 40-70% = average, >70% = poor.

### Step 5: Present Results
Follow OUTPUT FORMAT above. Prioritize recommendations by impact and effort. Include specific "how to fix" instructions for each issue.

## EDGE CASES
- Page cannot be crawled: Ask user to provide screenshots or describe page elements manually
- No GA4 connected: Score based on page analysis only, use industry benchmarks for comparison
- No ad copy provided: Skip message match scoring, note it as untestable
- Page is behind login/paywall: Ask user for screenshots, score what's visible
- Mobile-only landing page: Skip desktop analysis, focus entirely on mobile UX
- Multiple landing pages: Analyze each separately, provide comparison table