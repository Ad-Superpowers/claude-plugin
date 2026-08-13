---
name: gtm-container-auditor
description: "This skill should be used when the user asks to \"audit my GTM container\", \"find duplicate tags\", \"clean up Tag Manager\", mentions \"GTM health check\", \"unused tags and triggers\", or \"consent compliance of tags\". Do NOT use for: server-side tracking or CAPI implementation (use first-party-data-strategy), attribution discrepancies between platforms (use attribution-reconciler), or general tag implementation guidance (use platform-specific skills)."
---
# GTM Container Auditor

## Purpose

Help agencies and advertisers assess the health and quality of their Google Tag Manager
containers. Poor GTM hygiene causes duplicate conversions, inflated metrics, slow page
load (from excessive tags), and tracking gaps. A clean container typically improves data
accuracy by 15-40%.

## When to Use This Skill

Invoke when user mentions:
- **Health check:** "Audit my GTM container" / "Review my tag setup"
- **Duplicate tracking:** "My conversions look doubled" / "Are there duplicate tags?"
- **Performance:** "GTM is slowing my site" / "How many tags do I have?"
- **Governance:** "We have a messy GTM" / "Can you find unused tags?"
- **Migration:** "We switched platforms" / "Cleanup after agency handover"
- **Compliance:** "GDPR audit" / "Which tags fire before consent?"

## Required Tools

| Tool | Purpose |
|------|---------|
| `gtm_list_containers` | List all containers across accounts |
| `gtm_audit` | Deep audit of a specific container (tags, triggers, variables) |

---

## Part 1: Container Discovery

### Step 1: List Available Containers

```
gtm_list_containers()
```

Present a summary table:

| Account | Container Name | Public ID | Type | Workspaces |
|---------|---------------|-----------|------|-----------|
| [account] | [name] | GTM-XXXXX | web | [N] |

If multiple containers exist, ask the user which to audit, or audit all if requested.

---

## Part 2: Deep Container Audit

### Step 2: Run Full Audit

```
gtm_audit(container_path="accounts/[ID]/containers/[ID]")
```

The audit returns: tags, triggers, variables, workspace summary, built-in variables.

---

## Part 3: Health Scoring Framework

Score each area 0-100, then compute overall health:

### Tag Health (30% of score)

| Issue | Severity | Points Deducted |
|-------|----------|----------------|
| Tag with no trigger | Critical | -15 per tag |
| Duplicate tag name | High | -10 per duplicate |
| Paused tag (> 90 days) | Medium | -5 per tag |
| Tag firing on All Pages without filter | Medium | -5 per tag |
| Deprecated tag type | High | -10 per tag |
| More than 80 tags total | Low | -5 |

### Trigger Health (25% of score)

| Issue | Severity | Points Deducted |
|-------|----------|----------------|
| Unused trigger (no tags) | High | -10 per trigger |
| All Pages trigger on conversion tags | Critical | -20 |
| Duplicate trigger names | Medium | -5 per duplicate |
| Regex trigger without testing | Medium | -5 per trigger |

### Variable Health (20% of score)

| Issue | Severity | Points Deducted |
|-------|----------|----------------|
| Undefined variable referenced in tag | Critical | -20 per var |
| Unused variable (defined but not used) | Low | -3 per variable |
| Data Layer variable with typos | High | -10 per var |
| More than 50 custom variables | Low | -5 |

### Workspace Health (15% of score)

| Issue | Severity | Points Deducted |
|-------|----------|----------------|
| Unpublished changes > 30 days old | High | -15 |
| Multiple workspaces (> 3) active | Medium | -10 |
| No version history visible | Medium | -10 |

### Governance (10% of score)

| Issue | Severity | Points Deducted |
|-------|----------|----------------|
| Tags without notes/descriptions | Low | -3 per 10 tags |
| Inconsistent naming convention | Medium | -10 |
| No folder organization | Low | -5 |

### Health Score Bands

| Score | Rating | Action |
|-------|--------|--------|
| 90-100 | Excellent | Monitor only |
| 75-89 | Good | Minor cleanup recommended |
| 60-74 | Fair | Scheduled cleanup within 30 days |
| 40-59 | Poor | Immediate cleanup required |
| < 40 | Critical | Full audit and remediation urgently needed |

---

## Part 4: Common Issue Patterns

### Duplicate Conversion Tracking

Detected when: Multiple tags firing the same conversion event (e.g., two Google Ads
conversion tags for "purchase" or identical GA4 purchase events).

**Impact:** Doubles reported conversions, distorts ROAS, inflates Google Ads bidding.

