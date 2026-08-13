---
name: client-onboarding-checklist
description: "This skill should be used when the user asks to \"onboard a new advertising client\", \"audit an ad account before takeover\", \"build a client kickoff checklist\", \"structure a 30/60/90 day plan\", or mentions \"agency onboarding\" or \"account takeover\". Do NOT use for: specific platform campaign builds (use platform-specific skills), billing/contract setup (outside scope), or creative production workflows (use creative-fatigue-analyzer)."
---

# Agency Client Onboarding Checklist

## Purpose

Provide a structured, repeatable onboarding workflow for agencies taking on new advertising clients. A thorough onboarding prevents the most common causes of client churn: misaligned expectations, missed tracking issues, and slow time-to-results.

## When to Use This Skill

Invoke when user mentions:
- **New client:** "I'm onboarding a new client"
- **Account takeover:** "Taking over an ad account from another agency"
- **Onboarding process:** "What should I check when starting with a new client?"
- **Audit:** "Need to audit a client's ad accounts"
- **Kickoff:** "What should I cover in a kickoff meeting?"
- **Reporting:** "How should I structure client reports?"
- **30/60/90 plan:** "What does the first 90 days look like?"
- **Transition:** "Client is moving from in-house to our agency"

---

## Phase 1: Discovery (Days 1-5)

### Objective
Understand the business, goals, audience, and competitive landscape deeply enough to build a strategy. Do NOT touch the ad accounts yet.

### Discovery Meeting Agenda (90 minutes)

| Time | Topic | Questions to Ask |
|------|-------|-----------------|
| 0-15 min | Business overview | Revenue, margins, growth targets, product/service mix |
| 15-30 min | Target audience | Who buys? Demographics, psychographics, buying triggers |
| 30-45 min | Current marketing | What's working? What's been tried? What failed? |
| 45-60 min | Competitive landscape | Who are the top 3 competitors? How do they differentiate? |
| 60-75 min | Goals & KPIs | Revenue target, ROAS target, CPA target, timeline |
| 75-90 min | Access & logistics | Account access, brand guidelines, approval process, reporting cadence |

### Discovery Checklist

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Business model documented (B2C/B2B/D2C, margins, AOV) | ☐ | |
| 2 | Revenue targets and timeline confirmed | ☐ | Monthly/quarterly goals |
| 3 | Target audience personas (2-3 max) defined | ☐ | Age, location, interests, pain points |
| 4 | Competitive landscape mapped (top 3-5 competitors) | ☐ | Spend estimates, positioning |
| 5 | Current ad spend by platform documented | ☐ | |
| 6 | Historical performance baseline captured | ☐ | Last 90 days minimum |
| 7 | Seasonal patterns identified | ☐ | Peak periods, slow periods |
| 8 | Brand guidelines received | ☐ | Logo, colors, tone of voice, dos/don'ts |
| 9 | Existing creative assets inventoried | ☐ | Images, videos, copy bank |
| 10 | Approval workflow agreed upon | ☐ | Who approves ads? Turnaround time? |
| 11 | Reporting cadence agreed | ☐ | Weekly email, monthly call, quarterly review |
| 12 | Success metrics and KPIs agreed in writing | ☐ | Signed off by both sides |

### Access Requests

| Platform/Tool | Access Type | Who Provides | Priority |
|--------------|------------|-------------|----------|
| Meta Business Manager | Admin or Advertiser | Client | Day 1 |
| Google Ads | Standard or Admin | Client | Day 1 |
| Google Analytics 4 | Editor or Admin | Client | Day 1 |
| Google Search Console | Full user | Client | Day 1 |
| Google Tag Manager | Publish access | Client | Day 1 |
| TikTok Ads | Advertiser | Client | Day 1 |
| LinkedIn Campaign Manager | Account Manager | Client | Day 1 |
| Ad Superpowers | Connect accounts | Agency | Day 1-2 |
| Shopify / E-commerce | Analytics access | Client | Day 2 |
| CRM (HubSpot, Salesforce) | Reporting access | Client | Day 2-3 |
| Email platform (Klaviyo, etc.) | View access | Client | Day 3 |

---

## Phase 2: Audit (Days 3-8)

### Objective
Assess the current state of tracking, account structure, creative, and performance. Identify quick wins and critical issues.

### Tracking Audit Checklist

Use `gtm_audit` to get a comprehensive GTM container audit, then verify:

