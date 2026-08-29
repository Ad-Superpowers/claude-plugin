---
name: meta-ad-launch-playbook
description: "This skill should be used when the user wants to launch a Meta campaign end to end, create a batch of Meta ads, turn a folder of creatives into ads, go \"from creatives to live ads\", \"set up a campaign, ad set and ads\", or \"make ads with a different ratio per placement\". It is the single guided runbook from zero to live ads using the Ad Superpowers MCP write tools (meta_create, meta_create_ad), and it routes to the specialist skills for depth. Do NOT use for: getting a file into Meta / image_hash / hosting (use media-upload-guide), choosing a bid strategy in depth (use bid-strategy-selector), CBO vs ABO theory (use campaign-structure-advisor), writing the copy (use ad-copy-generator), creative testing matrices (use creative-diversification-generator), catalog / DPA strategy (use catalog-optimizer)."
---
# Meta Ad Launch Playbook

The end-to-end runbook for going from "I have some creatives" to live (paused) ads with the Ad Superpowers MCP tools. It owns the **orchestration** — the order of operations and the decisions that trip people up — and hands the deep mechanics to the specialist skills. Follow it top to bottom.

## The journey at a glance

```
[0] Page & Instagram        → confirm the client profile resolves a Page (+ IG)
        │
[1] Campaign                → meta_create(entity_type="campaign")     (budget → CBO)
        │
[2] Ad set                  → meta_create(entity_type="adset")        (+ creative-mode decision)
        │
[3] Creatives → ads         → meta_create_ad(...) per ad              (sequential batch)
        │
[4] Verify                  → meta_query / meta_get_creatives
```

Everything is created **PAUSED** by default. Nothing spends until you flip it to ACTIVE in review.

## §0 Before you start: Page & Instagram

Every ad needs a Facebook Page, and Instagram placements need an Instagram account. You usually do **not** pass these by hand — `meta_create_ad` resolves them from the client profile:

- **Auto-resolution.** If the client has a `facebook_page_id` (and optionally `instagram_user_id`) stored, `meta_create_ad` uses them. You only pass `page_id` / `instagram_user_id` to override.
- **Set them once** with `clients_update` if they are missing, so every future ad just works.
- **Facebook-only ads.** Pass `facebook_only=true` to deliberately skip Instagram (page-only creative). Do not also pass an Instagram id — that conflicts.
- **Error `1815199`** ("ad account has no access to this Instagram account") means the stored IG account is not linked to this ad account. Fix the link in Business settings or correct `instagram_user_id`; this is surfaced as a real error now rather than a silent page-only fallback.

Discover what is available:

```python
meta_query(account_id="act_...", entity_type="promotepages")   # Pages this account can advertise
```

## §1 Create the campaign

```python
meta_create(
    account_id="act_...",
    entity_type="campaign",
    name="Spring Launch",
    objective="OUTCOME_TRAFFIC",      # or OUTCOME_SALES / _LEADS / _ENGAGEMENT / _AWARENESS / _APP_PROMOTION
    daily_budget=2000,                # cents (€20.00/day). A budget is REQUIRED — pass daily_budget OR lifetime_budget.
    status="PAUSED",
)
```

Two things to internalize:

- **A campaign budget is required, which means every campaign is CBO** (Campaign Budget Optimization). The budget lives on the campaign and the ad sets share it. (ABO / per-ad-set budgets are not creatable through the tool yet.)
- **`bid_strategy` defaults to `LOWEST_COST_WITHOUT_CAP`.** You normally omit it. This is also why your ad sets do **not** need a `bid_amount` (see §2). Only set a different strategy if you have a real reason:
  - `LOWEST_COST_WITH_BID_CAP` or `COST_CAP` → require a `bid_amount` (set on the ad set).
  - `LOWEST_COST_WITH_MIN_ROAS` → needs a minimum-ROAS target that `meta_create` cannot set today, so this strategy is not configurable through the tool yet (set it in Ads Manager).
  - For the "which strategy and what number" decision, `use bid-strategy-selector`. For CBO vs ABO and budget-split theory, `use campaign-structure-advisor`.

## §2 Create the ad set

```python
meta_create(
    account_id="act_...",
    entity_type="adset",
    campaign_id="<from step 1>",
    name="NL · 25-45 · interests",
    targeting={"geo_locations": {"countries": ["NL"]}, "age_min": 25, "age_max": 45},
    optimization_goal="LINK_CLICKS",   # must fit the campaign objective
    status="PAUSED",
)
```

- **No budget here.** Under CBO the ad set inherits the campaign budget; passing one is rejected.
- **No `bid_amount` needed** with the default `LOWEST_COST_WITHOUT_CAP`. Only supply `bid_amount` if you deliberately chose a cap strategy in §1.
- `advantage_audience` defaults sensibly; some objectives require it (the tool tells you if so).

### The creative-mode decision (do this before §3)

This is the choice that quietly breaks launches. Pick one:

| You want… | Ad set setup | How you build the ad in §3 |
|-----------|--------------|----------------------------|
| **One creative concept, the right ratio per placement** (the common case) | **Standard ad set** (leave `is_dynamic_creative` off) | `placement_assets` on `meta_create_ad` |
| **Meta to auto-optimize across multiple text/creative variants** | **Dynamic Creative ad set**: `meta_create(entity_type="adset", ..., is_dynamic_creative=true)` | `body_variants` (and/or asset combos) on `meta_create_ad` |

Two things people get wrong:

- **`placement_assets` is NOT Dynamic Creative.** It builds an `asset_feed_spec` with placement `asset_customization_rules`, but that is just placement customization and runs on a **standard** ad set. Using `placement_assets` does not require — and should not be confused with — Dynamic Creative.
- **`body_variants` requires a Dynamic Creative ad set.** Today, if you pass `body_variants` to an ad on a standard ad set, `meta_create_ad` returns success — and even appends a note like "Meta will A/B test these variants" — but Meta drops the extra variants. **Do not trust that note unless the ad set was created with `is_dynamic_creative=true`.** So decide here: if you want multiple text variants, create the ad set with `is_dynamic_creative=true`; if you just want one message shown well across placements, stay standard and use `placement_assets`.

## §3 Creatives → ads

This is where the playbook earns its keep: **orchestration**. The file-handling mechanics (how to upload, URL vs hash, filename→ratio matching, the full placement list) live in `media-upload-guide` — `use media-upload-guide` for those and do not re-derive them here.

### Group, then build

```
1. Group your creatives by CONCEPT (a concept = one message/offer, in its various ratios).
2. One ad per concept.
3. Within a concept, bundle the aspect ratios via placement_assets (one ad serves the
   right ratio per placement, and keeps a single engagement post across placements).
4. Split into separate ads when:
     - the copy differs per ratio (placement_assets shares one body/headline), or
     - you are mixing image and video (Meta rejects mixed media in one ad), or
     - it is a genuinely different creative concept (that is a new ad).
```

A single concept with multiple ratios → one ad:

```python
meta_create_ad(
    account_id="act_...",
    adset_id="<from step 2>",
    headline="Spring launch",
    body="One message, shown well everywhere.",
    link_url="https://example.com",
    image_hash="<1x1 hash>",          # primary / catch-all fallback (1:1 is safe anywhere)
    placement_assets=[
        {"image_hash": "<9x16 hash>",
         "placements": ["instagram_stories", "facebook_stories", "instagram_reels"]},
        {"image_hash": "<4x5 hash>",
         "placements": ["instagram_feed", "facebook_feed"]},
    ],
    status="PAUSED",
)
```

Other creative types, same `meta_create_ad` call:
- **Single image / single video** — pass one of `image_url` / `image_hash` / `video_url` / `video_id` (exactly one).
- **Carousel** — pass `slides=[{image_hash, name, link}, ...]` (2–10 cards).
- **Per-placement carousel variants** — `placement_assets` entries of the shape `{slides, placements}`.

### Batch writes (no self-pacing needed)

There is **no bulk-create tool** — a batch is several `meta_create_ad` calls. You do not need to pace them yourself:

- The server mirrors Meta's documented rate model (writes are score-weighted, and **uploads count as writes**) and has an error-613 circuit breaker plus backoff on Meta's own usage headers. There is **no artificial per-hour write cap** — sequential writes in a normal drop need no self-pacing.
- Run the calls **sequentially** rather than as an unbounded parallel fan-out: sequential calls give clean per-ad results and let the server react to Meta's signals between calls.
- If a write is throttled, the error says so — back off, then resume where you left off; wait guidance is included where Meta provides it.
- If one ad in a batch hits a **Meta API** error, the others still succeed — that call returns a structured error result rather than aborting the run, so you can retry just the failures. Bad **inputs** are different: invalid media combinations, missing placements, a malformed carousel, or a `facebook_only` + Instagram conflict raise a validation error before the API call, so check each call's inputs before firing the batch.

## §4 Verify + honest limits

Read back what you created:

```python
meta_query(account_id="act_...", entity_type="ads", fields=["id","name","status","adset_id"])
# inspect the creative copy + placements (creative_id comes from the meta_create_ad response)
meta_get_creatives(account_id="act_...", scope="single", creative_id="<creative_id>")
```

Common stumbles and the fix:
- "Bid amount required" on the ad set → you (or an inherited strategy) chose a cap strategy without a `bid_amount`. With the default `LOWEST_COST_WITHOUT_CAP` this should not happen; if it does, omit the strategy or supply `bid_amount`.
- Instagram error `1815199` → see §0.
- `body_variants` "did nothing" → the ad set was standard, not Dynamic Creative (see §2).
- Mixed image + video rejected → split into separate ads.

**Honest limits (today):**
- **Catalog / Advantage+ catalog ads** cannot be created through MCP: this release ships no catalog tool, so catalog data is not reachable either. Build catalog ads in Ads Manager; `use catalog-optimizer` for the strategy.
- **No bulk-create tool** — batch = sequential `meta_create_ad` calls (see §3).

## Complementary skills

- `use media-upload-guide` — get files into Meta (URL vs hash, hosting, filename→ratio, the full placement list).
- `use bid-strategy-selector` — pick the bid strategy and the number when you override the default.
- `use campaign-structure-advisor` — CBO vs ABO, budget splits, account structure.
- `use ad-copy-generator` / `use video-script-writer` — produce the copy/script before you build.
- `use creative-diversification-generator` — plan the creative matrix (concepts × angles) feeding §3.
- `use catalog-optimizer` — catalog / DPA strategy (creation is Ads-Manager-only for now).

## Account integrity reminder

Every `meta_create_ad` and every upload is a write. The server's protection stack mirrors Meta's own rate model and backs off on Meta's throttle signals — there is **no artificial hourly cap**, so a normal batch needs no self-pacing. If a write is throttled, the error says so; back off and resume. Everything ships PAUSED so you can review before any spend.
