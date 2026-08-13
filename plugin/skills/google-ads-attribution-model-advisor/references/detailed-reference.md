## Google Ads Script: Attribution Analyzer

```javascript
/**
 * Attribution Model Comparison Analyzer
 *
 * Analyzes differences between Last Click and Data-Driven Attribution
 * for budget allocation optimization.
 *
 * Note: This script uses Search Query Report data as a proxy,
 * actual DDA data is only available via the UI.
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',
  DATE_RANGE: 'LAST_30_DAYS',

  // Threshold for significant differences (20% = 0.20)
  SIGNIFICANCE_THRESHOLD: 0.20,

  // Minimum conversions for analysis
  MIN_CONVERSIONS: 5
};

function main() {
  var report = {
    summary: {},
    campaigns: [],
    recommendations: []
  };

  // Analyze campaign performance
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var totalConversions = 0;
  var campaignData = [];

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var stats = campaign.getStatsFor(CONFIG.DATE_RANGE);
    var conversions = stats.getConversions();
    var cost = stats.getCost();
    var clicks = stats.getClicks();

    if (conversions >= CONFIG.MIN_CONVERSIONS) {
      var data = {
        name: campaign.getName(),
        type: getCampaignType(campaign.getName()),
        conversions: conversions,
        cost: cost,
        cpa: cost / conversions,
        clicks: clicks
      };

      // Estimate assisted conversions (proxy via search terms)
      data.assistedRatio = estimateAssistedRatio(campaign);
      data.estimatedTotalValue = conversions * (1 + data.assistedRatio);

      campaignData.push(data);
      totalConversions += conversions;
    }
  }

  report.summary = {
    totalCampaigns: campaignData.length,
    totalConversions: totalConversions,
    ddaEligible: totalConversions >= 600
  };

  // Identify opportunities
  report.campaigns = campaignData.sort(function(a, b) {
    return b.assistedRatio - a.assistedRatio;
  });

  // Generate recommendations
  report.recommendations = generateRecommendations(report);

  sendReport(report);
  Logger.log('Attribution analysis complete');
}

function getCampaignType(name) {
  var nameLower = name.toLowerCase();
  if (nameLower.indexOf('brand') > -1) return 'Brand';
  if (nameLower.indexOf('display') > -1) return 'Display';
  if (nameLower.indexOf('video') > -1 || nameLower.indexOf('youtube') > -1) return 'Video';
  if (nameLower.indexOf('shopping') > -1 || nameLower.indexOf('pmax') > -1) return 'Shopping/PMax';
  return 'Generic Search';
}

function estimateAssistedRatio(campaign) {
  // This is a proxy - actual assisted data not available via API
  // Estimation based on campaign type
  var name = campaign.getName().toLowerCase();

  if (name.indexOf('display') > -1) return 0.8;
  if (name.indexOf('video') > -1 || name.indexOf('youtube') > -1) return 1.2;
  if (name.indexOf('brand') > -1) return 0.1;
  if (name.indexOf('shopping') > -1 || name.indexOf('pmax') > -1) return 0.3;
  return 0.4; // Generic search
}

function generateRecommendations(report) {
  var recs = [];

  // Check DDA eligibility
  if (!report.summary.ddaEligible) {
    recs.push({
      priority: 'INFO',
      action: 'Account has < 600 conversions/month. DDA not yet available.',
      detail: 'Consider Time Decay or Position Based as an alternative.'
    });
  } else {
    recs.push({
      priority: 'HIGH',
      action: 'Account qualifies for Data-Driven Attribution.',
      detail: 'Activate DDA for more accurate budget allocation.'
    });
  }

  // Check for high assisted ratio campaigns
  var highAssisted = report.campaigns.filter(function(c) {
    return c.assistedRatio > 0.5 && c.type !== 'Brand';
  });

  if (highAssisted.length > 0) {
    recs.push({
      priority: 'MEDIUM',
      action: highAssisted.length + ' campaigns are possibly undervalued with Last Click.',
      detail: 'Consider budget increase for: ' +
              highAssisted.slice(0, 3).map(function(c) { return c.name; }).join(', ')
    });
  }

  return recs;
}

function sendReport(report) {
  var subject = 'Attribution Analysis - ' + AdsApp.currentAccount().getName();
  var body = 'Attribution Model Analysis Report\n';
  body += '=================================\n\n';

  body += 'SUMMARY:\n';
  body += '• Total campaigns analyzed: ' + report.summary.totalCampaigns + '\n';
  body += '• Total conversions: ' + report.summary.totalConversions + '\n';
  body += '• DDA eligible: ' + (report.summary.ddaEligible ? 'Yes' : 'No (need 600+)') + '\n\n';

  body += 'CAMPAIGN ANALYSIS (by estimated assisted value):\n';
  body += '────────────────────────────────────────────────\n';

  var topCampaigns = report.campaigns.slice(0, 10);
  for (var i = 0; i < topCampaigns.length; i++) {
    var c = topCampaigns[i];
    body += '• ' + c.name + '\n';
    body += '  Type: ' + c.type + ' | Conv: ' + c.conversions.toFixed(0);
    body += ' | Est. Assisted Ratio: ' + (c.assistedRatio * 100).toFixed(0) + '%\n';
  }

  body += '\nRECOMMENDATIONS:\n';
  body += '────────────────\n';

  for (var j = 0; j < report.recommendations.length; j++) {
    var rec = report.recommendations[j];
    body += '[' + rec.priority + '] ' + rec.action + '\n';
    body += '  → ' + rec.detail + '\n\n';
  }

  body += '\n---\nGenerated by Attribution Analyzer Script';
  body += '\nNote: Assisted ratios are estimates. Check UI for actual DDA data.';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Recommended Attribution Model
**[MODEL NAME]**

### Why This Model
1. [Reason 1 - based on data volumes]
2. [Reason 2 - based on business type]
3. [Reason 3 - based on channel mix]

### Expected Impact per Campaign Type

| Campaign Type | Current Conv | Expected (new model) | Difference |
|---------------|--------------|----------------------|------------|
| Brand Search  | [X]          | [X]                  | [%]        |
| Generic Search| [X]          | [X]                  | [%]        |
| Display       | [X]          | [X]                  | [%]        |
| Shopping      | [X]          | [X]                  | [%]        |

### Implementation Plan

**Week 1: Preparation**
- Document baseline metrics
- Calculate new ROAS/CPA targets
- Communicate with stakeholders

**Week 2: Activation**
- Change attribution model in Google Ads
- Update conversion action settings
- Monitor daily

**Week 3-4: Evaluation**
- Compare pre/post metrics
- Analyze Smart Bidding impact
- Fine-tune targets

### Lookback Window Recommendation
- **Click-through:** [X] days
- **View-through:** [X] days
- **Engaged-view:** [X] days

### Cross-Channel Integration
- [ ] GA4 linked to Google Ads
- [ ] Import GA4 conversions (if desired)
- [ ] Cross-device tracking enabled
- [ ] Enhanced conversions active

### Monitoring Dashboard Setup
□ Model comparison report (weekly)
□ Path analysis review (monthly)
□ Assisted conversion tracking (ongoing)
□ Budget allocation review (quarterly)
```