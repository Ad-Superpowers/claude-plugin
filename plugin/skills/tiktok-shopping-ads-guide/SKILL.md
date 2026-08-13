---
name: tiktok-shopping-ads-guide
description: "This skill should be used when the user asks to \"set up TikTok Shop ads\", \"create dynamic product ads on TikTok\", \"fix TikTok product feed errors\", \"build collection ads on TikTok\", or mentions \"TikTok Shopping\", \"Video Shopping Ads\", or \"TikTok product catalog\". Do NOT use for: general TikTok creative strategy (use tiktok-hook-optimization-guide), audience building (use tiktok-audience-strategy), or Spark Ads (use tiktok-spark-ads-strategy)."
---

# TikTok Shopping Ads Guide

## Purpose

Help advertisers set up and optimize product-focused advertising on TikTok, including catalog-based dynamic ads, Video Shopping Ads (VSA), TikTok Shop integration, and collection ads. E-commerce on TikTok is growing at 3-4x the rate of traditional social commerce, but the technical setup and creative requirements are unique to the platform.

## When to Use This Skill

Invoke when user mentions:
- **TikTok Shop:** "How do I set up TikTok Shop ads?"
- **Product catalog:** "How do I upload my product feed to TikTok?"
- **Dynamic product ads:** "How do I retarget with product ads on TikTok?"
- **Shopping ads:** "What are Video Shopping Ads?"
- **Collection ads:** "How do I create collection ads on TikTok?"
- **Product feed:** "My TikTok product feed has errors"

## Required Tools

| Tool | Purpose |
|------|---------|
| `tiktok_query` | Pull campaign data, ad group configurations, and catalog status |
| `tiktok_get_report` | Retrieve product-level and ad-level performance data |

---

## Part 1: TikTok Shopping Ad Formats

### Automated Shopping Campaign Types

TikTok offers two automated campaign types optimized for shopping outcomes:

| Campaign Type | What It Does | Best For |
|---|---|---|
| **Smart+ Shopping Campaigns** | Fully automated targeting, bidding, and creative optimization using AI | Accounts with sufficient pixel data (50+ purchases/week), hands-off scaling |
| **GMV Max** | Maximizes Gross Merchandise Value across TikTok Shop organics + paid ads | TikTok Shop sellers wanting to maximize total store revenue |

**Smart+ vs Manual:** Smart+ often outperforms manual setup once the algorithm has learned (typically after 7-14 days and 50+ conversions). Start manual to establish baseline data, then test Smart+. GMV Max is only available for TikTok Shop (in-app checkout) sellers.

### Format Overview

```
TIKTOK SHOPPING AD ECOSYSTEM:
─────────────────────────────

VIDEO SHOPPING ADS (VSA)
├── Full-screen video with product card overlay
├── Product card shows: image, title, price, CTA
├── Tap product card → product detail page → checkout
├── Can link to TikTok Shop OR external website
├── Best for: Single product promotion with storytelling
└── ROAS benchmark: 3-6x for optimized campaigns

CATALOG LISTING ADS
├── Auto-generated ads from product catalog
├── TikTok creates the creative using catalog images
├── Product title, price, and image displayed
├── Lower creative effort, algorithmic optimization
├── Best for: Large catalogs (100+ SKUs)
└── ROAS benchmark: 2-4x (less creative control)

COLLECTION ADS
├── Video ad with swipeable product gallery below
├── Gallery shows 2-6 products from catalog
├── Video plays while user browses products
├── Tap product → instant landing page (in-app)
├── Best for: Product discovery, category promotion
└── ROAS benchmark: 2.5-5x

DYNAMIC SHOWCASE ADS (DSA)
├── Personalized product ads based on user behavior
├── Retargets users who viewed/carted/purchased
├── Auto-generates creative from catalog
├── Shows products the user previously engaged with
├── Best for: Retargeting, abandoned cart recovery
└── ROAS benchmark: 5-12x (retargeting advantage)

LIVE SHOPPING ADS
├── Promote a live stream with integrated product cards
├── Users watch live, tap products in real-time
├── Combines entertainment with instant purchase
├── Requires TikTok Shop + live streaming capability
├── Best for: Flash sales, product launches, demonstrations
└── ROAS benchmark: 4-10x (high engagement, high conversion)
```

