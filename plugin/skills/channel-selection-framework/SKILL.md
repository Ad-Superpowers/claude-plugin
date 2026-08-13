---
name: channel-selection-framework
description: "This skill should be used when the user asks to \"choose an advertising platform\", \"compare Meta vs Google vs LinkedIn\", \"plan a media mix\", mentions \"which channel should I use\", \"budget allocation across platforms\", or \"best platform for my audience\". Do NOT use for: cross-platform attribution issues (use attribution-reconciler), audience persona creation (use buyer-persona-framework), or market sizing for budget justification (use market-sizing-guide)."
---
# Channel Selection Framework for Advertising

## Purpose

Enable agencies and advertisers to make data-driven decisions about which advertising channels to use for specific campaigns. Move from intuition-based channel selection to systematic, objective-matched decisions.

## When to Use This Skill

Invoke when user mentions:
- **Channel selection:** "Which platform should I use?"
- **Platform comparison:** "Meta vs Google Ads"
- **Media mix:** "How should I split budget across channels?"
- **New campaign planning:** "Starting a new campaign, where should I advertise?"
- **Channel fit:** "Is TikTok right for my audience?"
- **Budget decisions:** "How much do I need for LinkedIn?"
- **Funnel stage:** "Best platform for awareness/conversion?"

---

## Part 1: Channel Selection Decision Tree

### Quick Decision Framework

```
START: What is your PRIMARY objective?
│
├─► AWARENESS (Reach, Brand Recognition)
│   │
│   ├─► Budget > €5,000/month?
│   │   ├─► YES: Meta + TikTok + YouTube
│   │   └─► NO: Meta (best reach per €)
│   │
│   └─► Target Audience?
│       ├─► 18-34: TikTok primary, Meta secondary
│       ├─► 35-54: Meta primary, YouTube secondary
│       └─► 55+: Meta primary, Google Display secondary
│
├─► CONSIDERATION (Engagement, Traffic, Interest)
│   │
│   ├─► B2B or B2C?
│   │   ├─► B2B: LinkedIn + Google Search + Meta
│   │   └─► B2C: Meta + TikTok + Google Display
│   │
│   └─► Content Type?
│       ├─► Video: TikTok, YouTube, Meta
│       ├─► Written: LinkedIn, Google
│       └─► Visual: Meta, Pinterest
│
├─► CONVERSION (Sales, Leads, Signups)
│   │
│   ├─► Product Type?
│   │   ├─► E-commerce: Google Shopping + Meta + TikTok Shop
│   │   ├─► SaaS/B2B: Google Search + LinkedIn + Meta
│   │   ├─► Local Service: Google Local + Meta
│   │   └─► App: Meta App + TikTok + Google App
│   │
│   └─► Sales Cycle?
│       ├─► Impulse (<24h): Google Search + Meta retargeting
│       ├─► Short (1-7 days): Meta + Google
│       ├─► Medium (7-30 days): Full multi-touch
│       └─► Long (30+ days): LinkedIn + Content + Retargeting
│
└─► FULL FUNNEL (Brand + Performance)
    │
    └─► Budget Level?
        ├─► <€5k/mo: Pick ONE platform, full funnel within it
        ├─► €5-15k/mo: 2 platforms, complementary roles
        ├─► €15-50k/mo: 3 platforms, defined roles per funnel stage
        └─► €50k+/mo: 4+ platforms, sophisticated attribution
```

---

## Part 2: Platform Strengths & Weaknesses Matrix

### Comprehensive Platform Comparison

| Dimension | Meta (FB/IG) | Google Search | Google Display | LinkedIn | TikTok | YouTube |
|-----------|-------------|---------------|----------------|----------|--------|---------|
| **Awareness** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Consideration** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Conversion** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **B2B Targeting** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **B2C Targeting** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Reach Efficiency** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Cost Efficiency** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Targeting Precision** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Creative Flexibility** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Attribution Clarity** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Ease of Management** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Learning Curve** | Medium | High | Medium | Medium | Low | Medium |

### Platform Strengths Summary

**Meta (Facebook/Instagram):**
- ✅ Largest addressable audience
- ✅ Best lookalike audiences
- ✅ Strong visual/video formats
- ✅ Excellent retargeting
- ❌ Privacy changes impacting targeting
- ❌ Creative fatigue (10-14 day cycle)
- 💰 Minimum viable: €1,000/month

