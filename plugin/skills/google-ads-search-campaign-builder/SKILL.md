---
name: google-ads-search-campaign-builder
description: "This skill should be used when the user asks to \"build a Search campaign\", \"write RSA ad copy\", \"improve Ad Strength\", \"set up sitelinks and callouts\", or mentions \"lead generation campaign\", \"call extensions\", \"lead forms\", or \"search campaign structure\". Do NOT use for: Performance Max campaigns (use performance-max-optimizer), Shopping campaigns (use shopping-campaign-structure-advisor), bid strategy selection (use bid-strategy-selector)."
---
# Search Campaign Builder

Complete guide for setting up high-performance Google Ads Search campaigns specifically for lead generation with RSA best practices and full ad extensions setup.



## 2026 Updates: AI Max + Broad Match + Smart Bidding

### AI Max Search Campaign Type (2026)
AI Max is a new Search campaign subtype that combines RSA ad serving with expanded keyword matching powered by Google AI. Key differences from standard Search:

- Automatically matches to relevant queries beyond your keyword list
- Uses landing page and asset content to find additional traffic
- Requires: Smart Bidding (tCPA or Max Conversions), RSA with 8+ headlines
- URL expansion: Google may direct to most relevant landing page
- Best for: advertisers with strong conversion data who want to scale Search

To create an AI Max campaign, set `advertising_channel_sub_type = 'SEARCH_EXPRESS'` in API v23+. Note: `url_expansion_opt_out` was removed in v22; URL expansion control is now via `final_url_expansion_opt_out` at the campaign level.

### Broad Match + Smart Bidding (Google's 2026 Recommendation)
Google's official recommendation: use **broad match keywords paired with Smart Bidding** (tCPA or Max Conversions) rather than exact+phrase-heavy structures. Smart Bidding's signals prevent broad match from serving on irrelevant queries.

Decision guide:
- Account has <30 conversions/month: Start with exact+phrase, add broad later
- Account has 30-100 conversions/month: Mix phrase + broad with tCPA
- Account has >100 conversions/month: Broad match + tCPA is recommended, fewer ad groups needed

### GAQL: Audit Search Campaign Health

```sql
SELECT campaign.name, campaign.status, campaign.bidding_strategy_type,
    ad_group.name, metrics.impressions, metrics.clicks,
    metrics.cost_micros, metrics.conversions,
    metrics.search_impression_share, metrics.search_top_impression_share
FROM ad_group
WHERE campaign.advertising_channel_type = 'SEARCH'
AND campaign.status = 'ENABLED'
AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

```sql
-- Check search terms quality (match type performance)
SELECT campaign.name, search_term_view.search_term,
    search_term_view.status, segments.keyword.ad_group_criterion,
    metrics.impressions, metrics.clicks, metrics.conversions,
    metrics.cost_micros
FROM search_term_view
WHERE campaign.advertising_channel_type = 'SEARCH'
AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

## Campaign Structure for Lead Gen

### Recommended Account Structure

```
LEAD GEN ACCOUNT STRUCTURE
══════════════════════════

CAMPAIGN 1: Brand
├── Ad Group: Brand Exact
│   ├── [company name]
│   ├── [brand + service]
│   └── High bid, maximize conversions
├── Budget: 10-15% of total
└── Goal: Capture branded intent

CAMPAIGN 2: High-Intent Non-Brand
├── Ad Group: Service + Action
│   ├── "[service] request"
│   ├── "[service] quote"
│   └── "[service] contact"
├── Ad Group: Service + Urgency
│   ├── "[service] today"
│   ├── "[service] immediate"
│   └── "[service] now"
├── Budget: 50-60% of total
└── Goal: Qualified leads

CAMPAIGN 3: Research/Consideration
├── Ad Group: Service + Info
│   ├── "best [service]"
│   ├── "[service] comparison"
│   └── "how much does [service] cost"
├── Budget: 20-25% of total
└── Goal: Top-funnel leads

CAMPAIGN 4: Competitor
├── Ad Group: Competitor Names
│   ├── [competitor 1]
│   ├── [competitor 2] alternative
│   └── Strict negatives
├── Budget: 5-10% of total
└── Goal: Competitive conquest
```

