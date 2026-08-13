---
name: linkedin-lead-scoring-framework
description: "This skill should be used when the user asks to \"score LinkedIn leads\", \"improve MQL to SQL conversion\", \"reduce cost per qualified lead\", \"build a lead scoring model\", or mentions \"LinkedIn lead quality\", \"lead qualification framework\", or \"CRM integration for LinkedIn leads\". Do NOT use for: lead form design or A/B testing (use linkedin-lead-gen-optimizer), campaign performance diagnostics (use linkedin-performance-troubleshooter), or ABM account scoring (use linkedin-abm-targeting-strategy)."
---

# LinkedIn Lead Scoring Framework

## Purpose

Help advertisers build lead scoring models that distinguish high-intent buyers from casual form fillers on LinkedIn. The platform's high CPLs (€30-150+) make lead quality critical — a 10% improvement in MQL-to-SQL conversion typically saves more than a 20% CPL reduction. This skill provides scoring matrices, qualification frameworks, and cost analysis models to optimize for pipeline, not just leads.

## When to Use This Skill

Invoke when user mentions:
- **Lead quality:** "My LinkedIn leads aren't converting to sales"
- **Lead scoring:** "How do I score LinkedIn leads?"
- **MQL/SQL:** "What's a good MQL to SQL rate for LinkedIn?"
- **Cost per qualified lead:** "My CPL is too high but leads are bad"
- **CRM integration:** "How do I get LinkedIn lead data into my CRM?"
- **Form optimization:** "Should I add more fields to qualify leads?"

## Required Tools

| Tool | Purpose |
|------|---------|
| `linkedin_get_analytics` | Pull lead metrics, cost data, and conversion analytics |

---

## Part 1: Lead Classification Hierarchy

### Definitions for LinkedIn Advertising

```
RAW LEAD
├── Anyone who submits a LinkedIn Lead Gen Form
├── No qualification applied
├── Metric: CPL (Cost Per Lead)
└── LinkedIn benchmark: €30-150 depending on industry/geo

MARKETING QUALIFIED LEAD (MQL)
├── Passes demographic + behavioral scoring threshold
├── Matches ICP on firmographics (company size, industry, seniority)
├── Shows intent beyond form submission (content consumption, repeat visits)
├── Metric: CPMQL (Cost Per MQL)
└── Benchmark: 40-65% of raw leads should qualify as MQL

SALES ACCEPTED LEAD (SAL)
├── Sales team verifies MQL data and accepts for follow-up
├── Contact info is valid, company is real, timing is plausible
├── Metric: MQL-to-SAL rate
└── Benchmark: 70-85% of MQLs should be accepted

SALES QUALIFIED LEAD (SQL)
├── Sales confirms genuine buying intent through conversation
├── Has budget, authority, need, and timeline (BANT qualified)
├── Metric: SAL-to-SQL rate
└── Benchmark: 30-50% of SALs qualify as SQL

OPPORTUNITY
├── SQL enters sales pipeline with defined deal value
├── Metric: SQL-to-Opportunity rate
└── Benchmark: 50-70% of SQLs become opportunities
```

### Funnel Conversion Benchmarks by Industry

| Industry | Raw→MQL | MQL→SAL | SAL→SQL | SQL→Opp | Net Lead→Opp |
|----------|---------|---------|---------|---------|--------------|
| SaaS / MarTech | 55-65% | 75-85% | 35-45% | 55-65% | 8-16% |
| Enterprise IT | 45-55% | 70-80% | 30-40% | 50-60% | 5-11% |
| Financial Services | 50-60% | 80-90% | 40-50% | 60-70% | 10-19% |
| Professional Services | 60-70% | 80-85% | 35-45% | 55-65% | 9-17% |
| Manufacturing / Industrial | 40-50% | 70-80% | 25-35% | 45-55% | 3-8% |
| Healthcare / Life Sciences | 45-55% | 75-85% | 30-40% | 50-60% | 5-11% |
| Education / EdTech | 55-65% | 70-80% | 30-40% | 50-60% | 6-12% |

---

## Part 2: Lead Scoring Matrix

