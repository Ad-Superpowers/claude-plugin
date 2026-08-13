---
name: google-ads-youtube-ads-strategist
description: "This skill should be used when the user asks to \"plan YouTube Ads strategy\", \"choose video ad formats\", \"set up Bumper ads\", \"target YouTube audiences\", or mentions \"TrueView\", \"ABCD framework\", \"YouTube remarketing\", or \"video campaign optimization\". Do NOT use for: standard Display campaigns (use display-campaign-optimizer), Performance Max video assets (use pmax-asset-group-optimizer)."
---
# YouTube Ads Strategist

Complete guide for YouTube advertising strategy, video ad formats, targeting, and campaign optimization within Google Ads.



See [decision-trees.md](references/decision-trees.md) for details.



## YouTube Ad Formats Overview

### Format Comparison

```
YOUTUBE AD FORMATS 2025/2026
════════════════════════════

⚠️ IMPORTANT CHANGE (2025): Video Action Campaigns (VAC) have been merged
   into Demand Gen. For conversion-focused video advertising, use Demand Gen
   campaigns with video assets + tCPA/Maximize Conversions bidding.

┌──────────────────────┬────────────┬──────────────┬─────────────┬──────────────┐
│ Format               │ Length     │ Skippable    │ Pay Model   │ Best for     │
├──────────────────────┼────────────┼──────────────┼─────────────┼──────────────┤
│ Skippable In-Stream  │ 12s - 3min │ After 5 sec  │ CPV/CPM     │ Engagement   │
│ Non-Skip In-Stream   │ 15-20 sec  │ No           │ CPM         │ Reach        │
│ Bumper Ads           │ 6 sec      │ No           │ CPM         │ Awareness    │
│ In-Feed Video        │ Any        │ N/A          │ CPV         │ Consideration│
│ Demand Gen (video)   │ 10s - 3min │ After 5 sec  │ CPA/tCPA    │ Conversions  │
│ YouTube Shorts       │ <60 sec    │ Variable     │ CPV/CPM     │ Mobile reach │
│ Masthead             │ 24 hours   │ N/A          │ CPD/CPM     │ Mass reach   │
└──────────────────────┴────────────┴──────────────┴─────────────┴──────────────┘

CPV = Cost Per View (30 sec or full video)
CPM = Cost Per 1000 Impressions
CPA = Cost Per Action (conversion)
CPD = Cost Per Day (masthead)

Note: "Video Action Campaigns" (VAC) is the legacy name. In 2025 these were
merged into Demand Gen. Use Demand Gen + video assets for conversion goals.
```

### Skippable In-Stream Ads

```
SKIPPABLE IN-STREAM (TrueView)
══════════════════════════════

┌──────────────────────────────────────────────────────────────┐
│                                                              │
│    ┌─────────────────────────────────────────────────────┐   │
│    │                                                     │   │
│    │              VIDEO CONTENT                          │   │
│    │                                                     │   │
│    │    [Skip Ad ▶]                  [Ad · 0:23]        │   │
│    │                                                     │   │
│    └─────────────────────────────────────────────────────┘   │
│                                                              │
│    Companion Banner (300x60)                                 │
│    ┌─────────────────────────────────────────┐               │
│    │ Shop Now - Free Shipping                │               │
│    └─────────────────────────────────────────┘               │
│                                                              │
└──────────────────────────────────────────────────────────────┘

SPECIFICATIONS:
├── Minimum length: 12 seconds
├── Recommended length: 15-60 seconds
├── Maximum length: No limit (3 min recommended max)
├── Skip option: After 5 seconds
├── Payment: CPV (30 sec view or full video if shorter)
└── CTA: Companion banner + video overlay possible

BEST PRACTICES:
├── Hook within 5 seconds (before skip)
├── Brand visibility in first 5 sec
├── CTA in video and companion banner
├── Add subtitles (85% watch without sound)
└── Mobile-first design (60%+ mobile views)
```

### Bumper Ads

