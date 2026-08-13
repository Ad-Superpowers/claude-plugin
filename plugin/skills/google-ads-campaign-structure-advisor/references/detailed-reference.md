# Campaign Structure Advisor — Detailed Reference

## Google Ads Script: Structure Analyzer

```javascript
/**
 * Account Structure Analyzer
 *
 * Analyzes account structure and provides recommendations
 * for consolidation and optimization.
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Run manually or schedule monthly
 */

var CONFIG = {
  EMAIL: 'you@example.com',
  DATE_RANGE: 'LAST_30_DAYS',
  MIN_CONVERSIONS_PER_CAMPAIGN: 30,
  MIN_CONVERSIONS_PER_ADGROUP: 5,
  MAX_KEYWORDS_PER_ADGROUP: 30,
  MIN_KEYWORDS_PER_ADGROUP: 3
};

function main() {
  var report = {
    overview: {},
    consolidationCandidates: [],
    structureIssues: [],
    recommendations: []
  };

  report.overview = getAccountOverview();

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var analysis = analyzeCampaign(campaign);
    if (analysis.isConsolidationCandidate) {
      report.consolidationCandidates.push(analysis);
    }
    report.structureIssues = report.structureIssues.concat(analysis.issues);
  }

  report.recommendations = generateStructureRecommendations(report);
  sendStructureReport(report);
}

function getAccountOverview() {
  var stats = AdsApp.currentAccount().getStatsFor(CONFIG.DATE_RANGE);
  var campaigns = AdsApp.campaigns().withCondition('Status = ENABLED').get();
  var adGroups = AdsApp.adGroups().withCondition('Status = ENABLED').get();
  var keywords = AdsApp.keywords().withCondition('Status = ENABLED').get();

  var campaignCount = 0;
  while (campaigns.hasNext()) { campaigns.next(); campaignCount++; }
  var adGroupCount = 0;
  while (adGroups.hasNext()) { adGroups.next(); adGroupCount++; }
  var keywordCount = 0;
  while (keywords.hasNext()) { keywords.next(); keywordCount++; }

  return {
    campaigns: campaignCount,
    adGroups: adGroupCount,
    keywords: keywordCount,
    conversions: stats.getConversions(),
    cost: stats.getCost(),
    avgConvPerCampaign: stats.getConversions() / Math.max(campaignCount, 1),
    avgKeywordsPerAdGroup: keywordCount / Math.max(adGroupCount, 1)
  };
}

function analyzeCampaign(campaign) {
  var name = campaign.getName();
  var stats = campaign.getStatsFor(CONFIG.DATE_RANGE);
  var conversions = stats.getConversions();
  var cost = stats.getCost();

  var analysis = {
    name: name, conversions: conversions, cost: cost,
    adGroups: 0, keywords: 0,
    isConsolidationCandidate: false, issues: []
  };

  var adGroups = campaign.adGroups().withCondition('Status = ENABLED').get();
  while (adGroups.hasNext()) {
    var adGroup = adGroups.next();
    analysis.adGroups++;
    var keywords = adGroup.keywords().withCondition('Status = ENABLED').get();
    var kwCount = 0;
    while (keywords.hasNext()) { keywords.next(); kwCount++; analysis.keywords++; }

    if (kwCount > CONFIG.MAX_KEYWORDS_PER_ADGROUP) {
      analysis.issues.push({
        campaign: name, adGroup: adGroup.getName(),
        type: 'TOO_MANY_KEYWORDS',
        detail: kwCount + ' keywords (max ' + CONFIG.MAX_KEYWORDS_PER_ADGROUP + ')'
      });
    }
    if (kwCount === 1) {
      analysis.issues.push({
        campaign: name, adGroup: adGroup.getName(),
        type: 'SKAG_DETECTED',
        detail: 'Single keyword ad group - consider consolidating'
      });
    }
  }

  if (conversions < CONFIG.MIN_CONVERSIONS_PER_CAMPAIGN && cost > 0) {
    analysis.isConsolidationCandidate = true;
    analysis.consolidationReason = 'Low conversion volume (' + conversions.toFixed(0) + '/month)';
  }
  return analysis;
}

function generateStructureRecommendations(report) {
  var recs = [];
  var skagCount = report.structureIssues.filter(function(i) {
    return i.type === 'SKAG_DETECTED';
  }).length;

  if (skagCount > 10) {
    recs.push({
      priority: 'HIGH', category: 'SKAG_MIGRATION',
      action: skagCount + ' SKAGs detected. Migrate to themed ad groups.',
      impact: 'Improved Smart Bidding performance, easier management'
    });
  }

  if (report.consolidationCandidates.length > 2) {
    var totalConv = report.consolidationCandidates.reduce(function(sum, c) {
      return sum + c.conversions;
    }, 0);
    recs.push({
      priority: 'HIGH', category: 'CONSOLIDATION',
      action: 'Consolidate ' + report.consolidationCandidates.length +
              ' low-volume campaigns (' + totalConv.toFixed(0) + ' total conv/month)',
      impact: 'Faster learning, better optimization'
    });
  }

  if (report.overview.campaigns > 20 && report.overview.avgConvPerCampaign < 50) {
    recs.push({
      priority: 'MEDIUM', category: 'SIMPLIFICATION',
      action: 'Account has ' + report.overview.campaigns + ' campaigns with avg ' +
              report.overview.avgConvPerCampaign.toFixed(0) + ' conv/campaign',
      impact: 'Consider reducing campaign count for better data aggregation'
    });
  }
  return recs;
}

function sendStructureReport(report) {
  var subject = 'Account Structure Analysis - ' + AdsApp.currentAccount().getName();
  var body = 'Account Structure Analysis Report\n==================================\n\n';
  body += 'ACCOUNT OVERVIEW:\n';
  body += 'Campaigns: ' + report.overview.campaigns + '\n';
  body += 'Ad Groups: ' + report.overview.adGroups + '\n';
  body += 'Keywords: ' + report.overview.keywords + '\n';
  body += 'Avg conversions/campaign: ' + report.overview.avgConvPerCampaign.toFixed(1) + '\n';
  body += 'Avg keywords/ad group: ' + report.overview.avgKeywordsPerAdGroup.toFixed(1) + '\n\n';

  if (report.consolidationCandidates.length > 0) {
    body += 'CONSOLIDATION CANDIDATES:\n';
    for (var i = 0; i < report.consolidationCandidates.length; i++) {
      var c = report.consolidationCandidates[i];
      body += '- ' + c.name + ': Conv: ' + c.conversions.toFixed(0) + ' | ' + c.consolidationReason + '\n';
    }
    body += '\n';
  }

  if (report.structureIssues.length > 0) {
    body += 'STRUCTURE ISSUES (first 20):\n';
    var issuesToShow = report.structureIssues.slice(0, 20);
    for (var j = 0; j < issuesToShow.length; j++) {
      var issue = issuesToShow[j];
      body += '- [' + issue.type + '] ' + issue.campaign;
      if (issue.adGroup) body += ' / ' + issue.adGroup;
      body += '\n  ' + issue.detail + '\n';
    }
    body += '\n';
  }

  if (report.recommendations.length > 0) {
    body += 'RECOMMENDATIONS:\n';
    for (var k = 0; k < report.recommendations.length; k++) {
      var rec = report.recommendations[k];
      body += '[' + rec.priority + '] ' + rec.category + '\n';
      body += 'Action: ' + rec.action + '\n';
      body += 'Impact: ' + rec.impact + '\n\n';
    }
  }

  body += '\n---\nGenerated by Account Structure Analyzer';
  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Enterprise Account Structure

### Multi-Product/Region Accounts

```
ENTERPRISE ACCOUNT ARCHITECTURE
════════════════════════════════

