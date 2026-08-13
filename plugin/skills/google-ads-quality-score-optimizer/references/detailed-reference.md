## Google Ads Script: Quality Score Monitor

```javascript
/**
 * Quality Score Monitor & Alert Script
 *
 * Features:
 * - Monitors QS changes over time
 * - Alerts on significant QS drops
 * - Weekly QS report
 * - Identifies improvement opportunities
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Schedule: Daily
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Thresholds
  MIN_IMPRESSIONS: 100,           // Minimum impressions for analysis
  QS_DROP_ALERT: 2,               // Alert on QS drop of X points
  LOW_QS_THRESHOLD: 5,            // Keywords with QS below this = priority

  // Spreadsheet for historical tracking (optional)
  SPREADSHEET_URL: '',            // Leave empty to skip

  // Report frequency
  SEND_WEEKLY_REPORT: true,
  REPORT_DAY: 1                   // 1 = Monday
};

function main() {
  var today = new Date();
  var dayOfWeek = today.getDay();

  var report = analyzeQualityScores();

  // Daily alerts for significant drops
  if (report.alerts.length > 0) {
    sendAlertEmail(report.alerts);
  }

  // Weekly report
  if (CONFIG.SEND_WEEKLY_REPORT && dayOfWeek === CONFIG.REPORT_DAY) {
    sendWeeklyReport(report);
  }

  // Log to spreadsheet
  if (CONFIG.SPREADSHEET_URL) {
    logToSpreadsheet(report);
  }
}

function analyzeQualityScores() {
  var report = {
    totalKeywords: 0,
    averageQS: 0,
    lowQSKeywords: [],
    belowAverageComponents: {
      expectedCtr: [],
      adRelevance: [],
      landingPageExperience: []
    },
    alerts: [],
    qsDistribution: {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
  };

  var totalQS = 0;
  var keywordsWithQS = 0;

  var keywords = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .withCondition('Impressions > ' + CONFIG.MIN_IMPRESSIONS)
    .forDateRange('LAST_30_DAYS')
    .get();

  while (keywords.hasNext()) {
    var keyword = keywords.next();
    var qs = keyword.getQualityScore();

    if (qs === null) continue;

    report.totalKeywords++;
    keywordsWithQS++;
    totalQS += qs;

    // QS Distribution
    report.qsDistribution[qs]++;

    // Low QS keywords
    if (qs < CONFIG.LOW_QS_THRESHOLD) {
      report.lowQSKeywords.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        adGroup: keyword.getAdGroup().getName(),
        qs: qs,
        expectedCtr: getStatusText(keyword.getExpectedCtr()),
        adRelevance: getStatusText(keyword.getAdRelevance()),
        landingPageExperience: getStatusText(keyword.getLandingPageExperience())
      });
    }

    // Below Average Components
    if (keyword.getExpectedCtr() === 'BELOW_AVERAGE') {
      report.belowAverageComponents.expectedCtr.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        qs: qs
      });
    }

    if (keyword.getAdRelevance() === 'BELOW_AVERAGE') {
      report.belowAverageComponents.adRelevance.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        qs: qs
      });
    }

    if (keyword.getLandingPageExperience() === 'BELOW_AVERAGE') {
      report.belowAverageComponents.landingPageExperience.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        qs: qs
      });
    }
  }

  report.averageQS = keywordsWithQS > 0 ?
    (totalQS / keywordsWithQS).toFixed(1) : 0;

  return report;
}

function getStatusText(status) {
  switch(status) {
    case 'ABOVE_AVERAGE': return 'Above Avg';
    case 'AVERAGE': return 'Average';
    case 'BELOW_AVERAGE': return 'Below Avg';
    default: return 'Unknown';
  }
}

function sendAlertEmail(alerts) {
  var subject = 'Quality Score Alert - ' + AdsApp.currentAccount().getName();
  var body = 'Quality Score Alerts\n';
  body += '====================\n\n';

  for (var i = 0; i < alerts.length; i++) {
    body += alerts[i] + '\n';
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}

function sendWeeklyReport(report) {
  var subject = 'Weekly Quality Score Report - ' + AdsApp.currentAccount().getName();
  var body = 'Quality Score Weekly Report\n';
  body += '===========================\n\n';

  body += 'SUMMARY:\n';
  body += '────────\n';
  body += 'Total Keywords Analyzed: ' + report.totalKeywords + '\n';
  body += 'Average Quality Score: ' + report.averageQS + '\n';
  body += 'Keywords with QS < ' + CONFIG.LOW_QS_THRESHOLD + ': ' +
          report.lowQSKeywords.length + '\n\n';

  body += 'QS DISTRIBUTION:\n';
  body += '────────────────\n';
  for (var qs = 10; qs >= 1; qs--) {
    var count = report.qsDistribution[qs];
    var bar = '';
    for (var j = 0; j < Math.min(count, 20); j++) bar += '█';
    body += 'QS ' + (qs < 10 ? ' ' : '') + qs + ': ' + bar + ' (' + count + ')\n';
  }
  body += '\n';

  body += 'BELOW AVERAGE COMPONENTS:\n';
  body += '─────────────────────────\n';
  body += 'Expected CTR: ' + report.belowAverageComponents.expectedCtr.length + ' keywords\n';
  body += 'Ad Relevance: ' + report.belowAverageComponents.adRelevance.length + ' keywords\n';
  body += 'Landing Page Exp: ' +
          report.belowAverageComponents.landingPageExperience.length + ' keywords\n\n';

  if (report.lowQSKeywords.length > 0) {
    body += 'TOP 10 LOW QS KEYWORDS:\n';
    body += '───────────────────────\n';
    var sorted = report.lowQSKeywords.sort(function(a, b) { return a.qs - b.qs; });
    for (var k = 0; k < Math.min(sorted.length, 10); k++) {
      var kw = sorted[k];
      body += '- ' + kw.keyword + ' (QS: ' + kw.qs + ')\n';
      body += '  Campaign: ' + kw.campaign + '\n';
      body += '  CTR: ' + kw.expectedCtr + ' | ';
      body += 'Ad Rel: ' + kw.adRelevance + ' | ';
      body += 'LP: ' + kw.landingPageExperience + '\n\n';
    }
  }

  body += '\n---\nGenerated by Quality Score Monitor Script';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
  Logger.log('Weekly report sent');
}

function logToSpreadsheet(report) {
  if (!CONFIG.SPREADSHEET_URL) return;

  try {
    var ss = SpreadsheetApp.openByUrl(CONFIG.SPREADSHEET_URL);
    var sheet = ss.getSheetByName('QS_History') ||
                ss.insertSheet('QS_History');

    var today = new Date();
    var row = [
      today,
      report.totalKeywords,
      report.averageQS,
      report.lowQSKeywords.length,
      report.belowAverageComponents.expectedCtr.length,
      report.belowAverageComponents.adRelevance.length,
      report.belowAverageComponents.landingPageExperience.length
    ];

    sheet.appendRow(row);
    Logger.log('Logged to spreadsheet');
  } catch (e) {
    Logger.log('Spreadsheet error: ' + e);
  }
}
```