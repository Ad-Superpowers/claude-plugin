---
name: landing-page-optimization-guide
description: "This skill should be used when the user asks to \"optimize my landing page\", \"improve conversion rate\", \"audit my landing page for CRO\", mentions \"message match between ads and pages\", \"high bounce rate on paid traffic\", or \"A/B test prioritization\". Do NOT use for: ad creative optimization (use platform-specific creative/fatigue skills), channel selection (use channel-selection-framework), or tracking/pixel implementation (use first-party-data-strategy or gtm-container-auditor)."
---
# Landing Page Optimization Guide for Paid Traffic

## Purpose

Help advertisers optimize landing pages specifically for paid traffic. Ad-driven visitors have different expectations and behaviors than organic traffic - this guide addresses those unique needs.

## When to Use This Skill

Invoke when user mentions:
- **Landing page optimization:** "How do I improve my landing page?"
- **Conversion rate:** "My conversion rate is low"
- **CRO audit:** "Can you review my landing page?"
- **Message match:** "My ads and page don't align"
- **Bounce rate:** "People leave without converting"
- **A/B testing:** "What should I test on my landing page?"

---


> Full scoring rubric and detailed examples: `references/detailed-reference.md` | Industry benchmarks: `references/benchmarks.md`

## The Landing Page Scorecard (100 Points)

### Scoring Categories

| Category | Points | Why It Matters |
|----------|--------|----------------|
| Message Match | 20 | Aligns ad promise with page delivery |
| Value Proposition | 20 | Clear, compelling reason to act |
| Trust & Credibility | 15 | Reduces perceived risk |
| CTA Effectiveness | 15 | Drives the actual conversion |
| Form Optimization | 10 | Removes friction from conversion |
| Mobile Experience | 10 | Where 60%+ of traffic comes from |
| Technical Performance | 10 | Speed and tracking |

### Quick Scoring Guide

```
MESSAGE MATCH (20 pts)
├── Headline reflects ad copy: 0-5
├── Offer matches ad promise: 0-5
├── Visual continuity (colors, images): 0-5
└── Same tone/language as ad: 0-5

VALUE PROPOSITION (20 pts)
├── Clear benefit in headline: 0-5
├── Specific (numbers, outcomes): 0-5
├── Differentiated from competitors: 0-5
└── Addresses user pain point: 0-5

TRUST & CREDIBILITY (15 pts)
├── Social proof (testimonials, reviews): 0-5
├── Trust badges (security, guarantees): 0-5
└── Authority signals (logos, certifications): 0-5

CTA EFFECTIVENESS (15 pts)
├── Visible without scrolling: 0-5
├── Action-oriented text (not "Submit"): 0-5
└── Contrasting design, stands out: 0-5

FORM OPTIMIZATION (10 pts)
├── Minimal fields (only essentials): 0-5
└── Clear labels, no friction: 0-5

MOBILE EXPERIENCE (10 pts)
├── Responsive, readable, tap-friendly: 0-5
└── Fast load, no horizontal scroll: 0-5

TECHNICAL (10 pts)
├── Page speed < 3 seconds: 0-5
└── Tracking working (pixels, events): 0-5

SCORE INTERPRETATION:
├── 80-100: Excellent — minor tweaks only
├── 60-79: Good — 2-3 improvements needed
├── 40-59: Needs work — significant gaps
└── 0-39: Critical — major overhaul needed
```

### Industry Conversion Benchmarks

| Industry | Search Avg | Display Avg | Social Avg | Top 25% |
|----------|-----------|-------------|------------|---------|
| E-commerce | 2.5% | 0.8% | 1.5% | 5.0%+ |
| SaaS/B2B | 3.0% | 0.5% | 2.0% | 7.0%+ |
| Finance | 4.5% | 0.6% | 1.2% | 9.0%+ |
| Healthcare | 3.5% | 0.5% | 1.0% | 6.5%+ |
| Legal | 5.0% | 0.8% | 1.5% | 10.0%+ |
| Real Estate | 3.0% | 0.4% | 1.0% | 6.0%+ |
| Education | 4.0% | 0.5% | 2.5% | 8.0%+ |

---

## Quick Audit Framework

### 30-Second Audit

Look at the page for 5 seconds, then answer:
1. What does this company sell? □ Clear □ Unclear
2. Why should I care? □ Compelling □ Generic
3. What should I do next? □ Obvious □ Hidden
4. Do I trust them? □ Yes □ Unsure