**Fix:** Consolidate to one tag per conversion event. Use GA4 linked conversions instead
of separate Google Ads conversion pixel where possible.

### All-Pages Firing Tags

Detected when: A tag (especially conversion or remarketing tags) has "All Pages" as its
only trigger.

**Impact:** Fires conversion on every page visit → massive false conversion count.

**Fix:** Replace with specific page/event trigger (e.g., `Thank You Page` URL trigger,
`form_submit` event trigger).

### Orphaned Tags

Detected when: Tags exist with no trigger assigned (paused indefinitely or accidentally
created).

**Impact:** Clutter, confusion during future edits, potential accidental activation.

**Fix:** Delete confirmed-unused tags or add a descriptive note + archive label.

### Data Layer Race Conditions

Detected when: Variables reference dataLayer keys (e.g., `ecommerce.purchase.revenue`)
but no dataLayer push is confirmed in the trigger configuration.

**Impact:** Variables evaluate as `undefined` → broken conversions, empty event params.

**Fix:** Ensure dataLayer.push() fires BEFORE GTM fires the tag. Use "DOM Ready" or
custom event triggers instead of page load triggers for dynamically loaded data.

### Consent Violation Risk

Detected when: Marketing/analytics tags (Google Ads, Meta Pixel, LinkedIn Insight) fire
without a consent check trigger or Consent Mode configuration.

**Impact:** GDPR non-compliance. Potential fines up to 4% of annual revenue.

**Fix:** Implement Consent Mode v2. Add "consent granted" trigger to all marketing tags.
Ensure tags default to `denied` before consent.

> **Consent Mode v2 is mandatory for EEA advertisers since March 2024.** Consent Mode v2 adds two new required parameters beyond the original v1:
> - `ad_user_data`: Controls whether user data can be sent to Google for advertising
> - `ad_personalization`: Controls whether ads can be personalized for the user
>
> Both must be explicitly set. Without them, Google may restrict access to audience features and Smart Bidding in the EEA. Check that your CMP (Cookiebot, OneTrust, Usercentrics, etc.) is configured to pass all four parameters: `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`.

---

## Part 5: Tag Type Classification

Classify all tags found:

| Category | Tag Types | Risk Level |
|----------|-----------|-----------|
| Analytics | GA4, UA, Adobe Analytics | Low |
| Advertising | Google Ads, Meta Pixel, LinkedIn Insight, TikTok Pixel | High (consent) |
| Remarketing | Dynamic remarketing tags, Custom audience pixels | High (consent) |
| Conversion | Google Ads conversion, GA4 conversion events | Critical (accuracy) |
| Utility | Custom HTML, Custom Image, Hotjar, Clarity | Medium |
| Deprecated | UA/GA3 tags, old conversion linkers | High (remove) |

Flag any **deprecated** tag types immediately — Universal Analytics ended July 2024.

---

## Part 6: Output Format

