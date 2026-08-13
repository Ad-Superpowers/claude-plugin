## Quick Decision Guide

```
AUTOMATED RULES OR SCRIPTS?
│
├─► Simple action, UI-configurable
│   └─► AUTOMATED RULES
│       ├── No code required
│       ├── Easy to manage
│       └── Limited logic capabilities
│
├─► Complex logic, multiple conditions
│   └─► GOOGLE ADS SCRIPTS
│       ├── JavaScript code
│       ├── More flexibility
│       └── External data integration possible
│
├─► Real-time optimization
│   └─► SMART BIDDING + RULES COMBO
│       ├── Let Google AI handle bidding
│       └── Rules for edge cases
│
└─► Multi-account management
    └─► MCC SCRIPTS
        ├── Cross-account automation
        └── Central monitoring
```

## Google Ads Script Equivalents

### When Scripts vs Rules

```
RULES VS SCRIPTS DECISION GUIDE
════════════════════════════════

USE AUTOMATED RULES WHEN:
─────────────────────────
✓ Simple IF-THEN logic
✓ Single condition/action
✓ Standard metrics (CPA, CTR, etc.)
✓ No external data needed
✓ Quick setup desired
✓ Non-technical team

USE SCRIPTS WHEN:
─────────────────
✓ Complex calculations (e.g., ROAS thresholds)
✓ Combining multiple conditions
✓ External data integration (spreadsheets, API)
✓ Cross-entity logic (campaign + ad group)
✓ Custom reporting
✓ MCC-level automation
✓ Advanced alerting

HYBRID APPROACH:
────────────────
Rules for: Simple, time-sensitive actions
Scripts for: Complex logic, reporting
PMax/Smart bidding: Real-time optimization

EXAMPLE:
────────
Automated Rule: Pause keyword if CPA > €50
Script: Analyze N-grams and send report with suggestions
Smart Bidding: Real-time bid optimization
```

### Script Templates for Common Rules

```javascript
/**
 * Advanced Budget Protection Script
 *
 * This script provides advanced budget protection
 * that goes beyond what automated rules can do.
 *
 * Features:
 * - Multi-campaign budget caps
 * - Rolling window analysis
 * - Slack/email alerts
 * - Automatic recovery
 *
 * Schedule: Hourly
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Account-level daily cap
  ACCOUNT_DAILY_CAP: 1000,  // €1000 per day

  // Campaign-level caps (optional)
  CAMPAIGN_CAPS: {
    'Brand Campaign': 200,
    'Generic Campaign': 300
  },

  // Auto-pause or alert only
  AUTO_PAUSE: true,

  // Recovery: Re-enable next day
  AUTO_RECOVERY: true
};

function main() {
  var today = new Date();
  var todayString = Utilities.formatDate(today, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');

  // Get total account spend today
  var accountStats = AdsApp.currentAccount().getStatsFor(todayString, todayString);
  var totalSpend = accountStats.getCost();

  Logger.log('Total spend today: €' + totalSpend.toFixed(2));

  // Check account-level cap
  if (totalSpend >= CONFIG.ACCOUNT_DAILY_CAP) {
    var message = 'Account daily cap reached: €' + totalSpend.toFixed(2) + ' / €' + CONFIG.ACCOUNT_DAILY_CAP;

    if (CONFIG.AUTO_PAUSE) {
      pauseAllCampaigns();
      message += '\nAll campaigns have been paused.';
    }

    sendAlert('Budget Cap Reached', message);
    return;
  }

  // Check campaign-level caps
  for (var campaignName in CONFIG.CAMPAIGN_CAPS) {
    var cap = CONFIG.CAMPAIGN_CAPS[campaignName];

    var campaigns = AdsApp.campaigns()
      .withCondition('Name = "' + campaignName + '"')
      .withCondition('Status = ENABLED')
      .get();

    while (campaigns.hasNext()) {
      var campaign = campaigns.next();
      var stats = campaign.getStatsFor(todayString, todayString);
      var spend = stats.getCost();

      if (spend >= cap) {
        var msg = campaignName + ' reached cap: €' + spend.toFixed(2) + ' / €' + cap;

        if (CONFIG.AUTO_PAUSE) {
          campaign.pause();
          // Add label for recovery
          campaign.applyLabel('AutoPaused-Budget');
          msg += ' - Campaign paused.';
        }

        sendAlert('Campaign Budget Cap', msg);
      }
    }
  }

  // Auto-recovery: Re-enable paused campaigns from yesterday
  if (CONFIG.AUTO_RECOVERY) {
    recoverPausedCampaigns();
  }
}

function pauseAllCampaigns() {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    campaign.pause();
    campaign.applyLabel('AutoPaused-Budget');
  }
}

function recoverPausedCampaigns() {
  // Check if label exists
  var labelIterator = AdsApp.labels()
    .withCondition('Name = "AutoPaused-Budget"')
    .get();

  if (!labelIterator.hasNext()) return;

  var campaigns = AdsApp.campaigns()
    .withCondition('LabelNames CONTAINS_ANY ["AutoPaused-Budget"]')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    campaign.enable();
    campaign.removeLabel('AutoPaused-Budget');
    Logger.log('Re-enabled: ' + campaign.getName());
  }
}

function sendAlert(subject, body) {
  var fullSubject = 'WARNING: ' + subject + ' - ' + AdsApp.currentAccount().getName();
  MailApp.sendEmail(CONFIG.EMAIL, fullSubject, body);
  Logger.log('Alert sent: ' + subject);
}
```

