## Quick Decision Guide

```
WHICH ENHANCED CONVERSIONS OPTION FITS YOUR SITUATION?
│
├─► E-COMMERCE (Online Sales)
│   └─► ENHANCED CONVERSIONS FOR WEB
│       ├── Automatic via Google Tag
│       ├── Or manual via GTM
│       └── Requires: checkout form data
│
├─► LEAD GENERATION (Forms)
│   └─► ENHANCED CONVERSIONS FOR LEADS
│       ├── Capture lead data on form submit
│       ├── Later: link to offline sale
│       └── Requires: CRM integration
│
├─► OFFLINE SALES / LONG SALES CYCLE
│   └─► OFFLINE CONVERSION IMPORT
│       ├── Import sales data via API/upload
│       ├── Match with GCLID or enhanced matching
│       └── Requires: CRM with GCLID tracking
│
└─► FULL ATTRIBUTION STACK
    └─► SERVER-SIDE TAGGING
        ├── First-party data collection
        ├── More control over data
        ├── Better ad blocker bypass
        └── Requires: Server infrastructure
```

## Diagnostics & Troubleshooting

### Enhanced Conversions Diagnostics

```
DIAGNOSTICS CHECKLIST
═════════════════════

GOOGLE ADS UI CHECK:
────────────────────
1. Tools → Conversions → [Conversion]
2. Check "Diagnostics" tab
3. Status should show:
   ├── "Recording conversions": Active
   ├── "Enhanced conversions": Active
   └── "Data quality": Good/Excellent

COMMON ISSUES:
──────────────

ISSUE: "Not receiving enhanced conversion data"
CAUSES:
├── Tag not correctly configured
├── Consent not granted
├── Form fields not found (auto mode)
FIXES:
├── Verify tag setup in GTM
├── Check consent mode signals
└── Switch to manual data layer

ISSUE: "Low match rate"
CAUSES:
├── Data not correctly formatted
├── Only email, no phone/name
├── Hash mismatch
FIXES:
├── Normalize data (lowercase, trim)
├── Add more data points
└── Verify hashing (or send plain text)

ISSUE: "Enhanced conversions not recording"
CAUSES:
├── Conversion action not configured
├── Tag fires but no data
├── Consent denied for ad_user_data
FIXES:
├── Enable in conversion settings
├── Add user-provided data to tag
└── Check consent mode implementation

VERIFICATION SCRIPT:
────────────────────
// Console check for enhanced conversions data
console.log('Checking enhanced conversions data...');
if (window.google_tag_manager) {
  // Check dataLayer
  var dl = window.dataLayer || [];
  var ecData = dl.find(function(item) {
    return item.enhanced_conversion_data;
  });
  if (ecData) {
    console.log('Enhanced Conversion Data Found:', ecData.enhanced_conversion_data);
  } else {
    console.warn('No enhanced_conversion_data in dataLayer');
  }
}
```

### Enhanced Conversions Diagnostics

```
DIAGNOSTICS CHECKLIST
═════════════════════

GOOGLE ADS UI CHECK:
────────────────────
1. Tools → Conversions → [Conversion]
2. Check "Diagnostics" tab
3. Status should show:
   ├── "Recording conversions": Active
   ├── "Enhanced conversions": Active
   └── "Data quality": Good/Excellent

COMMON ISSUES:
──────────────

ISSUE: "Not receiving enhanced conversion data"
CAUSES:
├── Tag not correctly configured
├── Consent not granted
├── Form fields not found (auto mode)
FIXES:
├── Verify tag setup in GTM
├── Check consent mode signals
└── Switch to manual data layer

ISSUE: "Low match rate"
CAUSES:
├── Data not correctly formatted
├── Only email, no phone/name
├── Hash mismatch
FIXES:
├── Normalize data (lowercase, trim)
├── Add more data points
└── Verify hashing (or send plain text)

ISSUE: "Enhanced conversions not recording"
CAUSES:
├── Conversion action not configured
├── Tag fires but no data
├── Consent denied for ad_user_data
FIXES:
├── Enable in conversion settings
├── Add user-provided data to tag
└── Check consent mode implementation

VERIFICATION SCRIPT:
────────────────────
// Console check for enhanced conversions data
console.log('Checking enhanced conversions data...');
if (window.google_tag_manager) {
  // Check dataLayer
  var dl = window.dataLayer || [];
  var ecData = dl.find(function(item) {
    return item.enhanced_conversion_data;
  });
  if (ecData) {
    console.log('Enhanced Conversion Data Found:', ecData.enhanced_conversion_data);
  } else {
    console.warn('No enhanced_conversion_data in dataLayer');
  }
}
```

## Google Ads Script: Enhanced Conversions Monitor

```javascript
/**
 * Enhanced Conversions Health Monitor
 *
 * Monitors enhanced conversion status and diagnostics
 *
 * Setup:
 * 1. Update CONFIG
 * 2. Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',
  MIN_MATCH_RATE: 0.4 // 40% minimum match rate
};

function main() {
  var report = {
    conversions: [],
    issues: []
  };

  // Check conversion actions
  var conversionActions = AdsApp.conversions().get();

  while (conversionActions.hasNext()) {
    var conversion = conversionActions.next();
    var name = conversion.getName();

    // Enhanced conversions status is not directly available via API
    // This script logs conversion configuration for manual review

    report.conversions.push({
      name: name,
      category: conversion.getCategory(),
      status: conversion.isEnabled() ? 'Enabled' : 'Disabled',
      countingType: conversion.getCountingType()
    });
  }

  // Generate summary
  var enabledCount = report.conversions.filter(function(c) {
    return c.status === 'Enabled';
  }).length;

  Logger.log('Conversion Actions Report');
  Logger.log('========================');
  Logger.log('Total conversions: ' + report.conversions.length);
  Logger.log('Enabled: ' + enabledCount);

  // Log details
  for (var i = 0; i < report.conversions.length; i++) {
    var conv = report.conversions[i];
    Logger.log('');
    Logger.log('Conversion: ' + conv.name);
    Logger.log('  Category: ' + conv.category);
    Logger.log('  Status: ' + conv.status);
    Logger.log('  Counting: ' + conv.countingType);
  }

  // Recommendations
  Logger.log('');
  Logger.log('RECOMMENDATIONS:');
  Logger.log('----------------');
  Logger.log('1. Check Google Ads UI → Conversions → Diagnostics');
  Logger.log('   for enhanced conversions match rate');
  Logger.log('2. Target match rate: 40%+ for good attribution');
  Logger.log('3. Add more data points (phone, name) for better matching');
}
```