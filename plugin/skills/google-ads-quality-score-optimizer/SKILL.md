---
name: google-ads-quality-score-optimizer
description: "This skill should be used when the user asks to \"improve Quality Score\", \"reduce CPC through QS\", \"diagnose low Quality Score\", \"optimize ad relevance\", or mentions \"landing page experience\", \"expected CTR\", or \"Quality Score components\". Do NOT use for: full account audits (use account-auditor), landing-page-only issues without QS context."
---
# Quality Score Optimizer

Complete guide for understanding and improving Google Ads Quality Score to achieve lower CPCs and better ad positions.

## Pull Quality Score Data via MCP First

```
# Identify keywords with low Quality Score
google_ads_run_gaql(query="
  SELECT ad_group_criterion.keyword.text,
         ad_group_criterion.keyword.match_type,
         ad_group_criterion.quality_info.quality_score,
         ad_group_criterion.quality_info.search_predicted_ctr,
         ad_group_criterion.quality_info.ad_relevance,
         ad_group_criterion.quality_info.landing_page_experience,
         metrics.impressions, metrics.clicks, metrics.ctr,
         metrics.cost_micros, campaign.name, ad_group.name
  FROM keyword_view
  WHERE segments.date DURING LAST_30_DAYS
    AND campaign.status = 'ENABLED'
    AND ad_group_criterion.status = 'ENABLED'
    AND ad_group_criterion.quality_info.quality_score < 7
  ORDER BY metrics.cost_micros DESC
  LIMIT 50
")
```

This surfaces your most expensive low-QS keywords — the highest ROI targets for optimization.

## What Is Quality Score?

```
QUALITY SCORE FUNDAMENTALS
══════════════════════════

Quality Score = Google's assessment of your ad quality
Score: 1-10 (10 = best)

┌─────────────────────────────────────────────────────────────────┐
│  QUALITY SCORE COMPONENTS (2025)                                 │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  EXPECTED CTR                               ~39% weight   │ │
│  │  ├── Historical CTR of your ads                           │ │
│  │  ├── Predicted CTR for this keyword                       │ │
│  │  └── Compared with competitors                            │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  AD RELEVANCE                               ~22% weight   │ │
│  │  ├── Match between keyword and ad copy                    │ │
│  │  ├── Semantic relevance                                   │ │
│  │  └── Intent alignment                                     │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  LANDING PAGE EXPERIENCE                    ~39% weight   │ │
│  │  ├── Landing page relevance                               │ │
│  │  ├── User experience (mobile, speed)                      │ │
│  │  ├── Trust signals                                        │ │
│  │  └── Easy navigation                                      │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘

IMPORTANT NUANCE:
Quality Score in the UI is a HISTORICAL metric.
Google uses REAL-TIME quality signals in every auction.
```

## Quality Score Impact

### QS and CPC Relationship

```
QUALITY SCORE IMPACT ON CPC
════════════════════════════

FORMULA:
Ad Rank = Max CPC x Quality Score (simplified)
Actual CPC = (Ad Rank of advertiser below you / Your QS) + 0.01

┌────────────────┬─────────────────┬──────────────────────────────┐
│ Quality Score  │ CPC Impact      │ Comparison (base QS=5)       │
├────────────────┼─────────────────┼──────────────────────────────┤
│ QS 10          │ -50% CPC        │ Pay half for same position   │
│ QS 8           │ -25% CPC        │ Significant advantage        │
│ QS 7           │ -15% CPC        │ Small advantage              │
│ QS 5           │ Baseline        │ Average                      │
│ QS 3           │ +35% CPC        │ Disadvantage, inefficient    │
│ QS 1           │ +400% CPC       │ Not competitive              │
└────────────────┴─────────────────┴──────────────────────────────┘

PRACTICAL EXAMPLE:
────────────────────
Keyword: "buy running shoes"
Market average CPC: $1.00

├── With QS 10: You pay ~$0.50
├── With QS 7:  You pay ~$0.85
├── With QS 5:  You pay ~$1.00 (baseline)
├── With QS 3:  You pay ~$1.35
└── With QS 1:  You pay ~$5.00 (often not shown)

ANNUAL IMPACT ($50k ad spend):
──────────────────────────────
QS 5 → QS 7:  Save ~$7,500/year
QS 5 → QS 8:  Save ~$12,500/year
QS 5 → QS 10: Save ~$25,000/year
```

