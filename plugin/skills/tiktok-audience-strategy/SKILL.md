---
name: tiktok-audience-strategy
description: "This skill should be used when the user asks to \"build TikTok audiences\", \"choose TikTok lookalike size\", \"set up TikTok custom audiences\", \"decide between broad and narrow targeting on TikTok\", or mentions \"TikTok audience strategy\", \"audience refresh cadence\", or \"TikTok interest targeting\". Do NOT use for: creative optimization (use tiktok-hook-optimization-guide), Spark Ads strategy (use tiktok-spark-ads-strategy), or product/shopping ads (use tiktok-shopping-ads-guide)."
---

# TikTok Audience Strategy

## Purpose

Help advertisers build and manage audience targeting strategies on TikTok that balance reach with relevance. TikTok's algorithm is exceptionally good at finding the right users within broad audiences — often outperforming narrow targeting. This skill provides frameworks for when to go broad vs narrow, how to build and layer audiences, lookalike sizing guidance, and refresh cadence to prevent audience fatigue.

## When to Use This Skill

Invoke when user mentions:
- **Targeting:** "How should I target my TikTok ads?"
- **Audiences:** "How do I build audiences on TikTok?"
- **Lookalikes:** "What lookalike size should I use on TikTok?"
- **Broad vs narrow:** "Should I use interest targeting or go broad?"
- **Custom audiences:** "How do I create a custom audience from my pixel?"
- **Audience refresh:** "When should I refresh my TikTok audiences?"

## Required Tools

| Tool | Purpose |
|------|---------|
| `tiktok_get_audiences` | Retrieve existing audiences, their sizes, and configurations |
| `tiktok_query` | Pull campaign targeting configurations and audience performance |

---

## Part 1: TikTok Targeting Architecture

### Targeting Layer Overview

```
TIKTOK TARGETING HIERARCHY:
───────────────────────────

LAYER 0: SEARCH ADS (highest intent — new as of Sep 2025)
├── Keyword-based targeting in TikTok's built-in search
├── Reaches users actively searching on TikTok
├── Formats: text ads and video ads in search results
├── Best for: high-intent users, product discovery
└── Note: TikTok Search Ads available in most markets since Q3 2025

LAYER 1: DEMOGRAPHICS (broadest)
├── Location (country, region, DMA)
├── Age (13-17, 18-24, 25-34, 35-44, 45-54, 55+)
├── Gender (male, female, all)
├── Language
└── These are always set, even in "broad" campaigns

LAYER 2: INTERESTS (medium precision)
├── Interest categories (predefined by TikTok)
├── Based on: content consumed, accounts followed, interactions
├── Examples: "Fashion", "Cooking", "Fitness", "Technology"
├── Can select multiple interests (OR logic within category)
└── Refreshes: Updates dynamically based on recent behavior

LAYER 3: BEHAVIORS (higher precision)
├── Video interactions (liked, commented, shared specific content types)
├── Creator interactions (followed certain creator categories)
├── Hashtag interactions (engaged with specific hashtags)
└── More recent signal than interests (last 7-15 days of activity)

LAYER 4: CUSTOM AUDIENCES (highest precision)
├── Pixel-based (website visitors, converters)
├── Engagement-based (ad interactions, video views)
├── Customer file (email/phone upload)
├── App activity (install, in-app events)
└── Lead generation (people who submitted lead forms)

LAYER 5: LOOKALIKE AUDIENCES (algorithmic expansion)
├── Built from any custom audience
├── Sizes: Narrow (1%), Balanced (2-3%), Broad (5-10%)
├── TikTok finds users similar to your seed audience
└── Quality depends heavily on seed audience quality
```

### Targeting Logic Rules

