# Account Auditor — Detailed Reference

## Section 8: Unused Feature Detection

```
UNUSED FEATURES AUDIT
=====================
This section identifies money left on the table - features that are
available but not being used, representing optimization opportunities.

□ PERFORMANCE MAX (E-commerce Not Using?)
├── E-commerce account with Shopping feed but no PMax?
│   └── Potential: 15-30% more conversions across channels
├── PMax active but no Search themes configured?
│   └── Missing: Search coverage control
├── PMax active but weak audience signals?
│   └── Missing: Faster learning, better targeting
├── Asset groups not segmented (all products in one)?
│   └── Missing: Granular optimization
└── Score: [Optimized / Basic / Not Using]

□ ENHANCED CONVERSIONS (Enabled but Low Match?)
├── Enhanced Conversions enabled but match rate <70%?
│   └── Missing: Full attribution value
├── Only email sent? Phone/address not included?
│   └── Missing: Additional match signals
├── Server-side implementation not done?
│   └── Missing: Best match rates (vs tag-only)
├── Consent Mode v2 not implemented?
│   └── Risk: EU compliance, data loss
└── Score: [OK / Partial / Not Optimized]

□ AUDIENCE ASSETS (Created but Not Used?)
├── Customer Match lists uploaded but not active?
│   └── Wasted: First-party data not leveraged
├── Remarketing lists exist but no RLSA campaigns?
│   └── Wasted: Warm audiences not being targeted
├── Website visitors list exists but no Display remarketing?
│   └── Missing: Cross-network retargeting
├── Optimized Targeting disabled in Display/YouTube campaigns?
│   └── Missing: AI-driven audience expansion
├── Customer list for exclusions not set up?
│   └── Waste: Paying for existing customer clicks
└── Score: [Using All / Partial / Many Unused]

□ AD EXTENSIONS/ASSETS (Not Enabled?)
├── Sitelink extensions missing?
│   └── Missing: ~10-15% CTR lift
├── Callout extensions missing?
│   └── Missing: USP communication
├── Structured snippets missing?
│   └── Missing: Additional info
├── Image extensions not enabled (eligible accounts)?
│   └── Missing: Visual differentiation
├── Call extensions (if phone conversions matter)?
│   └── Missing: Direct response channel
├── Location extensions (if local business)?
│   └── Missing: Local presence
├── Price extensions (if applicable)?
│   └── Missing: Price transparency
├── Promotion extensions (if sales active)?
│   └── Missing: Promotion visibility
└── Score: [Full / Partial / Missing Many]

□ AUTOMATION & RULES (Not Configured?)
├── No automated rules for basic management?
│   └── Missing: Proactive alerts, less manual work
├── No scripts for advanced automation?
│   └── Missing: Custom optimization opportunities
├── No portfolio bid strategies (multi-campaign)?
│   └── Missing: Unified optimization across campaigns
├── Conversion value rules not configured?
│   └── Missing: Value-based optimization accuracy
├── Scheduled bid adjustments not set?
│   └── Missing: Time-of-day optimization
└── Score: [Using / Basic / None]

□ DEMAND GEN & YOUTUBE (Not Tested?)
├── E-commerce/Lead Gen but no Demand Gen campaigns?
│   └── Missing: YouTube, Discover, Gmail reach (replaces Discovery + Video Action)
├── Demand Gen with video assets tested?
│   └── Note: Video Action Campaigns merged into Demand Gen in 2025
├── YouTube Shorts ads via Demand Gen tested?
│   └── Missing: Vertical video format reach
├── YouTube remarketing not set up?
│   └── Missing: Video viewer retargeting
└── Score: [Using / Tested / None]

□ FEED OPTIMIZATION (Shopping/PMax)
├── Merchant Center promotions not used?
│   └── Missing: Promotional visibility
├── Custom labels not configured?
│   └── Missing: Granular bidding control
├── Product ratings not enabled?
│   └── Missing: Social proof in ads
├── Free listings not enabled?
│   └── Missing: Free organic traffic
├── Local inventory ads (if stores)?
│   └── Missing: O2O traffic
└── Score: [Optimized / Basic / Not Using]

□ MEASUREMENT TOOLS (Not Used?)
├── Experiments (A/B testing) not running?
│   └── Missing: Statistical testing framework
├── Bid simulator not reviewed?
│   └── Missing: Budget optimization insights
├── Recommendations review not regular?
│   └── Missing: Google's optimization suggestions
├── Attribution reports not analyzed?
│   └── Missing: Cross-channel journey insights
├── Auction insights not monitored?
│   └── Missing: Competitive intelligence
└── Score: [Using / Basic / None]

UNUSED FEATURES SCORE: ___/80 points

OPPORTUNITY COST ESTIMATE:
├── No PMax (e-commerce): ~15-30% fewer conversions
├── Low Enhanced Conversions adoption: ~10-20% attribution loss
├── Missing extensions: ~10-15% lower CTR
├── Unused audiences: ~15-25% efficiency loss
├── No automation: ~3-5 hours/week manual work
├── No Demand Gen/YouTube: ~20-40% of audience unreached
└── TOTAL ESTIMATED OPPORTUNITY: ___/month
```