### Format Selection Decision Tree

```
                    What's your primary goal?
                            │
           ┌────────────────┼────────────────┐
           ▼                ▼                ▼
     Product           Retargeting      Brand +
     Discovery                          Commerce
           │                │                │
           ▼                ▼                ▼
      How many           Dynamic         Video Shopping
      products?          Showcase Ads     Ads (VSA)
           │                                 │
     ┌─────┼─────┐                           ▼
     ▼     ▼     ▼                    Single product
    1-5   6-50   50+                  or category?
     │     │     │                     │         │
     ▼     ▼     ▼                     ▼         ▼
   VSA   Collection  Catalog         VSA      Collection
         Ads        Listing Ads               Ads

Do you have TikTok Shop set up?
├── Yes → All formats available, prefer in-platform checkout
└── No  → VSA + Collection Ads linking to external website
          (Dynamic Showcase requires pixel + catalog)
```

---

## Part 2: Product Catalog Setup

### Catalog Creation Methods

| Method | Best For | Setup Time | Maintenance |
|--------|----------|------------|-------------|
| Manual upload (CSV) | Small catalogs (<100 products) | 1-2 hours | Manual updates |
| Scheduled feed (URL) | Medium catalogs (100-10K) | 2-4 hours | Auto-refresh (hourly/daily) |
| TikTok Catalog Manager API | Large catalogs (10K+) | 4-8 hours | Fully automated |
| Shopify integration | Shopify stores | 30 minutes | Auto-sync |
| WooCommerce integration | WooCommerce stores | 1-2 hours | Auto-sync |
| BigCommerce integration | BigCommerce stores | 30 minutes | Auto-sync |

### Product Feed Specification

Required fields:

| Field | Format | Example | Notes |
|-------|--------|---------|-------|
| `sku_id` | String, max 100 | "PROD-12345" | Unique per product, never reuse |
| `title` | String, max 255 | "Blue Organic Cotton T-Shirt" | Include key attributes |
| `description` | String, max 10,000 | "Premium organic cotton..." | Rich description, no HTML |
| `availability` | Enum | "in stock" | "in stock", "out of stock", "preorder" |
| `condition` | Enum | "new" | "new", "refurbished", "used" |
| `price` | Decimal + currency | "29.99 EUR" | Must match landing page price |
| `link` | URL | "https://shop.com/product" | Product detail page URL |
| `image_link` | URL | "https://cdn.com/img.jpg" | Min 500x500px, max 4MB |
| `brand` | String | "EcoBrand" | Brand name |

Recommended fields (improve performance by 20-40%):

| Field | Format | Impact |
|-------|--------|--------|
| `additional_image_link` | Up to 10 URLs | +15-25% CTR (more visual variety) |
| `product_type` | Category path | Better algorithmic matching |
| `google_product_category` | Google taxonomy ID | Standard categorization |
| `sale_price` | Decimal + currency | Triggers "SALE" badge (+20% CTR) |
| `custom_label_0` through `custom_label_4` | Any string | Segment products for campaigns |
| `age_group` | Enum | Compliance in regulated categories |
| `gender` | Enum | Better targeting alignment |
| `color` | String | Visual attribute matching |
| `size` | String | Size-specific remarketing |
| `material` | String | Helps with search/discovery |

### Product Feed Best Practices

