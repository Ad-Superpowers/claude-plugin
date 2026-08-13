# Competitive Analysis Toolkit — Detailed Reference

## Google Ads Script: Competitive Monitor

```javascript
/**
 * Competitive Analysis Monitor
 *
 * Monitors proxy metrics and impression share,
 * sending alerts on significant competitor changes.
 *
 * Note: Auction Insights data is not directly available via API.
 * This script monitors proxy metrics and impression share.
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Schedule: Daily
 */

var CONFIG = {
  EMAIL: 'you@example.com',
  IMPRESSION_SHARE_DROP_THRESHOLD: -0.15,
  CPC_INCREASE_THRESHOLD: 0.20,
  POSITION_DROP_THRESHOLD: 0.5,
  CAMPAIGNS_TO_MONITOR: [],
  CURRENT_PERIOD: 'LAST_7_DAYS',
  PREVIOUS_PERIOD: 'LAST_14_DAYS'
};

function main() {
  var report = {
    alerts: [],
    metrics: [],
    summary: {}
  };

  var campaignIterator;
  if (CONFIG.CAMPAIGNS_TO_MONITOR.length > 0) {
    campaignIterator = AdsApp.campaigns()
      .withCondition('Status = ENABLED')
      .withCondition("Name IN ['" + CONFIG.CAMPAIGNS_TO_MONITOR.join("','") + "']")
      .get();
  } else {
    campaignIterator = AdsApp.campaigns()
      .withCondition('Status = ENABLED')
      .get();
  }

  while (campaignIterator.hasNext()) {
    var campaign = campaignIterator.next();
    var analysis = analyzeCampaignCompetitiveness(campaign);
    report.metrics.push(analysis.metrics);
    report.alerts = report.alerts.concat(analysis.alerts);
  }

  report.summary = {
    campaignsAnalyzed: report.metrics.length,
    alertsGenerated: report.alerts.length,
    timestamp: new Date().toISOString()
  };

  if (report.alerts.length > 0) {
    sendCompetitiveReport(report);
  }
}

function analyzeCampaignCompetitiveness(campaign) {
  var name = campaign.getName();
  var alerts = [];
  var currentStats = campaign.getStatsFor(CONFIG.CURRENT_PERIOD);
  var previousStats = campaign.getStatsFor(CONFIG.PREVIOUS_PERIOD);

  var current = {
    impressions: currentStats.getImpressions(),
    clicks: currentStats.getClicks(),
    cost: currentStats.getCost(),
    avgCpc: currentStats.getAverageCpc()
  };

  var previous = {
    impressions: previousStats.getImpressions() - current.impressions,
    clicks: previousStats.getClicks() - current.clicks,
    cost: previousStats.getCost() - current.cost
  };
  previous.avgCpc = previous.clicks > 0 ? previous.cost / previous.clicks : 0;

  var metrics = {
    name: name,
    currentImpressions: current.impressions,
    previousImpressions: previous.impressions,
    impressionChange: previous.impressions > 0 ?
      (current.impressions - previous.impressions) / previous.impressions : 0,
    currentCpc: current.avgCpc,
    previousCpc: previous.avgCpc,
    cpcChange: previous.avgCpc > 0 ?
      (current.avgCpc - previous.avgCpc) / previous.avgCpc : 0
  };

  try {
    var report = AdsApp.report(
      'SELECT CampaignName, SearchImpressionShare ' +
      'FROM CAMPAIGN_PERFORMANCE_REPORT ' +
      'WHERE CampaignName = "' + name + '" ' +
      'DURING ' + CONFIG.CURRENT_PERIOD.replace('_', '').replace('LAST', 'LAST_')
    );
    var rows = report.rows();
    if (rows.hasNext()) {
      var row = rows.next();
      var isStr = row['SearchImpressionShare'];
      if (isStr && isStr !== '--' && isStr !== ' --') {
        metrics.impressionShare = parseFloat(isStr.replace('%', '')) / 100;
      }
    }
  } catch (e) {
    Logger.log('Could not get impression share for ' + name);
  }

  if (metrics.impressionChange <= CONFIG.IMPRESSION_SHARE_DROP_THRESHOLD &&
      previous.impressions > 100) {
    alerts.push({
      campaign: name, type: 'IMPRESSION_DROP', severity: 'WARNING',
      message: 'Impressions dropped by ' + (Math.abs(metrics.impressionChange) * 100).toFixed(1) + '%',
      current: current.impressions, previous: previous.impressions,
      possibleCause: 'Competitor activity or budget/bid issues'
    });
  }

  if (metrics.cpcChange >= CONFIG.CPC_INCREASE_THRESHOLD && previous.avgCpc > 0) {
    alerts.push({
      campaign: name, type: 'CPC_SPIKE', severity: 'WARNING',
      message: 'Average CPC increased by ' + (metrics.cpcChange * 100).toFixed(1) + '%',
      current: current.avgCpc.toFixed(2), previous: previous.avgCpc.toFixed(2),
      possibleCause: 'Increased competition or Quality Score decline'
    });
  }

  if (metrics.impressionShare && metrics.impressionShare < 0.30) {
    alerts.push({
      campaign: name, type: 'LOW_IMPRESSION_SHARE', severity: 'INFO',
      message: 'Impression Share is ' + (metrics.impressionShare * 100).toFixed(1) + '%',
      possibleCause: 'Budget or bid limitations, or strong competition'
    });
  }

  return { metrics: metrics, alerts: alerts };
}

function sendCompetitiveReport(report) {
  var subject = 'Competitive Alert - ' + AdsApp.currentAccount().getName();
  var body = 'Competitive Analysis Report\n===========================\n\n';
  body += 'SUMMARY:\n';
  body += 'Campaigns analyzed: ' + report.summary.campaignsAnalyzed + '\n';
  body += 'Alerts generated: ' + report.summary.alertsGenerated + '\n\n';

  if (report.alerts.length > 0) {
    body += 'COMPETITIVE ALERTS:\n';
    for (var i = 0; i < report.alerts.length; i++) {
      var alert = report.alerts[i];
      body += '[' + alert.severity + '] ' + alert.campaign + '\n';
      body += 'Type: ' + alert.type + '\n';
      body += 'Issue: ' + alert.message + '\n';
      if (alert.current) {
        body += 'Current: ' + alert.current + ' | Previous: ' + alert.previous + '\n';
      }
      body += 'Possible cause: ' + alert.possibleCause + '\n\n';
    }
  }

  body += 'CAMPAIGN METRICS:\n';
  for (var j = 0; j < Math.min(report.metrics.length, 10); j++) {
    var m = report.metrics[j];
    body += '- ' + m.name + '\n';
    body += '  Impressions: ' + m.currentImpressions;
    body += ' (change: ' + (m.impressionChange * 100).toFixed(1) + '%)\n';
    body += '  Avg CPC: ' + m.currentCpc.toFixed(2);
    body += ' (change: ' + (m.cpcChange * 100).toFixed(1) + '%)\n';
    if (m.impressionShare) {
      body += '  Impression Share: ' + (m.impressionShare * 100).toFixed(1) + '%\n';
    }
    body += '\n';
  }

  body += '\n---\nGenerated by Competitive Monitor Script';
  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Competitive Monitoring Setup

### Automated Alerts

```
COMPETITIVE MONITORING ALERTS
═════════════════════════════

