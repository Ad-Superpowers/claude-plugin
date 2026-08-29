---
name: meta-media-upload-guide
description: "This skill should be used when the user asks to \"upload a video to Meta\", \"upload an image to Meta\", \"push a local file into Meta media library\", \"use a Canva / Google Drive / Dropbox asset for an ad\", \"Meta says it can't upload my local file\", \"how do I get an image_hash\", \"bulk upload creatives\", or mentions \"image_url vs image_hash\", \"video_url vs video_id\", \"Meta Media Library\", \"Zakelijke media\", or \"Meta asset hosting\". Covers the complete decision tree from a file on disk to a usable Meta asset. Do NOT use for: ad copy (use ad-copy-generator), video scripts (use video-script-writer), creative strategy (use creative-diversification-generator), CAPI / pixel setup (use capi-implementation-guide)."
---
# Meta Media Upload Guide

The single source of truth for getting creative assets into Meta Ads when using Ad Superpowers' MCP tools. Eliminates the most common workflow confusion: **"why won't Claude upload my local file?"**.

## Three Upload Tiers (in order of preference)

Three routes get media into Meta. Prefer them in this order — they trade off convenience for friction.

**Tier 1 — Public URL (preferred for everything).**
The lowest-friction path. Works for images and videos alike. Meta fetches server-side, no MCP transport cost. Use this whenever the asset already lives on a URL (Notion, Google Drive, Dropbox, Canva, S3, Cloudinary, your own CDN).

**Tier 2 — Local file upload (images only, up to 4 MB).**
`meta_upload_image(image_data=<base64>)` accepts base64-encoded bytes directly from Claude Desktop (Cowork) or Claude Code. The MCP tool decodes and forwards to Meta's `adimages` endpoint as bytes. Great for one-off image uploads from a file on disk. **Videos do not have this path** — a typical ad video is 5–50 MB and the MCP transport is not designed for GB-scale binary payloads. Host videos somewhere and use Tier 1.

**Tier 3 — Manual Ads Manager upload + library discovery.**
Drag-drop into the Ads Manager Media Library UI (NL: "Media op advertentieaccountniveau" / "Zakelijke media"), then `meta_query(account_id, "adimages")` or `"advideos"` to list hashes + IDs. Ideal for bulk drops (50+ files) and for situations where Meta is the only sanctioned store.

**Why not inline bytes for video?** A 50 MB video → ~67 MB base64 → bloats every message in the conversation and often exceeds the MCP response limit. Meta's own recommendation is server-side URL fetch for video. Don't fight it.

## Decision Tree

```
START: What do you have?
│
├─► Public URL already (Canva export, Notion, Drive direct link, Dropbox, etc.)
│   └─► PATH A — image_url / video_url on meta_create_ad (Tier 1)
│
├─► image_hash / video_id already in Meta's library
│   └─► PATH B — reuse by hash/id (fastest, zero upload cost)
│
├─► Local IMAGE file on disk, ≤ 4 MB
│   └─► PATH C — meta_upload_image(image_data=<base64>) (Tier 2)
│
├─► Local VIDEO file on disk (any size)
│   └─► PATH D — host first (Drive/Dropbox/Cloudinary/S3), then PATH A
│
└─► A folder of 10+ creatives for bulk
    └─► PATH E — Ads Manager UI drag-drop → meta_query(adimages/advideos) (Tier 3)
```

**Filename hints reduce friction on every path.** Use consistent aspect-ratio suffixes when you name files (`_1x1`, `_9x16`, `_4x5`, `_16x9`, `_1.91x1`) so Claude can match the right asset to the right placement automatically after upload. See "Filename-based aspect ratio matching" below.

## PATH A — You already have a URL

Simplest case. The URL must be:

