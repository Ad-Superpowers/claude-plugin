---
name: tracking-plan-builder
description: "This skill should be used when the user asks to \"build a tracking plan\", \"map business goals to conversion events\", \"audit what events to track\", \"define event naming conventions\", or mentions \"measurement strategy\", \"cross-platform event mapping\", or \"KPI to event mapping\". Do NOT use for: GTM tag/trigger implementation (use gtm-conversion-setup-guide), server-side tagging (use gtm-server-side-tagging-guide), or consent/privacy setup (use gtm-consent-mode-guide)."
---

# Tracking Plan Builder

A tracking plan is the single source of truth for what your website or app measures. Without one, you end up with duplicate events, missing parameters, inconsistent naming, and ad platforms that cannot optimize because they never receive the signals they need. This skill walks you through creating a tracking plan from business goals down to individual event parameters, then maps those events to every ad platform you run.

## Step 1: Identify Your Business Model

Your business model determines which events matter most. Start here before touching any tool.

### Business Model Decision Tree

```
What does the user DO on your site?
|
+-- Buys a product online -----------> E-COMMERCE
|
+-- Fills out a form / requests quote -> LEAD GENERATION
|
+-- Signs up for a trial / subscribes -> SaaS
|
+-- Calls, visits store, books appt --> LOCAL BUSINESS
|
+-- Multiple of the above -----------> HYBRID (pick primary, layer secondary)
```

## Step 2: Map Goals to KPIs to Events

### E-Commerce Tracking Plan

| Business Goal | KPI | GA4 Event | Key Parameters |
|---|---|---|---|
| Revenue | Total revenue | `purchase` | `value`, `currency`, `transaction_id`, `items[]` |
| Cart performance | Cart-to-purchase rate | `add_to_cart` | `value`, `currency`, `items[]` |
| Checkout drop-off | Checkout completion rate | `begin_checkout` | `value`, `currency`, `items[]`, `coupon` |
| Product interest | Product view rate | `view_item` | `value`, `currency`, `items[]` |
| Discovery | List engagement | `view_item_list` | `item_list_id`, `item_list_name`, `items[]` |
| Promotions | Promo click rate | `select_promotion` | `promotion_id`, `promotion_name`, `creative_name` |
| Shipping info | Shipping step rate | `add_shipping_info` | `value`, `currency`, `shipping_tier` |
| Payment info | Payment step rate | `add_payment_info` | `value`, `currency`, `payment_type` |
| Refunds | Refund rate | `refund` | `value`, `currency`, `transaction_id`, `items[]` |
| Wishlists | Wishlist engagement | `add_to_wishlist` | `value`, `currency`, `items[]` |

### Lead Generation Tracking Plan

| Business Goal | KPI | GA4 Event | Key Parameters |
|---|---|---|---|
| Lead volume | Total leads | `generate_lead` | `value`, `currency`, `lead_type` |
| Form engagement | Form start rate | `form_start` (custom) | `form_id`, `form_name`, `form_location` |
| Contact requests | Contact form submissions | `contact_form_submit` (custom) | `form_id`, `lead_type` |
| Phone calls | Call click rate | `click_to_call` (custom) | `phone_number`, `page_location` |
| Content downloads | Download rate | `file_download` | `file_name`, `file_extension`, `link_url` |
| Demo requests | Demo booking rate | `demo_request` (custom) | `value`, `service_type` |
| Quote requests | Quote request rate | `quote_request` (custom) | `value`, `service_category` |

### SaaS Tracking Plan

| Business Goal | KPI | GA4 Event | Key Parameters |
|---|---|---|---|
| Sign-ups | Registration rate | `sign_up` | `method` |
| Trial starts | Trial activation rate | `trial_start` (custom) | `plan_name`, `trial_length` |
| Activation | Feature adoption | `feature_use` (custom) | `feature_name`, `feature_category` |
| Subscription | Conversion to paid | `purchase` | `value`, `currency`, `plan_name`, `billing_cycle` |
| Upgrades | Upgrade rate | `plan_upgrade` (custom) | `old_plan`, `new_plan`, `value` |
| Engagement | DAU/MAU ratio | `login` | `method` |
| Onboarding | Onboarding completion | `tutorial_complete` | `step_count` |

### Local Business Tracking Plan

| Business Goal | KPI | GA4 Event | Key Parameters |
|---|---|---|---|
| Store visits | Direction clicks | `get_directions` (custom) | `store_id`, `store_name` |
| Phone calls | Call clicks | `click_to_call` (custom) | `phone_number`, `store_id` |
| Appointments | Booking rate | `book_appointment` (custom) | `service_type`, `value`, `store_id` |
| Online orders | Order value | `purchase` | `value`, `currency`, `transaction_id` |
| Reservations | Reservation rate | `reserve` (custom) | `party_size`, `date`, `store_id` |
| Contact | Inquiry rate | `generate_lead` | `value`, `lead_type`, `store_id` |

