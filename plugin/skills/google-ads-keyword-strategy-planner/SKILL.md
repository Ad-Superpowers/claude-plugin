---
name: google-ads-keyword-strategy-planner
description: "This skill should be used when the user asks to \"plan keyword strategy\", \"choose match types\", \"build negative keyword lists\", \"analyze search terms report\", or mentions \"query sculpting\", \"keyword clustering\", or \"Broad vs Phrase vs Exact match\". Do NOT use for: bid strategy selection (use bid-strategy-selector), campaign structure decisions (use campaign-structure-advisor), or Quality Score optimization (use quality-score-optimizer)."
---
# Keyword Strategy Planner

Complete guide for setting up an effective Google Ads keyword strategy with match types, negatives, and search terms analysis.

## Pull Search Terms Data via MCP First

Always start with real data before planning strategy:

```
# Get search term performance for the account
google_ads_run_gaql(query="
  SELECT search_term_view.search_term,
         search_term_view.status,
         metrics.clicks, metrics.impressions, metrics.ctr,
         metrics.conversions, metrics.cost_micros,
         metrics.cost_per_conversion,
         campaign.name, ad_group.name
  FROM search_term_view
  WHERE segments.date DURING LAST_30_DAYS
    AND metrics.clicks > 5
  ORDER BY metrics.conversions DESC
  LIMIT 100
")

# Get keyword performance with Quality Score
google_ads_run_gaql(query="
  SELECT ad_group_criterion.keyword.text,
         ad_group_criterion.keyword.match_type,
         ad_group_criterion.quality_info.quality_score,
         metrics.clicks, metrics.conversions,
         metrics.cost_per_conversion, metrics.search_impression_share
  FROM keyword_view
  WHERE segments.date DURING LAST_30_DAYS
    AND campaign.status = 'ENABLED'
    AND ad_group_criterion.status = 'ENABLED'
  ORDER BY metrics.cost_per_conversion DESC
  LIMIT 50
")
```

## Quick Decision Guide

```
WHICH MATCH TYPE STRATEGY FITS YOUR CASE?
│
├──► NEW ACCOUNT / LIMITED DATA
│   └──► BROAD MATCH + SMART BIDDING
│       ├── Maximum reach
│       ├── Let AI discover queries
│       └── Strict negative management
│
├──► PROVEN KEYWORDS / HIGH VOLUME
│   └──► PHRASE MATCH (Core)
│       ├── Balance between reach and control
│       ├── Intent preserved
│       └── Predictable performance
│
├──► BRAND / HIGH-VALUE KEYWORDS
│   └──► EXACT MATCH
│       ├── Maximum control
│       ├── Premium bidding
│       └── Quality traffic
│
├──► AI MAX CAMPAIGN (2026)
│   └──► KEYWORDS ARE OPTIONAL SIGNALS
│       ├── AI Max matches based on landing page + assets
│       ├── Keywords guide intent, not control reach
│       ├── Focus on strong negatives + audience signals
│       └── Smart Bidding Exploration enabled by default
│
└──► MODERN BEST PRACTICE (2026+)
    └──► HYBRID APPROACH
        ├── Broad Match + Smart Bidding (discovery)
        ├── Phrase Match (core volume)
        ├── Exact Match (top performers)
        └── Aggressive negatives
```

## Match Type Comparison

### 2026 Match Type Behavior