## Google Ads Script: Account Health Monitor

```javascript
/**
 * Google Ads Account Health Monitor
 *
 * Runs weekly health check and sends report.
 *
 * Setup:
 * 1. Update EMAIL
 * 2. Adjust THRESHOLDS to your preferences
 * 3. Schedule weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Thresholds
  MIN_CTR: 0.02,           // 2% minimum CTR
  MAX_CPA_INCREASE: 0.25,  // 25% CPA increase = alert
  MIN_QUALITY_SCORE: 5,    // Quality Score minimum
  MIN_IMPRESSION_SHARE: 0.5, // 50% minimum IS
  MIN_AD_STRENGTH: 'GOOD'  // Minimum ad strength
};

function main() {
  var report = {
    date: new Date().toDateString(),
    accountName: AdsApp.currentAccount().getName(),
    issues: [],
    metrics: {},
    score: 0
  };

  // Run all checks
  checkConversions(report);
  checkCampaignStatus(report);
  checkKeywordQuality(report);
  checkAdStrength(report);
  checkImpressionShare(report);
  checkBudgetUtilization(report);

  // Calculate health score
  calculateHealthScore(report);

  // Send report
  sendHealthReport(report);

  Logger.log('Health check complete. Score: ' + report.score + '/100');
}

function checkConversions(report) {
  var stats = AdsApp.currentAccount().getStatsFor('LAST_7_DAYS');
  var conversions = stats.getConversions();
  var cost = stats.getCost();

  report.metrics.conversions7d = conversions;
  report.metrics.cost7d = cost;
  report.metrics.cpa7d = conversions > 0 ? cost / conversions : 0;

  var prevStats = AdsApp.currentAccount().getStatsFor('LAST_14_DAYS');
  var prevConv = prevStats.getConversions() - conversions;
  var prevCost = prevStats.getCost() - cost;
  var prevCPA = prevConv > 0 ? prevCost / prevConv : 0;

  if (prevCPA > 0 && report.metrics.cpa7d > 0) {
    var cpaChange = (report.metrics.cpa7d - prevCPA) / prevCPA;
    if (cpaChange > CONFIG.MAX_CPA_INCREASE) {
      report.issues.push({
        severity: 'HIGH',
        area: 'Performance',
        issue: 'CPA increased by ' + (cpaChange * 100).toFixed(1) + '%',
        action: 'Review bid strategies and targeting'
      });
    }
  }

  if (conversions === 0) {
    report.issues.push({
      severity: 'CRITICAL',
      area: 'Tracking',
      issue: 'Zero conversions in last 7 days',
      action: 'Verify conversion tracking immediately'
    });
  }
}

function checkCampaignStatus(report) {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var limitedCount = 0;
  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var stats = campaign.getStatsFor('LAST_7_DAYS');
    var budget = campaign.getBudget().getAmount();
    var spend = stats.getCost();
    var spendRatio = spend / (budget * 7);
    if (spendRatio > 0.95) {
      limitedCount++;
    }
  }

  if (limitedCount > 0) {
    report.issues.push({
      severity: 'MEDIUM',
      area: 'Budget',
      issue: limitedCount + ' campaign(s) may be limited by budget',
      action: 'Review budget allocation'
    });
  }
  report.metrics.limitedCampaigns = limitedCount;
}

function checkKeywordQuality(report) {
  var keywords = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .forDateRange('LAST_30_DAYS')
    .get();

  var totalKeywords = 0;
  var lowQSCount = 0;
  while (keywords.hasNext()) {
    var keyword = keywords.next();
    totalKeywords++;
    var qs = keyword.getQualityScore();
    if (qs && qs < CONFIG.MIN_QUALITY_SCORE) {
      lowQSCount++;
    }
  }

  report.metrics.totalKeywords = totalKeywords;
  report.metrics.lowQSKeywords = lowQSCount;

  var lowQSPercentage = totalKeywords > 0 ? lowQSCount / totalKeywords : 0;
  if (lowQSPercentage > 0.2) {
    report.issues.push({
      severity: 'MEDIUM',
      area: 'Keywords',
      issue: (lowQSPercentage * 100).toFixed(1) + '% of keywords have QS < 5',
      action: 'Improve ad relevance and landing pages'
    });
  }
}

function checkAdStrength(report) {
  var ads = AdsApp.ads()
    .withCondition('Type = RESPONSIVE_SEARCH_AD')
    .withCondition('Status = ENABLED')
    .get();
  var totalAds = 0;
  while (ads.hasNext()) { ads.next(); totalAds++; }
  report.metrics.totalAds = totalAds;
}

function checkImpressionShare(report) {
  var campaignIterator = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .withCondition('AdvertisingChannelType = SEARCH')
    .forDateRange('LAST_7_DAYS')
    .get();
  var count = 0;
  while (campaignIterator.hasNext()) { campaignIterator.next(); count++; }
  report.metrics.searchCampaigns = count;
}

function checkBudgetUtilization(report) {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .forDateRange('LAST_7_DAYS')
    .get();

  var totalBudget = 0;
  var totalSpend = 0;
  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var budget = campaign.getBudget().getAmount() * 7;
    var spend = campaign.getStatsFor('LAST_7_DAYS').getCost();
    totalBudget += budget;
    totalSpend += spend;
  }

  var utilization = totalBudget > 0 ? totalSpend / totalBudget : 0;
  report.metrics.budgetUtilization = utilization;

  if (utilization < 0.7) {
    report.issues.push({
      severity: 'LOW',
      area: 'Budget',
      issue: 'Budget utilization at ' + (utilization * 100).toFixed(1) + '%',
      action: 'Review targeting or increase bids'
    });
  }
}

function calculateHealthScore(report) {
  var score = 100;
  for (var i = 0; i < report.issues.length; i++) {
    switch (report.issues[i].severity) {
      case 'CRITICAL': score -= 25; break;
      case 'HIGH': score -= 15; break;
      case 'MEDIUM': score -= 10; break;
      case 'LOW': score -= 5; break;
    }
  }
  report.score = Math.max(0, score);
}

function sendHealthReport(report) {
  var subject = 'Account Health: ' + report.score + '/100 - ' + report.accountName;
  var body = 'GOOGLE ADS ACCOUNT HEALTH REPORT\n';
  body += '=================================\n\n';
  body += 'Account: ' + report.accountName + '\n';
  body += 'Date: ' + report.date + '\n';
  body += 'Health Score: ' + report.score + '/100\n\n';
  body += 'KEY METRICS (Last 7 Days)\n';
  body += '-------------------------\n';
  body += 'Conversions: ' + report.metrics.conversions7d + '\n';
  body += 'Cost: ' + report.metrics.cost7d.toFixed(2) + '\n';
  body += 'CPA: ' + report.metrics.cpa7d.toFixed(2) + '\n';
  body += 'Budget Utilization: ' + (report.metrics.budgetUtilization * 100).toFixed(1) + '%\n\n';

  if (report.issues.length > 0) {
    body += 'ISSUES FOUND (' + report.issues.length + ')\n';
    body += '-------------\n';
    for (var i = 0; i < report.issues.length; i++) {
      var issue = report.issues[i];
      body += '\n[' + issue.severity + '] ' + issue.area + '\n';
      body += 'Issue: ' + issue.issue + '\n';
      body += 'Action: ' + issue.action + '\n';
    }
  } else {
    body += 'No issues found!\n';
  }
  body += '\n---\nGenerated by Account Health Monitor';
  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Audit Report Template

```markdown
# Google Ads Account Audit Report

