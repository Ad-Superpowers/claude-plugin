---
description: "Comprehensive competitive analysis combining deep research with ad platform data. Includes competitor profiling, positioning maps, spend estimation, creative analysis, and strategic recommendations. Integrates Google Ads auction insights and Meta Ad Library research. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Competitive Intelligence & Ad Strategy Analysis

Conduct competitive analysis for [specify company_name] in [specify industry].
Known competitors: To be discovered.
Focus: general.

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### EXECUTIVE SUMMARY
- Competitive landscape overview (2-3 sentences)
- [specify company_name]'s position: [leader/challenger/niche/new entrant]
- Top 3 threats with threat level (High/Medium/Low)
- Top 3 opportunities (gaps in competitor coverage)

### COMPETITOR PROFILES (top 3-5)
For each competitor:
| Attribute | Details |
|-----------|---------|
| Website | [URL] |
| Size/Revenue | [estimate] |
| Target Audience | [segments] |
| Value Proposition | [their main pitch] |
| Strengths | [2-3 bullets] |
| Weaknesses | [2-3 bullets] |

### AD PRESENCE OVERVIEW
| Competitor | Meta Ads | Google Ads | LinkedIn | TikTok | Est. Monthly Spend |
|------------|----------|------------|----------|--------|-------------------|

### COMPETITIVE THREAT MATRIX
| Competitor | Market Share /10 | Ad Aggressiveness /10 | Brand Strength /10 | Innovation /10 | Total /40 | Trend |
|------------|-----------------|----------------------|--------------------|----|-----------|-------|
30-40: Critical | 20-29: Significant | 10-19: Moderate | <10: Low

### POSITIONING MAP
Axes: [Dimension 1] (Low-High) x [Dimension 2] (Low-High)
| Company | X Position | Y Position | Quadrant |
|---------|-----------|-----------|----------|
White space opportunities: [underserved positions]

### STRATEGIC RECOMMENDATIONS
**Defensive:** [protect against top threats]
**Offensive:** [exploit competitor gaps]
**Messaging differentiation:**
| Angle | Why It Works | Competitors Not Using |
|-------|-------------|---------------------|

**Positioning statement:** "For [audience] who [need], [specify company_name] is the [category] that [differentiator]. Unlike [competitors], we [unique benefit]."

### BUDGET BENCHMARKING
| Scenario | Monthly Budget | Expected SOV | Position |
|----------|---------------|-------------|----------|
| Maintain | [amount] | XX% | Hold current |
| Grow | [amount] | XX% | Match top competitor |
| Dominate | [amount] | XX% | Market leader |

## EXECUTION STEPS

### Step 1: Gather Platform Data
- `meta_list_ad_accounts()` -> check connected accounts
- `google_ads_list_accounts()` -> get customer IDs
- `linkedin_list_ad_accounts()` -> check LinkedIn presence
- `tiktok_get_advertiser_info()` -> check TikTok presence

### Step 2: Google Ads Auction Insights (if available)
```
google_ads_run_gaql(
    customer_id="FROM_STEP_1",
    query="SELECT campaign.name, auction_insight.domain, metrics.auction_insight_search_impression_share, metrics.auction_insight_search_top_impression_percentage, metrics.auction_insight_search_outranking_share, metrics.auction_insight_search_overlap_rate, metrics.auction_insight_search_position_above_rate FROM auction_insight WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.auction_insight_search_impression_share DESC LIMIT 20"
)
```

**Auction Insights interpretation:**
| Metric | Meaning | Good Benchmark |
|--------|---------|---------------|
| Impression Share | How often you appear vs competitors | >50% brand, >15% generic |
| Top of Page Rate | Above organic results | >70% brand terms |
| Overlap Rate | Competitor appears with you | Monitor high overlaps |
| Position Above Rate | Competitor ranks above you | <50% = you're winning |
| Outranking Share | You rank higher or show alone | Higher = better |

### Step 3: Competitor Research

Use web search tools (if available) to research for each competitor:
1. **Discovery:** Top 5-10 competitors (direct, indirect, emerging) - company, website, size, products, funding
2. **Positioning:** Value proposition, target audience, pricing (premium/mid/budget), key messaging
3. **Digital presence:** Social following, SEO visibility, review ratings

### Step 4: Ad Library Research

**Meta Ad Library** (facebook.com/ads/library): For each competitor document active ad count, formats (video/image/carousel), messaging themes, CTAs, refresh frequency.

**LinkedIn:** Check competitor pages > Posts > Ads for B2B ad formats and content offers.

**TikTok Creative Center** (ads.tiktok.com/business/creativecenter): Search for industry keywords, analyze top formats and hooks.

### Step 5: Estimate Competitor Spend

**Method 1 - Platform clues:** Meta active ads x 50-200/day | LinkedIn ads x 100-300/day | Google impression share indicates relative spend

**Method 2 - Company size benchmarks:**
| Size | Typical Monthly Ad Budget |
|------|--------------------------|
| Startup (<20 emp) | 1K-10K |
| SMB (20-100) | 10K-50K |
| Mid-market (100-500) | 50K-200K |
| Enterprise (500+) | 200K+ |

### Step 6: Analyze & Score

**Threat scoring (per competitor):**
- Market Share (1-10): estimated share of target market
- Ad Aggressiveness (1-10): volume and frequency of advertising
- Brand Strength (1-10): recognition and reputation
- Innovation (1-10): product/service innovation pace

**Positioning map axes** (pick most relevant for [specify industry]):
Price (Low-Premium) | Quality (Basic-Advanced) | Market (SMB-Enterprise) | Approach (Traditional-Innovative) | Focus (Generalist-Specialist)

### Step 7: Present Results
Follow OUTPUT FORMAT above. Include competitor profiles, threat matrix, positioning map, and actionable recommendations.

## EDGE CASES
- No Google Ads connected: Skip auction insights, rely on ad library research and web research
- No known competitors provided: Use web research to discover top 5-10 based on industry
- No ad accounts connected at all: Pure research-based analysis using ad libraries and web search
- Only 1 competitor known: Expand discovery to find 4+ additional competitors
- Niche industry with few competitors: Include adjacent industry competitors, note smaller competitive set
- API errors: Note the error, continue with available data sources