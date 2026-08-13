---
name: attribution-reconciler
description: "This skill should be used when the user asks to \"reconcile attribution data\", \"compare conversions across platforms\", \"fix attribution discrepancies\", mentions \"which conversion number should I believe\", \"why do Meta and GA4 show different numbers\", or \"GDPR impact on tracking\". Do NOT use for: single-platform optimization (use platform-specific skills), incrementality testing design (use incrementality-testing-guide), or first-party data / CAPI implementation details (use first-party-data-strategy)."
---
# Cross-Platform Attribution Reconciler

## Purpose

Help advertisers understand and reconcile the conversion discrepancies they see between Meta, Google Ads, GA4, TikTok, and LinkedIn. This is the #1 pain point across all advertising platforms - different platforms report different numbers for the same conversions.

## When to Use This Skill

Invoke when user mentions:
- **Discrepancies:** "Why do Meta and GA4 show different numbers?"
- **Trust questions:** "Which platform's data should I believe?"
- **Budget decisions:** "How do I allocate budget across channels?"
- **Reconciliation:** "How do I reconcile attribution across channels?"
- **Specific gaps:** "What's causing the 30% discrepancy I'm seeing?"

## Required Tools

Use these MCP tools to pull live data when diagnosing attribution discrepancies:

| Tool | Purpose |
|------|---------|
| `ga4_run_report` | Pull GA4 Key Events (conversions) as neutral baseline |
| `meta_query` | Pull Meta campaign conversions by attribution window |
| `google_ads_run_gaql` | Pull Google Ads conversion data for comparison |
| `tiktok_get_report` | Pull TikTok conversion data |
| `linkedin_get_analytics` | Pull LinkedIn conversion data |

**Recommended diagnostic sequence:**
```
1. ga4_run_report(property_id="...", start_date="2026-03-08", end_date="2026-04-05", metrics=["keyEvents"], dimensions=["date"])
2. meta_get_insights(account_id="act_...", level="campaign", date_preset="last_28d", fields=["spend","actions","impressions"])
3. google_ads_run_gaql(customer_id="...", query="SELECT campaign.name, metrics.conversions, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_28_DAYS")
```

---

## Quick Reference: Expected Discrepancies

These discrepancy ranges are **normal** and don't necessarily indicate a problem:

| Platform Comparison | Expected Difference | Primary Cause |
|--------------------|--------------------| --------------|
| Meta vs GA4 | Meta +15-30% higher | View-through + modeled conversions |
| Google Ads vs GA4 | Google +10-25% higher | Enhanced Conversions + modeling |
| TikTok vs GA4 | TikTok +20-40% higher | VTA attribution (30% of conversions) |
| LinkedIn vs GA4 | LinkedIn +15-35% higher | Long B2B cycles, cross-device |
| GA4 vs All | GA4 -18-35% lower | Cookie blocking, consent mode |

## Decision Framework: When to Investigate

```
                         What's the discrepancy level?
                                    |
        +---------------------------+---------------------------+
        |                           |                           |
        v                           v                           v
     <15%                       15-35%                       >35%
   ─────────                   ─────────                   ─────────
        |                           |                           |
        v                           v                           v
   NORMAL                    EXPECTED                    INVESTIGATE
   No action                 Check attribution           Check implementation
   needed                    windows first               issues
```

### Investigation Checklist (>35% Discrepancy)

**Step 1: Technical Implementation**
- [ ] Is the pixel/tag firing correctly? (Test with browser dev tools)
- [ ] Is server-side tracking (CAPI) set up?
- [ ] Are event IDs deduplicated properly?
- [ ] Are UTM parameters consistent across all ad URLs?
- [ ] Is Consent Mode v2 implemented? (Required for EEA since March 2024 — includes `ad_user_data` and `ad_personalization` parameters)

**Step 2: Attribution Settings**

| Platform | Where to Check | Default Setting |
|----------|---------------|-----------------|
| Meta | Settings > Attribution | 7-day click, 1-day view |
| Google Ads | Tools > Conversions > Settings | Last-click (or DDA) |
| GA4 | Admin > Attribution Settings | Cross-channel DDA (reports Key Events, not "Conversions") |
| TikTok | Assets > Events > Attribution | 7-day click, 1-day view |
| LinkedIn | Account Settings > Attribution | 30-day click, 7-day view |