```
TITLE OPTIMIZATION:
├── Structure: [Brand] + [Product Type] + [Key Attribute] + [Variant]
├── Example: "EcoBrand Organic Cotton T-Shirt - Ocean Blue, M"
├── Include: Brand, product type, material, color, size
├── Exclude: ALL CAPS, excessive punctuation, promotional text
├── Length: 65-150 characters (optimal for display)
└── Impact: Optimized titles improve CTR by 15-30%

IMAGE OPTIMIZATION:
├── Primary image: Product on white/clean background
├── Additional images: Lifestyle, in-use, detail shots
├── Resolution: 800x800px minimum (1200x1200px recommended)
├── Aspect ratio: 1:1 for catalog display
├── No text overlay on product images (TikTok policy)
├── No watermarks or logos on images
└── Impact: High-quality images improve CVR by 20-40%

PRICE ACCURACY:
├── Feed price MUST match landing page price (within 1 hour)
├── Include sale_price when on promotion
├── Currency must match target market
├── Price updates should sync at minimum every 6 hours
└── Impact: Price mismatches = ad disapproval + trust destruction

AVAILABILITY SYNC:
├── Out-of-stock products waste ad spend (clicks to dead ends)
├── Sync inventory at minimum every 4 hours
├── Set up alerts for high-traffic products going OOS
├── Use "preorder" status for upcoming launches
└── Impact: Accurate stock = 10-15% better ROAS
```

### Feed Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| "Invalid image URL" | Image URL returns 404 or is not HTTPS | Use HTTPS CDN URLs, verify accessibility |
| "Price format invalid" | Missing currency or wrong decimal format | Use "29.99 EUR" format (space between value and currency) |
| "Duplicate SKU" | Same sku_id used for multiple products | Ensure unique sku_id per variant |
| "Title too long" | Title exceeds 255 characters | Shorten to essential attributes |
| "Missing required field" | Required field empty or null | Fill all required fields, use "N/A" only where permitted |
| "Image too small" | Image below 500x500px | Re-export at minimum 800x800px |
| "Price mismatch" | Feed price differs from landing page | Sync feed more frequently, check currency |
| "Category not recognized" | Non-standard product_type value | Use Google Product Taxonomy categories |
| Low match rate | Products not showing in ads | Check availability, increase image quality |

---

## Part 3: Video Shopping Ads (VSA)

### VSA Structure

```
┌─────────────────────────────────┐
│                                 │
│         FULL-SCREEN VIDEO       │
│                                 │
│    (15-60 second TikTok ad)     │
│                                 │
│                                 │
│  ┌───────────────────────────┐  │
│  │ 📦 Product Name     €29  │  │
│  │ ⭐ 4.8 (2.1K reviews)   │  │
│  │        [Shop Now]         │  │
│  └───────────────────────────┘  │
│                                 │
│    ♥ 💬 ↗ 🎵                   │
└─────────────────────────────────┘

Product card appears at bottom of video.
Tapping card → Product Detail Page → Checkout
```

### VSA Creative Best Practices

```
VIDEO REQUIREMENTS:
├── Length: 15-60 seconds (optimal: 21-34 seconds)
├── Aspect ratio: 9:16 (full screen vertical)
├── Resolution: 720x1280 minimum (1080x1920 recommended)
├── Show product within first 3 seconds
├── Product must be clearly visible (not blurry/distant)
├── Include at least one close-up product shot
└── End with product in hand/use + verbal CTA

CREATIVE STRUCTURE FOR VSA:
Second 0-2:   Hook (problem statement or product reveal)
Second 3-8:   Product introduction (what it is, why it matters)
Second 9-18:  Demonstration (show product in use)
Second 19-25: Social proof (reviews, results, testimonials)
Second 26-30: CTA + price anchor ("only €29, link below")

TOP-PERFORMING VSA FORMATS:
1. "TikTok Made Me Buy It" review (conversion-focused)
2. Product demo/tutorial (consideration-focused)
3. Before/after transformation (proof-focused)
4. Unboxing experience (excitement-focused)
5. "Found this on TikTok" story (social proof-focused)
```

### VSA Performance Benchmarks

| Metric | Below Average | Average | Good | Excellent |
|--------|--------------|---------|------|-----------|
| ROAS | <2x | 2-4x | 4-7x | >7x |
| CTR | <0.8% | 0.8-1.5% | 1.5-2.5% | >2.5% |
| CVR (from click) | <1% | 1-2.5% | 2.5-5% | >5% |
| Add to Cart Rate | <3% | 3-6% | 6-10% | >10% |
| Product Card Click Rate | <2% | 2-5% | 5-8% | >8% |
| Cost Per Purchase | >€50 | €25-50 | €10-25 | <€10 |