## Step 3: Event Naming Conventions

Consistent naming prevents chaos at scale. Adopt one convention and enforce it everywhere.

### Recommended Convention: snake_case (GA4 standard)

```
{object}_{action}

Examples:
  form_submit         (not formSubmit, not Form Submit)
  video_play          (not videoPlay)
  click_to_call       (not clickToCall)
  product_view        (not productView)
```

### Rules

| Rule | Good | Bad |
|---|---|---|
| Use snake_case | `form_submit` | `formSubmit`, `Form Submit` |
| Max 40 characters | `newsletter_signup` | `user_newsletter_email_signup_completed` |
| No spaces or special characters | `add_to_cart` | `add to cart`, `add-to-cart` |
| Start with noun or verb | `purchase`, `view_item` | `1_purchase`, `_view` |
| No PII in event names | `form_submit` | `john_form_submit` |
| Use GA4 recommended names when they exist | `purchase` | `completed_order` |
| Prefix custom events consistently | `custom_quiz_complete` | `quiz_complete` (ambiguous origin) |

### Parameter Naming

```
{object}_{descriptor}

Examples:
  item_id             (not itemId)
  item_name           (not itemName)
  form_id             (not formID)
  lead_type           (not leadType)
  button_text         (not buttonText)
```

### Reserved Parameter Names (GA4)

Do not create custom parameters with these names -- they are already used by GA4:

`page_location`, `page_referrer`, `page_title`, `screen_name`, `engagement_time_msec`, `session_id`, `user_id`, `debug_mode`

## Step 4: Priority Matrix

Not every event deserves equal attention. Use this matrix to decide implementation order.

### Priority Levels

| Priority | Label | Definition | Timeline |
|---|---|---|---|
| P0 | Must Track | Revenue/conversion events that ad platforms need for optimization | Week 1 |
| P1 | Should Track | Funnel events that explain drop-offs and inform bidding | Week 1-2 |
| P2 | Nice to Have | Engagement events for audience building and analysis | Week 2-4 |
| P3 | Future | Advanced events for mature measurement setups | Month 2+ |

### E-Commerce Priority Matrix

| Priority | Events |
|---|---|
| P0 | `purchase`, `add_to_cart`, `begin_checkout` |
| P1 | `view_item`, `add_payment_info`, `add_shipping_info` |
| P2 | `view_item_list`, `select_item`, `add_to_wishlist`, `select_promotion` |
| P3 | `view_cart`, `remove_from_cart`, `refund`, `view_promotion` |

### Lead Gen Priority Matrix

| Priority | Events |
|---|---|
| P0 | `generate_lead` (main form), `purchase` (if applicable) |
| P1 | `form_start`, `click_to_call`, `demo_request` |
| P2 | `file_download`, `video_play`, `page_scroll` (key pages) |
| P3 | `newsletter_signup`, `social_share`, `chat_open` |

### SaaS Priority Matrix

| Priority | Events |
|---|---|
| P0 | `sign_up`, `purchase` (subscription), `trial_start` |
| P1 | `login`, `feature_use` (core feature), `plan_upgrade` |
| P2 | `tutorial_complete`, `invite_sent`, `integration_connected` |
| P3 | `settings_changed`, `export_data`, `support_ticket` |

## Step 5: Platform-Specific Event Mapping

Each ad platform needs specific events sent in specific formats. This table maps your GA4 events to every platform.

### Cross-Platform Event Map

| GA4 Event | Meta Pixel | Google Ads | LinkedIn | TikTok |
|---|---|---|---|---|
| `purchase` | `Purchase` | `purchase` / Conversion Action | `conversion` (custom) | `CompletePayment` |
| `add_to_cart` | `AddToCart` | `add_to_cart` | -- | `AddToCart` |
| `begin_checkout` | `InitiateCheckout` | `begin_checkout` | -- | `InitiateCheckout` |
| `view_item` | `ViewContent` | `view_item` | -- | `ViewContent` |
| `generate_lead` | `Lead` | `submit_lead_form` | `conversion` (custom) | `SubmitForm` |
| `sign_up` | `CompleteRegistration` | `sign_up` | `conversion` (custom) | `CompleteRegistration` |
| `add_payment_info` | `AddPaymentInfo` | `add_payment_info` | -- | `AddPaymentInfo` |
| `search` | `Search` | -- | -- | `Search` |
| `contact` | `Contact` | -- | -- | `Contact` |
| `page_view` | `PageView` (auto) | `page_view` (auto) | `pageview` (auto) | `PageView` (auto) |

