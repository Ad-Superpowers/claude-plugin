## Google Ads Script: Learning Phase Monitor

```javascript
/**
 * Learning Phase Monitor Script
 *
 * Monitors Smart Bidding learning phase status and sends alerts.
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Schedule: Daily at 9:00
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Alert thresholds
  LEARNING_DAYS_WARNING: 14,  // Alert if >14 days in learning
  LEARNING_DAYS_CRITICAL: 21, // Critical alert

  // Performance monitoring during learning
  CPA_SPIKE_THRESHOLD: 0.50,  // Alert on 50% CPA spike
  CONV_DROP_THRESHOLD: 0.30   // Alert on 30% conversion drop
};

function main() {
  var report = {
    learningCampaigns: [],
    limitedCampaigns: [],
    eligibleCampaigns: [],
    alerts: [],
    recommendations: []
  };

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var status = analyzeLearningStatus(campaign);

    if (status.isLearning) {
      report.learningCampaigns.push(status);

      if (status.estimatedDays > CONFIG.LEARNING_DAYS_WARNING) {
        report.alerts.push({
          campaign: status.name,
          type: status.estimatedDays > CONFIG.LEARNING_DAYS_CRITICAL ? 'CRITICAL' : 'WARNING',
          message: 'Learning phase has been running for ' + status.estimatedDays + ' days'
        });
      }
    } else if (status.isLimited) {
      report.limitedCampaigns.push(status);
      report.alerts.push({
        campaign: status.name,
        type: 'ACTION_REQUIRED',
        message: 'Learning Limited - action required'
      });
    } else {
      report.eligibleCampaigns.push(status);
    }

    // Check performance changes during learning
    if (status.isLearning) {
      var perfAlerts = checkPerformanceDuringLearning(campaign);
      report.alerts = report.alerts.concat(perfAlerts);
    }
  }

  // Generate recommendations
  report.recommendations = generateLearningRecommendations(report);

  // Send report
  sendLearningReport(report);

  Logger.log('Learning Phase Monitor Complete');
  Logger.log('Campaigns in learning: ' + report.learningCampaigns.length);
  Logger.log('Campaigns limited: ' + report.limitedCampaigns.length);
  Logger.log('Alerts: ' + report.alerts.length);
}

function analyzeLearningStatus(campaign) {
  var name = campaign.getName();
  var bidStrategy = campaign.getBiddingStrategyType();

  // Get conversion stats
  var stats14d = campaign.getStatsFor('LAST_14_DAYS');
  var stats30d = campaign.getStatsFor('LAST_30_DAYS');

  var conv14d = stats14d.getConversions();
  var conv30d = stats30d.getConversions();

  // Estimate learning status based on conversion volume
  // Note: Actual status requires UI check, this is proxy
  var isLearning = conv30d < 50;
  var isLimited = conv30d < 30 && conv14d < 15;

  // Estimate days in learning
  var avgDailyConv = conv30d / 30;
  var estimatedDays = avgDailyConv > 0 ?
    Math.min(Math.ceil(50 / avgDailyConv), 60) : 60;

  return {
    name: name,
    bidStrategy: bidStrategy,
    conversions30d: conv30d,
    conversions14d: conv14d,
    avgDailyConv: avgDailyConv,
    isLearning: isLearning,
    isLimited: isLimited,
    estimatedDays: isLearning ? estimatedDays : 0,
    cost30d: stats30d.getCost()
  };
}

function checkPerformanceDuringLearning(campaign) {
  var alerts = [];
  var name = campaign.getName();

  var currentStats = campaign.getStatsFor('LAST_7_DAYS');
  var previousStats = campaign.getStatsFor('LAST_14_DAYS');

  // Current period
  var currentConv = currentStats.getConversions();
  var currentCost = currentStats.getCost();
  var currentCPA = currentConv > 0 ? currentCost / currentConv : 0;

  // Previous period (week before last week)
  var prevConv = previousStats.getConversions() - currentConv;
  var prevCost = previousStats.getCost() - currentCost;
  var prevCPA = prevConv > 0 ? prevCost / prevConv : 0;

  // Check CPA spike
  if (prevCPA > 0 && currentCPA > 0) {
    var cpaChange = (currentCPA - prevCPA) / prevCPA;
    if (cpaChange > CONFIG.CPA_SPIKE_THRESHOLD) {
      alerts.push({
        campaign: name,
        type: 'PERFORMANCE',
        message: 'CPA spike during learning: ' +
                 (cpaChange * 100).toFixed(0) + '% increase'
      });
    }
  }

  // Check conversion drop
  if (prevConv > 0) {
    var convChange = (prevConv - currentConv) / prevConv;
    if (convChange > CONFIG.CONV_DROP_THRESHOLD) {
      alerts.push({
        campaign: name,
        type: 'PERFORMANCE',
        message: 'Conversion drop during learning: ' +
                 (convChange * 100).toFixed(0) + '% decline'
      });
    }
  }

  return alerts;
}

function generateLearningRecommendations(report) {
  var recs = [];

  // Limited campaigns
  if (report.limitedCampaigns.length > 0) {
    recs.push({
      priority: 'HIGH',
      action: 'Address Learning Limited campaigns',
      detail: 'Consider: increasing budget, relaxing target, or consolidating'
    });
  }

  // Long learning campaigns
  var longLearning = report.learningCampaigns.filter(function(c) {
    return c.estimatedDays > CONFIG.LEARNING_DAYS_WARNING;
  });

  if (longLearning.length > 0) {
    recs.push({
      priority: 'MEDIUM',
      action: longLearning.length + ' campaigns too long in learning',
      detail: 'Evaluate conversion volumes and bid strategy choice'
    });
  }

  // Low volume campaigns
  var lowVolume = report.learningCampaigns.filter(function(c) {
    return c.avgDailyConv < 2;
  });

  if (lowVolume.length > 0) {
    recs.push({
      priority: 'MEDIUM',
      action: lowVolume.length + ' campaigns with <2 conv/day',
      detail: 'Consider Portfolio bid strategy or higher-funnel conversion'
    });
  }

  return recs;
}

function sendLearningReport(report) {
  var subject = 'Learning Phase Report - ' + AdsApp.currentAccount().getName();
  var body = 'Smart Bidding Learning Phase Report\n';
  body += '====================================\n\n';

  // Summary
  body += 'SUMMARY:\n';
  body += '- Campaigns in learning: ' + report.learningCampaigns.length + '\n';
  body += '- Campaigns limited: ' + report.limitedCampaigns.length + '\n';
  body += '- Campaigns eligible: ' + report.eligibleCampaigns.length + '\n';
  body += '- Alerts: ' + report.alerts.length + '\n\n';

  // Alerts
  if (report.alerts.length > 0) {
    body += 'ALERTS:\n';
    body += '────────\n';

    for (var i = 0; i < report.alerts.length; i++) {
      var alert = report.alerts[i];
      body += '[' + alert.type + '] ' + alert.campaign + '\n';
      body += '  ' + alert.message + '\n\n';
    }
  }

  // Learning campaigns detail
  if (report.learningCampaigns.length > 0) {
    body += 'CAMPAIGNS IN LEARNING:\n';
    body += '──────────────────────\n';

    for (var j = 0; j < report.learningCampaigns.length; j++) {
      var lc = report.learningCampaigns[j];
      body += '- ' + lc.name + '\n';
      body += '  Conv/30d: ' + lc.conversions30d.toFixed(0);
      body += ' | Avg/day: ' + lc.avgDailyConv.toFixed(1);
      body += ' | Est. days remaining: ' + lc.estimatedDays + '\n\n';
    }
  }

  // Limited campaigns
  if (report.limitedCampaigns.length > 0) {
    body += 'LEARNING LIMITED (Action Required):\n';
    body += '─────────────────────────────────\n';

    for (var k = 0; k < report.limitedCampaigns.length; k++) {
      var ltd = report.limitedCampaigns[k];
      body += '- ' + ltd.name + '\n';
      body += '  Conv/30d: ' + ltd.conversions30d.toFixed(0);
      body += ' | Cost: $' + ltd.cost30d.toFixed(0) + '\n\n';
    }
  }

  // Recommendations
  if (report.recommendations.length > 0) {
    body += 'RECOMMENDATIONS:\n';
    body += '────────────────\n';

    for (var l = 0; l < report.recommendations.length; l++) {
      var rec = report.recommendations[l];
      body += '[' + rec.priority + '] ' + rec.action + '\n';
      body += '  → ' + rec.detail + '\n\n';
    }
  }

  body += '\n---\nGenerated by Learning Phase Monitor Script';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```