| # | Check | Tool | Status | Severity if Missing |
|---|-------|------|--------|-------------------|
| 1 | Google Analytics 4 properly installed | `gtm_audit` | ☐ | Critical |
| 2 | GA4 key events configured (purchase, lead, etc.) | `ga4_run_report` | ☐ | Critical |
| 3 | Meta Pixel firing on all pages | `gtm_audit` | ☐ | Critical |
| 4 | Meta Conversions API (CAPI) active | Meta Events Manager | ☐ | Critical (mandatory for signal quality) |
| 5 | Google Ads conversion tracking active | `google_ads_run_gaql` | ☐ | Critical |
| 6 | Enhanced conversions enabled (Google) | Google Ads UI | ☐ | High |
| 7 | TikTok Pixel installed (if using TikTok) | `gtm_audit` | ☐ | Critical for TikTok |
| 8 | LinkedIn Insight Tag installed (if using LinkedIn) | `gtm_audit` | ☐ | Critical for LinkedIn |
| 9 | UTM tagging consistent across platforms | `ga4_run_report` (source/medium) | ☐ | High |
| 10 | Cross-domain tracking configured (if needed) | GA4 settings | ☐ | Medium |
| 11 | E-commerce data layer complete | GTM preview mode | ☐ | High for e-commerce |
| 12 | No duplicate tags or conflicting pixels | `gtm_audit` | ☐ | Medium |
| 13 | Cookie consent implemented (GDPR) | Site inspection | ☐ | Legal requirement |
| 14 | Server-side tracking evaluated | GTM Server container | ☐ | Medium |

### Account Structure Audit

**Meta Ads — Use `meta_get_insights` at campaign, adset, and ad levels:**

| Check | What to Look For | Red Flag |
|-------|-----------------|----------|
| Campaign count | How many active campaigns? | > 10 campaigns (fragmentation) |
| Ad set count per campaign | How many ad sets? | > 5 per campaign (audience splitting) |
| Audience overlap | Are ad sets competing? | Same audience in multiple ad sets |
| Budget distribution | Where is spend concentrated? | > 80% in one campaign |
| Learning phase | Are ad sets exiting learning? | Majority stuck in learning |
| Creative volume | How many active ads? | < 3 per ad set (insufficient testing) |
| Naming convention | Is there a system? | Random names = no system |

**Google Ads — Use `google_ads_run_gaql`:**

```sql
-- Account structure overview
SELECT
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign.bidding_strategy_type,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.cost_micros
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
```

| Check | What to Look For | Red Flag |
|-------|-----------------|----------|
| Campaign types | Search, Shopping, PMax, Display, Video | Missing Search or Shopping for e-commerce |
| Keyword match types | Broad, Phrase, Exact mix | All broad match with no negatives |
| Negative keywords | Negative keyword lists | None or minimal negatives |
| Quality scores | Average quality score | < 5/10 on high-spend keywords |
| Search terms | Irrelevant queries | > 20% spend on irrelevant terms |
| Ad extensions | Sitelinks, callouts, structured snippets | Missing basic extensions |
| Conversion actions | What's being tracked | Multiple or wrong conversion actions |

### Creative Audit

| Dimension | What to Assess | Tool |
|-----------|---------------|------|
| Creative volume | Number of active creatives per platform | `meta_get_insights` (ad level) |
| Creative age | How old are current creatives? | Platform UI / date filters |
| Format diversity | Image vs video vs carousel | `meta_get_insights` (ad level) |
| Message consistency | Do ads match landing page? | Manual review |
| A/B testing history | Have they been testing? | Experiment logs |
| Creative fatigue | Frequency vs performance trends | `meta_get_insights` (date breakdown) |

### Competitive Research

| Research Area | Method | Output |
|--------------|--------|--------|
| Meta Ad Library | facebook.com/ads/library | Competitor creative, messaging, offers |
| Google Ads Auction Insights | `google_ads_run_gaql` (auction insights) | Impression share, overlap rate |
| SEMrush / SpyFu | Third-party tools | Competitor keyword strategy |
| TikTok Creative Center | ads.tiktok.com/business/creativecenter | Trending formats, competitor ads |
| LinkedIn Ad Library | linkedin.com/ad-library | B2B competitor messaging |

### Audit Report Deliverable

Present findings as:

```
AUDIT SUMMARY FOR [CLIENT NAME]
Date: [Date]
Prepared by: [Agency Name]

CRITICAL ISSUES (Fix immediately):
1. [Issue] — Impact: [what's broken] — Fix: [action]
2. ...

HIGH PRIORITY (Fix within 2 weeks):
1. [Issue] — Impact: [lost efficiency] — Fix: [action]
2. ...

QUICK WINS (Easy improvements):
1. [Opportunity] — Expected impact: [X% improvement]
2. ...

PERFORMANCE BASELINE:
| Metric | Last 30 Days | Last 90 Days | Benchmark |
| Spend | €X | €X | N/A |
| Conversions | X | X | N/A |
| CPA | €X | €X | €X (industry avg) |
| ROAS | Xx | Xx | Xx (industry avg) |
```

---

## Phase 3: Strategy (Days 6-10)

### Objective
Define the channel mix, budget allocation, audience strategy, and creative brief for the first 90 days.

### Channel Mix Decision

Use the channel-selection-framework skill for detailed guidance. Quick decision:

| Business Type | Primary Channel | Secondary Channel | Budget Split |
|--------------|----------------|-------------------|-------------|
| E-commerce (<€5K/mo) | Meta Ads | Google Shopping | 60/40 |
| E-commerce (€5-25K/mo) | Meta + Google | TikTok | 40/40/20 |
| E-commerce (>€25K/mo) | Meta + Google + TikTok | YouTube, Pinterest | 35/35/20/10 |
| Lead gen (B2C) | Meta + Google Search | TikTok | 50/40/10 |
| Lead gen (B2B) | LinkedIn + Google Search | Meta | 40/40/20 |
| Local business | Google Search | Meta | 70/30 |
| SaaS | Google Search + LinkedIn | Meta | 40/35/25 |

### Budget Allocation Framework

```
Total monthly budget: €X

Step 1: Platform split (see table above)
Step 2: Funnel split per platform
  - Prospecting: 40-60% of platform budget
  - Retargeting: 30-40% of platform budget
  - Retention: 10-20% of platform budget
Step 3: Campaign-level allocation within each bucket
Step 4: Reserve 10-15% for testing
```

### Strategy Document Template

```
[CLIENT NAME] — ADVERTISING STRATEGY
Period: [Start Date] to [End Date]
Prepared by: [Agency]

1. OBJECTIVES
   - Primary goal: [Revenue / Leads / Awareness]
   - Target: [Specific number with timeline]
   - Budget: [Monthly, with platform breakdown]

2. AUDIENCE STRATEGY
   - Primary audience: [Description, size estimate]
   - Secondary audience: [Description, size estimate]
   - Retargeting audiences: [Windows, exclusions]

3. CHANNEL STRATEGY
   - [Platform 1]: Role, budget, campaign types
   - [Platform 2]: Role, budget, campaign types
   - [Platform 3]: Role, budget, campaign types

4. CREATIVE STRATEGY
   - Formats: [Image, video, carousel, UGC]
   - Messages: [Key value props, offers, CTAs]
   - Volume: [X creatives per month, X tests per month]

5. MEASUREMENT PLAN
   - Primary KPI: [ROAS / CPA / MER]
   - Secondary KPIs: [CTR, CVR, AOV]
   - Attribution model: [Last click, data-driven, MER]
   - Reporting: [Weekly email, monthly deck, quarterly review]

6. 90-DAY ROADMAP
   - Month 1: [Foundation, fix tracking, launch campaigns]
   - Month 2: [Optimize, test, scale winners]
   - Month 3: [Scale, expand, introduce new channels/audiences]
```

---

## Phase 4: Setup (Days 8-15)

### Objective
Implement tracking fixes, build campaign structure, and prepare creatives for launch.

### Tracking Implementation Checklist

| # | Task | Tool | Owner | Status |
|---|------|------|-------|--------|
| 1 | Fix any critical tracking issues from audit | `gtm_audit`, GTM | Agency | ☐ |
| 2 | Set up UTM naming convention | Spreadsheet template | Agency | ☐ |
| 3 | Configure GA4 key events | GA4 Admin | Agency | ☐ |
| 4 | Verify Meta CAPI implementation | Meta Events Manager | Agency/Dev | ☐ |
| 5 | Set up enhanced conversions (Google) | GTM or Google Ads | Agency | ☐ |
| 6 | Create custom conversions per platform | Platform UIs | Agency | ☐ |
| 7 | Build retargeting audiences | Meta, Google, TikTok | Agency | ☐ |
| 8 | Set up dashboards (Looker Studio or similar) | Dashboard tool | Agency | ☐ |

### Campaign Build Checklist

