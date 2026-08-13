# Scaling Calculator — Detailed Reference

## Detailed Break-Even Tables

### ROAS Break-Even Table

```
┌────────────────┬──────────────┬───────────────┬──────────────┐
│ GROSS MARGIN   │ BREAK-EVEN   │ TARGET ROAS   │ IDEAL ROAS   │
│ (after COGS)   │ ROAS         │ (10% profit)  │ (20% profit) │
├────────────────┼──────────────┼───────────────┼──────────────┤
│ 20%            │ 5.00x        │ 5.55x         │ 6.25x        │
│ 25%            │ 4.00x        │ 4.44x         │ 5.00x        │
│ 30%            │ 3.33x        │ 3.70x         │ 4.17x        │
│ 35%            │ 2.86x        │ 3.17x         │ 3.57x        │
│ 40%            │ 2.50x        │ 2.78x         │ 3.13x        │
│ 45%            │ 2.22x        │ 2.47x         │ 2.78x        │
│ 50%            │ 2.00x        │ 2.22x         │ 2.50x        │
│ 60%            │ 1.67x        │ 1.85x         │ 2.08x        │
└────────────────┴──────────────┴───────────────┴──────────────┘
```

### CPA Break-Even Table

```
┌────────────┬───────────┬──────────────┬──────────────┐
│ AOV        │ MARGIN    │ BREAK-EVEN   │ TARGET CPA   │
│            │           │ CPA          │ (20% profit) │
├────────────┼───────────┼──────────────┼──────────────┤
│ $50        │ 40%       │ $20          │ $16          │
│ $75        │ 40%       │ $30          │ $24          │
│ $100       │ 40%       │ $40          │ $32          │
│ $100       │ 50%       │ $50          │ $40          │
│ $150       │ 35%       │ $52.50       │ $42          │
│ $200       │ 30%       │ $60          │ $48          │
│ $300       │ 25%       │ $75          │ $60          │
└────────────┴───────────┴──────────────┴──────────────┘
```

## iROAS Calculation Methods

```
iROAS CALCULATION METHODS
═════════════════════════

METHOD 1: GEO EXPERIMENT
──────────────────────────
1. Split audiences geographically
2. Group A: Current budget
3. Group B: Increased budget
4. Measure difference in revenue
5. Calculate: (Rev B - Rev A) / (Budget B - Budget A)

METHOD 2: BUDGET STEP TEST
───────────────────────────
1. Measure performance per budget level
2. Plot revenue vs spend curve
3. Calculate marginal return per step

Budget Steps:
├── Week 1: $1,000 → Revenue $4,500 (4.5x)
├── Week 2: $1,500 → Revenue $6,000 (4.0x)
│   └── iROAS step: ($6,000-$4,500)/($1,500-$1,000) = 3.0x
├── Week 3: $2,000 → Revenue $7,200 (3.6x)
│   └── iROAS step: ($7,200-$6,000)/($2,000-$1,500) = 2.4x
└── Week 4: $2,500 → Revenue $8,000 (3.2x)
    └── iROAS step: ($8,000-$7,200)/($2,500-$2,000) = 1.6x

METHOD 3: HOLDOUT EXPERIMENT
──────────────────────────────
1. Pause campaign for subset audience
2. Measure organic/other channel lift
3. Difference = incremental value
4. Calculate true incrementality %

Typical Incrementality:
├── Brand campaigns: 30-60% incremental
├── Non-brand Search: 60-80% incremental
├── Shopping: 50-70% incremental
├── PMax: 60-80% incremental
└── Remarketing: 20-50% incremental
```

## MER (Marketing Efficiency Ratio) Analysis

