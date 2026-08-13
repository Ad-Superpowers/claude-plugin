---
name: ga4-bigquery-export
description: "This skill should be used when the user asks to \"export GA4 to BigQuery\", \"query raw GA4 event data\", \"set up BigQuery linking\", or mentions \"GA4 data warehouse\", \"BigQuery dashboard\", or \"unsampled GA4 data\". Do NOT use for: GA4 Data API reporting (use ga4-api-reporting), standard GA4 UI reports (use ga4-revenue-analysis)."
---
# GA4 BigQuery Export Guide

Complete guide for configuring BigQuery export and analyzing GA4 raw event data.

## Quick Decision Tree

```
GA4 BIGQUERY EXPORT FLOW
│
├─► DO YOU NEED BIGQUERY?
│   ├─► YES, if you need:
│   │   ├─► Raw event-level data
│   │   ├─► Custom attribution models
│   │   ├─► Unsampled data
│   │   ├─► Data joins with other sources
│   │   ├─► ML/AI analyses
│   │   └─► Long-term data storage
│   │
│   └─► NO, GA4 UI is sufficient if:
│       ├─► Standard reports suffice
│       ├─► Exploration capabilities are enough
│       └─► No external data joins needed
│
├─► WHICH EXPORT TYPE?
│   ├─► Daily export (free)
│   │   └─► Data available next day
│   │
│   ├─► Streaming export (GA360)
│   │   └─► Real-time data (within minutes)
│   │
│   └─► Fresh daily export (GA360)
│       └─► Multiple times per day
│
└─► COST CONSIDERATIONS?
    ├─► GA4 daily export itself: FREE (no GA360 needed)
    ├─► BigQuery storage: ~$0.02/GB/month (GCP cost, not GA4)
    ├─► Queries: $5/TB scanned (on-demand) or flat rate
    └─► Optimize with partitioning to reduce query costs
```

## Configuring BigQuery Export

```
BIGQUERY LINKING SETUP
======================

PREREQUISITES:
├── Google Cloud Project with billing enabled
├── BigQuery API enabled
├── GA4 property Editor or Admin access
└── BigQuery Admin permissions in GCP project

STEP 1: PREPARE GCP PROJECT
────────────────────────────
1. Go to console.cloud.google.com
2. Create project or select existing project
3. Enable BigQuery API:
   └── APIs & Services → Enable APIs → BigQuery API

4. Billing setup (required for export)

STEP 2: CREATE GA4 BIGQUERY LINK
─────────────────────────────────
LOCATION: GA4 Admin → Product Links → BigQuery Links

┌────┬────────────────────────────────────────────────────────────────┐
│ 1  │ Click "Link"                                                   │
├────┼────────────────────────────────────────────────────────────────┤
│ 2  │ Select Google Cloud project                                    │
├────┼────────────────────────────────────────────────────────────────┤
│ 3  │ Choose data location (EU/US) - CANNOT be changed later!       │
├────┼────────────────────────────────────────────────────────────────┤
│ 4  │ Select data streams to export                                  │
├────┼────────────────────────────────────────────────────────────────┤
│ 5  │ Choose export frequency:                                       │
│    │ ├── Daily (free, recommended to start)                         │
│    │ └── Streaming (GA360 only)                                     │
├────┼────────────────────────────────────────────────────────────────┤
│ 6  │ Include advertising ID (optional, for app data)                │
├────┼────────────────────────────────────────────────────────────────┤
│ 7  │ Click "Submit"                                                  │
└────┴────────────────────────────────────────────────────────────────┘

IMPORTANT:
├── Data location (EU/US) CANNOT be changed
├── Choose the SAME region as other data for joins
├── Export usually starts within 24 hours
└── Historical data is NOT exported
```

## BigQuery Dataset Structure