```
BUMPER ADS (6 SECONDS)
══════════════════════

┌──────────────────────────────────────────────────────────────┐
│                                                              │
│    ┌─────────────────────────────────────────────────────┐   │
│    │                                                     │   │
│    │              6 SECOND VIDEO                         │   │
│    │                                                     │   │
│    │         NON-SKIPPABLE                  [Ad · 0:06] │   │
│    │                                                     │   │
│    └─────────────────────────────────────────────────────┘   │
│                                                              │
└──────────────────────────────────────────────────────────────┘

WHEN TO USE:
├── Brand awareness campaigns
├── Frequency building (multiple touchpoints)
├── Remarketing sequences
├── Teaser for longer content
└── Seasonal promotions

BEST PRACTICES:
├── One clear message
├── Brand in first AND last frame
├── No complex storylines
├── Audio-first design (short and punchy)
├── Sequencing: 3-5 bumpers in rotation
└── Combine with longer formats

CREATIVE STRUCTURE (6 sec):
├── Frame 1-2: Grab attention + brand
├── Frame 3-4: Core message
├── Frame 5-6: CTA + brand
└── Audio: Consistent brand sound
```

### Demand Gen Video (formerly Video Action Campaigns)

```
DEMAND GEN CONVERSION VIDEO (2025+)
════════════════════════════════════

⚠️ Video Action Campaigns (VAC) were merged into Demand Gen in 2025.
   This format now lives inside Demand Gen campaigns. The features and
   capabilities are the same; only the campaign container changed.

┌──────────────────────────────────────────────────────────────┐
│                                                              │
│    ┌─────────────────────────────────────────────────────┐   │
│    │                                                     │   │
│    │              VIDEO + CTA OVERLAY                    │   │
│    │                                                     │   │
│    │    [Skip Ad ▶]        ┌──────────────────────┐     │   │
│    │                       │  SHOP NOW            │     │   │
│    │                       │  Free Shipping >$50  │     │   │
│    │                       └──────────────────────┘     │   │
│    │                                                     │   │
│    └─────────────────────────────────────────────────────┘   │
│                                                              │
│    ┌──────────────────────────────────────────────────────┐ │
│    │ Product Feed (optional)                             │ │
│    │ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                     │ │
│    │ │ $29 │ │ $49 │ │ $35 │ │ $59 │                     │ │
│    │ └─────┘ └─────┘ └─────┘ └─────┘                     │ │
│    └──────────────────────────────────────────────────────┘ │
│                                                              │
└──────────────────────────────────────────────────────────────┘

HOW TO SET UP (2025+):
├── Create a Demand Gen campaign
├── Select conversion goal (Sales/Leads)
├── Add video assets (horizontal + vertical for Shorts)
├── Set bid strategy: tCPA or Maximize Conversions
└── Optional: Link product feed for shopping overlay

FEATURES:
├── Conversion-optimized
├── Automatic placement (YouTube in-stream + Shorts + Discover + Gmail)
├── CTA buttons and sitelinks
├── Product feed integration possible
└── Bid strategy: tCPA or Maximize Conversions

SETUP REQUIREMENTS:
├── Conversion tracking active
├── Minimum 50 conversions/month recommended
├── Video: 10-180 seconds (30-60 sec optimal)
├── Include vertical 9:16 video for YouTube Shorts placement
└── CTA overlay: headline max 10 chars, description max 15 chars
```

## Audience Targeting Strategies

### Targeting Options

```
YOUTUBE AUDIENCE TARGETING
══════════════════════════

LAYER 1: DEMOGRAPHICS
──────────────────────
□ Age: 18-24, 25-34, 35-44, 45-54, 55-64, 65+
□ Gender: Male, Female, Unknown
□ Parental Status: Parent, Not a parent
□ Household Income: Top 10%, 11-20%, 21-30%, etc.

LAYER 2: AUDIENCES
──────────────────
□ Affinity Audiences
├── Lifestyle-based (Foodies, Fashionistas, etc.)
├── Broad reach
└── Brand awareness campaigns

□ In-Market Audiences
├── Active purchase intent
├── High conversion potential
└── Specific product categories

□ Life Events
├── Moving, Graduating, Getting Married
├── Smaller audiences, high intent
└── Time-sensitive targeting

□ Custom Audiences
├── Keyword-based: People searching for X
├── URL-based: Visitors of competitor sites
└── App-based: Users of specific apps

LAYER 3: CONTENT TARGETING
──────────────────────────
□ Topics
├── Content categories
├── Broad reach
└── Brand safety considerations

□ Placements
├── Specific YouTube channels
├── Specific videos
├── YouTube homepage

□ Keywords
├── Video content targeting
├── Combine with other targeting
└── Add negatives for brand safety
```