| # | Task | Platform | Priority |
|---|------|----------|----------|
| 1 | Create naming convention document | All | High |
| 2 | Build campaign structure per strategy | All | High |
| 3 | Set up audiences (prospecting + retargeting) | All | High |
| 4 | Upload and configure product catalog/feed | Meta, Google | High (e-commerce) |
| 5 | Create ad creatives (images, video, copy) | All | High |
| 6 | Set up ad extensions (Google) | Google | Medium |
| 7 | Build negative keyword lists (Google) | Google | Medium |
| 8 | Configure bid strategies per campaign | All | Medium |
| 9 | Set up automated rules (budget caps, alerts) | All | Medium |
| 10 | Peer review all campaigns before launch | Internal | High |

### Naming Convention Template

```
Platform_FunnelStage_Campaign_Targeting_GeoDate

Examples:
  META_TOF_Prospecting_BroadInterest_NL_2026Q2
  META_BOF_Retargeting_CartAbandoners_NL_2026Q2
  GOOGLE_MOF_Shopping_AllProducts_NL_2026Q2
  GOOGLE_BOF_Search_BrandTerms_NL_2026Q2
  TIKTOK_TOF_Prospecting_BroadInterest_NL_2026Q2

Ad Set Level:
  [Audience]_[Placement]_[Budget]

Ad Level:
  [Format]_[CreativeConcept]_[Version]_[Date]
  IMAGE_SocialProof_v1_20260415
  VIDEO_ProductDemo_v2_20260415
```

---

## Phase 5: Launch (Days 13-17)

### Pre-Launch QA Checklist

| # | Check | Verified |
|---|-------|---------|
| 1 | All tracking pixels firing correctly on landing pages | ☐ |
| 2 | Conversion events triggering on test purchases/leads | ☐ |
| 3 | UTM parameters passing correctly to GA4 | ☐ |
| 4 | All ad copy proofread (no typos, correct pricing) | ☐ |
| 5 | Landing page URLs all working (no 404s) | ☐ |
| 6 | Mobile experience tested (ads + landing pages) | ☐ |
| 7 | Budget caps set correctly (daily/lifetime) | ☐ |
| 8 | Targeting reviewed (geo, age, placements correct) | ☐ |
| 9 | Ad account billing confirmed (payment method active) | ☐ |
| 10 | Client approval received on all creatives | ☐ |
| 11 | Campaign scheduling correct (start/end dates) | ☐ |
| 12 | Automated alerts set up (spend anomalies, disapprovals) | ☐ |

### Launch Day Monitoring Plan

| Time | Action | What to Check |
|------|--------|--------------|
| Hour 0-1 | Verify delivery started | Impressions accumulating, no disapprovals |
| Hour 1-4 | Monitor spend pacing | Not overspending or underspending |
| Hour 4-8 | Check early signals | CTR reasonable, no obvious issues |
| End of Day 1 | First status check | Spend, impressions, clicks — sanity check |
| Day 2 | Delivery confirmation | All campaigns delivering, pixel events firing |
| Day 3-5 | Early optimization | Pause clear losers, adjust budgets slightly |
| Day 7 | First weekly report | Full performance review with client |

### Client Communication at Launch

```
SUBJECT: [Client Name] — Campaign Launch Confirmation

Hi [Client Name],

Your campaigns are now live across [platforms]. Here's what to expect:

WHAT'S LIVE:
- [Campaign 1]: [Brief description]
- [Campaign 2]: [Brief description]

WHAT TO EXPECT:
- Days 1-3: Platforms are in learning phase. Performance will fluctuate.
- Days 4-7: Early signals will emerge. We'll share first insights.
- Weeks 2-4: Algorithms optimize. This is when we start seeing real patterns.

IMPORTANT: Please don't make any changes directly in the ad accounts.
All optimizations will be managed by our team.

Your first weekly report will arrive on [day].

Best,
[Agency]
```

---

## Phase 6: Optimization (30/60/90 Day Plan)

### Days 1-30: Foundation & Learning Phase

| Week | Focus | Actions | MCP Tools |
|------|-------|---------|-----------|
| Week 1 | Delivery verification | Confirm all campaigns delivering, fix disapprovals | `meta_get_insights`, `google_ads_run_gaql` |
| Week 2 | Early optimization | Pause worst-performing ads, adjust audience/bids | `meta_get_insights`, `google_ads_run_gaql` |
| Week 3 | Creative refresh | Add 2-3 new creatives based on early winners | Platform UIs |
| Week 4 | Month-end review | Full performance analysis, identify trends | All platform tools + `ga4_run_report` |

**Month 1 Goals:**
- All campaigns exiting learning phase
- Baseline metrics established
- Worst performers cut, winners identified
- First creative test completed