**Step 3: Common Technical Issues**

| Issue | Symptom | Fix |
|-------|---------|-----|
| Broken pixel | GA4 shows 0, platform shows conversions | Reinstall/verify pixel |
| Missing UTM | Traffic shows as "direct" in GA4 | Add UTM parameters |
| Event mismatch | Different event names across platforms | Standardize naming |
| Time zone | Conversions on different days | Align time zones |
| Currency | Revenue doesn't match | Use same currency code |

## Which Number to Use: Decision Framework

```
                    What's your use case?
                            |
    +---------------+-------+-------+---------------+---------------+
    |               |               |               |               |
    v               v               v               v               v
OPTIMIZING      CROSS-CHANNEL    REPORTING      STRATEGIC       TRUE
SINGLE          BUDGET           TO             PLANNING        INCREMENTAL
PLATFORM        ALLOCATION       STAKEHOLDERS                   VALUE
    |               |               |               |               |
    v               v               v               v               v
Use             Use unified      Use GA4 as     Use MMM         Run
platform's      BI dashboard     source of      outputs         incrementality
own data        or GA4           truth                          tests
```

### Detailed Guidance by Use Case

#### 1. Optimizing a Single Platform
**Use: Platform's own data**

The platform's algorithm optimizes based on its own signals. Optimizing Meta campaigns based on GA4 data means fighting the algorithm.

*Example: Meta reports 100 conversions, GA4 shows 70. Optimize within Meta Ads Manager using Meta's 100.*

#### 2. Cross-Channel Budget Allocation
**Use: Unified BI or GA4 Key Events (with caveats)**

Need apples-to-apples comparison. GA4 uses consistent attribution across channels.

> **Terminology note:** GA4 renamed "Conversions" to **Key Events** in 2024. In GA4 reports, look for "Key events" (formerly conversions). Google Ads still shows "Conversions" — those are imported from GA4 Key Events or set up via Google Ads conversion tracking. Don't confuse the two.

**Caveats:**
- GA4 underreports by 18-35%
- Add modeling factor: multiply GA4 by 1.2-1.4
- Or use MMM for strategic allocation

#### 3. Reporting to Stakeholders
**Use: GA4 Key Events as single source of truth + context**

Consistency matters for trust. Explain discrepancies upfront.

*Script: "We use GA4 Key Events as our source of truth for cross-channel comparison. Note that GA4 captures ~70-80% of true conversions due to cookie restrictions. Platform dashboards show higher numbers due to view-through attribution and modeling."*

#### 4. Strategic Planning
**Use: Marketing Mix Modeling (MMM)**

MMM accounts for upper-funnel impact, offline conversions, and cross-channel effects.

*Best for: Budget >$50K/month, multiple channels, brand + performance mix.*

#### 5. Understanding True Incremental Value
**Use: Incrementality testing**

Only way to know what would be lost if a channel were turned off.

**Methods:**
- Geo holdouts (recommended)
- Ghost ads
- Pre/post analysis

## Attribution Window Comparison

### What Each Platform Captures

```
User Journey: Ad View (Day 0) -> Website Visit (Day 3) -> Purchase (Day 5)

Platform Attribution:
─────────────────────

META (7-day click + 1-day view):
├─ Day 0: View ──────────────────────────────► ✓ Counted (view-through)
├─ Day 3: Click ─────────────────────────────► ✓ Counted (7-day click)
└─ Day 5: Purchase

GOOGLE ADS (Last-click):
├─ Day 0: View ──────────────────────────────► ✗ Not counted
├─ Day 3: Click (if Google was last) ────────► ✓ Counted
└─ Day 5: Purchase

GA4 (Cross-channel DDA):
├─ Day 0: View ──────────────────────────────► Partial credit
├─ Day 3: Click ─────────────────────────────► Partial credit
└─ Day 5: Purchase (only if cookie persists) ─► May undercount

TIKTOK (7-day click + optional VTA):
├─ Day 0: View ──────────────────────────────► ✓ If VTA enabled (+30%)
├─ Day 3: Click ─────────────────────────────► ✓ Counted
└─ Day 5: Purchase
```

### Recommended Window Alignment

