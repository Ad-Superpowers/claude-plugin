---
name: ga4-debugging-validation
description: "This skill should be used when the user asks to \"debug GA4 tracking\", \"validate tag implementation\", \"use DebugView\", or mentions \"data quality checks\", \"GA4 audit\", or \"event tracking not working\". Do NOT use for: e-commerce event setup (use ga4-ecommerce-setup), BigQuery data analysis (use ga4-bigquery-export)."
---
# GA4 Debugging & Validation Guide

Complete guide for debugging GA4 implementations and ensuring data quality.

## GA4 DebugView Setup

```
CONFIGURING DEBUGVIEW
======================

WHAT IS DEBUGVIEW:
├── Real-time event monitoring in GA4
├── Shows events within 1 minute
├── Including parameters and user properties
├── Perfect for development and QA
└── No impact on production data

LOCATION: GA4 Admin → Property → DebugView

METHOD 1: CHROME EXTENSION
───────────────────────────
1. Install "Google Analytics Debugger" extension
   └── Chrome Web Store → search "GA Debugger"

2. Activate extension (icon in toolbar)

3. Refresh page where GA4 is active

4. Open GA4 → Admin → DebugView

5. Select your device in dropdown

NOTE:
├── Extension must be ON
├── Can take 1-2 minutes for device to appear
└── Multiple devices may be visible

METHOD 2: GTM PREVIEW MODE
───────────────────────────
1. Open GTM → Preview

2. Enter website URL

3. Debug session starts automatically

4. Events are visible in:
   ├── GTM Preview panel
   └── GA4 DebugView

ADVANTAGE: See GTM tag firing + GA4 simultaneously

METHOD 3: DEBUG PARAMETER
──────────────────────────
Add parameter to URL:
https://example.com?debug_mode=true

OR in GTM tag configuration:
├── GA4 Configuration tag
├── Fields to Set
├── Field name: debug_mode
└── Value: true

OR via dataLayer:
gtag('config', 'G-XXXXXXXXXX', { 'debug_mode': true });

METHOD 4: MOBILE APP DEBUGGING
───────────────────────────────
iOS:
├── Xcode → Product → Scheme → Edit Scheme
├── Arguments Passed On Launch
└── Add: -FIRAnalyticsDebugEnabled

Android:
adb shell setprop debug.firebase.analytics.app [package_name]

Stop debugging:
adb shell setprop debug.firebase.analytics.app .none.
```

## Interpreting DebugView

```
DEBUGVIEW INTERFACE EXPLAINED
==============================

MAIN SECTIONS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Section                 │ Shows                                    │
├─────────────────────────┼──────────────────────────────────────────┤
│ Device selector         │ Debug devices (choose correct device)    │
├─────────────────────────┼──────────────────────────────────────────┤
│ Timeline (left)         │ Chronological event stream               │
├─────────────────────────┼──────────────────────────────────────────┤
│ Event details (right)   │ Parameters of selected event             │
├─────────────────────────┼──────────────────────────────────────────┤
│ Top events (above)      │ Most recent events (quick overview)      │
└─────────────────────────┴──────────────────────────────────────────┘

EVENT COLOR CODES:
──────────────────
Green     → Automatically collected events (first_visit, session_start)
Blue      → Enhanced Measurement events (scroll, click, etc.)
Purple    → Custom events (your implementation)
Yellow    → Key Events (marked as conversions)
Red       → Errors or issues

CHECKING EVENT PARAMETERS:
──────────────────────────
1. Click on event in timeline
2. View "Parameters" section on right
3. Verify:
   ├── All expected parameters present
   ├── Values correct (types: string/int/double)
   ├── No empty values where data expected
   └── Parameter names exactly right (case sensitive!)

USER PROPERTIES:
────────────────
├── Scroll down in event details
├── "User properties" section
├── Check that custom user properties are correctly set
└── Persistent across sessions

COMMON ISSUES TO SPOT:
──────────────────────
├── Event not visible → Tag not fired
├── Parameters missing → DataLayer issue
├── Wrong values → Mapping/transformation error
├── Duplicate events → Multiple tags for same event
└── Events too fast → Possible bot/automation
```