### Platform-Specific Parameter Requirements

#### Meta Pixel Parameters

Meta requires these parameters for optimization to work:

| Parameter | Required For | Format |
|---|---|---|
| `value` | Purchase, AddToCart, InitiateCheckout | Float (e.g., 49.99) |
| `currency` | Any event with value | ISO 4217 (e.g., "EUR", "USD") |
| `content_ids` | Dynamic Product Ads | Array of product IDs matching catalog |
| `content_type` | Dynamic Product Ads | "product" or "product_group" |
| `content_name` | ViewContent optimization | Product/page name string |
| `num_items` | AddToCart optimization | Integer count |

#### Google Ads Parameters

| Parameter | Required For | Format |
|---|---|---|
| `value` | Smart Bidding (tROAS) | Float |
| `currency` | Smart Bidding (tROAS) | ISO 4217 |
| `transaction_id` | Deduplication | Unique string |
| `send_to` | Conversion tracking | "AW-XXXXXXXXX/XXXXXX" |
| `new_customer` | New Customer Acquisition goal | Boolean |

#### LinkedIn Parameters

| Parameter | Required For | Format |
|---|---|---|
| `conversionId` | Conversion tracking | LinkedIn conversion ID |
| `value` | Revenue tracking | Float |
| `currency` | Revenue tracking | ISO 4217 |

#### TikTok Parameters

| Parameter | Required For | Format |
|---|---|---|
| `value` | Value-based optimization | Float |
| `currency` | Value-based optimization | ISO 4217 |
| `content_id` | Dynamic Showcase Ads | Product ID string |
| `content_type` | Dynamic Showcase Ads | "product" or "product_group" |
| `content_name` | Reporting | String |
| `quantity` | Reporting | Integer |

## Step 6: The items[] Array (E-Commerce)

The `items[]` array is shared across GA4, Google Ads, and (in adapted form) Meta and TikTok. Get this right once and every platform benefits.

### Standard items[] Object

```json
{
  "item_id": "SKU-12345",
  "item_name": "Blue Running Shoe",
  "item_brand": "BrandName",
  "item_category": "Shoes",
  "item_category2": "Running",
  "item_category3": "Men",
  "item_variant": "Blue / Size 10",
  "price": 129.99,
  "quantity": 1,
  "discount": 10.00,
  "coupon": "SUMMER10",
  "index": 0,
  "item_list_id": "category_shoes",
  "item_list_name": "Shoes Category Page"
}
```

### Minimum Viable items[] (P0)

If you cannot populate every field, these are the absolute minimum:

```json
{
  "item_id": "SKU-12345",
  "item_name": "Blue Running Shoe",
  "price": 129.99,
  "quantity": 1
}
```

## Step 7: Tracking Plan Spreadsheet Template

Use this structure in Google Sheets or Excel. One row per event.

### Column Structure

| Column | Description | Example |
|---|---|---|
| Event Name | snake_case event name | `purchase` |
| Event Type | Standard or Custom | Standard |
| Priority | P0 / P1 / P2 / P3 | P0 |
| Description | What triggers this event | User completes checkout |
| Trigger Location | Page or element | /checkout/confirmation |
| Parameters | JSON-like list | `value`, `currency`, `transaction_id`, `items[]` |
| GA4 | Checkmark if sent to GA4 | Yes |
| Meta | Matching Meta event name | `Purchase` |
| Google Ads | Matching conversion action | `purchase` |
| LinkedIn | Matching conversion name | `conversion` |
| TikTok | Matching TikTok event | `CompletePayment` |
| Data Source | Where the data comes from | Data Layer / URL / DOM |
| Owner | Who implements | Developer / Agency |
| Status | Not Started / In Progress / Live / QA | Live |
| Notes | Implementation notes | Fires after payment confirmation |

### Example Row

| Event Name | Type | Priority | Description | Trigger | Parameters | GA4 | Meta | Google Ads | LinkedIn | TikTok | Source | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `purchase` | Standard | P0 | Order confirmed | /thank-you | value, currency, transaction_id, items[] | Yes | Purchase | purchase | conversion | CompletePayment | Data Layer | Dev | Live |
| `generate_lead` | Standard | P0 | Contact form submit | /contact | value, lead_type | Yes | Lead | submit_lead_form | conversion | SubmitForm | Form Submit | Dev | QA |
| `form_start` | Custom | P1 | User begins form | /contact | form_id, form_name | Yes | -- | -- | -- | -- | JS listener | Dev | Not Started |

