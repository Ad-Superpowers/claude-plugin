---
name: google-ads-performance-max-optimizer
description: "This skill should be used when the user asks to \"set up Performance Max\", \"optimize PMax campaigns\", \"configure audience signals\", \"choose search themes\", or mentions \"PMax asset group strategy\", \"channel performance breakdown\", or \"e-commerce vs lead gen PMax\". Do NOT use for: PMax audit scoring (use pmax-audit-checklist), PMax retail-specific optimization (use pmax-retail-optimizer), PMax vs Search cannibalization (use pmax-search-cannibalization-detector)."
---
# Performance Max Optimizer

Complete guide for setting up, optimizing and scaling Google Ads Performance Max campaigns for e-commerce and lead generation.



See [decision-trees.md](references/decision-trees.md) for details.





See [detailed-reference.md](references/detailed-reference.md) for details.





See [detailed-reference.md](references/detailed-reference.md) for details.



## Audience Signals

### Important Nuance: Signals != Targeting

```
CRUCIAL CONCEPT
===================

Audience Signals = HINTS for Google AI
Audience Signals != Targeting restrictions

Google WILL advertise outside your signals if it
expects better results. Signals accelerate
the learning phase and provide direction.

Good Signals -> Faster optimization
Bad Signals -> Slower learning, but not a disaster
```

### Audience Signal Strategy

```
AUDIENCE SIGNAL LAYERING
========================

LAYER 1: First-Party Data (Highest value)
------------------------------------------
[ ] Customer Match
+-- All Customers (conversions)
+-- High-Value Customers (top 20% LTV)
+-- Recent Buyers (30 days)
+-- Lapsed Customers (180+ days)

[ ] Website Visitors
+-- All visitors (180 days)
+-- Product viewers (90 days)
+-- Cart abandoners (30 days)
+-- Converters (exclude or include)

LAYER 2: Google Audiences
--------------------------
[ ] In-Market Segments
+-- Select 3-5 most relevant
+-- Based on: Real purchase intent
+-- Example: "Apparel & Accessories Shoppers"

[ ] Affinity Segments
+-- Broader, more volume
+-- Example: "Fashionistas", "Bargain Hunters"
+-- Less specific, more reach

[ ] Life Events
+-- Very powerful for specific moments
+-- Example: "Recently Moved", "Getting Married"
+-- Smaller audiences, high intent

LAYER 3: Custom Segments
-------------------------
[ ] Search Term Based
+-- People who searched specific terms
+-- Competitor names
+-- Product-specific queries

[ ] Website Based
+-- Visitors of competitor sites
+-- Review sites
+-- Industry publications
```

## Search Themes (2024+ Feature)

### What Are Search Themes?

```
SEARCH THEMES EXPLAINED
========================

Search Themes = Keywords you give PMax
to help it understand which search queries are relevant.

DIFFERENCE FROM SEARCH CAMPAIGNS:
+-- Search Campaign Keywords: Exact match/phrase targeting
+-- PMax Search Themes: Hints for AI, no guarantee

WHEN TO USE:
+-- New PMax campaigns (accelerates learning)
+-- Specific product niches
+-- When you also run Search (alignment)
+-- Protecting branded terms
```

### Search Themes Best Practices

```
SEARCH THEMES SETUP
===================

RECOMMENDATIONS PER ASSET GROUP:
+-- Count: 3-7 themes per asset group
+-- Type: Mix of broad and specific
+-- Negative keywords: Campaign-level negatives ARE supported (v20+ feature)
+--   Apply via google_ads_mutate with a campaign_criterion operation
+--   marked as negative. Account-level negative lists apply to PMax too.

EXAMPLE (Fashion E-commerce):
Asset Group: Winter Jackets
+-- Theme 1: "winter jacket women"
+-- Theme 2: "warm jacket buy"
+-- Theme 3: "[brand] winter jackets"
+-- Theme 4: "parka women"
+-- Theme 5: "winter jacket sale"

EXAMPLE (B2B Software):
Asset Group: CRM Software
+-- Theme 1: "crm software"
+-- Theme 2: "customer management system"
+-- Theme 3: "sales pipeline tool"
+-- Theme 4: "[brand] crm"

TIPS:
+-- Use keyword research data
+-- Include branded terms
+-- Check Search Terms report for ideas
+-- Update monthly based on performance
```



