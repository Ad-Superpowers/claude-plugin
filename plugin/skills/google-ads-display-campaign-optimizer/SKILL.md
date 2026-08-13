---
name: google-ads-display-campaign-optimizer
description: "This skill should be used when the user asks to \"optimize Display campaigns\", \"set up Responsive Display Ads\", \"configure display placement targeting\", \"improve viewability\", or mentions \"GDN\", \"banner formats\", \"brand safety\", or \"Display Network\". Do NOT use for: search campaign optimization (use search-campaign-optimizer), Performance Max setup (use pmax-strategy-builder), or bid strategy selection (use bid-strategy-selector)."
---
# Display Campaign Optimizer

Complete guide for Google Display Network (GDN) campaigns - from Responsive Display Ads to placement targeting and viewability optimization.



See [decision-trees.md](references/decision-trees.md) for details.



## Display Network Overview

### What is the Google Display Network?

```
GOOGLE DISPLAY NETWORK (GDN)
════════════════════════════

REACH:
──────
├── 35+ million websites and apps
├── 90%+ of internet users worldwide
├── YouTube, Gmail, Google Finance, etc.
└── Mobile apps via AdMob

INVENTORY TYPES:
────────────────
┌──────────────────────────────────────────────────────────────┐
│ GOOGLE OWNED PROPERTIES                                       │
│ ├── YouTube (non-video placements)                            │
│ ├── Gmail (Promotions tab)                                    │
│ ├── Google Finance                                            │
│ └── Blogger                                                   │
├──────────────────────────────────────────────────────────────┤
│ PARTNER WEBSITES                                              │
│ ├── News sites (CNN.com, BBC.com, etc.)                       │
│ ├── Blogs and content sites                                   │
│ ├── Forums and communities                                    │
│ └── Niche websites                                            │
├──────────────────────────────────────────────────────────────┤
│ MOBILE APPS                                                   │
│ ├── Gaming apps                                               │
│ ├── Utility apps                                              │
│ └── Social/Entertainment apps                                 │
└──────────────────────────────────────────────────────────────┘

DISPLAY VS SEARCH:
──────────────────
┌─────────────┬─────────────────────┬─────────────────────┐
│ Aspect      │ Search              │ Display             │
├─────────────┼─────────────────────┼─────────────────────┤
│ User Intent │ Actively searching  │ Passively browsing  │
│ Format      │ Text-based          │ Visual (image/video)│
│ Targeting   │ Keywords            │ Audiences/Context   │
│ Funnel      │ Bottom (high intent)│ Top/Mid (awareness) │
│ CTR         │ 2-10%               │ 0.1-1%              │
│ CPC         │ Higher              │ Lower               │
│ Volume      │ Limited by searches │ Much higher         │
└─────────────┴─────────────────────┴─────────────────────┘
```

## Responsive Display Ads (RDA)

### RDA Asset Requirements

```
RESPONSIVE DISPLAY AD SPECIFICATIONS
════════════════════════════════════

IMAGES (Required):
───────────────────
┌───────────────┬────────────┬───────────────┬─────────────────┐
│ Type          │ Ratio      │ Minimum Size  │ Recommended     │
├───────────────┼────────────┼───────────────┼─────────────────┤
│ Landscape     │ 1.91:1     │ 600x314       │ 1200x628        │
│ Square        │ 1:1        │ 300x300       │ 1200x1200       │
└───────────────┴────────────┴───────────────┴─────────────────┘

QUANTITIES:
├── Landscape: 1-5 images (upload 5 for best performance)
├── Square: 1-5 images (upload 5 for best performance)
├── Maximum file size: 5MB
└── Formats: JPG, PNG, GIF (static)

LOGO (Required):
─────────────────
├── Square logo: 1:1 ratio (min 128x128, recommended 1200x1200)
├── Landscape logo: 4:1 ratio (min 512x128, recommended 1200x300)
├── Transparent background recommended
└── Maximum file size: 5MB

HEADLINES:
──────────
├── Short Headlines: 1-5 (max 30 characters each)
├── Long Headline: 1 (max 90 characters)
└── Mix of USPs, CTAs, and benefits

DESCRIPTIONS:
─────────────
├── Quantity: 1-5 descriptions
├── Length: Max 90 characters each
└── Vary with features, benefits, social proof

BUSINESS NAME:
──────────────
├── Max 25 characters
├── Official brand name
└── No promotions

OPTIONAL:
─────────
├── Video: Up to 5 videos (YouTube links)
├── Call to Action: Select from preset options
└── Custom colors: Match brand colors
```