## Step 8: Data Layer Design

The data layer is the bridge between your website and your tags. A well-structured data layer makes GTM implementation straightforward.

### Standard Data Layer Push (E-Commerce Purchase)

```javascript
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: 'T-20260403-001',
    value: 149.99,
    currency: 'EUR',
    tax: 26.05,
    shipping: 5.99,
    coupon: 'SPRING10',
    items: [
      {
        item_id: 'SKU-12345',
        item_name: 'Blue Running Shoe',
        item_brand: 'BrandName',
        item_category: 'Shoes',
        price: 129.99,
        quantity: 1,
        discount: 10.00
      }
    ]
  }
});
```

### Standard Data Layer Push (Lead Gen)

```javascript
window.dataLayer.push({
  event: 'generate_lead',
  lead_type: 'contact_form',
  form_id: 'contact-main',
  value: 50,
  currency: 'EUR'
});
```

### Data Layer Validation Checklist

- [ ] `dataLayer` is initialized before GTM snippet loads
- [ ] All monetary values are numbers (not strings)
- [ ] Currency is ISO 4217 (3-letter code)
- [ ] `transaction_id` is unique per transaction
- [ ] `items[]` array is present for all e-commerce events
- [ ] Each item has at minimum `item_id`, `item_name`, `price`, `quantity`
- [ ] No PII (names, emails, phone numbers) in the data layer
- [ ] Custom event names follow snake_case convention
- [ ] Events fire at the correct moment (after action, not on page load)

## Step 9: Audit Your Current Setup

Use the Ad Superpowers MCP tools to audit what you currently have:

### Available MCP Tools

1. **`gtm_list_containers`** -- List all GTM containers to identify which accounts and containers exist. Start here to get your container IDs.

2. **`gtm_audit`** -- Audit a GTM container to see all tags, triggers, and variables currently configured. Compare this against your tracking plan to find gaps.

3. **`ga4_run_report`** -- Pull GA4 reports to verify which events are actually arriving and with what parameters. Cross-reference with your tracking plan to find events that are planned but not firing, or firing but not planned.

### Audit Workflow

```
1. gtm_list_containers
   -> Get container ID and account ID

2. gtm_audit(container_path="accounts/123456/containers/789012")
   -> Export all tags, triggers, variables
   -> Compare against tracking plan

3. ga4_run_report(
     property_id="...",
     dimensions=["eventName"],
     metrics=["eventCount"],
     start_date="28daysAgo",
     end_date="today"
   )
   -> See which events actually fire
   -> Check for events in GA4 not in your plan (rogue events)
   -> Check for events in your plan not in GA4 (missing events)
```

### Common Audit Findings

| Finding | Severity | Action |
|---|---|---|
| P0 event missing entirely | Critical | Implement immediately |
| P0 event fires but missing `value` parameter | High | Add parameter to data layer |
| Duplicate events (same event, different tags) | High | Consolidate into single tag |
| Events with wrong naming convention | Medium | Rename and migrate |
| Rogue events not in tracking plan | Low | Document or remove |
| P2/P3 events not yet implemented | Low | Schedule for next sprint |

## Step 10: Maintenance and Governance

A tracking plan is a living document. Without governance, it rots within months.

### Quarterly Review Checklist

- [ ] All P0 events verified firing correctly (check GA4 real-time)
- [ ] New features/pages assessed for tracking needs
- [ ] Removed pages/features: decommission orphaned events
- [ ] Ad platform conversion actions match tracking plan
- [ ] Data layer schema matches tracking plan parameters
- [ ] GTM container audit shows no unauthorized tags
- [ ] Consent mode functioning (check consent rates)
- [ ] Cross-platform conversion counts reconciled

### Change Management Process

```
1. Request: "We need to track X"
2. Add to tracking plan spreadsheet (event name, parameters, platforms, priority)
3. Review: Does this duplicate an existing event? Is naming consistent?
4. Implement: Data layer push + GTM tags
5. QA: Verify in GTM Preview, GA4 DebugView, platform event managers
6. Document: Update tracking plan status to "Live"
7. Monitor: Check event counts after 48 hours
```

### Version History

Keep a changelog tab in your tracking plan:

| Date | Change | Reason | Author |
|---|---|---|---|
| 2026-04-01 | Added `quiz_complete` event | New quiz feature launch | Dev team |
| 2026-03-15 | Removed `old_form_submit` | Form redesigned | Marketing |
| 2026-03-01 | Added `value` to `generate_lead` | Enable Google Ads tROAS bidding | PPC team |