```
================================================================================
               GTM CONTAINER AUDIT REPORT
               Container: [GTM-XXXXX] — [Container Name]
               Account: [Account Name]
               Audit Date: [YYYY-MM-DD]
================================================================================

OVERALL HEALTH SCORE: [N]/100 — [Rating]

SUMMARY
───────────────────────────────────
Total Tags:       [N] ([N] active, [N] paused)
Total Triggers:   [N] ([N] unused)
Total Variables:  [N] custom + [N] built-in
Workspaces:       [N] ([N] with unpublished changes)
Container Type:   [web/ios/android/amp]

CATEGORY SCORES
───────────────────────────────────
Tag Health:        [N]/100
Trigger Health:    [N]/100
Variable Health:   [N]/100
Workspace Health:  [N]/100
Governance:        [N]/100

═══════════════════════════════════
CRITICAL ISSUES (Fix Immediately)
═══════════════════════════════════
[List issues with Severity: Critical]

Example:
⛔ 2 conversion tags fire on ALL PAGES — false conversions guaranteed
   Tags: "GA4 - Purchase", "Google Ads - Conversion"
   Fix: Replace trigger with "Thank You Page" URL contains /thank-you

⛔ Google Ads conversion tag has no trigger
   Tag: "Ads Conversion - Lead"
   Fix: Assign appropriate trigger or delete if unused

═══════════════════════════════════
HIGH PRIORITY (Fix Within 7 Days)
═══════════════════════════════════
[List high-severity issues]

⚠️ 4 orphaned triggers (no tags using them)
   Triggers: [list names]
   Fix: Delete unused triggers to reduce confusion

⚠️ Universal Analytics tag detected — GA3 deprecated since July 2024
   Tag: "UA - Pageview"
   Fix: Remove. Ensure GA4 replaces all UA functionality.

═══════════════════════════════════
MEDIUM PRIORITY (Fix Within 30 Days)
═══════════════════════════════════
[List medium-severity issues]

═══════════════════════════════════
TAG INVENTORY
═══════════════════════════════════
| Tag Name | Type | Trigger | Status | Issue |
|----------|------|---------|--------|-------|
| GA4 Config | GA4 | All Pages | Active | ✅ OK |
| Ads - Purchase | Google Ads | Thank You | Active | ✅ OK |
| Old UA Tag | UA | All Pages | Paused | ⚠️ Deprecated |

═══════════════════════════════════
CONSENT COMPLIANCE CHECK (Consent Mode v2)
═══════════════════════════════════
Marketing tags found: [N]
Tags with consent trigger: [N]
Tags WITHOUT consent check: [N] ← [Compliant / RISK]

Consent Mode v2 status:
  ad_storage configured:        [Yes / No / Unknown]
  analytics_storage configured: [Yes / No / Unknown]
  ad_user_data configured:      [Yes / No / Unknown]  ← v2 required
  ad_personalization configured:[Yes / No / Unknown]  ← v2 required

[List non-compliant tags if any]

Note: All four Consent Mode v2 parameters are mandatory for EEA advertisers
(required by Google since March 2024). Missing ad_user_data or ad_personalization
will restrict Smart Bidding and audience features in Google Ads.

═══════════════════════════════════
REMEDIATION ROADMAP
═══════════════════════════════════
Week 1 — Critical fixes:
1. [Specific action]
2. [Specific action]

Week 2 — High priority:
3. [Specific action]

Month 1 — Medium priority:
4. [Specific action]

ESTIMATED EFFORT: [X] hours
EXPECTED DATA ACCURACY IMPROVEMENT: [X]%
```

---

## Part 6b: Server-Side Tagging Assessment

Server-side GTM (sGTM) is now mainstream and directly relevant to container audits. When auditing a web container, assess whether server-side tagging should be recommended.

### Signs Server-Side Tagging Would Help

| Observation | Recommendation |
|-------------|---------------|
| 15+ tags on All Pages | Move heavy tags (Meta Pixel, GA4) to server-side |
| Ad blockers impacting conversion data | Server-side bypasses most ad blockers |
| ITP/cookie restrictions on Safari | Server-side extends cookie lifetime |
| CAPI or Enhanced Conversions not implemented | sGTM is the easiest path to server-side |
| Page load > 3s with GTM contributing | Offload tag execution server-side |

### sGTM vs Web GTM Responsibilities

| Function | Web GTM | Server GTM |
|----------|---------|------------|
| Data layer push | Yes | No |
| Event collection (GA4) | Can be replaced | Preferred |
| Ad pixels (Meta, TikTok, LinkedIn) | High risk (consent/blocking) | Better — consent-aware server call |
| Conversion tracking (Google Ads) | Fine | Also fine via Enhanced Conversions |
| Custom HTML tags | Full control | Limited (server-side only) |

When a web container has many marketing tags AND no server container is in use, flag this in the audit with a recommendation to consider sGTM as a Phase 2 improvement.

---

## Part 7: Industry Benchmarks

### Healthy Container Metrics

| Metric | Healthy Range | Warning | Critical |
|--------|--------------|---------|----------|
| Total tags | < 50 | 50-100 | > 100 |
| Unused triggers | < 5% | 5-15% | > 15% |
| Tags without notes | < 20% | 20-50% | > 50% |
| Paused tags | < 10% | 10-25% | > 25% |
| Active workspaces | 1-2 | 3-4 | > 4 |

### GTM Performance Impact

Each additional tag on All Pages adds ~5-15ms to page load time:
- 20 tags: ~100-300ms overhead
- 50 tags: ~250-750ms overhead
- 100 tags: ~500ms-1.5s overhead (significant SEO and UX impact)

Recommend: Audit tags that fire on All Pages. Can most fire on specific events instead?

## Optional: Enrich with Live Data

If the user has connected their GTM account, run a live container audit instead of relying on manual review:

```python
# Pull a full audit of the container — tags, triggers, variables, and issues
gtm_audit(container_path="accounts/YOUR_ACCOUNT_ID/containers/YOUR_CONTAINER_ID")
```

This returns tag counts, firing rules, variable usage, and flags common issues (missing notes, paused tags, All Pages over-triggers). Use the audit output to populate the framework above with real data rather than estimates.