- **Publicly reachable HTTPS** (open an incognito browser window to verify — no auth wall, no VPN)
- **Direct link to the media file itself**, not a viewer page (for Google Drive / Dropbox, see PATH C hosting rules)
- **Format**: JPG / PNG for images; MP4 / MOV for video; GIF also accepted
- **Size constraints** (Meta-side): video 1s–241min, resolution ≥120x120, file ≤4 GB via URL fetch
- **Temporary URLs are fine** — Meta ingests the bytes server-side within seconds, so expiring links (presigned S3, Canva exports) work.

Commands:

```python
# Image ad
meta_create_ad(
    account_id="act_...",
    adset_id="...",
    headline="...", body="...", link_url="https://...",
    image_url="https://your-host/image.jpg",
)

# Video ad (single call — upload + ready-poll + create)
meta_create_ad(
    account_id="act_...",
    adset_id="...",
    headline="...", body="...", link_url="https://...",
    video_url="https://your-host/video.mp4",
)

# Pre-upload a video (decouple from ad creation)
meta_upload_video(account_id="act_...", video_url="https://...", title="Spring Launch v3")
# → returns {video_id: "12345...", status: "processing"}
# Wait 30-120s, then:
meta_get_video_status(video_id="12345...")
# → status: "ready" → now usable in meta_create_ad(video_id="12345...")
```

## PATH B — Reuse an existing library asset

If your asset is already in Meta's library (uploaded via an earlier ad, bulk-dropped in Ads Manager, or pushed via `meta_upload_video`), just reuse its handle. No re-upload.

**Find existing assets:**

```python
# Images in this ad account's library
meta_query(account_id="act_...", entity_type="adimages", limit=100)
# Returns items with: hash, name, width, height, aspect_ratio_bucket,
# created_time, url_128 (thumbnail), permalink_url, status, creatives[]

# Videos
meta_query(account_id="act_...", entity_type="advideos", limit=50)
# Returns items with: id, title, source, picture, length, format, aspect_ratio_bucket

# Filter by date — only assets uploaded since April 17
meta_query(account_id="act_...", entity_type="adimages", since="2026-04-17")
```

**Filter by placement using `aspect_ratio_bucket`:**

| Bucket | Placement use case |
|--------|-------------------|
| `9:16` | Stories, Reels, Instagram vertical |
| `4:5` | Mobile feed (Facebook + Instagram) |
| `1:1` | Feed carousel, square placements |
| `16:9` | Landscape video, in-stream |
| `1.91:1` | Link preview, right-column |

```python
# Pick an asset for Stories
result = await meta_query(account_id, "adimages")
stories_assets = [i for i in result["data"] if i["aspect_ratio_bucket"] == "9:16"]
hash_to_use = stories_assets[0]["hash"]

# Use in ad
meta_create_ad(..., image_hash=hash_to_use)
```

**Gotcha:** `image_hash` is scoped to the ad account. You cannot reuse a hash from account A in account B. Each account needs its own copy.

## PATH C — Local IMAGE file (base64 upload, Tier 2)

You have a `.jpg` / `.png` on disk, under 4 MB raw. Use `meta_upload_image` with `image_data`:

```python
# AI client (Claude Desktop / Cowork / Claude Code) reads the file:
#   with open("/path/to/hero.jpg", "rb") as f:
#       image_bytes = f.read()
#   image_data = base64.b64encode(image_bytes).decode()
#
# Then calls:
meta_upload_image(
    account_id="act_...",
    image_data="<base64 string>",
    name="spring-2026-hero_1x1_1080x1080",  # encode aspect-ratio hint
)
# → returns {success, image_hash, width, height, image_url (Meta CDN), deploy_hint}

# Then use the returned hash:
meta_create_ad(
    account_id="act_...",
    adset_id="...",
    headline="...", body="...", link_url="https://...",
    image_hash="<returned hash>",
)
```

**Naming discipline pays off.** The `name` argument is how you find the asset back later via `meta_query(adimages)` — and how Claude can auto-pick the right ratio per placement (see Filename Matching section below). Prefer descriptive names with aspect hints:

- `spring-hero_1x1_1080x1080.jpg`
- `nike-summer_9x16_1080x1920.jpg`
- `bundle-offer_4x5.png`

**Size cap:** 4 MB raw (~5.4 MB base64). For larger images, either downsize (1080x1080 JPEG quality 85 is typically well under 500 KB) or host the file and use PATH A.

**Cowork caveat:** Claude Desktop in Cowork mode reads local files and passes base64 along — this is the path that just works. Without Cowork, you're back to hosting the file first or using Claude Code with filesystem access.

## PATH D — Local VIDEO file (host first, Tier 1)

Video bytes are too large for MCP transport. Pick a hosting option, get a public URL, then use `meta_upload_video(video_url=...)` or `meta_create_ad(video_url=...)`.

### Hosting options (ranked by practicality)

| Option | Good for | Tradeoff |
|--------|----------|----------|
| **Ads Manager "Zakelijke media" UI** | One-off uploads, bulk drops | Manual; see PATH D for bulk flow |
| **Canva export link** | Assets designed in Canva | Share link must be "Anyone with the link can view"; Meta only needs seconds to fetch |
| **Google Drive direct link** | Files already in your Drive | Needs the `?export=download` trick (below) |
| **Dropbox direct link** | Files in Dropbox | Swap `?dl=0` for `?dl=1` |
| **Cloudinary (free tier)** | Programmatic pipelines, auto-optimization | Requires account; 25 credits/month free |
| **S3 presigned URL / Cloudflare R2** | Agency / team automation | Requires AWS or CF account; best for scale |
| **WeTransfer / SmashTransfer** | **Don't** | Transfer links expire mid-fetch; unreliable |

### Google Drive direct link trick

Google Drive's normal share link opens a viewer page, not the file. Meta's fetcher chokes on it. You need to convert it.

1. In Drive, right-click the file → Share → set to "Anyone with the link"
2. Copy the share link — it looks like:
   ```
   https://drive.google.com/file/d/1A2B3C4D5E6F/view?usp=sharing
   ```
3. Extract the file ID: `1A2B3C4D5E6F`
4. Build the direct-download URL:
   ```
   https://drive.google.com/uc?export=download&id=1A2B3C4D5E6F
   ```
5. Use this URL in `image_url` / `video_url`.

**Known issue:** for video files > ~25 MB Google Drive shows a "virus scan warning" interstitial that breaks direct fetch. For those, use Dropbox, S3, or Cloudinary instead.

### Dropbox direct link trick

1. In Dropbox, right-click → Share → Copy link
2. You get:
   ```
   https://www.dropbox.com/scl/fi/abcdef/video.mp4?rlkey=xyz&dl=0
   ```
3. Change `dl=0` → `dl=1`:
   ```
   https://www.dropbox.com/scl/fi/abcdef/video.mp4?rlkey=xyz&dl=1
   ```
4. Use this URL.

### Cloudinary (recommended for programmatic flows)

Free tier: 25 monthly credits ≈ 25 GB bandwidth. Upload via their API, get a permanent `https://res.cloudinary.com/...` URL, pass to Meta. Also handles image format conversion and video transcoding if needed.

### S3 presigned URL (recommended for agencies)

```bash
aws s3 cp video.mp4 s3://your-bucket/ads/
aws s3 presign s3://your-bucket/ads/video.mp4 --expires-in 3600
```

Meta fetches within seconds — a 1-hour TTL is plenty.

## PATH E — Bulk upload via Ads Manager UI (Tier 3)

You have a folder with 50+ creatives. Avoid one-at-a-time uploads.

**Flow:**

1. Go to Ads Manager → Ad Account → **Media Library** (NL: "Zakelijke media" voor media op businessniveau, **"Media op advertentieaccountniveau"** voor account-media)
2. Drag-drop the whole folder
3. Wait for Meta to process (few seconds per image, 30-120s per video)
4. Come back to Claude:
   ```python
   meta_query(account_id="act_...", entity_type="adimages", limit=250)
   ```