### Ad Group Best Practices

```
AD GROUP SETUP FOR LEAD GEN
════════════════════════════

KEYWORDS PER AD GROUP:
──────────────────────
□ 10-20 keywords per ad group (STAG approach)
□ Same intent cluster
□ Same landing page
□ Same ad copy theme

MATCH TYPE STRATEGY (Lead Gen 2026):
───────────────────────────────────
┌──────────────────────────────────────────────────────────────────────┐
│ Match Type │ Budget % │ Use Case                                     │
├────────────┼──────────┼──────────────────────────────────────────────┤
│ Exact      │ 30-40%   │ Proven converting queries, brand terms       │
│ Phrase     │ 20-30%   │ Core service terms, medium accounts          │
│ Broad      │ 30-50%   │ Scale with Smart Bidding — Google's primary  │
│            │          │ recommendation for accounts >30 conv/month   │
└────────────┴──────────┴──────────────────────────────────────────────┘

LEAD GEN SPECIFIC:
├── Broad match REQUIRES tCPA or Max Conversions bidding (never manual)
├── Heavy negatives for quality regardless of match type
├── For accounts <30 conversions/month: stick to exact+phrase only
└── Focus on qualified leads, not CTR
```

## RSA Best Practices

### Responsive Search Ad Structure

```
RSA ANATOMY (2025)
══════════════════

HEADLINES (Max 15, Min 8):
──────────────────────────
Position 1 Headlines (Pin 2-3):
├── [Keyword] - [Primary Benefit]
├── [Service] Request | Direct Contact
└── "[Keyword]" + CTA

Position 2 Headlines (Pin 1-2):
├── [Key USP]
├── Free [Quote/Consultation/Demo]
└── [Social Proof]

Position 3+ Headlines (No Pin, let Google test):
├── Benefit statements
├── Trust signals
├── Urgency (where appropriate)
├── Location specific
└── CTA variations

DESCRIPTIONS (Max 4, Min 3):
────────────────────────────
Description 1 (Pin to position 1):
├── Keyword + primary value prop
├── Call-to-action
└── Max 90 chars for visibility

Description 2-4 (No pinning):
├── Social proof / testimonials
├── Process explanation
├── Trust signals
└── Secondary benefits

AD STRENGTH TARGETS:
────────────────────
□ "Excellent" = no guarantee of better performance
□ "Good" = sufficient, focus on conversions
□ Minimum "Average" = below this level action required
```

### Improving Ad Strength

```
AD STRENGTH OPTIMIZATION
═════════════════════════

"POOR" OR "AVERAGE" AD STRENGTH? CHECK:
────────────────────────────────────────

1. HEADLINE DIVERSITY
   □ Use all 15 headline slots
   □ Vary sentence structure
   □ Mix keywords, benefits, CTAs
   □ Avoid repetition

2. DESCRIPTION DIVERSITY
   □ Use all 4 description slots
   □ Each with unique message
   □ Different lengths

3. KEYWORD INCLUSION
   □ Keywords in minimum 3 headlines
   □ Keywords in minimum 1 description
   □ Natural fit, no keyword stuffing

4. UNIQUE SELLING POINTS
   □ Minimum 5 unique USPs incorporated
   □ Concrete numbers (30% discount, 1000+ customers)
   □ Differentiators vs competitors

QUICKLY IMPROVE AD STRENGTH:
────────────────────────────
□ Add "popular" headlines that Google suggests
□ Include prices/numbers
□ Add location headlines
□ Mix short and long headlines
```



## Ad Extensions Setup

### Required Extensions for Lead Gen

