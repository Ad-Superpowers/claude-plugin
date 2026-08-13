---
name: gtm-server-side-tagging-guide
description: "This skill should be used when the user asks to \"set up server-side GTM\", \"implement Meta CAPI via sGTM\", \"migrate from client-side to server-side tagging\", \"estimate sGTM hosting costs\", or mentions \"server-side tagging\", \"sGTM\", or \"first-party data strategy\". Do NOT use for: client-side GTM tag setup (use gtm-conversion-setup-guide), strategic tracking planning (use tracking-plan-builder), or consent mode implementation (use gtm-consent-mode-guide)."
---

# Server-Side GTM Guide

Server-side Google Tag Manager (sGTM) moves tag execution from the visitor's browser to a server you control. Instead of loading multiple third-party scripts on the client, your browser sends a single request to your server, which then fans out events to GA4, Meta, Google Ads, LinkedIn, TikTok, and any other destination. This improves page speed, data quality, privacy compliance, and resilience against ad blockers.

## When to Use sGTM: Decision Framework

sGTM is not free and not simple. Use this decision tree to determine whether it is right for your situation.

### sGTM Decision Tree

```
Is accurate conversion tracking critical to your business?
|
+-- No ---> Stay client-side. sGTM adds cost and complexity you don't need.
|
+-- Yes
    |
    Are ad blockers or ITP (Safari) causing >15% data loss?
    |
    +-- No
    |   |
    |   Do you need Google Enhanced Conversions or LinkedIn CAPI?
    |   (Note: Meta CAPI is now mandatory — implement via sGTM or backend code)
    |   |
    |   +-- No ---> Stay client-side. sGTM won't add enough value.
    |   +-- Yes --> Consider sGTM. Server-side is the cleanest way to implement these.
    |
    +-- Yes
        |
        Is your monthly ad spend >EUR 5,000?
        |
        +-- No ---> The cost of sGTM may exceed the value recovered. Start with
        |           Enhanced Conversions client-side as a cheaper alternative.
        |
        +-- Yes --> sGTM is strongly recommended. The data quality improvement
                    will pay for itself in better optimization.
```

### Benefits vs. Costs

| Benefit | Impact | Who Benefits Most |
|---|---|---|
| First-party cookie control | Extends cookie lifetime from 7 days (ITP) to up to 400 days | Safari-heavy audiences (EU, mobile) |
| Ad blocker bypass | Recovers 15-30% of lost events | Sites with tech-savvy audiences |
| Faster page loads | Removes 3-8 third-party scripts from browser | All sites, especially mobile |
| Data enrichment | Add server-side data (CRM, margin, LTV) to events | E-commerce, SaaS |
| Single point of control | All vendor tags managed server-side | Multi-platform advertisers |
| Privacy compliance | PII never leaves your server | EU businesses under GDPR |
| Meta CAPI quality score | Score 7+ with redundant setup | All Meta advertisers (CAPI is now mandatory for signal quality) |

| Cost | Estimate |
|---|---|
| Hosting | EUR 30-500/month depending on traffic |
| Setup time | 20-80 hours (depends on complexity) |
| Maintenance | 2-5 hours/month |
| Debugging complexity | Higher than client-side |
| Team knowledge | Requires someone who understands HTTP, cookies, server infra |

## Architecture Overview

### Client-Side Only (Before)

```
Browser                  Third-party servers
  |
  +---> gtm.js ---------> GA4 (analytics.google.com)
  +---> fbevents.js -----> Meta (connect.facebook.net)
  +---> ads.js ----------> Google Ads (googleads.g.doubleclick.net)
  +---> insight.js ------> LinkedIn (snap.licdn.com)
  +---> pixel.js --------> TikTok (analytics.tiktok.com)

5 third-party scripts, 5 network connections, 5 points of failure
```

### Hybrid (Client + Server, Recommended)

```
Browser                   Your Server (sGTM)          Platforms
  |                           |
  +---> gtm.js               |
  |     (client container)    |
  |     |                     |
  |     +-- GA4 Config -------> First-party endpoint
  |     |   (transport_url)    |
  |     |                      +--> GA4 (Measurement Protocol)
  |     +-- dataLayer events   +--> Meta (Conversions API)
  |         via HTTP POST ---->+--> Google Ads (Enhanced Conv.)
  |                            +--> LinkedIn (CAPI)
  |                            +--> TikTok (Events API)
  |
  +---> fbevents.js (optional, for dedup + fallback)

1 first-party request + optional client pixels for redundancy
```

