---
name: first-party-data-strategy
description: "This skill should be used when the user asks to \"set up server-side tracking\", \"implement CAPI\", \"build a first-party data strategy\", mentions \"Consent Mode V2\", \"cookieless advertising\", or \"GDPR-compliant tracking setup\". Do NOT use for: attribution discrepancy diagnosis (use attribution-reconciler), GTM container auditing (use gtm-container-auditor), or incrementality measurement (use incrementality-testing-guide)."
---
# First-Party Data Strategy Guide

## Purpose

Help advertisers build a robust first-party data infrastructure that maintains measurement quality and targeting effectiveness in an increasingly privacy-restricted advertising landscape.

## When to Use This Skill

Invoke when user mentions:
- **First-party data:** "How do I collect first-party data?"
- **Server-side tracking:** "Should I implement CAPI?"
- **Privacy compliance:** "How do I handle GDPR tracking?"
- **Consent Mode:** "What is Consent Mode V2?"
- **CDPs:** "Do I need a Customer Data Platform?"
- **Cookieless:** "How do I prepare for cookie deprecation?"
- **Signal loss:** "My conversion tracking is getting worse"

---

## Part 1: The Privacy Landscape (2025-2026)

### Current State of Digital Advertising Privacy

| Change | Status | Impact |
|--------|--------|--------|
| iOS App Tracking Transparency | Active (since 2021) | 40-60% signal loss on mobile |
| GDPR Consent Requirements | Active | ~50% opt-in rates in EU |
| Chrome 3rd Party Cookie Deprecation | Active (phasing out 2025-2026) | Major ongoing impact — not a future risk |
| Meta Aggregated Event Measurement | Active | Limited to 8 priority events |
| Google Privacy Sandbox | Deployed | Topics API, Protected Audiences replacing cookie-based targeting |

> **Cookie deprecation is happening now, not in the future.** Chrome began restricting third-party cookies in 2024 and is continuing the phase-out through 2025-2026. Safari and Firefox have blocked third-party cookies for years. The practical impact on tracking is already visible in attribution gaps. First-party data strategy is not preparation for a future change — it is the fix for a current problem.

### Signal Loss by Region

| Region | Cookie Consent Rate | Mobile Opt-in Rate | Total Signal Loss |
|--------|--------------------|--------------------|-------------------|
| EU (GDPR) | 45-55% | 25-35% | 50-65% |
| UK | 50-60% | 30-40% | 45-55% |
| US (No federal law) | 75-85% | 35-45% | 25-35% |
| California (CCPA) | 65-75% | 35-45% | 35-45% |

### The First-Party Data Advantage

| Data Type | Definition | Privacy Status | Value |
|-----------|------------|----------------|-------|
| **First-party** | Data you collect directly | Owned, compliant | Highest |
| **Second-party** | Partner's first-party data | Licensed | Medium |
| **Third-party** | Aggregated from many sources | Declining | Lowest |

**Why First-Party Data Wins:**
- You own it (no dependency on external sources)
- Compliant by design (collected with consent)
- More accurate (direct from customer)
- Future-proof (not affected by browser changes)

---

## Part 2: First-Party Data Collection Strategy

### Data Collection Framework

**What to Collect:**

| Data Type | Examples | Collection Method | Priority |
|-----------|----------|-------------------|----------|
| **Identity** | Email, phone, user ID | Account creation, checkout | P0 |
| **Behavioral** | Page views, clicks, time on site | Analytics, server logs | P0 |
| **Transactional** | Purchases, order value, products | E-commerce platform | P0 |
| **Preference** | Newsletter signup, interests | Preference centers | P1 |
| **Engagement** | Email opens, app usage | Email/app analytics | P1 |
| **Feedback** | Reviews, surveys, NPS | Direct collection | P2 |

### Collection Points

| Touchpoint | Data Collected | Consent Required | Implementation |
|------------|---------------|------------------|----------------|
| Website registration | Email, name | Yes | Form + CMP |
| Newsletter signup | Email | Yes | Double opt-in |
| Purchase checkout | Email, phone, address | Legitimate interest | Order flow |
| Account creation | Profile data | Yes | Sign-up flow |
| Loyalty program | Preferences, history | Yes | Program enrollment |
| Mobile app | Device ID, behavior | Yes (ATT) | SDK |
| Customer service | Interaction history | Legitimate interest | CRM |

### Data Quality Hierarchy

**Email Quality Ladder:**

| Level | Description | Match Rate | Value |
|-------|-------------|------------|-------|
| **Verified email** | Confirmed via double opt-in | 95%+ | Highest |
| **Checkout email** | Provided at purchase | 85-95% | High |
| **Registration email** | Account signup | 70-85% | Medium |
| **Lead form email** | Marketing capture | 50-70% | Lower |
| **Third-party list** | Purchased data | 20-40% | Lowest |

