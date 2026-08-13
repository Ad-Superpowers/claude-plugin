# Remarketing List Builder — Detailed Reference

## Dynamic Remarketing Setup

```
DYNAMIC REMARKETING (E-commerce / Lead Gen)
════════════════════════════════════════════

WHAT IS DYNAMIC REMARKETING?
────────────────────────────
= Automatically show the right products/services
= Based on what the user viewed
= Personalized ads at scale

REQUIREMENTS:
─────────────
□ Google Merchant Center (e-commerce) OR
□ Business data feed (services)
□ Dynamic remarketing tag with parameters
□ Responsive display ads

SETUP FOR E-COMMERCE:
─────────────────────

1. MERCHANT CENTER FEED
───────────────────────
Ensure Merchant Center is active with:
├── Product feed up-to-date
├── All products approved
└── Linked to Google Ads

2. DYNAMIC REMARKETING TAG
──────────────────────────
Add product parameters to pages:

<script>
gtag('event', 'view_item', {
  'send_to': 'AW-CONVERSION_ID',
  'value': 29.99,
  'items': [{
    'id': 'SKU12345',
    'google_business_vertical': 'retail'
  }]
});
</script>

Events:
├── view_item: Product page view
├── add_to_cart: Added to cart
├── view_cart: Viewed cart
└── purchase: Completed purchase

3. DYNAMIC DISPLAY CAMPAIGN
────────────────────────────
1. New Campaign → Sales → Display
2. Campaign subtype: Display (standard)
3. Audiences: Website visitors (targeting)
4. Ads: Responsive display ads
5. Enable: "Add a data feed for personalized ads"

SETUP FOR SERVICES (Lead Gen):
──────────────────────────────

1. BUSINESS DATA FEED
─────────────────────
Create CSV with services:

ID,Item title,Final URL,Image URL,Item description,Price
service-1,"Website Development","https://site.com/websites","https://...",Description,from $999
service-2,"SEO Optimization","https://site.com/seo","https://...",Description,from $499

2. UPLOAD FEED
──────────────
1. Tools → Business data → +Data feed
2. Template: Custom
3. Upload CSV
4. Map fields

3. DYNAMIC TAG FOR SERVICES
────────────────────────────
<script>
gtag('event', 'page_view', {
  'send_to': 'AW-CONVERSION_ID',
  'dynx_itemid': 'service-1',
  'dynx_pagetype': 'offerdetail'
});
</script>

Page types:
├── home: Homepage
├── searchresults: Service overview
├── offerdetail: Specific service page
├── conversionintent: Contact/pricing page
└── conversion: Thank you page
```

## Cross-Device Remarketing

```
CROSS-DEVICE REMARKETING
═════════════════════════

HOW DOES CROSS-DEVICE WORK?
────────────────────────────
User visits site on mobile → later retargeted on desktop
Possible through:
├── Google signed-in users
├── GA4 User-ID tracking
└── Device graph estimation

MAXIMIZE CROSS-DEVICE TRACKING:
───────────────────────────────

1. GOOGLE SIGNALS (GA4)
───────────────────────
Setup:
1. GA4 → Admin → Data Settings → Data Collection
2. Enable "Google signals data collection"
3. Acknowledgment: Accept

Result:
├── Cross-device user journeys
├── Better remarketing matching
└── Demographics/interests data

2. USER-ID TRACKING (If user logs in)
──────────────────────────────────────
For sites with login:

<script>
gtag('config', 'G-XXXXXXX', {
  'user_id': 'USER_ID_HASH'
});
</script>

WARNING: Use hashed user ID, not plain text

3. SAME ACCOUNT LINKING
────────────────────────
Ensure all properties are linked:
├── GA4 ↔ Google Ads
├── YouTube ↔ Google Ads
├── Firebase ↔ Google Ads (apps)
└── All accounts in same organization

CROSS-DEVICE AUDIENCE STRATEGY:
───────────────────────────────

Multi-device user journey:
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  MOBILE (Discovery)          DESKTOP (Conversion)              │
│  ─────────────────          ─────────────────────              │
│                                                                │
│  1. User sees ad on mobile   4. Retarget on desktop            │
│  2. Visits site, browses     5. Recognition by Google          │
│  3. Leaves (no conversion)   6. Conversion!                    │
│                                                                │
│  ↓                                                             │
│  Remarketing list captures visit (cross-device enabled)        │
│                                                                │
└────────────────────────────────────────────────────────────────┘

DEVICE BID ADJUSTMENTS:
───────────────────────
Combine device bids with RLSA:

Remarketing visitors (RLSA):
├── Mobile: +20% (assist device)
├── Desktop: +30% (conversion device)
└── Tablet: +10%

Adjust based on data:
1. Segment by device in reports
2. Check conversion rate per device for RLSA
3. Adjust bids accordingly
```

## Google Ads Script: Remarketing List Health Check