```
GA4 BIGQUERY DATASET STRUCTURE
===============================

DATASET NAME FORMAT:
analytics_[PROPERTY_ID]

TABLES:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Table                   │ Description                              │
├─────────────────────────┼──────────────────────────────────────────┤
│ events_YYYYMMDD         │ Daily export table (partitioned)         │
├─────────────────────────┼──────────────────────────────────────────┤
│ events_intraday_YYYYMMDD│ Streaming export (GA360)                 │
├─────────────────────────┼──────────────────────────────────────────┤
│ pseudonymous_users_*    │ User data export (if enabled)            │
└─────────────────────────┴──────────────────────────────────────────┘

TABLE SCHEMA (SIMPLIFIED):
──────────────────────────
┌─────────────────────────┬───────────┬────────────────────────────────┐
│ Column                  │ Type      │ Description                    │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ event_date              │ STRING    │ Date (YYYYMMDD)                │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ event_timestamp         │ INTEGER   │ Unix timestamp (microseconds)  │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ event_name              │ STRING    │ Event name (page_view, etc.)   │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ event_params            │ RECORD    │ REPEATED - Event parameters    │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ user_id                 │ STRING    │ Custom user ID (if set)        │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ user_pseudo_id          │ STRING    │ GA4 client ID                  │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ user_properties         │ RECORD    │ REPEATED - User properties     │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ device                  │ RECORD    │ Device info (category, etc.)   │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ geo                     │ RECORD    │ Geo info (country, city)       │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ traffic_source          │ RECORD    │ Session traffic source         │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ ecommerce               │ RECORD    │ E-commerce data                │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ items                   │ RECORD    │ REPEATED - Product items       │
└─────────────────────────┴───────────┴────────────────────────────────┘
```

## Basic Query Examples

```sql
-- ============================================
-- GA4 BIGQUERY BASIC QUERIES
-- ============================================

-- 1. COUNT EVENTS PER DAY
-- ───────────────────────
SELECT
  event_date,
  event_name,
  COUNT(*) as event_count
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
GROUP BY
  event_date, event_name
ORDER BY
  event_date, event_count DESC;

-- 2. UNIQUE USERS PER DAY
-- ───────────────────────
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) as unique_users
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
GROUP BY
  event_date
ORDER BY
  event_date;

-- 3. PAGE VIEWS WITH PAGE LOCATION
-- ─────────────────────────────────
SELECT
  event_date,
  (SELECT value.string_value
   FROM UNNEST(event_params)
   WHERE key = 'page_location') as page_url,
  COUNT(*) as pageviews
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'page_view'
GROUP BY
  event_date, page_url
ORDER BY
  pageviews DESC
LIMIT 100;

-- 4. EXTRACT EVENT PARAMETERS
-- ───────────────────────────
SELECT
  event_date,
  event_name,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_title') as page_title,
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'engagement_time_msec') as engagement_time,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'session_engaged') as session_engaged
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX = '20240115'
  AND event_name = 'page_view'
LIMIT 100;
```

## E-commerce Queries

```sql
-- ============================================
-- GA4 BIGQUERY E-COMMERCE QUERIES
-- ============================================

-- 1. PURCHASE TRANSACTIONS
-- ────────────────────────
SELECT
  event_date,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'transaction_id') as transaction_id,
  ecommerce.purchase_revenue as revenue,
  ecommerce.total_item_quantity as items_qty,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'coupon') as coupon_code
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'purchase'
ORDER BY
  event_date DESC;

-- 2. PRODUCT PERFORMANCE
-- ──────────────────────
SELECT
  items.item_name,
  items.item_brand,
  items.item_category,
  SUM(items.quantity) as total_quantity,
  SUM(items.item_revenue) as total_revenue,
  COUNT(DISTINCT
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'transaction_id')
  ) as transaction_count
FROM
  `project.analytics_XXXXXX.events_*`,
  UNNEST(items) as items
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'purchase'
GROUP BY
  items.item_name, items.item_brand, items.item_category
ORDER BY
  total_revenue DESC
LIMIT 50;

-- 3. CHECKOUT FUNNEL ANALYSIS
-- ───────────────────────────
WITH funnel_events AS (
  SELECT
    user_pseudo_id,
    event_name,
    event_timestamp
  FROM
    `project.analytics_XXXXXX.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
    AND event_name IN ('view_cart', 'begin_checkout', 'add_shipping_info', 'add_payment_info', 'purchase')
)
SELECT
  event_name,
  COUNT(DISTINCT user_pseudo_id) as users
