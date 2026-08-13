---
name: google-ads-conversion-tracking-debugger
description: "This skill should be used when the user asks to \"debug conversion tracking\", \"fix missing conversions\", \"resolve duplicate conversions\", \"troubleshoot tag not firing\", or mentions \"GCLID issues\", \"conversion discrepancy\", or \"Enhanced Conversions not working\". Do NOT use for: initial conversion tracking setup (use conversion-tracking-setup), Meta conversion issues (use meta tools), GA4 event debugging (use ga4 tools)."
---
# Conversion Tracking Debugger

Systematic troubleshooting guide for Google Ads conversion tracking issues. Use the diagnostic flow below to quickly identify root causes, then follow the detailed decision trees in the references.

## Quick Diagnosis Flow

```
WHAT IS THE PROBLEM?
│
├─► [A] Conversions NOT appearing
│   ├── Timing check: Wait 24-48 hours before debugging
│   ├── Check: Google Ads → Goals → Conversions → Status column
│   │   ├── "Inactive" → Tag not found on site
│   │   ├── "Unverified" → Setup incomplete
│   │   └── "No recent conversions" → Tag found but not firing
│   ├── Verify tag: Chrome DevTools → Network → filter "googleads"
│   └── Detailed steps: See references/decision-trees.md Section 1
│
├─► [B] Too MANY conversions (duplicates)
│   ├── Add unique transaction_id to conversion tag
│   ├── Set Count: "One" for leads, "Every" for purchases
│   ├── Check for duplicate tags (GTM + hardcoded)
│   └── Detailed steps: See references/decision-trees.md Section 2
│
├─► [C] Numbers DON'T MATCH (GA4 vs Ads)
│   ├── 10-30% difference = NORMAL (different attribution models)
│   ├── Align attribution windows for comparison
│   ├── Compare "All Conversions" column in Google Ads
│   └── Detailed steps: See references/decision-trees.md Section 3
│
├─► [D] Enhanced Conversions not working
│   ├── Check user_data object in dataLayer
│   ├── Verify consent: ad_user_data = "granted"
│   ├── Validate SHA-256 hash format (if pre-hashed)
│   ├── Wait 48-72 hours for status update
│   └── Detailed steps: See references/decision-trees.md Section 4
│
├─► [E] Offline conversion import failing
│   ├── Validate GCLID format and age (< 90 days)
│   ├── Check timestamp timezone (must match account)
│   ├── Verify conversion action name matches exactly
│   ├── Handle partial failures via error report
│   └── Detailed steps: See references/decision-trees.md Section 5
│
└─► [F] Tag/Pixel firing issues
    ├── Check JS console for errors
    ├── Verify GTM container is published
    ├── Test trigger conditions in GTM Preview
    ├── Remove duplicate implementations
    └── Detailed steps: See references/decision-trees.md Section 6
```

## MCP Tool Integration

```
STEP 1: Pull current conversion data
google_ads_run_gaql(query="
  SELECT
    conversion_action.name,
    conversion_action.status,
    conversion_action.type,
    metrics.conversions,
    metrics.all_conversions,
    metrics.conversions_by_conversion_date
  FROM conversion_action
  WHERE segments.date DURING LAST_30_DAYS
  ORDER BY metrics.conversions DESC
")

STEP 2: Compare with GA4 (if linked)
ga4_run_report(
  property_id="YOUR_PROPERTY",
  metrics=["keyEvents", "sessions"],
  dimensions=["sessionDefaultChannelGroup"],
  start_date="30daysAgo",
  end_date="today"
)

STEP 3: Check for tracking anomalies
google_ads_run_gaql(query="
  SELECT
    campaign.name,
    metrics.conversions,
    metrics.clicks,
    metrics.conversions_from_interactions_rate
  FROM campaign
  WHERE segments.date DURING LAST_7_DAYS
    AND metrics.clicks > 100
    AND metrics.conversions_from_interactions_rate < 0.001
  ORDER BY metrics.clicks DESC
")
→ Campaigns with clicks but near-zero conversions = likely tracking issue
```

## Quick Reference Card

```
CONVERSION TRACKING DEBUG CHEAT SHEET
======================================

NOT SHOWING?
→ Check tag presence (Network tab)
→ Verify conversion ID/label
→ Test consent state
→ Wait 24-48 hours

DUPLICATES?
→ Add transaction_id
→ Set Count: "One" for leads
→ Check for duplicate tags
→ Implement sessionStorage check

GA4 DISCREPANCY?
→ 10-30% difference = normal
→ Align attribution windows
→ Compare All Conversions column
→ Accept baseline, track trends

ENHANCED NOT WORKING?
→ Check user_data in dataLayer
→ Verify consent: ad_user_data
→ Validate hash format
→ Wait 48 hours for status

OFFLINE IMPORT FAILING?
→ Validate GCLID format/age
→ Check timestamp timezone
→ Verify conversion action name
→ Handle partial failures

TAG NOT FIRING?
→ Check JS console for errors
→ Verify GTM published
→ Test trigger conditions
→ Remove duplicate implementations
```

## Consent Mode v2 Impact (2024+)

```
CONSENT MODE & CONVERSIONS
───────��───────────────────
EU visitors with consent denied:
├── Basic consent mode: No conversion tags fire
├── Advanced consent mode: Cookieless pings → modeled conversions
└── Check: Google Ads → Conversions → "Modeled" column

IF modeled conversions are low:
├── Verify consent mode implementation (GTM → Consent Overview)
├── Check CMP (Consent Management Platform) is firing before tags
├── Ensure default consent state is set before page load
└── Consider: Advanced consent mode for better modeling
```

## Output: Debug Report Template

```markdown
# Conversion Tracking Debug Report

## Issue
- **Problem type:** [Missing / Duplicate / Discrepancy / Enhanced / Offline / Tag]
- **First noticed:** [Date]
- **Affected campaigns:** [List]

## Diagnosis
- **Root cause:** [Description]
- **Evidence:** [What you found]

## Fix Applied
1. [Action taken]
2. [Verification step]

## Verification
- [ ] Conversion firing in Tag Assistant
- [ ] Conversion appearing in Google Ads (wait 24-48h)
- [ ] Numbers align with GA4 (within 10-30%)
- [ ] No duplicate conversions
- [ ] Consent mode working correctly
```
