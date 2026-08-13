---
description: "Proactively detect ad creative fatigue before performance tanks. Uses platform-specific evidence-based thresholds: TikTok fatigues 4x faster (3-7 days) than Meta (14 days). Google Ads uses asset ratings (4-8 weeks). LinkedIn has longest cycles (4-6 weeks). (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, tiktok, linkedin, google_ads
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Creative Fatigue Scanner

Scan for creative fatigue across all ad platforms. Each platform fatigues at dramatically different speeds — apply the correct thresholds or you will miss TikTok fatigue and over-rotate on LinkedIn.

| Platform | Fatigue Cycle | Refresh Cadence | Creatives Needed | Detection Method | Decline Speed |
|----------|--------------|-----------------|------------------|-----------------|---------------|
| TikTok | 3-7 days | 3-5 days | 8-12 | Frequency + CTR | Cliff (-20%/day) |
| Meta | ~14 days | 7-14 days | 4-6 | Frequency + CTR | Gradual (~2%/day) |
| LinkedIn | 4-6 weeks | 4-6 weeks | 3-4 | Frequency + CTR | Slow (~1%/day) |
| Google Ads | 4-8 weeks | Monthly | 15+ per asset group | Asset Ratings | Very slow (~0.5%/wk) |

Fatigue speed: TikTok (4x) > Meta (1x) > LinkedIn (0.25x) > Google Ads (0.125x). Google Ads uses Asset Ratings (Best/Good/Low/Pending) instead of frequency.

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### PLATFORM SUMMARY
| Platform | Ads/Assets Scanned | Healthy | Warning | Critical | Avg Age |
|----------|-------------------|---------|---------|----------|---------|
| TikTok | X | Y | Z | W | D days |
| Meta | X | Y | Z | W | D days |
| Google Ads | X assets | Y | Z | W | D days |
| LinkedIn | X | Y | Z | W | D days |

Note: TikTok ads fatigue 4x faster — check these first. Google Ads uses Asset Ratings instead of frequency.

### HIGH FATIGUE - TIKTOK (Refresh within 24-48h)
| Ad Name | Freq | CTR Change (3d) | CPM Change | Days Active | Score |
|---------|------|-----------------|------------|-------------|-------|

### HIGH FATIGUE - META (Refresh within 7 days)
| Ad Name | Freq | CTR Change (7d) | CPM Change | Days Active | Score |
|---------|------|-----------------|------------|-------------|-------|

### HIGH FATIGUE - GOOGLE ADS (Refresh within 2-4 weeks)
| Asset Group/Ad | % Low Rated | CTR Change (30d) | CPA Change | Last Refresh | Score |
|----------------|-------------|------------------|------------|--------------|-------|
"% Low Rated" = percentage of assets rated "Low" for 30+ days.

### HIGH FATIGUE - LINKEDIN (Refresh within 2 weeks)
| Ad Name | Freq | CTR Change (14d) | CPM Change | Days Active | Score |
|---------|------|------------------|------------|-------------|-------|

### RECOMMENDATIONS
**TikTok:** Rotate every 3-5 days. Keep 8-12 creatives in rotation. UGC lasts 20-30% longer. New hook = highest impact refresh.

**Meta:** Rotate every 7-14 days. Keep 4-6 creatives per ad set. Dynamic Creative extends lifespan. UGC lasts 17-18 days vs 10-12 polished.

**Google Ads:** Monthly 20-30% asset refresh. Replace "Low" rated assets after 30+ days. Add variations of "Best" rated assets. PMax needs 15+ assets per group.

**LinkedIn:** Rotate every 4-6 weeks. Keep 3-4 creatives per campaign. Message Ads fatigue slower. Professional audience tolerates higher frequency.

## EXECUTION STEPS

### Step 1: Discover Accounts
- `meta_list_ad_accounts()`
- `google_ads_list_accounts()`
- `linkedin_list_ad_accounts()`
- `tiktok_get_advertiser_info()`

### Step 2: Gather Creative Data Per Platform

**Meta Ads:** `meta_get_insights(account_id="FROM_STEP_1", date_preset="last_14d", level="ad", fields=["ad_name","impressions","reach","frequency","clicks","ctr","cpm","cpc","actions","spend"])`

Also get previous period: `meta_get_insights(account_id="FROM_STEP_1", level="ad", fields=["ad_name","frequency","ctr","cpm"], time_range={"since":"21_DAYS_AGO","until":"8_DAYS_AGO"})`