## GTM Preview Mode

```
GTM PREVIEW DEBUGGING
======================

STARTING:
─────────
1. Open GTM container
2. Click "Preview" (top right)
3. Enter website URL
4. Debug tab opens automatically

INTERFACE SECTIONS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Panel                   │ Function                                 │
├─────────────────────────┼──────────────────────────────────────────┤
│ Summary                 │ Overview of fired tags                   │
├─────────────────────────┼──────────────────────────────────────────┤
│ Tags                    │ All tags, which fired/not fired          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Variables               │ Values of all variables                  │
├─────────────────────────┼──────────────────────────────────────────┤
│ Data Layer              │ Complete dataLayer contents               │
├─────────────────────────┼──────────────────────────────────────────┤
│ Errors                  │ JavaScript errors, tag failures         │
└─────────────────────────┴──────────────────────────────────────────┘

EVENT SELECTION:
────────────────
├── Left: List of GTM events
├── Select event to see state
├── "Container Loaded" = DOM Ready
├── "Window Loaded" = Window Load
├── Custom events (add_to_cart, purchase, etc.)
└── DataLayer events

COMMON DEBUG ACTIONS:
─────────────────────
1. TAG NOT FIRED
   ├── Check Triggers: Is trigger condition correct?
   ├── Check Variables: Do they have expected values?
   ├── Check Blocking: Are there exception triggers?
   └── Check event timing: Does event arrive?

2. TAG FIRED WITH WRONG VALUES
   ├── Variables tab: Check variable values
   ├── Data Layer tab: Check source data
   └── Compare with expected values

3. DUPLICATE TAGS
   ├── Tags tab: Check "Times Fired"
   └── Review trigger configuration

GTM PREVIEW TIPS:
─────────────────
├── Share preview link with team (button top right)
├── Clear cookies if preview doesn't work
├── Check for conflicting extensions
├── Use incognito if normal window has issues
└── Break on event for complex debugging
```

## Browser DevTools Debugging

```
CHROME DEVTOOLS FOR GA4
========================

NETWORK TAB:
────────────
1. Open DevTools (F12 or Cmd+Opt+I)
2. Go to Network tab
3. Filter on: "collect" or "google-analytics"

WHAT TO LOOK FOR:
├── collect requests = events to GA4
├── Payload contains encoded event data
├── Response 204 = success
└── Response errors = tracking issues

DECODED PARAMETERS:
───────────────────
Query string parameters to decode:
├── en = event name
├── ep.* = event parameters
├── up.* = user properties
├── cid = client ID
├── tid = tracking/measurement ID
└── _ss = session start (1 = new session)

CONSOLE TAB:
────────────
// Inspect DataLayer
console.log(dataLayer);

// Enable GA4 debug logging
gtag('config', 'G-XXXXXX', { 'debug_mode': true });

// Test custom event
gtag('event', 'test_event', {
  'custom_param': 'test_value'
});

// Push DataLayer event
dataLayer.push({
  event: 'test_event',
  test_param: 'test_value'
});

ELEMENTS TAB:
─────────────
├── Verify GTM container snippet is present
├── Check for gtag.js conflicts (analytics.js / Universal Analytics fully retired July 2024)
├── Inspect data attributes on elements
└── Check consent management implementation

APPLICATION TAB:
────────────────
├── Cookies: Check _ga, _gid cookies
├── LocalStorage: Check GTM storage
├── Session Storage: Check session data
└── Verify consent preferences stored
```

## Data Quality Checks