5. Claude picks the right `hash` per placement using `aspect_ratio_bucket` (PATH B).

**Why not the Business Media Library at business level?** That folder structure is API-gated (Business Creative Asset Management requires Meta partner approval). Ad-account media library is unrestricted and exactly what our tools list via `adimages` / `advideos`.

## Filename-Based Aspect Ratio Matching

When a campaign has multiple aspect ratios of the same creative (one per placement), Claude should match filenames intelligently rather than inspect every asset pixel-by-pixel. This section defines the patterns Claude should recognize. **This is interpretation-driven, not deterministic** — use judgment when a filename is ambiguous, fall back to `aspect_ratio_bucket` (post-upload, from `meta_query(adimages)`) as ground truth.

### Recognized Patterns (per aspect ratio)

**1:1 — Square (feed, carousel):**
- Explicit separators: `1x1`, `1X1`, `1-1`, `1_1`, `1.1`, `1:1`
- Compact codes: `11` (when clearly a ratio code in context, not a version number or year)
- Keywords: `square`, `sq`, `feed-square`, `ig-square`
- Resolution fingerprint: `1080x1080`, `1200x1200`, any `NxN` where N == N

**9:16 — Vertical (Stories, Reels):**
- Explicit separators: `9x16`, `9X16`, `9-16`, `9_16`, `9:16`, `9.16`
- Compact codes: `916`
- Keywords: `vertical`, `vert`, `portrait`, `story`, `stories`, `reel`, `reels`, `full-screen`, `fullscreen`
- Resolution fingerprint: `1080x1920`, `720x1280`, any `NxM` where M/N ≈ 1.78 (ratio 0.55–0.57)

**4:5 — Mobile feed (Instagram + Facebook):**
- Explicit separators: `4x5`, `4X5`, `4-5`, `4_5`, `4:5`, `4.5`
- Compact codes: `45` (when clearly a ratio code, not a year/version)
- Keywords: `mobile-feed`, `mobile`, `feed-mobile`, `ig-feed-mobile`, `portrait-feed`
- Resolution fingerprint: `1080x1350`, `1200x1500`, any `NxM` where M/N ≈ 1.25 (ratio 0.78–0.82)

**16:9 — Landscape (video feed, in-stream):**
- Explicit separators: `16x9`, `16X9`, `16-9`, `16_9`, `16:9`, `16.9`
- Compact codes: `169`
- Keywords: `horizontal`, `horiz`, `landscape`, `wide`, `widescreen`, `in-stream`, `instream`
- Resolution fingerprint: `1920x1080`, `1280x720`, any `NxM` where N/M ≈ 1.78 (ratio 1.75–1.78)

**1.91:1 — Link preview (open-graph style, right-column):**
- Explicit separators: `1.91x1`, `1.91-1`, `1.91_1`, `1.91:1`, `1_91x1`, `1p91x1`
- Compact codes: `1911` (rare but unambiguous in a ratio context)
- Keywords: `link`, `preview`, `og`, `banner`, `right-column`, `og-image`
- Resolution fingerprint: `1200x628`, `1080x566`, any `NxM` where N/M ≈ 1.91

### Interpretation Rules

1. **Explicit ratio tokens beat compact codes.** If a filename has `1x1`, read that — don't also try to interpret the `1080x1080` tail as `10801080`.
2. **Resolution > compact code when both present.** `hero_1080x1920.jpg` → 9:16 (from dims), even if the name doesn't carry a keyword.
3. **Keywords beat compact codes.** `spring_story_final.mp4` → 9:16 (from `story`), don't try to read `storyfinal` as a ratio.
4. **Compact codes need ratio context.** `v11.jpg` is a version number. `hero_v2_11.jpg` at first glance could be version 11 — but if the sibling file is `hero_v2_916.jpg`, the `_11` is very likely a 1:1 marker. Look at siblings and naming conventions within the same folder before deciding.
5. **Year-like and version-like numbers are NOT ratios.** `campaign_2026_hero.jpg` → not a ratio. `hero_v9.jpg` → not 9:16.
6. **When ambiguous, check post-upload.** `meta_query(account_id, "adimages", since="...")` returns `aspect_ratio_bucket` derived from the actual pixel dimensions — that's ground truth. Use it to reconcile.
7. **Prefer multiple variants over guessing.** If the user has 3 files like `hero_1x1.jpg`, `hero_9x16.jpg`, `hero_4x5.jpg`, build 3 ads (one per ratio with matching placements) rather than picking one and forcing it into all placements.