```
AD EXTENSIONS CHECKLIST (Lead Gen)
══════════════════════════════════

1. SITELINK EXTENSIONS [REQUIRED]
─────────────────────────────────
Minimum 4 sitelinks (max 8 for desktop):

Lead Gen Sitelinks:
├── "Request a Quote" → /quote
├── "Call Us Directly" → /contact (with phone number)
├── "Our Services" → /services
├── "About Us" → /about
├── "Reviews & References" → /reviews
├── "Free Consultation" → /consultation
├── "FAQ / Common Questions" → /faq
└── "Locations" → /locations

Sitelink Best Practices:
□ 25+ characters descriptions
□ Unique landing pages
□ Mobile-first thinking
□ Track sitelink conversions

2. CALLOUT EXTENSIONS [REQUIRED]
────────────────────────────────
Minimum 4 callouts (max 10):

Examples:
├── "Free Quote"
├── "Response Within 24 Hours"
├── "No Call-Out Fee"
├── "Certified"
├── "15+ Years Experience"
├── "Personal Advice"
├── "Custom Solutions"
├── "Flexible Hours"
├── "All-Inclusive Pricing"
└── "Satisfaction Guarantee"

3. STRUCTURED SNIPPETS [REQUIRED]
─────────────────────────────────
Choose relevant headers:

Services: [service 1], [service 2], [service 3]
Types: [type 1], [type 2], [type 3]
Brands: [brand 1], [brand 2], [brand 3] (if dealer)

4. CALL EXTENSIONS [CRITICAL FOR LEAD GEN]
──────────────────────────────────────────
□ Main phone number
□ Call tracking number (via Google Ads or third party)
□ Schedule: Only show during business hours
□ Mobile: Click-to-call prominent

5. LEAD FORM EXTENSIONS [OPTIONAL]
──────────────────────────────────
Native Google lead forms:
├── Low friction (no landing page needed)
├── Pre-filled with Google account data
├── Directly in search results
├── CRM integration (Zapier, native)

WARNING: Trade-off: Lower lead quality vs more volume
```

### Advanced Extension Setup

```
ADVANCED EXTENSIONS
═══════════════════

6. LOCATION EXTENSIONS
──────────────────────
□ Link Google Business Profile
□ Show distance in ads
□ Driving directions
□ Store visits tracking

7. PRICE EXTENSIONS
───────────────────
Ideal for services with fixed pricing:
├── "Consultation" - "From $99"
├── "Basic Package" - "$199/month"
├── "Premium Service" - "$499"
└── Link to relevant pages

8. IMAGE EXTENSIONS
───────────────────
□ Relevant product/service image
□ 1.91:1 aspect ratio
□ High quality, no text in image
□ A/B test different images

9. BUSINESS NAME & LOGO
────────────────────────
□ Automatically from Business Profile
□ Ensure correct branding
□ Logo meets guidelines

EXTENSION SCHEDULING:
─────────────────────
□ Call extensions: Business hours only
□ Sitelinks "Call Now": Office hours only
□ Urgency callouts: Specific days/times
```

## Lead Form Extensions Setup

### Native Lead Forms Configuration

```
LEAD FORM EXTENSION SETUP
══════════════════════════

WHEN TO USE:
────────────
Yes: Volume more important than quality
Yes: Simple lead capture (name, email, phone)
Yes: No complex qualification needed
Yes: Mobile-heavy traffic

WHEN NOT TO USE:
────────────────
No: Complex B2B with qualification questions
No: High-value leads needing nurturing
No: When landing page is part of the sales process

SETUP STEPS:
────────────
1. Campaign → Extensions → Lead Form
2. Choose form type:
   ├── More leads: Shorter form, more volume
   └── More qualified: Longer form, better quality

3. Configure fields:
   STANDARD FIELDS:
   ├── Name (always on)
   ├── Email (always on)
   ├── Phone number (optional)
   └── City/Postal code (optional)

   CUSTOM QUESTIONS (max 5):
   ├── "When do you need this service?"
   │   └── Options: Immediately, Within 1 month, 1-3 months, Later
   ├── "What is your budget?"
   │   └── Options: $1k-5k, $5k-10k, $10k+, Unknown
   └── "How can we help you?"
       └── Open text field

4. Headline & Description:
   └── "Get a free quote" + short value prop

5. Privacy policy URL:
   └── Required: link to privacy page

6. Submit button text:
   └── "Submit" or "Request"

7. Background image:
   └── Optional, increases engagement

LEAD DELIVERY:
──────────────
□ Webhook to CRM (real-time)
□ Email notification
□ Download CSV (manual)
□ Zapier integration
```

