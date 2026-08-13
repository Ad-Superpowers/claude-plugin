## API Setup & Authentication

```
GA4 DATA API SETUP
==================

STEP 1: CONFIGURE GCP PROJECT
──────────────────────────────
1. Go to console.cloud.google.com
2. Create new project or select existing
3. Enable APIs:
   └── APIs & Services → Enable APIs
       └── "Google Analytics Data API"

STEP 2: CREATE SERVICE ACCOUNT
──────────────────────────────
1. IAM & Admin → Service Accounts
2. Create Service Account:
   ├── Name: ga4-reporting-service
   └── Description: GA4 Data API access

3. Create Key:
   ├── Keys tab → Add Key → Create new key
   ├── Key type: JSON
   └── Download and store securely!

STEP 3: GRANT GA4 ACCESS
─────────────────────────
1. Go to GA4 Admin → Property Access Management
2. Add Users → Add service account email
   └── Email format: <name>@<project-id>.iam.gserviceaccount.com
3. Role: Viewer (for read-only API access)

AUTHENTICATION OPTIONS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Method                  │ Use Case                                 │
├─────────────────────────┼──────────────────────────────────────────┤
│ Service Account (JSON)  │ Server-to-server, automated scripts     │
├─────────────────────────┼──────────────────────────────────────────┤
│ OAuth 2.0               │ User-facing apps, interactive access    │
├─────────────────────────┼──────────────────────────────────────────┤
│ API Key                 │ NOT supported for GA4 Data API          │
└─────────────────────────┴──────────────────────────────────────────┘
```

## Python Implementation

```python
# ============================================
# GA4 DATA API - PYTHON EXAMPLES
# ============================================

# INSTALLATION:
# pip install google-analytics-data

# BASIC SETUP
# ───────────
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest,
    DateRange,
    Dimension,
    Metric,
    FilterExpression,
    Filter,
)
import os

# Authentication via environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/service-account.json"

# Or via explicit credentials
# from google.oauth2 import service_account
# credentials = service_account.Credentials.from_service_account_file('key.json')
# client = BetaAnalyticsDataClient(credentials=credentials)

client = BetaAnalyticsDataClient()
property_id = "YOUR_PROPERTY_ID"  # Numeric ID only, no "properties/" prefix


# EXAMPLE 1: BASIC REPORT
# ────────────────────────
def get_basic_report():
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="date"),
            Dimension(name="country"),
        ],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="sessions"),
            Metric(name="screenPageViews"),
        ],
        date_ranges=[
            DateRange(start_date="30daysAgo", end_date="yesterday")
        ],
    )

    response = client.run_report(request)

    # Process response
    for row in response.rows:
        date = row.dimension_values[0].value
        country = row.dimension_values[1].value
        users = row.metric_values[0].value
        sessions = row.metric_values[1].value
        pageviews = row.metric_values[2].value
        print(f"{date} | {country} | Users: {users} | Sessions: {sessions}")

    return response


# EXAMPLE 2: E-COMMERCE REPORT
# ─────────────────────────────
def get_ecommerce_report():
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="date"),
            Dimension(name="sessionSourceMedium"),
        ],
        metrics=[
            Metric(name="ecommercePurchases"),
            Metric(name="purchaseRevenue"),
            Metric(name="averagePurchaseRevenue"),
            Metric(name="transactions"),
        ],
        date_ranges=[
            DateRange(start_date="30daysAgo", end_date="yesterday")
        ],
        order_bys=[
            {"metric": {"metric_name": "purchaseRevenue"}, "desc": True}
        ],
        limit=50,
    )

    return client.run_report(request)


# EXAMPLE 3: FILTERED REPORT
# ───────────────────────────
def get_filtered_report():
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="pagePath"),
        ],
        metrics=[
            Metric(name="screenPageViews"),
            Metric(name="averageSessionDuration"),
        ],
        date_ranges=[
            DateRange(start_date="7daysAgo", end_date="yesterday")
        ],
        dimension_filter=FilterExpression(
            filter=Filter(
                field_name="pagePath",
                string_filter=Filter.StringFilter(
                    match_type=Filter.StringFilter.MatchType.CONTAINS,
                    value="/products/"
                )
            )
        ),
    )

    return client.run_report(request)


# EXAMPLE 4: REALTIME REPORT
# ───────────────────────────
def get_realtime_report():
    from google.analytics.data_v1beta.types import RunRealtimeReportRequest

    request = RunRealtimeReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="country"),
            Dimension(name="city"),
        ],
        metrics=[
            Metric(name="activeUsers"),
        ],
    )

    return client.run_realtime_report(request)


# EXAMPLE 5: EXPORT TO PANDAS
# ────────────────────────────
def export_to_dataframe():
    import pandas as pd

    response = get_basic_report()

    # Extract data
    rows = []
    for row in response.rows:
        rows.append({
            "date": row.dimension_values[0].value,
            "country": row.dimension_values[1].value,
            "users": int(row.metric_values[0].value),
            "sessions": int(row.metric_values[1].value),
            "pageviews": int(row.metric_values[2].value),
        })

    df = pd.DataFrame(rows)
    return df
```

