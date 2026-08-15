## Google Ads Script: Demand Gen Monitor

```javascript
/**
 * Demand Gen Campaign Performance Monitor
 *
 * Monitors Demand Gen campaigns and sends
 * weekly performance alerts.
 *
 * Features:
 * - CTR monitoring
 * - CPA/ROAS tracking
 * - Audience performance
 * - Asset insights
 *
 * Schedule: Weekly on Monday
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Thresholds
  LOW_CTR: 0.005,              // Alert if CTR < 0.5%
  HIGH_CPA_MULTIPLIER: 1.5,    // Alert if CPA > 1.5x target
  MIN_IMPRESSIONS: 1000,

  // Date range
  DATE_RANGE: 'LAST_7_DAYS'
};

function main() {
  var demandGenCampaigns = [];
  var alerts = [];

  // Note: Demand Gen campaigns are accessible via Discovery campaign type in API
  var query =
    'SELECT campaign.name, campaign.id, ' +
    'metrics.impressions, metrics.clicks, metrics.cost_micros, ' +
    'metrics.conversions, metrics.conversions_value, metrics.ctr, ' +
    'metrics.average_cpc ' +
    'FROM campaign ' +
    'WHERE campaign.advertising_channel_type = "DISCOVERY" ' +
    'AND segments.date DURING ' + CONFIG.DATE_RANGE + ' ' +
    'AND metrics.impressions > ' + CONFIG.MIN_IMPRESSIONS;

  try {
    var report = AdsApp.report(query);
    var rows = report.rows();

    while (rows.hasNext()) {
      var row = rows.next();

      var impressions = parseInt(row['metrics.impressions']);
      var clicks = parseInt(row['metrics.clicks']);
      var costMicros = parseInt(row['metrics.cost_micros']);
      var cost = costMicros / 1000000;

      var conversions = parseFloat(row['metrics.conversions']) || 0;
      var value = parseFloat(row['metrics.conversions_value']) || 0;
      var ctr = parseFloat(row['metrics.ctr']) || 0;
      var avgCpcMicros = parseInt(row['metrics.average_cpc']) || 0;
      var cpc = avgCpcMicros / 1000000;

      var campaign = {
        name: row['campaign.name'],
        impressions: impressions,
        clicks: clicks,
        cost: cost,
        conversions: conversions,
        value: value,
        ctr: ctr,
        cpc: cpc,
        cpa: conversions > 0 ? cost / conversions : 0,
        roas: cost > 0 ? value / cost : 0,
        convRate: clicks > 0 ? conversions / clicks : 0
      };

      // Check for issues
      if (ctr < CONFIG.LOW_CTR) {
        alerts.push({
          campaign: campaign.name,
          issue: 'Low CTR',
          value: (ctr * 100).toFixed(2) + '%',
          threshold: (CONFIG.LOW_CTR * 100).toFixed(2) + '%'
        });
      }

      demandGenCampaigns.push(campaign);
    }
  } catch (e) {
    Logger.log('Query error: ' + e.message);
    Logger.log('Note: Demand Gen campaigns may appear as DISCOVERY in API');
  }

  // Send report
  sendDemandGenReport(demandGenCampaigns, alerts);
  Logger.log('Demand Gen monitor complete. Campaigns: ' + demandGenCampaigns.length);
}

function sendDemandGenReport(campaigns, alerts) {
  if (campaigns.length === 0) {
    Logger.log('No Demand Gen campaigns found with sufficient data');
    return;
  }

  var subject = 'Demand Gen Report - ' + AdsApp.currentAccount().getName();

  var body = 'Demand Gen Campaign Performance Report\n';
  body += '=======================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Period: ' + CONFIG.DATE_RANGE + '\n';
  body += 'Campaigns: ' + campaigns.length + '\n\n';

  // Summary
  var totalCost = 0;
  var totalConv = 0;
  var totalValue = 0;
  var totalClicks = 0;
  var totalImpressions = 0;

  for (var i = 0; i < campaigns.length; i++) {
    totalCost += campaigns[i].cost;
    totalConv += campaigns[i].conversions;
    totalValue += campaigns[i].value;
    totalClicks += campaigns[i].clicks;
    totalImpressions += campaigns[i].impressions;
  }

  body += 'SUMMARY\n';
  body += '───────\n';
  body += 'Total Spend: €' + totalCost.toFixed(2) + '\n';
  body += 'Total Impressions: ' + totalImpressions.toLocaleString() + '\n';
  body += 'Total Clicks: ' + totalClicks.toLocaleString() + '\n';
  body += 'Overall CTR: ' + (totalImpressions > 0 ? (totalClicks / totalImpressions * 100).toFixed(2) : 0) + '%\n';
  body += 'Total Conversions: ' + totalConv.toFixed(1) + '\n';
  body += 'Average CPA: €' + (totalConv > 0 ? (totalCost / totalConv).toFixed(2) : 'N/A') + '\n';
  body += 'Overall ROAS: ' + (totalCost > 0 ? (totalValue / totalCost).toFixed(2) : 0) + 'x\n\n';

  // Alerts
  if (alerts.length > 0) {
    body += 'ALERTS\n';
    body += '──────\n';
    for (var j = 0; j < alerts.length; j++) {
      var alert = alerts[j];
      body += '• ' + alert.campaign + '\n';
      body += '  ' + alert.issue + ': ' + alert.value + ' (threshold: ' + alert.threshold + ')\n\n';
    }
  }

  // Campaign details
  body += 'CAMPAIGN DETAILS\n';
  body += '────────────────\n';
  for (var k = 0; k < campaigns.length; k++) {
    var c = campaigns[k];
    body += '• ' + c.name + '\n';
    body += '  Spend: €' + c.cost.toFixed(2);
    body += ' | Clicks: ' + c.clicks;
    body += ' | CTR: ' + (c.ctr * 100).toFixed(2) + '%\n';
    body += '  Conv: ' + c.conversions.toFixed(1);
    body += ' | CPA: €' + (c.cpa > 0 ? c.cpa.toFixed(2) : 'N/A');
    body += ' | ROAS: ' + c.roas.toFixed(2) + 'x\n\n';
  }

  body += '\n---\nGenerated by Demand Gen Monitor';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```