### Full Server-Side (Advanced)

```
Browser                   Your Server (sGTM)          Platforms
  |                           |
  +-- Single HTTP request --> |
      (custom fetch/beacon)   +--> GA4
                              +--> Meta CAPI
                              +--> Google Ads
                              +--> LinkedIn CAPI
                              +--> TikTok Events API

No third-party scripts at all. Maximum speed and control.
Requires custom client-side code (no GTM client container).
```

## Hosting Options

### Option 1: Google Cloud Run (Official)

Google's recommended hosting. The sGTM container runs as a Cloud Run service.

| Aspect | Detail |
|---|---|
| Setup | GTM UI > Admin > Install Tag Manager > Server-side > Auto-provision |
| Scaling | Auto-scales 0 to N instances based on traffic |
| Region | Choose EU (europe-west1) for GDPR compliance |
| Min instances | Set to 1-3 for production (avoids cold starts) |
| CPU allocation | "CPU is always allocated" for consistent performance |

**Cost Estimation (Google Cloud Run):**

| Monthly Events | Estimated Cost (EUR) | Notes |
|---|---|---|
| 100,000 | 15-30 | 1 min instance, low CPU |
| 500,000 | 40-80 | 2 min instances |
| 1,000,000 | 70-150 | 3 min instances |
| 5,000,000 | 200-400 | 5-8 min instances |
| 10,000,000 | 350-700 | 8-15 min instances |
| 50,000,000+ | 700-2,000 | Auto-scaling, consider reserved instances |

**Setup Steps:**

1. Create a Google Cloud project (or use existing)
2. Enable billing on the project
3. In GTM, create a Server container
4. Choose "Automatically provision tagging server"
5. Select Cloud Run region (pick EU for EU businesses)
6. GTM creates the Cloud Run service automatically
7. Set min instances to at least 1 in Cloud Run console
8. Configure custom domain (see Custom Domain section below)

### Option 2: Stape.io (Managed)

Easiest option. Stape manages the infrastructure.

| Aspect | Detail |
|---|---|
| Setup | 10 minutes, no cloud console needed |
| Pricing | From EUR 20/month (500k events) to EUR 200+/month |
| Features | Custom domain, auto-SSL, EU hosting, preview mode support |
| Best for | Teams without DevOps/cloud infrastructure expertise |

**Stape Pricing (as of 2026):**

| Plan | Monthly Events | Price (EUR) |
|---|---|---|
| Starter | 500,000 | ~20 |
| Business | 2,000,000 | ~50 |
| Pro | 10,000,000 | ~150 |
| Enterprise | Custom | Custom |

### Option 3: AWS / Other Cloud

For teams already on AWS or Azure. Run the sGTM Docker image on ECS, Fargate, or App Service.

| Aspect | Detail |
|---|---|
| Docker image | `gcr.io/cloud-tagging-10302018/gtm-cloud-image:stable` |
| Required env vars | `CONTAINER_CONFIG` (from GTM UI), `PORT` (default 8080) |
| Load balancer | Required (ALB on AWS, App Gateway on Azure) |
| Auto-scaling | Configure based on CPU/request count |
| Estimated cost | Similar to GCR, depends on instance type |

### Hosting Comparison

| Factor | Google Cloud Run | Stape.io | AWS/Azure |
|---|---|---|---|
| Setup time | 30-60 min | 10 min | 2-4 hours |
| Technical skill | Medium | Low | High |
| Cost control | Full | Limited | Full |
| EU hosting | Yes | Yes | Yes |
| Custom domain | Manual | Built-in | Manual |
| Preview server | Separate instance | Built-in | Separate instance |
| Vendor lock-in | Low (Docker image) | Medium | Low |

## Custom Domain Setup (Critical)

Without a custom domain, your sGTM server uses a Google Cloud URL. This means requests are still "third-party" and gain no cookie benefit. A custom domain makes your server first-party.

### Steps

1. **Choose a subdomain:** `sgtm.yourdomain.com` or `data.yourdomain.com`
2. **Create DNS record:** CNAME pointing to your Cloud Run service URL
3. **Configure SSL:** Automatic via Cloud Run, or via Stape
4. **Update GTM client container:** Set `transport_url` in Google Tag to `https://sgtm.yourdomain.com`
5. **Set cookie domain:** Configure the GA4 client in sGTM to set cookies on `.yourdomain.com`