### Placement → ratio mapping (Meta 2026)

| Placement | Optimal ratio | Also accepted |
|-----------|---------------|---------------|
| Facebook Feed (desktop) | 1:1 | 1.91:1 |
| Facebook Feed (mobile) | 4:5 | 1:1 |
| Instagram Feed | 1:1 | 4:5 |
| Instagram Stories / Reels | 9:16 | — |
| Facebook Stories | 9:16 | — |
| Facebook Right Column | 1.91:1 | 1:1 |
| Audience Network | 1.91:1 | 1:1, 9:16 |
| Messenger inbox | 1:1 | 1.91:1 |
| In-stream video | 16:9 | 1:1, 4:5 |
| Threads | 1:1 | 9:16, 4:5 |

### Example — Claude picks assets for a multi-placement campaign

Given a folder with:
```
hero_1x1_1080x1080.jpg      → 1:1 (explicit + dims)
hero_9x16_1080x1920.jpg     → 9:16 (explicit + dims)
hero_4x5_1080x1350.jpg      → 4:5 (explicit + dims)
hero_story_1080x1920.mp4    → 9:16 (keyword + dims)
hero_169_1920x1080.mp4      → 16:9 (compact + dims)
```

A campaign targeting "feed + stories + in-stream" has two paths:

**Preferred — one ad, multiple assets via `placement_assets`:**
```python
# Upload all variants first (Recipe 5), then one meta_create_ad call:
meta_create_ad(
    ...,
    image_hash="<1x1 hash>",        # primary fallback
    placement_assets=[
        {"image_hash": "<9x16 hash>",
         "placements": ["instagram_stories", "facebook_stories", "instagram_reels"]},
    ],
)
# + a separate video ad for in-stream if the format is video:
meta_create_ad(..., video_id="<16:9 video_id>", adset_id="<video-specific adset>")
```

**Fallback — separate ads when bundling is impossible** (different copy per ratio, mixed image+video within one ad):
- Ad #1 with `hero_1x1` (feed placement)
- Ad #2 with `hero_9x16` + `hero_story` video (Stories / Reels)
- Ad #3 with `hero_169` (in-stream video)

Do NOT try to stretch a 1:1 asset across Stories placement — Meta's placement optimization may still deliver it, but the creative won't look native and performance drops.

## Troubleshooting

### "URL fetch failed" / "Image download failed"

- **Open the URL in an incognito browser window.** If you see a login wall, virus warning, or preview page (not the raw file), Meta's fetcher fails too.
- Google Drive: did you use the `?export=download` trick? Is the file >25 MB (if yes, switch to Dropbox / S3)?
- Dropbox: did you change `?dl=0` → `?dl=1`?
- Signed URLs: has the TTL expired between the ad creation attempt and Meta's fetch?
- CDN: some CDNs 403 non-browser user agents. Meta's fetcher identifies as `facebookexternalhit` — whitelist it or use a URL the CDN doesn't gate.

### "Unsupported format"

- Images: JPG, PNG, GIF. No WebP, no HEIC. Convert first (`sips -s format jpeg image.heic --out image.jpg` on Mac).
- Videos: MP4 or MOV. No MKV, no AVI, no WebM. Convert with ffmpeg: `ffmpeg -i input.mkv -c:v libx264 -c:a aac output.mp4`.

