---
name: google-ads-scripts-library
description: "This skill should be used when the user asks to \"set up Google Ads Scripts\", \"automate bid adjustments with scripts\", \"create budget pacing alerts\", \"detect performance anomalies\", or mentions \"N-gram analysis script\", \"broken URL checker\", or \"Google Ads automation scripts\". Do NOT use for: manual campaign optimization (use performance-troubleshooter), keyword strategy planning (use keyword-strategy-planner), or Quality Score improvement (use quality-score-optimizer)."
---
# Google Ads Scripts Library

Complete library with 15 production-ready Google Ads Scripts for automation, monitoring, and optimization.

## 2026 Context: Scripts vs. MCP Tools

Google Ads Scripts run inside the Google Ads UI and use the legacy AdsApp object. They are useful for scheduled, account-level automation that runs without human intervention. For ad-hoc analysis and conversational workflows, use the Ad Superpowers MCP tools instead:

```
# Pull anomaly data via MCP (no script required):
google_ads_run_gaql(query="
  SELECT campaign.name, metrics.cost_micros,
         metrics.conversions, metrics.cost_per_conversion
  FROM campaign
  WHERE segments.date DURING YESTERDAY
    AND campaign.status = 'ENABLED'
  ORDER BY metrics.cost_micros DESC
  LIMIT 20
")

# Scripts are best for: unattended scheduled alerts,
# automated pausing/bidding, and spreadsheet exports.
# MCP is best for: analysis, diagnosis, recommendations.
```

**Smart Bidding note (2026):** Scripts that manually adjust bids (e.g., device/dayparting modifiers) can conflict with Smart Bidding signals. Only apply manual bid adjustments to campaigns using Manual CPC or non-Smart strategies. For Smart Bidding campaigns, use budget and target adjustments instead.

**AI Max (2026):** Search campaigns with AI Max subtype use fully automated query matching — search term scripts still work but you cannot add exact/phrase negatives via script directly. Use campaign-level negative keyword lists.

## Scripts Overview

```
TOP 15 GOOGLE ADS SCRIPTS
═════════════════════════

MONITORING & ALERTS:
├── 1. Performance Anomaly Detector
├── 2. Budget Pacing Monitor
├── 3. Broken URL Checker
├── 4. Quality Score Tracker
└── 5. Zero Impressions Alert

OPTIMIZATION:
├── 6. N-Gram Analysis
├── 7. Search Query Mining
├── 8. Negative Keyword Builder
├── 9. Bid Adjustment by Hour/Day
└── 10. Low Performer Pauser

REPORTING:
├── 11. Daily/Weekly Report Generator
├── 12. Competitor Auction Insights
├── 13. Campaign Performance Tracker
├── 14. Ad Extension Monitor
└── 15. Account Health Dashboard

SETUP INSTRUCTIONS (for all scripts):
─────────────────────────────────────
1. Google Ads → Tools & Settings → Bulk Actions → Scripts
2. + New Script
3. Paste code
4. Authorize (first run)
5. Preview → Run (test)
6. Schedule (daily/hourly)
```

## Script 1: Performance Anomaly Detector