### RDA Example Combinations

```
HOW RDAs ARE ASSEMBLED
══════════════════════

Google automatically combines your assets into different formats:

NATIVE AD (In-feed):
┌─────────────────────────────────────────────────────────┐
│  ┌─────────┐  Short Headline                           │
│  │  LOGO   │  Description text here...                 │
│  └─────────┘                        [Shop Now]         │
└─────────────────────────────────────────────────────────┘

BANNER AD (Leaderboard 728x90):
┌─────────────────────────────────────────────────────────┐
│  ┌─────────────┐  Headline Text    ┌──────────────┐    │
│  │   IMAGE     │  Description...   │  [CTA BUTTON]│    │
│  └─────────────┘                   └──────────────┘    │
└─────────────────────────────────────────────────────────┘

LARGE RECTANGLE (336x280):
┌──────────────────────────────┐
│  ┌────────────────────────┐  │
│  │                        │  │
│  │        IMAGE           │  │
│  │                        │  │
│  └────────────────────────┘  │
│  Long Headline Here          │
│  Description text...         │
│  ┌────────────────┐          │
│  │   SHOP NOW     │   LOGO   │
│  └────────────────┘          │
└──────────────────────────────┘

INTERSTITIAL (Mobile):
┌────────────────────┐
│         x          │
│  ┌──────────────┐  │
│  │              │  │
│  │    IMAGE     │  │
│  │              │  │
│  └──────────────┘  │
│  Headline          │
│  Description       │
│  ┌──────────────┐  │
│  │  [ACTION]    │  │
│  └──────────────┘  │
└────────────────────┘
```

## Uploaded Image Ads

### Banner Formats

```
GOOGLE DISPLAY BANNER SIZES
═══════════════════════════

TOP PERFORMING SIZES (focus on these):
────────────────────────────────────
┌─────────────────────┬────────────────┬────────────────────┐
│ Size                │ Name           │ Typical Placement  │
├─────────────────────┼────────────────┼────────────────────┤
│ 300x250             │ Medium Rect    │ In-content, sidebar│
│ 336x280             │ Large Rect     │ In-content         │
│ 728x90              │ Leaderboard    │ Header, footer     │
│ 300x600             │ Half Page      │ Sidebar            │
│ 320x50              │ Mobile Banner  │ Mobile header      │
│ 320x100             │ Large Mobile   │ Mobile             │
└─────────────────────┴────────────────┴────────────────────┘

FULL LIST (for maximum reach):
──────────────────────────────
Desktop:
├── 300x250 (Medium Rectangle) *
├── 336x280 (Large Rectangle) *
├── 728x90 (Leaderboard) *
├── 300x600 (Half Page) *
├── 160x600 (Wide Skyscraper)
├── 970x90 (Large Leaderboard)
├── 970x250 (Billboard)
├── 468x60 (Banner)
└── 250x250 (Square)

Mobile:
├── 320x50 (Mobile Leaderboard) *
├── 320x100 (Large Mobile Banner) *
├── 300x250 (Medium Rectangle)
└── 336x280 (Large Rectangle)

RECOMMENDATION:
────────────────
Minimum upload: 300x250, 728x90, 320x50, 300x600
Optimal: All sizes marked with *
Maximum reach: All sizes
```

### Banner Design Best Practices