```
WITHIN a targeting category: OR logic
├── Interest: "Fashion" OR "Beauty" → users interested in either
├── Behavior: "Liked cooking videos" OR "Follows food creators"
└── Result: Broader audience (union of groups)

BETWEEN targeting categories: AND logic
├── Interest: "Fashion" AND Behavior: "Shopping app users"
├── Result: Narrower audience (intersection of groups)
└── Every additional category narrows the audience

EXCLUSIONS: NOT logic
├── Custom audience exclusion: NOT "past purchasers"
├── Result: Removes excluded users from targeting
└── Essential for separating prospecting from retargeting
```

---

## Part 2: The Broad vs Narrow Framework

### TikTok's Algorithm Advantage

TikTok's recommendation algorithm is among the most sophisticated in advertising. It can identify high-intent users from behavioral signals that manual targeting cannot capture. This fundamentally changes the broad vs narrow calculus compared to other platforms.

```
BROAD TARGETING ON TIKTOK:
├── Demographics only (age + gender + location)
├── No interest or behavior layering
├── Let TikTok's algorithm find the best users
├── Requires: Strong pixel data (50+ conversions/week)
├── Requires: Compelling creative (algorithm needs engagement signals)
├── Performance: Often outperforms narrow by 10-30% CPA after learning
└── Learning period: 5-10 days (longer than narrow)

NARROW TARGETING ON TIKTOK:
├── Demographics + interests + behaviors
├── You pre-select who should see the ad
├── Algorithm optimizes within your constraints
├── Requires: Accurate audience understanding
├── Requires: Sufficient audience size (>500K for conversions)
├── Performance: Faster learning, more predictable, may cap out sooner
└── Learning period: 3-5 days
```

### When to Use Broad vs Narrow

| Scenario | Recommended | Why |
|----------|-------------|-----|
| New account, no pixel data | Narrow | Algorithm needs guidance without conversion history |
| Mature account, 50+ conv/week | Broad or Smart+ | Algorithm can optimize from rich data; Smart+ campaigns automate this |
| Niche product (small TAM) | Narrow | Broad wastes spend on irrelevant users |
| Mass market product | Broad | TikTok finds buyers you wouldn't target |
| Brand awareness campaign | Broad | Maximize reach, let algorithm optimize |
| Retargeting campaign | Custom audience | Precision matters, known intent |
| Testing new market/geo | Narrow first | Learn what works before going broad |
| Scaling proven campaign | Move narrow → broad | Expand after proving unit economics |
| High AOV / long sales cycle | Narrow | Can't afford waste on unqualified users |
| Low AOV / impulse purchase | Broad | Volume economics favor broad reach |

### The Broad Testing Protocol

```
PHASE 1: ESTABLISH BASELINE WITH NARROW (Week 1-2)
├── Set up campaign with interest + behavior targeting
├── Budget: €50-100/day
├── Goal: Establish baseline CPA with 20+ conversions
├── Record: CPA, CTR, CVR, audience size, delivery
└── This is your benchmark

PHASE 2: LAUNCH BROAD TEST (Week 3-4)
├── Duplicate campaign, remove all interest/behavior targeting
├── Keep: Demographics only (age, gender, location)
├── Budget: Same as narrow campaign
├── Goal: Let algorithm learn (expect higher CPA in first 5 days)
└── Patience: Don't judge until 20+ conversions

PHASE 3: COMPARE AND DECIDE (Week 5)
├── Compare CPA: Broad within 25% of narrow? → Go broad
├── Compare scale: Broad delivering more volume at similar CPA? → Go broad
├── Compare quality: Check downstream conversion quality (LTV, repeat rate)
├── If broad wins: Shift 70% budget to broad, keep 30% narrow as safety net
└── If narrow wins: Maintain narrow, retest broad in 30 days with new creative

PHASE 4: HYBRID (Ongoing)
├── 60-70% budget on winning strategy
├── 20-30% budget on the other strategy (hedge)
└── 10% budget on testing new audiences
```

---

## Part 3: Custom Audience Types

### Pixel-Based Custom Audiences