```
MATCH TYPE EVOLUTION (2026)
═══════════════════════════

┌─────────────┬────────────────────────────────────────────────────┐
│ MATCH TYPE  │ MATCHING BEHAVIOR                                  │
├─────────────┼────────────────────────────────────────────────────┤
│ BROAD       │ Synonyms, related terms, intent-based              │
│ [keyword]   │ "running shoes" → "buy running sneakers"           │
│             │ "best sports shoes", "nike runners"                │
│             │ ONLY effective with Smart Bidding!                 │
├─────────────┼────────────────────────────────────────────────────┤
│ PHRASE      │ Meaning must be preserved                          │
│ "keyword"   │ "running shoes" → "cheap running shoes"            │
│             │ "women's running shoes sale"                       │
│             │ Most predictable, intent-focused                   │
├─────────────┼────────────────────────────────────────────────────┤
│ EXACT       │ Same meaning, close variants                       │
│ [keyword]   │ [running shoes] → "running shoes"                  │
│             │ "running shoe", "shoes for running"                │
│             │ Maximum control, premium bids                      │
└─────────────┴────────────────────────────────────────────────────┘

IMPORTANT (2024-2026):
   - Broad Match Modifier (BMM) no longer exists
   - Phrase Match has taken over BMM functionality
   - Broad Match is much broader than before — AI-based matching on intent, not words
   - Smart Bidding Exploration (v21+): Smart Bidding may intentionally explore
     queries with lower historical conversion rates to discover new opportunities
   - AI Max (2026): New Search subtype where Google controls query matching
     entirely — keywords are intent signals, not auction triggers
   - Similar Audiences: Fully removed Aug 2023 → use Optimized Targeting instead
```

### Match Type Selection Matrix

```
MATCH TYPE SELECTION MATRIX
═══════════════════════════

                    │ Control │ Volume │ CPA Risk │ Best For
────────────────────┼─────────┼────────┼──────────┼───────────────
BROAD MATCH         │ Low     │ High   │ High     │ Discovery,
                    │         │        │          │ Smart Bidding
────────────────────┼─────────┼────────┼──────────┼───────────────
PHRASE MATCH        │ Medium  │ Medium │ Medium   │ Core keywords,
                    │         │        │          │ Predictable
────────────────────┼─────────┼────────┼──────────┼───────────────
EXACT MATCH         │ High    │ Low    │ Low      │ Top performers,
                    │         │        │          │ Brand keywords
────────────────────┴─────────┴────────┴──────────┴───────────────

BUDGET ALLOCATION GUIDELINE:
├── Exact Match: 30-40% (proven keywords)
├── Phrase Match: 40-50% (core volume)
└── Broad Match: 10-30% (discovery/Smart Bidding)
```

## Keyword Structure Strategies

### Modern Account Structure (2026)

```
RECOMMENDED KEYWORD STRUCTURE
═════════════════════════════

OLD METHOD (NO LONGER RECOMMENDED):
────────────────────────────────────
SKAGs (Single Keyword Ad Groups)
├── Extreme granularity
├── High maintenance
├── Limited data per ad group
└── Not compatible with Smart Bidding

MODERN METHOD (RECOMMENDED):
─────────────────────────────
Theme-Based Ad Groups (STAGs)
├── Keywords grouped by intent/theme
├── 10-20 keywords per ad group
├── Sufficient data for Smart Bidding
└── RSAs can optimize effectively

EXAMPLE STRUCTURE:
──────────────────
Campaign: Running Shoes
│
├── Ad Group: Men's Running Shoes
│   ├── [men's running shoes] (exact)
│   ├── "running shoes for men" (phrase)
│   ├── "men's running sneakers" (phrase)
│   ├── men's running shoes (broad)
│   └── ... (10-15 related keywords)
│
├── Ad Group: Women's Running Shoes
│   ├── [women's running shoes] (exact)
│   ├── "running shoes for women" (phrase)
│   └── ... (10-15 related keywords)
│
└── Ad Group: Running Shoes Sale
    ├── [running shoes sale] (exact)
    ├── "running shoes discount" (phrase)
    └── ... (10-15 related keywords)
```

### Keyword Clustering Method

```
KEYWORD CLUSTERING WORKFLOW
═══════════════════════════

STEP 1: Keyword Research
────────────────────────
□ Google Keyword Planner
□ Search Terms Report (existing campaigns)
□ Competitor analysis tools
□ Google Autocomplete
□ Related searches

STEP 2: Intent Categorization
─────────────────────────────
TRANSACTIONAL (Purchase intent)
├── "buy", "order", "price"
├── "online shop", "sale", "discount"
└── Priority: HIGH

COMMERCIAL (Comparison intent)
├── "best", "review", "compare"
├── "vs", "or", "alternatives"
└── Priority: MEDIUM-HIGH

INFORMATIONAL (Info intent)
├── "how to", "what is", "why"
├── "guide", "tips", "tutorial"
└── Priority: LOW (usually exclude)

NAVIGATIONAL (Brand intent)
├── Brand names, specific products
├── Competitor brands
└── Priority: VARIABLE

STEP 3: Cluster Formation
─────────────────────────
Group keywords with:
├── Same landing page intent
├── Same user journey stage
├── Comparable CPC range
└── Logical ad copy fit
```