---

## Part 4: Dynamic Showcase Ads (Retargeting)

### How DSA Works

```
USER JOURNEY → DSA RESPONSE:

1. User views product page (pixel fires ViewContent)
   → DSA shows that exact product + similar products

2. User adds to cart (pixel fires AddToCart)
   → DSA shows carted products with urgency messaging

3. User initiates checkout but doesn't complete (pixel fires InitiateCheckout)
   → DSA shows checkout products with "complete your order" CTA

4. User purchased (pixel fires CompletePayment)
   → DSA shows complementary/upsell products

5. User browsed category but no specific product (pixel fires PageView on category)
   → DSA shows top products from that category
```

### DSA Retargeting Windows

| Audience | Window | Creative Angle | Expected ROAS |
|----------|--------|---------------|---------------|
| Viewed product (no action) | 1-7 days | "Still thinking about it?" | 3-6x |
| Viewed product (no action) | 8-14 days | "This is selling fast" | 2-4x |
| Added to cart | 1-3 days | "Your cart is waiting" | 8-15x |
| Added to cart | 4-7 days | "Still available — for now" | 5-10x |
| Initiated checkout | 1-3 days | "Complete your order" + discount | 10-20x |
| Purchased (cross-sell) | 7-30 days | "Customers also bought" | 4-8x |
| Purchased (replenish) | 30-60 days | "Time for a refill?" | 5-10x |

### DSA Setup Requirements

```
PREREQUISITES:
□ TikTok Pixel installed and firing correctly
□ Pixel events configured: ViewContent, AddToCart, InitiateCheckout, CompletePayment
□ Product catalog uploaded and approved (>20 active products)
□ Catalog items match pixel content_id parameter
□ Minimum 1,000 pixel events in last 28 days (for algorithm learning)
□ Custom audience created from pixel events

COMMON ISSUES:
├── "No products to show" → content_id in pixel doesn't match sku_id in catalog
├── "Low delivery" → Retargeting audience too small (<1,000 users)
├── "Products showing wrong" → Catalog not synced, stale product data
└── "High CPC" → Window too long (showing to cold users)
```

---

## Part 5: Collection Ads

### Collection Ad Structure

```
┌─────────────────────────────────┐
│                                 │
│         HERO VIDEO              │
│    (plays automatically)        │
│                                 │
│                                 │
├─────────────────────────────────┤
│  ┌──────┐  ┌──────┐  ┌──────┐  │
│  │ Prod │  │ Prod │  │ Prod │  │
│  │  1   │  │  2   │  │  3   │  │
│  │ €29  │  │ €39  │  │ €19  │  │
│  └──────┘  └──────┘  └──────┘  │
│         Swipe for more →        │
└─────────────────────────────────┘

Tapping any product → Instant Page (in-app) → External site / TikTok Shop
```

### Collection Ad Best Practices

```
HERO VIDEO:
├── Length: 10-30 seconds (shorter is better for collections)
├── Show all gallery products in the video
├── Feature products in lifestyle/use context
├── End with a browse CTA ("Swipe to shop the look")
└── Don't make the video too product-dense (3-4 products max)

PRODUCT GALLERY:
├── 2-6 products (optimal: 4 products)
├── Products should have visual cohesion (same collection/style)
├── Price range should be clear (anchor low and high)
├── Lead with best seller or lowest price
├── Include a mix of price points
└── All products must be in stock

INSTANT PAGE (landing experience):
├── TikTok hosts the page (loads in-app, not external browser)
├── Load time: <1 second (native, not web redirect)
├── Include: Product images, description, price, Add to Cart
├── Customizable layout (TikTok templates available)
├── Can include video embedded in the page
└── Exit to external site for checkout (if not TikTok Shop)
```

### Collection Ad Use Cases

