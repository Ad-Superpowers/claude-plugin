---
name: meta-page-instagram-connector
description: |
  This skill should be used when the user wants to set up a client's Facebook Page and Instagram
  for ads, connect Meta Page and Instagram to a client, wire a client's Meta Page and IG, decide
  which Facebook Page a client's ads post from, or fix a client's Instagram-access (error 1815199)
  problem. It discovers the promotable Pages and connected Instagram accounts for the client's Meta
  ad account and saves the chosen identities onto the client profile, so meta_create_ad resolves them
  automatically on every ad. Do NOT use for: building the ad itself (use ad-launch-playbook), general
  client import/grouping (use client-context-onboarding), or bid strategy (use bid-strategy-selector).
---
# Meta Page & Instagram Connector

Wire a client's **Facebook Page** and **Instagram account** onto their profile so their Meta ads post from the right Page and run on the right Instagram identity. Once set, `meta_create_ad` resolves these automatically — you never pass `page_id` / `instagram_user_id` per ad. Because you pick the Instagram account from the ones the ad account is actually linked to, this heads off most `1815199` ("no access to this Instagram account") failures — though a wrong or later-revoked IG can still surface at ad-creation time.

This skill orchestrates existing tools (`meta_wire_pages`, `clients`, `meta_query`, `clients_update`); it changes nothing until you save.

## Fast path (recommended): `meta_wire_pages`

For most clients there is exactly one promotable Page and one connected Instagram account per ad account — `meta_wire_pages` discovers and (optionally) wires them in one call:

```python
# 1. Preview — discovers Pages + IG per Meta-linked account, proposes the
#    unambiguous + currently-missing ids. Writes nothing.
meta_wire_pages(client="acme-corp")

# 2. Apply — persists the unambiguous proposals onto the client profile.
meta_wire_pages(client="acme-corp", apply=True)
```

Each result row reports `proposed_facebook_page_id` / `proposed_instagram_user_id` (the auto-wire candidates), plus `page_choices` / `ig_choices` and a `status`:
- `would_wire` / `wired` — a single Page and/or IG was the obvious choice.
- `needs_manual_choice` — 0 or >1 options; fall back to the manual flow below to pick.
- `already_wired` — both ids already set (nothing to do).

Use the manual flow below when `status` is `needs_manual_choice`, for **Facebook-only** clients (no Instagram), or to override an auto-wired choice.

## When to use

- Right after a client is created/imported (`use client-context-onboarding` for that import step), to complete the Meta wiring.
- Any time a client's ads post from the wrong Page, or Instagram placements fail with `1815199`.

## The flow

### 1. Find the client and its Meta account

```python
clients(action="get", client="acme-corp")     # by slug/UUID
# or, if you only know the ad account:
clients(action="get", account_id="act_1234567890")
```

Prefer identifying the client by slug/UUID (`client=`). If you only have the ad account, run `clients(action="list")` first and check how many clients carry that `account_id` in their `linked_accounts`: if more than one, confirm with the user which client this is for before saving — do not let a `get`-by-`account_id` silently pick one. Then read the chosen client's `linked_accounts` for the `platform == "meta"` entries — each has `account_id`, and (once set) `facebook_page_id` / `instagram_user_id`.

### 2. Discover the Pages and Instagram accounts

```python
meta_query(account_id="act_1234567890", entity_type="promotepages")
# Pages this account can advertise: each item has an id + name.

meta_query(account_id="act_1234567890", entity_type="connected_instagram_accounts")
# Instagram accounts linked to the page/account: id + username (+ follower_count, etc).
```

### 3. Let the user choose

Show the Pages by **name** (not just id) and the Instagram accounts by **username**, and ask which to use. Offer **Facebook-only** as an explicit option when the client does not run Instagram placements.

### 4. Save the choice onto the client

```python
clients_update(
    action="update",
    client="acme-corp",
    linked_accounts=[
        {
            "platform": "meta",
            "account_id": "act_1234567890",
            "facebook_page_id": "1074464832418530",
            "instagram_user_id": "17841423948601304",
        }
    ],
)
```

- `linked_accounts` is patch-merged on `(platform, account_id)`, so this updates just that account; other linked accounts and fields are untouched.
- **Facebook-only:** set `facebook_page_id` and pass `"instagram_user_id": null` to clear any stored IG.
- Both IDs are numeric strings (pattern `^\d+$`) — use the exact ids returned by `meta_query`, not the Page name or IG username.

### 5. Verify

```python
clients(action="get", client="acme-corp")   # confirm facebook_page_id / instagram_user_id are set
```

From now on, `meta_create_ad` for this client resolves the Page/IG automatically. To launch, `use ad-launch-playbook`.

## Edge cases

- **No promotable Pages** (`promotepages` empty): the ad account has no Page access. Grant the account access to the Page in Meta Business settings, then retry.
- **No connected Instagram / error `1815199`**: the Page has no linked Instagram, or the ad account cannot access it. Either run **Facebook-only** (Page set, `instagram_user_id` null), or link the Instagram account in Business settings and retry. Do not store an IG id the account cannot access — that is exactly what produces `1815199` at ad-creation time.
- **More than one client on the same ad account:** disambiguate with the user before saving; never silently pick a client.
- **Picked the wrong one:** rerun step 4 with the corrected id (patch-merge overwrites it).

## Tools used

- `clients(action="get")` — read the client profile + its Meta `linked_accounts`.
- `meta_query(entity_type="promotepages")` — discover promotable Pages (id + name).
- `meta_query(entity_type="connected_instagram_accounts")` — discover linked Instagram accounts (id + username).
- `clients_update(action="update")` — persist `facebook_page_id` / `instagram_user_id` on the linked account.

## Complementary skills

- `use client-context-onboarding` — import and group connected ad accounts into client profiles (run this first; this skill completes the Meta wiring).
- `use ad-launch-playbook` — once the Page/IG are wired, build and launch the ads.