```
tiktok_get_audiences(
    audience_type="custom"
)
```

| Pixel Event | Audience Name | Window | Min Size | Use Case |
|-------------|--------------|--------|----------|----------|
| PageView | All Visitors | 30 days | 1,000 | Broad retargeting |
| ViewContent | Product Viewers | 14 days | 1,000 | Product-specific retargeting |
| AddToCart | Cart Abandoners | 7 days | 500 | Abandoned cart recovery |
| InitiateCheckout | Checkout Abandoners | 3 days | 300 | Urgent recovery (highest intent) |
| CompletePayment | Purchasers | 180 days | 1,000 | Exclusion + lookalike seed |
| CompleteRegistration | Leads/Signups | 90 days | 500 | Upsell + lookalike seed |

### Engagement-Based Custom Audiences

| Engagement Type | Signal Strength | Recommended Window | Min Events |
|----------------|----------------|-------------------|------------|
| Video view (any) | Low | 30 days | 5,000 |
| Video view (50%+) | Medium | 21 days | 2,000 |
| Video view (75%+) | High | 14 days | 1,000 |
| Video view (100%) | Very high | 14 days | 500 |
| Clicked ad | High | 14 days | 500 |
| Profile visit | Medium-High | 30 days | 1,000 |
| Liked ad | Medium | 21 days | 1,000 |
| Commented on ad | Very high | 30 days | 200 |
| Shared ad | Very high | 30 days | 200 |

### Customer File Audiences

Upload your CRM data for precise targeting:

```
SUPPORTED IDENTIFIERS (in order of match rate):
1. Phone number (hashed, E.164 format) — 60-80% match rate
2. Email address (hashed, lowercase) — 40-60% match rate
3. IDFA / GAID (mobile advertising IDs) — 70-85% match rate

MINIMUM SIZE: 1,000 records (TikTok requirement)
RECOMMENDED: 5,000+ records for reliable matching

BEST PRACTICES:
├── Hash all PII before upload (SHA-256)
├── Normalize emails (lowercase, trim whitespace)
├── Normalize phone numbers (E.164: +31612345678)
├── Include both email AND phone when available (+15-20% match)
├── Remove duplicates before upload
├── Update lists monthly (add new customers, remove churned)
└── Segment lists by value (high-value, medium-value, churned)
```

### Custom Audience Layering Strategy

```
AUDIENCE PRIORITY PYRAMID:

                    ┌──────────────┐
                    │   Checkout    │  Window: 3 days
                    │  Abandoners   │  Priority: HIGHEST
                    ├──────────────┤  Budget: 15% of retargeting
                    │    Cart      │
                    │  Abandoners  │  Window: 7 days
                    ├──────────────┤  Budget: 20% of retargeting
                    │   Product    │
                    │   Viewers    │  Window: 14 days
                    ├──────────────┤  Budget: 25% of retargeting
                    │    All       │
                    │   Visitors   │  Window: 30 days
                    ├──────────────┤  Budget: 20% of retargeting
                    │  Engagement  │
                    │  (video 50%+)│  Window: 21 days
                    └──────────────┘  Budget: 20% of retargeting

Each layer EXCLUDES the layer above it:
├── Cart Abandoners excludes Checkout Abandoners
├── Product Viewers excludes Cart + Checkout Abandoners
├── All Visitors excludes Product Viewers + Cart + Checkout
└── Engagement excludes All Visitors + above
```

---

## Part 4: Lookalike Audience Strategy

### Lookalike Sizing Guide

```
LOOKALIKE SIZE SPECTRUM:

 1%     2%     3%     5%     10%
  │      │      │      │       │
  ▼      ▼      ▼      ▼       ▼
Most                         Most
Similar                      Reach
to seed                      (less
                             similar)

Size selection depends on:
├── Seed quality (high quality seed → can go broader)
├── Campaign objective (conversions → narrow, awareness → broad)
├── Budget (small budget → narrow, large budget → broad)
├── Market size (small market → broader to get reach)
└── Current performance (strong CPA → test broader for scale)
```