See [detailed-reference.md](references/detailed-reference.md) for details.



## Channel Performance Analysis

### Insights Reporting (2025+)

```
PMAX CHANNEL BREAKDOWN
======================

Location: Campaign -> Insights -> Asset Performance

AVAILABLE METRICS PER CHANNEL:
+-- Search (incl. Shopping)
+-- YouTube
+-- Display
+-- Discover
+-- Gmail
+-- Maps (if local is active)

WHAT TO ANALYZE:
+-- Which channel delivers the most conversions?
+-- ROAS per channel (if visible)
+-- Video views and engagement (YouTube)
+-- Impression share (Search/Shopping)
+-- Top converting asset combinations
```

### Asset Performance Optimization

```
ASSET PERFORMANCE (AD STRENGTH — PMax primary signal since v22)
================================================================

⚠️ Performance labels (Best/Good/Low/Pending) were REMOVED for PMax
   campaigns in API v22. Use Ad Strength as the primary asset quality
   signal for PMax.

AD STRENGTH RATINGS:
+-- Excellent: Best setup, keep structure
+-- Good: Solid, consider adding variety
+-- Average: Add more diverse assets
+-- Poor: Immediate overhaul needed

Monitor via:
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    asset_group.name,
    asset_group.ad_strength,
    asset_group.status,
    metrics.impressions,
    metrics.clicks,
    metrics.cost_micros,
    metrics.conversions,
    metrics.conversions_value
  FROM asset_group
  WHERE segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
")

OPTIMIZATION WORKFLOW:
-----------------------
Week 1-2: Learning phase, no changes
Week 3-4: Check asset ratings
+-- Remove: Assets with "Low" rating >30 days
+-- Add: New variations of "Best" assets
+-- Test: New concepts

Monthly:
+-- Refresh 20% of assets
+-- Test new headlines
+-- Seasonal updates
+-- Analyze performance trends
```



See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.



## Google Ads Script: PMax Performance Monitor

