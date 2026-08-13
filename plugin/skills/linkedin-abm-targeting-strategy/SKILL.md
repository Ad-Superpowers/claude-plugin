---
name: linkedin-abm-targeting-strategy
description: "This skill should be used when the user asks to \"target specific companies on LinkedIn\", \"build an ABM campaign\", \"reach the buying committee\", \"create a company list for LinkedIn\", or mentions \"account-based marketing\", \"decision-maker targeting\", or \"account penetration\". Do NOT use for: general LinkedIn campaign optimization (use linkedin-performance-troubleshooter), lead form strategy (use linkedin-lead-gen-optimizer), or campaign scaling (use linkedin-campaign-scaling-guide)."
---

# LinkedIn ABM Targeting Strategy

## Purpose

Help advertisers build and execute account-based marketing campaigns on LinkedIn by mapping target accounts to decision-maker personas, building tiered company lists, and layering seniority/function targeting for maximum account penetration. ABM on LinkedIn consistently delivers 2-5x higher conversion rates vs broad targeting, but only when the targeting architecture is correct.

## When to Use This Skill

Invoke when user mentions:
- **ABM campaigns:** "I want to target specific companies on LinkedIn"
- **Company list targeting:** "I have a list of target accounts"
- **Decision makers:** "How do I reach the buying committee?"
- **Account penetration:** "I need to reach multiple people at the same company"
- **Named account strategy:** "We're doing account-based marketing"
- **Enterprise targeting:** "How do I target Fortune 500 companies?"

## Required Tools

| Tool | Purpose |
|------|---------|
| `linkedin_query` | Pull campaign data, audience sizes, and targeting configurations |
| `linkedin_get_analytics` | Measure account penetration, engagement rates by company |

---

## Part 1: ABM Tier Architecture

### Three-Tier Account Model

ABM effectiveness depends on matching investment level to account value. Never treat all target accounts the same.

```
TIER 1: Strategic Accounts (5-25 accounts)
├── Highest deal value (>€50K ACV)
├── Named account campaigns (1 campaign per 3-5 accounts)
├── Fully custom creative per account cluster
├── Budget: 40-50% of total ABM spend
├── Goal: Multi-threaded engagement (3+ contacts per account)
└── Measurement: Account penetration rate, meetings booked

TIER 2: Target Accounts (25-200 accounts)
├── Medium deal value (€10K-50K ACV)
├── Grouped campaigns by industry/segment (10-30 accounts each)
├── Semi-custom creative per segment
├── Budget: 30-35% of total ABM spend
├── Goal: Initial engagement + MQL generation
└── Measurement: Engagement rate, lead volume, pipeline influenced

TIER 3: Market Accounts (200-1,000 accounts)
├── Lower deal value (<€10K ACV) or early-stage prospects
├── Broad campaigns by firmographic cluster
├── Template creative with dynamic elements
├── Budget: 15-25% of total ABM spend
├── Goal: Awareness + demand generation
└── Measurement: Reach, website visits, content engagement
```

### Company List Upload Requirements

LinkedIn Matched Audiences company list specs:
- **Minimum:** 300 companies per list (LinkedIn requires this for delivery)
- **Recommended:** 1,000+ companies for stable delivery and optimization
- **Format:** CSV with company name + domain (both required for best match)
- **Match rate benchmark:** 60-80% typical; below 50% indicates data quality issues
- **Update cadence:** Re-upload monthly to capture CRM pipeline changes

### Data Enrichment Before Upload

Always enrich lists before uploading to maximize match rates:

| Field | Priority | Impact on Match Rate |
|-------|----------|---------------------|
| Company name (exact legal entity) | Required | +40% base match |
| Company domain (website URL) | Required | +25% match improvement |
| Company LinkedIn page URL | High | +15% match improvement |
| Company email domain | Medium | +5% match improvement |
| Industry/size (for validation) | Low | Used for post-match QA |

---