```
GA4 DATA QUALITY CHECKLIST
============================

DAILY CHECKS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Check                   │ How to verify                            │
├─────────────────────────┼──────────────────────────────────────────┤
│ Events coming in        │ Realtime report > 0 users                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Key events tracking     │ Key Events report has data               │
├─────────────────────────┼──────────────────────────────────────────┤
│ E-commerce data         │ Monetization report has revenue          │
├─────────────────────────┼──────────────────────────────────────────┤
│ No sudden drops         │ Compare with previous day/week           │
├─────────────────────────┼──────────────────────────────────────────┤
│ No sudden spikes        │ Check for bot traffic or errors          │
└─────────────────────────┴──────────────────────────────────────────┘

WEEKLY CHECKS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Check                   │ Expected outcome                         │
├─────────────────────────┼──────────────────────────────────────────┤
│ Bounce rate             │ 20-70% (depending on site type)          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Avg. session duration   │ > 30 seconds (most sites)                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Conversion rate         │ Consistent with historical               │
├─────────────────────────┼──────────────────────────────────────────┤
│ Traffic source data     │ (not set) < 5% of traffic                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Device distribution     │ Consistent with expectations             │
└─────────────────────────┴──────────────────────────────────────────┘

DATA ANOMALY DETECTION:
───────────────────────
SIGNIFICANT DEVIATION THRESHOLDS:
├── Users: > 30% difference vs previous week
├── Sessions: > 30% difference
├── Pageviews: > 30% difference
├── Key Events: > 20% difference
├── Revenue: > 20% difference
└── Bounce rate: > 10 percentage points

AUTOMATED ALERTS SETUP:
───────────────────────
1. GA4 → Admin → Custom Insights
2. Create → Anomaly detection
3. Configure:
   ├── Metric: Users/Sessions/etc.
   ├── Evaluation period: Daily/Weekly
   ├── Anomaly condition: % change
   └── Notification: Email
```

## Event Validation Queries

```
GA4 EXPLORATION FOR VALIDATION
================================

EXPLORATION 1: EVENT COMPLETENESS
──────────────────────────────────
Technique: Free form

Setup:
├── Rows: Event name
├── Values:
│   ├── Event count
│   ├── Users
│   └── Event value (if relevant)
├── Date range: Last 7 days
└── Export and compare with expected events

CHECK:
├── All expected events present
├── No unexpected event names
├── Event counts in expected range
└── No events with 0 users (ghost events)

EXPLORATION 2: PARAMETER FILL RATE
───────────────────────────────────
Technique: Free form

Setup:
├── Rows: Event name
├── Values:
│   ├── Event count (all)
│   ├── [Custom metric for parameter count]
├── Filter: Specific event type

Note: Parameter fill rate requires BigQuery or calculated metric

EXPLORATION 3: ECOMMERCE FUNNEL VALIDATION
───────────────────────────────────────────
Technique: Funnel exploration

Setup:
├── Steps:
│   ├── view_item
│   ├── add_to_cart
│   ├── begin_checkout
│   └── purchase
└── Validate drop-off rates are realistic

RED FLAGS:
├── 100% completion rate → possible duplicate events
├── 0% completion rate → broken tracking
├── Completion > 100% → sequence issues
└── Large gaps → missing events

EXPLORATION 4: SOURCE/MEDIUM QUALITY
─────────────────────────────────────
Technique: Free form

Setup:
├── Rows: Session source/medium
├── Values: Sessions
├── Sort: Descending

CHECK:
├── "(not set)" percentage (target: < 5%)
├── "(direct) / (none)" not too high
├── Expected sources present
└── No bizarre/spam sources
```

## Implementation Audit Checklist