```javascript
/**
 * Performance Max Campaign Monitor
 *
 * This script monitors PMax campaigns and sends alerts
 * on significant performance changes.
 *
 * Setup:
 * 1. Adjust SETTINGS to your preferences
 * 2. Schedule: Daily at 9:00
 */

// === SETTINGS ===
var SETTINGS = {
  // Email for alerts
  EMAIL: 'you@example.com',

  // Performance thresholds
  CPA_INCREASE_THRESHOLD: 0.25,    // Alert on 25% CPA increase
  ROAS_DECREASE_THRESHOLD: 0.20,   // Alert on 20% ROAS decrease
  SPEND_CHANGE_THRESHOLD: 0.30,    // Alert on 30% spend change

  // Comparison period
  COMPARE_DAYS: 7,  // Compare last 7 days with previous 7 days

  // Minimum spend for analysis
  MIN_SPEND: 100
};

function main() {
  var pMaxCampaigns = AdsApp.performanceMaxCampaigns()
    .withCondition('Status = ENABLED')
    .get();

  var alerts = [];

  while (pMaxCampaigns.hasNext()) {
    var campaign = pMaxCampaigns.next();
    var campaignAlerts = analyzeCampaign(campaign);
    alerts = alerts.concat(campaignAlerts);
  }

  if (alerts.length > 0) {
    sendAlertEmail(alerts);
  }

  Logger.log('PMax Monitor completed. Alerts: ' + alerts.length);
}

function analyzeCampaign(campaign) {
  var alerts = [];
  var campaignName = campaign.getName();

  // Current period
  var currentStats = campaign.getStatsFor('LAST_' + SETTINGS.COMPARE_DAYS + '_DAYS');

  // Previous period (calculate manually)
  var today = new Date();
  var previousEnd = new Date(today.getTime() - (SETTINGS.COMPARE_DAYS * 24 * 60 * 60 * 1000));
  var previousStart = new Date(previousEnd.getTime() - (SETTINGS.COMPARE_DAYS * 24 * 60 * 60 * 1000));

  var previousStats = campaign.getStatsFor(
    formatDate(previousStart),
    formatDate(previousEnd)
  );

  // Check minimum spend
  if (currentStats.getCost() < SETTINGS.MIN_SPEND) {
    return alerts;
  }

  // CPA Analysis
  var currentCPA = calculateCPA(currentStats);
  var previousCPA = calculateCPA(previousStats);

  if (previousCPA > 0 && currentCPA > 0) {
    var cpaChange = (currentCPA - previousCPA) / previousCPA;
    if (cpaChange > SETTINGS.CPA_INCREASE_THRESHOLD) {
      alerts.push({
        campaign: campaignName,
        metric: 'CPA',
        current: currentCPA.toFixed(2),
        previous: previousCPA.toFixed(2),
        change: (cpaChange * 100).toFixed(1) + '%',
        severity: cpaChange > 0.5 ? 'HIGH' : 'MEDIUM'
      });
    }
  }

  // ROAS Analysis
  var currentROAS = calculateROAS(currentStats);
  var previousROAS = calculateROAS(previousStats);

  if (previousROAS > 0 && currentROAS > 0) {
    var roasChange = (currentROAS - previousROAS) / previousROAS;
    if (roasChange < -SETTINGS.ROAS_DECREASE_THRESHOLD) {
      alerts.push({
        campaign: campaignName,
        metric: 'ROAS',
        current: currentROAS.toFixed(2),
        previous: previousROAS.toFixed(2),
        change: (roasChange * 100).toFixed(1) + '%',
        severity: roasChange < -0.4 ? 'HIGH' : 'MEDIUM'
      });
    }
  }

  // Spend Analysis
  var currentSpend = currentStats.getCost();
  var previousSpend = previousStats.getCost();

  if (previousSpend > 0) {
    var spendChange = (currentSpend - previousSpend) / previousSpend;
    if (Math.abs(spendChange) > SETTINGS.SPEND_CHANGE_THRESHOLD) {
      alerts.push({
        campaign: campaignName,
        metric: 'Spend',
        current: '$' + currentSpend.toFixed(2),
        previous: '$' + previousSpend.toFixed(2),
        change: (spendChange * 100).toFixed(1) + '%',
        severity: 'LOW'
      });
    }
  }

  return alerts;
}

function calculateCPA(stats) {
  var conversions = stats.getConversions();
  var cost = stats.getCost();
  return conversions > 0 ? cost / conversions : 0;
}

function calculateROAS(stats) {
  var conversionValue = stats.getConversionValue();
  var cost = stats.getCost();
  return cost > 0 ? conversionValue / cost : 0;
}

function formatDate(date) {
  return Utilities.formatDate(date, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');
}

function sendAlertEmail(alerts) {
  var subject = 'PMax Performance Alert - ' + AdsApp.currentAccount().getName();

  var body = 'Performance Max Campaign Alerts\n';
  body += '================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Date: ' + new Date().toDateString() + '\n\n';

  for (var i = 0; i < alerts.length; i++) {
    var alert = alerts[i];
    body += '[' + alert.severity + '] ' + alert.campaign + '\n';
    body += '  ' + alert.metric + ': ' + alert.previous + ' -> ' + alert.current;
    body += ' (' + alert.change + ')\n\n';
  }

  body += '\n---\nGenerated by PMax Performance Monitor Script';

  MailApp.sendEmail(SETTINGS.EMAIL, subject, body);
}
```

## PMax 2025-2026 Feature Updates