```
DISPLAY BANNER DESIGN GUIDELINES
════════════════════════════════

VISUAL HIERARCHY:
─────────────────
1. Attention grabber (image/product)
2. Headline (large, readable)
3. USP/Offer (core message)
4. CTA button (contrasting color)
5. Logo (recognition)

┌─────────────────────────────────────┐
│  1. ATTENTION                       │
│  ┌─────────────────────────────┐    │
│  │     PRODUCT / IMAGE         │    │
│  └─────────────────────────────┘    │
│                                     │
│  2. HEADLINE (short & powerful)     │
│                                     │
│  3. USP: Free Shipping!            │
│                                     │
│  4. ┌────────────────┐   5. [LOGO]  │
│     │  SHOP NOW  >   │              │
│     └────────────────┘              │
└─────────────────────────────────────┘

DO's:
─────
+ Clear call-to-action
+ Contrasting colors
+ Readable text (min 10pt at small size)
+ Animation max 30 seconds (GIF)
+ Brand consistent
+ Mobile-first design

DON'Ts:
───────
- Too much text
- Flashing or distracting animations
- Misleading elements (fake buttons)
- Low quality images
- Too small text
- No CTA button

FILE SPECS:
───────────
├── Formats: GIF, JPG, PNG, HTML5
├── Max file size: 150KB
├── HTML5: Max 1MB with assets
├── Animation: Max 30 sec, then freeze
└── Audio: Not allowed
```

## Targeting Strategies

### Audience Targeting

```
DISPLAY AUDIENCE TARGETING
══════════════════════════

LAYER 1: YOUR DATA (First-Party)
────────────────────────────────
Highest value, lowest volume

□ Website Remarketing
├── All Visitors: 30, 60, 90, 180 days
├── Category Viewers: Visitors to specific pages
├── Product Viewers: Dynamic remarketing
├── Cart Abandoners: Highest intent
└── Converters: Cross-sell / upsell

□ Customer Match
├── Upload email lists
├── Phone numbers
├── Lifetime value segments
└── Exclude existing customers (prospecting)

□ YouTube Viewers
├── Video viewers
├── Channel subscribers
└── Video engagers (likes, comments)

LAYER 2: OPTIMIZED TARGETING
─────────────────────────────
Expands beyond selected audiences using Google AI

□ Based on Converters list
├── Add converter list as targeting signal
├── Optimized Targeting finds similar users automatically
└── High conversion potential

□ Based on Cart Abandoners
├── High purchase intent signals
├── Google expands to users with similar patterns
└── Monitor via "Targeting expansion" report

LAYER 3: IN-MARKET AUDIENCES
────────────────────────────
Active purchase intent

□ In-Market Categories
├── Select relevant categories
├── Google's intent signals
├── Active in last 7-14 days
└── Example: "Laptops", "Running Shoes"

LAYER 4: AFFINITY AUDIENCES
───────────────────────────
Lifestyle and interests

□ Affinity Categories
├── Broader targeting
├── Long-term interests
├── Good for awareness
└── Example: "Tech Enthusiasts", "Fashionistas"

LAYER 5: CUSTOM AUDIENCES
─────────────────────────
Self-defined

□ Custom Intent
├── Keyword-based: People searching for [X]
├── URL-based: Visitors to competitor sites
└── App-based: Users of specific apps

□ Custom Affinity
├── Broader interest targeting
├── Combine keywords + URLs + apps
└── Provide audience description
```

### Content Targeting

```
DISPLAY CONTENT TARGETING
═════════════════════════

TOPICS TARGETING:
─────────────────
□ Advertise on sites about specific topics
├── Broad categories: /Autos & Vehicles
├── Subcategories: /Autos/Classic Vehicles
├── Good for: Contextual relevance
└── Risk: Limited reach, less precise

PLACEMENT TARGETING:
────────────────────
□ Specific websites or apps
├── URL-level: www.example.com
├── Section-level: www.example.com/tech
├── App targeting: Specific apps
├── YouTube channels/videos
└── Good for: Premium placements, brand safety

KEYWORDS (Contextual):
──────────────────────
□ Pages containing specific keywords
├── Display keywords (not Search keywords)
├── Content matching
├── Good for: Thematic targeting
└── Combine with audience for better results

TARGETING COMBINATIONS:
──────────────────────
┌─────────────────────────────────────────────────────────┐
│ TARGETING APPROACH                  │ RESULT             │
├─────────────────────────────────────┼────────────────────┤
│ Audience ONLY                       │ Broad, any site    │
│ Placement ONLY                      │ Limited, premium   │
│ Audience + Placement                │ Sweet spot         │
│ Audience + Topics                   │ Contextual         │
│ Keywords + Audience                 │ Very specific      │
└─────────────────────────────────────┴────────────────────┘

RECOMMENDATION:
────────────────
Remarketing: Audience only (follow users everywhere)
Prospecting: Audience + Topics/Keywords
Premium: Placement targeting + Audience
```