### Audience Strategy per Funnel Stage

```
FUNNEL-BASED TARGETING STRATEGY
═══════════════════════════════

AWARENESS (Top of Funnel)
─────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Goal: Maximum reach within target audience               │
│                                                         │
│ Targeting:                                              │
│ ├── Demographics + Affinity Audiences                   │
│ ├── Topic targeting (related content)                   │
│ └── Lookalike audiences (similar to converters)         │
│                                                         │
│ Formats: Bumper Ads, Non-skip In-Stream                 │
│ KPIs: CPM, Reach, Brand Lift                            │
│ Budget: 40% of video budget                             │
└─────────────────────────────────────────────────────────┘

CONSIDERATION (Middle of Funnel)
────────────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Goal: Stimulate engagement and consideration             │
│                                                         │
│ Targeting:                                              │
│ ├── In-Market Audiences                                 │
│ ├── Custom Audiences (competitor keywords)              │
│ ├── Video viewers (awareness campaigns)                 │
│ └── Website visitors (soft remarketing)                 │
│                                                         │
│ Formats: Skippable In-Stream, In-Feed Video             │
│ KPIs: View Rate, CPV, Engagement Rate                   │
│ Budget: 30% of video budget                             │
└─────────────────────────────────────────────────────────┘

CONVERSION (Bottom of Funnel)
─────────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Goal: Direct action / conversion                         │
│                                                         │
│ Targeting:                                              │
│ ├── Cart abandoners (remarketing)                       │
│ ├── Product page viewers                                │
│ ├── Previous converters (cross-sell/upsell)             │
│ └── Video completers (high intent)                      │
│                                                         │
│ Formats: Demand Gen (video) — formerly Video Action     │
│ KPIs: CPA, ROAS, Conversions                            │
│ Budget: 30% of video budget                             │
└─────────────────────────────────────────────────────────┘
```

## Video Creative Best Practices

### ABCD Framework

```
GOOGLE'S ABCD FRAMEWORK FOR VIDEO ADS
══════════════════════════════════════

A - ATTRACT (First 5 seconds)
─────────────────────────────
□ Open with action or intrigue
□ Faces grab attention
□ Movement in first frame
□ Audio hook (music or voice)
□ Contrast and bright colors
□ Avoid slow builds

EXAMPLES:
✓ "What if you could save $500 on..."
✓ [Person runs into frame, turns around]
✓ [Product in action, direct demo]
✗ Logo fade-in for 3 seconds
✗ Slow establishing shots

B - BRAND (Early and often)
───────────────────────────
□ Brand in first 5 seconds
□ Logo visible (corner or watermark)
□ Brand colors consistent
□ Audio branding (jingle, voice)
□ Show product in context
□ Repeat brand at end

BRAND INTEGRATION TIPS:
├── Logo overlay: 10% screen size
├── Brand mention: Within 8 seconds
├── Product visibility: 50%+ of video
└── End card: Minimum 3 seconds

C - CONNECT (Emotion and Story)
───────────────────────────────
□ Relatable situations
□ Humor (if appropriate for brand)
□ Music supports emotion
□ Human elements
□ Problem-solution structure
□ Testimonials or user stories

STORY STRUCTURES:
├── Problem → Solution → CTA
├── Before → After → How
├── Question → Discovery → Answer
└── Teaser → Reveal → Action

D - DIRECT (Clear CTA)
───────────────────────
□ Ask for specific action
□ Create urgency (if relevant)
□ Visual CTA button
□ Verbal CTA in audio
□ End with clear next step
□ Use words like: "Shop now", "Learn more"

CTA BEST PRACTICES:
├── Maximum 1 CTA per video
├── Repeat CTA 2x (middle + end)
├── CTA button: Contrasting color
└── Urgency: "Now", "Today", "Limited"
```

### Video Length Recommendations

