## Placement Management

### Placement Performance Analysis

```
PLACEMENT OPTIMIZATION
════════════════════════

WHERE TO FIND PLACEMENT DATA:
────────────────────────────
Google Ads → Campaigns → [Campaign] → Placements
├── Where ads showed: Automatic placements
└── Targeted: Your added placements

PLACEMENT METRICS:
──────────────────
┌────────────────────┬─────────────────────────────────────┐
│ Metric             │ What to look for                    │
├────────────────────┼─────────────────────────────────────┤
│ Impressions        │ Volume per site                     │
│ CTR                │ Engagement quality                  │
│ Conversions        │ Actual value                        │
│ Conv Rate          │ Site quality                        │
│ Cost/Conv          │ Efficiency                          │
│ Viewability        │ Visibility (if available)           │
└────────────────────┴─────────────────────────────────────┘

EXCLUSION CRITERIA:
───────────────────
Exclude placements that:
├── High impressions, no conversions, high spend
├── Very low CTR (<0.01%)
├── Irrelevant content (brand safety)
├── Mobile gaming apps (often accidental clicks)
└── Low quality / MFA sites

COMMON EXCLUSIONS:
──────────────────
□ App categories to exclude:
├── Games (unless relevant)
├── Comics
├── Entertainment (often kids content)
└── Wallpapers/Screensavers

□ Site types to exclude:
├── Parked domains
├── Error pages
├── Below the fold only
└── Sensitive content

EXCLUSION SETUP:
────────────────
1. Campaign → Settings → Additional Settings
2. Content exclusions
3. Placements → Exclusions tab
4. Upload exclusion list or add per site
```

### Placement Exclusion Script

