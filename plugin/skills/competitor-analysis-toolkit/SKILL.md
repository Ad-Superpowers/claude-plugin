---
name: competitor-analysis-toolkit
description: "This skill should be used when the user asks to \"analyze competitor ads\", \"estimate competitor ad spend\", \"research competitors in Meta Ad Library\", mentions \"share of voice\", \"auction insights\", or \"competitive positioning strategy\". Do NOT use for: keyword gap analysis between organic and paid (use seo-sea-keyword-gap-analyzer), channel selection decisions (use channel-selection-framework), or creative fatigue on own ads (use platform-specific fatigue skills)."
---
# Competitor Analysis Toolkit for Advertising

## Purpose

Enable agencies and advertisers to systematically gather, analyze, and act on competitive intelligence. Move from reactive "what are competitors doing?" to proactive competitive strategy.

## When to Use This Skill

Invoke when user mentions:
- **Competitor research:** "Who are our competitors?"
- **Ad spend estimation:** "How much is competitor X spending?"
- **Creative analysis:** "What ads are they running?"
- **Positioning:** "How do we position against competitors?"
- **Auction insights:** "Interpret auction insights data"
- **Share of voice:** "What's our SOV vs competitors?"
- **Meta Ad Library:** "Research competitor ads on Facebook"
- **Competitive strategy:** "How do we beat competitor X?"

---

## Part 1: Competitor Discovery Framework

### Competitor Types

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         COMPETITOR LANDSCAPE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   DIRECT COMPETITORS                      INDIRECT COMPETITORS              │
│   ─────────────────────                   ───────────────────               │
│   Same product/service                    Different product                 │
│   Same target market                      Same customer need                │
│   Same price tier                         Alternative solution              │
│                                                                             │
│   Example: Shopify vs WooCommerce         Example: Shopify vs Etsy         │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ASPIRATIONAL COMPETITORS                EMERGING COMPETITORS              │
│   ─────────────────────────               ───────────────────               │
│   Larger players in space                 Startups, new entrants            │
│   Set industry standards                  Potential disruptors              │
│   Often in adjacent markets               Watch for innovation              │
│                                                                             │
│   Example: Amazon for any e-commerce      Example: New DTC brands           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Discovery Methods

| Method | Best For | Tools/Sources |
|--------|----------|---------------|
| **Search Analysis** | Finding SEO competitors | Google search, SEMrush, Ahrefs |
| **Ad Library Research** | Active advertisers | Meta Ad Library, TikTok Creative Center |
| **Auction Insights** | Google Ads competitors | Google Ads interface |
| **Industry Research** | Market players | Crunchbase, G2, Capterra |
| **Customer Research** | Alternatives considered | Surveys, sales team |
| **Social Listening** | Brand mentions | Brand24, Mention |

### Competitor Research Checklist

For each competitor, gather:

**Company Information:**
- [ ] Company name and website
- [ ] Founded date
- [ ] Headquarters location
- [ ] Employee count (LinkedIn)
- [ ] Funding history (Crunchbase)
- [ ] Revenue estimates (if available)

**Product/Service:**
- [ ] Main offerings
- [ ] Pricing structure
- [ ] Target segments
- [ ] Unique features
- [ ] Recent product launches

**Digital Presence:**
- [ ] Website traffic (SimilarWeb)
- [ ] Social following by platform
- [ ] Content strategy
- [ ] SEO visibility
- [ ] Review ratings

---

## Part 2: Ad Spend Estimation

### Method 1: Meta Ad Library Analysis

**Step-by-step process:**