```
VIDEO LENGTH PER GOAL
═════════════════════

AWARENESS CAMPAIGNS
───────────────────
├── Bumper: 6 seconds (no choice)
├── Non-skip: 15 seconds (standard)
└── Skippable: 15-20 seconds recommended
    └── Focus on memorability, not story

CONSIDERATION CAMPAIGNS
───────────────────────
├── Skippable: 30-60 seconds optimal
├── In-Feed: 2-3 minutes allowed
└── Longer videos for:
    ├── Product demos
    ├── How-to content
    └── Testimonials

CONVERSION CAMPAIGNS
────────────────────
├── Video Action: 15-30 seconds optimal
├── Product focus ads: 10-20 seconds
└── Remarketing: 15 seconds (they already know you)

RETENTION CURVES (average):
───────────────────────────
6 sec:  ██████████████████████████████████████ 95%
15 sec: ████████████████████████████████████   90%
30 sec: █████████████████████████████          70%
60 sec: █████████████████████                  50%
2 min:  ████████████                           30%
5 min:  ████████                               20%
```

## YouTube Campaign Setup

### Step-by-Step Setup

```
YOUTUBE VIDEO CAMPAIGN SETUP
════════════════════════════

STEP 1: CHOOSE CAMPAIGN GOAL
─────────────────────────────
□ Sales: Video Action Campaigns
□ Leads: Video Action Campaigns
□ Website Traffic: Video Views
□ Brand Awareness: Video Reach
□ Product/Brand Consideration: Video Views

STEP 2: CAMPAIGN SUBTYPE
─────────────────────────
□ Video Reach: Maximum reach (bumpers/non-skip)
□ Video Views: Skippable in-stream + in-feed
□ Ad Sequence: Storytelling with multiple videos
□ Demand Gen (conversion video): Use Demand Gen campaign type instead
  (Video Action Campaigns were merged into Demand Gen in 2025)

STEP 3: BID STRATEGY SELECTION
──────────────────────────────
┌─────────────────────────┬───────────────────────────────┐
│ Campaign Type           │ Recommended Bid Strategy      │
├─────────────────────────┼───────────────────────────────┤
│ Video Reach             │ Target CPM                    │
│ Video Views             │ Maximum CPV                   │
│ Demand Gen (video)      │ Target CPA / Maximize Conv    │
│ Brand Awareness         │ Target CPM                    │
└─────────────────────────┴───────────────────────────────┘

STEP 4: TARGETING SETUP
────────────────────────
□ Define audiences (demographics + interests)
□ Set content exclusions
□ Device targeting (optional)
□ Frequency capping: 3-5x per week recommended
□ Schedule: All day or peak hours

STEP 5: VIDEO AD CREATION
──────────────────────────
□ Upload video to YouTube (unlisted OK)
□ Set Final URL
□ Add CTA (Video Action only)
□ Add companion banner (300x60)
□ Preview on mobile and desktop
```

### Budget and Bidding

```
YOUTUBE BUDGET GUIDELINES
═════════════════════════

MINIMUM BUDGETS:
────────────────
├── Bumper/Non-skip: $20/day minimum
├── Skippable In-Stream: $10/day minimum
├── Video Action: $30/day minimum (conversion focus)
└── In-Feed: $10/day minimum

BENCHMARK CPV/CPM RANGES:
─────────────────────────
├── Bumper Ads: $3-7 CPM
├── Non-skip 15s: $8-15 CPM
├── Skippable In-Stream: $0.03-0.08 CPV
├── In-Feed Video: $0.02-0.05 CPV
└── Video Action: $0.10-0.30 CPV (conversion-optimized)

BUDGET ALLOCATION (Full-Funnel):
────────────────────────────────
Awareness (Reach):     40% │████████████████
Consideration (Views): 30% │████████████
Conversion (Action):   30% │████████████

BIDDING TIPS:
─────────────
├── Start 20% above benchmark, optimize downward
├── Video Action: Start without target, add after 50 conv
├── CPM campaigns: Watch frequency (not >5x/week)
└── Seasonal adjustment: +20-30% during peak periods
```

## YouTube Remarketing Strategies

### Video Remarketing Audiences

