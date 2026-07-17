---
description: Audit your Google Tag Manager containers for misconfigurations, duplicate tracking, unused tags/triggers, consent compliance gaps, and performance issues. Returns a prioritized remediation roadmap with health scores. (requires Pro subscription)
disable-model-invocation: true
---

> **Platforms:** google_tag_manager
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# GTM Container Audit

Audit Google Tag Manager containers for issues, health scoring, and prioritized remediation.

- Container: all
- Focus: all

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### Health Score: [N]/100 -- [Excellent/Good/Fair/Poor/Critical]

Score bands: 90-100 Excellent | 75-89 Good | 60-74 Fair | 40-59 Poor | <40 Critical

### Summary
| Metric | Count |
|--------|-------|
| Active Tags | N |
| Paused Tags | N |
| Triggers | N (N unused) |
| Custom Variables | N |
| Built-in Variables | N |
| Workspaces | N |

### Category Scores
| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Tag Health | N/100 | 30% | N |
| Trigger Health | N/100 | 25% | N |
| Variable Health | N/100 | 20% | N |
| Workspace Health | N/100 | 15% | N |
| Governance | N/100 | 10% | N |
| **Overall** | | | **N/100** |

### Critical Issues (fix immediately)
| # | Issue | Tag/Trigger | Impact | Fix |
|---|-------|-------------|--------|-----|

### High Priority (fix within 7 days)
| # | Issue | Tag/Trigger | Impact | Fix |
|---|-------|-------------|--------|-----|

### Consent Compliance
| Metric | Value |
|--------|-------|
| Marketing/Ad tags | N |
| With consent gate | N |
| At risk (no consent) | N |
Tags at risk: [list tag names firing without consent check]

### Tag Inventory
| Tag Name | Type | Trigger | Status | Issue |
|----------|------|---------|--------|-------|

### Remediation Roadmap
**Week 1 (Critical):** [actions]
**Week 2 (High):** [actions]
**Month 1 (Medium):** [actions]
Estimated effort: X hours

## EXECUTION STEPS

### Step 1: Discover containers
{% if container_id == "all" or not container_id %}
```
gtm_list_containers()
```
List all containers. Present container names and IDs. Proceed to audit each (or ask user to pick one if many).

Audit container: [specify container_id]


### Step 2: Run deep audit
For each container to audit:
```
gtm_audit(container_path="CONTAINER_ID")
```
This returns the full container state: all tags, triggers, variables, workspaces, and their relationships.

### Step 3: Score Tag Health (30% weight)
Start at 100, deduct:
| Issue | Severity | Deduction |
|-------|----------|-----------|
| Tag with no trigger | Critical | -15 each |
| Duplicate tag names | High | -10 each |
| Tag firing on All Pages without filter | Medium | -5 each |
| Deprecated UA/GA3 tags | High | -10 each |
| More than 80 total tags | Low | -5 |

### Step 4: Score Trigger Health (25% weight)
Start at 100, deduct:
| Issue | Severity | Deduction |
|-------|----------|-----------|
| Conversion tag on All Pages trigger | Critical | -20 |
| Unused triggers (no tags reference them) | High | -10 each |
| Duplicate trigger names | Medium | -5 each |

### Step 5: Score Variable Health (20% weight)
Start at 100, deduct:
| Issue | Severity | Deduction |
|-------|----------|-----------|
| Undefined variable referenced in tag | Critical | -20 each |
| Unused custom variables | Low | -3 each |
| More than 50 custom variables | Low | -5 |

### Step 6: Score Workspace Health (15% weight)
Start at 100, deduct:
| Issue | Severity | Deduction |
|-------|----------|-----------|
| Unpublished changes > 30 days old | High | -15 |
| More than 3 active workspaces | Medium | -10 |

### Step 7: Score Governance (10% weight)
Start at 100, deduct:
| Issue | Severity | Deduction |
|-------|----------|-----------|
| Tags without notes/description | Low | -3 per 10 tags |
| Inconsistent naming conventions | Medium | -10 |
| No folder organization | Low | -5 |

### Step 8: Consent compliance check
Identify all advertising/marketing tags:
- Google Ads conversion/remarketing tags
- Meta/Facebook Pixel
- LinkedIn Insight Tag
- TikTok Pixel
- Any tag type containing "ads", "remarketing", "pixel", "conversion"

For each, check:
- Does its trigger include a consent condition (e.g., consent_granted, cookie_accepted)?
- Is Consent Mode v2 configured in the container?
- Flag any marketing tag that could fire without user consent as GDPR risk.

### Step 9: Calculate overall score and compile
```
overall = (tag_score * 0.30) + (trigger_score * 0.25) + (variable_score * 0.20) + (workspace_score * 0.15) + (governance_score * 0.10)
```
Classify all issues by severity (Critical/High/Medium). Generate the remediation roadmap ordered by severity.

## EDGE CASES
- **No containers found**: User may not have GTM access connected. Advise connecting GTM in the Ad Superpowers dashboard.
- **Empty container (no tags)**: Score as 100/100 for tag/trigger/variable health but note the container is unused. Recommend setting up initial tracking.
- **No access to container**: gtm_audit will return a permission error. Advise user to grant read access to the service account.
- **Very large container (100+ tags)**: Scoring still applies but note that large containers inherently have more governance challenges. Recommend splitting into multiple containers by site section.
- **Multiple containers for same site**: Flag potential duplicate tracking risk. Check if the same conversion tags appear in multiple containers.
{% if focus != "all" and focus %}
- **Focused audit ([specify focus])**: Only score and report on the [specify focus] dimension. Skip other category scores but still calculate overall health with available data.