1. Go to [Meta Ad Library](https://www.facebook.com/ads/library/)
2. Search for competitor name
3. Select country/region
4. Filter by platform (Facebook, Instagram)
5. Document:
   - Total active ads count
   - Date range of active ads
   - Ad types (video, image, carousel)
   - Landing page destinations

**Spend Estimation Formula:**

```
Estimated Monthly Spend = Active Ads × Average Daily Spend per Ad × 30 days

Where Average Daily Spend per Ad:
- Image ads: €20-80/day
- Video ads: €50-150/day
- Carousel ads: €30-100/day
- Mixed portfolio: €50-100/day average
```

**Spend Estimation Table:**

| Active Ads | Estimated Monthly Spend | Confidence |
|------------|------------------------|------------|
| 1-5 | €3,000 - €15,000 | Low |
| 6-15 | €10,000 - €45,000 | Medium |
| 16-30 | €25,000 - €90,000 | Medium |
| 31-50 | €50,000 - €150,000 | Medium |
| 51-100 | €100,000 - €300,000 | Medium-High |
| 100+ | €200,000+ | Medium-High |

**Refinements:**
- More video ads = higher spend (video CPM 2-3x image)
- International targeting = multiply by country count
- Long-running ads = likely higher daily budgets (proven performers)
- Fresh ads (< 7 days) = testing phase, lower spend

### Method 2: Google Ads Auction Insights

**Interpretation Guide:**

| Metric | What It Tells You | Spend Implication |
|--------|------------------|-------------------|
| **Impression Share** | How often they appear | High IS = high budget or high Quality Score |
| **Overlap Rate** | How often you compete | High overlap = same keywords/audiences |
| **Position Above Rate** | Who wins when both show | Higher = likely higher bids/budget |
| **Top of Page Rate** | Premium placement frequency | High = willing to pay premium |
| **Outranking Share** | Overall competitive position | Composite measure |

**Spend Estimation from Auction Insights:**

```
If competitor impression share is X% and yours is Y%:

Estimated Competitor Spend = Your Spend × (X / Y)

Example:
- Your impression share: 30%
- Your spend: €10,000/month
- Competitor impression share: 45%
- Estimated competitor spend: €10,000 × (45/30) = €15,000/month
```

**Caveats:**
- Quality Score differences affect this ratio
- Different keyword portfolios
- Geographic targeting differences

### Method 3: Industry Benchmarks

**Ad Spend as % of Revenue by Industry:**

| Industry | Startup/Growth | Established | Aggressive Growth |
|----------|---------------|-------------|-------------------|
| E-commerce | 8-15% | 4-8% | 15-25% |
| SaaS | 20-40% | 10-20% | 40-60% |
| Financial Services | 5-10% | 3-6% | 10-15% |
| Healthcare | 3-6% | 2-4% | 6-10% |
| Travel | 8-12% | 5-8% | 12-18% |
| Retail | 3-6% | 2-4% | 6-10% |
| Professional Services | 5-10% | 3-6% | 10-15% |

**Estimation:**
```
Estimated Ad Spend = Estimated Revenue × Industry Ad Ratio

Example:
- Competitor revenue: €10M (from Crunchbase/estimates)
- Industry: SaaS (established)
- Ad ratio: 15%
- Estimated spend: €1.5M/year = €125K/month
```

### Method 4: Traffic-Based Estimation

**Using SimilarWeb or Similar Tools:**

```
Estimated Paid Traffic = Total Traffic × Paid Traffic %
Estimated Spend = Paid Traffic × Average CPC × (1 / CTR)

Example:
- Monthly traffic: 500,000 visits
- Paid traffic %: 30% = 150,000 visits
- Average industry CPC: €1.50
- Estimated spend: 150,000 × €1.50 = €225,000/month
```

---

## Part 3: Creative Analysis Framework

### Ad Creative Audit Template

For each competitor's ads, document:

| Element | Options to Note |
|---------|-----------------|
| **Format** | Image / Video / Carousel / Collection / Stories |
| **Visual Style** | Product shot / Lifestyle / UGC / Animation / Testimonial |
| **Length** (video) | <15s / 15-30s / 30-60s / 60s+ |
| **Hook Type** | Question / Statistic / Problem / Benefit / Shock |
| **Copy Length** | Short (1-2 lines) / Medium (3-5 lines) / Long (6+ lines) |
| **CTA Type** | Shop Now / Learn More / Sign Up / Get Offer / Book Now |
| **Offer Type** | Discount / Free shipping / Free trial / Demo / Content |
| **Social Proof** | Reviews / Numbers / Logos / Testimonials / Awards |
| **Urgency** | Limited time / Stock scarcity / None |

### Creative Pattern Analysis

**Video Ad Hook Categories:**

| Hook Type | Example | Best For |
|-----------|---------|----------|
| **Question** | "Struggling with X?" | Problem-aware audiences |
| **Statistic** | "87% of marketers say..." | Data-driven audiences |
| **Problem** | "Tired of wasting money on..." | Pain point focus |
| **Result** | "How I got 10x ROAS" | Results-focused |
| **Controversy** | "Everyone's wrong about..." | Attention grabbing |
| **Demo** | Shows product in action | Product-focused |
| **Testimonial** | Customer story | Trust building |
| **UGC** | Authentic user content | Relatability |

**Scoring Competitor Creatives:**

| Dimension | 1 (Weak) | 3 (Average) | 5 (Strong) |
|-----------|----------|-------------|------------|
| **Attention** | Generic visuals | Somewhat engaging | Thumb-stopping |
| **Clarity** | Confusing message | Clear but forgettable | Crystal clear + memorable |
| **Relevance** | Generic messaging | Some targeting | Highly specific |
| **Desire** | No emotional pull | Some benefits | Strong value prop |
| **Action** | Weak/no CTA | Standard CTA | Compelling CTA + urgency |

### Creative Gap Analysis

**Identify opportunities by mapping:**

| Creative Approach | Competitor A | Competitor B | Competitor C | Opportunity? |
|-------------------|--------------|--------------|--------------|--------------|
| Video testimonials | ✅ Heavy use | ❌ None | ✅ Some | Low |
| UGC style | ❌ None | ✅ Heavy use | ❌ None | Medium |
| Product demos | ✅ Some | ✅ Some | ✅ Heavy | Low |
| Educational content | ❌ None | ❌ None | ❌ None | **HIGH** |
| Humor/entertainment | ❌ None | ✅ Some | ❌ None | Medium |

---

## Part 4: Positioning Analysis

### Positioning Map Framework

**Step 1: Identify Relevant Axes**

Common positioning dimensions:

| Dimension | Low End | High End |
|-----------|---------|----------|
| **Price** | Budget/affordable | Premium/luxury |
| **Quality** | Basic/good enough | Best-in-class |
| **Complexity** | Simple/easy | Full-featured/complex |
| **Target** | SMB/consumer | Enterprise/professional |
| **Approach** | Traditional | Innovative/disruptive |
| **Focus** | Generalist | Specialist/niche |
| **Service** | Self-serve | High-touch/consultative |
| **Speed** | Thorough/careful | Fast/agile |

**Step 2: Map Competitors**

```
                              PREMIUM
                                 │
                  ┌──────────────┼──────────────┐
                  │              │              │
           [Comp C]           [Comp A]         │
                  │              │              │
    SIMPLE ───────┼──────────[YOU]─────────────┼─────── COMPLEX
                  │              │              │
                  │          [Comp B]      [Comp D]
                  │              │              │
                  └──────────────┼──────────────┘
                                 │
                              BUDGET
```

**Step 3: Identify Opportunities**

- **White space**: Quadrants with no competitors
- **Crowded space**: Areas to differentiate or avoid
- **Movement opportunities**: Where positioning could shift

### Competitive Messaging Matrix

| Competitor | Primary Message | Secondary Message | Proof Points | Emotional Appeal |
|------------|-----------------|-------------------|--------------|------------------|
| [Name] | "[Main claim]" | "[Supporting claim]" | [Evidence used] | [Emotion targeted] |

**Message Differentiation Analysis:**

| Message Theme | Comp A | Comp B | Comp C | Opportunity |
|---------------|--------|--------|--------|-------------|
| Price/Value | ✅ | ❌ | ✅ | Crowded |
| Innovation | ✅ | ✅ | ❌ | Moderate |
| Ease of Use | ❌ | ❌ | ✅ | **Open** |
| Trust/Security | ❌ | ✅ | ❌ | **Open** |
| Speed/Efficiency | ❌ | ❌ | ❌ | **Strong** |

---

## Part 5: Competitive Threat Scoring

### Threat Assessment Matrix

Score each competitor 1-10 on:

| Factor | Weight | Description |
|--------|--------|-------------|
| **Market Share** | 25% | Current share of target market |
| **Growth Rate** | 20% | How fast they're growing |
| **Ad Aggressiveness** | 20% | Volume and frequency of advertising |
| **Product Strength** | 15% | Feature parity/superiority |
| **Brand Recognition** | 10% | Market awareness |
| **Resources** | 10% | Funding, team size |

**Calculation:**

```
Threat Score = (Market Share × 0.25) + (Growth Rate × 0.20) +
               (Ad Aggressiveness × 0.20) + (Product Strength × 0.15) +
               (Brand Recognition × 0.10) + (Resources × 0.10)
```

**Threat Levels:**

| Score | Level | Recommended Response |
|-------|-------|---------------------|
| 8-10 | **Critical** | Dedicated competitive strategy, monitor weekly |
| 6-7.9 | **High** | Active monitoring, defensive positioning |
| 4-5.9 | **Moderate** | Regular monitoring, maintain awareness |
| 2-3.9 | **Low** | Periodic check-ins |
| 0-1.9 | **Minimal** | Annual review sufficient |

### Competitive Response Framework

**When competitor launches new campaign:**

| Signal | Urgency | Response Options |
|--------|---------|------------------|
| New product launch | High | Accelerate own roadmap, counter-positioning |
| Price reduction | Medium-High | Evaluate match/differentiate on value |
| New creative approach | Medium | Test similar approach, or counter-position |
| New channel entry | Medium | Assess channel opportunity |
| Increased spend | High | Increase SOV or differentiate |

---

## Part 6: Share of Voice Analysis

### SOV Calculation

**For Paid Media:**

```
Your SOV = Your Impressions / Total Market Impressions × 100

Estimated from auction insights:
Your SOV ≈ Your Impression Share × Market Spend Estimate
```

**For Specific Keywords (Search):**

```
Keyword SOV = Your Impression Share for Keyword
Top competitor = Highest impression share
Your relative position = Your IS / Top competitor IS
```

### SOV Benchmarks

**Ehrenberg-Bass Rule:**

```
Market Share Growth = f(Excess Share of Voice)

ESOV = SOV - SOM (Share of Market)

For each 10 points of ESOV, expect ~0.5% market share growth/year
```

**SOV Strategy by Objective:**

| Objective | Target SOV vs SOM |
|-----------|-------------------|
| Maintain position | SOV = SOM |
| Gradual growth | SOV = SOM + 5-10pp |
| Aggressive growth | SOV = SOM + 15-25pp |
| Market entry | SOV = 2-3x target SOM |

---

## Part 7: Output Templates

### Competitive Intelligence Summary

```
## Competitive Intelligence Report: [Client Name]

### Market Overview
- Total competitors identified: X
- Primary competitors: [List top 3-5]
- Total estimated market ad spend: €X/month

### Top Competitor Profiles

**1. [Competitor Name]**
- Estimated monthly ad spend: €XX,XXX
- Primary channels: [Meta/Google/LinkedIn/TikTok]
- Key messaging: "[Main message]"
- Threat level: [Critical/High/Medium/Low]

[Repeat for top competitors]

### Your Competitive Position
- Estimated market share: X%
- Share of voice: X%
- Key competitive advantages: [List]
- Vulnerabilities: [List]

### Recommended Actions

**Defensive:**
1. [Action to protect against threat]
2. [Action to protect against threat]

**Offensive:**
1. [Opportunity to exploit]
2. [Opportunity to exploit]

### Monitoring Cadence
- Daily: [What to track]
- Weekly: [What to review]
- Monthly: [What to analyze]
```

### Ad Spend Comparison Table

```
| Competitor | Est. Monthly Spend | Confidence | Primary Channels | Trend |
|------------|-------------------|------------|------------------|-------|
| [Name] | €XX,XXX | High/Med/Low | Meta, Google | ↑↓→ |
| [Name] | €XX,XXX | High/Med/Low | Google, LinkedIn | ↑↓→ |
| **You** | €XX,XXX | - | [Channels] | - |
```

### Creative Analysis Summary

```
| Competitor | Active Ads | Primary Format | Key Theme | Differentiator |
|------------|-----------|----------------|-----------|----------------|
| [Name] | XX | Video | [Theme] | [What makes them unique] |
| [Name] | XX | Image | [Theme] | [What makes them unique] |
```

---

## Quick Reference: Research Sources

| Source | Best For | URL |
|--------|----------|-----|
| Meta Ad Library | Facebook/Instagram ads | facebook.com/ads/library |
| TikTok Creative Center | TikTok ad inspiration | ads.tiktok.com/business/creativecenter |
| Google Ads Transparency | Google Display ads | adstransparency.google.com |
| LinkedIn Ad Library | LinkedIn ads | linkedin.com/ad-library |
| SimilarWeb | Traffic estimates | similarweb.com |
| Crunchbase | Company funding/info | crunchbase.com |
| G2/Capterra | Software reviews | g2.com, capterra.com |
| BuiltWith | Tech stack | builtwith.com |

---

## Optional: Enrich with Live Data

If the user has connected accounts, complement manual competitor research with live platform data:

```python
# Pull auction insights to see which competitors you're bidding against in Google Ads
google_ads_run_gaql(
    customer_id="YOUR_CUSTOMER_ID",
    query="SELECT auction_insight.domain, metrics.search_impression_share, metrics.search_outranking_share FROM auction_insight_view WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.search_impression_share DESC LIMIT 20"
)
```

```python
# Check your own organic keyword positions for gap analysis vs competitors
gsc_search_analytics(site_url="https://yourdomain.com", dimensions=["query"], days=30, row_limit=50)
```

Auction insights show which competitors are actively bidding on your keywords. GSC positions show where you rank organically — compare these to identify where competitors outrank you and where you have room to take share.

*Last updated: February 2026*
*Framework based on industry best practices and Ad Superpowers methodology*