---

## Part 3: Server-Side Tracking Implementation

### Why Server-Side Tracking

| Client-Side (Traditional) | Server-Side |
|---------------------------|-------------|
| Blocked by ad blockers (25-40%) | Not affected by ad blockers |
| Affected by ITP/ETP | Resistant to browser restrictions |
| Limited by cookie consent | Works with proper consent |
| 6-7 day cookie lifetime (Safari) | Extended attribution |
| Visible to user | More control over data |

### Platform-Specific Implementation

#### Meta Conversions API (CAPI)

**What it does:** Send conversion events directly from your server to Meta.

**Implementation Options:**

| Method | Complexity | Best For |
|--------|------------|----------|
| **Partner integration** | Low | Shopify, WooCommerce, Segment |
| **Gateway API** | Medium | Custom sites with GTM |
| **Direct integration** | High | Full control, custom platforms |

**Required Fields:**

| Field | Type | Match Quality Impact |
|-------|------|---------------------|
| email (hashed) | em | High |
| phone (hashed) | ph | Medium |
| first_name (hashed) | fn | Low |
| last_name (hashed) | ln | Low |
| IP address | client_ip_address | Low |
| User agent | client_user_agent | Low |
| Click ID (fbc) | fbc | Highest |
| Browser ID (fbp) | fbp | High |

**Event Match Quality (EMQ) Targets:**

| EMQ Score | Status | Action |
|-----------|--------|--------|
| 8.0+ | Excellent | Maintain |
| 6.0-7.9 | Good | Minor improvements |
| 4.0-5.9 | Fair | Add customer parameters |
| <4.0 | Poor | Urgent: add email/phone |

#### Google Enhanced Conversions

**What it does:** Send hashed first-party data with conversion tags for better measurement.

**Setup Options:**

| Method | Requirements |
|--------|--------------|
| **Tag Manager** | GTM, data layer with user data |
| **gtag.js** | Manual implementation |
| **Google Ads API** | Server-side sending |

**Required Data:**
- Email (hashed SHA256)
- Phone number (hashed)
- Name (optional)
- Address (optional)

**Implementation Checklist:**
- [ ] Enable Enhanced Conversions in Google Ads
- [ ] Configure data layer to include user data
- [ ] Hash all PII before sending
- [ ] Verify setup with Tag Assistant
- [ ] Monitor in Diagnostics tab

#### TikTok Events API

**Setup Options:**
- Direct API integration
- Partner integrations (Shopify, etc.)
- GTM server-side container

**Key Parameters:**
- email (hashed)
- phone (hashed)
- external_id
- ttclid (click ID)
- ttp (pixel ID)

#### LinkedIn Conversions API

**Implementation:**
- Via LinkedIn Partner (Segment, mParticle)
- Direct API integration

**Match Keys:**
- email (SHA256)
- LinkedIn First-Party ID
- Google Click ID (for cross-platform)

### Deduplication Strategy

**Critical:** Sending both client-side and server-side events can cause double-counting.

| Platform | Deduplication Method |
|----------|---------------------|
| Meta | event_id matching |
| Google | transaction_id matching |
| TikTok | event_id matching |
| LinkedIn | conversion_id matching |

**Implementation:**
1. Generate unique event_id on client-side
2. Include same event_id in server-side call
3. Platform deduplicates automatically

---

## Part 4: Consent Mode v2 (Google)

### What is Consent Mode v2?

Consent Mode v2 is Google's framework that allows tags to adjust behavior based on user consent status, while still enabling conversion modeling for non-consented users. **Consent Mode v2 has been mandatory for EEA advertisers since March 2024.** Version 1 is no longer sufficient.

### What's New in v2 vs v1

Consent Mode v2 added two parameters on top of the original two:

| Parameter | Version | What It Controls | Default Without Consent |
|-----------|---------|------------------|------------------------|
| `ad_storage` | v1 | Advertising cookies | `denied` (no cookies) |
| `analytics_storage` | v1 | Analytics cookies | `denied` (no cookies) |
| `ad_user_data` | **v2 new** | Sending user data to Google for ads | `denied` |
| `ad_personalization` | **v2 new** | Personalized / remarketing ads | `denied` |

**Failing to implement `ad_user_data` and `ad_personalization` means:**
- Google may restrict audience list creation in the EEA
- Smart Bidding signals are degraded
- Remarketing audiences shrink

### Implementation Levels

| Level | Description | Data Recovery |
|-------|-------------|---------------|
| **Basic** | Block all tags when no consent | 0% |
| **Advanced** | Send cookieless pings, modeling enabled | 40-70% recovery |
| **Full** | Advanced + Enhanced Conversions | 70-85% recovery |