| Use Case | Hero Video Content | Gallery Products | Goal |
|----------|-------------------|-----------------|------|
| "Shop the Look" | Outfit / lifestyle video | Individual items from the look | Cross-sell |
| "New Arrivals" | Season/collection launch video | 4-6 new products | Discovery |
| "Best Sellers" | Compilation of product shots | Top 4-6 sellers | Social proof |
| "Gift Guide" | Gift-giving scenario video | Curated gift options by price | Seasonal |
| "Under €50" | Value-focused lifestyle video | Best products under price point | Conversion |
| "Bundle Deal" | Bundle in use | Individual items + bundle | AOV increase |

---

## Part 6: TikTok Shop Integration

### TikTok Shop vs External Website

| Factor | TikTok Shop | External Website |
|--------|------------|-----------------|
| Checkout friction | Very low (in-app checkout) | Higher (redirect to browser) |
| Conversion rate | 2-4x higher | Baseline |
| Customer data ownership | TikTok owns primary data | You own all data |
| Payment processing | TikTok handles (commission 2-8%) | Your processor |
| Return/refund handling | TikTok policies apply | Your policies |
| Branding control | Limited (TikTok template) | Full control |
| Attribution | Built-in, accurate | Pixel-dependent |
| Organic discovery | Products appear in TikTok Shop tab | No organic TikTok traffic |
| Shipping | TikTok logistics available | Your fulfillment |
| Available markets | US, UK, ID, TH, MY, VN, PH, SG, IE | Global |

### TikTok Shop Setup Requirements

```
ELIGIBILITY:
□ Business registered in supported market
□ Business license or registration document
□ Bank account for payouts
□ Product compliance (no prohibited categories)
□ Minimum inventory and fulfillment capability
□ Agree to TikTok Shop seller terms

SETUP STEPS:
1. Apply at seller-center.tiktok.com
2. Upload business documents for verification (1-3 business days)
3. Set up warehouse and shipping templates
4. Upload products (manual, CSV, or API)
5. Set pricing and promotions
6. Link TikTok Ads Manager account
7. Create first Video Shopping Ad

COMMISSION STRUCTURE (varies by category):
├── Electronics: 3-5%
├── Fashion/Apparel: 5-8%
├── Beauty/Personal Care: 5-8%
├── Home & Garden: 5-8%
├── Food & Beverage: 2-5%
└── General: 5% baseline
```

### TikTok Shop Performance Optimization

```
PRODUCT LISTING OPTIMIZATION:
├── Title: Include search keywords (TikTok Shop has search)
├── Images: 5-9 images per product (includes lifestyle shots)
├── Video: Add product video (listings with video get 2x views)
├── Reviews: Seed with initial reviews (offer samples to early buyers)
├── Price: Competitive within TikTok Shop (users compare easily)
└── Shipping: Offer free shipping if possible (biggest conversion driver)

PROMOTIONS:
├── Flash deals: 24-hour discounts (3-5x traffic increase)
├── Bundle deals: Buy 2+ for discount (AOV increase)
├── Vouchers: Shop-wide or product-specific coupons
├── Free shipping thresholds: Increase AOV
└── Exclusive TikTok pricing: Incentivize in-app purchase
```

---

## Part 7: Product Feed Custom Labels Strategy

### Using Custom Labels for Campaign Segmentation

Custom labels (custom_label_0 through custom_label_4) allow you to segment your catalog for targeted campaigns.

```
RECOMMENDED LABEL STRATEGY:

custom_label_0: PERFORMANCE TIER
├── "bestseller" — Top 20% by revenue
├── "mid-performer" — Middle 60%
├── "slow-mover" — Bottom 20%
└── Use: Allocate more budget to bestseller campaigns

custom_label_1: MARGIN TIER
├── "high-margin" — Gross margin >60%
├── "medium-margin" — Gross margin 30-60%
├── "low-margin" — Gross margin <30%
└── Use: Set ROAS targets by margin (higher margin = lower ROAS acceptable)

custom_label_2: SEASONALITY
├── "spring-summer" — Seasonal products
├── "fall-winter" — Seasonal products
├── "evergreen" — Year-round products
├── "holiday" — Holiday-specific products
└── Use: Activate/deactivate seasonal campaigns automatically

custom_label_3: PRICE RANGE
├── "under-25" — Products under €25
├── "25-50" — Products €25-50
├── "50-100" — Products €50-100
├── "over-100" — Products over €100
└── Use: Tailor creative and targeting by price sensitivity

custom_label_4: PRODUCT TYPE / COLLECTION
├── "new-arrival" — Last 30 days
├── "clearance" — End of lifecycle
├── "core-collection" — Always available
├── "limited-edition" — Scarcity messaging
└── Use: Match messaging to product lifecycle stage
```