```
MER ANALYSIS EXAMPLE:
──────────────────────
Month 1 ($20k spend):
├── Google Ads Revenue: $70k (ROAS 3.5x)
├── Meta Ads Revenue: $30k (ROAS 3.0x)
├── Organic/Direct Revenue: $50k
├── Total Revenue: $150k
└── MER: $150k / $20k = 7.5x

Month 2 ($30k spend, +50%):
├── Google Ads Revenue: $90k (ROAS 3.0x)
├── Meta Ads Revenue: $40k (ROAS 2.7x)
├── Organic/Direct Revenue: $70k (+40% halo)
├── Total Revenue: $200k
└── MER: $200k / $30k = 6.7x

Conclusion:
├── Channel ROAS dropped
├── MER dropped less (7.5x → 6.7x)
├── Brand lift boosted organic
└── Scaling was profitable overall
```

## Google Ads Script: Scaling Monitor

```javascript
/**
 * Scaling Performance Monitor
 *
 * Features:
 * - Tracks performance during budget changes
 * - Calculates incremental metrics
 * - Alerts on significant performance drops
 * - Recommends scaling decisions
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Set BREAK_EVEN_ROAS for your business
 * 3. Schedule: Daily
 */

var CONFIG = {
  EMAIL: 'you@example.com',
  BREAK_EVEN_ROAS: 2.5,
  ROAS_DROP_ALERT: 0.20,
  CPA_INCREASE_ALERT: 0.25,
  MIN_SPEND_FOR_ANALYSIS: 100,
  CURRENT_PERIOD: 'LAST_7_DAYS',
  PREVIOUS_PERIOD: 14
};

function main() {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .withCondition('Cost > ' + CONFIG.MIN_SPEND_FOR_ANALYSIS)
    .forDateRange(CONFIG.CURRENT_PERIOD)
    .get();

  var report = {
    date: new Date().toDateString(),
    accountName: AdsApp.currentAccount().getName(),
    campaigns: [], alerts: [], recommendations: []
  };

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var analysis = analyzeCampaign(campaign);
    report.campaigns.push(analysis);
    if (analysis.alerts.length > 0) {
      report.alerts = report.alerts.concat(analysis.alerts);
    }
    if (analysis.recommendation) {
      report.recommendations.push(analysis.recommendation);
    }
  }

  if (report.alerts.length > 0 || report.recommendations.length > 0) {
    sendScalingReport(report);
  }
  logSummary(report);
}

function analyzeCampaign(campaign) {
  var name = campaign.getName();
  var currentStats = campaign.getStatsFor(CONFIG.CURRENT_PERIOD);
  var currentSpend = currentStats.getCost();
  var currentRevenue = currentStats.getConversionValue();
  var currentConversions = currentStats.getConversions();
  var currentROAS = currentSpend > 0 ? currentRevenue / currentSpend : 0;
  var currentCPA = currentConversions > 0 ? currentSpend / currentConversions : 0;

  var today = new Date();
  var previousEnd = new Date(today.getTime() - (7 * 24 * 60 * 60 * 1000));
  var previousStart = new Date(previousEnd.getTime() - (7 * 24 * 60 * 60 * 1000));
  var previousStats = campaign.getStatsFor(formatDate(previousStart), formatDate(previousEnd));
  var previousSpend = previousStats.getCost();
  var previousRevenue = previousStats.getConversionValue();
  var previousConversions = previousStats.getConversions();
  var previousROAS = previousSpend > 0 ? previousRevenue / previousSpend : 0;
  var previousCPA = previousConversions > 0 ? previousSpend / previousConversions : 0;

  var spendChange = previousSpend > 0 ? (currentSpend - previousSpend) / previousSpend : 0;
  var roasChange = previousROAS > 0 ? (currentROAS - previousROAS) / previousROAS : 0;
  var cpaChange = previousCPA > 0 ? (currentCPA - previousCPA) / previousCPA : 0;

  var iROAS = 0, iCPA = 0;
  if (spendChange > 0) {
    var incrementalSpend = currentSpend - previousSpend;
    var incrementalRevenue = currentRevenue - previousRevenue;
    var incrementalConversions = currentConversions - previousConversions;
    iROAS = incrementalSpend > 0 ? incrementalRevenue / incrementalSpend : 0;
    iCPA = incrementalConversions > 0 ? incrementalSpend / incrementalConversions : 0;
  }

  var alerts = [];
  if (roasChange < -CONFIG.ROAS_DROP_ALERT) {
    alerts.push({
      type: 'ROAS_DROP', campaign: name,
      message: 'ROAS dropped ' + Math.abs(roasChange * 100).toFixed(1) + '%',
      current: currentROAS.toFixed(2), previous: previousROAS.toFixed(2)
    });
  }
  if (cpaChange > CONFIG.CPA_INCREASE_ALERT) {
    alerts.push({
      type: 'CPA_INCREASE', campaign: name,
      message: 'CPA increased ' + (cpaChange * 100).toFixed(1) + '%',
      current: currentCPA.toFixed(2), previous: previousCPA.toFixed(2)
    });
  }

  var recommendation = null;
  if (currentROAS > CONFIG.BREAK_EVEN_ROAS * 1.5 && spendChange <= 0) {
    recommendation = {
      campaign: name, action: 'SCALE_UP',
      reason: 'ROAS ' + currentROAS.toFixed(2) + 'x is well above break-even. Consider +15-20% budget increase.'
    };
  } else if (iROAS > 0 && iROAS < CONFIG.BREAK_EVEN_ROAS) {
    recommendation = {
      campaign: name, action: 'PAUSE_SCALING',
      reason: 'Incremental ROAS ' + iROAS.toFixed(2) + 'x is below break-even.'
    };
  } else if (currentROAS < CONFIG.BREAK_EVEN_ROAS * 0.8) {
    recommendation = {
      campaign: name, action: 'REDUCE_BUDGET',
      reason: 'ROAS ' + currentROAS.toFixed(2) + 'x is below break-even.'
    };
  }

  return {
    name: name, currentSpend: currentSpend, currentROAS: currentROAS,
    currentCPA: currentCPA, spendChange: spendChange, roasChange: roasChange,
    iROAS: iROAS, iCPA: iCPA, alerts: alerts, recommendation: recommendation
  };
}

function formatDate(date) {
  return Utilities.formatDate(date, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');
}

function sendScalingReport(report) {
  var subject = 'Scaling Monitor Alert - ' + report.accountName;
  var body = 'Scaling Performance Report\n==========================\n';
  body += 'Date: ' + report.date + '\n';
  body += 'Break-Even ROAS Target: ' + CONFIG.BREAK_EVEN_ROAS + 'x\n\n';

  if (report.alerts.length > 0) {
    body += 'ALERTS:\n';
    for (var i = 0; i < report.alerts.length; i++) {
      var alert = report.alerts[i];
      body += '- [' + alert.type + '] ' + alert.campaign + '\n';
      body += '  ' + alert.message + '\n';
      body += '  Previous: ' + alert.previous + ' -> Current: ' + alert.current + '\n\n';
    }
  }

  if (report.recommendations.length > 0) {
    body += 'RECOMMENDATIONS:\n';
    for (var j = 0; j < report.recommendations.length; j++) {
      var rec = report.recommendations[j];
      body += '- [' + rec.action + '] ' + rec.campaign + '\n';
      body += '  ' + rec.reason + '\n\n';
    }
  }

  body += '\n---\nGenerated by Scaling Monitor Script';
  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}

function logSummary(report) {
  Logger.log('=== Scaling Monitor Summary ===');
  Logger.log('Campaigns analyzed: ' + report.campaigns.length);
  Logger.log('Alerts: ' + report.alerts.length);
  for (var i = 0; i < report.campaigns.length; i++) {
    var c = report.campaigns[i];
    Logger.log(c.name + ': ROAS=' + c.currentROAS.toFixed(2) +
               ', Spend Change=' + (c.spendChange * 100).toFixed(1) + '%' +
               (c.iROAS > 0 ? ', iROAS=' + c.iROAS.toFixed(2) : ''));
  }
}
```