```
GA4 IMPLEMENTATION AUDIT
=========================

[ ] BASE SETUP
├── [ ] Measurement ID correct (G-XXXXXXXXXX)
├── [ ] Property timezone correct
├── [ ] Property currency correct
├── [ ] Data retention set to 14 months
├── [ ] Google Signals configured
└── [ ] BigQuery export (if needed)

[ ] DATA STREAMS
├── [ ] Web stream active
├── [ ] Enhanced Measurement configured
├── [ ] Site search parameter correct
├── [ ] Cross-domain tracking (if needed)
└── [ ] Referral exclusion list correct

[ ] EVENT TRACKING
├── [ ] page_view fires on all pages
├── [ ] Automatic events working
├── [ ] Custom events correctly implemented
├── [ ] Event parameters present
├── [ ] Event naming consistent
└── [ ] No duplicate events

[ ] E-COMMERCE (if applicable)
├── [ ] view_item event working
├── [ ] add_to_cart event working
├── [ ] purchase event working
├── [ ] transaction_id is unique
├── [ ] Revenue data correct
├── [ ] Currency correct
└── [ ] Items array populated

[ ] KEY EVENTS
├── [ ] Key events marked in GA4 Admin
├── [ ] Key event counting correct
├── [ ] Attribution settings correct
└── [ ] Google Ads import (if linked)

[ ] USER TRACKING
├── [ ] user_id correctly implemented (if needed)
├── [ ] User properties correctly set
├── [ ] Consent Mode v2 implemented (required for EEA since March 2024)
│   ├── [ ] analytics_storage signal firing correctly
│   ├── [ ] ad_storage signal firing correctly
│   └── [ ] Modeled conversions visible in GA4 (confirms v2 working)
└── [ ] PII compliance (no PII in data)

[ ] GTM CONFIGURATION
├── [ ] Container correctly placed
├── [ ] Tags correctly configured
├── [ ] Triggers correct
├── [ ] Variables working
├── [ ] No JavaScript errors
└── [ ] Container published

[ ] INTEGRATIONS
├── [ ] Google Ads linked
├── [ ] Search Console linked
├── [ ] BigQuery linked (optional)
└── [ ] Third-party tools working
```

## Automated Testing Setup

```
AUTOMATED GA4 TESTING
======================

PLAYWRIGHT TEST EXAMPLE:
─────────────────────────
// playwright.config.ts
import { PlaywrightTestConfig } from '@playwright/test';

const config: PlaywrightTestConfig = {
  use: {
    baseURL: 'https://example.com',
  },
};

export default config;

// tests/ga4-tracking.spec.ts
import { test, expect } from '@playwright/test';

test('GA4 page_view fires on page load', async ({ page }) => {
  // Intercept GA4 requests
  const ga4Requests: string[] = [];

  page.on('request', request => {
    if (request.url().includes('google-analytics.com/g/collect')) {
      ga4Requests.push(request.url());
    }
  });

  await page.goto('/');
  await page.waitForTimeout(2000);

  // Verify page_view event
  expect(ga4Requests.some(url => url.includes('en=page_view'))).toBeTruthy();
});

test('GA4 add_to_cart fires correctly', async ({ page }) => {
  const ga4Requests: string[] = [];

  page.on('request', request => {
    if (request.url().includes('google-analytics.com/g/collect')) {
      ga4Requests.push(request.url());
    }
  });

  await page.goto('/product/test-product');
  await page.click('[data-testid="add-to-cart"]');
  await page.waitForTimeout(2000);

  // Verify add_to_cart event
  const addToCartRequest = ga4Requests.find(url => url.includes('en=add_to_cart'));
  expect(addToCartRequest).toBeTruthy();

  // Verify item parameters
  expect(addToCartRequest).toContain('ep.item_id');
});

test('GA4 purchase fires with correct revenue', async ({ page }) => {
  // Complete checkout flow...
  // Verify purchase event with transaction_id and value
});

CYPRESS TEST EXAMPLE:
─────────────────────
// cypress/support/commands.ts
Cypress.Commands.add('interceptGA4', () => {
  cy.intercept('POST', '**/google-analytics.com/g/collect*').as('ga4');
});

// cypress/e2e/ga4-tracking.cy.ts
describe('GA4 Tracking', () => {
  beforeEach(() => {
    cy.interceptGA4();
  });

  it('fires page_view on load', () => {
    cy.visit('/');
    cy.wait('@ga4').then((interception) => {
      expect(interception.request.url).to.include('en=page_view');
    });
  });

  it('fires add_to_cart with parameters', () => {
    cy.visit('/product/123');
    cy.get('[data-testid="add-to-cart"]').click();
    cy.wait('@ga4').then((interception) => {
      expect(interception.request.url).to.include('en=add_to_cart');
      expect(interception.request.url).to.include('ep.item_id');
    });
  });
});

CI/CD INTEGRATION:
──────────────────
# .github/workflows/ga4-tests.yml
name: GA4 Tracking Tests

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install dependencies
        run: npm ci

      - name: Install Playwright
        run: npx playwright install

      - name: Run GA4 tests
        run: npx playwright test tests/ga4-tracking.spec.ts

      - name: Upload report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report
          path: playwright-report/
```