```javascript
/**
 * Remarketing List Health Monitor
 *
 * Monitors:
 * - List sizes and growth
 * - List expirations
 * - Coverage vs campaigns
 *
 * Setup:
 * 1. Update CONFIG
 * 2. Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',
  MIN_LIST_SIZE_SEARCH: 1000,
  MIN_LIST_SIZE_DISPLAY: 100,
  GROWTH_WARNING_THRESHOLD: -0.10,
  CRITICAL_LISTS: [
    'All Visitors',
    'Converters',
    'High Intent'
  ]
};

function main() {
  var report = {
    lists: [],
    warnings: [],
    recommendations: []
  };

  var audienceIterator = AdsApp.userlists().get();
  while (audienceIterator.hasNext()) {
    var audience = audienceIterator.next();
    var listData = {
      name: audience.getName(),
      type: audience.getType(),
      searchSize: formatSize(audience.getSizeForSearch()),
      displaySize: formatSize(audience.getSizeForDisplay()),
      status: getListStatus(audience.getSizeForSearch(), audience.getSizeForDisplay()),
      membershipLifespan: audience.getMembershipLifespan()
    };
    report.lists.push(listData);
    checkListHealth(listData, report);
  }
  checkCampaignCoverage(report);
  sendReport(report);
}

function formatSize(size) {
  if (size === 0) return '0';
  if (size < 1000) return size.toString();
  if (size < 1000000) return Math.round(size / 1000) + 'k';
  return (size / 1000000).toFixed(1) + 'M';
}

function getListStatus(searchSize, displaySize) {
  if (searchSize >= CONFIG.MIN_LIST_SIZE_SEARCH) return 'OK';
  if (displaySize >= CONFIG.MIN_LIST_SIZE_DISPLAY) return 'Display Only';
  return 'Too Small';
}

function checkListHealth(listData, report) {
  for (var i = 0; i < CONFIG.CRITICAL_LISTS.length; i++) {
    if (listData.name.indexOf(CONFIG.CRITICAL_LISTS[i]) !== -1) {
      if (listData.status === 'Too Small') {
        report.warnings.push({
          type: 'CRITICAL_LIST_SMALL',
          list: listData.name,
          message: 'Critical list "' + listData.name + '" is too small for targeting'
        });
      }
    }
  }
  if (listData.membershipLifespan && listData.membershipLifespan < 7) {
    report.recommendations.push({
      type: 'SHORT_MEMBERSHIP',
      list: listData.name,
      message: 'List "' + listData.name + '" has very short membership (' +
               listData.membershipLifespan + ' days). Consider extending.'
    });
  }
}

function checkCampaignCoverage(report) {
  var campaignsWithRemarketing = 0;
  var campaignsWithoutRemarketing = 0;
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignType = SEARCH')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var audiences = campaign.targeting().audiences().get();
    if (audiences.hasNext()) {
      campaignsWithRemarketing++;
    } else {
      campaignsWithoutRemarketing++;
    }
  }

  if (campaignsWithoutRemarketing > 0) {
    report.recommendations.push({
      type: 'MISSING_RLSA',
      message: campaignsWithoutRemarketing + ' Search campaigns have no RLSA audiences.'
    });
  }
  report.summary = {
    campaignsWithRLSA: campaignsWithRemarketing,
    campaignsWithoutRLSA: campaignsWithoutRemarketing
  };
}

function sendReport(report) {
  var subject = 'Remarketing Health Report - ' + AdsApp.currentAccount().getName();
  var body = 'Remarketing Lists Health Check\n';
  body += '===============================\n\n';
  body += 'SUMMARY:\n';
  body += 'Total lists: ' + report.lists.length + '\n';
  body += 'Campaigns with RLSA: ' + report.summary.campaignsWithRLSA + '\n';
  body += 'Campaigns without RLSA: ' + report.summary.campaignsWithoutRLSA + '\n\n';

  if (report.warnings.length > 0) {
    body += 'WARNINGS:\n';
    for (var i = 0; i < report.warnings.length; i++) {
      body += '- ' + report.warnings[i].message + '\n';
    }
    body += '\n';
  }

  body += 'LIST STATUS:\n';
  for (var j = 0; j < Math.min(report.lists.length, 15); j++) {
    var list = report.lists[j];
    var status = list.status === 'OK' ? '[OK]' :
                 list.status === 'Display Only' ? '[Display]' : '[Small]';
    body += status + ' ' + list.name + '\n';
    body += '  Search: ' + list.searchSize + ' | Display: ' + list.displaySize + '\n';
  }

  if (report.recommendations.length > 0) {
    body += '\nRECOMMENDATIONS:\n';
    for (var k = 0; k < report.recommendations.length; k++) {
      body += '- ' + report.recommendations[k].message + '\n';
    }
  }

  body += '\n---\nGenerated by Remarketing Health Monitor';
  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```
