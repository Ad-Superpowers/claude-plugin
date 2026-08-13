# Audience Strategy Planner — Detailed Reference

## In-Market Audience Categories

### B2B Services
```
├── Business Services
│   ├── Accounting & Finance Services
│   ├── Advertising & Marketing Services
│   ├── Business Technology
│   ├── Corporate Event Planning
│   └── Office Supplies
├── Business Technology
│   ├── Enterprise Software
│   ├── CRM Software
│   ├── Cloud Storage
│   └── Cybersecurity
└── Financial Services
    ├── Business Loans
    ├── Insurance
    └── Merchant Services
```

### B2C Services
```
├── Home Services
│   ├── Home Improvement
│   ├── Cleaning Services
│   ├── Moving & Relocation
│   └── Pest Control
├── Legal Services
├── Financial Services
│   ├── Personal Loans
│   ├── Insurance
│   └── Investment Services
└── Education
    ├── Post-Secondary Education
    └── Professional Training
```

## Affinity Audience Categories

```
BUSINESS PROFESSIONALS:
├── Business Professionals
├── Small Business Owners
├── Corporate Executives
└── IT Professionals

TECHNOPHILES:
├── Tech Enthusiasts
├── Social Media Enthusiasts
└── Mobile Enthusiasts

LIFESTYLE:
├── Green Living Enthusiasts
├── Luxury Shoppers
├── Value Shoppers
└── Home Decor Enthusiasts
```

## Custom Segments Detailed Setup

```
CUSTOM SEGMENTS (Formerly Custom Intent)
════════════════════════════════════════

WHEN TO USE:
────────────
□ No suitable In-market/Affinity audience available
□ Niche market or product
□ Competitor targeting needed
□ Very specific intent

1. CUSTOM INTENT (Search-based)
───────────────────────────────
"People who searched for these terms"

Setup:
1. Audience Manager → Custom Segments → +
2. Name: "CS_[Purpose]_[Date]"
3. Type: "People who searched for any of these terms"
4. Add keywords:
   ├── Transactional queries
   ├── Problem-based queries
   ├── Competitor + alternative queries
   └── 10-50 keywords recommended

Example (B2B CRM):
├── "best crm software"
├── "crm for small business"
├── "salesforce alternative"
├── "hubspot vs pipedrive"
└── "customer management software"

2. CUSTOM AFFINITY (Interest-based)
───────────────────────────────────
"People who have interests in..."

Setup:
1. Type: "People with any of these interests or purchase intentions"
2. Add:
   ├── Interest keywords
   ├── URLs of relevant websites
   └── Apps they might use

Example (Marketing Professionals):
├── Keywords: digital marketing, content strategy
├── URLs: marketingweek.com, hubspot.com/blog
└── Apps: Hootsuite, Buffer, Sprout Social

3. COMPETITOR TARGETING
───────────────────────
Target users who visit competitor sites

Setup:
1. Type: "People who browse types of websites"
2. Add competitor URLs:
   ├── competitor1.com
   ├── competitor2.com
   └── competitor3.com

WARNING: This targets people WHO BROWSE SIMILAR SITES
   Not exactly those sites — Google's interpretation

BEST PRACTICES:
───────────────
□ Test segments with "Observation" first
□ Start broad, narrow down over time
□ Combine with other targeting
□ Minimum 10 keywords/URLs for good reach
□ Monitor weekly for performance
```

## Google Ads Script: Audience Performance Analyzer