```
YOUTUBE REMARKETING AUDIENCES
═════════════════════════════

AVAILABLE AUDIENCES:
────────────────────
□ Channel subscribers
□ Channel visitors
□ Video viewers (specific videos)
□ Video viewers (any video)
□ Video likes
□ Video shares
□ Video comments
□ Playlist adds

VIDEO VIEW SEGMENTATION:
────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Audience                  │ Intent Level │ Retarget with│
├───────────────────────────┼──────────────┼──────────────┤
│ Viewed any video          │ Low          │ Awareness    │
│ Viewed 25% of video       │ Medium-Low   │ Consideration│
│ Viewed 50% of video       │ Medium       │ Consideration│
│ Viewed 75% of video       │ Medium-High  │ Conversion   │
│ Viewed 100% of video      │ High         │ Conversion   │
│ Engaged (like/comment)    │ Very High    │ Conversion   │
│ Subscribed                │ Highest      │ Loyalty      │
└───────────────────────────┴──────────────┴──────────────┘

REMARKETING FLOW:
─────────────────
1. Awareness Ad Viewers (25%+)
   └─► Retarget with Consideration Video (30 days)

2. Consideration Viewers (50%+)
   └─► Retarget with Video Action Campaign (14 days)

3. Video Action Non-Converters
   └─► Retarget with Display/Search (7 days)

4. Converters
   └─► Exclude or Cross-sell campaign
```

### Sequential Video Ads

```
AD SEQUENCING STRATEGY
══════════════════════

WHAT IS AD SEQUENCING:
──────────────────────
Show multiple videos to the same user in a fixed
order to build a story.

SEQUENCE TYPES:
───────────────
1. INTRODUCE → REINFORCE → CONVERT
   ├── Video 1: Brand story (60 sec skippable)
   ├── Video 2: Product benefits (30 sec skippable)
   └── Video 3: CTA + offer (15 sec skippable)

2. TEASER → REVEAL → REMIND
   ├── Video 1: Teaser bumper (6 sec)
   ├── Video 2: Full reveal (45 sec)
   └── Video 3: Reminder bumper (6 sec)

3. PROBLEM → SOLUTION → PROOF
   ├── Video 1: Identify problem (20 sec)
   ├── Video 2: Present solution (40 sec)
   └── Video 3: Social proof/testimonial (30 sec)

SETUP IN GOOGLE ADS:
────────────────────
Campaign type: Video
Campaign subtype: Ad sequence
└─► Add steps with different videos
    ├── Step 1: Impression-based (show to all)
    ├── Step 2: View-based (25%+ of step 1)
    └── Step 3: View-based (50%+ of step 2)
```



See [detailed-reference.md](references/detailed-reference.md) for details.



## Measurement & Optimization

### Key Metrics per Campaign Type

```
YOUTUBE METRICS PER CAMPAIGN TYPE
═════════════════════════════════

⚠️ API METRIC NAME CHANGES (v22+):
   video_views         → metrics.video_trueview_views
   average_cpv         → metrics.trueview_average_cpv
   These renames apply when querying via GAQL / MCP tool calls.
   The Google Ads UI still shows "Video views" and "Avg. CPV" as friendly names.

AWARENESS (Reach) CAMPAIGNS:
────────────────────────────
Primary KPIs:
├── Unique Reach: Number of unique users
├── CPM: Cost per 1000 impressions (metrics.average_cpm)
├── Frequency: Average number of views per person
└── Brand Lift: Survey-based brand metrics

Secondary KPIs:
├── Impressions (metrics.impressions)
├── Video plays
└── Earned views (shares, subscribes)

CONSIDERATION (Views) CAMPAIGNS:
────────────────────────────────
Primary KPIs:
├── View Rate: Views / Impressions (metrics.video_view_rate)
├── CPV: Cost per view (API: metrics.trueview_average_cpv)
├── Watch Time: Average watch time
└── Engagement Rate: Likes + Comments + Shares

Secondary KPIs:
├── 25% / 50% / 75% / 100% completion rates
├── Click-through rate (metrics.ctr)
└── Earned subscribers

CONVERSION (Action/Demand Gen) CAMPAIGNS:
──────────────────────────────────────────
Primary KPIs:
├── Conversions (metrics.conversions)
├── CPA: Cost per acquisition (metrics.cost_per_conversion)
├── ROAS: Return on ad spend (metrics.conversions_value / cost)
└── Conversion Rate (metrics.conversions_from_interactions_rate)

Secondary KPIs:
├── View-through conversions (metrics.view_through_conversions)
├── Click-through conversions
└── Assisted conversions

BENCHMARK TARGETS:
──────────────────
├── View Rate: >25% (skippable in-stream)
├── CTR: >0.5%
├── Video Completion (100%): >15%
├── CPV: <$0.08 (brand), <$0.15 (action)
└── CPA: Depends on industry
```