### Improving Lead Form Quality

```
LEAD FORM QUALITY OPTIMIZATION
═══════════════════════════════

PROBLEM: Poor lead quality

SOLUTIONS:
──────────

1. ADD QUALIFICATION QUESTIONS
   ├── Budget question filters tire-kickers
   ├── Timing question prioritizes hot leads
   └── Specific needs question shows serious intent

2. USE LONGER FORM VARIANT
   └── Google offers "More qualified" template

3. COMBINE WITH LANDING PAGE
   └── Lead form only for mobile
   └── Desktop to landing page

4. FAST FOLLOW-UP
   ├── Contact within 5 minutes = 21x higher connect rate
   ├── Webhook to sales team
   └── Auto-responder email

5. LEAD SCORING SETUP
   ├── Score based on answers
   ├── High-score leads = priority
   └── Low-score leads = nurturing track
```

## Call Tracking Setup

### Google Ads Call Tracking

```
CALL TRACKING IMPLEMENTATION
═════════════════════════════

OPTION 1: GOOGLE ADS CALL TRACKING (Free)
──────────────────────────────────────────
How it works:
├── Google replaces your number with a tracking number
├── Tracks calls as conversions
└── Limited: only clicks from ads

Setup:
1. Tools → Conversions → New conversion → Phone calls
2. Choose: "Calls from ads using call extensions"
3. Set call length threshold (often 60+ sec)
4. Link to campaigns

OPTION 2: WEBSITE CALL CONVERSIONS
───────────────────────────────────
Tracks calls from website (after ad click):
1. Tools → Conversions → "Calls from website"
2. Implement Google forwarding snippet
3. Dynamic number replacement
4. Tracked in full customer journey

OPTION 3: THIRD-PARTY CALL TRACKING
────────────────────────────────────
Tools: CallRail, CallTrackingMetrics, Infinity
Advantages:
├── Call recording
├── Call scoring/qualification
├── Multi-channel attribution
├── CRM integration
└── Keyword-level tracking

CALL CONVERSION SETTINGS:
─────────────────────────
□ Call length: 60+ seconds (lead gen)
□ Count: One (not every)
□ Attribution: Data-driven (if sufficient data)
□ Value: Average lead value
```

## Google Ads Script: Lead Gen Campaign Checker