```javascript
/**
 * Multi-Condition Performance Rule Script
 *
 * More advanced than automated rules:
 * combines multiple conditions with AND/OR logic.
 *
 * Schedule: Daily
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Complex rule: Pause if ALL conditions met
  PAUSE_CONDITIONS: {
    minCost: 100,           // Spend > €100
    maxConversions: 0,      // 0 conversions
    minImpressions: 500,    // Had enough impressions
    dateRange: 'LAST_14_DAYS'
  },

  // Alert if ANY condition met
  ALERT_CONDITIONS: [
    { metric: 'CPA', operator: '>', value: 50, dateRange: 'LAST_7_DAYS' },
    { metric: 'CTR', operator: '<', value: 0.01, dateRange: 'LAST_7_DAYS' },
    { metric: 'ConvRate', operator: '<', value: 0.005, dateRange: 'LAST_7_DAYS' }
  ],

  // Dry run mode
  DRY_RUN: true
};

function main() {
  var keywordsToPause = [];
  var alertItems = [];

  var keywords = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .get();

  while (keywords.hasNext()) {
    var keyword = keywords.next();
    var stats = keyword.getStatsFor(CONFIG.PAUSE_CONDITIONS.dateRange);

    var cost = stats.getCost();
    var conversions = stats.getConversions();
    var impressions = stats.getImpressions();
    var clicks = stats.getClicks();

    // Check pause conditions (ALL must be true)
    if (cost >= CONFIG.PAUSE_CONDITIONS.minCost &&
        conversions <= CONFIG.PAUSE_CONDITIONS.maxConversions &&
        impressions >= CONFIG.PAUSE_CONDITIONS.minImpressions) {

      keywordsToPause.push({
        text: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        cost: cost,
        impressions: impressions,
        keyword: keyword
      });
    }

    // Check alert conditions (ANY can trigger)
    var cpa = conversions > 0 ? cost / conversions : 0;
    var ctr = impressions > 0 ? clicks / impressions : 0;
    var convRate = clicks > 0 ? conversions / clicks : 0;

    for (var i = 0; i < CONFIG.ALERT_CONDITIONS.length; i++) {
      var condition = CONFIG.ALERT_CONDITIONS[i];
      var metricValue = 0;

      switch (condition.metric) {
        case 'CPA': metricValue = cpa; break;
        case 'CTR': metricValue = ctr; break;
        case 'ConvRate': metricValue = convRate; break;
      }

      var triggered = false;
      if (condition.operator === '>' && metricValue > condition.value) triggered = true;
      if (condition.operator === '<' && metricValue < condition.value && cost > 50) triggered = true;

      if (triggered) {
        alertItems.push({
          keyword: keyword.getText(),
          campaign: keyword.getCampaign().getName(),
          condition: condition.metric + ' ' + condition.operator + ' ' + condition.value,
          actualValue: metricValue
        });
        break; // One alert per keyword is enough
      }
    }
  }

  // Execute pauses
  if (keywordsToPause.length > 0) {
    for (var j = 0; j < keywordsToPause.length; j++) {
      if (!CONFIG.DRY_RUN) {
        keywordsToPause[j].keyword.pause();
      }
    }
  }

  // Send report
  if (keywordsToPause.length > 0 || alertItems.length > 0) {
    sendReport(keywordsToPause, alertItems);
  }

  Logger.log('Processed. To pause: ' + keywordsToPause.length + ', Alerts: ' + alertItems.length);
}

function sendReport(toPause, alerts) {
  var subject = 'Performance Rules Report - ' + AdsApp.currentAccount().getName();
  var dryRunNote = CONFIG.DRY_RUN ? '[DRY RUN] ' : '';

  var body = dryRunNote + 'Performance Rules Report\n';
  body += '========================\n\n';

  if (toPause.length > 0) {
    body += 'KEYWORDS TO PAUSE (' + toPause.length + '):\n';
    body += '───────────────────────────\n';
    for (var i = 0; i < Math.min(20, toPause.length); i++) {
      body += '• "' + toPause[i].text + '"\n';
      body += '  Campaign: ' + toPause[i].campaign + '\n';
      body += '  Spend: €' + toPause[i].cost.toFixed(2) + ', 0 conversions\n\n';
    }
  }

  if (alerts.length > 0) {
    body += '\nALERTS (' + alerts.length + '):\n';
    body += '─────────────────────\n';
    for (var j = 0; j < Math.min(20, alerts.length); j++) {
      body += '• "' + alerts[j].keyword + '"\n';
      body += '  Triggered: ' + alerts[j].condition + '\n';
      body += '  Actual: ' + alerts[j].actualValue.toFixed(4) + '\n\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

### When Scripts vs Rules

```
RULES VS SCRIPTS DECISION GUIDE
════════════════════════════════

USE AUTOMATED RULES WHEN:
─────────────────────────
✓ Simple IF-THEN logic
✓ Single condition/action
✓ Standard metrics (CPA, CTR, etc.)
✓ No external data needed
✓ Quick setup desired
✓ Non-technical team

USE SCRIPTS WHEN:
─────────────────
✓ Complex calculations (e.g., ROAS thresholds)
✓ Combining multiple conditions
✓ External data integration (spreadsheets, API)
✓ Cross-entity logic (campaign + ad group)
✓ Custom reporting
✓ MCC-level automation
✓ Advanced alerting

HYBRID APPROACH:
────────────────
Rules for: Simple, time-sensitive actions
Scripts for: Complex logic, reporting
PMax/Smart bidding: Real-time optimization

EXAMPLE:
────────
Automated Rule: Pause keyword if CPA > €50
Script: Analyze N-grams and send report with suggestions
Smart Bidding: Real-time bid optimization
```