### DNS Record Example

```
Type: CNAME
Name: sgtm
Value: your-service-abc123-ew.a.run.app
TTL: 300
```

### First-Party Cookie Configuration

In the sGTM container, the GA4 client automatically sets a `_ga`-equivalent cookie. Because the request goes to your subdomain, the cookie is first-party and not subject to ITP 7-day expiry.

| Cookie | Domain | Lifetime | Purpose |
|---|---|---|---|
| `_ga` (server-set) | `.yourdomain.com` | Up to 400 days | GA client ID |
| `_ga_XXXXX` | `.yourdomain.com` | Up to 400 days | GA session data |
| `FPID` | `.yourdomain.com` | Up to 400 days | First-party ID for sGTM |

## Migration: Client-Side to Server-Side

Do not rip out client-side tags and go full server-side in one step. Use a phased approach.

### Phase 1: Parallel (Week 1-2)

Run both client-side and server-side simultaneously. Compare event counts.

```
Client GTM Container:
  - GA4 Config tag: add transport_url = https://sgtm.yourdomain.com
  - All other tags: keep as-is (still fire client-side)

Server GTM Container:
  - GA4 Client: receives forwarded GA4 hits
  - GA4 Tag: sends to GA4 property (same as client-side)

Result: GA4 receives events from BOTH client and server.
Use GA4 DebugView to confirm both paths work.
Deduplicate via measurement_protocol_secret or disable client direct sends.
```

### Phase 2: Add Server-Side Destinations (Week 2-4)

Add Meta CAPI, Google Ads Enhanced Conversions, etc. as server-side tags.

```
Server GTM Container:
  - GA4 Client (receiving from client)
  - GA4 Tag (forwarding to GA4)
  - Meta CAPI Tag (NEW - sending to Meta server-side)
  - Google Ads Enhanced Conversions Tag (NEW)
  - LinkedIn CAPI Tag (NEW, if supported)

Client GTM Container:
  - Keep Meta Pixel (redundant, for dedup)
  - Keep LinkedIn Insight Tag (redundant, for dedup)
```

### Phase 3: Reduce Client-Side (Week 4-8)

Once server-side events are confirmed working and deduplicated, remove redundant client-side tags.

```
Client GTM Container:
  - GA4 Config (with transport_url pointing to sGTM)
  - Meta Pixel base code (for dedup event_id matching only)
  - Remove: standalone Meta event tags
  - Remove: LinkedIn Insight Tag (if CAPI covers it)
  - Remove: TikTok Pixel (if Events API covers it)

Server GTM Container:
  - Handles all conversion forwarding
```

### Phase 4: Optimize (Month 2+)

- Add data enrichment (CRM data, margin, LTV)
- Implement consent-aware server-side processing
- Remove remaining unnecessary client-side scripts
- Monitor and tune server costs

## Server-Side Clients (Receiving Data)

Clients in sGTM receive incoming HTTP requests and parse them into an event data object that tags can use.

### GA4 Client (Built-In)

| Setting | Recommended Value |
|---|---|
| Priority | Default |
| GA4 Measurement ID Allowlist | Add your `G-XXXXXXXXXX` IDs |
| Default GA4 paths | `/g/collect`, `/j/collect` |
| Set cookie on | `.yourdomain.com` |
| FPID cookie lifetime | 400 days |
| JavaScript managed | Not required (auto) |

The GA4 client intercepts requests from the client-side Google Tag (when `transport_url` points to your sGTM server) and creates an event data object.

### Custom Client (Webhook)

For receiving events from your backend (not browser-initiated):

```javascript
// Custom client template
const claimRequest = require('claimRequest');
const getRequestBody = require('getRequestBody');
const getRequestHeader = require('getRequestHeader');
const JSON = require('JSON');
const runContainer = require('runContainer');

// Only claim POST requests to /webhook
if (getRequestHeader('method') === 'POST' && 
    getRequestPath().indexOf('/webhook') === 0) {
  
  claimRequest();
  
  const body = JSON.parse(getRequestBody());
  
  const eventData = {
    event_name: body.event,
    // Map your webhook fields to event data
  };
  
  runContainer(eventData, () => {
    // Response after all tags fire
  });
}
```