See [detailed-reference.md](references/detailed-reference.md) for details.

## MCP Tool Integration

```
STEP 1: Display campaign performance overview
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign.status,
    campaign.bidding_strategy_type,
    metrics.impressions,
    metrics.clicks,
    metrics.ctr,
    metrics.average_cpc,
    metrics.cost_micros,
    metrics.conversions,
    metrics.cost_per_conversion,
    metrics.active_view_viewability
  FROM campaign
  WHERE campaign.advertising_channel_type = 'DISPLAY'
    AND campaign.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")

STEP 2: Placement performance (find non-converting placements)
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    detail_placement_view.display_name,
    detail_placement_view.placement,
    detail_placement_view.placement_type,
    metrics.impressions,
    metrics.clicks,
    metrics.cost_micros,
    metrics.conversions
  FROM detail_placement_view
  WHERE campaign.advertising_channel_type = 'DISPLAY'
    AND segments.date DURING LAST_30_DAYS
    AND metrics.impressions > 500
  ORDER BY metrics.cost_micros DESC
  LIMIT 100
")

STEP 3: Audience segment performance
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    ad_group.name,
    ad_group_criterion.type,
    ad_group_criterion.status,
    metrics.impressions,
    metrics.clicks,
    metrics.conversions,
    metrics.cost_micros,
    metrics.cost_per_conversion
  FROM ad_group_criterion
  WHERE campaign.advertising_channel_type = 'DISPLAY'
    AND ad_group_criterion.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
  LIMIT 100
")

STEP 4: RDA asset performance
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    ad_group.name,
    ad_group_ad.ad.name,
    ad_group_ad.status,
    metrics.impressions,
    metrics.clicks,
    metrics.conversions,
    metrics.cost_micros
  FROM ad_group_ad
  WHERE campaign.advertising_channel_type = 'DISPLAY'
    AND ad_group_ad.ad.type = 'RESPONSIVE_DISPLAY_AD'
    AND ad_group_ad.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")
```

## Bidding & Budget

### Bid Strategies

```
DISPLAY BIDDING STRATEGIES
══════════════════════════

┌────────────────────────┬─────────────────────┬─────────────────────┐
│ Strategy               │ Best for            │ Requirements        │
├────────────────────────┼─────────────────────┼─────────────────────┤
│ Manual CPC             │ Full control        │ Time to optimize    │
│ Enhanced CPC           │ Assisted bidding    │ Conversion tracking │
│ Maximize Clicks        │ Traffic focus       │ None                │
│ Maximize Conversions   │ Lead gen/sales      │ Conv tracking       │
│ Target CPA             │ Efficiency focus    │ 15+ conv/month      │
│ Target ROAS            │ E-commerce value    │ Conv value tracking │
│ Viewable CPM (vCPM)    │ Brand awareness     │ None                │
└────────────────────────┴─────────────────────┴─────────────────────┘

STRATEGY SELECTION:
───────────────────

REMARKETING CAMPAIGNS:
├── Start: Maximize Conversions
├── After 15+ conv: Target CPA (20% above average)
└── Optimize: Lower CPA target by 10-15%

PROSPECTING CAMPAIGNS:
├── Awareness: vCPM (viewable impressions)
├── Traffic: Maximize Clicks
└── Conversions: Target CPA (higher target than remarketing)

BID ADJUSTMENTS:
────────────────
Device:
├── Mobile: -20% to +20% depending on performance
├── Tablet: Often -10% to -30%
└── Desktop: Baseline

Demographics:
├── Age: Adjust per segment
├── Gender: Adjust per segment
└── Household Income: Especially relevant for B2B

Schedule:
├── Peak hours: +10-20%
└── Night: -20-50% or exclude
```

### Budget Allocation