**Google Search:**
- ✅ Highest purchase intent
- ✅ Best attribution clarity
- ✅ Keyword-level control
- ✅ Works for all industries
- ❌ Limited creative options
- ❌ Can be expensive in competitive verticals
- 💰 Minimum viable: €500/month

**LinkedIn:**
- ✅ Best B2B targeting (job title, company, industry)
- ✅ Professional context
- ✅ Lead Gen Forms (high conversion)
- ❌ Highest CPCs/CPMs
- ❌ Smaller audiences
- ❌ Limited to professional content
- 💰 Minimum viable: €2,000/month

**TikTok:**
- ✅ Lowest CPMs, great reach
- ✅ Viral potential
- ✅ Strong Gen Z/Millennial reach
- ✅ TikTok Shop integration
- ❌ Fastest creative fatigue (4-7 days)
- ❌ Requires native content style
- ❌ Less suited for B2B/older demos
- 💰 Minimum viable: €1,000/month

**YouTube:**
- ✅ Video storytelling
- ✅ Brand safety controls
- ✅ Connected TV reach
- ✅ Google ecosystem integration
- ❌ Requires video production
- ❌ Higher production costs
- 💰 Minimum viable: €1,500/month

---

## Part 3: Audience Fit Analysis by Platform

### Demographic Fit Matrix

| Age Group | Meta | Google | LinkedIn | TikTok | YouTube |
|-----------|------|--------|----------|--------|---------|
| 13-17 | ⭐⭐ | ⭐⭐ | ❌ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 18-24 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 25-34 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 35-44 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 45-54 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| 55-64 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐⭐⭐ |
| 65+ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ❌ | ⭐⭐⭐ |

### Audience Type Recommendations

| Audience Type | Primary Channel | Secondary | Avoid |
|---------------|-----------------|-----------|-------|
| **Gen Z consumers** | TikTok | Meta (IG) | LinkedIn |
| **Millennials** | Meta | TikTok, YouTube | - |
| **Gen X** | Meta | Google, LinkedIn | TikTok |
| **Baby Boomers** | Google | Meta | TikTok |
| **B2B Decision Makers** | LinkedIn | Google Search | TikTok |
| **C-Suite** | LinkedIn | Google | TikTok |
| **Small Business Owners** | Meta | Google | - |
| **Tech Professionals** | LinkedIn | Google | - |
| **Healthcare** | Google | LinkedIn | TikTok |
| **Finance** | LinkedIn | Google | TikTok |
| **E-commerce shoppers** | Meta | Google Shopping | LinkedIn |
| **App users** | TikTok | Meta | LinkedIn |
| **Local customers** | Google Local | Meta | LinkedIn |

### Industry-Specific Channel Recommendations

| Industry | Primary | Secondary | Notes |
|----------|---------|-----------|-------|
| **E-commerce/DTC** | Meta, Google Shopping | TikTok | Visual products thrive on Meta/TikTok |
| **SaaS B2B** | LinkedIn, Google Search | Meta retargeting | Long sales cycle, professional targeting |
| **SaaS B2C** | Meta, Google | TikTok | Consumer-focused, broad reach |
| **Professional Services** | LinkedIn, Google | Meta | Trust and credibility important |
| **Healthcare** | Google Search | Meta, LinkedIn | High intent searches, regulations |
| **Finance/Insurance** | Google, LinkedIn | Meta | Compliance considerations |
| **Education** | Meta, Google | TikTok | Depends on age of students |
| **Travel** | Meta, Google | TikTok, YouTube | Visual inspiration + booking intent |
| **Real Estate** | Meta, Google | LinkedIn (commercial) | Local targeting important |
| **Automotive** | YouTube, Meta | Google | Video for consideration |
| **Food & Beverage** | TikTok, Meta | Google Local | UGC and visual content |
| **Fashion** | Meta, TikTok | Google Shopping | Visual-first platforms |
| **Gaming** | TikTok, YouTube | Meta | Engagement and video |
| **Non-profit** | Meta, Google | LinkedIn | Lower costs, mission-driven |

---

## Part 4: Budget Thresholds by Channel

### Minimum Viable Budgets