| Platform | Recommended Setting | Notes |
|----------|-------------------|-------|
| Meta | 7-day click, 1-day view | Default is fine |
| Google Ads | Data-driven attribution | Better than last-click |
| GA4 | Cross-channel DDA | Default is fine |
| TikTok | 7-day click, 1-day view | Match Meta |
| LinkedIn | 30-day click (B2B needs longer) | Don't shorten |

## Privacy Impact Assessment

### iOS 14+ Impact by Platform

| Platform | Data Loss | Mitigation | Recovery |
|----------|-----------|------------|----------|
| Meta | 30-50% | CAPI, AEM, broad targeting | ~70% with CAPI |
| Google | 15-25% | Enhanced Conversions, Consent Mode | ~85% with EC |
| TikTok | 20-35% | Events API, SKAN | ~75% with Events API |
| LinkedIn | 10-20% | Insight Tag, CAPI (beta) | ~90% with proper setup |

### Consent Mode Impact

With Consent Mode V2 properly implemented:
- **Consented users:** Full tracking
- **Non-consented users:** Modeled conversions (60-80% accuracy)
- **Net effect:** ~10-15% undercount vs pre-privacy world

### 🇪🇺 EU/GDPR-Specific Impact (DDMA 2025 Data)

European advertisers face additional signal loss due to GDPR compliance:

| Metric | EU | US | Delta | Impact |
|--------|----|----|-------|--------|
| Cookie consent opt-in | ~50% | ~78% (Meta) | -28pp | Smaller addressable audiences |
| CTR impact | -2.1% | Baseline | -2.1pp | Lower campaign efficiency |
| Conversion rate | -5.4% | Baseline | -5.4pp | Higher CPAs |
| Revenue per click | -5.7% | Baseline | -5.7pp | Reduced ROAS |
| Acquisition costs | +25% | Baseline | +25% | SMB impact especially |

#### EU Consent Rates by Country
| Country | Consent Rate | Implication |
|---------|--------------|-------------|
| Germany | 62% | Best EU performance |
| Netherlands | ~55% | Above EU average |
| France | 38% | Lowest major market |
| EU Average | ~50% | vs 32% US opt-in rate |

**Critical Insight:** EU advertisers should expect:
- +20-35% higher attribution discrepancies vs US benchmarks
- Meta underreports by additional 10-15% in low-consent markets (France)
- GA4 modeling less accurate (60-70% vs 80% in US)

### Privacy Signal Loss Compensation Recommendations

#### For EU Advertisers (High Privacy Impact)

**Tier 1: Essential (Do First)**
1. **Implement Consent Mode V2**
   - Recovers 60-80% of lost signals via Google modeling
   - Required for Google Ads in EEA since March 2024

2. **Deploy Server-Side Tracking (CAPI)**
   - Meta CAPI: Recovers ~70% of ATT signal loss
   - Google Enhanced Conversions: Recovers ~85%
   - TikTok Events API: Recovers ~75%

3. **Configure Event ID Deduplication**
   - Prevents double-counting between browser + server

**Tier 2: Advanced (Strong Signal Recovery)**
1. **First-Party Data Matching**
   - Meta Advanced Matching (email, phone hashes)
   - Google Customer Match
   - LinkedIn Matched Audiences

2. **Zero-Party Data Collection**
   - Progressive profiling in forms
   - Quiz/survey data for segmentation

3. **Probabilistic Modeling**
   - Meta Modeled Conversions
   - Google Enhanced Attribution

**Tier 3: Strategic (Long-Term)**
1. **Marketing Mix Modeling (MMM)**
   - Accounts for untracked conversions
   - Best for budgets >€50K/month

2. **Incrementality Testing**
   - Geo holdouts quarterly
   - Ghost ads for validation

3. **CDP Implementation**
   - Unified customer view
   - Privacy-compliant audience building

### EU Attribution Adjustment Factors

Apply these multipliers when comparing EU platforms to GA4:

| Platform | Standard Adjustment | EU Adjustment (Low Consent) |
|----------|--------------------|-----------------------------|
| Meta | +15-30% | +25-40% |
| Google Ads | +10-25% | +15-30% |
| TikTok | +20-40% | +30-50% |
| LinkedIn | +15-35% | +20-45% |

*Example: If Meta reports 100 conversions and GA4 reports 60 in Germany (62% consent), the 67% difference is likely within normal range for EU.*

## Validation Approaches

### Method 1: Geo Holdout Test (Recommended)