```
DISPLAY BUDGET GUIDELINES
══════════════════════════

MINIMUM BUDGETS:
──────────────────
├── Remarketing: $20/day minimum
├── Prospecting: $30/day minimum
├── Both: $50/day total recommended
└── Scaling: Max 20% increase per week

BUDGET DISTRIBUTION:
─────────────────
Total Display Budget: 100%

Remarketing Focus:
├── Remarketing: 60-70%
├── Prospecting: 30-40%
└── Reason: Higher ROI on remarketing

Awareness Focus:
├── Remarketing: 30-40%
├── Prospecting: 60-70%
└── Reason: Volume and reach priority

DISPLAY VS OTHER CHANNELS:
──────────────────────────
Total Digital Budget: 100%
├── Search: 50-60%
├── Display: 15-25%
├── Social: 15-25%
└── Video: 5-15%

REMARKETING BUDGET LOGIC:
─────────────────────────
Website Traffic/month x Conv Rate x Target CPA = Max Budget

Example:
100,000 visitors x 2% remarketing eligible x $50 tCPA
= 2,000 x $50 = $100,000 potential / month
Realistic spend: $20,000-30,000/month
```

## Brand Safety & Viewability

### Content Exclusions

```
BRAND SAFETY SETUP
══════════════════

CONTENT EXCLUSIONS (Campaign Level):
────────────────────────────────────
Settings → Additional Settings → Content Exclusions

□ Digital Content Labels:
├── DL-G: General audiences (safest)
├── DL-PG: Most audiences
├── DL-T: Teen and older
├── DL-MA: Mature audiences
└── Not yet labeled

□ Sensitive Content Categories:
├── Tragedy and conflict
├── Sensitive social issues
├── Sexually suggestive content
├── Profanity and rough language
└── Shocking content

RECOMMENDED EXCLUSIONS:
──────────────────────
Conservative brands:
├── Exclude: DL-T, DL-MA, Not labeled
├── Exclude: All sensitive categories
└── Placement review: Weekly

Moderate brands:
├── Exclude: DL-MA, Not labeled
├── Exclude: Tragedy, Sexually suggestive, Shocking
└── Placement review: Monthly

PLACEMENT TYPE EXCLUSIONS:
──────────────────────────
□ Inventory types:
├── Standard inventory (default)
├── Expanded inventory (more volume, less control)
└── Limited inventory (premium only, less volume)

□ Content types:
├── Embedded videos
├── Live streaming videos
├── Games
└── In-apps (selective)
```

### Viewability Optimization

```
VIEWABILITY METRICS
═══════════════════

WHAT IS VIEWABILITY?
───────────────────
An ad is "viewable" if:
├── Display: 50%+ pixels visible for 1+ second
└── Video: 50%+ pixels visible for 2+ seconds

INDUSTRY BENCHMARKS:
────────────────────
├── Average viewability: 50-60%
├── Good viewability: 60-70%
├── Excellent viewability: 70%+
└── Premium inventory: 80%+

IMPROVING VIEWABILITY:
───────────────────────

1. BID STRATEGY
   └── Use vCPM (viewable CPM) for awareness

2. PLACEMENT SELECTION
   ├── Above the fold placements
   ├── Premium publishers
   └── Exclude low viewability sites

3. AD SIZE SELECTION
   ├── 300x250: High viewability (in-content)
   ├── 728x90: Medium (header, can be below fold)
   ├── 300x600: High viewability (sticky sidebar)
   └── 320x50: Variable (mobile header)

4. EXCLUSIONS
   ├── Exclude sites with <40% viewability
   ├── Exclude embedded placements
   └── Exclude below-the-fold only inventory

SETTING UP VIEWABILITY REPORTS:
────────────────────────────
Reports → Predefined → Display
├── Add: Active View viewable impressions
├── Add: Active View measurable impressions
├── Add: Active View viewable rate
└── Segment by: Placement
```

## Display Campaign Optimization

### Optimization Checklist