ALERT 1: IMPRESSION SHARE DROP
──────────────────────────────
Trigger: Your IS drops >15% week-over-week
Action: Email alert
Cause: Competitor more aggressive or your issue
Response: Investigate root cause

ALERT 2: NEW COMPETITOR
───────────────────────
Trigger: New domain name in Auction Insights
Action: Email alert with competitor details
Cause: Market entry
Response: Analyze and monitor

ALERT 3: POSITION LOSS
──────────────────────
Trigger: Avg position drops >0.5 or Top IS drops >20%
Action: Email alert
Cause: Competitor bids, your QS, or budget
Response: Diagnose and adjust

ALERT 4: CPC SPIKE
──────────────────
Trigger: Avg CPC rises >20%
Action: Email alert
Cause: Competitive pressure or QS decline
Response: Check auction insights for correlation

SETUP VIA GOOGLE ADS RULES:
───────────────────────────
Tools → Bulk Actions → Rules → Create Rule

Example:
├── Rule Type: Email when...
├── Condition: Search Impr. Share < 40%
├── Frequency: Weekly
└── Action: Send email to team
```

### Weekly Competitive Review

```
WEEKLY COMPETITIVE REVIEW CHECKLIST
════════════════════════════════════

EVERY MONDAY (15-30 min):
─────────────────────────

□ 1. AUCTION INSIGHTS REVIEW
  ├── Download Auction Insights (last 7 days)
  ├── Compare to previous week
  ├── Note significant changes
  └── Identify new competitors

□ 2. IMPRESSION SHARE TREND
  ├── Chart IS over last 4 weeks
  ├── Identify trends (up/down/stable)
  └── Correlate with competitor activity

□ 3. POSITION METRICS
  ├── Top of page rate trend
  ├── Abs top of page rate trend
  └── Compare to competitors

□ 4. MANUAL SPOT CHECK
  ├── Search top 5 keywords (incognito)
  ├── Screenshot competitor ads
  ├── Note new offers/messages
  └── Check landing pages

□ 5. ACTION ITEMS
  ├── List required responses
  ├── Prioritize by impact
  ├── Assign and schedule
  └── Document decisions

MONTHLY DEEP DIVE (1 hour):
────────────────────────────
□ Full competitor landscape analysis
□ Strategy assessment per competitor
□ Trend analysis (3-month view)
□ Strategic recommendations
□ Budget allocation review
```

## Competitor Ad Intelligence

### Manual Research

```
COMPETITOR AD RESEARCH
══════════════════════

METHOD 1: MANUAL SEARCH
────────────────────────
□ Open incognito/private browser
□ Search your most important keywords
□ Note:
  ├── Which competitors appear
  ├── Ad positions
  ├── Headlines and descriptions
  ├── Extensions in use
  ├── Offers and promotions
  └── Landing page URLs

TEMPLATE FOR AD NOTES:
──────────────────────
Keyword: [keyword]
Date: [date]

Competitor A:
├── Position: [1/2/3/etc]
├── Headline 1: "[text]"
├── Headline 2: "[text]"
├── Headline 3: "[text]"
├── Description: "[text]"
├── Extensions: [Sitelinks/Callouts/etc]
├── Offer: [Discount/Free/etc]
└── Landing Page: [URL]

FREQUENCY:
├── Weekly check: Top 10 keywords
├── Monthly deep dive: Top 50 keywords
└── Event-based: When major competitor changes occur

METHOD 2: GOOGLE ADS TRANSPARENCY CENTER
─────────────────────────────────────────
https://adstransparency.google.com/

□ Search by competitor name
□ See all ads they are running
□ Filter by region, time, format
□ View creative variations

METHOD 3: SEMRUSH / SPYFU KEYWORD GAP
──────────────────────────────────────
For keyword-level competitive overlap beyond what Auction Insights shows:
├── Enter your domain + competitor domains
├── See shared keywords and keyword gaps
├── Identify terms competitor bids on that you do not
└── Combine with search_impression_share GAQL data for full picture
```