### Campaign Structure Using Custom Labels

```
CAMPAIGN: Prospecting (cold audiences)
├── Ad Group 1: Bestsellers, high margin → Aggressive bidding
├── Ad Group 2: New arrivals → Discovery-focused creative
└── Ad Group 3: Core collection → Evergreen creative

CAMPAIGN: Retargeting (warm audiences)
├── Ad Group 1: Viewed products (DSA) → "Still interested?"
├── Ad Group 2: Cart abandoners (DSA) → "Complete your order"
└── Ad Group 3: Past purchasers → Cross-sell complementary products

CAMPAIGN: Seasonal
├── Ad Group 1: Spring-summer products → Seasonal creative
├── Ad Group 2: Holiday products → Gift-guide creative
└── Ad Group 3: Clearance products → Urgency + deep discount
```

---

## Part 8: Measuring Shopping Ad Performance

### Pull Shopping Ad Data

```
tiktok_get_report(
    start_date="2026-03-29",
    end_date="2026-04-05",
    level="ad",
    metrics=["spend", "impressions", "clicks", "conversion",
             "cost_per_conversion", "conversion_rate",
             "total_purchase_value", "total_onsite_shopping_value"]
)
# Note: ROAS is calculated as total_purchase_value / spend.
```

### Shopping-Specific KPIs

| KPI | Formula | Good Benchmark | Action if Below |
|-----|---------|---------------|-----------------|
| ROAS | Revenue / Ad Spend | >3x (prospecting), >6x (retargeting) | Review product selection, creative quality |
| Add-to-Cart Rate | Add to Carts / Clicks | >5% | Improve product page / pricing |
| Cart-to-Purchase Rate | Purchases / Add to Carts | >30% | Fix checkout friction, add urgency |
| Product Card CTR | Product Card Clicks / Impressions | >3% | Improve product card image/price display |
| Average Order Value | Total Revenue / Number of Orders | Above product price (cross-sell working) | Add bundles, recommendations |
| Cost Per Acquisition | Ad Spend / Purchases | <30% of AOV | Optimize targeting, creative, product mix |
| Catalog Match Rate | Matched Products / Total Products | >90% | Fix feed errors, update sku_ids |

### Product-Level Optimization

Identify your best and worst performing products:

```
PRODUCT PERFORMANCE QUADRANT:

             HIGH ROAS
                │
    SCALE UP    │    CASH COWS
    (high ROAS, │    (high ROAS,
     low spend) │    high spend)
                │
   ─────────────┼─────────────── HIGH SPEND
                │
    CUT/FIX     │    REVIEW
    (low ROAS,  │    (low ROAS,
     low spend) │    high spend)
                │
             LOW ROAS

Action by quadrant:
├── Cash Cows: Maintain, protect, increase budget cautiously
├── Scale Up: Increase budget, promote to collection ads hero
├── Review: Test new creative, check product page, fix pricing
└── Cut/Fix: Pause if ROAS <1x, fix feed issues, or remove from catalog
```

---

## Quick Reference: Shopping Ads Setup Checklist

1. Choose shopping format(s) based on goal and product count
2. Set up product catalog with all required fields
3. Upload additional images and optimized titles
4. Configure custom labels for campaign segmentation
5. Install and verify TikTok Pixel (ViewContent, AddToCart, InitiateCheckout, CompletePayment)
6. Verify pixel content_id matches catalog sku_id
7. Create product sets using custom labels
8. Set up prospecting campaign (Collection or VSA with bestsellers)
9. Set up retargeting campaign (DSA with pixel audiences, 1-7 day windows)
10. Monitor catalog health daily, product performance weekly, ROAS continuously
