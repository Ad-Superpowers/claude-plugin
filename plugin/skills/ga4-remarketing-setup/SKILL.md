---
name: ga4-remarketing-setup
description: "This skill should be used when the user asks to \"export GA4 audiences to Google Ads\", \"set up RLSA\", \"configure remarketing lists\", or mentions \"audience sync issues\", \"Display remarketing\", or \"YouTube remarketing\". Do NOT use for: audience creation in GA4 (use ga4-audience-builder), predictive audiences (use ga4-predictive-audiences), audience exclusion strategy (use ga4-audience-exclusions)."
---
# GA4 Remarketing Setup Guide

Complete guide for exporting and activating GA4 audiences in Google Ads for effective remarketing campaigns.

## Step 1: Verify Google Ads Link

```
GOOGLE ADS LINK VERIFICATION
==============================

LOCATION: Admin → Product Links → Google Ads Links

REQUIREMENTS FOR REMARKETING:
┌─────────────────────────────┬────────────────────────────────────────────┐
│ Setting                     │ Required Status                            │
├─────────────────────────────┼────────────────────────────────────────────┤
│ Google Ads account linked   │ Active                                     │
│                             │ (All accounts that need audiences)         │
├─────────────────────────────┼────────────────────────────────────────────┤
│ Enable personalized         │ ON                                         │
│ advertising                 │ (CRITICAL for audience export!)            │
├─────────────────────────────┼────────────────────────────────────────────┤
│ Auto-tagging                │ Enabled in Google Ads                      │
│                             │ (For correct attribution)                  │
└─────────────────────────────┴────────────────────────────────────────────┘

CREATING THE LINK (if not existing):
─────────────────────────────────────
1. GA4: Admin → Product Links → Google Ads Links
2. Click "Link"
3. Select Google Ads account(s)
4. Enable "Enable personalized advertising"
5. Click "Submit"
6. Wait 24-48 hours for sync

VERIFICATION IN GOOGLE ADS:
────────────────────────────
1. Google Ads → Tools & Settings → Linked accounts
2. Find Google Analytics (GA4) section
3. Verify: Link status = "Active"
4. Check: "Import site metrics" = ON
```

## Step 2: Configure Google Signals

```
GOOGLE SIGNALS FOR REMARKETING
===============================

WHY IT MATTERS:
├── Cross-device remarketing (user on mobile → desktop)
├── Demographic targeting in Google Ads
├── Increased match rates with Google users
└── Required for some predictive audiences

LOCATION: Admin → Data Settings → Data Collection

SETUP:
┌────┬────────────────────────────────────────────────────────────────────┐
│ 1  │ Go to Admin → Data Settings → Data Collection                     │
├────┼────────────────────────────────────────────────────────────────────┤
│ 2  │ Click "Get started" next to Google signals                        │
├────┼────────────────────────────────────────────────────────────────────┤
│ 3  │ Accept data collection terms                                      │
├────┼────────────────────────────────────────────────────────────────────┤
│ 4  │ Enable for all regions (or select specific ones)                  │
├────┼────────────────────────────────────────────────────────────────────┤
│ 5  │ Toggle: "Enable Google signals data collection" = ON              │
└────┴────────────────────────────────────────────────────────────────────┘

GDPR CONSIDERATIONS:
├── Requires cookie consent for personalization
├── Consent Mode v2 required for EEA since March 2024
│   └─► Must send analytics_storage AND ad_storage signals
│   └─► Without v2: audience match rates significantly lower in EEA
├── Not all users will be matched (opt-in required)
└── May activate data thresholding in reports
```

## Step 3: Configure Audiences for Export

```
AUDIENCE EXPORT CONFIGURATION
==============================

WHEN CREATING AN AUDIENCE:
──────────────────────────
When you create an audience in GA4:
├── Scroll to "Audience destinations"
├── Select: Google Ads
├── Select: All linked accounts that need the audience
└── Save audience

EXPORTING EXISTING AUDIENCES:
─────────────────────────────
1. Go to Admin → Audiences
2. Click on audience name
3. Edit → Scroll to "Audience destinations"
4. Select Google Ads accounts
5. Save

WHICH AUDIENCES TO EXPORT:
┌─────────────────────────┬────────────┬─────────────────────────────────┐
│ Audience                │ Priority   │ Use Case                        │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ All Users               │ ***        │ Baseline for exclusions         │
│                         │            │ Display prospecting             │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Purchasers (all time)   │ ***        │ Cross-sell, lookalikes          │
│                         │            │ RLSA bid adjustments            │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Recent purchasers       │ ***        │ Exclusion from acquisition      │
│ (30 days)               │            │ Cross-sell timing               │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Cart abandoners         │ ***        │ Recovery campaigns              │
│                         │            │ High intent retargeting         │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Product viewers         │ **         │ Consideration retargeting       │
│                         │            │ Category-specific ads           │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Engaged visitors        │ **         │ Awareness retargeting           │
│ (high session duration) │            │ Brand building                  │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Likely purchasers       │ ***        │ Smart Bidding optimization      │
│ (predictive)            │            │ High priority targeting         │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Likely churners         │ **         │ Retention campaigns             │
│ (predictive)            │            │ Win-back messaging              │
└─────────────────────────┴────────────┴─────────────────────────────────┘
```