### Demographic Score (Fit Score): 0-50 Points

How well does the lead match your Ideal Customer Profile?

```
CATEGORY: JOB SENIORITY (max 15 points)
──────────────────────────────────────────
CXO / Owner / Partner               15 pts
VP                                   13 pts
Director                             11 pts
Manager                               8 pts
Senior Individual Contributor          5 pts
Entry Level / Intern                   2 pts
Unknown / Not provided                 0 pts

CATEGORY: JOB FUNCTION (max 15 points)
──────────────────────────────────────────
Primary target function (exact match)  15 pts
Adjacent function (related buyer)      10 pts
Influencer function (IT, Finance)       7 pts
Unrelated function                      2 pts
Unknown / Not provided                  0 pts

CATEGORY: COMPANY SIZE (max 10 points)
──────────────────────────────────────────
Sweet spot (e.g., 200-2,000 employees) 10 pts
Close match (e.g., 51-200 or 2K-10K)   7 pts
Viable (e.g., 10K+)                     4 pts
Too small (e.g., 1-50)                  1 pt
Unknown                                 0 pts

CATEGORY: INDUSTRY (max 10 points)
──────────────────────────────────────────
Primary target industry                10 pts
Adjacent industry                       7 pts
Viable industry                         4 pts
Non-target industry                     1 pt
Unknown                                 0 pts
```

### Behavioral Score (Intent Score): 0-50 Points

How much buying intent has the lead demonstrated?

```
CATEGORY: FORM ENGAGEMENT (max 20 points)
──────────────────────────────────────────────
Completed form with custom questions       20 pts
Completed standard form (prefilled)        10 pts
Opened form but abandoned                   3 pts
(Abandonment = clicked CTA but no submit)

CATEGORY: CONTENT ENGAGEMENT (max 15 points)
──────────────────────────────────────────────
Downloaded gated content (whitepaper, etc.) 10 pts
Watched video 75%+                          8 pts
Watched video 50%+                          5 pts
Clicked through to website                  5 pts
Engaged with multiple ads (3+)              8 pts
Engaged with single ad only                 3 pts
Document Ad: read 75%+ of pages             7 pts
Document Ad: read first page only           2 pts

CATEGORY: TEMPORAL SIGNALS (max 15 points)
──────────────────────────────────────────────
Submitted form on first ad exposure          5 pts
(High intent: they knew what they wanted)
Submitted after 3+ ad exposures             10 pts
(Nurtured: they researched before acting)
Submitted during business hours (9-18)       3 pts
Submitted on weekday (Mon-Fri)               2 pts
Repeat visitor within 7 days                 5 pts
```

### Total Score Interpretation

| Score Range | Classification | Recommended Action |
|-------------|---------------|-------------------|
| 80-100 | Hot Lead (SQL-ready) | Immediate sales outreach within 1 hour |
| 65-79 | Warm Lead (MQL) | Sales development outreach within 24 hours |
| 45-64 | Cool Lead (Marketing Nurture) | Add to email nurture sequence, retarget |
| 25-44 | Cold Lead (Low Priority) | Add to long-term nurture, re-score in 30 days |
| 0-24 | Unqualified | Do not pass to sales; review targeting |

---

## Part 3: LinkedIn-Specific Intent Signals

### Signals Available from LinkedIn Data

| Signal | Where to Find | Intent Strength |
|--------|--------------|-----------------|
| Job title / seniority | Lead Gen Form (prefilled) | Demographic fit |
| Company name / size | Lead Gen Form (prefilled) | Demographic fit |
| Form completion time | Inferred from submission speed | Speed <30s = auto-filled (lower intent) |
| Custom question answers | Lead Gen Form (custom fields) | High intent (effort required) |
| Content interaction depth | Document Ad page views, video % | Behavioral intent |
| Multi-touch engagement | Multiple ad clicks over time | Strong behavioral intent |
| Ad format of conversion | Which format generated the lead | See format scoring below |
| Geographic location | Profile data / targeting | Fit validation |

### Intent Scoring by Ad Format

Different formats signal different intent levels:

| Format | Base Intent Score | Rationale |
|--------|------------------|-----------|
| Message Ads (InMail) form submit | High (+8) | Responded to direct outreach |
| Conversation Ads (chose demo path) | High (+10) | Self-qualified through branching |
| Conversation Ads (chose content path) | Medium (+5) | Interested but not ready |
| Lead Gen Form (after Document Ad) | High (+8) | Consumed content then converted |
| Lead Gen Form (Single Image) | Medium (+5) | Standard conversion path |
| Lead Gen Form (Carousel) | Medium (+6) | Engaged with multiple slides |
| Website conversion (LinkedIn traffic) | High (+9) | Left LinkedIn to convert |

### Custom Question Scoring

Custom questions in Lead Gen Forms are the strongest quality signal. Score responses:

```
HIGH-INTENT QUESTIONS (recommended):
──────────────────────────────────────
"What's your timeline for implementation?"
  → "This quarter"         +15 pts
  → "Next quarter"         +10 pts
  → "This year"            +5 pts
  → "Just researching"     +2 pts

"What's your annual budget for [category]?"
  → >€100K                 +15 pts
  → €50K-100K              +10 pts
  → €10K-50K               +5 pts
  → "<€10K / Not sure"     +2 pts

"What is your biggest challenge with [topic]?"
  → Specific problem match  +10 pts
  → Related problem          +5 pts
  → Generic / vague          +2 pts

"Are you currently using a solution for [problem]?"
  → "Yes, looking to switch" +12 pts
  → "Yes, but evaluating"    +8 pts
  → "No, starting fresh"     +5 pts
  → "No, not a priority"     +1 pt
```

---

## Part 4: Cost Per Qualified Lead Analysis

### The True Cost Calculation

Most advertisers report CPL. What matters is CPQL (Cost Per Qualified Lead).

```
CPQL Formula:
─────────────
CPQL = Total LinkedIn Spend / Number of SQLs

Example:
Total spend: €15,000
Raw leads: 150 (CPL = €100)
MQLs: 90 (60% qualification rate → CPMQL = €167)
SALs: 72 (80% acceptance rate → CPSAL = €208)
SQLs: 29 (40% qualification rate → CPQL = €517)
Opportunities: 17 (59% conversion → CPOpp = €882)

The real cost of a sales-ready lead is 5x the reported CPL.
```

### CPQL Benchmarks by Industry

| Industry | Avg CPL | Avg CPQL (SQL) | CPL-to-CPQL Ratio |
|----------|---------|----------------|-------------------|
| SaaS (SMB) | €40-80 | €200-500 | 5-6x |
| SaaS (Enterprise) | €80-150 | €500-1,200 | 6-8x |
| Financial Services | €60-120 | €300-800 | 5-7x |
| Professional Services | €50-100 | €250-600 | 5-6x |
| Manufacturing | €70-130 | €400-1,000 | 6-8x |
| Healthcare | €80-150 | €500-1,200 | 6-8x |
| Education | €30-70 | €150-400 | 4-6x |

### When to Optimize for Quality vs Quantity

```
OPTIMIZE FOR LEAD QUALITY WHEN:
├── MQL rate is below 40% (targeting too broad)
├── SAL-to-SQL rate is below 25% (wrong decision makers)
├── Sales team complains about lead quality
├── ACV (annual contract value) is >€10K
├── Sales team capacity is limited (<5 reps)
└── Long sales cycle (>60 days)

OPTIMIZE FOR LEAD VOLUME WHEN:
├── MQL rate is above 65% (can afford broader reach)
├── Sales team has spare capacity
├── ACV is <€5K (volume economics)
├── Product-led growth (self-serve onboarding)
├── Building retargeting audiences
└── Short sales cycle (<30 days)
```

---

## Part 5: Form Design for Scoring

### Field Strategy: Balancing Volume vs Quality