ORGANIZATION PRINCIPLES:
────────────────────────

1. CAMPAIGN = BUDGET ALLOCATION UNIT
   └── Separate campaigns for separate budgets
   └── Not: Separate campaigns for organization

2. LABELS = ORGANIZATION
   └── Product lines
   └── Teams/ownership
   └── Initiatives
   └── Reporting groups

3. MCC FOR TRUE SEPARATION
   └── Different business units
   └── Different billing
   └── Compliance requirements

STRUCTURE EXAMPLE:
──────────────────

Large E-commerce (3 product lines, 2 regions):

Account
├── Campaign: NL - Brand Search
│   ├── Labels: [Netherlands] [Brand]
│   └── All product lines (shared brand)
│
├── Campaign: NL - Electronics Search
│   ├── Labels: [Netherlands] [Electronics] [Non-Brand]
│   ├── Ad Groups: TVs, Laptops, Phones
│   └── Bidding: tROAS 400%
│
├── Campaign: NL - Home & Living Search
│   ├── Labels: [Netherlands] [Home] [Non-Brand]
│   ├── Ad Groups: Furniture, Decor, Kitchen
│   └── Bidding: tROAS 350%
│
├── Campaign: NL - Performance Max
│   ├── Labels: [Netherlands] [Full-funnel]
│   ├── Asset Groups: Per category
│   └── All products feed
│
├── Campaign: BE - Brand Search
│   ├── Labels: [Belgium] [Brand]
│   └── Belgian brand terms
│
├── Campaign: BE - Non-Brand (Combined)
│   ├── Labels: [Belgium] [Non-Brand]
│   └── Smaller market = combined
│
└── Campaign: Retargeting (All regions)
    ├── Labels: [Remarketing] [Cross-region]
    └── Shared audiences
```

### Budget & Target Hierarchies

```
BUDGET HIERARCHY
════════════════

LEVEL 1: ACCOUNT TOTAL
──────────────────────
= Total monthly budget for all advertising

Allocation to:
├── Per market/region
├── Per business unit
└── Per objective

LEVEL 2: CAMPAIGN GROUPS
────────────────────────
= Grouped campaigns with shared budget

Example:
├── Brand Protection: $5,000/month
│   └── Campaigns: NL Brand, BE Brand
│
├── Volume Drivers: $30,000/month
│   └── Campaigns: NL Non-Brand, BE Non-Brand, PMax
│
└── Efficiency Focus: $15,000/month
    └── Campaigns: High-ROAS campaigns

LEVEL 3: INDIVIDUAL CAMPAIGNS
─────────────────────────────
= Daily budgets per campaign

Setting:
├── Standard: Even spread over month
├── Accelerated: Spend as fast as possible (riskier)
└── Shared: Pool budget over campaigns

TARGET HIERARCHY:
─────────────────

Account Target:
├── Blended ROAS: 380%
└── Blended CPA: N/A (e-commerce)

Campaign Targets:
├── Brand: ROAS 800% (low cost, high return)
├── Non-Brand: ROAS 350% (acquisition)
├── Retargeting: ROAS 500% (warm audience)
└── PMax: ROAS 400% (blended)

Ad Group Targets:
└── Inherited from campaign (Smart Bidding)
```