## Output: Debugging Report Template

```markdown
# GA4 Debugging & Validation Report

## Audit Information
- **Property ID:** G-XXXXXXXXXX
- **Website:** [URL]
- **Audit date:** [Date]
- **Auditor:** [Name]

## Executive Summary

| Category | Status | Score |
|----------|--------|-------|
| Base Setup | Pass | 100% |
| Event Tracking | Issues | 85% |
| E-commerce | Pass | 100% |
| Data Quality | Issues | 90% |
| **Overall** | **Issues** | **94%** |

## Base Setup Verification

| Check | Status | Notes |
|-------|--------|-------|
| Measurement ID correct | ✅ | G-XXXXXXXXXX |
| Timezone | ✅ | Europe/Amsterdam |
| Currency | ✅ | EUR |
| Data retention | ✅ | 14 months |
| Google Signals | ✅ | Enabled |
| Enhanced Measurement | ✅ | All enabled |

## Event Tracking Validation

### Automatic Events

| Event | Status | Notes |
|-------|--------|-------|
| page_view | ✅ | Fires correctly |
| first_visit | ✅ | Working |
| session_start | ✅ | Working |
| scroll | ✅ | 90% threshold |
| click | ✅ | Outbound clicks |

### Custom Events

| Event | Status | Parameters Verified | Notes |
|-------|--------|---------------------|-------|
| sign_up | ✅ | method | Working |
| login | ✅ | method | Working |
| purchase | Issues | transaction_id, value | Missing coupon |
| add_to_cart | ✅ | items array | Working |

## E-commerce Validation

| Event | Status | Notes |
|-------|--------|-------|
| view_item | ✅ | All parameters present |
| add_to_cart | ✅ | Items array correct |
| begin_checkout | ✅ | Value matches cart |
| purchase | ✅ | Revenue verified vs backend |

### Revenue Reconciliation

| Source | Revenue | Variance |
|--------|---------|----------|
| GA4 | EUR 12,345 | - |
| Backend | EUR 12,401 | 0.45% |

**Status:** Within acceptable range (<1%)

## Data Quality Metrics

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| (not set) source | 3.2% | <5% | ✅ |
| Bounce rate | 45% | 20-70% | ✅ |
| Avg session | 2:34 | >30s | ✅ |
| Self-referrals | 0.1% | <1% | ✅ |

## Issues Found

### Critical (Blocking)
- None

### High Priority
1. **Missing coupon parameter in purchase event**
   - Impact: Cannot track promotion effectiveness
   - Fix: Add coupon to dataLayer purchase push

### Medium Priority
1. **Form submission double-firing**
   - Impact: Inflated form submission counts (~5%)
   - Fix: Add deduplication logic

### Low Priority
1. **Video engagement not tracking on custom player**
   - Impact: Missing video metrics
   - Fix: Implement custom video tracking

## Recommended Actions

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| High | Add coupon parameter | Low | High |
| Medium | Fix form double-fire | Medium | Medium |
| Low | Video tracking | High | Low |

## Test Results

| Test Suite | Passed | Failed | Skipped |
|------------|--------|--------|---------|
| Page tracking | 12 | 0 | 0 |
| E-commerce | 8 | 1 | 0 |
| Custom events | 15 | 2 | 1 |
| **Total** | **35** | **3** | **1** |

## Next Steps

1. [ ] Fix coupon parameter in purchase event
2. [ ] Implement form deduplication
3. [ ] Re-run validation after fixes
4. [ ] Set up automated monitoring alerts

## Appendix

### DebugView Screenshots
[Attach relevant screenshots]

### GTM Preview Logs
[Attach relevant logs]

### Network Requests Sample
[Attach sample collect requests]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, run validation checks against production data to surface discrepancies:

```python
# Cross-check event counts and session data against expected values from debugging session
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="7daysAgo",
    end_date="today",
    metrics=["sessions", "eventCount", "keyEvents"],
    dimensions=["eventName", "date"]
)
```

Compare live event counts against what you observed in DebugView/GTM Preview. Unexpected gaps between debug mode and production indicate environment differences (consent mode, sampling, or tag firing conditions).