```
PMAX RECENT UPDATES (IMPORTANT FOR OPTIMIZATION)
==================================================

v20 (2024): Campaign-level negative keywords
+-- PMax now supports negative keywords at campaign level
+-- Apply via google_ads_mutate using a campaign_criterion operation
+--   with the negative flag set to true (pass as part of operations list)
+-- Account-level shared negative keyword lists also apply

v21 (2025): Search term reporting + Smart Bidding Exploration
+-- Use campaign_search_term_view (NOT search_term_view) for PMax queries
+-- Smart Bidding Exploration: target_roas_tolerance_percent_millis
+-- Brand guidelines default ON for new PMax campaigns

v22 (2025): ad_network_type + Asset performance labels removed
+-- Channel breakdown via segments.ad_network_type
+-- asset_group_asset.performance_label REMOVED for PMax
+-- url_expansion_opt_out REMOVED → use AssetAutomationType
+-- Ad Strength is now primary asset quality signal

v23 / Mar 2026: Budget forecasting, High Value Mode, demographic reporting
+-- High Value Mode for new customer acquisition (premium bidding)
+-- First-party audience exclusions available
+-- Demographic reporting in Insights

HOW TO CHECK PMAX SEARCH TERMS (v21+):
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    campaign_search_term_view.search_term,
    metrics.impressions,
    metrics.clicks,
    metrics.cost_micros,
    metrics.conversions
  FROM campaign_search_term_view
  WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
    AND segments.date DURING LAST_30_DAYS
    AND metrics.cost_micros > 0
  ORDER BY metrics.cost_micros DESC
  LIMIT 200
")
```

## PMax vs Search: Coexistence Strategy

```
PMAX + SEARCH COEXISTENCE
==========================

GOOGLE'S PRIORITIZATION:
+-- Exact match Search keyword -> Search wins
+-- Phrase/Broad match -> Can be either
+-- No keyword match -> PMax wins
+-- Shopping queries -> PMax Shopping wins

RECOMMENDED SETUP:
-------------------
1. Search Campaign: Brand + Top non-brand exact match
2. PMax: Everything else (let AI optimize)
3. Monitor: Search Terms report in both

BRAND PROTECTION:
+-- Option 1: Brand keywords in Search (exact)
+-- Option 2: Brand exclusions in PMax
+-- Option 3: Both (maximum control)
+-- Check: Search Themes for brand alignment

MEASURING INCREMENTALITY:
+-- Run: 2 weeks with both on
+-- Pause: PMax for 2 weeks
+-- Compare: Total conversions + CPA
+-- Decide: Based on incremental lift
```

## Output: PMax Setup Checklist

```markdown
# Performance Max Setup Checklist

## Pre-Launch
[ ] Conversion tracking verified (test conversions)
[ ] Merchant Center feed approved (e-commerce)
[ ] Enhanced Conversions enabled
[ ] Minimum budget allocated ($50+/day)

## Campaign Setup
[ ] Campaign type: Performance Max
[ ] Goal: Sales / Leads (correctly selected)
[ ] Bid strategy: [Maximize Conversions / tROAS / tCPA]
[ ] Target: [X] (if applicable)
[ ] Budget: $[X]/day

## Asset Groups
[ ] Asset Group 1: [Name]
  [ ] Final URL: [URL]
  [ ] Headlines: 5-15 items
  [ ] Long headlines: 1-5 items
  [ ] Descriptions: 4-5 items
  [ ] Images: Landscape + Square + Portrait
  [ ] Logo: Square + Landscape
  [ ] Video: Optional but recommended
  [ ] Audience Signals: Configured
  [ ] Search Themes: 3-7 items

## Listing Groups (E-commerce)
[ ] Product selection correct
[ ] Custom labels used for segmentation
[ ] Exclusions set (out of stock, low margin)

## Final Checks
[ ] Final URL expansion: configured via AssetAutomationType.FINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION
    (Note: url_expansion_opt_out field was removed in v22 — use AssetAutomationType instead)
[ ] Brand exclusions: [Yes/No, which]
[ ] URL exclusions configured
[ ] Schedule: 24/7 or custom

## Post-Launch Monitoring
[ ] Day 1: Verify delivery
[ ] Day 3: Check asset eligibility
[ ] Week 1: Monitor learning phase
[ ] Week 2: First asset performance check
[ ] Week 4: Full optimization review
```
