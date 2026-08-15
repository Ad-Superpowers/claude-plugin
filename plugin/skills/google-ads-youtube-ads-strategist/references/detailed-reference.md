## Google Ads Script: YouTube Campaign Monitor

```javascript
/**
 * YouTube Campaign Performance Monitor
 *
 * This script monitors YouTube video campaigns and sends
 * weekly performance reports.
 *
 * Features:
 * - View rate tracking
 * - CPV/CPM analysis
 * - Audience performance
 * - Video completion rates
 *
 * Schedule: Weekly on Monday
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Thresholds
  LOW_VIEW_RATE: 0.20,           // Alert if view rate < 20%
  HIGH_CPV: 0.10,                // Alert if CPV > $0.10
  MIN_IMPRESSIONS: 1000,         // Minimum for analysis

  // Date range
  DATE_RANGE: 'LAST_7_DAYS'
};

function main() {
  var videoCampaigns = [];

  // Query video campaign data
  var query =
    'SELECT campaign.name, campaign.id, ' +
    'metrics.impressions, metrics.video_trueview_views, metrics.cost_micros, ' +
    'metrics.video_trueview_view_rate, metrics.trueview_average_cpv, ' +
    'metrics.video_quartile_p25_rate, metrics.video_quartile_p50_rate, ' +
    'metrics.video_quartile_p75_rate, metrics.video_quartile_p100_rate, ' +
    'metrics.conversions, metrics.conversions_value ' +
    'FROM campaign ' +
    'WHERE campaign.advertising_channel_type = "VIDEO" ' +
    'AND segments.date DURING ' + CONFIG.DATE_RANGE + ' ' +
    'AND metrics.impressions > ' + CONFIG.MIN_IMPRESSIONS;

  var report = AdsApp.report(query);
  var rows = report.rows();

  while (rows.hasNext()) {
    var row = rows.next();

    var impressions = parseInt(row['metrics.impressions']);
    var views = parseInt(row['metrics.video_trueview_views']);
    var costMicros = parseInt(row['metrics.cost_micros']);
    var cost = costMicros / 1000000;

    var viewRate = parseFloat(row['metrics.video_view_rate']) || 0;
    var avgCpvMicros = parseInt(row['metrics.trueview_average_cpv']) || 0;
    var avgCpv = avgCpvMicros / 1000000;

    var q25 = parseFloat(row['metrics.video_quartile_p25_rate']) || 0;
    var q50 = parseFloat(row['metrics.video_quartile_p50_rate']) || 0;
    var q75 = parseFloat(row['metrics.video_quartile_p75_rate']) || 0;
    var q100 = parseFloat(row['metrics.video_quartile_p100_rate']) || 0;

    var conversions = parseFloat(row['metrics.conversions']) || 0;
    var value = parseFloat(row['metrics.conversions_value']) || 0;

    var campaign = {
      name: row['campaign.name'],
      impressions: impressions,
      views: views,
      cost: cost,
      viewRate: viewRate,
      cpv: avgCpv,
      cpm: impressions > 0 ? (cost / impressions) * 1000 : 0,
      q25: q25,
      q50: q50,
      q75: q75,
      q100: q100,
      conversions: conversions,
      value: value,
      cpa: conversions > 0 ? cost / conversions : 0,
      roas: cost > 0 ? value / cost : 0
    };

    // Check for issues
    campaign.issues = [];
    if (viewRate < CONFIG.LOW_VIEW_RATE) {
      campaign.issues.push('Low view rate: ' + (viewRate * 100).toFixed(1) + '%');
    }
    if (avgCpv > CONFIG.HIGH_CPV && views > 100) {
      campaign.issues.push('High CPV: $' + avgCpv.toFixed(3));
    }

    videoCampaigns.push(campaign);
  }

  // Sort by cost descending
  videoCampaigns.sort(function(a, b) { return b.cost - a.cost; });

  // Send report
  sendReport(videoCampaigns);
  Logger.log('YouTube monitor complete. Campaigns analyzed: ' + videoCampaigns.length);
}

function sendReport(campaigns) {
  var subject = 'YouTube Campaign Report - ' + AdsApp.currentAccount().getName();

  var body = 'YouTube Campaign Performance Report\n';
  body += '====================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Period: ' + CONFIG.DATE_RANGE + '\n';
  body += 'Campaigns: ' + campaigns.length + '\n\n';

  // Summary stats
  var totalCost = 0;
  var totalViews = 0;
  var totalImpressions = 0;
  var totalConversions = 0;
  var campaignsWithIssues = 0;

  for (var i = 0; i < campaigns.length; i++) {
    totalCost += campaigns[i].cost;
    totalViews += campaigns[i].views;
    totalImpressions += campaigns[i].impressions;
    totalConversions += campaigns[i].conversions;
    if (campaigns[i].issues.length > 0) campaignsWithIssues++;
  }

  body += 'SUMMARY\n';
  body += '───────\n';
  body += 'Total Spend: $' + totalCost.toFixed(2) + '\n';
  body += 'Total Views: ' + totalViews.toLocaleString() + '\n';
  body += 'Total Impressions: ' + totalImpressions.toLocaleString() + '\n';
  body += 'Avg View Rate: ' + (totalImpressions > 0 ? (totalViews / totalImpressions * 100).toFixed(1) : 0) + '%\n';
  body += 'Total Conversions: ' + totalConversions.toFixed(1) + '\n';
  body += 'Campaigns with Issues: ' + campaignsWithIssues + '\n\n';

  // Campaigns with issues first
  if (campaignsWithIssues > 0) {
    body += 'CAMPAIGNS NEEDING ATTENTION\n';
    body += '───────────────────────────\n';
    for (var j = 0; j < campaigns.length; j++) {
      var c = campaigns[j];
      if (c.issues.length > 0) {
        body += '• ' + c.name + '\n';
        for (var k = 0; k < c.issues.length; k++) {
          body += '  - ' + c.issues[k] + '\n';
        }
        body += '\n';
      }
    }
  }

  // Top campaigns by spend
  body += 'TOP CAMPAIGNS BY SPEND\n';
  body += '──────────────────────\n';
  for (var m = 0; m < Math.min(5, campaigns.length); m++) {
    var camp = campaigns[m];
    body += '• ' + camp.name + '\n';
    body += '  Spend: $' + camp.cost.toFixed(2);
    body += ' | Views: ' + camp.views.toLocaleString();
    body += ' | VR: ' + (camp.viewRate * 100).toFixed(1) + '%';
    body += ' | CPV: $' + camp.cpv.toFixed(3) + '\n';
    body += '  Video Completion: 25%=' + (camp.q25 * 100).toFixed(0) + '%';
    body += ', 50%=' + (camp.q50 * 100).toFixed(0) + '%';
    body += ', 75%=' + (camp.q75 * 100).toFixed(0) + '%';
    body += ', 100%=' + (camp.q100 * 100).toFixed(0) + '%\n';
    if (camp.conversions > 0) {
      body += '  Conv: ' + camp.conversions.toFixed(1);
      body += ' | CPA: $' + camp.cpa.toFixed(2);
      body += ' | ROAS: ' + camp.roas.toFixed(2) + 'x\n';
    }
    body += '\n';
  }

  body += '\n---\nGenerated by YouTube Campaign Monitor';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```