```javascript
/**
 * SCRIPT 1: Performance Anomaly Detector
 *
 * Detects significant deviations in key metrics
 * and sends email alerts.
 *
 * Features:
 * - CPA/ROAS anomaly detection
 * - Spend pacing alerts
 * - Conversion volume drops
 * - Statistical outlier detection
 *
 * Schedule: Daily at 9:00
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Anomaly thresholds (% change vs 7-day average)
  CPA_THRESHOLD: 0.30,         // Alert on 30% CPA increase
  ROAS_THRESHOLD: 0.25,        // Alert on 25% ROAS drop
  SPEND_THRESHOLD: 0.40,       // Alert on 40% spend deviation
  CONV_THRESHOLD: 0.35,        // Alert on 35% conversion drop

  // Minimum values for analysis
  MIN_CONVERSIONS: 5,
  MIN_SPEND: 50,

  // Lookback period
  LOOKBACK_DAYS: 7
};

function main() {
  var anomalies = [];

  // Analyze campaigns
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var campaignAnomalies = detectAnomalies(campaign);
    anomalies = anomalies.concat(campaignAnomalies);
  }

  // Send alert if anomalies found
  if (anomalies.length > 0) {
    sendAnomalyAlert(anomalies);
  }

  Logger.log('Anomaly detection complete. Found: ' + anomalies.length + ' anomalies');
}

function detectAnomalies(campaign) {
  var anomalies = [];
  var name = campaign.getName();

  // Get yesterday's stats
  var yesterday = getDateString(1);
  var dayBeforeYesterday = getDateString(2);
  var yesterdayStats = campaign.getStatsFor(dayBeforeYesterday, yesterday);

  // Get 7-day average stats
  var weekAgo = getDateString(8);
  var weekStats = campaign.getStatsFor(weekAgo, dayBeforeYesterday);

  var yesterdaySpend = yesterdayStats.getCost();
  var yesterdayConv = yesterdayStats.getConversions();
  var yesterdayValue = yesterdayStats.getConversionValue();

  // Skip low-volume campaigns
  if (yesterdaySpend < CONFIG.MIN_SPEND) return anomalies;

  // Calculate averages
  var avgDailySpend = weekStats.getCost() / 7;
  var avgDailyConv = weekStats.getConversions() / 7;

  // Calculate metrics
  var yesterdayCPA = yesterdayConv > 0 ? yesterdaySpend / yesterdayConv : 0;
  var yesterdayROAS = yesterdaySpend > 0 ? yesterdayValue / yesterdaySpend : 0;

  var avgCPA = avgDailyConv > 0 ? (weekStats.getCost() / 7) / avgDailyConv : 0;
  var avgROAS = avgDailySpend > 0 ?
    (weekStats.getConversionValue() / 7) / avgDailySpend : 0;

  // Check for anomalies
  // CPA spike
  if (avgCPA > 0 && yesterdayCPA > avgCPA * (1 + CONFIG.CPA_THRESHOLD)) {
    anomalies.push({
      campaign: name,
      type: 'CPA_SPIKE',
      yesterday: yesterdayCPA.toFixed(2),
      average: avgCPA.toFixed(2),
      change: ((yesterdayCPA / avgCPA - 1) * 100).toFixed(1) + '%'
    });
  }

  // ROAS drop
  if (avgROAS > 0 && yesterdayROAS < avgROAS * (1 - CONFIG.ROAS_THRESHOLD)) {
    anomalies.push({
      campaign: name,
      type: 'ROAS_DROP',
      yesterday: yesterdayROAS.toFixed(2),
      average: avgROAS.toFixed(2),
      change: ((yesterdayROAS / avgROAS - 1) * 100).toFixed(1) + '%'
    });
  }

  // Spend anomaly
  if (avgDailySpend > 0) {
    var spendDiff = Math.abs(yesterdaySpend - avgDailySpend) / avgDailySpend;
    if (spendDiff > CONFIG.SPEND_THRESHOLD) {
      anomalies.push({
        campaign: name,
        type: yesterdaySpend > avgDailySpend ? 'SPEND_SPIKE' : 'SPEND_DROP',
        yesterday: yesterdaySpend.toFixed(2),
        average: avgDailySpend.toFixed(2),
        change: ((yesterdaySpend / avgDailySpend - 1) * 100).toFixed(1) + '%'
      });
    }
  }

  // Conversion drop
  if (avgDailyConv >= CONFIG.MIN_CONVERSIONS &&
      yesterdayConv < avgDailyConv * (1 - CONFIG.CONV_THRESHOLD)) {
    anomalies.push({
      campaign: name,
      type: 'CONVERSION_DROP',
      yesterday: yesterdayConv.toFixed(0),
      average: avgDailyConv.toFixed(1),
      change: ((yesterdayConv / avgDailyConv - 1) * 100).toFixed(1) + '%'
    });
  }

  return anomalies;
}

function getDateString(daysAgo) {
  var date = new Date();
  date.setDate(date.getDate() - daysAgo);
  return Utilities.formatDate(date, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');
}

function sendAnomalyAlert(anomalies) {
  var subject = 'Performance Anomaly Alert - ' + AdsApp.currentAccount().getName();

  var body = 'Performance Anomaly Detection Report\n';
  body += '====================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Date: ' + new Date().toDateString() + '\n\n';
  body += 'ANOMALIES DETECTED:\n';
  body += '───────────────────\n\n';

  for (var i = 0; i < anomalies.length; i++) {
    var a = anomalies[i];
    body += '[' + a.type + '] ' + a.campaign + '\n';
    body += '  Yesterday: ' + a.yesterday + '\n';
    body += '  7-Day Avg: ' + a.average + '\n';
    body += '  Change: ' + a.change + '\n\n';
  }

  body += '\n---\nGenerated by Performance Anomaly Detector';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Script 2: Budget Pacing Monitor

```javascript
/**
 * SCRIPT 2: Budget Pacing Monitor
 *
 * Monitors budget spending pace and predicts
 * under/overspend scenarios.
 *
 * Schedule: Daily at 10:00
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Pacing thresholds
  UNDERPACE_ALERT: 0.15,    // Alert if >15% behind pace
  OVERPACE_ALERT: 0.10,     // Alert if >10% ahead of pace

  // Include campaigns with budget > this
  MIN_DAILY_BUDGET: 20
};

function main() {
  var today = new Date();
  var dayOfMonth = today.getDate();
  var daysInMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();
  var percentMonthPassed = dayOfMonth / daysInMonth;

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var pacingReport = [];

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var budget = campaign.getBudget().getAmount();

    if (budget < CONFIG.MIN_DAILY_BUDGET) continue;

    var monthlyBudget = budget * daysInMonth;
    var expectedSpend = monthlyBudget * percentMonthPassed;

    // Get month-to-date spend
    var firstOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
    var stats = campaign.getStatsFor(
      formatDate(firstOfMonth),
      formatDate(today)
    );
    var actualSpend = stats.getCost();

    var pacePercent = expectedSpend > 0 ? actualSpend / expectedSpend : 0;
    var variance = pacePercent - 1;

    var status = 'ON_PACE';
    if (variance < -CONFIG.UNDERPACE_ALERT) {
      status = 'UNDERPACING';
    } else if (variance > CONFIG.OVERPACE_ALERT) {
      status = 'OVERPACING';
    }

    if (status !== 'ON_PACE') {
      pacingReport.push({
        campaign: campaign.getName(),
        dailyBudget: budget,
        monthlyBudget: monthlyBudget,
        expectedSpend: expectedSpend,
        actualSpend: actualSpend,
        pacePercent: pacePercent,
        status: status,
        projectedMonthEnd: actualSpend / percentMonthPassed
      });
    }
  }

  if (pacingReport.length > 0) {
    sendPacingReport(pacingReport, dayOfMonth, daysInMonth);
  }

  Logger.log('Pacing check complete. Issues found: ' + pacingReport.length);
}

function formatDate(date) {
  return Utilities.formatDate(date, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');
}

function sendPacingReport(report, dayOfMonth, daysInMonth) {
  var subject = 'Budget Pacing Alert - ' + AdsApp.currentAccount().getName();

  var body = 'Budget Pacing Report\n';
  body += '====================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Day of Month: ' + dayOfMonth + ' / ' + daysInMonth + '\n\n';

  var underpacing = report.filter(function(r) { return r.status === 'UNDERPACING'; });
  var overpacing = report.filter(function(r) { return r.status === 'OVERPACING'; });

  if (underpacing.length > 0) {
    body += 'UNDERPACING CAMPAIGNS:\n';
    body += '──────────────────────\n';
    for (var i = 0; i < underpacing.length; i++) {
      var c = underpacing[i];
      body += '  ' + c.campaign + '\n';
      body += '  Expected: €' + c.expectedSpend.toFixed(2) + '\n';
      body += '  Actual: €' + c.actualSpend.toFixed(2) + '\n';
      body += '  Pace: ' + (c.pacePercent * 100).toFixed(1) + '%\n';
      body += '  Projected month-end: €' + c.projectedMonthEnd.toFixed(2) +
              ' (Budget: €' + c.monthlyBudget.toFixed(2) + ')\n\n';
    }
  }

  if (overpacing.length > 0) {
    body += 'OVERPACING CAMPAIGNS:\n';
    body += '─────────────────────\n';
    for (var j = 0; j < overpacing.length; j++) {
      var c = overpacing[j];
      body += '  ' + c.campaign + '\n';
      body += '  Expected: €' + c.expectedSpend.toFixed(2) + '\n';
      body += '  Actual: €' + c.actualSpend.toFixed(2) + '\n';
      body += '  Pace: ' + (c.pacePercent * 100).toFixed(1) + '%\n';
      body += '  Projected month-end: €' + c.projectedMonthEnd.toFixed(2) +
              ' (Budget: €' + c.monthlyBudget.toFixed(2) + ')\n\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```



See [detailed-reference.md](references/detailed-reference.md) for details.





See [detailed-reference.md](references/detailed-reference.md) for details.



## Script 5: Low Performer Pauser

```javascript
/**
 * SCRIPT 5: Low Performer Pauser
 *
 * Automatically pauses ads and keywords that perform
 * poorly according to defined criteria.
 *
 * WARNING: This script makes changes!
 * Test first with DRY_RUN = true
 *
 * SMART BIDDING NOTE (2026):
 * Pausing keywords in Smart Bidding campaigns reduces
 * the data pool for bid optimization. Prefer raising
 * tCPA/lowering tROAS targets instead of pausing.
 * Use this script primarily for Manual CPC campaigns
 * or keywords with zero impressions for 30+ days.
 *
 * AI MAX NOTE (2026):
 * Keywords in AI Max Search campaigns use automated
 * query matching — pausing keywords may have limited
 * effect. Monitor search term insights instead.
 *
 * Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Set to false to actually pause items
  DRY_RUN: true,

  // Keyword thresholds
  KEYWORD_MIN_IMPRESSIONS: 500,
  KEYWORD_MIN_CLICKS: 10,
  KEYWORD_MAX_CPA: 100,          // Pause if CPA > €100
  KEYWORD_MIN_ROAS: 1.0,         // Pause if ROAS < 1.0x

  // Ad thresholds
  AD_MIN_IMPRESSIONS: 1000,
  AD_MIN_CTR: 0.01,              // Pause if CTR < 1%

  // Lookback period
  DATE_RANGE: 'LAST_30_DAYS'
};

function main() {
  var pausedKeywords = [];
  var pausedAds = [];

  // Process Keywords
  var keywords = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('Impressions > ' + CONFIG.KEYWORD_MIN_IMPRESSIONS)
    .forDateRange(CONFIG.DATE_RANGE)
    .get();

  while (keywords.hasNext()) {
    var keyword = keywords.next();
    var stats = keyword.getStatsFor(CONFIG.DATE_RANGE);

    var clicks = stats.getClicks();
    var cost = stats.getCost();
    var conversions = stats.getConversions();
    var value = stats.getConversionValue();

    if (clicks < CONFIG.KEYWORD_MIN_CLICKS) continue;

    var cpa = conversions > 0 ? cost / conversions : Infinity;
    var roas = cost > 0 ? value / cost : 0;

    var shouldPause = false;
    var reason = '';

    if (conversions === 0 && cost > CONFIG.KEYWORD_MAX_CPA) {
      shouldPause = true;
      reason = 'No conversions, €' + cost.toFixed(2) + ' spend';
    } else if (cpa > CONFIG.KEYWORD_MAX_CPA) {
      shouldPause = true;
      reason = 'CPA €' + cpa.toFixed(2) + ' > €' + CONFIG.KEYWORD_MAX_CPA;
    } else if (conversions > 0 && roas < CONFIG.KEYWORD_MIN_ROAS) {
      shouldPause = true;
      reason = 'ROAS ' + roas.toFixed(2) + 'x < ' + CONFIG.KEYWORD_MIN_ROAS + 'x';
    }

    if (shouldPause) {
      if (!CONFIG.DRY_RUN) {
        keyword.pause();
      }
      pausedKeywords.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        reason: reason,
        cost: cost,
        conversions: conversions
      });
    }
  }

  // Process Ads
  var ads = AdsApp.ads()
    .withCondition('Status = ENABLED')
    .withCondition('Impressions > ' + CONFIG.AD_MIN_IMPRESSIONS)
    .forDateRange(CONFIG.DATE_RANGE)
    .get();

  while (ads.hasNext()) {
    var ad = ads.next();
    var stats = ad.getStatsFor(CONFIG.DATE_RANGE);

    var impressions = stats.getImpressions();
    var clicks = stats.getClicks();
    var ctr = impressions > 0 ? clicks / impressions : 0;

    if (ctr < CONFIG.AD_MIN_CTR) {
      if (!CONFIG.DRY_RUN) {
        ad.pause();
      }
      pausedAds.push({
        headline: ad.getHeadlinePart1(),
        campaign: ad.getCampaign().getName(),
        adGroup: ad.getAdGroup().getName(),
        ctr: ctr,
        impressions: impressions
      });
    }
  }

  // Send report
  if (pausedKeywords.length > 0 || pausedAds.length > 0) {
    sendPauseReport(pausedKeywords, pausedAds);
  }

  Logger.log('Low performer check complete.');
  Logger.log('Keywords paused: ' + pausedKeywords.length);
  Logger.log('Ads paused: ' + pausedAds.length);
  Logger.log('DRY RUN: ' + CONFIG.DRY_RUN);
}

function sendPauseReport(keywords, ads) {
  var dryRunNote = CONFIG.DRY_RUN ? '[DRY RUN - No changes made]\n\n' : '';

  var subject = (CONFIG.DRY_RUN ? '[DRY RUN] ' : '') +
                'Low Performer Pause Report - ' + AdsApp.currentAccount().getName();

  var body = 'Low Performer Pause Report\n';
  body += '==========================\n\n';
  body += dryRunNote;
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Date Range: ' + CONFIG.DATE_RANGE + '\n\n';

  if (keywords.length > 0) {
    body += 'KEYWORDS PAUSED: ' + keywords.length + '\n';
    body += '─────────────────────────\n';
    for (var i = 0; i < keywords.length; i++) {
      var kw = keywords[i];
      body += '  "' + kw.keyword + '"\n';
      body += '  Campaign: ' + kw.campaign + '\n';
      body += '  Reason: ' + kw.reason + '\n\n';
    }
  }

  if (ads.length > 0) {
    body += 'ADS PAUSED: ' + ads.length + '\n';
    body += '────────────────────\n';
    for (var j = 0; j < ads.length; j++) {
      var ad = ads[j];
      body += '  "' + ad.headline + '"\n';
      body += '  Ad Group: ' + ad.adGroup + '\n';
      body += '  CTR: ' + (ad.ctr * 100).toFixed(2) + '%\n\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```



See [detailed-reference.md](references/detailed-reference.md) for details.



## Additional Scripts Quick Reference

```
ADDITIONAL SCRIPTS (Brief descriptions)
════════════════════════════════════════

SCRIPTS 7-10: Additional Optimization Scripts
──────────────────────────────────────────────

7. SEARCH QUERY MINING
   - Retrieves search terms with conversions
   - Suggests new keywords
   - Output to spreadsheet

8. NEGATIVE KEYWORD BUILDER
   - Automatic negative suggestions
   - Based on non-converting terms
   - Bulk upload ready output

9. AUTOMATED BID ADJUSTMENTS
   - Device bid modifiers
   - Location bid modifiers
   - Audience bid modifiers

10. AD ROTATION OPTIMIZER
    - Identifies winner ads
    - Suggests ad tests
    - Pauses underperformers

SCRIPTS 11-15: Reporting Scripts
────────────────────────────────

11. DAILY REPORT GENERATOR
    - Automatic daily reporting
    - Key metrics summary
    - Week-over-week comparison

12. COMPETITOR AUCTION INSIGHTS
    - Weekly competitor monitoring
    - Impression share trends
    - Position tracking

13. CAMPAIGN PERFORMANCE TRACKER
    - Historical data logging
    - Trend analysis
    - Goal tracking

14. AD EXTENSION MONITOR
    - Extension eligibility check
    - Performance per extension type
    - Missing extensions alert

15. ACCOUNT HEALTH DASHBOARD
    - Comprehensive health score
    - Weighted metrics
    - Monthly trend report
```

## Scripts Implementation Checklist

```markdown
# Scripts Implementation Checklist

## Pre-Implementation
- [ ] Backup current account settings
- [ ] Determine email recipients
- [ ] Create shared spreadsheets (if needed)
- [ ] Define threshold values for your account

## Script-by-Script Setup

### 1. Performance Anomaly Detector
- [ ] Set EMAIL address
- [ ] Adjust thresholds for your CPA/ROAS
- [ ] Schedule: Daily at 9:00
- [ ] Test: Preview mode first

### 2. Budget Pacing Monitor
- [ ] Set EMAIL address
- [ ] Adjust pacing thresholds
- [ ] Schedule: Daily at 10:00
- [ ] Verify budget values

### 3. Broken URL Checker
- [ ] Set EMAIL address
- [ ] Schedule: Weekly on Monday
- [ ] First run: Expect many results

### 4. N-Gram Analysis
- [ ] Set EMAIL address
- [ ] Optional: Create output spreadsheet
- [ ] Schedule: Weekly
- [ ] Review results before acting

### 5. Low Performer Pauser
- [ ] Set EMAIL address
- [ ] Start with DRY_RUN = true
- [ ] Adjust CPA/ROAS thresholds
- [ ] Schedule: Weekly
- [ ] Review dry run before enabling

### 6. Bid Adjustments
- [ ] Set EMAIL address
- [ ] Start with APPLY_ADJUSTMENTS = false
- [ ] Review suggestions first
- [ ] Schedule: Weekly

## Post-Implementation
- [ ] Monitor email alerts for 1 week
- [ ] Adjust thresholds based on results
- [ ] Document custom configurations
- [ ] Create maintenance schedule
```