| Channel | Absolute Minimum | Recommended Minimum | Sweet Spot |
|---------|-----------------|---------------------|------------|
| **Meta** | €500/month | €1,500/month | €5,000-15,000/month |
| **Google Search** | €300/month | €1,000/month | €3,000-10,000/month |
| **Google Shopping** | €500/month | €1,500/month | €5,000-15,000/month |
| **LinkedIn** | €1,000/month | €3,000/month | €10,000-30,000/month |
| **TikTok** | €500/month | €1,500/month | €5,000-15,000/month |
| **YouTube** | €1,000/month | €2,500/month | €7,500-20,000/month |

### Budget-to-Channel Mapping

| Monthly Budget | Recommended Channels | Channel Count |
|----------------|---------------------|---------------|
| €0 - €1,000 | Meta OR Google Search | 1 |
| €1,000 - €3,000 | Meta + Google Search | 2 |
| €3,000 - €5,000 | Meta + Google + 1 other | 2-3 |
| €5,000 - €10,000 | Meta + Google + TikTok or LinkedIn | 3 |
| €10,000 - €25,000 | 3-4 channels with clear roles | 3-4 |
| €25,000 - €50,000 | Full multi-channel | 4-5 |
| €50,000+ | All relevant channels | 4-6 |

### Cost Efficiency Ranking (2025-2026)

**By CPM (Lowest to Highest):**
1. TikTok (€3-8)
2. Meta Display (€5-12)
3. Meta Feed (€8-15)
4. Google Display (€5-15)
5. YouTube (€10-20)
6. Google Search (N/A - CPC based)
7. LinkedIn (€25-60)

**By CPC (Lowest to Highest):**
1. TikTok (€0.20-0.80)
2. Meta (€0.40-1.50)
3. Google Display (€0.30-1.00)
4. Google Search (€0.80-5.00+)
5. YouTube (€0.10-0.30 per view)
6. LinkedIn (€2.00-8.00)

---

## Part 5: Funnel Stage Channel Selection

### Awareness Stage (TOFU)

**Goal:** Maximize reach and brand recognition

| Priority | Channel | Role | KPIs |
|----------|---------|------|------|
| 1 | Meta (Reach campaigns) | Broad awareness | Reach, CPM, Frequency |
| 2 | TikTok | Viral potential | Views, CPM, Shares |
| 3 | YouTube | Video storytelling | Views, VTR, CPV |
| 4 | Google Display | Broad visibility | Impressions, Reach |

**Budget Split:** 60-70% of awareness budget

### Consideration Stage (MOFU)

**Goal:** Drive engagement and intent signals

| Priority | Channel | Role | KPIs |
|----------|---------|------|------|
| 1 | Meta (Traffic/Engagement) | Content engagement | CTR, Time on Site |
| 2 | Google Search (Generic) | Research queries | CTR, Bounce Rate |
| 3 | LinkedIn (Content) | B2B engagement | Engagement Rate |
| 4 | YouTube | Product consideration | View Rate, Subscribers |

**Budget Split:** 20-30% of total budget

### Conversion Stage (BOFU)

**Goal:** Drive purchases, leads, signups

| Priority | Channel | Role | KPIs |
|----------|---------|------|------|
| 1 | Google Search (Intent) | High intent capture | CPA, ROAS, CVR |
| 2 | Meta (Retargeting) | Re-engage visitors | CPA, ROAS |
| 3 | Google Shopping | Product purchase | ROAS, CPA |
| 4 | LinkedIn Lead Gen | B2B leads | CPL, Lead Quality |

**Budget Split:** 40-50% of performance budget

### Full-Funnel Budget Template

| Funnel Stage | Budget % | Primary Channel | Secondary |
|--------------|----------|-----------------|-----------|
| Awareness | 30% | Meta/TikTok | YouTube |
| Consideration | 20% | Meta/Google Display | LinkedIn |
| Conversion | 50% | Google Search | Meta Retargeting |

---

## Part 6: Channel Selection Checklist

### Pre-Selection Questions

**Business Context:**
- [ ] What is the primary campaign objective?
- [ ] What is the available monthly budget?
- [ ] What is the product/service type (B2B/B2C/E-commerce)?
- [ ] What is the typical sales cycle length?
- [ ] What geography are we targeting?