## Negative Keyword Strategy

### Negative Match Types

```
NEGATIVE MATCH TYPES EXPLAINED
══════════════════════════════

NEGATIVES WORK DIFFERENTLY THAN POSITIVE KEYWORDS!

NEGATIVE EXACT [keyword]
────────────────────────
Blocks ONLY that exact query
├── Negative: [free running shoes]
├── Blocks: "free running shoes"
├── Does NOT block: "free running shoes buy"
└── Use for: Very specific blocks

NEGATIVE PHRASE "keyword"
─────────────────────────
Blocks queries containing the phrase
├── Negative: "free"
├── Blocks: "free running shoes"
├── Blocks: "running shoes free shipping"
├── Does NOT block: "gratuite chaussures" (other language)
└── Use for: Most commonly used negative type

NEGATIVE BROAD keyword
──────────────────────
Blocks queries with ALL words (any order)
├── Negative: free discount
├── Blocks: "discount free shipping"
├── Blocks: "free items with discount"
├── Does NOT block: "free shipping" (missing "discount")
└── Use for: Carefully, can block too broadly
```

### Negative Keyword List Structure

```
NEGATIVE KEYWORD MANAGEMENT
═══════════════════════════

ACCOUNT-LEVEL NEGATIVES (Shared Library)
────────────────────────────────────────
Block for ALL campaigns:

□ Free Seekers
├── "free", "download"
├── "torrent", "crack", "pirate"
└── Unless you offer freemium

□ Job Seekers
├── "job", "career", "hiring"
├── "salary", "employment", "position"
└── Unless you do recruitment

□ DIY/How-to (often low-value)
├── "how to make", "do it yourself"
├── "tutorial", "diy"
└── Evaluate per business

□ Competitor Exclusions (optional)
├── Competitor brand names
├── If you don't want to bid on competitors
└── Or put in a separate campaign

CAMPAIGN-LEVEL NEGATIVES
────────────────────────
Specific per campaign type:

E-commerce Campaign Negatives:
├── "second hand", "used", "refurbished"
├── "repair", "fix"
├── Product types you do NOT sell
└── Competitor product names (optional)

Lead Gen Campaign Negatives:
├── "free consult" (if you offer paid)
├── Geographic exclusion (other regions)
├── Industry verticals you don't serve
└── Job-related searches

Brand Campaign Negatives:
├── "[brand] jobs"
├── "[brand] complaints"
├── "[brand] login" (support, not sales)
└── "[brand] customer service"
```

### Negative Keyword Discovery

```
NEGATIVE DISCOVERY WORKFLOW
═══════════════════════════

WEEKLY SEARCH TERMS REVIEW:
───────────────────────────
1. Go to: Keywords → Search Terms
2. Filter: Last 7 days
3. Sort by: Impressions (high to low)
4. Analyze each term:
   ├── Relevant + Converted → Keep
   ├── Relevant + No Conv → Monitor
   ├── Irrelevant + Spend → NEGATIVE
   └── Irrelevant + No Spend → Ignore or negative

QUICK FILTERS FOR NEGATIVES:
─────────────────────────────
□ Conversions = 0 AND Clicks > 10
□ Cost > €X AND Conversions = 0
□ CTR < 1% (often irrelevant)
□ Avg CPC > €X AND no conversions

AUTO-NEGATIVE RULES (Script):
─────────────────────────────
Automatically add negatives when:
├── Query has 5+ clicks, 0 conversions
├── Query CPA > 3x campaign average
├── Query contains known negative terms
└── Query CTR < 0.5%
```

