---
description: End-to-end creative refresh pipeline: analyze ad performance, detect fatigue, build a creative brief from your top performers, then upload and deploy a new image you provide (local file up to 4 MB, or any public HTTPS URL). Image generation happens outside the app — bring your own image from Photoshop, Canva, Midjourney, Gemini, or anywhere. (requires Pro subscription)
disable-model-invocation: true
---

> **Platforms:** meta
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Creative Refresh

End-to-end creative refresh pipeline: analyze performance → detect fatigue → build a creative brief from top performers → upload your new image → deploy as a paused ad for review.

**Image generation is intentionally NOT part of this workflow.** Use whatever image tool you prefer (Photoshop, Canva, Midjourney, ChatGPT/Gemini in your client, etc.) — this workflow handles everything around the image: the analysis, the brief that tells you what to make, the upload, and the deployment.

**Requirements:**
- Connected Meta Ads account
- A new image you want to deploy (after Step 5):
  - **Local file:** any PNG/JPEG up to **4 MB raw**. Your AI client reads and base64-encodes the bytes for you.
  - **Public URL:** any HTTPS link (Canva export, S3, CDN, etc.). No size limit beyond Meta's own (~30 MB).

## OUTPUT FORMAT

### CREATIVE AUDIT SUMMARY
| Metric | Value |
|--------|-------|
| Account | {account name} |
| Campaign | {campaign name} |
| Active Ads | {count} |
| Fatigued Ads | {count} |
| Top Performer | {ad name} (CTR: X%, ROAS: Y) |
| Avg Creative Age | {days} days |

### TOP PERFORMERS (Reference for the Creative Brief)
| Ad Name | CTR | CPC | ROAS | Impressions | Days Active | Image Style |
|---------|-----|-----|------|-------------|-------------|-------------|

### FATIGUED ADS (Need Refresh)
| Ad Name | Frequency | CTR Decline | CPM Change | Days Active | Fatigue Score |
|---------|-----------|-------------|------------|-------------|---------------|

### CREATIVE BRIEF (For You to Execute Externally)
- **Visual style:** {derived from top performer}
- **Subject / focal point:** {derived}
- **Color palette:** {derived}
- **Composition / framing:** {derived}
- **Lighting:** {derived}
- **Aspect ratio:** 4:5
- **Variations to produce:** {{ num_variations | default(2) }}
- **Negative cues (avoid):** {derived}

### UPLOAD + DEPLOYMENT STATUS
| Image | Source | image_hash | Ad Name | Ad Set | Status | Ad ID |
|-------|--------|------------|---------|--------|--------|-------|

## EXECUTION STEPS

### Step 1: Discover Account
```
meta_list_ad_accounts()
```
Let the user select their account or use account `[specify account_id]`.

### Step 2: Creative Audit
Fetch current creatives with performance data:
```
meta_get_creatives(account_id="FROM_STEP_1", scope="campaign", campaign_id="[specify campaign_id]")
```

Then get insights for trend analysis:
```
meta_get_insights(account_id="FROM_STEP_1", date_preset="last_14d", level="ad", fields=["ad_name","impressions","reach","frequency","clicks","ctr","cpm","cpc","spend","actions"])
```

Also get the previous period for comparison:
```
meta_get_insights(account_id="FROM_STEP_1", level="ad", fields=["ad_name","frequency","ctr","cpm"], time_range={"since":"21_DAYS_AGO","until":"8_DAYS_AGO"})
```

### Step 3: Fatigue Detection
Apply Meta fatigue thresholds:
| Indicator | Warning | Critical |
|-----------|---------|----------|
| Frequency | >4/week | >6/week |
| CTR Decline (WoW) | >15% | >20% |
| CPM Increase (WoW) | >25% | >40% |
| Days Active | >14 days | >21 days |

Score each ad (100-point scale):
- Frequency above threshold: +30 points
- CTR decline: +25 points
- CPM increase: +25 points
- Creative age: +20 points

Score >=50 = HIGH FATIGUE | 30-49 = WARNING | <30 = HEALTHY

### Step 4: Analyze Top Performers
From the creative audit, identify the winning elements of the best-performing ads (highest CTR + ROAS):
- **Visual style:** Product photo, lifestyle, UGC, flat lay
- **Color palette:** Dominant colors, contrast level
- **Composition:** Layout, subject placement, background
- **Lighting:** Natural, studio, dramatic, soft
- **Mood / emotion:** Confident, calm, urgent, aspirational

### Step 5: Output the Creative Brief
Synthesize Step 4 into a structured creative brief in the OUTPUT FORMAT above. **Stop here and present the brief to the user.** The user will use this brief externally (in their image tool of choice) to produce {{ num_variations | default(2) }} new image(s).

Wait for the user to come back with the image(s). Each image must be delivered as a **public HTTPS URL** (e.g., Canva export, Google Drive share link, Dropbox, S3). Meta fetches the image server-side — no base64 upload required. If the user has a local file, ask them to host it somewhere accessible first.

### Step 6: Deploy the New Creative(s)
For each image URL the user provides, pass it directly to `meta_create_ad` — the tool handles the Meta upload internally and creates the ad in one call.

### Step 7: Deploy to Meta (Approved Only)
For each approved image URL:
```
meta_create_ad(
    account_id="FROM_STEP_1",
    adset_id="FROM_USER",
    image_url="FROM_USER",
    headline="FROM_USER",
    body="FROM_USER",
    link_url="FROM_USER",
    cta_type="LEARN_MORE",
    status="PAUSED"
)
```

Ads are created as PAUSED for final review. Activate with `meta_update()`.

## EDGE CASES
- **No fatigued ads:** Confirm healthy status. Still offer a proactive refresh if any ad is >10 days old.
- **User has no image yet:** Stop at Step 5 with the creative brief. They'll come back with an image URL, then resume from Step 6.
- **User only has a local file:** Ask them to host it publicly (Canva export, Google Drive share link, Dropbox, S3) and provide the URL.
- **Image is not PNG/JPEG:** Ask the user to convert (Meta only accepts standard image formats).
- **Meta upload fails:** `meta_create_ad` returns a structured error with a hint. Surface it to the user — common causes are invalid `account_id`, an unreachable image URL, or missing ad-creation permissions.
- **No ad sets available:** Help the user identify the right ad set via `meta_query`.
- **All ads performing well:** Suggest A/B testing the new creative against the current winners rather than replacing them.