### Recommended Lookalike Sizes by Use Case

| Seed Audience | Seed Size | Recommended Lookalike | Rationale |
|---------------|-----------|----------------------|-----------|
| Purchasers (high AOV) | 1,000-5,000 | 1-2% | Highest quality seed, keep precision |
| Purchasers (all) | 5,000-20,000 | 2-3% | Good quality, moderate expansion |
| Leads / Signups | 5,000-50,000 | 3-5% | Medium quality, need more reach |
| Add to Cart | 2,000-10,000 | 2-3% | Strong intent signal |
| Product Viewers | 10,000-100,000 | 3-5% | Weaker signal, need algorithmic help |
| Video Viewers (75%+) | 5,000-50,000 | 3-5% | Engagement signal, not conversion |
| Customer File (top 20% LTV) | 1,000-5,000 | 1-2% | Best seed possible |
| Customer File (all) | 5,000-50,000 | 2-3% | Good general seed |
| Email subscribers | 10,000-100,000 | 3-5% | Interest signal, not purchase |
| Website visitors | 50,000+ | 5-10% | Broad signal, need expansion |

### Lookalike Testing Framework

```
TEST STRUCTURE: Same creative, same budget, different lookalike sizes

Ad Group A: 1% lookalike from purchasers     → €30/day
Ad Group B: 3% lookalike from purchasers     → €30/day
Ad Group C: 5% lookalike from purchasers     → €30/day
Ad Group D: Broad (no lookalike, interests)  → €30/day

RUN FOR: 7-14 days minimum
METRIC: CPA as primary, volume as secondary

TYPICAL RESULTS:
├── 1% LAL: Lowest CPA, lowest volume
├── 3% LAL: Slightly higher CPA, 2-3x volume
├── 5% LAL: Moderate CPA, 3-5x volume
└── Broad: Variable CPA, maximum volume

DECISION FRAMEWORK:
├── If 1% CPA is >30% better than 3% → Stay narrow
├── If 3% CPA is within 15% of 1% → Use 3% (better scale)
├── If 5% CPA is within 25% of 1% → Use 5% (best scale)
└── If broad beats all LAL → Go broad (algorithm is better)
```

### Seed Audience Quality Checklist

Before creating a lookalike, verify your seed audience:

```
□ Seed size: At least 1,000 users (minimum for TikTok LAL)
□ Seed recency: Based on last 90 days of data (not historical)
□ Seed action: Based on conversion event, not just visits
□ Seed purity: Excludes fraud, bot traffic, and employees
□ Seed relevance: Matches the audience you want to find more of
□ Seed diversity: Not dominated by a single demographic segment
□ Seed value: Ideally based on high-value customers, not all customers
```

---

## Part 5: Interest and Behavior Targeting

### Interest Category Performance Guide

| Interest Category | Audience Size (est.) | Avg CPM | Avg CTR | Competition |
|------------------|---------------------|---------|---------|-------------|
| Fashion & Apparel | Very Large | €4-8 | 1.2-2.0% | High |
| Beauty & Personal Care | Very Large | €5-10 | 1.5-2.5% | Very High |
| Food & Beverage | Very Large | €3-7 | 1.3-2.2% | Medium |
| Technology & Electronics | Large | €5-10 | 0.8-1.5% | High |
| Fitness & Sports | Large | €4-8 | 1.0-1.8% | Medium |
| Home & Garden | Medium | €3-7 | 1.0-1.6% | Medium |
| Pets & Animals | Medium | €3-6 | 1.5-2.5% | Low |
| Education & Learning | Medium | €4-8 | 0.8-1.4% | Medium |
| Business & Finance | Small-Medium | €6-12 | 0.6-1.2% | High |
| Travel & Tourism | Large | €4-9 | 1.0-1.8% | Medium-High |
| Gaming | Very Large | €3-6 | 1.2-2.0% | High |
| Parenting & Family | Medium | €4-8 | 1.0-1.8% | Medium |