## Remarketing Types in Google Ads

### RLSA (Remarketing Lists for Search Ads)

```
RLSA SETUP
==========

WHAT IT IS:
├── Adjust bids for GA4 audiences on Search
├── Target specific keywords only for audiences
├── Combine audience signals with search intent
└── No separate ads needed (same ads, different bids)

MINIMUM SIZE: 1,000 users

SETUP IN GOOGLE ADS:
────────────────────
1. Go to Campaign → Audiences
2. Click "+ Add audience segments"
3. Browse → "Your data" → "Website visitors" (GA4)
4. Select GA4 audiences
5. Choose: "Targeting" or "Observation"

TARGETING VS OBSERVATION:
┌───────────────────┬────────────────────────────────────────────────────┐
│ Mode              │ Meaning                                            │
├───────────────────┼────────────────────────────────────────────────────┤
│ Observation       │ Audience sees the same ads, with bid adjustment    │
│                   │ └─► Start with this! Measure performance first     │
├───────────────────┼────────────────────────────────────────────────────┤
│ Targeting         │ ONLY the audience sees ads on these keywords       │
│                   │ └─► For specific remarketing keywords              │
└───────────────────┴────────────────────────────────────────────────────┘

RLSA BID ADJUSTMENT STRATEGY:
──────────────────────────────
┌─────────────────────────┬─────────────┬─────────────────────────────────┐
│ Audience                │ Bid Adj.    │ Rationale                       │
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ All converters          │ +20% to +50%│ Proven buyers                   │
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ Cart abandoners         │ +30% to +60%│ High intent, nearly converted   │
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ Product viewers         │ +10% to +25%│ Interested, not ready yet       │
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ Likely purchasers       │ +40% to +80%│ ML predicts high probability    │
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ Bounced visitors        │ -20% to -40%│ Low engagement, lower value     │
└─────────────────────────┴─────────────┴─────────────────────────────────┘

Note: Smart Bidding adjusts automatically. Use audience insights
for strategy, not manual bid adjustments with Smart Bidding.
```

### Display Remarketing

```
DISPLAY REMARKETING SETUP
=========================

WHAT IT IS:
├── Banner/image ads on Google Display Network
├── Reach users across millions of websites
├── Visual remarketing for brand recall
└── Lower CPC than Search, higher reach

MINIMUM SIZE: 100 users

CAMPAIGN SETUP:
───────────────
1. Google Ads → + New Campaign
2. Goal: Sales/Leads/Website traffic
3. Campaign type: Display
4. Audiences: Add GA4 audiences
5. Creatives: Responsive display ads

BEST PRACTICES:
┌────────────────────────────────────────────────────────────────────────┐
│ DO: Set frequency capping (3-5 impressions/day)                       │
│ DO: Add exclusions (recent purchasers)                                │
│ DO: Separate campaigns per audience tier                              │
│ DO: Dynamic remarketing if e-commerce                                 │
│ DO: Brand-safe placements (exclude sensitive content)                 │
│ DON'T: Put all audiences in one campaign                              │
│ DON'T: Unlimited frequency (ad fatigue!)                              │
└────────────────────────────────────────────────────────────────────────┘

DISPLAY AUDIENCE TIERS:
───────────────────────
Tier 1 (Highest intent): Cart abandoners, checkout abandoners
├── Frequency: 5-7/day
├── Budget: Highest share
└── Creative: Product-focused, urgency

Tier 2 (Medium intent): Product viewers, engaged visitors
├── Frequency: 3-5/day
├── Budget: Medium share
└── Creative: Benefits, social proof

Tier 3 (Lower intent): All visitors
├── Frequency: 2-3/day
├── Budget: Lowest share
└── Creative: Brand awareness, value prop
```

