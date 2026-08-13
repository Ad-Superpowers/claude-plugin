---
name: ga4-api-reporting
description: "This skill should be used when the user asks to \"use the GA4 Data API\", \"build automated reports\", \"create a custom GA4 dashboard\", or mentions \"GA4 API quotas\", \"data extraction scripts\", or \"programmatic GA4 reporting\". Do NOT use for: GA4 UI reports (use ga4-revenue-analysis), BigQuery raw data (use ga4-bigquery-export), event tracking setup (use ga4-event-tracking-setup)."
---
# GA4 Data API Reporting Guide

Complete guide for using the GA4 Data API for custom reporting and automated dashboards.

## Quick Note: Ad Superpowers MCP Tool

The Ad Superpowers MCP server wraps the GA4 Data API into the `ga4_run_report()` tool, which handles authentication and pagination automatically. Use it for ad-hoc analysis before building custom API integrations:

```python
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["sessions", "activeUsers", "keyEvents"],
    dimensions=["date", "sessionDefaultChannelGroup"],
    start_date="30daysAgo",
    end_date="yesterday"
)
```

For programmatic/automated reporting, use the GA4 Data API v1 (v1beta) directly as documented below. The API base URL is `analyticsdata.googleapis.com/v1beta/` — no v2 exists as of 2026.

## Available Metrics & Dimensions

```
COMMONLY USED DIMENSIONS
=========================

USER & SESSION:
├── userId (custom user ID)
├── userAgeBracket
├── userGender
├── newVsReturning
├── sessionSource
├── sessionMedium
├── sessionSourceMedium
├── sessionCampaignName
└── sessionDefaultChannelGroup

TIME:
├── date (YYYYMMDD)
├── dateHour
├── dateHourMinute
├── dayOfWeek
├── hour
├── month
└── year

PAGE & SCREEN:
├── pagePath
├── pageTitle
├── pagePathPlusQueryString
├── landingPage
├── exitPage
└── screenName

DEVICE & GEO:
├── deviceCategory
├── platform
├── browser
├── operatingSystem
├── country
├── city
└── region

E-COMMERCE:
├── itemName
├── itemId
├── itemBrand
├── itemCategory
├── transactionId
└── orderCoupon

COMMONLY USED METRICS
======================

USERS & SESSIONS:
├── activeUsers
├── newUsers
├── totalUsers
├── sessions
├── sessionsPerUser
├── engagedSessions
├── averageSessionDuration
└── bounceRate

ENGAGEMENT:
├── screenPageViews
├── screenPageViewsPerSession
├── eventCount
├── engagementRate
└── userEngagementDuration

E-COMMERCE:
├── ecommercePurchases
├── transactions
├── purchaseRevenue
├── totalRevenue
├── averagePurchaseRevenue
├── itemsPurchased
├── itemRevenue
└── itemsViewed

KEY EVENTS (CONVERSIONS):
├── keyEvents (current metric name — was "conversions" before March 2024, both still work in API)
├── keyEventRate
├── eventValue
└── [customEvent]:eventCount

FULL LIST:
──────────
developers.google.com/analytics/devguides/reporting/data/v1/api-schema
```

## Automated Reporting Setup