```
FEWER FIELDS (3-4 fields) → Higher completion rate, lower quality
├── Use for: Tier 3 ABM, top-of-funnel content, audience building
├── Expected completion rate: 12-18% of form opens
├── Fields: Name, Email, Company (all prefilled by LinkedIn)
└── Scoring impact: Low — almost no behavioral signal from form itself

MODERATE FIELDS (5-6 fields) → Balanced
├── Use for: Tier 2 ABM, mid-funnel content, webinar registrations
├── Expected completion rate: 8-14% of form opens
├── Fields: Name, Email, Company + 1-2 custom questions
└── Scoring impact: Medium — custom answers provide qualification data

MORE FIELDS (7-8 fields) → Lower completion rate, higher quality
├── Use for: Tier 1 ABM, bottom-of-funnel offers, demo requests
├── Expected completion rate: 4-8% of form opens
├── Fields: Name, Email, Company, Phone + 2-3 custom questions
└── Scoring impact: High — each additional field is a friction filter
```

### Recommended Custom Questions by Funnel Stage

| Funnel Stage | Question Type | Example | Scoring Value |
|-------------|---------------|---------|---------------|
| Awareness | Interest qualifier | "Which topic interests you most?" (multi-select) | Low (2-5 pts) |
| Interest | Problem qualifier | "What's your biggest [category] challenge?" (dropdown) | Medium (5-10 pts) |
| Consideration | Timeline qualifier | "When do you plan to implement?" (dropdown) | High (5-15 pts) |
| Decision | Budget qualifier | "What's your annual budget for [category]?" (dropdown) | High (5-15 pts) |
| Decision | Authority qualifier | "What's your role in purchasing decisions?" (dropdown) | High (5-15 pts) |

### Form Field Completion Rate Impact

Each additional form field reduces completion rate:

| Number of Fields | Relative Completion Rate | Quality Signal |
|-----------------|-------------------------|---------------|
| 3 (all prefilled) | 100% baseline | Very low |
| 4 (1 custom) | 80-90% of baseline | Low |
| 5 (2 custom) | 65-80% of baseline | Medium |
| 6 (3 custom) | 50-65% of baseline | Medium-High |
| 7 (4 custom) | 35-50% of baseline | High |
| 8+ (5+ custom) | 20-35% of baseline | Very high |

---

## Part 6: Measuring Lead Quality with MCP Tools

### Pull Lead Performance Data

```
linkedin_get_analytics(
    account_id="<account>",
    start_date="YYYY-MM-DD",
    end_date="YYYY-MM-DD",
    level="campaign",
    entity_id="<campaign_id>",
    fields=["costInLocalCurrency", "clicks", "impressions"]
)
```

### Lead Quality Analysis Framework

After pulling data, calculate these derived metrics:

```
1. Lead Rate = Leads / Clicks × 100
   ├── Good: >5%
   ├── Average: 2-5%
   └── Poor: <2% (targeting or creative issue)

2. CPL = Spend / Leads
   ├── Compare to industry benchmarks above
   └── Track weekly trend (rising CPL = audience fatigue)

3. CPMQL = Spend / MQLs (requires CRM data)
   ├── If CPMQL > 3× CPL → scoring too strict OR targeting misaligned
   └── If CPMQL < 1.5× CPL → scoring may be too lenient

4. Lead Velocity = (This month MQLs - Last month MQLs) / Last month MQLs × 100
   ├── Positive trend: Scaling working
   └── Negative trend: Audience exhaustion or quality issues

5. Speed-to-Contact Score = % of leads contacted within 1 hour
   ├── Target: >80%
   └── Impact: Leads contacted within 5 minutes are 21× more likely to qualify
```

### Campaign Comparison for Quality

Compare lead quality across campaigns:

```
Step 1: Pull analytics for all active campaigns
Step 2: Calculate CPL per campaign
Step 3: Map to CRM qualification rates per campaign
Step 4: Calculate CPQL per campaign
Step 5: Rank campaigns by CPQL (not CPL)

Often the highest-CPL campaign has the lowest CPQL because
it attracts more qualified leads through tighter targeting.
```

---

## Part 7: CRM Integration Approach

### Data Flow Architecture