```javascript
/**
 * Audience Performance Analyzer
 *
 * Analyzes performance of all audiences
 * Generates recommendations for bid adjustments
 *
 * Setup:
 * 1. Update CONFIG
 * 2. Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',
  DATE_RANGE: 'LAST_30_DAYS',
  MIN_IMPRESSIONS: 1000,
  MIN_CLICKS: 50,
  PERFORMANCE_GOOD: 1.2,
  PERFORMANCE_POOR: 0.8,
  GOOD_BID_ADJUSTMENT: 20,
  POOR_BID_ADJUSTMENT: -20
};

function main() {
  var report = {
    audiences: [],
    recommendations: [],
    topPerformers: [],
    underperformers: []
  };

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .forDateRange(CONFIG.DATE_RANGE)
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var campaignStats = campaign.getStatsFor(CONFIG.DATE_RANGE);
    var campaignCPA = calculateCPA(campaignStats);

    var audienceTargeting = campaign.targeting().audiences().get();
    while (audienceTargeting.hasNext()) {
      var audience = audienceTargeting.next();
      var stats = audience.getStatsFor(CONFIG.DATE_RANGE);
      if (stats.getImpressions() < CONFIG.MIN_IMPRESSIONS) continue;

      var audienceCPA = calculateCPA(stats);
      var performance = campaignCPA > 0 ?
        campaignCPA / (audienceCPA || 9999) : 0;

      var audienceData = {
        campaign: campaign.getName(),
        name: audience.getName(),
        impressions: stats.getImpressions(),
        clicks: stats.getClicks(),
        conversions: stats.getConversions(),
        cost: stats.getCost(),
        cpa: audienceCPA,
        performance: performance,
        currentBidMod: audience.getBidModifier()
      };

      report.audiences.push(audienceData);

      if (performance >= CONFIG.PERFORMANCE_GOOD && stats.getClicks() >= CONFIG.MIN_CLICKS) {
        report.topPerformers.push(audienceData);
        if (audience.getBidModifier() < 1 + (CONFIG.GOOD_BID_ADJUSTMENT / 100)) {
          report.recommendations.push({
            campaign: campaign.getName(),
            audience: audience.getName(),
            action: 'INCREASE BID',
            current: Math.round((audience.getBidModifier() - 1) * 100) + '%',
            recommended: '+' + CONFIG.GOOD_BID_ADJUSTMENT + '%',
            reason: 'CPA ' + Math.round((1 - 1/performance) * 100) + '% better than campaign avg'
          });
        }
      } else if (performance <= CONFIG.PERFORMANCE_POOR && stats.getClicks() >= CONFIG.MIN_CLICKS) {
        report.underperformers.push(audienceData);
        report.recommendations.push({
          campaign: campaign.getName(),
          audience: audience.getName(),
          action: 'DECREASE BID or EXCLUDE',
          current: Math.round((audience.getBidModifier() - 1) * 100) + '%',
          recommended: CONFIG.POOR_BID_ADJUSTMENT + '%',
          reason: 'CPA ' + Math.round((1/performance - 1) * 100) + '% worse than campaign avg'
        });
      }
    }
  }
  sendReport(report);
}

function calculateCPA(stats) {
  var conversions = stats.getConversions();
  return conversions > 0 ? stats.getCost() / conversions : 0;
}

function sendReport(report) {
  var subject = 'Audience Performance Report - ' + AdsApp.currentAccount().getName();
  var body = 'Weekly Audience Performance Analysis\n=====================================\n\n';
  body += 'SUMMARY:\n';
  body += 'Total audiences analyzed: ' + report.audiences.length + '\n';
  body += 'Top performers: ' + report.topPerformers.length + '\n';
  body += 'Underperformers: ' + report.underperformers.length + '\n';
  body += 'Recommendations: ' + report.recommendations.length + '\n\n';

  if (report.topPerformers.length > 0) {
    body += 'TOP PERFORMERS:\n';
    for (var i = 0; i < Math.min(report.topPerformers.length, 5); i++) {
      var top = report.topPerformers[i];
      body += '- ' + top.name + ' (' + top.campaign + ')\n';
      body += '  Conversions: ' + top.conversions + ' | CPA: $' + top.cpa.toFixed(2) + '\n';
    }
    body += '\n';
  }

  if (report.recommendations.length > 0) {
    body += 'RECOMMENDATIONS:\n';
    for (var j = 0; j < Math.min(report.recommendations.length, 10); j++) {
      var rec = report.recommendations[j];
      body += '- ' + rec.audience + ' (' + rec.campaign + ')\n';
      body += '  Action: ' + rec.action + '\n';
      body += '  Current: ' + rec.current + ' -> Recommended: ' + rec.recommended + '\n';
      body += '  Reason: ' + rec.reason + '\n\n';
    }
  }

  body += '\n---\nGenerated by Audience Performance Analyzer';
  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```
