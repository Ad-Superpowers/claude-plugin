## Google Ads Script: Asset Group Monitor

```javascript
/**
 * Performance Max Asset Group Monitor
 *
 * Monitors PMax asset groups and sends
 * weekly performance reports.
 *
 * Features:
 * - Asset group performance comparison
 * - Conversion/ROAS tracking per AG
 * - Trend analysis
 * - Recommendations
 *
 * Schedule: Weekly on Monday
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Thresholds
  MIN_SPEND: 50,                 // Minimum spend for analysis
  LOW_ROAS_THRESHOLD: 1.5,       // ROAS below 1.5x = alert
  HIGH_CPA_MULTIPLIER: 1.5,      // CPA 1.5x above average

  // Date range
  DATE_RANGE: 'LAST_7_DAYS',
  COMPARE_RANGE: 'LAST_14_DAYS'
};

function main() {
  var assetGroupData = [];

  // Query asset group performance
  var query =
    'SELECT campaign.name, asset_group.name, asset_group.id, ' +
    'metrics.impressions, metrics.clicks, metrics.cost_micros, ' +
    'metrics.conversions, metrics.conversions_value ' +
    'FROM asset_group ' +
    'WHERE campaign.advertising_channel_type = "PERFORMANCE_MAX" ' +
    'AND segments.date DURING ' + CONFIG.DATE_RANGE;

  try {
    var report = AdsApp.report(query);
    var rows = report.rows();

    while (rows.hasNext()) {
      var row = rows.next();

      var costMicros = parseInt(row['metrics.cost_micros']) || 0;
      var cost = costMicros / 1000000;

      if (cost < CONFIG.MIN_SPEND) continue;

      var impressions = parseInt(row['metrics.impressions']) || 0;
      var clicks = parseInt(row['metrics.clicks']) || 0;
      var conversions = parseFloat(row['metrics.conversions']) || 0;
      var value = parseFloat(row['metrics.conversions_value']) || 0;

      assetGroupData.push({
        campaign: row['campaign.name'],
        assetGroup: row['asset_group.name'],
        impressions: impressions,
        clicks: clicks,
        cost: cost,
        conversions: conversions,
        value: value,
        ctr: impressions > 0 ? clicks / impressions : 0,
        cpc: clicks > 0 ? cost / clicks : 0,
        cpa: conversions > 0 ? cost / conversions : 0,
        roas: cost > 0 ? value / cost : 0,
        convRate: clicks > 0 ? conversions / clicks : 0
      });
    }
  } catch (e) {
    Logger.log('Query error: ' + e.message);
  }

  // Calculate averages for comparison
  var avgCPA = 0;
  var avgROAS = 0;
  var totalConv = 0;
  var totalCost = 0;
  var totalValue = 0;

  for (var i = 0; i < assetGroupData.length; i++) {
    totalConv += assetGroupData[i].conversions;
    totalCost += assetGroupData[i].cost;
    totalValue += assetGroupData[i].value;
  }

  avgCPA = totalConv > 0 ? totalCost / totalConv : 0;
  avgROAS = totalCost > 0 ? totalValue / totalCost : 0;

  // Identify issues
  var issues = [];
  var topPerformers = [];
  var lowPerformers = [];

  for (var j = 0; j < assetGroupData.length; j++) {
    var ag = assetGroupData[j];

    // Low ROAS
    if (ag.roas < CONFIG.LOW_ROAS_THRESHOLD && ag.conversions > 0) {
      lowPerformers.push({
        name: ag.assetGroup,
        campaign: ag.campaign,
        issue: 'Low ROAS: ' + ag.roas.toFixed(2) + 'x',
        cost: ag.cost,
        roas: ag.roas
      });
    }

    // High CPA
    if (ag.cpa > avgCPA * CONFIG.HIGH_CPA_MULTIPLIER && ag.conversions > 0) {
      issues.push({
        name: ag.assetGroup,
        campaign: ag.campaign,
        issue: 'High CPA: $' + ag.cpa.toFixed(2) + ' (avg: $' + avgCPA.toFixed(2) + ')'
      });
    }

    // Top performers
    if (ag.roas > avgROAS * 1.2 && ag.conversions >= 3) {
      topPerformers.push({
        name: ag.assetGroup,
        campaign: ag.campaign,
        roas: ag.roas,
        conversions: ag.conversions
      });
    }
  }

  // Sort
  assetGroupData.sort(function(a, b) { return b.value - a.value; });
  topPerformers.sort(function(a, b) { return b.roas - a.roas; });
  lowPerformers.sort(function(a, b) { return a.roas - b.roas; });

  // Send report
  sendReport(assetGroupData, topPerformers, lowPerformers, issues, avgCPA, avgROAS);
  Logger.log('Asset Group Monitor complete. Groups analyzed: ' + assetGroupData.length);
}

function sendReport(data, top, low, issues, avgCPA, avgROAS) {
  if (data.length === 0) {
    Logger.log('No asset groups with sufficient data');
    return;
  }

  var subject = 'PMax Asset Group Report - ' + AdsApp.currentAccount().getName();

  var body = 'Performance Max Asset Group Report\n';
  body += '===================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Period: ' + CONFIG.DATE_RANGE + '\n';
  body += 'Asset Groups Analyzed: ' + data.length + '\n\n';

  // Summary
  var totalSpend = 0;
  var totalConv = 0;
  var totalVal = 0;
  for (var i = 0; i < data.length; i++) {
    totalSpend += data[i].cost;
    totalConv += data[i].conversions;
    totalVal += data[i].value;
  }

  body += 'SUMMARY\n';
  body += '───────\n';
  body += 'Total Spend: $' + totalSpend.toFixed(2) + '\n';
  body += 'Total Conversions: ' + totalConv.toFixed(1) + '\n';
  body += 'Average CPA: $' + avgCPA.toFixed(2) + '\n';
  body += 'Average ROAS: ' + avgROAS.toFixed(2) + 'x\n\n';

  // Top Performers
  if (top.length > 0) {
    body += 'TOP PERFORMERS (' + top.length + '):\n';
    body += '──────────────────────────\n';
    for (var t = 0; t < Math.min(5, top.length); t++) {
      body += '• ' + top[t].name + '\n';
      body += '  ROAS: ' + top[t].roas.toFixed(2) + 'x | Conv: ' + top[t].conversions.toFixed(1) + '\n';
    }
    body += '\n';
  }

  // Low Performers
  if (low.length > 0) {
    body += 'NEEDS ATTENTION (' + low.length + '):\n';
    body += '──────────────────────────────\n';
    for (var l = 0; l < Math.min(5, low.length); l++) {
      body += '• ' + low[l].name + '\n';
      body += '  ' + low[l].issue + '\n';
    }
    body += '\n';
  }

  // All Asset Groups
  body += 'ALL ASSET GROUPS (by value):\n';
  body += '────────────────────────────\n';
  for (var d = 0; d < data.length; d++) {
    var ag = data[d];
    body += '• ' + ag.assetGroup + ' (' + ag.campaign + ')\n';
    body += '  Spend: $' + ag.cost.toFixed(2);
    body += ' | Conv: ' + ag.conversions.toFixed(1);
    body += ' | ROAS: ' + ag.roas.toFixed(2) + 'x\n';
  }

  body += '\n---\nGenerated by Asset Group Monitor';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Asset Variation Strategy

```
ASSET VARIATION BEST PRACTICES
══════════════════════════════

