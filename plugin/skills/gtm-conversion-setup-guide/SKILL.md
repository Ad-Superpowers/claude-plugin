---
name: gtm-conversion-setup-guide
description: "This skill should be used when the user asks to \"set up conversion tags in GTM\", \"configure a Meta Pixel trigger\", \"debug a tag not firing\", \"add Google Ads conversion tracking in GTM\", or mentions \"GTM tag setup\", \"trigger conditions\", or \"LinkedIn Insight Tag\". Do NOT use for: strategic tracking planning (use tracking-plan-builder), server-side tagging (use gtm-server-side-tagging-guide), or consent implementation (use gtm-consent-mode-guide)."
---

# GTM Conversion Setup Guide

This skill covers the tactical implementation of conversion tracking tags in Google Tag Manager. For each ad platform, you get the exact tag type, required fields, trigger configuration, and variable setup needed to make conversions fire correctly.

## Prerequisites

Before implementing tags, ensure you have:

- [ ] A GTM container installed on all pages (via `<script>` in `<head>`)
- [ ] A tracking plan defining which events to implement (see tracking-plan-builder skill)
- [ ] A data layer pushing events from your website code
- [ ] Access to each ad platform's conversion/event configuration UI
- [ ] GTM Preview mode familiarity (the debugger panel)

Use **`gtm_list_containers`** to verify your GTM containers and **`gtm_audit`** to see what is already configured.

## Part 1: GA4 Tags

### GA4 Configuration Tag (Google Tag)

This is the foundation. Every GA4 property needs exactly one Google Tag that loads on all pages.

| Setting | Value |
|---|---|
| Tag Type | Google Tag |
| Tag ID | `G-XXXXXXXXXX` (your Measurement ID) |
| Trigger | All Pages (Page View) |
| Firing Priority | High (fires first) |

#### Configuration Parameters (optional but recommended)

| Parameter | Value | Purpose |
|---|---|---|
| `send_page_view` | `true` | Auto page views (default) |
| `debug_mode` | `true` (dev only) | Enables GA4 DebugView |
| `user_id` | `{{DLV - user_id}}` | Cross-device tracking |
| `cookie_flags` | `SameSite=None;Secure` | Cross-site cookie support |

### GA4 Event Tags

Create one GA4 Event tag per custom event or per standard event that needs extra parameters.

#### Purchase Event Tag

| Setting | Value |
|---|---|
| Tag Type | Google Analytics: GA4 Event |
| Measurement ID | `G-XXXXXXXXXX` |
| Event Name | `purchase` |
| Trigger | Custom Event: `purchase` |

**Event Parameters:**

| Parameter Name | Value |
|---|---|
| `transaction_id` | `{{DLV - ecommerce.transaction_id}}` |
| `value` | `{{DLV - ecommerce.value}}` |
| `currency` | `{{DLV - ecommerce.currency}}` |
| `tax` | `{{DLV - ecommerce.tax}}` |
| `shipping` | `{{DLV - ecommerce.shipping}}` |
| `coupon` | `{{DLV - ecommerce.coupon}}` |
| `items` | `{{DLV - ecommerce.items}}` |

#### Generate Lead Event Tag

| Setting | Value |
|---|---|
| Tag Type | Google Analytics: GA4 Event |
| Measurement ID | `G-XXXXXXXXXX` |
| Event Name | `generate_lead` |
| Trigger | Custom Event: `generate_lead` |

**Event Parameters:**

| Parameter Name | Value |
|---|---|
| `value` | `{{DLV - value}}` |
| `currency` | `{{DLV - currency}}` |
| `lead_type` | `{{DLV - lead_type}}` |

#### Other Standard Event Tags

Use the same pattern for these events. Each gets its own GA4 Event tag:

| Event | Trigger | Key Parameters |
|---|---|---|
| `sign_up` | Custom Event: `sign_up` | `method` |
| `add_to_cart` | Custom Event: `add_to_cart` | `value`, `currency`, `items` |
| `begin_checkout` | Custom Event: `begin_checkout` | `value`, `currency`, `items` |
| `add_payment_info` | Custom Event: `add_payment_info` | `value`, `currency`, `payment_type` |
| `add_shipping_info` | Custom Event: `add_shipping_info` | `value`, `currency`, `shipping_tier` |
| `view_item` | Custom Event: `view_item` | `value`, `currency`, `items` |

## Part 2: Google Ads Tags

### Google Ads Conversion Tracking Tag

You need one tag per conversion action. Get the Conversion ID and Label from Google Ads > Goals > Conversions > your action > Tag setup.

| Setting | Value |
|---|---|
| Tag Type | Google Ads Conversion Tracking |
| Conversion ID | `AW-XXXXXXXXX` |
| Conversion Label | `XXXXXXXXXXXXXXXXXX` |
| Conversion Value | `{{DLV - ecommerce.value}}` |
| Currency Code | `{{DLV - ecommerce.currency}}` |
| Transaction ID | `{{DLV - ecommerce.transaction_id}}` |
| Trigger | Custom Event: `purchase` |

#### Conversion Linker Tag (Required)

This tag must fire on all pages for Google Ads conversion tracking to work. Without it, conversions from Google Ads clicks will not be attributed.

| Setting | Value |
|---|---|
| Tag Type | Conversion Linker |
| Trigger | All Pages (Page View) |
| Enable linking across domains | Check if multi-domain |
| Firing Priority | High (before conversion tags) |

#### Enhanced Conversions Setup

Enhanced Conversions use first-party data (hashed email, phone) to improve attribution. Configure in the Google Ads Conversion Tracking tag:

| Setting | Value |
|---|---|
| Include user-provided data | Check |
| Data source | Code / Data Layer |
| Email | `{{DLV - user_data.email}}` |
| Phone | `{{DLV - user_data.phone}}` |
| First Name | `{{DLV - user_data.first_name}}` |
| Last Name | `{{DLV - user_data.last_name}}` |
| Street Address | `{{DLV - user_data.street}}` |
| City | `{{DLV - user_data.city}}` |
| Postal Code | `{{DLV - user_data.postal_code}}` |
| Country | `{{DLV - user_data.country}}` |

Data layer push for Enhanced Conversions:

```javascript
window.dataLayer.push({
  event: 'purchase',
  user_data: {
    email: 'user@example.com',    // Will be hashed by GTM
    phone: '+31612345678',
    first_name: 'Jan',
    last_name: 'de Vries',
    street: 'Keizersgracht 100',
    city: 'Amsterdam',
    postal_code: '1015 AA',
    country: 'NL'
  },
  ecommerce: { /* ... */ }
});
```

### Google Ads Remarketing Tag

| Setting | Value |
|---|---|
| Tag Type | Google Ads Remarketing |
| Conversion ID | `AW-XXXXXXXXX` (same as conversion) |
| Trigger | All Pages |
| Custom Parameters | See below for dynamic remarketing |

**Dynamic Remarketing Parameters (E-Commerce):**

| Parameter | Value | Purpose |
|---|---|---|
| `ecomm_prodid` | `{{DLV - ecommerce.items.0.item_id}}` | Product ID for dynamic ads |
| `ecomm_pagetype` | `{{Page Type}}` | home/category/product/cart/purchase |
| `ecomm_totalvalue` | `{{DLV - ecommerce.value}}` | Cart/transaction value |
| `ecomm_category` | `{{DLV - ecommerce.items.0.item_category}}` | Product category |

## Part 3: Meta Pixel Tags

### Meta Pixel Base Code (via Custom HTML Tag)

While Meta provides a GTM template in the Community Template Gallery, the Custom HTML approach gives you full control.

| Setting | Value |
|---|---|
| Tag Type | Custom HTML |
| Trigger | All Pages |
| Tag firing priority | 100 (fire early) |