### YouTube Remarketing

```
YOUTUBE REMARKETING SETUP
=========================

WHAT IT IS:
├── Video ads for GA4 website audiences
├── In-stream, discovery, bumper ads
├── Combine video impact with remarketing precision
└── Great option for brand consideration

MINIMUM SIZE: 1,000 users

CAMPAIGN SETUP:
───────────────
1. Google Ads → + New Campaign
2. Goal: Brand awareness/Product consideration
3. Campaign type: Video
4. Audiences: Add GA4 audiences
5. Ad formats: Choose based on goal

YOUTUBE AD FORMATS:
┌───────────────────┬─────────────┬────────────────────────────────────────┐
│ Format            │ Skippable   │ Best For                               │
├───────────────────┼─────────────┼────────────────────────────────────────┤
│ In-stream         │ After 5s    │ Story-telling, longer messages         │
│ (skippable)       │             │ Pay per view (30s or completion)       │
├───────────────────┼─────────────┼────────────────────────────────────────┤
│ In-stream         │ No          │ Short, punchy messages (15s max)       │
│ (non-skippable)   │             │ Brand recall, reach                    │
├───────────────────┼─────────────┼────────────────────────────────────────┤
│ Bumper            │ No (6s)     │ Quick reminder, frequency reach        │
│                   │             │ Awareness only                         │
├───────────────────┼─────────────┼────────────────────────────────────────┤
│ Discovery         │ N/A         │ YouTube search/homepage                │
│                   │             │ High-intent video seekers              │
└───────────────────┴─────────────┴────────────────────────────────────────┘

YOUTUBE REMARKETING STRATEGY:
──────────────────────────────
Cart abandoners → Short reminder video (15-30s)
├── Focus: Product reminder, incentive
└── CTA: Return to cart

Product viewers → Longer story video (30-60s)
├── Focus: Benefits, testimonials
└── CTA: Learn more

All visitors → Brand video (15-30s)
├── Focus: Brand values, unique selling points
└── CTA: Visit website
```

### Performance Max Remarketing

```
PERFORMANCE MAX AUDIENCE SIGNALS
================================

WHAT IT IS:
├── Cross-channel automation (Search, Display, YouTube, etc.)
├── GA4 audiences as "audience signals"
├── Google's ML optimizes targeting
└── Signals provide hints, not hard targeting

HOW IT WORKS:
──────────────
1. Add GA4 audiences as "audience signals"
2. Google uses this as a starting signal
3. ML expands to similar users
4. Audience is a hint, not a restriction

SETUP:
──────
1. Performance Max campaign → Asset Groups
2. Scroll to "Audience signals"
3. Add: Your data → GA4 audiences
4. Add: Custom segments (optional)
5. Add: Demographics, interests

BEST PRACTICES:
┌────────────────────────────────────────────────────────────────────────┐
│ DO: Add multiple GA4 audiences (layered signals)                      │
│ DO: Combine with customer match lists                                 │
│ DO: Review "Audience insights" tab for learnings                      │
│ DO: Separate asset groups for acquisition vs retention                │
│ DON'T: Expect only the GA4 audience to be targeted                    │
│ DON'T: Provide too few audiences as signals                           │
└────────────────────────────────────────────────────────────────────────┘

AUDIENCE SIGNAL STRATEGY:
──────────────────────────
High-value signals (add first):
├── All converters (GA4)
├── High-value customers (GA4)
├── Customer match: email lists
└── Likely purchasers (predictive)

Supporting signals:
├── Product/category viewers
├── Engaged visitors
├── Cart abandoners
└── Website visitors (all)
```

## Audience Size & Match Rates

```
AUDIENCE SIZE REQUIREMENTS
==========================

MINIMUM SIZES PER NETWORK:
┌─────────────────────────┬──────────────┬─────────────────────────────────┐
│ Network                 │ Minimum      │ Recommended                     │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Display Network         │ 100          │ 1,000+ for consistent reach     │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Search (RLSA)           │ 1,000        │ 5,000+ for significant impact   │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ YouTube                 │ 1,000        │ 5,000+ for better targeting     │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Discovery               │ 1,000        │ 10,000+ for scale               │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Gmail                   │ 1,000        │ 5,000+ for deliverability       │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Similar/Lookalike       │ 1,000+       │ 5,000+ for ML optimization      │
└─────────────────────────┴──────────────┴─────────────────────────────────┘

MATCH RATE FACTORS:
────────────────────
GA4 audience size ≠ Google Ads audience size

Typical match rates: 30-70%

Factors that affect match rate:
├── Google Signals enabled (higher = better match)
├── Cross-device tracking (more touchpoints = better match)
├── Consent mode (more consents = higher match)
├── User login status (logged in = higher match)
└── Region (EU/GDPR = lower match)

IMPROVING MATCH RATE:
──────────────────────
├── Enable Google Signals
├── Implement consent mode correctly
├── Encourage user login
├── Use customer match supplemental lists
└── Extend membership duration (more users accumulate)
```