HEADLINE VARIATION:
───────────────────
Type 1: Brand Headlines
├── "[Brand] Official Store"
├── "Shop [Brand] Online"
└── "[Brand] - Since 2010"

Type 2: USP Headlines
├── "Free Shipping Above $50"
├── "100-Day Return Policy"
└── "Handmade in USA"

Type 3: Benefit Headlines
├── "Premium Quality"
├── "Sustainable Materials"
└── "Designed for Comfort"

Type 4: Action Headlines
├── "Shop Now & Save"
├── "Discover Our Collection"
└── "Get Yours Today"

Type 5: Offer Headlines
├── "Up to 50% Off"
├── "New Arrivals"
└── "Bestsellers Collection"

IMAGE VARIATION:
───────────────
Type 1: Product Only
├── Clean product shot
├── White background
└── Multiple angles

Type 2: Lifestyle
├── Product in use
├── Model wearing/using
└── Environment context

Type 3: Detail Shots
├── Close-up features
├── Material texture
└── Unique details

Type 4: Seasonal/Promotional
├── Sale imagery
├── Holiday themes
└── Limited edition visuals

VIDEO VARIATION:
───────────────
Type 1: Product Demo
├── How it works
├── Features showcase
└── Unboxing

Type 2: Testimonial
├── Customer reviews
├── Before/after
└── Social proof