## Search Terms Analysis

### Search Terms Report Optimization

```
SEARCH TERMS ANALYSIS FRAMEWORK
════════════════════════════════

STEP 1: DATA EXPORT
────────────────────
1. Keywords → Search Terms
2. Date range: Last 30-90 days
3. Download as CSV/Excel
4. Include: All columns

STEP 2: CATEGORIZATION
──────────────────────
Create columns for:
├── Category: [Brand/Non-brand/Competitor]
├── Intent: [Trans/Comm/Info/Nav]
├── Action: [Keep/Negative/New Keyword]
└── Priority: [High/Med/Low]

STEP 3: ANALYSIS METRICS
─────────────────────────
POSITIVE INDICATORS:
├── Conversions > 0
├── Conv. Rate > Campaign Avg
├── ROAS > Target
└── High CTR (>3%)

NEGATIVE INDICATORS:
├── Clicks > 5, Conv = 0
├── CTR < 1%
├── Irrelevant intent
└── CPA > 3x target

STEP 4: ACTIONS
───────────────
UPGRADE TO KEYWORD:
├── Search term with 3+ conversions
├── Better CPA than campaign avg
├── Add as Exact Match
└── Create dedicated ad copy

ADD AS NEGATIVE:
├── 0 conversions, significant spend
├── Clearly irrelevant intent
├── Add at the right level
└── Phrase or Exact negative
```

### Query Sculpting Technique

```
QUERY SCULPTING STRATEGY
═════════════════════════

WHAT IS QUERY SCULPTING?
────────────────────────
= Routing queries to the most suitable ad group
  through strategic use of negatives

EXAMPLE:
────────
Campaign: Running Shoes
├── Ad Group: Premium Running Shoes
│   ├── "nike running shoes" (phrase)
│   └── Negative: "cheap", "budget", "sale"
│
├── Ad Group: Budget Running Shoes
│   ├── "cheap running shoes" (phrase)
│   └── Negative: "nike", "adidas", "premium"
│
└── Result: Queries go to the right ad group

BENEFITS:
├── More relevant ads per query
├── Better Quality Score
├── Higher CTR
└── Optimized bids per segment

IMPLEMENTATION:
──────────────
1. Identify overlapping keywords
2. Determine which ad group is primary
3. Add cross-negatives
4. Monitor search terms for leakage
5. Adjust negatives as needed
```

## Keyword Research Tools & Methods

### Google Keyword Planner Best Practices

```
KEYWORD PLANNER BEST PRACTICES
══════════════════════════════

DISCOVERY MODE:
───────────────
1. "Discover new keywords"
2. Start with:
   ├── Competitor URL (discover their keywords)
   ├── Seed keywords (your top 5 keywords)
   └── Product/Service category

3. Filter on:
   ├── Avg monthly searches: 100-10000
   ├── Competition: Low-Medium (for new accounts)
   ├── Top of page bid: Within budget
   └── Language & Location: Your targets

FORECAST MODE:
──────────────
1. "Get search volume and forecasts"
2. Upload your keyword list
3. Set:
   ├── Budget: Your planned budget
   ├── Date range: Next 3 months
   └── Match types: All (compare)

4. Analyze:
   ├── Estimated clicks
   ├── Estimated CPC
   ├── Total cost
   └── Match type differences

COMPETITOR ANALYSIS:
────────────────────
1. Tools → Keyword Planner
2. "Start with a website"
3. Enter: competitor URL
4. Filter: Products/Services only
5. Export their top keywords
6. Compare with your own list
```

### Alternative Keyword Research