## JavaScript/Node.js Implementation

```javascript
// ============================================
// GA4 DATA API - NODE.JS EXAMPLES
// ============================================

// INSTALLATION:
// npm install @google-analytics/data

const { BetaAnalyticsDataClient } = require('@google-analytics/data');

// Authentication via environment variable
// GOOGLE_APPLICATION_CREDENTIALS=path/to/key.json

const analyticsDataClient = new BetaAnalyticsDataClient();
const propertyId = 'YOUR_PROPERTY_ID';


// EXAMPLE 1: BASIC REPORT
// ────────────────────────
async function runBasicReport() {
  const [response] = await analyticsDataClient.runReport({
    property: `properties/${propertyId}`,
    dateRanges: [
      {
        startDate: '30daysAgo',
        endDate: 'yesterday',
      },
    ],
    dimensions: [
      { name: 'date' },
      { name: 'country' },
    ],
    metrics: [
      { name: 'activeUsers' },
      { name: 'sessions' },
    ],
  });

  console.log('Report result:');
  response.rows.forEach(row => {
    console.log(
      row.dimensionValues[0].value,
      row.dimensionValues[1].value,
      row.metricValues[0].value,
      row.metricValues[1].value
    );
  });

  return response;
}


// EXAMPLE 2: E-COMMERCE DATA
// ──────────────────────────
async function runEcommerceReport() {
  const [response] = await analyticsDataClient.runReport({
    property: `properties/${propertyId}`,
    dateRanges: [
      { startDate: '7daysAgo', endDate: 'yesterday' },
    ],
    dimensions: [
      { name: 'itemName' },
      { name: 'itemCategory' },
    ],
    metrics: [
      { name: 'itemsPurchased' },
      { name: 'itemRevenue' },
    ],
    orderBys: [
      { metric: { metricName: 'itemRevenue' }, desc: true },
    ],
    limit: 20,
  });

  return response;
}


// EXAMPLE 3: WITH FILTERS
// ────────────────────────
async function runFilteredReport() {
  const [response] = await analyticsDataClient.runReport({
    property: `properties/${propertyId}`,
    dateRanges: [
      { startDate: '30daysAgo', endDate: 'yesterday' },
    ],
    dimensions: [
      { name: 'sessionSourceMedium' },
    ],
    metrics: [
      { name: 'sessions' },
      { name: 'conversions' },
    ],
    dimensionFilter: {
      filter: {
        fieldName: 'sessionSourceMedium',
        stringFilter: {
          matchType: 'CONTAINS',
          value: 'google',
        },
      },
    },
  });

  return response;
}


// EXAMPLE 4: REALTIME DATA
// ────────────────────────
async function runRealtimeReport() {
  const [response] = await analyticsDataClient.runRealtimeReport({
    property: `properties/${propertyId}`,
    dimensions: [
      { name: 'country' },
    ],
    metrics: [
      { name: 'activeUsers' },
    ],
  });

  return response;
}


// Run
runBasicReport().catch(console.error);
```