```
LinkedIn Lead Gen Form
        │
        ▼
LinkedIn Lead Sync (native or Zapier/webhook)
        │
        ▼
CRM (HubSpot / Salesforce / Pipedrive)
        │
        ├── Auto-assign lead score (demographic + behavioral)
        ├── Auto-assign to sales rep (round-robin or territory)
        ├── Trigger notification (Slack, email) for hot leads (80+ score)
        ├── Add to nurture sequence (for leads scoring 25-64)
        └── Tag with LinkedIn campaign source for attribution
        │
        ▼
Feedback loop: CRM outcomes → LinkedIn campaign optimization
```

### CRM Sync Options

| Method | Speed | Complexity | Best For |
|--------|-------|------------|----------|
| LinkedIn native CRM sync (HubSpot, Salesforce) | Real-time | Low | Standard setups |
| Zapier / Make.com webhook | Near real-time (1-5 min) | Medium | Custom workflows, multi-tool |
| LinkedIn Marketing API (manual) | Batch (manual pull) | High | Custom scoring models |
| LinkedIn Lead Sync via HubSpot Connector | Real-time | Low | HubSpot users |

### LinkedIn Revenue Attribution Reports

LinkedIn's native Revenue Attribution Reports (available in Campaign Manager > Analyze > Revenue Attribution) connect LinkedIn ad exposure to CRM pipeline and revenue using direct CRM integration (Salesforce, HubSpot, Dynamics 365). This provides closed-loop reporting without manual CSV exports.

**How it works:**
1. Connect your CRM to LinkedIn Campaign Manager (native integration)
2. LinkedIn matches contacts who saw/engaged with ads to CRM contacts
3. Report shows: pipeline influenced, revenue influenced, deal stages, average deal size by campaign

**When to use over manual tracking:** Any account spending >€5K/month on LinkedIn with a connected CRM. The data quality is significantly better than last-touch attribution.

### Closed-Loop Reporting

The ultimate optimization is feeding CRM outcomes back to LinkedIn:

```
CRM Stage Updates → Tag LinkedIn leads with:
├── "Won" → High-performing campaign/creative identified
├── "Lost - Wrong fit" → Targeting adjustment needed
├── "Lost - No budget" → Budget qualifier question needed in form
├── "Lost - Bad timing" → Nurture sequence needed, timeline question in form
├── "No response" → Contact info quality issue, phone number field needed
└── "Disqualified" → Scoring model needs recalibration
```

---

## Part 8: Scoring Model Calibration

### Monthly Calibration Process

1. **Export last 30 days of leads** with final CRM disposition
2. **Calculate predicted vs actual qualification rate** per score band
3. **Adjust scoring weights** if any band is off by more than 15%
4. **Review disqualification reasons** to identify new scoring criteria
5. **Check for score inflation/deflation** trends over time

### Calibration Red Flags

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| >70% of leads score 80+ | Scoring too generous | Tighten behavioral thresholds |
| <20% of leads score 45+ | Scoring too strict | Lower seniority requirements or expand functions |
| High scores but low SQL rate | Demographic score weighted too heavily | Increase behavioral score weight |
| Low scores but some converting | Behavioral signals underweighted | Add engagement depth scoring |
| All leads score 45-55 | No differentiation in model | Add custom question scoring, widen point ranges |

### A/B Testing Scoring Models

Run parallel scoring models for 30 days:
- **Model A:** Current scoring weights
- **Model B:** Adjusted weights based on calibration
- Compare MQL-to-SQL conversion rates between models
- Adopt the model with higher SQL conversion per euro spent

---

## Quick Reference: Lead Scoring Checklist

1. Define MQL, SAL, and SQL criteria specific to your business
2. Build demographic score (seniority + function + company size + industry = 50 pts)
3. Build behavioral score (form engagement + content depth + temporal signals = 50 pts)
4. Set threshold bands (Hot 80+, Warm 65-79, Cool 45-64, Cold 25-44, Unqualified 0-24)
5. Add custom form questions aligned to scoring (timeline, budget, authority)
6. Configure CRM sync for real-time lead routing
7. Set up speed-to-contact alerts for hot leads (80+ score)
8. Create nurture sequences for cool leads (45-64 score)
9. Calibrate scoring model monthly using CRM outcome data
10. Track CPQL (not just CPL) as the primary efficiency metric