### Behavior Targeting Options

```
PURCHASE BEHAVIORS:
├── TikTok Shop purchasers (high commercial intent)
├── In-app purchase users (willingness to pay)
├── Frequent online shoppers (cross-platform signal)
└── Category-specific purchasers (e.g., "bought fashion items")

CONTENT BEHAVIORS (last 15 days):
├── Liked videos in category (medium intent)
├── Commented on videos in category (high engagement)
├── Shared videos in category (high advocacy)
├── Followed accounts in category (sustained interest)
└── Watched full videos in category (deep engagement)

DEVICE/TECH BEHAVIORS:
├── Operating system (iOS vs Android)
├── Device price range (proxy for income)
├── Connection type (WiFi vs cellular)
├── New device users (recently upgraded)
└── App categories installed (interest proxy)

CREATOR INTERACTION BEHAVIORS:
├── Followed specific creator categories
├── Watched creator content in specific verticals
├── Engaged with branded content from creators
└── Interacted with Spark Ads
```

### Interest + Behavior Stacking

```
STACKING EXAMPLE: E-COMMERCE FASHION BRAND

Targeting Strategy A (Interest-Only):
├── Interest: "Fashion & Apparel"
├── Audience size: ~50M (US)
└── Too broad for conversion campaigns

Targeting Strategy B (Interest + Behavior):
├── Interest: "Fashion & Apparel"
├── AND Behavior: "Online shoppers" + "Engaged with fashion content"
├── Audience size: ~8M (US)
└── Better precision, still ample scale

Targeting Strategy C (Behavior-Only):
├── Behavior: "Purchased fashion items on TikTok Shop" +
│   "Engaged with fashion brand content in last 15 days"
├── Audience size: ~2M (US)
└── Highest intent, limited scale

RECOMMENDATION: Start with B, test C as a separate ad group.
If pixel has 50+ conversions/week, also test broad (demographics only).
```

---

## Part 6: Audience Refresh Strategy

### Why Audiences Need Refreshing