```javascript
/**
 * Display Placement Analyzer
 *
 * Analyzes placements and identifies
 * low performers for exclusion.
 *
 * Features:
 * - High spend / no conversion detection
 * - CTR anomaly detection
 * - App placement analysis
 * - Automated exclusion suggestions
 *
 * Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Thresholds for exclusion suggestion
  MIN_COST_FOR_ANALYSIS: 5,        // Min $5 spend
  MIN_IMPRESSIONS: 100,            // Min 100 impressions
  MAX_COST_NO_CONV: 50,            // $50+ spend, 0 conversions
  MIN_CTR: 0.0005,                 // CTR < 0.05%

  // Date range
  DATE_RANGE: 'LAST_30_DAYS',

  // Exclude mobile apps by default
  EXCLUDE_APPS: true
};

function main() {
  var displayCampaigns = AdsApp.campaigns()
    .withCondition('AdvertisingChannelType = DISPLAY')
    .withCondition('Status = ENABLED')
    .get();

  var placementsToExclude = [];
  var appsToExclude = [];

  while (displayCampaigns.hasNext()) {
    var campaign = displayCampaigns.next();

    // Analyze automatic placements
    var placementReport = campaign.targeting().placements()
      .forDateRange(CONFIG.DATE_RANGE)
      .get();

    while (placementReport.hasNext()) {
      var placement = placementReport.next();
      var stats = placement.getStatsFor(CONFIG.DATE_RANGE);

      var impressions = stats.getImpressions();
      var clicks = stats.getClicks();
      var cost = stats.getCost();
      var conversions = stats.getConversions();
      var url = placement.getUrl();

      if (impressions < CONFIG.MIN_IMPRESSIONS) continue;
      if (cost < CONFIG.MIN_COST_FOR_ANALYSIS) continue;

      var ctr = clicks / impressions;
      var shouldExclude = false;
      var reason = '';

      // High spend, no conversions
      if (cost > CONFIG.MAX_COST_NO_CONV && conversions === 0) {
        shouldExclude = true;
        reason = 'High spend ($' + cost.toFixed(2) + '), 0 conversions';
      }

      // Very low CTR
      if (ctr < CONFIG.MIN_CTR && impressions > 1000) {
        shouldExclude = true;
        reason = 'Very low CTR: ' + (ctr * 100).toFixed(3) + '%';
      }

      // Mobile app detection
      if (CONFIG.EXCLUDE_APPS && url.indexOf('mobileapp::') === 0) {
        appsToExclude.push({
          campaign: campaign.getName(),
          url: url,
          cost: cost,
          impressions: impressions,
          conversions: conversions
        });
      }

      if (shouldExclude) {
        placementsToExclude.push({
          campaign: campaign.getName(),
          url: url,
          cost: cost,
          impressions: impressions,
          clicks: clicks,
          ctr: ctr,
          conversions: conversions,
          reason: reason
        });
      }
    }
  }

  // Sort by cost
  placementsToExclude.sort(function(a, b) { return b.cost - a.cost; });
  appsToExclude.sort(function(a, b) { return b.cost - a.cost; });

  // Send report
  if (placementsToExclude.length > 0 || appsToExclude.length > 0) {
    sendPlacementReport(placementsToExclude, appsToExclude);
  }

  Logger.log('Placement analysis complete.');
  Logger.log('Placements to exclude: ' + placementsToExclude.length);
  Logger.log('Apps to exclude: ' + appsToExclude.length);
}

function sendPlacementReport(placements, apps) {
  var subject = 'Display Placement Analysis - ' + AdsApp.currentAccount().getName();

  var body = 'Display Placement Analysis Report\n';
  body += '=================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Period: ' + CONFIG.DATE_RANGE + '\n\n';

  if (placements.length > 0) {
    body += 'PLACEMENTS TO EXCLUDE (' + placements.length + '):\n';
    body += '──────────────────────────────────────\n\n';

    var totalWaste = 0;
    for (var i = 0; i < Math.min(20, placements.length); i++) {
      var p = placements[i];
      totalWaste += p.cost;
      body += '- ' + truncateUrl(p.url, 50) + '\n';
      body += '  Campaign: ' + p.campaign + '\n';
      body += '  Spend: $' + p.cost.toFixed(2);
      body += ' | Impr: ' + p.impressions;
      body += ' | Conv: ' + p.conversions + '\n';
      body += '  Reason: ' + p.reason + '\n\n';
    }

    body += 'Total potential savings: $' + totalWaste.toFixed(2) + '\n\n';
  }

  if (apps.length > 0) {
    body += 'MOBILE APPS TO REVIEW (' + apps.length + '):\n';
    body += '────────────────────────────────────\n\n';

    var appSpend = 0;
    for (var j = 0; j < Math.min(10, apps.length); j++) {
      var app = apps[j];
      appSpend += app.cost;
      body += '- ' + app.url.replace('mobileapp::', '') + '\n';
      body += '  Spend: $' + app.cost.toFixed(2);
      body += ' | Conv: ' + app.conversions + '\n\n';
    }

    body += 'Total app spend: $' + appSpend.toFixed(2) + '\n';
    body += 'Consider excluding app categories in campaign settings.\n\n';
  }

  body += '\n---\nGenerated by Display Placement Analyzer';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}

function truncateUrl(url, maxLength) {
  if (url.length <= maxLength) return url;
  return url.substring(0, maxLength - 3) + '...';
}
```

### Placement Exclusion Script