## Part 2: Decision-Maker Targeting Matrix

### The Buying Committee Framework

B2B purchases involve 6-10 decision makers on average. ABM must reach multiple roles.

```
ROLE IN PURCHASE    │ JOB FUNCTION           │ SENIORITY LEVEL      │ CONTENT ANGLE
────────────────────┼────────────────────────┼──────────────────────┼──────────────────────
Champion            │ Core function (e.g.,   │ Manager, Director    │ Product-focused,
(finds & advocates) │ Marketing, IT, Sales)  │                      │ how-to, comparison
────────────────────┼────────────────────────┼──────────────────────┼──────────────────────
Decision Maker      │ Core function or       │ VP, C-Suite          │ ROI, strategic value,
(signs off)         │ General Management     │                      │ case studies
────────────────────┼────────────────────────┼──────────────────────┼──────────────────────
Influencer          │ Adjacent function      │ Senior, Manager      │ Integration benefits,
(shapes opinion)    │ (e.g., Ops, Finance)   │                      │ workflow improvement
────────────────────┼────────────────────────┼──────────────────────┼──────────────────────
Blocker             │ IT Security, Legal,    │ Manager, Director    │ Compliance, security,
(can veto)          │ Procurement            │                      │ risk mitigation
────────────────────┼────────────────────────┼──────────────────────┼──────────────────────
End User            │ Core function          │ Entry, Senior        │ Ease of use, daily
(uses product)      │                        │                      │ workflow benefits
```

### LinkedIn Seniority Mapping

LinkedIn seniority levels and their typical roles:

| LinkedIn Seniority | Typical Titles | ABM Use Case |
|-------------------|----------------|--------------|
| CXO | CEO, CFO, CTO, CMO, CRO | Final decision maker; strategic messaging only |
| VP | VP Marketing, VP Engineering, VP Sales | Budget holder; ROI and business impact |
| Director | Director of Ops, Director of IT | Evaluation leader; comparison and proof |
| Manager | Marketing Manager, Product Manager | Champion/influencer; tactical content |
| Senior | Senior Engineer, Senior Analyst | Influencer/end user; product capabilities |
| Entry | Analyst, Associate, Coordinator | End user; UX and workflow content |

### Job Function Targeting Combinations

High-performing ABM function + seniority combinations:

**SaaS / MarTech:**
```
Primary:   Marketing + Director/VP + company list
Secondary: Information Technology + Manager/Director + company list
Tertiary:  Operations + VP/Director + company list
```

**Enterprise IT / Security:**
```
Primary:   Information Technology + Director/VP/CXO + company list
Secondary: Engineering + Manager/Director + company list
Tertiary:  Operations + VP/Director + company list
```

**HR Tech:**
```
Primary:   Human Resources + Director/VP + company list
Secondary: Operations + Manager/Director + company list
Tertiary:  General Management + VP/CXO + company list
```

**Financial Services / FinTech:**
```
Primary:   Finance + Director/VP/CXO + company list
Secondary: Accounting + Manager/Director + company list
Tertiary:  Information Technology + Director/VP + company list
```

---

## Part 3: Campaign Architecture for ABM

### Campaign Structure Decision Tree

```
                    How many target accounts?
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          5-25          25-200       200-1,000
        (Tier 1)      (Tier 2)      (Tier 3)
              │            │            │
              ▼            ▼            ▼
     1 campaign per   1 campaign per   1-3 campaigns
     3-5 accounts     industry/segment  by company size
              │            │            │
              ▼            ▼            ▼
     Custom creative  Segment-specific  Template creative
     per cluster      creative          with variations
              │            │            │
              ▼            ▼            ▼
     €50-100/day      €30-75/day       €25-50/day
     per campaign     per campaign      per campaign
```

### Layered Targeting Setup

For each ABM campaign, layer targeting in this order:

**Layer 1 (Required): Company List**
```
linkedin_query(
    account_id="<account>",
    entity_type="campaigns",
    status=["ACTIVE"]
)
```
Upload matched audience list as base targeting.

**Layer 2 (Required): Job Function + Seniority**
Narrow to relevant decision makers within target accounts.

**Layer 3 (Optional): Skills or Groups**
Add skill-based targeting for technical roles (e.g., "Salesforce" skill for CRM buyers).

**Layer 4 (Optional): Exclusions**
- Exclude current customers (upload customer list)
- Exclude competitors (upload competitor company list)
- Exclude disqualified leads from CRM

### Audience Size Guidelines for ABM

| Tier | Target Audience Size | Too Small | Too Large |
|------|---------------------|-----------|-----------|
| Tier 1 | 1,000 - 10,000 | <500 (won't deliver) | >20,000 (too broad) |
| Tier 2 | 10,000 - 50,000 | <5,000 (limited optimization) | >100,000 (losing ABM precision) |
| Tier 3 | 50,000 - 300,000 | <20,000 (underspending) | >500,000 (not really ABM) |

If audience is too small: Broaden seniority levels or add adjacent job functions.
If audience is too large: Tighten seniority, add skill filters, or split into more campaigns.

---

## Part 4: Account Penetration Measurement

### Account Penetration Score

Track how deeply you're reaching into each target account:

```
Account Penetration Score = (Unique Contacts Engaged / Total Buying Committee Size) x 100

Benchmarks:
- <10%: Low penetration — not enough contacts seeing your ads
- 10-25%: Developing — early-stage awareness building
- 25-50%: Strong — multiple decision makers engaged
- >50%: High penetration — ready for sales activation
```

### Engagement Depth Scoring

Weight different engagement types:

| Engagement Type | Weight | Signal Strength |
|----------------|--------|-----------------|
| Ad impression | 1 | Awareness |
| Ad click | 5 | Interest |
| Video view (50%+) | 3 | Consideration |
| Lead form open | 8 | Intent |
| Lead form submit | 15 | Strong intent |
| Website visit (from ad) | 7 | Active research |
| Content download | 10 | Evaluation |
| Multiple ad interactions (3+) | 12 | High engagement |

### Measuring with MCP Tools

```
linkedin_get_analytics(
    account_id="<account>",
    start_date="YYYY-MM-DD",
    end_date="YYYY-MM-DD",
    level="campaign",
    entity_id="<tier1_campaign>",
    fields=["impressions", "clicks", "costInLocalCurrency"]
)
# Note: per-company breakdown is not available via API — check Campaign Manager
# Demographics tab for company-level engagement data.
```

Key ABM metrics to track:
- **Account reach:** Unique companies reached / total target accounts
- **Multi-contact reach:** Accounts with 2+ unique contacts engaged
- **Engagement rate by tier:** Should increase from Tier 3 → Tier 1
- **Pipeline influence:** Accounts that entered pipeline after ad exposure
- **Sales cycle acceleration:** Days to close for ABM-touched vs non-ABM accounts

---

## Part 5: LinkedIn Audience Network for ABM

### When to Use Audience Network

LinkedIn Audience Network (LAN) extends ads to partner sites and apps.

**Use LAN when:**
- Tier 2/3 campaigns need more reach at lower CPMs
- Frequency is high (>8/month) on LinkedIn feed alone
- Brand awareness is the primary objective
- You need to stretch budget across large account lists

**Do NOT use LAN when:**
- Tier 1 campaigns (keep premium placement)
- Lead generation is the objective (forms are LinkedIn-only)
- Conversion tracking requires LinkedIn-specific attribution
- Brand safety is a top concern (less control on partner sites)

### LAN Performance Benchmarks

| Metric | LinkedIn Feed Only | With LAN Enabled |
|--------|-------------------|------------------|
| CPM | €25-60 | €15-35 |
| CTR | 0.35-0.65% | 0.20-0.40% |
| Viewability | 70-80% | 50-65% |
| Lead quality | Baseline | 15-30% lower |
| Reach extension | Baseline | +30-60% |

---

## Part 6: Account Expansion Strategies

### Expanding from Engaged Accounts

Once accounts show engagement, expand strategically:

**Horizontal expansion** (more roles at engaged accounts):
- Add adjacent job functions (e.g., Finance after reaching IT)
- Lower seniority threshold (e.g., add Manager after reaching Director+)
- Add Blocker personas (Legal, Procurement) for late-stage accounts

**Vertical expansion** (similar companies to engaged accounts):
- LinkedIn Lookalike from engaged company list (1% size)
- LinkedIn Predictive Audiences — AI-generated audiences built from your CRM data or intent signals (available in Campaign Manager under Audiences > Create Audience > Predictive)
- Industry + company size mirroring of Tier 1 engaged accounts
- Promote engaged Tier 2 accounts to Tier 1 treatment

**Content expansion** (deeper funnel for engaged accounts):
```
Stage 1 (Awareness):  Thought leadership, industry trends     → All tiers
Stage 2 (Interest):   Solution overview, comparison guides     → Engaged accounts
Stage 3 (Evaluation): Case studies, ROI calculators            → Multi-contact engaged
Stage 4 (Decision):   Demo offers, free trials, consultation   → High penetration accounts
```

### Re-Tiering Cadence

Review and adjust account tiers quarterly:

| Signal | Action |
|--------|--------|
| Tier 2 account shows 3+ contacts engaged | Promote to Tier 1 |
| Tier 1 account shows zero engagement after 90 days | Demote to Tier 2 or review ICP fit |
| Tier 3 account requests demo or starts trial | Promote to Tier 1 |
| Any account becomes a customer | Move to customer expansion campaign |
| Account churns or goes dark for 180 days | Remove from active ABM, add to nurture |

---

## Part 7: Budget Allocation Framework

### ABM Budget Calculator

```
Monthly ABM Budget Allocation:

Total LinkedIn ABM Budget: €________/month

Tier 1 (40-50%):  €________ ÷ [# Tier 1 campaigns] = €________/campaign/day
Tier 2 (30-35%):  €________ ÷ [# Tier 2 campaigns] = €________/campaign/day
Tier 3 (15-25%):  €________ ÷ [# Tier 3 campaigns] = €________/campaign/day

Minimum viable ABM budget:
- Tier 1 only: €3,000/month (5-10 accounts, 2-3 campaigns)
- Tier 1+2:    €6,000/month (up to 100 accounts)
- Full 3-tier: €10,000+/month (up to 1,000 accounts)
```

### Expected ABM Performance by Tier

| Metric | Tier 1 | Tier 2 | Tier 3 |
|--------|--------|--------|--------|
| CPM | €40-70 | €30-55 | €20-45 |
| CTR | 0.5-0.9% | 0.35-0.6% | 0.25-0.45% |
| Lead rate | 2-5% of clicks | 1-3% of clicks | 0.5-1.5% of clicks |
| Cost per lead | €80-200 | €100-300 | €150-500 |
| Account engagement rate | 40-70% | 20-40% | 10-25% |
| Pipeline influence | 15-30% of Tier 1 accounts | 5-15% | 2-8% |

---

## Quick Reference: ABM Campaign Checklist

1. Define ICP and build tiered account list (Tier 1/2/3)
2. Map buying committee roles per tier (Champion, Decision Maker, Influencer, Blocker, End User)
3. Upload company lists to LinkedIn Matched Audiences (min 300 per list)
4. Layer job function + seniority targeting on each list
5. Create tier-appropriate creative (custom → segment → template)
6. Set budget allocation by tier (40/30/25 split)
7. Exclude current customers and competitors
8. Launch and monitor account penetration weekly
9. Re-tier accounts quarterly based on engagement signals
10. Coordinate with sales on Tier 1 account engagement handoffs