```javascript
/**
 * Lead Gen Campaign Health Check Script
 *
 * Checks:
 * - Extension coverage
 * - Ad strength
 * - Conversion tracking
 * - Budget utilization
 *
 * Setup:
 * 1. Update CONFIG
 * 2. Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Thresholds
  MIN_SITELINKS: 4,
  MIN_CALLOUTS: 4,
  MIN_AD_STRENGTH: 'GOOD', // POOR, AVERAGE, GOOD, EXCELLENT
  MIN_CONVERSION_RATE: 0.02, // 2%

  // Date range
  DATE_RANGE: 'LAST_30_DAYS'
};

function main() {
  var report = {
    campaigns: [],
    issues: [],
    recommendations: []
  };

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignType = SEARCH')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var campaignReport = analyzeCampaign(campaign);
    report.campaigns.push(campaignReport);

    if (campaignReport.issues.length > 0) {
      report.issues = report.issues.concat(campaignReport.issues);
    }
  }

  // Generate recommendations
  report.recommendations = generateRecommendations(report);

  if (report.issues.length > 0) {
    sendReport(report);
  }

  Logger.log('Lead Gen Check Complete');
  Logger.log('Campaigns analyzed: ' + report.campaigns.length);
  Logger.log('Issues found: ' + report.issues.length);
}

function analyzeCampaign(campaign) {
  var name = campaign.getName();
  var issues = [];

  // Check Extensions
  var sitelinks = campaign.extensions().sitelinks().get();
  var sitelinkCount = 0;
  while (sitelinks.hasNext()) { sitelinks.next(); sitelinkCount++; }

  if (sitelinkCount < CONFIG.MIN_SITELINKS) {
    issues.push({
      campaign: name,
      type: 'EXTENSION',
      issue: 'Fewer than ' + CONFIG.MIN_SITELINKS + ' sitelinks (' + sitelinkCount + ')'
    });
  }

  var callouts = campaign.extensions().callouts().get();
  var calloutCount = 0;
  while (callouts.hasNext()) { callouts.next(); calloutCount++; }

  if (calloutCount < CONFIG.MIN_CALLOUTS) {
    issues.push({
      campaign: name,
      type: 'EXTENSION',
      issue: 'Fewer than ' + CONFIG.MIN_CALLOUTS + ' callouts (' + calloutCount + ')'
    });
  }

  // Check Call Extensions
  var hasCallExtension = false;
  try {
    var callExtensions = campaign.extensions().phoneNumbers().get();
    if (callExtensions.hasNext()) {
      hasCallExtension = true;
    }
  } catch (e) {}

  if (!hasCallExtension) {
    issues.push({
      campaign: name,
      type: 'EXTENSION',
      issue: 'No call extension active'
    });
  }

  // Check Ad Strength per Ad Group
  var adGroups = campaign.adGroups()
    .withCondition('Status = ENABLED')
    .get();

  while (adGroups.hasNext()) {
    var adGroup = adGroups.next();
    var ads = adGroup.ads()
      .withCondition('Type = RESPONSIVE_SEARCH_AD')
      .withCondition('Status = ENABLED')
      .get();

    while (ads.hasNext()) {
      var ad = ads.next();
      var rsa = ad.asType().responsiveSearchAd();
      var strength = rsa.getAdStrength();

      if (isWeakAdStrength(strength)) {
        issues.push({
          campaign: name,
          adGroup: adGroup.getName(),
          type: 'AD_STRENGTH',
          issue: 'RSA ad strength is ' + strength
        });
      }
    }
  }

  // Check Conversion Rate
  var stats = campaign.getStatsFor(CONFIG.DATE_RANGE);
  var clicks = stats.getClicks();
  var conversions = stats.getConversions();

  if (clicks > 100) {
    var convRate = conversions / clicks;
    if (convRate < CONFIG.MIN_CONVERSION_RATE) {
      issues.push({
        campaign: name,
        type: 'PERFORMANCE',
        issue: 'Conversion rate ' + (convRate * 100).toFixed(2) +
               '% is below target ' + (CONFIG.MIN_CONVERSION_RATE * 100) + '%'
      });
    }
  }

  return {
    name: name,
    sitelinks: sitelinkCount,
    callouts: calloutCount,
    hasCallExtension: hasCallExtension,
    conversions: conversions,
    clicks: clicks,
    issues: issues
  };
}

function isWeakAdStrength(strength) {
  var strengthOrder = ['POOR', 'AVERAGE', 'GOOD', 'EXCELLENT'];
  var minIndex = strengthOrder.indexOf(CONFIG.MIN_AD_STRENGTH);
  var currentIndex = strengthOrder.indexOf(strength);
  return currentIndex < minIndex;
}

function generateRecommendations(report) {
  var recommendations = [];

  var extensionIssues = report.issues.filter(function(i) {
    return i.type === 'EXTENSION';
  });

  if (extensionIssues.length > 0) {
    recommendations.push({
      priority: 'HIGH',
      action: 'Add missing extensions for better CTR and lead volume',
      campaigns: extensionIssues.length + ' campaigns affected'
    });
  }

  var adStrengthIssues = report.issues.filter(function(i) {
    return i.type === 'AD_STRENGTH';
  });

  if (adStrengthIssues.length > 0) {
    recommendations.push({
      priority: 'MEDIUM',
      action: 'Improve ad strength by adding more headline/description variation',
      campaigns: adStrengthIssues.length + ' ad groups affected'
    });
  }

  return recommendations;
}

function sendReport(report) {
  var subject = 'Lead Gen Campaign Check - ' + AdsApp.currentAccount().getName();
  var body = 'Lead Generation Campaign Health Check\n';
  body += '=====================================\n\n';

  body += 'CAMPAIGNS ANALYZED: ' + report.campaigns.length + '\n';
  body += 'ISSUES FOUND: ' + report.issues.length + '\n\n';

  if (report.issues.length > 0) {
    body += 'ISSUES:\n';
    body += '───────\n';

    for (var i = 0; i < report.issues.length; i++) {
      var issue = report.issues[i];
      body += '• ' + issue.campaign;
      if (issue.adGroup) body += ' / ' + issue.adGroup;
      body += '\n  ' + issue.issue + '\n\n';
    }
  }

  if (report.recommendations.length > 0) {
    body += 'RECOMMENDATIONS:\n';
    body += '────────────────\n';

    for (var j = 0; j < report.recommendations.length; j++) {
      var rec = report.recommendations[j];
      body += '[' + rec.priority + '] ' + rec.action + '\n';
      body += '  ' + rec.campaigns + '\n\n';
    }
  }

  body += '\n---\nGenerated by Lead Gen Campaign Checker Script';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
  Logger.log('Report sent to ' + CONFIG.EMAIL);
}
```

