# attention_points subtemplate + worked example

`attention_points` is the lean profile's catch-all digest (max 5000 characters).
Use the fixed headings below every time so rich research compresses consistently.
Skip a heading when there is nothing to say. Aim for ~3000 characters total; if you
approach 5000, shorten rather than let the write fail. Never include end-customer
personal data.

## The fixed headings

```
## Positioning        (<= 400 chars: what the company is and how it stands out)
## Audience           (<= 600: 1 to 3 primary personas or segments, tight)
## Competitors        (<= 500: top 3 to 5, one differentiator each)
## Brand voice        (<= 300: tone cues, dos and don'ts)
## KPI targets        (<= 400: ROAS / CPA / CPL / MER goals plus horizon)
## Season & timing    (<= 300: peaks, troughs, campaign moments)
## Constraints        (<= 500: no-go's, compliance, brand limits, budget caps)
```

## Worked example (fictional client, no PII)

A complete draft for a fictional D2C coffee brand, "Bean Theory". This is the shape a
`clients_update(action="create", status="draft", ...)` call should produce.

**name:** `Bean Theory`
**status:** `draft`
**budget_total:** `12000`
**currency:** `EUR`
**overall_goal:** `Grow online subscription revenue 40% YoY at a blended ROAS of 3.5 while holding CAC under EUR 35.`

**channels:** (each may carry multiple structured `targets` — `{metric, value,
action_type?}` — plus a `primary_metric` the reports headline; ROAS is a multiplier,
counts are monthly, use a period decimal)

| platform | budget | goal | targets | primary_metric |
|----------|--------|------|---------|----------------|
| `meta` | 6000 | Prospecting plus retargeting for subscription sign-ups | `cpa` 35 (`purchase`) + `roas` 3.5 | `cpa` |
| `google_ads` | 4000 | Brand defense plus shopping for one-off bag sales | `roas` 4.0 + `conversions` 120 | `roas` |
| `tiktok` | 2000 | Top-of-funnel reach with UGC creative | (none) | (none) |

**linked_accounts:**

| platform | account_id | account_name |
|----------|-----------|--------------|
| `meta` | `act_4455667788` | Bean Theory Main |
| `google_ads` | `135-246-3579` | Bean Theory EU |
| `google_analytics` | `properties/445566778` | Bean Theory GA4 |
| `tiktok` | `7012345678` | Bean Theory NL |

**attention_points:**

```
## Positioning
Specialty single-origin coffee sold direct via subscription. Premium but
approachable; competes on freshness (roast-to-ship in 48h) and provenance, not price.

## Audience
1) Home espresso enthusiasts, 28 to 45, urban, value origin stories and gear.
2) Gifting buyers around Q4 who convert on bundles. Lower repeat rate.

## Competitors
- BigRoast: scale and price; weak on freshness story.
- LocalBrew: strong brand love, narrow distribution.
- Supermarket private label: price anchor we must out-position on quality.

## Brand voice
Warm, knowledgeable, a little playful. No hype, no superlatives. Plain language.

## KPI targets
Blended ROAS 3.5, CAC < EUR 35, subscription share of revenue > 60% by year end.

## Season & timing
Strong Q4 gifting peak (Nov to Dec). Summer dip in hot espresso; push cold brew.

## Constraints
No health or medical claims about caffeine. Keep discounting off brand terms.
Monthly budget cap EUR 12k; do not exceed without sign-off.
```

## Notes

- Keep `overall_goal` to one sentence. Detail belongs in `attention_points`.
- Channel `goal` is a short per-platform intent (<= 500 chars), not a full brief.
- `linked_accounts` is the durable join: it is what lets
  `clients(action="get", account_id=...)` resolve an account back to this client.