Use **Advanced** mode minimum. Basic mode gives up all recovery potential.

### Setup Checklist

- [ ] Confirm CMP supports Consent Mode v2 (most major CMPs updated in 2024)
- [ ] Configure all four consent mode parameters (not just the original two)
- [ ] Pass consent state to all Google tags via GTM or gtag.js
- [ ] Enable conversion modeling in Google Ads
- [ ] Test with Tag Assistant (check for v2 parameters in network requests)
- [ ] Monitor consent rates in GA4 (Admin > Privacy > Consent overview)

### Recommended CMP Providers

| Provider | Complexity | Best For |
|----------|-----------|----------|
| Cookiebot | Low | Small-medium sites |
| OneTrust | Medium | Enterprise |
| Usercentrics | Medium | EU focus |
| Osano | Low | US focus |
| Built-in (Shopify) | Low | Shopify stores |

---

## Part 5: Customer Data Platforms (CDPs)

### Do You Need a CDP?

**CDP Decision Matrix:**

| Factor | Yes, Get a CDP | No, Not Yet |
|--------|---------------|-------------|
| Data sources | 5+ systems | 1-3 systems |
| Customer records | 100K+ | <50K |
| Monthly ad spend | €50K+ | <€20K |
| Team size (marketing) | 5+ people | <3 people |
| Multi-channel campaigns | Yes | Single platform |
| Real-time needs | Yes | Batch OK |

### CDP Vendor Comparison

| CDP | Best For | Price Range | Complexity |
|-----|----------|-------------|------------|
| **Segment** | Developer-first, integrations | €€€ | Medium |
| **Rudderstack** | Open-source alternative | €€ | Medium |
| **mParticle** | Mobile-first | €€€ | Medium |
| **Treasure Data** | Enterprise | €€€€ | High |
| **Klaviyo** | E-commerce, email | € | Low |
| **Customer.io** | Messaging focus | €€ | Low |
| **Hightouch** | Data warehouse-first | €€ | Medium |

### CDP vs. Other Solutions

| Solution | Best For | Limitation |
|----------|----------|------------|
| **CDP** | Unified customer view + activation | Cost, complexity |
| **Data warehouse + Reverse ETL** | Analytics teams | No real-time |
| **Marketing automation** | Email/SMS | Limited identity resolution |
| **Platform audiences** | Single-platform campaigns | No cross-platform |

---

## Part 6: Data Activation for Advertising

### Audience Activation Workflow

```
1. COLLECT → First-party data (email, behavior, transactions)
2. UNIFY → Match to single customer profile
3. SEGMENT → Create audiences based on attributes
4. ACTIVATE → Push to ad platforms
5. MEASURE → Close the loop with conversion data
```

### Platform Audience Matching

| Platform | Upload Method | Match Rate (Email) | Best Practice |
|----------|--------------|-------------------|---------------|
| Meta Custom Audiences | Manager or API | 60-80% | SHA256 hash, normalize |
| Google Customer Match | UI or API | 50-70% | Multiple identifiers |
| TikTok Audiences | UI or API | 50-70% | Include phone |
| LinkedIn Matched Audiences | UI or API | 40-60% | Work email performs better |

### Audience Strategy Matrix

| Audience Type | Source | Platforms | Use Case |
|---------------|--------|-----------|----------|
| **Purchasers** | Transaction data | All | Exclusion, lookalikes |
| **High-value customers** | LTV data | All | Lookalikes, upsell |
| **Cart abandoners** | Behavior data | Meta, Google | Retargeting |
| **Email subscribers** | CRM | Meta, Google | Retargeting |
| **Website visitors** | Analytics | All | Retargeting |
| **App users** | App analytics | Meta, TikTok | Re-engagement |

### Lookalike & Expansion Audiences

> Note: Google Ads deprecated "Similar Audiences" in May 2023. Use Optimized Targeting (Display/YouTube) or PMax Audience Signals instead. Meta and TikTok still support Lookalike Audiences natively.

**Quality Factors (Meta/TikTok Lookalikes & Google Audience Signals):**

| Factor | Impact on Expansion Quality |
|--------|----------------------------|
| Source audience size | 1K-50K optimal |
| Source quality | Higher LTV → better expansion |
| Data recency | Last 90 days best |
| Country scope | Single country performs better |

---

## Part 7: Data Clean Rooms

### What Are Data Clean Rooms?

Secure environments where multiple parties can analyze combined data without exposing raw PII.

### Use Cases

| Use Case | How It Works |
|----------|--------------|
| **Publisher collaboration** | Match your data with publisher data |
| **Retailer insights** | Connect ad exposure to retail sales |
| **Attribution** | Cross-platform measurement |
| **Audience building** | Create segments from multiple sources |