### "Video file too short" or "too long"

- Meta requires 1 second ≤ length ≤ 241 minutes
- Reels optimal: 15–60s (max 90s)
- Stories optimal: ≤15s (max 60s)
- Feed: 5–30s is the sweet spot

### "Image resolution too low"

- Minimum: 120x120
- Recommended: 1080x1080 (feed/carousel), 1080x1920 (Stories/Reels)
- Meta will refuse uploads smaller than 120px on either axis

### "Meta shows the old version of my image"

- Meta aggressively caches URLs. If you overwrote a file at the same URL, Meta may still serve the old version.
- **Fix:** rename the file OR add a cache buster (`?v=2` at the end of the URL) OR upload to a new URL entirely.

### "image_hash invalid" when reusing across accounts

- `image_hash` and `video_id` are scoped to the ad account. A hash from `act_111` will not work in `act_222`.
- **Fix:** re-upload to the target account. Optionally build a cross-account library via the Business Creative Asset Management API (requires Meta partner approval — not currently accessible).

### "Claude Desktop says it can't upload local files"

- For **images ≤ 4 MB**: use PATH C. `meta_upload_image(image_data=<base64>)` accepts inline bytes. Cowork can read the file and encode automatically. If the AI says "I can't", prompt it explicitly: "Use the `meta_upload_image` tool with the file base64-encoded via `image_data`".
- For **larger images or any video**: use PATH D. Host the file first (Google Drive direct link, Dropbox, Cloudinary, S3), then pass the URL. MCP binary transport is not designed for GB-scale payloads.
- Claude Code behaves the same — it reads files from disk and base64-encodes for `meta_upload_image`, OR hosts + passes URL for videos.

### "I uploaded a video 2 minutes ago but `meta_query(advideos)` doesn't show it"

- Meta's ad-account `/advideos` GET edge has 1–5 min eventual consistency for new uploads. Wait a moment and retry, or fetch the specific video directly via `meta_get_video_status(video_id=...)`.

## Quick Workflow Recipes

### Recipe 1 — Single image ad from Canva URL (fastest path, Tier 1)

```
1. In Canva: Share → Anyone with the link → Copy (or Download → Copy link)
2. Claude: meta_create_ad(
     account_id="act_...",
     adset_id="...",
     headline="...", body="...", link_url="https://...",
     image_url="<Canva link>",
   )
```

### Recipe 2 — Single image ad from a local file on disk (Tier 2)

```
1. User attaches hero_1x1_1080x1080.jpg to the conversation
   (Cowork mode reads it automatically; Claude Code reads it via file path).
2. Claude base64-encodes the bytes.
3. Claude: meta_upload_image(
     account_id="act_...",
     image_data="<base64 string>",
     name="spring-hero_1x1_1080x1080",
   )
   # → returns {image_hash: "abc...", width: 1080, height: 1080}
4. Claude: meta_create_ad(
     account_id="act_...",
     adset_id="...",
     headline="...", body="...", link_url="https://...",
     image_hash="abc...",
   )
```

### Recipe 3 — Single video ad from a local file (Tier 1 via hosting)

```
1. Upload video.mp4 to Dropbox → copy share link
2. Change ?dl=0 → ?dl=1
3. Claude: meta_create_ad(
     account_id="act_...",
     adset_id="...",
     headline="...", body="...", link_url="https://...",
     video_url="<Dropbox direct URL>",
   )
   # Meta fetches, processes, polls up to 10s for ready state.
```

### Recipe 4 — Reuse a Stories-shaped asset from last week (Tier 0 — best)

```
1. meta_query(account_id, "adimages", since="2026-04-13")
2. Pick the item with aspect_ratio_bucket == "9:16" and the right name
3. meta_create_ad(..., image_hash=<that hash>)
```

### Recipe 5 — Multi-ratio campaign from a folder of local images (Tier 2 batch)