## Server-Side Tags (Sending Data)

### Meta Conversions API Tag

The official Meta CAPI tag template is available in the sGTM Community Template Gallery.

| Setting | Value |
|---|---|
| Tag Template | Facebook Conversions API (Community) |
| API Access Token | Your Meta CAPI token (from Events Manager) |
| Pixel ID | Your Meta Pixel ID |
| Action Source | `website` |
| Event Name | Map from event_data (e.g., `Purchase`) |
| Event ID | Must match client-side `eventID` for dedup |

**Required User Data (for matching):**

| Field | Source | Hashing |
|---|---|---|
| Email | `event_data.user_data.email_address` | Auto-hashed (SHA256) |
| Phone | `event_data.user_data.phone_number` | Auto-hashed |
| First Name | `event_data.user_data.address.first_name` | Auto-hashed |
| Last Name | `event_data.user_data.address.last_name` | Auto-hashed |
| City | `event_data.user_data.address.city` | Auto-hashed |
| Country | `event_data.user_data.address.country` | Plain |
| IP Address | `event_data.ip_override` | Plain (auto-populated) |
| User Agent | `event_data.user_agent` | Plain (auto-populated) |
| FBC | `event_data.fbc` | Plain (from `_fbc` cookie) |
| FBP | `event_data.fbp` | Plain (from `_fbp` cookie) |

**Deduplication:**

Meta deduplicates events by matching `event_name` + `event_id`. The `event_id` sent from the client-side Pixel must match the `event_id` sent from the server-side CAPI tag.

In your client-side GTM:
```javascript
// Generate event_id and push to dataLayer
var eventId = 'evt_' + Date.now() + '_' + Math.random().toString(36).substr(2,9);
dataLayer.push({ event: 'purchase', event_id: eventId, ecommerce: { ... } });
```

In the Meta Pixel tag (client-side):
```javascript
fbq('track', 'Purchase', { value: 50, currency: 'EUR' }, { eventID: eventId });
```

In the sGTM Meta CAPI tag: map `event_data.event_id` to the Event ID field.

### Google Ads Enhanced Conversions Tag

| Setting | Value |
|---|---|
| Tag Type | Google Ads Conversion Tracking (built-in) |
| Conversion ID | `AW-XXXXXXXXX` |
| Conversion Label | `XXXXXXXXXXXXXXX` |
| Include user-provided data | Enable |
| Email | `event_data.user_data.email_address` |
| Phone | `event_data.user_data.phone_number` |
| Address | From `event_data.user_data.address.*` |

### LinkedIn Conversions API

LinkedIn supports server-side conversion tracking via their Conversions API. As of 2026, there is a community sGTM tag template.

| Setting | Value |
|---|---|
| API Token | LinkedIn CAPI access token |
| Conversion Rule ID | From LinkedIn Campaign Manager |
| User identifiers | Email (SHA256 hashed), LinkedIn first-party ID |

### TikTok Events API

TikTok also supports server-side event sending. Community sGTM tag template available.

| Setting | Value |
|---|---|
| Access Token | TikTok Events API token |
| Pixel ID | TikTok Pixel ID |
| Event | `CompletePayment`, `SubmitForm`, etc. |
| User data | Email, phone (hashed), IP, user agent |

## Event Data Enrichment

One of the most powerful sGTM features: enrich events with server-side data before sending to platforms.

### Common Enrichment Patterns

| Enrichment | Source | Benefit |
|---|---|---|
| Customer LTV | CRM / database lookup | Better Smart Bidding (tROAS) |
| Profit margin | Product database | Value-based bidding on margin, not revenue |
| Customer segment | CRM | Audience targeting signals |
| Lead score | CRM / marketing automation | Send qualified leads only |
| Offline conversion | CRM (delayed) | Feed back sales data to ad platforms |
| Cart contents | Backend session | More accurate than client-side scraping |

### Enrichment via Firestore Lookup (Example)

```
Trigger: purchase event arrives at sGTM

1. Extract customer_id from event_data
2. Firestore lookup: customers/{customer_id}
3. Get: ltv_score, customer_segment, first_purchase_date
4. Add to event_data:
   - event_data['x-ltv-score'] = ltv_score
   - event_data['x-customer-segment'] = customer_segment
   - event_data['x-new-customer'] = (first_purchase_date == today)
5. GA4 tag sends enriched data
6. Google Ads tag uses x-new-customer for New Customer Acquisition
```