```javascript
/**
 * Display Placement Analyzer
 *
 * Analyzes placements and identifies
 * low performers for exclusion.
 *
 * Features:
 * - High spend / no conversion detection
 * - CTR anomaly detection
 * - App placement analysis
 * - Automated exclusion suggestions
 *
 * Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Thresholds for exclusion suggestion
  MIN_COST_FOR_ANALYSIS: 5,        // Min $5 spend
  MIN_IMPRESSIONS: 100,            // Min 100 impressions
  MAX_COST_NO_CONV: 50,            // $50+ spend, 0 conversions
  MIN_CTR: 0.0005,                 // CTR < 0.05%

  // Date range
  DATE_RANGE: 'LAST_30_DAYS',

  // Exclude mobile apps by default
  EXCLUDE_APPS: true
};

function main() {
  var displayCampaigns = AdsApp.campaigns()
    .withCondition('AdvertisingChannelType = DISPLAY')
    .withCondition('Status = ENABLED')
    .get();

  var placementsToExclude = [];
  var appsToExclude = [];

  while (displayCampaigns.hasNext()) {
    var campaign = displayCampaigns.next();

    // Analyze automatic placements
    var placementReport = campaign.targeting().placements()
      .forDateRange(CONFIG.DATE_RANGE)
      .get();

    while (placementReport.hasNext()) {
      var placement = placementReport.next();
      var stats = placement.getStatsFor(CONFIG.DATE_RANGE);

      var impressions = stats.getImpressions();
      var clicks = stats.getClicks();
      var cost = stats.getCost();
      var conversions = stats.getConversions();
      var url = placement.getUrl();

      if (impressions < CONFIG.MIN_IMPRESSIONS) continue;
      if (cost < CONFIG.MIN_COST_FOR_ANALYSIS) continue;

      var ctr = clicks / impressions;
      var shouldExclude = false;
      var reason = '';

      // High spend, no conversions
      if (cost > CONFIG.MAX_COST_NO_CONV && conversions === 0) {
        shouldExclude = true;
        reason = 'High spend ($' + cost.toFixed(2) + '), 0 conversions';
      }

      // Very low CTR
      if (ctr < CONFIG.MIN_CTR && impressions > 1000) {
        shouldExclude = true;
        reason = 'Very low CTR: ' + (ctr * 100).toFixed(3) + '%';
      }

      // Mobile app detection
      if (CONFIG.EXCLUDE_APPS && url.indexOf('mobileapp::') === 0) {
        appsToExclude.push({
          campaign: campaign.getName(),
          url: url,
          cost: cost,
          impressions: impressions,
          conversions: conversions
        });
      }

      if (shouldExclude) {
        placementsToExclude.push({
          campaign: campaign.getName(),
          url: url,
          cost: cost,
          impressions: impressions,
          clicks: clicks,
          ctr: ctr,
          conversions: conversions,
          reason: reason
        });
      }
    }
  }

  // Sort by cost
  placementsToExclude.sort(function(a, b) { return b.cost - a.cost; });
  appsToExclude.sort(function(a, b) { return b.cost - a.cost; });

  // Send report
  if (placementsToExclude.length > 0 || appsToExclude.length > 0) {
    sendPlacementReport(placementsToExclude, appsToExclude);
  }

  Logger.log('Placement analysis complete.');
  Logger.log('Placements to exclude: ' + placementsToExclude.length);
  Logger.log('Apps to exclude: ' + appsToExclude.length);
}

function sendPlacementReport(placements, apps) {
  var subject = 'Display Placement Analysis - ' + AdsApp.currentAccount().getName();

  var body = 'Display Placement Analysis Report\n';
  body += '=================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Period: ' + CONFIG.DATE_RANGE + '\n\n';

  if (placements.length > 0) {
    body += 'PLACEMENTS TO EXCLUDE (' + placements.length + '):\n';
    body += '──────────────────────────────────────\n\n';

    var totalWaste = 0;
    for (var i = 0; i < Math.min(20, placements.length); i++) {
      var p = placements[i];
      totalWaste += p.cost;
      body += '- ' + truncateUrl(p.url, 50) + '\n';
      body += '  Campaign: ' + p.campaign + '\n';
      body += '  Spend: $' + p.cost.toFixed(2);
      body += ' | Impr: ' + p.impressions;
      body += ' | Conv: ' + p.conversions + '\n';
      body += '  Reason: ' + p.reason + '\n\n';
    }

    body += 'Total potential savings: $' + totalWaste.toFixed(2) + '\n\n';
  }

  if (apps.length > 0) {
    body += 'MOBILE APPS TO REVIEW (' + apps.length + '):\n';
    body += '────────────────────────────────────\n\n';

    var appSpend = 0;
    for (var j = 0; j < Math.min(10, apps.length); j++) {
      var app = apps[j];
      appSpend += app.cost;
      body += '- ' + app.url.replace('mobileapp::', '') + '\n';
      body += '  Spend: $' + app.cost.toFixed(2);
      body += ' | Conv: ' + app.conversions + '\n\n';
    }

    body += 'Total app spend: $' + appSpend.toFixed(2) + '\n';
    body += 'Consider excluding app categories in campaign settings.\n\n';
  }

  body += '\n---\nGenerated by Display Placement Analyzer';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}

function truncateUrl(url, maxLength) {
  if (url.length <= maxLength) return url;
  return url.substring(0, maxLength - 3) + '...';
}
```