**Preferred**: bundle all aspect ratios into ONE ad via `placement_assets`. This matches how Ads Manager "Customize media" works, preserves social proof across placements, and counts as 1 write instead of 3-4.

```
User provides a folder:
  /ads/spring/
    hero_1x1_1080x1080.jpg
    hero_4x5_1080x1350.jpg
    hero_9x16_1080x1920.jpg
    hero_1.91x1_1200x628.jpg

Claude reads filenames, applies Filename Matching rules:
  hero_1x1_*    → 1:1  (feed, carousel — primary/default)
  hero_4x5_*    → 4:5  (mobile feed)
  hero_9x16_*   → 9:16 (Stories, Reels)
  hero_1.91x1_* → 1.91:1 (right column, link preview)

Step 1 — upload all variants via meta_upload_image:
  meta_upload_image(account_id, image_data=<base64 1x1>, name="hero_1x1_1080x1080")
  meta_upload_image(account_id, image_data=<base64 4x5>, name="hero_4x5_1080x1350")
  meta_upload_image(account_id, image_data=<base64 9x16>, name="hero_9x16_1080x1920")
  meta_upload_image(account_id, image_data=<base64 1.91x1>, name="hero_1.91x1_1200x628")
  → collect image_hash values

Step 2 — create ONE ad with placement_assets bundling all variants:
  meta_create_ad(
      account_id=account_id,
      adset_id="...",
      headline="Spring launch",
      body="...",
      link_url="https://...",
      image_hash="<1x1 hash>",   # primary fallback (1:1 is the safest default)
      placement_assets=[
          {"image_hash": "<9x16 hash>",
           "placements": ["instagram_stories", "facebook_stories",
                          "instagram_reels", "facebook_reels"]},
          {"image_hash": "<4x5 hash>",
           "placements": ["instagram_feed", "facebook_feed"]},
          {"image_hash": "<1.91x1 hash>",
           "placements": ["facebook_right_column", "audience_network",
                          "messenger_inbox"]},
      ],
      status="PAUSED",
  )

Meta serves the right ratio per placement automatically. One ad, one
creative_id, one engagement post across placements.
```

**When to split into multiple ads instead of using `placement_assets`:**
- Headlines or body copy differ per ratio → can't bundle, each ad needs its own copy
- Mix of image and video per placement → Meta rejects mixed-media in one ad
- A/B testing different creative concepts (not just different ratios of the same concept)

### Placement_assets quick reference (2026-supported placements)

| Placement name | Meta platform + position | Typical ratio |
|----------------|-------------------------|---------------|
| `facebook_feed` | facebook / feed | 1:1, 4:5 |
| `facebook_stories` | facebook / story | 9:16 |
| `facebook_reels` | facebook / facebook_reels | 9:16 |
| `facebook_marketplace` | facebook / marketplace | 1:1 |
| `facebook_right_column` | facebook / right_hand_column | 1.91:1, 1:1 |
| `facebook_in_stream` | facebook / instream_video | 16:9 |
| `facebook_video_feeds` | facebook / video_feeds | 1:1, 16:9 |
| `facebook_search` | facebook / search | 1:1 |
| `instagram_feed` | instagram / stream | 1:1, 4:5 |
| `instagram_stories` | instagram / story | 9:16 |
| `instagram_reels` | instagram / reels | 9:16 |
| `instagram_profile_feed` | instagram / profile_feed | 1:1, 4:5 |
| `messenger_inbox` | messenger / messenger_home | 1:1, 1.91:1 |
| `audience_network` | audience_network / classic | 1.91:1, 1:1, 9:16 |
| `threads` | threads / feed | 1:1, 9:16 |

**Retired by Meta in Marketing API v26.0 (29 July 2026):** Instagram Explore
(both Explore and Explore Home) and Messenger Stories. Passing them now returns
an error explaining why. Explore is rejected by Meta outright; Messenger Stories
is worse if left in, because Meta accepts the ad and then never delivers to that
placement. Use `instagram_stories` and `facebook_stories` for 9:16 reach instead.

