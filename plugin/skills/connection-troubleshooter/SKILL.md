---
name: connection-troubleshooter
description: "This skill should be used when a user says the Ad Superpowers connector looks broken or half-empty: \"I only see a few tools\", \"my platform tools are missing\", \"the connector isn't working\", \"I connected my account but nothing shows up\", \"where are my Google Ads / Meta / GA4 tools\", \"a tool is not callable / not available\", or asks how to \"reconnect\" a platform. It explains that a short tool list almost always means a connection needs (re)connecting \u2014 not that the platform is broken \u2014 and walks through the exact fix (reconnect the affected platform on the dashboard, then start a fresh chat). It covers the Google specifics: Ads, Analytics, Search Console and Tag Manager are connected individually, so each can go missing on its own and each may need its own reconnect. Do NOT use for: diagnosing campaign/ad performance (use the per-platform performance-troubleshooter skills), billing/subscription questions, or building/onboarding client profiles (use client-context-onboarding)."
allowed-tools: skill, workflow, clients, clients_update
---

# Connection Troubleshooter

## Purpose

Help a user who suddenly sees only a handful of Ad Superpowers tools (typically
just `workflow`, `skill`, and `clients`, sometimes with `clients_update`)
understand what happened and fix it. In almost every case a short tool list
means **a platform connection needs (re)connecting** — the dashboard may still
say "connected", but the underlying login (the OAuth grant) has expired or been
revoked, so the server can no longer fetch that platform's data and hides its
tools rather than show broken ones. Nothing is "broken" and no data was lost;
the connection just needs to be refreshed.

## When to Use This Skill

Use this skill when the user reports any of:

- "I only see a few tools" / "most of my tools are gone" / "my platform tools are missing".
- "Where are my Google Ads / GA4 / Search Console / Tag Manager tools?" or
  "Where are my Meta / LinkedIn / TikTok tools?"
- "The connector isn't working" / "I connected my account but nothing shows up".
- "A tool is not callable" or "that tool isn't available."
- "How do I reconnect <platform>?"

Do **not** use it for campaign performance problems, billing questions, or
client onboarding — see the "Do NOT use for" note in the description.

## Why this happens (plain-language)

Ad Superpowers only shows a platform's tools when it can actually reach that
platform on your behalf. To do that it uses the login you granted when you
connected the account (an OAuth "grant"). Access to a platform is short-lived
and is refreshed automatically in the background — but if that grant was
**revoked or expired** (you changed your password, removed the app's access,
the refresh token aged out, an admin rotated permissions, etc.), the automatic
refresh fails. When the server can't get a working connection for a platform, it
**hides that platform's tools** instead of surfacing tools that would only
error. That is why the dashboard can still list the account as "connected" while
its tools have quietly disappeared from this chat.

A small set of universal tools never depends on any platform connection, so they
stay visible even when every platform tool is hidden: `workflow`, `skill`, and
`clients` for everyone, plus `clients_update` on write-enabled plans. Seeing only
these — and none of your platform tools — is the classic signature of a dead
connection.

## Figure out which platform to reconnect (works in any client)

You do not need any special access to diagnose this — **infer the missing
platform from the tools you can see right now:**

- No `google_ads_*` tools → **Google Ads** needs reconnecting.
- No `ga4_*` tools → **Google Analytics (GA4)**.
- No `gsc_*` tools → **Google Search Console**.
- No `gtm_*` tools → **Google Tag Manager**.
- No `meta_*` tools → **Meta** (Facebook/Instagram).
- No `linkedin_*` tools → **LinkedIn**.
- No `tiktok_*` tools → **TikTok**.

**Google is four separate connections.** Ads, Analytics, Search Console, and Tag
Manager are each connected **individually** on the dashboard, so any one of them
can go missing on its own — and each may need its own reconnect. They do share a
single Google sign-in, so reconnecting one Google service often brings the
others back at the same time, but that is not guaranteed once a login has been
revoked. The reliable rule: **reconnect every Google service whose tools are
missing.**

If several tool groups are missing, more than one connection needs attention. If
**every** platform group is missing, start with whichever platform the user
cares about most.

## The fix (step by step)

1. Go to the dashboard: **`https://app.adsuperpowers.ai/dashboard/integrations`**
   (the Integrations / Connected Accounts page).
2. For each platform that's missing its tools, click **Reconnect** (or
   **Connect**). For Google, do this for **each** Google service you use whose
   tools are gone — Google Ads, Analytics, Search Console, and Tag Manager are
   listed and reconnected separately.
3. Complete the login/consent in the browser.
4. **Start a fresh chat** in your MCP client (Claude, ChatGPT, Cursor, …). The
   tool list is negotiated once when a session connects, so the reconnected
   tools only reappear in a **new** conversation — refreshing the current chat is
   not enough.
5. Confirm the platform's tools are back (e.g. `google_ads_*` for Google Ads). If
   any expected Google tools are still missing, go back to step 2 and reconnect
   that specific Google service too.

## If it still doesn't work

- Double-check you reconnected the right platform on the dashboard and that the
  connection shows active and selected there. For Google, confirm each service
  you expected (Ads / Analytics / Search Console / Tag Manager) is reconnected.
- Make sure you truly started a **new** chat/session after reconnecting, not the
  same one.
- If the tools still don't appear in a fresh chat, the account may not be
  selected for use, or the connection may belong to a different organization
  than the one your API key resolves to. Contact Ad Superpowers support with the
  platform name and the account you expected to see.

## Key facts to remember

- A short tool list ≈ **(re)connect needed**, not "the platform is broken."
- **Google is four separate connections** (Ads, Analytics, Search Console, Tag
  Manager). Reconnect **each** Google service whose tools are missing —
  reconnecting one often restores the others (shared sign-in), but it is not
  guaranteed after a revoked login.
- **Always start a fresh chat** after reconnecting — the tool list only
  re-handshakes on a new session.
- A few universal tools (`workflow`, `skill`, `clients`, and `clients_update` on
  write-enabled plans) stay visible even when platform tools are hidden; only
  *platform* tools disappear when a connection dies.