TikTok audiences fatigue faster than other platforms because:
1. Users scroll 2-3x more content per session than Meta/LinkedIn
2. Creative fatigue sets in at 4-7 days (vs 10-14 on Meta)
3. Custom audiences based on short windows shrink as users fall out
4. Lookalike models are static at creation time (don't auto-update)

### Refresh Cadence by Audience Type

| Audience Type | Refresh Cadence | How to Refresh |
|---------------|----------------|----------------|
| Interest targeting | No refresh needed | TikTok updates dynamically |
| Behavior targeting | No refresh needed | TikTok updates dynamically |
| Pixel custom audience | Auto-refreshes | Ensure pixel is firing correctly |
| Customer file upload | Every 14-30 days | Re-upload with new customers |
| Lookalike audience | Every 14-21 days | Recreate from updated seed |
| Engagement audience | Auto-refreshes | Check for window size optimization |

### Lookalike Refresh Protocol

```
WEEK 0: Create lookalike from purchasers (last 90 days)
WEEK 2: Check performance — if CPA rising, refresh:
         ├── Re-export purchaser list (now includes 14 more days of data)
         ├── Create new lookalike (TikTok may find new patterns)
         ├── Launch new ad group with refreshed lookalike
         └── Pause old ad group after 2-day overlap
WEEK 4: Repeat refresh process
WEEK 6: Evaluate if seed audience has grown enough to change size
         ├── If seed grew 50%+: Test broader lookalike (e.g., 1% → 3%)
         └── If seed stable: Maintain current lookalike size
```

### Audience Fatigue Signals

| Signal | Threshold | Action |
|--------|-----------|--------|
| CPM rising >20% week-over-week | Yellow alert | Monitor for 3 more days |
| CPM rising >40% week-over-week | Red alert | Refresh audience immediately |
| CTR declining >15% week-over-week | Yellow alert | May be creative fatigue, not audience |
| Frequency >2x per week (per user) | Yellow alert | Audience too small for budget |
| Frequency >4x per week (per user) | Red alert | Expand audience or reduce budget |
| Conversion rate declining while CTR stable | Audience quality declining | Refresh lookalike or tighten targeting |

---

## Part 7: Exclusion Strategy

### Essential Exclusion List

```
ALWAYS EXCLUDE:
├── Recent purchasers (7-30 days) from prospecting campaigns
├── Existing customers (customer file) from acquisition campaigns
├── Lead form submitters from lead gen campaigns
├── App installers from install campaigns
├── Employees/team members (customer file upload)
└── Bot/fraud traffic (if identifiable via pixel patterns)

CONDITIONAL EXCLUSIONS:
├── Cart abandoners from retargeting (if separate campaign exists)
├── High-frequency users (8+ impressions) from brand campaigns
├── Negative engagers (hidden ad, reported) from all campaigns
└── Specific geos where you can't fulfill
```

### Exclusion Architecture

```
CAMPAIGN: Prospecting (new customers)
├── Include: Interest/Behavior targeting OR Broad OR Lookalike
├── Exclude: All custom audiences (purchasers, visitors, leads)
└── Goal: Only reach people who haven't interacted with your brand

CAMPAIGN: Retargeting (mid-funnel)
├── Include: Website visitors (14 days)
├── Exclude: Purchasers (30 days) + cart abandoners (if separate campaign)
└── Goal: Re-engage visitors who didn't convert

CAMPAIGN: Retargeting (bottom-funnel)
├── Include: Cart abandoners (7 days) + checkout abandoners (3 days)
├── Exclude: Purchasers (7 days)
└── Goal: Recover abandoned carts and checkouts

CAMPAIGN: Retention/Upsell
├── Include: Purchasers (30-180 days)
├── Exclude: Recent purchasers (7 days) — avoid post-purchase annoyance
└── Goal: Cross-sell, upsell, repeat purchase
```

---

## Part 8: Audience Testing Framework

### The Systematic Audience Test

```
TESTING HIERARCHY (test in this order):

TEST 1: Broad vs Interest (foundational)
├── Ad Group A: Broad (demographics only)
├── Ad Group B: Interest targeting (your best hypothesis)
├── Budget: Equal split, €30-50/day each
├── Duration: 7-10 days
└── Winner determines your base targeting approach

TEST 2: Interest vs Behavior vs Combined
├── Ad Group A: Interest only
├── Ad Group B: Behavior only
├── Ad Group C: Interest AND Behavior (stacked)
├── Budget: Equal split
├── Duration: 7-10 days
└── Identify which signal type works best for your product

TEST 3: Lookalike sizing
├── Ad Group A: 1% LAL from best seed
├── Ad Group B: 3% LAL from same seed
├── Ad Group C: 5% LAL from same seed
├── Budget: Equal split
├── Duration: 7-10 days
└── Find the optimal LAL size for your business

TEST 4: Seed audience quality
├── Ad Group A: LAL from purchasers
├── Ad Group B: LAL from high-value purchasers (top 20% LTV)
├── Ad Group C: LAL from leads
├── Budget: Equal split
├── Duration: 7-10 days
└── Determine which seed produces the best LAL
```

### Audience Performance Tracking

```
tiktok_query(
    entity_type="adgroups",
    status="ADGROUP_STATUS_ENABLE"
)

tiktok_get_audiences()
```

Track audience performance over time:

| Audience | Week 1 CPA | Week 2 CPA | Week 3 CPA | Week 4 CPA | Trend | Action |
|----------|-----------|-----------|-----------|-----------|-------|--------|
| Interest: Fashion | €12 | €13 | €15 | €18 | Rising | Refresh creative or expand |
| LAL 3% Purchasers | €10 | €11 | €11 | €13 | Stable | Maintain, refresh LAL at Week 3 |
| Broad (demo only) | €18 | €14 | €11 | €10 | Declining | Algorithm learning, scale up |
| Retargeting: Cart | €5 | €6 | €7 | €8 | Slowly rising | Normal, check frequency |

---

## Part 9: Advanced Audience Techniques

### Value-Based Lookalikes

Instead of using all purchasers as a seed, segment by value:

```
SEED SEGMENTATION:

Tier 1 Seed: Top 10% by LTV
├── Customers who purchased 3+ times OR spent >€200
├── Best for: 1% lookalike (highest quality)
└── Expected result: 20-40% lower CPA than all-purchaser LAL

Tier 2 Seed: Top 30% by LTV
├── Customers who purchased 2+ times OR spent >€100
├── Best for: 2-3% lookalike (good quality + scale)
└── Expected result: 10-20% lower CPA than all-purchaser LAL

Tier 3 Seed: All purchasers
├── Everyone who completed a purchase
├── Best for: 3-5% lookalike (maximum scale)
└── Expected result: Baseline performance
```

### Audience Combination Strategy

```
COMBINATION: INTEREST + LOOKALIKE (overlapping)
├── Target: Interest "Fashion" AND 5% LAL from purchasers
├── Effect: Lookalike quality within interest-relevant pool
├── When: LAL alone is underperforming, need interest refinement
└── Risk: May be too narrow if LAL and interest barely overlap

COMBINATION: LOOKALIKE + EXCLUSION (standard retargeting split)
├── Target: 3% LAL from purchasers
├── Exclude: All website visitors (30 days)
├── Effect: True cold prospecting with LAL quality
├── When: Standard approach for prospecting campaigns
└── Risk: Excludes high-intent revisitors (handle in retargeting campaign)

COMBINATION: BROAD + CUSTOM AUDIENCE EXCLUSION (algorithm-driven)
├── Target: Broad (demographics only)
├── Exclude: Everyone who's interacted with brand (all custom audiences)
├── Effect: Pure new user acquisition, fully algorithm-driven
├── When: Mature pixel (100+ conv/week), trust algorithm fully
└── Risk: Algorithm may take 7-10 days to optimize
```

### Frequency-Based Audience Segmentation

```
Create engagement audiences by frequency for differentiated messaging:

LIGHT TOUCH (1-2 impressions):
├── Users who've seen your ad 1-2 times
├── Serve: Intro-level creative, brand story, problem awareness
└── Goal: Build familiarity

WARM (3-5 impressions):
├── Users who've seen your ad 3-5 times but haven't converted
├── Serve: Social proof, testimonials, deeper product info
└── Goal: Build consideration

ENGAGED NON-CONVERTER (6+ impressions):
├── Users who've seen your ad 6+ times without converting
├── Option A: Exclude (they're not interested, stop wasting spend)
├── Option B: Serve completely different creative (new angle)
└── Option C: Strong offer (discount, free trial) as last attempt
```

---

## Quick Reference: Audience Strategy Checklist

1. Assess pixel data maturity (conversions per week determines broad vs narrow)
2. Build custom audiences: purchasers, cart abandoners, visitors, engagers
3. Upload customer file (hashed email + phone, minimum 1,000 records)
4. Create lookalikes at 3 sizes (1%, 3%, 5%) from purchaser seed
5. Set up audience exclusions (purchasers from prospecting, visitors from cold)
6. Run broad vs narrow test (7-10 days, equal budget, same creative)
7. Run lookalike size test (1% vs 3% vs 5%, same creative and budget)
8. Monitor audience fatigue weekly (CPM trends, frequency, CTR decay)
9. Refresh lookalikes every 14-21 days from updated seed
10. Re-upload customer files monthly with new customers