```
DISPLAY OPTIMIZATION WORKFLOW
═════════════════════════════

DAILY:
──────
□ Budget pacing check
□ Large deviations in spend/impressions
□ Disapproved ads check

WEEKLY:
──────
□ Placement performance review
├── Identify high-spend, low-conv placements
├── Add exclusions
└── Find new performing placements

□ Audience performance
├── CTR and Conv Rate per audience
├── Adjust bids per audience
└── Exclude underperformers

□ Asset performance (RDA)
├── Check asset ratings
├── Replace "Low" assets
└── Add new variations

MONTHLY:
────────
□ Creative refresh
├── New images/banners
├── New headlines
└── Seasonal updates

□ Audience expansion/contraction
├── Test new segments
├── Remove non-performers
└── Lookalike audiences

□ Bidding review
├── CPA trends
├── Bid adjustment optimization
└── Strategy changes

QUARTERLY:
──────────
□ Full account audit
□ Strategy review
□ Budget reallocation
□ Plan new tests
```

### Performance Benchmarks

```
DISPLAY BENCHMARKS
══════════════════

REMARKETING:
────────────
├── CTR: 0.3-0.8%
├── CPC: $0.30-0.80
├── Conv Rate: 1.5-4%
├── CPA: 20-40% lower than prospecting
└── ROAS: Typically highest of display

PROSPECTING:
────────────
├── CTR: 0.05-0.2%
├── CPC: $0.15-0.50
├── Conv Rate: 0.2-1%
├── CPA: Higher than remarketing
└── Focus: Volume and awareness

BY INDUSTRY:
──────────────
┌───────────────┬───────────┬───────────┬────────────┐
│ Industry      │ CTR       │ CPC       │ Conv Rate  │
├───────────────┼───────────┼───────────┼────────────┤
│ E-commerce    │ 0.15%     │ $0.35     │ 0.8%       │
│ B2B           │ 0.08%     │ $0.80     │ 0.5%       │
│ Finance       │ 0.10%     │ $0.90     │ 0.6%       │
│ Travel        │ 0.12%     │ $0.40     │ 0.4%       │
│ Retail        │ 0.20%     │ $0.30     │ 1.0%       │
└───────────────┴───────────┴───────────┴────────────┘
```

## Output: Display Campaign Template

```markdown
# Display Campaign Plan

## Campaign Overview
- **Advertiser:** [Name]
- **Type:** [Remarketing / Prospecting / Both]
- **Budget:** $[X]/day
- **Duration:** [Start] - [End]

## Campaign Structure
| Campaign | Type | Audience | Budget/day | Bid Strategy |
|----------|------|----------|------------|--------------|
| [Name] | Remarketing | Website visitors | $[X] | tCPA |
| [Name] | Prospecting | In-Market + Custom | $[X] | Max Conv |

## Audience Strategy
### Remarketing
- [ ] All visitors (30d, 60d, 90d)
- [ ] Product viewers
- [ ] Cart abandoners
- [ ] Past purchasers (exclude/cross-sell)

### Prospecting
- [ ] In-Market: [Categories]
- [ ] Custom Audiences: [Keywords/URLs]
- [ ] Optimized Targeting: [Enabled/Disabled, seed audiences]

## Creative Assets
### Responsive Display Ads
| Asset Type | Quantity | Status |
|------------|----------|--------|
| Landscape Images (1.91:1) | x5 | |
| Square Images (1:1) | x5 | |
| Square Logo | x1 | |
| Headlines (30 char) | x5 | |
| Long Headline (90 char) | x1 | |
| Descriptions (90 char) | x5 | |

### Uploaded Banners (Optional)
| Size | Format | Status |
|------|--------|--------|
| 300x250 | JPG/PNG | |
| 728x90 | JPG/PNG | |
| 320x50 | JPG/PNG | |
| 300x600 | JPG/PNG | |

## Brand Safety
- [ ] Content exclusions configured
- [ ] Sensitive categories excluded
- [ ] Placement exclusion list uploaded
- [ ] Mobile app categories reviewed

## Success Metrics
| Metric | Remarketing Target | Prospecting Target |
|--------|-------------------|-------------------|
| CTR | >0.4% | >0.1% |
| CPC | <$0.50 | <$0.40 |
| Conv Rate | >2% | >0.5% |
| CPA | $[X] | $[X] |

## Optimization Schedule
- Week 1: Launch, monitor delivery
- Week 2: Placement review, first exclusions
- Week 3-4: Audience optimization
- Monthly: Creative refresh, full review
```
</output>