```
AUTOMATED REPORTING
====================

OPTION 1: CLOUD FUNCTIONS + SCHEDULER
──────────────────────────────────────
# requirements.txt
google-analytics-data
google-cloud-storage
pandas

# main.py
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.cloud import storage
import pandas as pd
import json
from datetime import datetime

def daily_ga4_report(event, context):
    client = BetaAnalyticsDataClient()
    property_id = "YOUR_PROPERTY_ID"

    response = client.run_report(
        property=f"properties/{property_id}",
        dimensions=[{"name": "date"}, {"name": "sessionSourceMedium"}],
        metrics=[{"name": "sessions"}, {"name": "keyEvents"}],  # "keyEvents" is the current metric name (was "conversions" pre-2024)
        date_ranges=[{"start_date": "yesterday", "end_date": "yesterday"}]
    )

    # Convert to DataFrame
    rows = []
    for row in response.rows:
        rows.append({
            "date": row.dimension_values[0].value,
            "source_medium": row.dimension_values[1].value,
            "sessions": row.metric_values[0].value,
            "key_events": row.metric_values[1].value,
        })
    df = pd.DataFrame(rows)

    # Save to Cloud Storage
    bucket_name = "your-bucket"
    blob_name = f"ga4-reports/{datetime.now().strftime('%Y-%m-%d')}.csv"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')

    return "Report generated successfully"

# Cloud Scheduler setup:
# gcloud scheduler jobs create http daily-ga4-report \
#   --schedule="0 6 * * *" \
#   --uri="YOUR_CLOUD_FUNCTION_URL" \
#   --http-method=POST

OPTION 2: GITHUB ACTIONS
─────────────────────────
# .github/workflows/ga4-report.yml
name: Daily GA4 Report

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6:00 UTC
  workflow_dispatch:

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install google-analytics-data pandas

      - name: Create credentials file
        run: echo '${{ secrets.GA4_CREDENTIALS }}' > credentials.json

      - name: Run report
        env:
          GOOGLE_APPLICATION_CREDENTIALS: credentials.json
        run: python scripts/generate_report.py

      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: ga4-report
          path: output/*.csv

OPTION 3: AIRFLOW DAG
─────────────────────
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'analytics',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'ga4_daily_report',
    default_args=default_args,
    schedule_interval='0 6 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    def extract_ga4_data(**context):
        # GA4 API logic here
        pass

    def transform_data(**context):
        # Transform logic here
        pass

    def load_to_warehouse(**context):
        # Load to database/warehouse
        pass

    extract = PythonOperator(
        task_id='extract_ga4_data',
        python_callable=extract_ga4_data,
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id='load_to_warehouse',
        python_callable=load_to_warehouse,
    )

    extract >> transform >> load
```

## Output: API Integration Report Template

```markdown
# GA4 Data API Integration Report

## Configuration Details

| Setting | Value |
|---------|-------|
| GA4 Property ID | XXXXXXXXX |
| GCP Project ID | [project-id] |
| Service Account | [email]@[project].iam.gserviceaccount.com |
| API Version | v1beta (current as of 2026, no v2) |
| Setup Date | [Date] |

## Authentication Status

| Check | Status |
|-------|--------|
| Service Account created | ✅ |
| JSON key downloaded | ✅ |
| GA4 Viewer access granted | ✅ |
| Analytics Data API enabled | ✅ |
| Test query successful | ✅ |

## Implemented Reports

| Report Name | Dimensions | Metrics | Schedule |
|-------------|------------|---------|----------|
| Daily Traffic | date, sourceMedium | sessions, users | Daily 06:00 |
| E-commerce | date, itemCategory | revenue, transactions | Daily 07:00 |
| Realtime Dashboard | country | activeUsers | Every 5 min |

## Quota Usage

| Quota Type | Used | Limit | % Used |
|------------|------|-------|--------|
| Requests/day | X,XXX | 200,000 | X% |
| Tokens/day | XX,XXX | 1,750,000 | X% |
| Concurrent | X | 10 | X% |

## Data Output Locations

| Output | Type | Location |
|--------|------|----------|
| Raw exports | CSV | gs://bucket/ga4-exports/ |
| Dashboard data | BigQuery | project.dataset.ga4_reports |
| Looker Studio | Connector | [Dashboard URL] |

## Code Repository

```
/scripts
├── ga4_daily_report.py
├── ga4_ecommerce_report.py
├── requirements.txt
└── README.md
```

## Monitoring & Alerting

- [ ] Quota alerts configured
- [ ] Error notifications (email/Slack)
- [ ] Scheduled job monitoring
- [ ] Data freshness checks

## Next Steps

1. [ ] [Next action]
2. [ ] [Next action]
3. [ ] [Next action]

## Notes

[Any additional remarks]
```