## Google Sheets Integration

```
GA4 DATA API IN GOOGLE SHEETS
==============================

METHOD 1: GA4 DATA EXPORT ADD-ON
─────────────────────────────────
1. Extensions → Add-ons → Get add-ons
2. Search for "GA4 Reports" or "Supermetrics"
3. Install and authorize
4. Configure report queries

METHOD 2: APPS SCRIPT (CUSTOM)
───────────────────────────────
// In Google Sheets: Extensions → Apps Script

function getGA4Data() {
  const propertyId = 'YOUR_PROPERTY_ID';

  const request = {
    "dateRanges": [{
      "startDate": "30daysAgo",
      "endDate": "yesterday"
    }],
    "dimensions": [
      {"name": "date"},
      {"name": "sessionSourceMedium"}
    ],
    "metrics": [
      {"name": "sessions"},
      {"name": "conversions"}
    ]
  };

  const url = `https://analyticsdata.googleapis.com/v1beta/properties/${propertyId}:runReport`;

  const options = {
    'method': 'post',
    'contentType': 'application/json',
    'headers': {
      'Authorization': 'Bearer ' + ScriptApp.getOAuthToken()
    },
    'payload': JSON.stringify(request)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response.getContentText());

  // Write to sheet
  const sheet = SpreadsheetApp.getActiveSheet();
  sheet.clear();

  // Headers
  const headers = ['Date', 'Source/Medium', 'Sessions', 'Conversions'];
  sheet.appendRow(headers);

  // Data rows
  data.rows.forEach(row => {
    sheet.appendRow([
      row.dimensionValues[0].value,
      row.dimensionValues[1].value,
      row.metricValues[0].value,
      row.metricValues[1].value
    ]);
  });
}

// Add scheduled trigger:
// Triggers → Add Trigger → getGA4Data → Time-driven → Day timer

ADD OAUTH SCOPES:
──────────────────
// In appsscript.json:
{
  "oauthScopes": [
    "https://www.googleapis.com/auth/analytics.readonly",
    "https://www.googleapis.com/auth/spreadsheets"
  ]
}
```

## API Quota & Limits

```
GA4 DATA API QUOTAS
====================

STANDARD QUOTAS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Limit Type              │ Value                                    │
├─────────────────────────┼──────────────────────────────────────────┤
│ Requests per day        │ 200,000 per project                      │
├─────────────────────────┼──────────────────────────────────────────┤
│ Requests per property   │ 2,000 per property per hour              │
│ per hour                │                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Concurrent requests     │ 10 per property                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Tokens per project      │ 1,750,000 per day                        │
│ per day                 │                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Tokens per property     │ 175,000 per property per hour            │
│ per hour                │                                          │
└─────────────────────────┴──────────────────────────────────────────┘

TOKEN COSTS:
────────────
Each request consumes tokens depending on complexity:

┌─────────────────────────┬──────────────────────────────────────────┐
│ Request Type            │ Token Cost (approximate)                 │
├─────────────────────────┼──────────────────────────────────────────┤
│ Simple query            │ ~10 tokens                               │
│ (1-2 dimensions/metrics)│                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Medium query            │ ~50 tokens                               │
│ (3-5 dimensions/metrics)│                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Complex query           │ ~100+ tokens                             │
│ (filters, pivots, etc.) │                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Realtime report         │ ~200 tokens                              │
└─────────────────────────┴──────────────────────────────────────────┘

QUOTA OPTIMIZATION TIPS:
────────────────────────
1. BATCH REQUESTS
   └── Use runBatchReports for multiple queries

2. CACHE RESPONSES
   └── Store responses, refresh only when needed

3. LIMIT DATE RANGES
   └── Smaller ranges = fewer tokens

4. SELECT ONLY NEEDED FIELDS
   └── Fewer dimensions/metrics = fewer tokens

5. USE SAMPLING (if acceptable)
   └── Faster responses, fewer tokens

QUOTA MONITORING:
─────────────────
├── GCP Console → APIs & Services → Dashboard
├── Select "Analytics Data API"
└── View quota usage graphs
```