**Audit Date:** [DATE]
**Account:** [ACCOUNT NAME]
**Account ID:** [XXX-XXX-XXXX]
**Auditor:** [NAME]

---

## Executive Summary

### Health Score: [X]/420 ([X]%) - [STATUS]

**Strengths:**
1. [Strength with specific example]
2. [Strength with specific example]
3. [Strength with specific example]

**Critical Issues:**
1. [Critical] [Issue with impact]
2. [High] [Issue with impact]
3. [Medium] [Issue with impact]

**Estimated Wasted Spend:** [X]/month
**Potential Improvement:** [X-Y]% CPA reduction / ROAS increase

---

## Detailed Findings

### 1. Conversion Tracking & Data Quality
**Score:** [X]/50

| Check Item | Status | Notes |
|------------|--------|-------|
| Conversion Actions | OK | [Details] |
| Google Tag | OK | [Details] |
| Enhanced Conversions | Issues | [Details] |
| Data Quality | OK | [Details] |

**Issues:**
- [Issue 1]
- [Issue 2]

**Recommendations:**
1. [Recommendation with priority]
2. [Recommendation with priority]

---

### 2. Account Structure
**Score:** [X]/50

[Repeat format for each section]

---

## Prioritized Action Plan

### Week 1 (Critical)
- [ ] [Action 1 with responsible party]
- [ ] [Action 2 with responsible party]

### Week 2-3 (High)
- [ ] [Action 3]
- [ ] [Action 4]

### Month 1 (Medium)
- [ ] [Action 5]
- [ ] [Action 6]

### Ongoing (Low)
- [ ] [Action 7]
- [ ] [Action 8]

---

## Expected Impact

After implementing all recommendations:

| Metric | Current | Expected | Improvement |
|--------|---------|----------|-------------|
| CPA | [X] | [Y] | -[Z]% |
| ROAS | [X] | [Y] | +[Z]% |
| Conv Rate | [X]% | [Y]% | +[Z]% |
| Wasted Spend | [X] | [Y] | -[Z] |

---

## Follow-Up

**Next Audit Recommended:** [DATE]
**Review Meeting:** [DATE + TIME]
**Contact:** [EMAIL/PHONE]

---

*Report generated with Account Auditor Skill*
```