```
Setup:
1. Select 2-4 similar geographic regions
2. Turn off ads in half (control)
3. Run normally in others (test)
4. Measure conversion difference

Analysis:
- Incremental lift = Test conversions - Control conversions
- True ROAS = Incremental revenue / Ad spend

Timeline: 4-6 weeks minimum
Budget: ~10% of total to holdout
```

### Method 2: Cross-Reference with Source of Truth

```
Compare platform conversions to:
- CRM closed deals (ultimate truth)
- E-commerce platform orders (Shopify, etc.)
- Payment processor (Stripe, PayPal)

Calculate platform accuracy:
Platform Accuracy = Platform Reported / Verified Conversions
```

### Method 3: Triangulation

```
Example:
- Meta: 100 conversions
- Google: 80 conversions
- GA4: 60 conversions
- CRM: 85 actual deals

Then:
- Meta overcounts by ~18%
- Google undercounts by ~6%
- GA4 undercounts by ~29%

Apply these factors to future reporting.
```

## Practical Recommendations by Budget

### For Small Advertisers ($10K-50K/month)

1. **Accept discrepancies exist** - don't chase perfect attribution
2. **Use GA4 for unified reporting** - explain undercount to stakeholders
3. **Optimize within each platform** - use platform data for platform optimization
4. **Run simple holdout test** - turn off one channel for 2 weeks quarterly

### For Mid-Market ($50K-200K/month)

1. **Implement server-side tracking** - CAPI, Enhanced Conversions
2. **Build unified dashboard** - BigQuery/Looker with blended data
3. **Apply platform accuracy factors** - adjust based on CRM validation
4. **Consider lightweight MMM** - tools like Adinton, Marketing Evolution

### For Enterprise ($200K+/month)

1. **Full MMM implementation** - Meridian, Marketing Evolution, custom
2. **Regular incrementality testing** - quarterly geo holdouts
3. **Multi-touch attribution** - Northbeam, Triple Whale, Ruler
4. **Privacy-first infrastructure** - CDP, server-side, first-party data

## Online-to-Offline (O2O) Attribution

For retail, hospitality, and service businesses with physical locations, online ads often drive offline conversions. This is a critical blind spot in digital attribution.

### O2O Attribution Methods by Platform

#### Google Ads Store Visits
**Best for:** Retailers, restaurants, service providers with physical locations

| Requirement | Details |
|-------------|---------|
| Minimum locations | 10+ in most countries |
| Minimum conversions | ~100K ad clicks, ~thousands of store visits/month |
| Location data | Google My Business linked |
| Privacy | Based on aggregated, anonymized Location History |

**How to Enable:**
1. Link Google My Business to Google Ads
2. Enable location extensions
3. Reach volume threshold (~30 days)
4. Store Visit conversions auto-populate

**Accuracy:** ~70-80% (Google claim: 99% confidence)

#### Meta Offline Conversions

**Best for:** Any business with CRM/POS data

| Method | Setup Complexity | Accuracy |
|--------|-----------------|----------|
| Offline Conversions API | Medium | High (hashed match) |
| Partner Integrations (Square, Lightspeed) | Low | Medium |
| Manual Upload | High | Variable |

**How to Enable:**
1. Navigate to Events Manager > Offline Events
2. Create Offline Event Set
3. Upload CRM/POS data with event_time, email/phone hashes, value
4. Match window: 1-28 days (default: 7-day click)

**Key Fields for Upload:**
```
event_time, event_name, value, currency,
match_keys: {email, phone, fn, ln, zip, country}
```

#### LinkedIn Offline Conversions

**Best for:** B2B with long sales cycles

| Feature | Details |
|---------|---------|
| Match rate | Email-based, typically 30-50% |
| Sales cycle | Supports 90-day lookback |
| CRM integration | Salesforce, HubSpot, Marketo native |

**How to Enable:**
1. Campaign Manager > Account Assets > Offline Conversions
2. Connect CRM or upload CSV
3. Map fields (email required, company optional)
4. Set attribution window (default: 30-day)

#### TikTok Offline Events

**Status:** Limited availability (2025)

| Capability | Status |
|------------|--------|
| Events API | Available (requires developer setup) |
| Direct integrations | Shopify, Salesforce (beta) |
| Store visits | Not available |

### O2O Attribution Decision Framework