### Common Issues Quick Fixes

| Issue | Quick Fix | Impact |
|-------|-----------|--------|
| No above-fold CTA | Move CTA up | High |
| Generic headline | Add specific benefit | High |
| No social proof | Add testimonial | Medium |
| Too many form fields | Remove 2-3 fields | High |
| No visual hierarchy | Add whitespace, sizing | Medium |
| Slow loading | Compress images | High |
| "Submit" button | Change to value-oriented | Medium |

### A/B Test Prioritization (PIE Framework)

```
PRIORITIZE TESTS USING PIE:
├── P (Potential): How much improvement is possible? (1-10)
├── I (Importance): How valuable is this page/traffic? (1-10)
├── E (Ease): How easy is this to implement? (1-10)
└── Score = (P + I + E) / 3

HIGH PRIORITY (PIE > 7):
├── Headline changes on high-traffic pages
├── CTA button text/color on conversion pages
├── Form field reduction on lead gen pages

MEDIUM PRIORITY (PIE 4-7):
├── Social proof placement
├── Image/video changes
├── Page layout restructuring

LOW PRIORITY (PIE < 4):
├── Footer changes
├── Minor copy edits
├── Color scheme changes
```

---

## Landing Page Templates

### Lead Gen Template Structure

```
1. HEADER (minimal)
   - Logo only, no navigation

2. HERO SECTION
   - Headline (specific benefit)
   - Subheadline (how/what)
   - Form (right side or below)
   - CTA button

3. TRUST BAR
   - Client logos or "As seen in"
   - Review score

4. BENEFITS SECTION
   - 3 key benefits with icons
   - Benefit-focused, not feature-focused

5. SOCIAL PROOF
   - 2-3 testimonials with photos
   - Specific results mentioned

6. FAQ (optional)
   - Address main objections

7. FINAL CTA
   - Repeat the form or CTA
   - Add urgency or guarantee
```

### E-commerce Product Template Structure

```
1. HEADER
   - Logo, search, cart (minimal)

2. PRODUCT HERO
   - High-quality images/video
   - Product title
   - Price (with discount if applicable)
   - Add to cart CTA

3. TRUST ELEMENTS
   - Star rating
   - Review count
   - Security badges

4. PRODUCT DETAILS
   - Key features/benefits
   - Specifications

5. SOCIAL PROOF
   - Customer reviews
   - UGC photos

6. RELATED/UPSELL
   - "Complete the look"
   - "Customers also bought"

7. STICKY ADD TO CART
   - Mobile: sticky bottom bar
   - Desktop: sticky sidebar
```

---

## Output: Landing Page Audit Template

```markdown
# Landing Page Audit Report

## Page Details
- **URL:** [URL]
- **Traffic source:** [Google Ads / Meta / LinkedIn / etc.]
- **Current conversion rate:** [X]%
- **Industry benchmark:** [X]%

## Scorecard Results

| Category | Score | Max | Notes |
|----------|-------|-----|-------|
| Message Match | /20 | 20 | |
| Value Proposition | /20 | 20 | |
| Trust & Credibility | /15 | 15 | |
| CTA Effectiveness | /15 | 15 | |
| Form Optimization | /10 | 10 | |
| Mobile Experience | /10 | 10 | |
| Technical | /10 | 10 | |
| **TOTAL** | **/100** | **100** | |

## Top 3 Issues (Highest Impact)
1. **[Issue]** — [Fix] — Expected impact: [High/Medium]
2. **[Issue]** — [Fix] — Expected impact: [High/Medium]
3. **[Issue]** — [Fix] — Expected impact: [High/Medium]

## A/B Test Recommendations
| Test | PIE Score | Priority |
|------|-----------|----------|
| [Test 1] | [X] | [High/Med/Low] |
| [Test 2] | [X] | [High/Med/Low] |
| [Test 3] | [X] | [High/Med/Low] |
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, pull landing page performance data to identify which pages need the most attention:

```python
# Get landing page performance: sessions, bounce rate, and conversion rate per page
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="30daysAgo",
    end_date="today",
    metrics=["sessions", "bounceRate", "keyEvents", "averageSessionDuration"],
    dimensions=["landingPage"]
)
```

Sort by `sessions DESC` to find high-traffic pages with poor `keyEvents` or high `bounceRate` — these are your highest-impact optimisation targets. Pages with <30s session duration + high bounce = above-the-fold messaging failing immediately.