**TikTok Ads:** `tiktok_get_report(start_date="7_DAYS_AGO", end_date="TODAY", level="ad", metrics=["ad_name","impressions","reach","frequency","clicks","ctr","cpm","cpc","spend","conversions"])`

Also previous 3-day window for trend comparison.

**LinkedIn Ads:** `linkedin_get_analytics(account_id="FROM_STEP_1", start_date="30_DAYS_AGO", end_date="TODAY", fields=["impressions","clicks","costInLocalCurrency","externalWebsiteConversions"])`

**Google Ads:** `google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT asset_group.name, asset_group_asset.performance_label, asset_group_asset.field_type, campaign.name, metrics.impressions, metrics.clicks, metrics.ctr, metrics.cost_micros, metrics.conversions FROM asset_group_asset WHERE segments.date DURING LAST_30_DAYS")`

For Display/YouTube: `google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT ad_group_ad.ad.name, metrics.impressions, metrics.clicks, metrics.ctr, metrics.average_cpc, metrics.cost_micros, metrics.conversions FROM ad_group_ad WHERE campaign.advertising_channel_type IN ('DISPLAY','VIDEO') AND segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC")`

### Step 3: Apply Platform-Specific Fatigue Detection

**Meta Ads thresholds:**
| Indicator | Prospecting | Retargeting | Warning | Critical |
|-----------|-------------|-------------|---------|----------|
| Frequency | >3/week | >5/week | >4/week | >6/week |
| CTR Decline (WoW) | >10% | >15% | >15% | >20% |
| CPM Increase (WoW) | >20% | >25% | >25% | >40% |
| Days Active | >10 days | >14 days | >14 days | >21 days |

**TikTok Ads thresholds (4x faster!):**
| Indicator | Prospecting | Retargeting | Warning | Critical |
|-----------|-------------|-------------|---------|----------|
| Frequency | >4/week | >6/week | >5/week | >8/week |
| CTR Decline (3-day) | >15% | >20% | >20% | >30% |
| CPM Increase (3-day) | >20% | >25% | >25% | >40% |
| Days Active | >5 days | >7 days | >5 days | >7 days |

**LinkedIn Ads thresholds (slower B2B cycles):**
| Indicator | Lead Gen | Brand | Warning | Critical |
|-----------|----------|-------|---------|----------|
| Frequency | >4/week | >6/week | >5/week | >8/week |
| CTR Decline (2-week) | >15% | >20% | >20% | >30% |
| CPM Increase (2-week) | >25% | >30% | >30% | >50% |
| Days Active | >30 days | >45 days | >35 days | >45 days |

**Google Ads thresholds (Asset Ratings based — different method!):**
| Indicator | PMax | Display | YouTube | Warning | Critical |
|-----------|------|---------|---------|---------|----------|
| "Low" Assets | >20% | >25% | N/A | >30% | >40% |
| CTR Decline (month) | >10% | >15% | >15% VTR | >15% | >25% |
| CPA Increase (month) | >15% | >20% | >25% CPV | >20% | >35% |
| Days Active | >45 days | >30 days | >60 days | >45d | >60d |

Google Ads key differences: No frequency metric at creative level — use Asset Ratings. "Low" rated assets for 30+ days = fatigue. PMax: check asset group performance, not ad-level.

### Step 4: Calculate Fatigue Scores

Scoring (100-point scale):

**Frequency-based platforms (Meta, TikTok, LinkedIn):**
- Frequency above threshold: +30 points
- CTR decline above threshold: +25 points
- CPM increase above threshold: +25 points
- Creative age above threshold: +20 points

**Google Ads (asset-rating based):**
- % "Low" assets above threshold: +35 points
- CTR decline above threshold: +20 points
- CPA increase above threshold: +25 points
- Days since last refresh above threshold: +20 points

Score interpretation: >=50 = HIGH FATIGUE | 30-49 = WARNING | <30 = HEALTHY

### Step 5: Present Results
Follow OUTPUT FORMAT above EXACTLY. Sort high-fatigue ads by score descending. Show TikTok first (fastest fatigue).

## EDGE CASES
- No active ads on a platform: Skip that platform, note "No active ads"
- Account just launched (<7 days): Insufficient data for trend analysis — note "Too early to detect fatigue"
- All creatives healthy: Confirm healthy status, suggest proactive refresh schedule
- Google Ads without PMax: Use Display/YouTube thresholds only, skip asset rating analysis
- Single platform only: Run full analysis for that platform, skip cross-platform summary row
- TikTok with no frequency data: Fall back to CTR trend + creative age only
- API error on one platform: Note the error, continue with remaining platforms