```
                Do you have physical locations?
                            |
              +-------------+-------------+
              |                           |
             YES                          NO
              |                     Use online-only
    +---------+---------+              attribution
    |                   |
  10+ locations?    <10 locations?
    |                   |
    v                   v
Google Store        Use Offline
Visits eligible     Conversions API
    |               (Meta, LinkedIn)
    v
Enable Store
Visits + Offline
Conversions for
triangulation
```

### O2O Reconciliation: Expected Discrepancies

| Comparison | Expected Gap | Reason |
|------------|-------------|--------|
| Online Conv vs Store Visits | Store +20-50% | Many online-influenced visits untracked |
| Platform O2O vs POS data | Platform -30-50% | Match rate limitations |
| Google Store Visits vs Meta O2O | Variable | Different methodologies |

### Geo Holdout for O2O Validation

The gold standard for O2O attribution validation:

```
Setup:
1. Select matched metro areas (similar demographics, store density)
2. Split: 50% test (ads on), 50% control (ads off)
3. Run for 4-6 weeks minimum
4. Measure: Store traffic + sales in both groups

Calculation:
Incremental Store Visits = Test Area Visits - Control Area Visits
Incremental Revenue = Test Area Revenue - Control Area Revenue
True O2O ROAS = Incremental Revenue / Ad Spend (Test Area)

Example:
- Test area: 10,000 store visits, €500K revenue, €50K ad spend
- Control area: 7,500 store visits, €375K revenue, €0 ad spend
- Incremental: 2,500 visits, €125K revenue
- True O2O ROAS: €125K / €50K = 2.5x
```

### Retail-Specific Recommendations

| Budget Level | O2O Attribution Approach |
|--------------|-------------------------|
| <€10K/month | Manual POS correlation (pre/post analysis) |
| €10-50K/month | Meta/LinkedIn Offline Conversions |
| €50-200K/month | + Google Store Visits + quarterly geo holdouts |
| €200K+/month | Full MMM with O2O modeling |

## Quick Reference Card

### When Platforms Disagree

| Scenario | Likely Cause | Action |
|----------|-------------|--------|
| Meta >> GA4 | View-through attribution | Normal if <30% gap |
| Google >> GA4 | Enhanced Conversions modeling | Normal if <25% gap |
| TikTok >> GA4 | VTA + in-app browser | Normal if <40% gap |
| GA4 >> Platform | Unlikely (GA4 usually lower) | Check for tracking issue on platform |
| All platforms way off | Technical issue | Audit tracking implementation |

### Rule of Thumb

**Trust overlap, not outliers.**

If three platforms agree on directional trends (up/down, better/worse), trust that signal even if absolute numbers differ.

## Output Template

When diagnosing attribution issues, provide:

```
## Attribution Diagnosis

### Discrepancy Analysis
- Platform A vs Platform B: X% difference
- Expected range: Y-Z%
- Status: Normal / Investigate
- Region: [EU/US/Global] - affects expected ranges

### 🇪🇺 EU Privacy Context (if applicable)
- Consent rate estimate: [Country-specific %]
- Additional signal loss: [+X% vs US baseline]
- EU-adjusted expected range: [Y-Z%]

### Likely Causes (Ranked)
1. [Most likely cause]
2. [Second most likely]
3. [Third most likely]

### O2O Attribution (if retail/offline)
- Store Visits available: [Yes/No]
- Offline Conversions setup: [Yes/No]
- Estimated O2O contribution: [X% of total conversions]
- Validation: [Geo holdout recommended / POS correlation]

### Recommendations

**Immediate Actions:**
- [Action 1]
- [Action 2]

**Technical Improvements:**
- [Improvement 1]
- [Improvement 2]

**Privacy Signal Recovery (Priority Order):**
1. [Highest impact action - e.g., CAPI if not implemented]
2. [Second priority]
3. [Third priority]

**Which Number to Use:**
- For [use case]: Use [platform]
- For [use case]: Use [platform]
- For O2O: Use [triangulation method]

### Validation Approach
- [Recommended validation method]
- For O2O: [Geo holdout / POS correlation recommended]
```

---

*Based on 2025-2026 attribution research across Meta, Google, LinkedIn, TikTok, and GA4.*
*EU benchmarks from DDMA Privacy Monitor 2025, IAB Europe 2026.*