### Data Clean Room Options

| Provider | Type | Best For |
|----------|------|----------|
| Google Ads Data Hub | Platform-specific | Google campaigns |
| Meta Advanced Analytics | Platform-specific | Meta campaigns |
| AWS Clean Rooms | Cloud-native | Custom use cases |
| Snowflake Data Clean Rooms | Data warehouse | Analytics teams |
| LiveRamp | Independent | Multi-platform |
| InfoSum | Independent | Privacy-first |

### When to Consider

- Ad spend > €500K/year
- Need offline conversion attribution
- Working with large publishers/retailers
- Complex multi-party data needs

---

## Part 8: Implementation Roadmap

### Phase 1: Foundation (Weeks 1-4)

**Priority Actions:**

| Action | Effort | Impact |
|--------|--------|--------|
| Implement server-side tracking (Meta CAPI) | Medium | High |
| Enable Google Enhanced Conversions | Low | Medium |
| Review and optimize CMP | Low | Medium |
| Audit current data collection | Low | Foundation |

**Quick Wins:**
- [ ] Add Meta CAPI via partner integration (Shopify/WooCommerce)
- [ ] Enable Enhanced Conversions in Google Ads
- [ ] Implement Consent Mode V2 with advanced mode
- [ ] Add email collection to key conversion points

### Phase 2: Enhancement (Weeks 5-12)

**Focus Areas:**

| Area | Actions |
|------|---------|
| **Data quality** | Improve EMQ scores, add phone numbers |
| **Consent optimization** | A/B test CMP messaging |
| **Audience building** | Create customer match audiences |
| **Cross-platform** | Implement TikTok/LinkedIn APIs |

### Phase 3: Optimization (Ongoing)

**Regular Activities:**

| Cadence | Activity |
|---------|----------|
| Weekly | Monitor EMQ scores, consent rates |
| Monthly | Review audience performance |
| Quarterly | Audit data collection, update strategy |
| Annually | Review CDP/tech stack needs |

---

## Part 9: Compliance Checklist

### GDPR Compliance for Advertising Data

| Requirement | Implementation |
|-------------|----------------|
| **Legal basis** | Consent or legitimate interest documented |
| **Transparency** | Privacy policy updated |
| **Consent** | CMP implemented, records stored |
| **Data minimization** | Only necessary data collected |
| **Purpose limitation** | Clear advertising purposes stated |
| **Storage limitation** | Retention periods defined |
| **Security** | Encryption, access controls |
| **Data subject rights** | Delete/export capabilities |

### Platform-Specific Requirements

| Platform | Key Requirements |
|----------|-----------------|
| Meta | GDPR consent signal, Terms of Service |
| Google | Consent Mode, EU user consent policy |
| TikTok | EEA consent documentation |
| LinkedIn | Member consent documentation |

---

## Part 10: Quick Reference

### Signal Recovery Cheat Sheet

| Problem | Solution | Recovery |
|---------|----------|----------|
| Low Meta EMQ | Add email + phone to CAPI | +30-50% match |
| Google modeling inaccurate | Enable Enhanced Conversions | +20-40% accuracy |
| Safari cookie loss | Server-side tracking | +60-80% recovery |
| Ad blocker impact | Server-side tracking | +25-40% recovery |
| Low consent rates | Optimize CMP messaging | +10-20% consent |

### Tech Stack Recommendations by Budget

| Annual Ad Spend | Recommended Stack |
|-----------------|-------------------|
| <€50K | Native platform tools + GTM |
| €50-200K | GTM Server + Basic CDP (Klaviyo) |
| €200K-1M | Full CDP (Segment) + clean room |
| €1M+ | Enterprise CDP + custom data infrastructure |

### KPIs to Track

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Meta EMQ Score | >6.0 | Events Manager |
| Consent rate | >50% | CMP dashboard |
| Customer match rate | >60% | Platform reports |
| Server-side coverage | >80% events | GTM Server |
| Modeled conversions % | <40% | Platform reports |

---

## Optional: Enrich with Live Data

If the user has connected their GA4 account, check current consent rate and data coverage to benchmark where first-party data collection stands today:

```python
# Assess session volume and key event data — gaps indicate consent/tracking issues
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="30daysAgo",
    end_date="today",
    metrics=["sessions", "totalUsers", "keyEvents"],
    dimensions=["date", "sessionDefaultChannelGroup"]
)
```

If you see significantly fewer sessions in GA4 than in your CMS/server logs, that gap represents unconsented or untracked users — the exact population the first-party data strategy needs to address. Use the ratio as the baseline "data loss rate" to track improvement against.

*Last updated: February 2026*
*Based on platform documentation and industry best practices*