Type 3: Brand Story
├── Company values
├── Behind the scenes
└── Founder story

Type 4: Quick Promo
├── Sale announcement
├── New arrivals
└── Limited offer
```

## Search Themes Examples

```
SEARCH THEMES EXAMPLES
═══════════════════════

ASSET GROUP: WOMEN'S WINTER JACKETS
────────────────────────────────────
1. "winter jacket women"
2. "warm jacket buy"
3. "[brand] winter jackets"
4. "parka women winter"
5. "winter jacket waterproof"
6. "long winter jacket women"
7. "women's coat warm"

ASSET GROUP: RUNNING SHOES
──────────────────────────
1. "running shoes"
2. "best running shoes"
3. "[brand] running"
4. "best running shoes 2025"
5. "running shoes beginners"
6. "running shoes cushioning"

ASSET GROUP: B2B SOFTWARE
─────────────────────────
1. "crm software"
2. "customer management system"
3. "sales automation tool"
4. "[brand] crm"
5. "crm for small business"
6. "customer relationship software"

UPDATING SEARCH THEMES:
───────────────────────
Monthly:
├── Check Search Terms report
├── Identify new converting terms
├── Add high-performers
├── Remove non-performers
└── Monitor brand vs non-brand ratio
```

## Creative Testing in PMax

```
CREATIVE TESTING IN PERFORMANCE MAX
═══════════════════════════════════

TESTING LIMITATIONS:
────────────────────
PMax has NO native A/B testing.
Google combines assets automatically.

WORKAROUNDS:
────────────

OPTION 1: SEQUENTIAL TESTING
───────────────────────────
Week 1-2: Asset Set A
Week 3-4: Asset Set B
Week 5-6: Analyze and pick winner

Drawbacks:
├── Timing effects (seasonality)
├── Slow
└── Not statistically pure

OPTION 2: SPLIT ASSET GROUPS
───────────────────────────
AG 1: Creative Concept A
├── All assets in one style
└── Specific messaging

AG 2: Creative Concept B
├── All assets in different style
└── Alternative messaging

Compare performance after 2-4 weeks.

Advantages:
✓ Parallel testing
✓ Better comparison
✓ Can test different audiences

Drawbacks:
├── Split budget
├── Possible audience overlap
└── More management

OPTION 3: CAMPAIGN EXPERIMENTS
─────────────────────────────
Google Ads Experiments (beta for PMax)
├── True A/B split
├── Statistically significant
└── Check availability in your account

OPTION 4: ASSET RATING MONITORING
────────────────────────────────
Upload multiple variations:
├── Track which get "Best" rating
├── Replace "Low" performers
└── Iteratively improve
```

## Asset Refresh Strategy

```
ASSET REFRESH CADENCE
═════════════════════

WEEKLY:
───────
□ Check asset ratings
□ Minor copy updates if needed
□ Urgent fixes (disapprovals, errors)

MONTHLY:
────────
□ Full asset performance review
□ Replace "Low" performers (20-30%)
□ Add new variations
□ Test new concepts

QUARTERLY:
──────────
□ Complete creative refresh
□ New photo shoots/videos
□ Seasonal updates
□ Brand guideline updates

SEASONAL:
─────────
□ Pre-season: New seasonal assets
├── 2-3 weeks before season starts
├── Holiday themes
└── Sale/promo assets

□ In-season: Monitor and optimize
├── Weekly performance check
├── Quick wins implementation
└── Budget shift toward winners

□ Post-season: Cleanup
├── Remove seasonal assets
├── Archive for next year
└── Return to evergreen content
```