### QS Status Interpretation

```
COMPONENT STATUS EXPLANATION
═════════════════════════════

ABOVE AVERAGE (Green)
─────────────────────
You perform better than most advertisers
No immediate action needed
Focus on maintaining

AVERAGE (Yellow)
────────────────
You are average, room for improvement
Monitor and test improvements
Not an urgent problem

BELOW AVERAGE (Red)
────────────────────
You perform worse than most advertisers
Immediate action required
Costing you money and positions
```

## Expected CTR Optimization

### CTR Improvement Strategies

```
CTR OPTIMIZATION FRAMEWORK
═══════════════════════════

1. HEADLINE OPTIMIZATION
─────────────────────────
HIGH-CTR HEADLINE FORMULAS:

□ Include Keyword (Direct Match)
├── Keyword: "women's running shoes"
├── Headline: "Women's Running Shoes - Shop Now"
└── Impact: +20-40% CTR

□ Numbers & Specifics
├── "50+ Running Shoe Models"
├── "Starting at $49.95"
├── "4.8 Star Rating"
└── Impact: +15-30% CTR

□ Urgency/Scarcity
├── "Same-Day Delivery"
├── "This Week Only -30%"
├── "Last Items"
└── Impact: +10-25% CTR (use sparingly)

□ Power Words
├── "Free Shipping"
├── "Authorized Dealer"
├── "100% Authentic"
└── Impact: +10-20% CTR

2. DESCRIPTION OPTIMIZATION
────────────────────────────
□ First 90 characters = most visible
□ Include primary keyword
□ Clear CTA (Shop Now, Order Direct)
□ Benefit-focused, not feature-focused
□ Social proof (reviews, awards)

3. AD ASSETS IMPACT (formerly "Extensions")
────────────────────────────────────────────
Assets increase visual footprint = higher CTR
Note: Google rebranded "Extensions" to "Assets" in 2022.
The Google Ads API uses asset_group for PMax,
ad_group_ad_asset_view for Search ads.

CTR IMPACT PER ASSET TYPE:
├── Sitelinks: +10-15%
├── Callouts: +5-10%
├── Structured Snippets: +5-8%
├── Call Asset: +5-10%
├── Location Asset: +5-10%
└── Price Asset: +10-20%

USING ALL ASSETS = Up to +30% CTR boost
```

### RSA Optimization for CTR

```
RSA BEST PRACTICES FOR CTR
═══════════════════════════

HEADLINES (15 max):
───────────────────
□ Headlines 1-3: Keyword-focused
├── "Buy Running Shoes"
├── "Premium Running Shoes"
└── "Official [Brand] Store"

□ Headlines 4-6: Benefit-focused
├── "Free Shipping Over $50"
├── "Next-Day Delivery"
└── "30-Day Returns"

□ Headlines 7-9: USP/Trust
├── "15 Years of Expertise"
├── "4.8 Stars on Trustpilot"
└── "100% Authentic"

□ Headlines 10-12: CTA-focused
├── "Shop Now"
├── "Discover the Collection"
└── "Order Today"

□ Headlines 13-15: Dynamic/Variation
├── "New Arrivals"
├── "[Season] Collection"
└── Pinned headlines for control

DESCRIPTIONS (4 max):
─────────────────────
□ Description 1: Core value prop + keyword
□ Description 2: Social proof + benefits
□ Description 3: USPs + trust elements
□ Description 4: CTA + urgency

PIN STRATEGY:
─────────────
Position 1: Pin your best CTR headline
Position 2: Pin keyword-focused headline
Position 3: Let Google test
```



See [decision-trees.md](references/decision-trees.md) for details.



## Landing Page Experience

### Landing Page Optimization Checklist