## Best Practices

```
DO's
════
├── Start with "Observation" mode, not "Targeting"
│   └─► Collect data first before restricting
│
├── Layer audiences with exclusions
│   └─► Target cart abandoners EXCLUDE converters
│
├── Match creative to audience intent
│   └─► Cart abandoners → "Forgot something?" messaging
│
├── Set frequency caps
│   └─► Prevent ad fatigue and annoyance
│
├── Segment audiences into tiers
│   └─► High/medium/low intent with different bids
│
├── Monitor list sizes daily
│   └─► Catch tracking issues early
│
└── Combine with customer match
    └─► Email lists + GA4 = better coverage

DON'Ts
══════
├── Export ALL audiences to Google Ads
│   └─► Focus on actionable audiences
│
├── Forget to exclude recent converters
│   └─► Annoying and waste of budget
│
├── Use identical messaging for all audiences
│   └─► Cart abandoners ≠ new visitors
│
├── Use too short membership durations
│   └─► Audiences too small for effectiveness
│
├── Skip frequency capping
│   └─► Creepy and negative brand impact
│
└── Trust GA4 size = Google Ads size
    └─► Match rates cause differences
```

## Output: Remarketing Setup Recommendation Template

```markdown
# GA4 Remarketing Setup Report

## Account Link Status
| Setting | Status | Account ID |
|---------|--------|------------|
| Google Ads Link | [Y/N] | [XXX-XXX-XXXX] |
| Personalized Ads | [Y/N] | - |
| Google Signals | [Y/N] | - |
| Auto-tagging | [Y/N] | - |

## Audiences for Export

### Priority 1: Core Remarketing
| Audience | GA4 Size | Est. Ads Size | Export Status |
|----------|----------|---------------|---------------|
| All Converters | [X] | [X] | [Y/N] |
| Cart Abandoners | [X] | [X] | [Y/N] |
| Product Viewers | [X] | [X] | [Y/N] |

### Priority 2: Advanced Segments
| Audience | GA4 Size | Est. Ads Size | Export Status |
|----------|----------|---------------|---------------|
| Likely Purchasers | [X] | [X] | [Y/N] |
| High-Value Customers | [X] | [X] | [Y/N] |
| [Custom Audience] | [X] | [X] | [Y/N] |

## Campaign Recommendations

### RLSA (Search)
| Audience | Bid Adjustment | Rationale |
|----------|---------------|-----------|
| [Audience 1] | +[X]% | [Reason] |
| [Audience 2] | +[X]% | [Reason] |

### Display Remarketing
| Tier | Audience | Frequency Cap | Budget % |
|------|----------|---------------|----------|
| 1 (High intent) | [Audience] | [X]/day | [X]% |
| 2 (Medium) | [Audience] | [X]/day | [X]% |
| 3 (Low) | [Audience] | [X]/day | [X]% |

### YouTube (Optional)
| Audience | Ad Format | Length | Focus |
|----------|-----------|--------|-------|
| [Audience] | [Format] | [Xs] | [Message focus] |

## Exclusions Setup
| From Campaign | Exclude Audience | Reason |
|---------------|------------------|--------|
| [Campaign] | Recent Purchasers | Prevent waste |
| [Campaign] | [Audience] | [Reason] |

## Monitoring Checklist
- [ ] Weekly audience size check
- [ ] Match rate monitoring
- [ ] Performance per audience tier
- [ ] Frequency cap effectiveness
- [ ] Creative fatigue signals

## Action Items
1. [ ] [First action]
2. [ ] [Second action]
3. [ ] [Third action]

## Notes
[Specific recommendations or context]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, check remarketing pool sizes before setting up ad platform audiences:

```python
# Estimate funnel stage volumes for remarketing tiers
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["totalUsers"],
    dimensions=["sessionDefaultChannelGroup"],
    start_date="30daysAgo",
    end_date="today"
)
```

This helps size each remarketing tier (cart abandoners, product viewers, site visitors) and decide lookback windows. If 30-day pools are too small (<1k), extend to 60 or 90 days.