## Output: Search Campaign Setup Template

```markdown
# Search Campaign Setup Plan

## Campaign Overview
- **Business type:** [B2B/B2C/Local Service]
- **Target locations:** [Locations]
- **Monthly budget:** $[X]
- **Target CPL:** $[X]
- **Primary conversion:** [Form/Call/Lead Form]

## Campaign Structure

### Campaign 1: [Name]
**Type:** Search
**Bidding:** Target CPA / Maximize Conversions
**Daily budget:** $[X]

**Ad Groups:**
| Ad Group | Keywords (sample) | Match Types |
|----------|-------------------|-------------|
| [AG1] | [kw1], [kw2] | Exact, Phrase |
| [AG2] | [kw1], [kw2] | Phrase, Broad |

## RSA Setup

### Headlines (15):
1. [Keyword-focused headline - PIN position 1]
2. [Second keyword variation - PIN position 1]
3. [Primary benefit - PIN position 2]
4. [Social proof]
5-15. [Variations on benefits, CTAs, USPs]

### Descriptions (4):
1. [Keyword + value prop + CTA - PIN position 1]
2. [Trust + process]
3. [USPs + social proof]
4. [Urgency + secondary CTA]

## Extensions Checklist
- [ ] 6+ Sitelinks configured
- [ ] 6+ Callouts added
- [ ] Structured Snippets (2 types)
- [ ] Call Extension active
- [ ] Location Extension linked
- [ ] Lead Form Extension (optional)
- [ ] Image Extensions added

## Conversion Tracking
- [ ] Form submission tracking
- [ ] Call tracking enabled (60+ sec)
- [ ] Lead form webhook configured
- [ ] Value per conversion set

## Launch Checklist
- [ ] All ads reviewed for spelling/accuracy
- [ ] Landing pages mobile-optimized
- [ ] Negative keyword lists applied
- [ ] Budget and bids confirmed
- [ ] Conversion tracking verified
```

## Optional: Enrich with Live Data

If the user has connected their Google Ads account, check for existing campaigns before building new ones to avoid duplication and surface relevant performance history:

```python
# List active search campaigns with budget, status, and recent performance
google_ads_run_gaql(
    customer_id="YOUR_CUSTOMER_ID",
    query="SELECT campaign.name, campaign.status, campaign.advertising_channel_type, campaign_budget.amount_micros, metrics.impressions, metrics.clicks, metrics.conversions, metrics.cost_micros FROM campaign WHERE campaign.advertising_channel_type = 'SEARCH' AND campaign.status != 'REMOVED' AND segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC LIMIT 20"
)
```

Use this to understand the existing campaign structure, identify budget already allocated to search, and avoid duplicating keyword coverage. Existing high-performing campaigns may only need RSA copy improvements rather than a full rebuild.