### How `placement_assets` builds the creative (under the hood)

`meta_create_ad` turns your `placement_assets` into a Meta `asset_feed_spec` with
placement `asset_customization_rules`. You never write this by hand, but knowing the
shape helps when you debug a rejected creative:

- The primary `image_hash` / `video_id` becomes the **catch-all fallback**: a rule with
  an empty `customization_spec` that covers every placement you did not map explicitly.
  Always pass a primary (ideally a 1:1 or 4:5 that looks fine almost anywhere).
- Each `placement_assets` entry becomes one rule that targets its `placements`.
- Every asset carries an `adlabels` tag, and its rule points at that label by name, so
  Meta knows which asset belongs to which placement. That linkage is what makes the
  feature work. A creative whose rule references a label that no asset carries is the
  classic cause of a silent "something went wrong" rejection.
- `ad_formats` is `SINGLE_IMAGE` or `SINGLE_VIDEO`. One media type per ad: Meta does not
  allow mixed image and video in a single placement-customized ad.

**Typos fail loud.** An unknown placement name (for example `instragram_stories`) now
raises a clear `Unknown placement` error that lists the valid names, instead of being
dropped silently. Check the placement against the quick-reference table above.

### placement_assets ≠ Dynamic Creative

A frequent mix-up. `placement_assets` builds an `asset_feed_spec` with placement `asset_customization_rules` — but that is **placement customization**, not Dynamic Creative, and it runs on a **standard** ad set. You do not need (and should not turn on) Dynamic Creative to use `placement_assets`.

Dynamic Creative is a different thing: an ad set created with `is_dynamic_creative=true`, where Meta auto-optimizes across multiple text/asset variants (`body_variants`). If you pass `body_variants` to an ad on a *standard* ad set, `meta_create_ad` returns success (even noting it will A/B test) but Meta drops the extra variants — do not trust that note unless the ad set has `is_dynamic_creative=true`. So decide up front: one message shown well per placement → `placement_assets` on a standard ad set; multiple variants for Meta to optimize → a Dynamic Creative ad set. The end-to-end decision lives in `ad-launch-playbook`.

### Recipe 6 — Bulk drop 50+ creatives via Ads Manager (Tier 3)

```
1. Ads Manager → Media Library → drag whole folder → wait for processing
2. Claude: meta_query(account_id, "adimages", limit=250)
3. Claude groups by aspect_ratio_bucket, cross-references filenames via
   the Filename Matching rules, picks per placement, builds ads
   (one meta_create_ad per ad, run sequentially — the server mirrors Meta's
   rate limits; if Meta throttles, the error says so).
```

## Integration Points

**Tools used by this skill:**
- `meta_upload_image` — upload a local image file (base64, ≤4 MB) OR from a public URL, returns `image_hash`
- `meta_create_ad` — build image or video ads with hash or URL; supports `placement_assets` for multi-aspect-ratio bundling (one ad serves different variants per placement via Meta's asset_customization_rules)
- `meta_upload_video` + `meta_get_video_status` — pre-upload video asset pipeline (URL only)
- `meta_query(adimages)` — discover existing image library with `aspect_ratio_bucket` enrichment
- `meta_query(advideos)` — discover existing video library with dimension derivation

**Complementary skills:**
- `ad-launch-playbook` — the end-to-end campaign → ad set → ads runbook; calls this skill for the media step
- `meta-ad-copy-generator` — write the copy first, then use this skill for the media
- `meta-creative-diversification-generator` — plan the creative matrix first, then use this skill per concept
- `meta-video-script-writer` — script the video first, then host the rendered file

**Account integrity reminder:** every `meta_create_ad` call is a write. The server's protection stack mirrors Meta's documented rate model and backs off on Meta's throttle signals — there is **no artificial hourly cap**, so a bulk flow needs no self-imposed pacing. If a call returns a throttle error, back off and resume where you left off.