### MCP Tool Integration

```
STEP 1: YouTube campaign performance overview
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign.status,
    campaign.advertising_channel_type,
    campaign.bidding_strategy_type,
    metrics.impressions,
    metrics.video_trueview_views,
    metrics.video_view_rate,
    metrics.trueview_average_cpv,
    metrics.clicks,
    metrics.ctr,
    metrics.cost_micros
  FROM campaign
  WHERE campaign.advertising_channel_type IN ('VIDEO', 'DEMAND_GEN')
    AND campaign.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")

STEP 2: Video completion rates
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    ad_group.name,
    metrics.video_quartile_p25_rate,
    metrics.video_quartile_p50_rate,
    metrics.video_quartile_p75_rate,
    metrics.video_quartile_p100_rate,
    metrics.video_trueview_views,
    metrics.impressions
  FROM ad_group
  WHERE campaign.advertising_channel_type IN ('VIDEO', 'DEMAND_GEN')
    AND campaign.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.impressions DESC
  LIMIT 50
")

STEP 3: Conversion-focused (Demand Gen with video)
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    metrics.conversions,
    metrics.cost_per_conversion,
    metrics.view_through_conversions,
    metrics.cost_micros,
    metrics.impressions
  FROM campaign
  WHERE campaign.advertising_channel_type = 'DEMAND_GEN'
    AND campaign.status = 'ENABLED'
    AND segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")
```

## Output: YouTube Ads Strategy Template

```markdown
# YouTube Ads Strategy Document

## Executive Summary
- **Advertiser:** [Name]
- **Campaign Goal:** [Awareness/Consideration/Conversion]
- **Budget:** $[X]/month
- **Duration:** [Start] - [End]

## Target Audience
- **Demographics:** [Age, Gender, Location]
- **Interests:** [Affinity audiences]
- **In-Market:** [Relevant categories]
- **Custom Audiences:** [Keywords/URLs]

## Campaign Structure
| Campaign | Type | Format | Budget/day | Bid |
|----------|------|--------|------------|-----|
| [Name] | [Type] | [Format] | $[X] | [Strategy] |

## Creative Strategy
### Video Assets Needed:
- [ ] Awareness video: [X] sec
- [ ] Consideration video: [X] sec
- [ ] Conversion video: [X] sec
- [ ] Bumper ads: 6 sec x [X]

### Key Messages per Video:
1. **Awareness:** [Message]
2. **Consideration:** [Message]
3. **Conversion:** [Message]

## Targeting Strategy
### Funnel Stage 1: Awareness
- **Audience:** [Details]
- **Formats:** [Bumper/Non-skip]
- **Frequency Cap:** [X] per week

### Funnel Stage 2: Consideration
- **Audience:** [Awareness viewers + In-market]
- **Formats:** [Skippable/In-feed]
- **Frequency Cap:** [X] per week

### Funnel Stage 3: Conversion
- **Audience:** [Consideration viewers + Remarketing]
- **Formats:** [Video Action]
- **Frequency Cap:** [X] per week

## Success Metrics
| KPI | Target | Measurement |
|-----|--------|-------------|
| Reach | [X] | Unique users |
| View Rate | [X]% | Views/Impressions |
| CPV | $[X] | Cost/View |
| Conversions | [X] | Via Google Ads |
| CPA | $[X] | Cost/Conversion |

## Timeline & Milestones
- Week 1-2: Launch awareness phase
- Week 3-4: Analyze, optimize, add consideration
- Week 5-6: Scale performing audiences
- Week 7-8: Full-funnel activation

## Notes
[Additional notes]
```