```
LANDING PAGE EXPERIENCE CHECKLIST
══════════════════════════════════

1. RELEVANCE (Content Match)
─────────────────────────────
□ Keyword on landing page (H1, body text)
□ Ad promise = landing page delivery
□ Correct product/service directly visible
□ No bait-and-switch

EXAMPLE:
├── Keyword: "nike air max men"
├── Ad: "Nike Air Max Men - Shop Now"
├── LP BAD: Homepage with all shoes
└── LP GOOD: Filtered page Nike Air Max men

2. PAGE SPEED (Core Web Vitals)
────────────────────────────────
□ LCP (Largest Contentful Paint): <2.5s
□ FID (First Input Delay): <100ms
□ CLS (Cumulative Layout Shift): <0.1

QUICK FIXES:
├── Compress images (WebP format)
├── Lazy loading for below-fold images
├── Remove unused CSS/JS
├── Use CDN
└── Enable caching

3. MOBILE EXPERIENCE
─────────────────────
□ Mobile-responsive design
□ Readable text (16px+ font)
□ Tap targets >48px
□ No horizontal scrolling
□ Fast mobile load (<3s)

4. TRUST & TRANSPARENCY
────────────────────────
□ Clear privacy policy (linked)
□ Secure connection (HTTPS)
□ Business info (address, contact)
□ Reviews/testimonials visible
□ Return policy clear
□ Payment security badges

5. NAVIGATION & UX
───────────────────
□ Clear CTA above the fold
□ Easy navigation back/forward
□ No intrusive popups (especially mobile)
□ Form fields minimized
□ Guest checkout option (e-commerce)
```

### Landing Page Speed Optimization

```
PAGE SPEED IMPROVEMENT
══════════════════════

TESTING TOOLS:
──────────────
□ Google PageSpeed Insights
  https://pagespeed.web.dev/

□ Google Search Console
  Core Web Vitals report

□ GTmetrix
  https://gtmetrix.com/

□ WebPageTest
  https://webpagetest.org/

COMMON ISSUES & FIXES:
──────────────────────

ISSUE: Slow LCP (Largest Contentful Paint)
CAUSES:
├── Large hero image
├── Slow server response
└── Render-blocking resources
FIXES:
├── Preload hero image
├── Use CDN + caching
├── Defer non-critical JS
└── Inline critical CSS

ISSUE: High CLS (Layout Shift)
CAUSES:
├── Images without dimensions
├── Ads loading late
├── Dynamic content injection
FIXES:
├── Set width/height on images
├── Reserve space for ads
├── Use transform for animations
└── Skeleton loaders

ISSUE: Poor FID (First Input Delay)
CAUSES:
├── Heavy JavaScript execution
├── Third-party scripts
└── Large DOM
FIXES:
├── Code splitting
├── Defer third-party scripts
├── Reduce DOM size
└── Web workers for heavy tasks

QUICK WINS:
───────────
1. Compress images: 30-50% size reduction
2. Enable text compression (gzip/brotli)
3. Use browser caching
4. Remove unused code
5. Optimize fonts (subset, preload)
```



See [decision-trees.md](references/decision-trees.md) for details.





See [detailed-reference.md](references/detailed-reference.md) for details.



## Output: Quality Score Improvement Plan

```markdown
# Quality Score Improvement Plan

## Account Status
- **Account:** [Account Name]
- **Date:** [Date]
- **Current Avg QS:** [X.X]
- **Target Avg QS:** [X.X]

## Priority Keywords Analysis

### Critical (QS 1-3)
| Keyword | Campaign | QS | Exp CTR | Ad Rel | LP Exp | Action |
|---------|----------|----|---------| -------|--------|--------|
| [kw]    | [camp]   | 2  | Below   | Below  | Avg    | Restructure |

### High Priority (QS 4-5)
| Keyword | Campaign | QS | Issue | Action |
|---------|----------|----|-------|--------|
| [kw]    | [camp]   | 4  | LP Exp Below | Speed optimization |

## Improvement Actions

### Expected CTR Improvements
- [ ] Rewrite headlines with keywords
- [ ] Add all relevant extensions
- [ ] Test new RSA variations
- [ ] Target CTR improvement: +[X]%

### Ad Relevance Improvements
- [ ] Restructure ad groups (max 15 kw/group)
- [ ] Add keyword insertion where appropriate
- [ ] Match keyword intent with ad copy
- [ ] Create dedicated ads per theme

### Landing Page Improvements
- [ ] Page speed optimization (target: <2.5s LCP)
- [ ] Mobile experience audit
- [ ] Add trust signals
- [ ] Ensure keyword presence on page

## Timeline
- Week 1-2: Ad copy & extension updates
- Week 3-4: Ad group restructuring
- Week 5-6: Landing page optimizations
- Week 7-8: Review & iterate

## Success Metrics
- Current Avg QS: [X.X] → Target: [X.X]
- Current CPC: [X.XX] → Expected: [X.XX] (-X%)
- Keywords Below Avg: [X] → Target: [X]
```