**Audience Context:**
- [ ] What is the target age range?
- [ ] What platforms does the audience use?
- [ ] Are we targeting professionals or consumers?
- [ ] Do we have existing customer data for lookalikes?
- [ ] What content format resonates with this audience?

**Resource Context:**
- [ ] Do we have video production capability?
- [ ] How often can we refresh creative?
- [ ] What tracking/pixels are already set up?
- [ ] What is the team's platform expertise?

### Channel Selection Scorecard

Score each channel 1-5 for your specific situation:

| Factor | Meta | Google | LinkedIn | TikTok | Weight |
|--------|------|--------|----------|--------|--------|
| Audience fit | /5 | /5 | /5 | /5 | 25% |
| Objective match | /5 | /5 | /5 | /5 | 25% |
| Budget viability | /5 | /5 | /5 | /5 | 20% |
| Creative capability | /5 | /5 | /5 | /5 | 15% |
| Team expertise | /5 | /5 | /5 | /5 | 15% |
| **Weighted Score** | | | | | 100% |

**Interpretation:**
- 4.0+: Primary channel candidate
- 3.0-3.9: Secondary channel candidate
- 2.0-2.9: Test only if budget allows
- <2.0: Not recommended

---

## Part 7: Common Channel Combinations

### Proven Multi-Channel Strategies

**E-commerce Starter (€3-5k/month):**
- Meta (60%): Prospecting + Retargeting
- Google Shopping (40%): Product capture

**B2B Lead Gen (€5-10k/month):**
- LinkedIn (40%): Professional targeting
- Google Search (35%): Intent capture
- Meta Retargeting (25%): Re-engage visitors

**D2C Brand Building (€10-20k/month):**
- TikTok (35%): Awareness + UGC
- Meta (35%): Full-funnel
- Google (30%): Intent capture

**Local Business (€2-5k/month):**
- Google Local/Search (60%): High intent
- Meta (40%): Local awareness

**App Install (€10k+/month):**
- TikTok (40%): Cost-efficient installs
- Meta (35%): Lookalikes
- Google App (25%): Intent

**Enterprise B2B (€25k+/month):**
- LinkedIn (35%): Account-based
- Google Search (30%): Intent
- Meta (20%): Retargeting + Brand
- YouTube (15%): Thought leadership

---

## Part 8: Quick Reference Tables

### When to Use Each Platform

| Scenario | Best Platform | Why |
|----------|---------------|-----|
| New product launch | TikTok + Meta | Broad reach, visual showcase |
| B2B lead generation | LinkedIn + Google | Professional targeting + intent |
| E-commerce sales | Google Shopping + Meta | Purchase intent + retargeting |
| App downloads | TikTok + Meta | Cost-efficient installs |
| Local business | Google Local + Meta | Local intent + geo-targeting |
| Brand awareness | TikTok + YouTube | Video reach, viral potential |
| Retargeting | Meta + Google Display | Best retargeting capabilities |
| High-ticket B2B | LinkedIn | Professional context, lead quality |
| Quick sale B2C | Google Search | Immediate intent |

### Red Flags: When NOT to Use a Platform

| Platform | Don't Use When |
|----------|----------------|
| **TikTok** | B2B enterprise, 55+ audience, small budget (<€1k) |
| **LinkedIn** | B2C products, budget <€2k, impulse purchases |
| **Meta** | Very niche B2B, no creative resources |
| **Google Search** | No search volume for product category |
| **YouTube** | No video capability, <€1.5k budget |

---

## Optional: Enrich with Live Data

If the user has connected accounts, validate channel selection with actual traffic and search volume data:

```python
# See how existing traffic splits across channels — which are already performing?
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="30daysAgo",
    end_date="today",
    metrics=["sessions", "keyEvents", "totalUsers"],
    dimensions=["sessionDefaultChannelGroup"]
)
```

```python
# Check search impression volume for core keywords to confirm Google Search viability
google_ads_run_gaql(
    customer_id="YOUR_CUSTOMER_ID",
    query="SELECT search_term_view.search_term, metrics.impressions FROM search_term_view WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.impressions DESC LIMIT 25"
)
```

Use GA4 channel data to identify where you already have traction, and GAQL to verify that search demand actually exists before recommending Google Search as a channel.

*Last updated: February 2026*
*Framework based on industry best practices and Ad Superpowers platform data*