```html
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{{Meta Pixel ID}}');
fbq('track', 'PageView');
</script>
```

**Alternative:** Use the official "Meta Pixel" template from the GTM Community Template Gallery for a no-code setup.

### Meta Standard Event Tags

Create a Custom HTML tag for each standard event, OR use the Community Template.

#### Purchase Event

| Setting | Value |
|---|---|
| Tag Type | Custom HTML |
| Trigger | Custom Event: `purchase` |
| Tag Sequencing | Fires after Meta Pixel Base Code |

```html
<script>
fbq('track', 'Purchase', {
  value: {{DLV - ecommerce.value}},
  currency: '{{DLV - ecommerce.currency}}',
  content_ids: {{DLV - ecommerce.content_ids}},
  content_type: 'product',
  num_items: {{DLV - ecommerce.item_count}}
});
</script>
```

#### Lead Event

```html
<script>
fbq('track', 'Lead', {
  value: {{DLV - value}},
  currency: '{{DLV - currency}}',
  content_name: '{{DLV - lead_type}}'
});
</script>
```

#### Full Meta Standard Events Reference

| Meta Event | When to Fire | Required Parameters |
|---|---|---|
| `PageView` | Every page (in base code) | None |
| `ViewContent` | Product/content page view | `value`, `currency`, `content_ids`, `content_type` |
| `AddToCart` | Item added to cart | `value`, `currency`, `content_ids`, `content_type` |
| `InitiateCheckout` | Checkout started | `value`, `currency`, `num_items` |
| `AddPaymentInfo` | Payment info entered | `value`, `currency` |
| `Purchase` | Order completed | `value`, `currency`, `content_ids`, `content_type` |
| `Lead` | Lead form submitted | `value`, `currency` |
| `CompleteRegistration` | Account created | `value`, `currency` |
| `Search` | Search performed | `search_string` |
| `Contact` | Contact action taken | None |

### Meta Conversions API (Server-Side)

Meta Conversions API (CAPI) is mandatory for maintaining signal quality — client-side Pixel alone is no longer sufficient due to browser restrictions and iOS privacy changes. Implement both client-side (Pixel) and server-side (CAPI) for redundant event matching. The server-side component is covered in the gtm-server-side-tagging-guide skill. Key point: include an `event_id` parameter in both the Pixel event and the CAPI event for deduplication.

```html
<script>
var eventId = 'evt_' + Date.now() + '_' + Math.random().toString(36).substr(2,9);
fbq('track', 'Purchase', {
  value: {{DLV - ecommerce.value}},
  currency: '{{DLV - ecommerce.currency}}'
}, {eventID: eventId});
</script>
```

## Part 4: LinkedIn Insight Tag

### LinkedIn Insight Tag Base Code

| Setting | Value |
|---|---|
| Tag Type | Custom HTML (or LinkedIn Insight Tag template) |
| Trigger | All Pages |
| Tag firing priority | 90 |

```html
<script type="text/javascript">
_linkedin_partner_id = "{{LinkedIn Partner ID}}";
window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
window._linkedin_data_partner_ids.push(_linkedin_partner_id);
</script>
<script type="text/javascript">
(function(l) {
if (!l){window.lintrk = function(a,b){window.lintrk.q.push([a,b])};
window.lintrk.q=[]}
var s = document.getElementsByTagName("script")[0];
var b = document.createElement("script");
b.type = "text/javascript";b.async = true;
b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
s.parentNode.insertBefore(b, s);})(window.lintrk);
</script>
```

### LinkedIn Conversion Events

LinkedIn conversions are configured in Campaign Manager, not in GTM. In GTM, you fire the insight tag event that LinkedIn maps to its conversion.

#### Event-Specific Conversion (recommended)

```html
<script>
window.lintrk('track', { conversion_id: {{LinkedIn Conversion ID}} });
</script>
```