```
ADDITIONAL KEYWORD SOURCES
══════════════════════════

GOOGLE SEARCH FEATURES:
───────────────────────
□ Autocomplete
├── Type your keyword, note suggestions
├── Add letters: "[keyword] a", "[keyword] b"
└── Check other languages

□ Related Searches
├── Bottom of SERP
├── "People also search for"
└── Often long-tail variations

□ "People Also Ask"
├── FAQ-style queries
├── Good for content/ad copy
└── Informational intent

TOOLS (Besides Keyword Planner):
────────────────────────────────
□ Google Trends
├── Seasonal patterns
├── Trending topics
└── Geographic data

□ Search Console
├── Queries where you rank organically
├── Impressions = search volume proxy
└── CTR data for ad copy

□ Competitor Ad Libraries
├── Facebook Ad Library
├── Google Ads Transparency Center
└── What are they advertising?
```

## Google Ads Script: Search Terms Analyzer

```javascript
/**
 * Search Terms Analyzer Script
 *
 * Analyzes search terms and generates:
 * - Negative keyword suggestions
 * - New keyword opportunities
 * - Performance alerts
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Thresholds for negatives
  NEGATIVE_CLICKS_THRESHOLD: 5,      // Min clicks without conversion
  NEGATIVE_COST_THRESHOLD: 20,       // Min cost without conversion
  NEGATIVE_CTR_THRESHOLD: 0.01,      // Max CTR for low performers

  // Thresholds for new keywords
  NEW_KEYWORD_CONVERSIONS: 2,        // Min conversions
  NEW_KEYWORD_CPA_MULTIPLIER: 0.8,   // Max CPA vs campaign (80%)

  // Known negative terms (always exclude)
  ALWAYS_NEGATIVE: [
    'free', 'download',
    'job', 'career', 'hiring',
    'how to make', 'diy', 'do it yourself'
  ],

  // Date range
  DATE_RANGE: 'LAST_30_DAYS'
};

function main() {
  var report = {
    negativesSuggested: [],
    newKeywords: [],
    alerts: []
  };

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    analyzeSearchTerms(campaign, report);
  }

  if (report.negativesSuggested.length > 0 ||
      report.newKeywords.length > 0) {
    sendReport(report);
  }

  Logger.log('Analysis complete.');
  Logger.log('Negative suggestions: ' + report.negativesSuggested.length);
  Logger.log('New keyword opportunities: ' + report.newKeywords.length);
}

function analyzeSearchTerms(campaign, report) {
  var campaignName = campaign.getName();
  var campaignStats = campaign.getStatsFor(CONFIG.DATE_RANGE);
  var campaignCPA = campaignStats.getConversions() > 0 ?
    campaignStats.getCost() / campaignStats.getConversions() : 0;

  var searchTerms = campaign.searchTerms()
    .forDateRange(CONFIG.DATE_RANGE)
    .withCondition('Impressions > 10')
    .get();

  while (searchTerms.hasNext()) {
    var term = searchTerms.next();
    var query = term.getText().toLowerCase();
    var stats = term.getStatsFor(CONFIG.DATE_RANGE);

    var clicks = stats.getClicks();
    var cost = stats.getCost();
    var conversions = stats.getConversions();
    var ctr = stats.getCtr();

    // Check for always-negative terms
    for (var i = 0; i < CONFIG.ALWAYS_NEGATIVE.length; i++) {
      if (query.indexOf(CONFIG.ALWAYS_NEGATIVE[i]) !== -1) {
        report.negativesSuggested.push({
          campaign: campaignName,
          term: query,
          reason: 'Contains excluded term: ' + CONFIG.ALWAYS_NEGATIVE[i],
          clicks: clicks,
          cost: cost,
          conversions: conversions
        });
        break;
      }
    }

    // Check for non-converting high-spend terms
    if (conversions === 0) {
      if (clicks >= CONFIG.NEGATIVE_CLICKS_THRESHOLD ||
          cost >= CONFIG.NEGATIVE_COST_THRESHOLD) {
        report.negativesSuggested.push({
          campaign: campaignName,
          term: query,
          reason: 'High spend, no conversions',
          clicks: clicks,
          cost: cost.toFixed(2),
          conversions: conversions
        });
      }
    }

    // Check for low CTR terms
    if (ctr < CONFIG.NEGATIVE_CTR_THRESHOLD && clicks > 0) {
      report.negativesSuggested.push({
        campaign: campaignName,
        term: query,
        reason: 'Very low CTR: ' + (ctr * 100).toFixed(2) + '%',
        clicks: clicks,
        cost: cost.toFixed(2),
        conversions: conversions
      });
    }

    // Check for new keyword opportunities
    if (conversions >= CONFIG.NEW_KEYWORD_CONVERSIONS) {
      var termCPA = cost / conversions;
      if (campaignCPA === 0 || termCPA < (campaignCPA * CONFIG.NEW_KEYWORD_CPA_MULTIPLIER)) {
        report.newKeywords.push({
          campaign: campaignName,
          term: query,
          conversions: conversions,
          cpa: termCPA.toFixed(2),
          campaignCPA: campaignCPA.toFixed(2),
          cost: cost.toFixed(2)
        });
      }
    }
  }
}

function sendReport(report) {
  var subject = 'Search Terms Analysis - ' + AdsApp.currentAccount().getName();
  var body = 'Weekly Search Terms Analysis\n';
  body += '============================\n\n';

  if (report.negativesSuggested.length > 0) {
    body += 'NEGATIVE KEYWORD SUGGESTIONS:\n';
    body += '─────────────────────────────\n';
    for (var i = 0; i < Math.min(report.negativesSuggested.length, 20); i++) {
      var neg = report.negativesSuggested[i];
      body += '  "' + neg.term + '"\n';
      body += '  Campaign: ' + neg.campaign + '\n';
      body += '  Reason: ' + neg.reason + '\n';
      body += '  Clicks: ' + neg.clicks + ', Cost: €' + neg.cost + '\n\n';
    }
    if (report.negativesSuggested.length > 20) {
      body += '... and ' + (report.negativesSuggested.length - 20) + ' more\n';
    }
    body += '\n';
  }

  if (report.newKeywords.length > 0) {
    body += 'NEW KEYWORD OPPORTUNITIES:\n';
    body += '─────────────────────────\n';
    for (var j = 0; j < Math.min(report.newKeywords.length, 10); j++) {
      var kw = report.newKeywords[j];
      body += '  "' + kw.term + '"\n';
      body += '  Campaign: ' + kw.campaign + '\n';
      body += '  Conversions: ' + kw.conversions + ', CPA: €' + kw.cpa + '\n';
      body += '  (Campaign avg CPA: €' + kw.campaignCPA + ')\n\n';
    }
  }

  body += '\n---\nGenerated by Search Terms Analyzer Script';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
  Logger.log('Report sent to ' + CONFIG.EMAIL);
}
```