FROM
  funnel_events
GROUP BY
  event_name
ORDER BY
  CASE event_name
    WHEN 'view_cart' THEN 1
    WHEN 'begin_checkout' THEN 2
    WHEN 'add_shipping_info' THEN 3
    WHEN 'add_payment_info' THEN 4
    WHEN 'purchase' THEN 5
  END;

-- 4. REVENUE PER TRAFFIC SOURCE
-- ─────────────────────────────
SELECT
  traffic_source.source,
  traffic_source.medium,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNT(DISTINCT
    CASE WHEN event_name = 'purchase'
    THEN (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'transaction_id')
    END
  ) as transactions,
  SUM(
    CASE WHEN event_name = 'purchase'
    THEN ecommerce.purchase_revenue
    ELSE 0 END
  ) as total_revenue
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
GROUP BY
  traffic_source.source, traffic_source.medium
ORDER BY
  total_revenue DESC;
```

## User Journey Queries

```sql
-- ============================================
-- GA4 BIGQUERY USER JOURNEY QUERIES
-- ============================================

-- 1. USER PATH TO PURCHASE
-- ────────────────────────
WITH purchase_users AS (
  SELECT DISTINCT user_pseudo_id
  FROM `project.analytics_XXXXXX.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
    AND event_name = 'purchase'
),
user_events AS (
  SELECT
    e.user_pseudo_id,
    e.event_name,
    e.event_timestamp,
    ROW_NUMBER() OVER (PARTITION BY e.user_pseudo_id ORDER BY e.event_timestamp) as event_sequence
  FROM `project.analytics_XXXXXX.events_*` e
  INNER JOIN purchase_users p ON e.user_pseudo_id = p.user_pseudo_id
  WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
)
SELECT
  event_sequence,
  event_name,
  COUNT(*) as occurrences
FROM user_events
WHERE event_sequence <= 10
GROUP BY event_sequence, event_name
ORDER BY event_sequence, occurrences DESC;

-- 2. TIME TO CONVERSION
-- ─────────────────────
WITH first_visit AS (
  SELECT
    user_pseudo_id,
    MIN(event_timestamp) as first_timestamp
  FROM `project.analytics_XXXXXX.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  GROUP BY user_pseudo_id
),
purchases AS (
  SELECT
    user_pseudo_id,
    MIN(event_timestamp) as purchase_timestamp
  FROM `project.analytics_XXXXXX.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
    AND event_name = 'purchase'
  GROUP BY user_pseudo_id
)
SELECT
  CASE
    WHEN time_to_purchase_hours < 1 THEN '< 1 hour'
    WHEN time_to_purchase_hours < 24 THEN '1-24 hours'
    WHEN time_to_purchase_hours < 168 THEN '1-7 days'
    WHEN time_to_purchase_hours < 720 THEN '7-30 days'
    ELSE '> 30 days'
  END as time_bucket,
  COUNT(*) as conversions
FROM (
  SELECT
    f.user_pseudo_id,
    (p.purchase_timestamp - f.first_timestamp) / 3600000000 as time_to_purchase_hours
  FROM first_visit f
  INNER JOIN purchases p ON f.user_pseudo_id = p.user_pseudo_id
)
GROUP BY time_bucket
ORDER BY
  CASE time_bucket
    WHEN '< 1 hour' THEN 1
    WHEN '1-24 hours' THEN 2
    WHEN '1-7 days' THEN 3
    WHEN '7-30 days' THEN 4
    ELSE 5
  END;

-- 3. SESSION RECONSTRUCTION
-- ─────────────────────────
SELECT
  user_pseudo_id,
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') as session_id,
  MIN(TIMESTAMP_MICROS(event_timestamp)) as session_start,
  MAX(TIMESTAMP_MICROS(event_timestamp)) as session_end,
  COUNT(*) as event_count,
  COUNTIF(event_name = 'page_view') as pageviews,
  MAX(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) as converted
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX = '20240115'
GROUP BY
  user_pseudo_id, session_id
ORDER BY
  session_start DESC
LIMIT 100;
```

## Query Optimization Tips

```
BIGQUERY COST OPTIMIZATION
============================

USE PARTITIONING:
─────────────────
GOOD - Specific date suffix:
WHERE _TABLE_SUFFIX = '20240115'

GOOD - Date range with suffix:
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'

BAD - Scans ALL tables:
WHERE event_date = '2024-01-15'  -- Scans ALL tables!

COLUMN SELECTION:
─────────────────
GOOD - Specific columns:
SELECT event_name, event_date, user_pseudo_id

BAD - All columns:
SELECT * FROM events_*

EFFICIENT NESTED FIELDS:
────────────────────────
-- Unnest ONLY when needed
-- Use subquery for event_params

GOOD:
SELECT
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_title')

LESS EFFICIENT:
SELECT ep.value.string_value
FROM events, UNNEST(event_params) as ep
WHERE ep.key = 'page_title'

CACHING AND MATERIALIZED VIEWS:
────────────────────────────────
-- Create materialized view for frequently used queries

CREATE MATERIALIZED VIEW `project.dataset.daily_metrics`
AS
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNTIF(event_name = 'purchase') as purchases
FROM `project.analytics_XXXXXX.events_*`
WHERE _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
GROUP BY event_date;

COST ESTIMATION:
────────────────
┌─────────────────────┬──────────────────────────────────────────────┐
│ Table size           │ Estimated monthly cost                       │
├─────────────────────┼──────────────────────────────────────────────┤
│ 10 GB/month         │ Storage: ~$0.20 + Queries: variable          │
├─────────────────────┼──────────────────────────────────────────────┤
│ 100 GB/month        │ Storage: ~$2.00 + Queries: variable          │
├─────────────────────┼──────────────────────────────────────────────┤
│ 1 TB/month          │ Storage: ~$20.00 + Queries: variable         │
└─────────────────────┴──────────────────────────────────────────────┘

Query costs: $5 per TB scanned (on-demand pricing)
```

## Looker Studio Integration

```
BIGQUERY → LOOKER STUDIO
=========================

CREATING CONNECTION:
────────────────────
1. Go to lookerstudio.google.com
2. Create → Data source → BigQuery
3. Select project → dataset → table
4. (Optional) Use custom query

CUSTOM QUERY DATA SOURCE:
─────────────────────────
Advantages:
├── Pre-aggregated data (faster)
├── Complex calculations
├── Joins with other sources
└── Lower query costs

Example:
SELECT
  event_date,
  traffic_source.source,
  traffic_source.medium,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNTIF(event_name = 'purchase') as purchases,
  SUM(CASE WHEN event_name = 'purchase' THEN ecommerce.purchase_revenue END) as revenue
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
GROUP BY
  event_date, traffic_source.source, traffic_source.medium

PARAMETER IN QUERY (Date range):
─────────────────────────────────
SELECT *
FROM `project.analytics_XXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', @DS_START_DATE)
  AND FORMAT_DATE('%Y%m%d', @DS_END_DATE)

BLENDING WITH OTHER DATA:
─────────────────────────
├── Blend GA4 BQ data with CRM data
├── Join with ad spend data
├── Combine with product database
└── Match with offline sales
```

## Common Problems

```
TROUBLESHOOTING BIGQUERY EXPORT
================================

PROBLEM: No data in BigQuery
─────────────────────────────
Causes:
├── Link just created (wait 24-48 hours)
├── Wrong project selected
├── BigQuery API not enabled
├── Billing not active
└── No events in GA4

Solution:
├── Wait at least 24 hours after linking
├── Verify correct GCP project
├── Check BigQuery API status
├── Verify billing is enabled
└── Verify GA4 is receiving data

PROBLEM: Discrepancy GA4 UI vs BigQuery
────────────────────────────────────────
Causes:
├── Sampling in GA4 UI
├── Data processing timing
├── Session definitions differ
├── Consent mode differences
└── Timezone differences

Solution:
├── BQ has RAW data (no sampling)
├── Compare same time periods
├── Use same session definition
├── Filter on consent_granted if needed
├── Match timezones in queries

PROBLEM: Queries too expensive
──────────────────────────────
Causes:
├── Too broad date ranges
├── Using SELECT *
├── Inefficient UNNEST
├── No partitioning filter
└── Repeated queries

Solution:
├── Specific date suffixes
├── Select only needed columns
├── Use subqueries for nested data
├── ALWAYS use _TABLE_SUFFIX filter
├── Create scheduled queries/views

PROBLEM: Event parameters missing
──────────────────────────────────
Causes:
├── Custom events not correctly implemented
├── Parameter registration in GA4 admin
├── Data processing delay
└── Wrong parameter name

Solution:
├── Verify event in GA4 DebugView
├── Check custom dimensions setup
├── Wait for full processing
├── Query all available keys:

-- Find all event parameter keys:
SELECT DISTINCT
  ep.key
FROM
  `project.analytics_XXXXXX.events_*`,
  UNNEST(event_params) as ep
WHERE
  _TABLE_SUFFIX = '20240115'
  AND event_name = 'your_event'
```

## Output: BigQuery Setup Report Template

```markdown
# GA4 BigQuery Export Setup Report

## Configuration Details

| Setting | Value |
|---------|-------|
| GA4 Property ID | XXXXXXXXX |
| GCP Project ID | [project-id] |
| BigQuery Dataset | analytics_XXXXXXXXX |
| Data Location | EU / US |
| Export Type | Daily / Streaming |
| Link Date | [Date] |

## Exported Data Streams

| Stream Name | Measurement ID | Status |
|-------------|----------------|--------|
| Web - example.com | G-XXXXXXXXXX | Active |
| iOS App | [ID] | Active |
| Android App | [ID] | Pending |

## Table Availability

| Table Type | First Date | Last Date | Status |
|------------|------------|-----------|--------|
| events_YYYYMMDD | 2024-01-15 | [Yesterday] | Active |
| events_intraday | N/A | N/A | Not activated |

## Schema Verification

| Field | Present | Data Type |
|-------|---------|-----------|
| event_date | ✅ | STRING |
| event_name | ✅ | STRING |
| event_params | ✅ | RECORD |
| user_pseudo_id | ✅ | STRING |
| ecommerce | ✅ | RECORD |
| items | ✅ | RECORD |

## Query Templates Delivered

- [ ] Daily metrics query
- [ ] E-commerce performance query
- [ ] User journey query
- [ ] Checkout funnel query
- [ ] Traffic source revenue query

## Cost Estimate

| Component | Estimated Monthly Cost |
|-----------|----------------------|
| Storage (~XX GB) | $X.XX |
| Queries (estimated) | $XX.XX |
| **Total** | **$XX.XX** |

## Looker Studio Integration

| Dashboard | Data Source | Status |
|-----------|-------------|--------|
| [Dashboard name] | BQ Custom Query | Active |

## Next Steps

1. [ ] Create materialized views for frequently used queries
2. [ ] Set up scheduled queries for daily exports
3. [ ] Configure data retention policy
4. [ ] Configure team access

## Notes

[Any additional remarks or points of attention]
```

## Optional: Enrich with Live Data

If the user has connected their GA4 account, check current data volume to estimate BigQuery export size and costs before enabling:

```python
# Check session and event volume to project daily BQ export row count
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["sessions", "eventCount", "totalUsers"],
    dimensions=["date"],
    start_date="7daysAgo",
    end_date="today"
)
```

Multiply average daily `eventCount` by ~3-5 (BQ exports one row per event hit) to estimate rows/day. This determines whether to use daily export (standard) or streaming export (real-time, higher cost).