### Days 31-60: Optimize & Test

| Week | Focus | Actions | MCP Tools |
|------|-------|---------|-----------|
| Week 5 | Scaling winners | Increase budget on top-performing campaigns | `meta_get_insights`, `google_ads_run_gaql` |
| Week 6 | Audience expansion | Test new audiences, expand retargeting windows | `meta_get_insights` |
| Week 7 | A/B testing | Launch first structured A/B test | Platform experiments |
| Week 8 | Mid-quarter review | Comprehensive review, adjust strategy if needed | All tools + `ga4_run_report` |

**Month 2 Goals:**
- At least 1 A/B test completed
- Budget reallocation based on performance data
- New audiences or platforms tested
- CPA/ROAS improving month-over-month

### Days 61-90: Scale & Expand

| Week | Focus | Actions | MCP Tools |
|------|-------|---------|-----------|
| Week 9 | Scale systematically | Increase budgets 20% on proven campaigns | All platform tools |
| Week 10 | New channel testing | Launch secondary platform if not yet active | New platform tools |
| Week 11 | Advanced optimization | Implement bid strategy changes, audience layering | `google_ads_run_gaql`, `meta_get_insights` |
| Week 12 | Quarterly review | Full presentation, strategy update for Q+1 | All tools, `workflow` |

**Month 3 Goals:**
- Hitting or approaching KPI targets
- Systematic testing cadence established
- Secondary platform validated
- Quarterly review delivered to client

---

## Communication Templates

### Weekly Update Email

```
SUBJECT: [Client Name] Weekly Report — Week of [Date]

PERFORMANCE SUMMARY (vs previous week):
| Metric | This Week | Last Week | Change |
| Spend | €X | €X | +X% |
| Conversions | X | X | +X% |
| CPA | €X | €X | -X% |
| ROAS | Xx | Xx | +X% |

TOP PERFORMERS:
1. [Best campaign/ad] — [Why it's working]
2. [Second best] — [Why it's working]

ACTIONS TAKEN:
1. [What we changed this week]
2. [What we changed this week]

PLAN FOR NEXT WEEK:
1. [What we'll do]
2. [What we'll do]

QUESTIONS/NEEDS:
- [Any creative assets needed?]
- [Any approvals pending?]
```

### Monthly Report Structure

```
[CLIENT NAME] — MONTHLY PERFORMANCE REPORT
Period: [Month Year]

EXECUTIVE SUMMARY
- Total spend: €X (+X% vs last month)
- Total conversions: X (+X% vs last month)
- Blended CPA: €X (target: €X)
- Blended ROAS: Xx (target: Xx)

PLATFORM BREAKDOWN
[Table with per-platform metrics]

CAMPAIGN HIGHLIGHTS
- Best performing: [details]
- Worst performing: [details]
- Testing results: [details]

INSIGHTS & LEARNINGS
1. [Key insight from the data]
2. [Key insight from the data]

NEXT MONTH PLAN
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

BUDGET RECOMMENDATION
- [Maintain / Increase / Reallocate] based on [rationale]
```

### Quarterly Business Review Agenda

| Time | Topic | Content |
|------|-------|---------|
| 0-10 min | Recap goals | Original KPIs vs actual |
| 10-25 min | Performance review | 90-day trends, platform comparison |
| 25-35 min | Testing recap | What was tested, what was learned |
| 35-45 min | Competitive update | Market changes, competitor activity |
| 45-55 min | Strategy for next quarter | Updated targets, new opportunities |
| 55-60 min | Q&A | Open discussion, concerns, ideas |

---

## MCP Tool Usage by Onboarding Phase

| Phase | Tool | Usage |
|-------|------|-------|
| Discovery | `workflow(action="list")` | Find relevant analysis workflows |
| Audit | `gtm_audit` | Comprehensive tracking audit |
| Audit | `meta_get_insights` | Meta account structure + performance baseline |
| Audit | `google_ads_run_gaql` | Google Ads structure + performance baseline |
| Audit | `ga4_run_report` | Website analytics baseline |
| Audit | `gsc_search_analytics` | Organic search baseline |
| Audit | `tiktok_get_report` | TikTok performance baseline |
| Audit | `linkedin_get_analytics` | LinkedIn performance baseline |
| Strategy | `workflow(action="run")` | Run analysis workflows for strategy input |
| Strategy | `skill(action="search")` | Find relevant expert skills |
| Setup | `google_ads_run_keyword_planner` | Keyword research for Google campaigns |
| Optimization | All insight tools | Ongoing performance monitoring |