## Output: Keyword Strategy Template

```markdown
# Keyword Strategy Plan

## Account Overview
- **Business type:** [E-commerce / Lead Gen / SaaS]
- **Monthly budget:** €[X]
- **Target CPA/ROAS:** €[X] / [X]%
- **Primary markets:** [NL/BE/DACH/etc.]

## Keyword Structure

### Campaign: [Campaign Name]
**Match Type Mix:**
- Exact Match: [X]%
- Phrase Match: [X]%
- Broad Match: [X]%

**Ad Groups:**

#### Ad Group 1: [Theme]
| Keyword | Match Type | Expected CPC | Priority |
|---------|------------|--------------|----------|
| [keyword] | Exact | €X.XX | High |
| "keyword phrase" | Phrase | €X.XX | High |
| keyword broad | Broad | €X.XX | Medium |

## Negative Keyword Lists

### Account-Level Negatives
```
free
download
job
career
diy
do it yourself
```

### Campaign-Specific Negatives
```
[Campaign 1]: competitor name, irrelevant category
[Campaign 2]: out-of-scope locations, services not offered
```

## Search Terms Review Schedule
- **Frequency:** [Weekly/Bi-weekly]
- **Owner:** [Name]
- **Actions:**
  - [ ] Add converting terms as keywords
  - [ ] Add non-converting terms as negatives
  - [ ] Update ad copy based on insights

## KPIs & Monitoring
- **Target CTR:** [X]%
- **Target Quality Score:** [X]+
- **Max keyword CPA:** €[X]
- **Review date:** [Date]
```