| Setting | Value |
|---|---|
| Tag Type | Custom HTML |
| Trigger | Custom Event matching your conversion |
| Tag Sequencing | After LinkedIn Insight Tag base |

#### URL-Based Conversion (alternative)

Configure in LinkedIn Campaign Manager:
1. Go to Analyze > Conversions
2. Create conversion using "Page load" trigger
3. Set URL rule (equals, starts with, or contains your thank-you page URL)

No additional GTM tag needed -- the Insight Tag base code handles it.

## Part 5: TikTok Pixel

### TikTok Pixel Base Code

| Setting | Value |
|---|---|
| Tag Type | Custom HTML (or TikTok Pixel template) |
| Trigger | All Pages |
| Tag firing priority | 90 |

```html
<script>
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e};ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};
  ttq.load('{{TikTok Pixel ID}}');
  ttq.page();
}(window, document, 'ttq');
</script>
```

### TikTok Standard Event Tags

#### Purchase / CompletePayment Event

```html
<script>
ttq.track('CompletePayment', {
  value: {{DLV - ecommerce.value}},
  currency: '{{DLV - ecommerce.currency}}',
  content_id: '{{DLV - ecommerce.items.0.item_id}}',
  content_type: 'product',
  content_name: '{{DLV - ecommerce.items.0.item_name}}',
  quantity: {{DLV - ecommerce.item_count}}
});
</script>
```

#### Full TikTok Standard Events Reference

| TikTok Event | When to Fire | Key Parameters |
|---|---|---|
| `ViewContent` | Product page view | `content_id`, `content_type`, `content_name`, `value`, `currency` |
| `AddToCart` | Item added to cart | `content_id`, `content_type`, `value`, `currency`, `quantity` |
| `InitiateCheckout` | Checkout started | `value`, `currency` |
| `CompletePayment` | Purchase completed | `content_id`, `content_type`, `value`, `currency`, `quantity` |
| `SubmitForm` | Form submitted | `content_name` |
| `CompleteRegistration` | Account created | `content_name` |
| `Contact` | Contact action | -- |
| `Search` | Search performed | `query` |
| `ClickButton` | CTA clicked | `content_name` |
| `Download` | App/file download | `content_name` |

## Part 6: Triggers

Triggers determine WHEN tags fire. Choosing the right trigger type prevents misfires and missed events.

### Trigger Type Decision Tree

```
What initiates the event?
|
+-- Page loads --------------------------------> Page View trigger
|   +-- Every page ----------------------------> All Pages
|   +-- Specific URL --------------------------> Page View + URL condition
|
+-- User clicks something --------------------> Click trigger
|   +-- Any link ------------------------------> Just Links (Click - All)
|   +-- Specific button/element ---------------> Just Links or All Elements + CSS selector
|
+-- Data Layer event fires --------------------> Custom Event trigger
|   (RECOMMENDED for most conversion events)
|
+-- Form is submitted -------------------------> Form Submission trigger
|   (GTM intercepts native form submits)
|
+-- Element becomes visible -------------------> Element Visibility trigger
|   (lazy-loaded content, scroll-into-view)
|
+-- Timer fires ------------------------------> Timer trigger
|   (engagement time tracking)
|
+-- DOM is fully parsed -----------------------> DOM Ready trigger
|   (when you need DOM but not all resources)
|
+-- Page fully loaded -------------------------> Window Loaded trigger
|   (when you need all images/scripts loaded)
```

### Custom Event Trigger (Most Common for Conversions)

This is the recommended approach: push a data layer event, then trigger on it.

| Setting | Value |
|---|---|
| Trigger Type | Custom Event |
| Event Name | `purchase` (must match `event` key in dataLayer.push) |
| This trigger fires on | All Custom Events (or add conditions) |

### Click Trigger with CSS Selector

For tracking button clicks without a data layer event:

| Setting | Value |
|---|---|
| Trigger Type | Click - All Elements |
| This trigger fires on | Some Clicks |
| Condition | Click Element matches CSS selector `button.cta-submit` |

Common CSS selectors:

| Selector | Matches |
|---|---|
| `#submit-btn` | Element with id="submit-btn" |
| `.cta-button` | Elements with class="cta-button" |
| `button[type="submit"]` | Submit buttons |
| `a[href*="tel:"]` | Phone links |
| `a[href*="mailto:"]` | Email links |
| `form.contact-form` | Specific form element |

### URL Matching Conditions

| Match Type | Value | Matches |
|---|---|---|
| equals | `/thank-you` | Exact path only |
| contains | `thank-you` | Any URL containing the string |
| starts with | `/checkout/` | URLs beginning with /checkout/ |
| matches RegEx | `/(thank-you|confirmation)` | Either path |
| does not contain | `preview=true` | Excludes preview mode |

### Form Submission Trigger

| Setting | Value |
|---|---|
| Trigger Type | Form Submission |
| Wait for Tags | Check (waits for tags before form navigates) |
| Check Validation | Check (only fires if form validates) |
| Enable this trigger when | All Forms (or add conditions) |
| This trigger fires on | Some Forms |
| Condition | Form ID equals `contact-form` |

**Warning:** Form Submission triggers can be unreliable with SPAs (Single Page Applications) or AJAX forms. In those cases, use a Custom Event trigger with a data layer push from your form handler code.

## Part 7: Variables

Variables supply dynamic values to your tags. Set these up before creating tags.

### Data Layer Variables (Most Important)

| Variable Name | Data Layer Variable Name | Example Value |
|---|---|---|
| `DLV - ecommerce.value` | `ecommerce.value` | `149.99` |
| `DLV - ecommerce.currency` | `ecommerce.currency` | `EUR` |
| `DLV - ecommerce.transaction_id` | `ecommerce.transaction_id` | `T-20260403-001` |
| `DLV - ecommerce.items` | `ecommerce.items` | `[{item_id: ...}]` |
| `DLV - value` | `value` | `50` |
| `DLV - currency` | `currency` | `EUR` |
| `DLV - lead_type` | `lead_type` | `contact_form` |
| `DLV - user_data.email` | `user_data.email` | `user@example.com` |

### URL Variables

| Variable Name | Component Type | Example Use |
|---|---|---|
| `URL - Path` | Path | `/products/shoes` |
| `URL - Query` | Query (key: `utm_source`) | `google` |
| `URL - Full` | Full URL | `https://example.com/page?q=1` |
| `URL - Hostname` | Hostname | `example.com` |

### 1st Party Cookie Variables

| Variable Name | Cookie Name | Use Case |
|---|---|---|
| `Cookie - _ga` | `_ga` | GA client ID extraction |
| `Cookie - user_logged_in` | `user_logged_in` | Conditional tag firing |

### Lookup Table Variable (Page Type)

Map URL paths to page types for remarketing:

| Input (Page Path) | Output |
|---|---|
| `/` | `home` |
| contains `/product/` | `product` |
| contains `/category/` | `category` |
| `/cart` | `cart` |
| `/checkout/confirmation` | `purchase` |
| Default | `other` |

### Custom JavaScript Variable (Item Count)

```javascript
function() {
  var ecommerce = {{DLV - ecommerce.items}};
  if (ecommerce && Array.isArray(ecommerce)) {
    return ecommerce.reduce(function(sum, item) {
      return sum + (item.quantity || 1);
    }, 0);
  }
  return 0;
}
```

## Part 8: Tag Sequencing and Firing Order

Tags can depend on other tags. Use sequencing to control execution order.

### Recommended Firing Order