### Enrichment via HTTP Request (API Lookup)

Use the sGTM `sendHttpRequest` API to call your own backend:

```javascript
const sendHttpRequest = require('sendHttpRequest');
const JSON = require('JSON');

sendHttpRequest('https://api.yourdomain.com/enrich', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ...' },
  body: JSON.stringify({ transaction_id: event_data.transaction_id })
}, (statusCode, headers, body) => {
  const data = JSON.parse(body);
  // Add enriched data to event
});
```

## Debugging Server-Side Tags

### sGTM Preview Mode

1. In GTM Server container, click "Preview"
2. Send a test event from your website (with client GTM in Preview mode)
3. The sGTM Preview panel shows:
   - Incoming request details
   - Which client claimed the request
   - Event data object created
   - Which tags fired and their responses
   - Outgoing HTTP requests (to GA4, Meta, etc.)

### Debugging Checklist

| Check | How |
|---|---|
| Events reaching sGTM? | Check sGTM Preview > Requests tab |
| Client claiming request? | Check sGTM Preview > Client tab (should show "Claimed") |
| Event data populated? | Check sGTM Preview > Event Data tab |
| Tags firing? | Check sGTM Preview > Tags tab |
| Tags succeeding? | Check HTTP response codes (200 = success) |
| Meta CAPI received? | Meta Events Manager > Test Events > Server |
| GA4 received? | GA4 DebugView or Real-time reports |
| Google Ads received? | Google Ads > Tools > Conversions > Diagnostics |

### Common Server-Side Issues

| Issue | Cause | Fix |
|---|---|---|
| 0 events in sGTM | `transport_url` not set in client GA4 | Add `transport_url` to Google Tag |
| Client not claiming | Request path doesn't match client config | Check client path settings |
| Meta CAPI 400 error | Missing required fields (access token, pixel ID) | Verify CAPI configuration |
| Meta Event Match Quality low | Missing user data (email, phone, fbp, fbc) | Pass user data in dataLayer |
| Duplicate events in GA4 | Both client and server sending | Disable direct GA4 sends from client |
| Cookie not first-party | Custom domain not configured | Set up CNAME for sGTM subdomain |
| High latency | Cold starts (0 min instances) | Set min instances to 1+ |

## When NOT to Use sGTM

sGTM is not always the right answer. Skip it when:

| Situation | Why |
|---|---|
| Monthly ad spend < EUR 2,000 | Cost of sGTM exceeds attribution value recovered |
| Simple website (brochure site) | No conversions to track server-side |
| No technical resources | Ongoing maintenance requires server/cloud knowledge |
| Single platform (GA4 only) | Client-side GA4 with transport_url gives most benefits |
| Low traffic (< 10k monthly visits) | Client-side tracking is sufficient |
| No privacy requirements | Ad blocker bypass alone may not justify the cost |

**Cheaper Alternatives to Full sGTM:**

| Alternative | Cost | Benefit |
|---|---|---|
| GA4 Google Tag with `transport_url` | Free (uses Google's proxy) | First-party cookies for GA4 |
| Meta CAPI via backend code | Free (dev time only) | Server-side Meta without sGTM |
| Google Ads Enhanced Conversions (client) | Free | Better attribution without server |
| LinkedIn offline conversions upload | Free | Feed CRM data to LinkedIn |

## MCP Tools for sGTM

### Auditing Your Setup

Use **`gtm_audit`** to inspect both your client-side and server-side GTM containers:

```
# Audit client container
gtm_audit(container_path="accounts/123456/containers/CLIENT_ID")
-> Check: transport_url configured, event_id generation, user_data passing

# Audit server container  
gtm_audit(container_path="accounts/123456/containers/SERVER_ID")
-> Check: clients configured, tags for each platform, enrichment tags
```

### Verifying Data Flow

Use **`ga4_run_report`** to compare event volumes before and after sGTM migration:

```
ga4_run_report(
  property_id="...",
  dimensions=["eventName", "platform"],
  metrics=["eventCount"],
  start_date="7daysAgo",
  end_date="today"
)

Compare:
- Event counts before sGTM vs. after
- Expect 10-30% increase in tracked events (recovered from ad blockers)
- Expect improved session duration and engagement metrics
```