| Order | Tag | Why |
|---|---|---|
| 1 | Consent Initialization | Must fire before any tracking |
| 2 | Google Tag (GA4 Config) | Initializes GA4 |
| 3 | Conversion Linker | Required for Google Ads attribution |
| 4 | Meta Pixel Base | Initializes Meta tracking |
| 5 | LinkedIn Insight Tag Base | Initializes LinkedIn tracking |
| 6 | TikTok Pixel Base | Initializes TikTok tracking |
| 7+ | Event-specific tags | Fire on their respective triggers |

### Tag Sequencing Configuration

In any event tag (e.g., Meta Purchase):
1. Open tag settings > Advanced Settings > Tag Sequencing
2. Check "Fire a tag before [this tag] fires"
3. Select the base/init tag (e.g., Meta Pixel Base Code)
4. Check "Don't fire [this tag] if [setup tag] fails"

### Tag Firing Priority

Use numeric priority values (higher = fires first):

| Tag | Priority |
|---|---|
| Consent initialization | 200 |
| Google Tag (GA4 Config) | 150 |
| Conversion Linker | 140 |
| Platform base codes | 100 |
| Conversion event tags | 0 (default) |

## Part 9: Testing and Debugging

### GTM Preview Mode Checklist

1. Click "Preview" in GTM workspace
2. Enter your website URL
3. Navigate to the page/action you want to test
4. In the debug panel, verify:
   - [ ] Tags fire on the correct triggers
   - [ ] Tags fire in the correct order
   - [ ] Data Layer variables resolve to expected values
   - [ ] No tags fire that should not fire
   - [ ] No JavaScript errors in the console

### Platform-Specific Debugging Tools

| Platform | Tool | How to Access |
|---|---|---|
| GA4 | DebugView | GA4 > Admin > DebugView (enable `debug_mode` parameter) |
| GA4 | Real-Time | GA4 > Reports > Real-time |
| Google Ads | Tag Assistant | tagassistant.google.com |
| Meta | Pixel Helper | Chrome extension "Meta Pixel Helper" |
| Meta | Events Manager | business.facebook.com > Events Manager > Test Events |
| LinkedIn | Insight Tag Helper | Chrome extension "LinkedIn Insight Tag Helper" |
| TikTok | Pixel Helper | Chrome extension "TikTok Pixel Helper" |

### Common Debugging Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| Tag never fires | Trigger condition wrong | Check URL/event matching in Preview |
| Tag fires twice | Duplicate trigger or tag | Check for multiple tags with same purpose |
| Value shows as undefined | Data Layer variable path wrong | Check exact path in Data Layer tab |
| Conversion count differs from GA4 | Deduplication missing | Add `transaction_id` to both |
| Meta Pixel shows "inactive" | Base code not loading | Check tag sequencing, consent blocking |
| Google Ads shows 0 conversions | Conversion Linker missing | Add Conversion Linker on All Pages |

## Part 10: Using MCP Tools for GTM Management

### Available MCP Tools

- **`gtm_list_containers`** -- List all GTM containers and accounts. Use to find container IDs before auditing.

- **`gtm_audit`** -- Audit a container to see all tags, triggers, and variables. Use to verify your implementation matches your tracking plan, find duplicate tags, or identify missing conversion tags.

- **`gtm_manage`** -- Create, update, or delete tags, triggers, and variables programmatically. Use to batch-create tags from your tracking plan or update configurations across multiple tags.

### Audit After Implementation

After setting up all tags, run an audit to verify:

```
gtm_audit(container_path="accounts/123456/containers/789012")

Check for:
- All P0 conversion tags present
- Each tag has correct trigger
- No duplicate tags for same event
- Base/init tags have higher priority
- Tag sequencing configured for dependent tags
- Variables resolve correctly
```

### Batch Tag Creation Pattern

Use `gtm_manage` to create tags programmatically when setting up multiple platforms:

```
1. Create all Data Layer Variables first
2. Create triggers for each event
3. Create platform base tags (GA4 Config, Pixel base codes)
4. Create event-specific tags with correct triggers
5. Run gtm_audit to verify
6. Test in Preview mode
7. Publish workspace
```
