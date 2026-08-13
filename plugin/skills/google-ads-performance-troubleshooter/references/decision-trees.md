## Conversion Drop Diagnosis

### Decision Tree

```
CONVERSIONS DROPPED - DIAGNOSIS
════════════════════════════════

START: Conversions have dropped
│
├─► CHECK 1: Is tracking intact?
│   ├── Test conversion on website → Fired in Google Ads?
│   ├── Check Tag Assistant / Google Ads Conversions Report
│   └── Compare conversions in GA4 vs Google Ads
│       │
│       ├─► TRACKING BROKEN
│       │   └─► Fix: Check GTM, consent mode, tag status
│       │
│       └─► TRACKING OK → Go to Check 2
│
├─► CHECK 2: Have clicks dropped?
│   ├── Compare clicks week-over-week
│   │
│   ├─► CLICKS DROPPED
│   │   └─► Problem is upstream (traffic)
│   │       └─► Go to "Volume Decline Diagnosis"
│   │
│   └─► CLICKS STABLE → Conversion Rate dropped
│       └─► Go to Check 3
│
├─► CHECK 3: Has the landing page changed?
│   ├── Check page speed (PageSpeed Insights)
│   ├── Check mobile experience
│   ├── Is form/checkout working?
│   │
│   ├─► LANDING PAGE ISSUE
│   │   └─► Fix: Rollback changes, fix bugs
│   │
│   └─► LANDING PAGE OK → Go to Check 4
│
├─► CHECK 4: Has traffic quality changed?
│   ├── Check search terms report
│   ├── Are there new query types?
│   ├── Check device/location shifts
│   │
│   ├─► TRAFFIC QUALITY ISSUE
│   │   └─► Fix: Negatives, targeting, bid adjustments
│   │
│   └─► TRAFFIC QUALITY OK → Go to Check 5
│
└─► CHECK 5: External factors
    ├── Seasonality?
    ├── Competitor activity?
    ├── Market change?
    └─► Analyze and adapt strategy
```

### Conversion Tracking Verification

```
CONVERSION TRACKING CHECK
══════════════════════════

STEP 1: BASIC VERIFICATION
───────────────────────────
□ Google Ads → Tools → Conversions
□ Check "Recording status" per action
  ├── "Recording conversions" = OK
  ├── "No recent conversions" = Possible issue
  └── "Tag inactive" = Problem!

□ View conversions per day graph
  └── Sudden drop = Tracking issue
  └── Gradual decline = Other cause

STEP 2: TAG VERIFICATION
─────────────────────────
Via Google Tag Assistant (Chrome Extension):
□ Load conversion page
□ Check if conversion tag fired
□ Check if value is correct
□ Check consent mode status

Via Google Ads Tag Diagnostics:
□ Tools → Conversions → [Action] → Tag setup
□ Run diagnostics
□ Check website tag status

STEP 3: COMPARE SOURCES
────────────────────────
┌────────────────────────────────────────────────────────┐
│ Source         │ Conversions │ Difference vs GA4       │
├────────────────┼─────────────┼─────────────────────────┤
│ Google Ads     │ [X]         │ Baseline                │
│ GA4 (Google)   │ [X]         │ Should be approx. equal │
│ CRM/Backend    │ [X]         │ True source of truth    │
└────────────────┴─────────────┴─────────────────────────┘

If large discrepancy:
├── GA4 < Google Ads: Possibly duplicate tags
├── GA4 > Google Ads: Tracking not complete
└── CRM ≠ both: Attribution/timing differences

STEP 4: CONSENT MODE CHECK
───────────────────────────
□ Is consent banner implemented?
□ Is consent correctly passed?
□ Are conversion modeling settings correct?
□ Check: "Consent mode" column in conversions

Consent Mode Impact:
├── Well configured: Google models ~70-80%
├── Poorly configured: Large data gaps
└── Not present: Potential compliance issues
```

### Decision Tree

```
CONVERSIONS DROPPED - DIAGNOSIS
════════════════════════════════

START: Conversions have dropped
│
├─► CHECK 1: Is tracking intact?
│   ├── Test conversion on website → Fired in Google Ads?
│   ├── Check Tag Assistant / Google Ads Conversions Report
│   └── Compare conversions in GA4 vs Google Ads
│       │
│       ├─► TRACKING BROKEN
│       │   └─► Fix: Check GTM, consent mode, tag status
│       │
│       └─► TRACKING OK → Go to Check 2
│
├─► CHECK 2: Have clicks dropped?
│   ├── Compare clicks week-over-week
│   │
│   ├─► CLICKS DROPPED
│   │   └─► Problem is upstream (traffic)
│   │       └─► Go to "Volume Decline Diagnosis"
│   │
│   └─► CLICKS STABLE → Conversion Rate dropped
│       └─► Go to Check 3
│
├─► CHECK 3: Has the landing page changed?
│   ├── Check page speed (PageSpeed Insights)
│   ├── Check mobile experience
│   ├── Is form/checkout working?
│   │
│   ├─► LANDING PAGE ISSUE
│   │   └─► Fix: Rollback changes, fix bugs
│   │
│   └─► LANDING PAGE OK → Go to Check 4
│
├─► CHECK 4: Has traffic quality changed?
│   ├── Check search terms report
│   ├── Are there new query types?
│   ├── Check device/location shifts
│   │
│   ├─► TRAFFIC QUALITY ISSUE
│   │   └─► Fix: Negatives, targeting, bid adjustments
│   │
│   └─► TRAFFIC QUALITY OK → Go to Check 5
│
└─► CHECK 5: External factors
    ├── Seasonality?
    ├── Competitor activity?
    ├── Market change?
    └─► Analyze and adapt strategy
```

## Efficiency Degradation Diagnosis

### CPA Increased

```
CPA INCREASED - ROOT CAUSE ANALYSIS
════════════════════════════════════

POSSIBLE CAUSES (in order of likelihood):

1. COMPETITION INCREASED
────────────────────────
Symptoms:
├── Avg CPC increased
├── Impression share decreased
├── Same queries, higher costs

Verification:
└── Review Auction Insights
    ├── New competitors?
    ├── Overlap rate changed?
    └── Outranking share decreased?

Solution:
├── Increase budget (if ROI remains positive)
├── Focus on efficiency (neg keywords, targeting)
├── Differentiate (ad copy, landing page)
└── Explore other channels

2. QUALITY SCORE DROPPED
─────────────────────────
Symptoms:
├── QS column shows decline
├── Higher CPCs needed for same position
├── Expected CTR/Ad Relevance/LP experience dropped

Verification:
└── Review Columns → Quality Score (historical)

Solution:
└── See "Quality Score Troubleshoot" section

3. AUDIENCE/TRAFFIC SHIFT
──────────────────────────
Symptoms:
├── Different demographics converting
├── Device mix shifted
├── Geographic shifts

Verification:
├── Segment by device/location/audience
└── Compare converters vs non-converters

Solution:
├── Bid adjustments per segment
├── Separate campaigns for best segments
└── Exclude underperforming segments

4. LANDING PAGE PERFORMANCE
────────────────────────────
Symptoms:
├── Bounce rate increased
├── Time on site decreased
├── Form abandonment increased

Verification:
├── GA4 landing page report
├── User recordings (Hotjar/FullStory)
└── Page speed check

Solution:
├── Fix page speed issues
├── Improve mobile experience
├── Simplify conversion flow
└── A/B test landing page variants

5. SEASONALITY
──────────────
Symptoms:
├── Historically same period = worse
├── Industry-wide trends
├── Holiday/event impact

Verification:
├── Year-over-year comparison
└── Check industry benchmarks

Solution:
├── Adjust expectations
├── Seasonality adjustments in bidding
└── Prep for high season
```

### ROAS Decreased

```
ROAS DECREASED - DIAGNOSIS
═══════════════════════════

ROAS = Revenue / Ad Spend

ROAS decreased can be caused by:
├── A) Same revenue, higher spend
├── B) Lower revenue, same spend
└── C) Combination

DIAGNOSIS:

SCENARIO A: SPEND INCREASED
────────────────────────────
Check:
├── Budget automatically increased?
├── Bid strategy changed?
├── CPCs increased (competition)?

Solution:
├── Review budget settings
├── Check Smart Bidding targets
└── Analyze CPC trends

SCENARIO B: REVENUE DECREASED
──────────────────────────────
Check:
├── Average Order Value (AOV) decreased?
├── Fewer purchases?
├── Product mix shifted?

AOV decreased:
├── Cheaper products promoted?
├── Discounting increased?
├── Upsell/cross-sell not working?

Fewer purchases:
├── Conversion rate check (see earlier)
├── Cart abandonment increased?
├── Payment issues?

Solution:
├── Promote higher-margin products
├── Review promotional strategy
├── Check checkout flow
└── Deploy value-based bidding

SCENARIO C: BOTH FACTORS
─────────────────────────
Combination of above - common with:
├── Market downturn
├── Strong competitor entry
├── Major algorithm change

Action:
├── Run full audit
├── Competitive analysis
└── Strategy reconsideration
```

### ROAS Decreased

```
ROAS DECREASED - DIAGNOSIS
═══════════════════════════

ROAS = Revenue / Ad Spend

ROAS decreased can be caused by:
├── A) Same revenue, higher spend
├── B) Lower revenue, same spend
└── C) Combination

DIAGNOSIS:

SCENARIO A: SPEND INCREASED
────────────────────────────
Check:
├── Budget automatically increased?
├── Bid strategy changed?
├── CPCs increased (competition)?

Solution:
├── Review budget settings
├── Check Smart Bidding targets
└── Analyze CPC trends

SCENARIO B: REVENUE DECREASED
──────────────────────────────
Check:
├── Average Order Value (AOV) decreased?
├── Fewer purchases?
├── Product mix shifted?

AOV decreased:
├── Cheaper products promoted?
├── Discounting increased?
├── Upsell/cross-sell not working?

Fewer purchases:
├── Conversion rate check (see earlier)
├── Cart abandonment increased?
├── Payment issues?

Solution:
├── Promote higher-margin products
├── Review promotional strategy
├── Check checkout flow
└── Deploy value-based bidding

SCENARIO C: BOTH FACTORS
─────────────────────────
Combination of above - common with:
├── Market downturn
├── Strong competitor entry
├── Major algorithm change

Action:
├── Run full audit
├── Competitive analysis
└── Strategy reconsideration
```

## Volume Decline Diagnosis

### Impressions Dropped

```
IMPRESSIONS DROPPED - TROUBLESHOOT
═══════════════════════════════════

CHECK 1: BUDGET & BIDDING
──────────────────────────
□ Budget limited status?
□ Bid too low for positions?
□ Target CPA/ROAS too aggressive?

Budget Limited:
├── Increase budget
├── Or: Prioritize best performers
└── Or: Reduce targets to stay within budget

Bid Limited:
├── Increase bids/targets
├── Check search impression share (rank)
└── Improve Quality Score

CHECK 2: TARGETING CHANGES
───────────────────────────
□ Have keywords been paused?
□ Location targeting changed?
□ Device targeting changed?
□ Audience targeting (exclusions)?

Review recent changes:
├── Change History in Google Ads
└── Rollback if needed

CHECK 3: ADS/KEYWORDS STATUS
─────────────────────────────
□ Ads disapproved?
□ Keywords suspended?
□ Policy violations?

Check:
├── Ads → Status column
├── Keywords → Status column
└── Notifications/Emails

CHECK 4: SEARCH DEMAND
───────────────────────
□ Keyword Planner: search volume changed?
□ Seasonality effect?
□ Market trend shift?

Trend check:
├── Google Trends for key terms
└── Year-over-year comparison

CHECK 5: AUCTION DYNAMICS
──────────────────────────
□ Auction Insights: new competitors?
□ CPCs increased (but bids didn't)?
□ Market consolidation?

IMPRESSION SHARE BREAKDOWN:
───────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Metric                    │ Meaning                     │
├───────────────────────────┼─────────────────────────────┤
│ Search Impression Share   │ % of eligible impressions   │
├───────────────────────────┼─────────────────────────────┤
│ Lost IS (Budget)          │ Lost due to budget          │
├───────────────────────────┼─────────────────────────────┤
│ Lost IS (Rank)            │ Lost due to low Ad Rank     │
└───────────────────────────┴─────────────────────────────┘

If Lost IS (Budget) is high:
└── Increase budget or focus on efficiency

If Lost IS (Rank) is high:
└── Improve Quality Score or increase bids
```

### Clicks Dropped (but Impressions Stable)

```
CTR DROPPED - DIAGNOSIS
════════════════════════

SYMPTOM: Impressions stable, clicks dropped = CTR drop

CHECK 1: AD COPY/CREATIVE
──────────────────────────
□ Ads changed?
□ RSA assets in rotation changed?
□ Ad strength dropped?
□ Extensions removed/paused?

Verification:
├── Compare ad performance pre/post
├── Check RSA asset performance
└── Review extension status

Solution:
├── Revert ad changes
├── Add winning assets
├── Restore extensions
└── Test new variations

CHECK 2: SEARCH TERMS SHIFT
────────────────────────────
□ Different queries triggering ads?
□ Broad match expansion?
□ Low-intent queries?

Verification:
├── Search Terms report
├── Compare top queries pre/post
└── Check query intent

Solution:
├── Add negative keywords
├── Adjust match types
└── Refine ad copy for queries

CHECK 3: COMPETITOR ADS
────────────────────────
□ Competitors with better offers?
□ Competitors with extensions you don't have?
□ Competitors in higher positions?

Verification:
├── Manual search checks
├── Auction Insights
└── SEMrush/SpyFu competitor analysis

Solution:
├── Improve ad USPs
├── Add missing extensions
├── Test promotional offers
└── Bid for better positions (test)

CHECK 4: AD POSITION
─────────────────────
□ Average position dropped?
□ Top of page rate dropped?

Verification:
├── "Search top IS" metric
├── "Abs. top IS" metric
└── Average position trend

Correlation:
├── Lower position = lower CTR (expected)
└── Focus on impression share vs position trade-off

CHECK 5: AUDIENCE FATIGUE
──────────────────────────
□ Retargeting audiences overexposed?
□ Frequency too high?
□ Display/Video ad fatigue?

Symptoms:
├── CTR declining over time
├── Same audience reached too long
└── Creative has become "blind"

Solution:
├── Refresh creatives
├── Expand audiences
├── Implement frequency capping
```

### Impressions Dropped

```
IMPRESSIONS DROPPED - TROUBLESHOOT
═══════════════════════════════════

CHECK 1: BUDGET & BIDDING
──────────────────────────
□ Budget limited status?
□ Bid too low for positions?
□ Target CPA/ROAS too aggressive?

Budget Limited:
├── Increase budget
├── Or: Prioritize best performers
└── Or: Reduce targets to stay within budget

Bid Limited:
├── Increase bids/targets
├── Check search impression share (rank)
└── Improve Quality Score

CHECK 2: TARGETING CHANGES
───────────────────────────
□ Have keywords been paused?
□ Location targeting changed?
□ Device targeting changed?
□ Audience targeting (exclusions)?

Review recent changes:
├── Change History in Google Ads
└── Rollback if needed

CHECK 3: ADS/KEYWORDS STATUS
─────────────────────────────
□ Ads disapproved?
□ Keywords suspended?
□ Policy violations?

Check:
├── Ads → Status column
├── Keywords → Status column
└── Notifications/Emails

CHECK 4: SEARCH DEMAND
───────────────────────
□ Keyword Planner: search volume changed?
□ Seasonality effect?
□ Market trend shift?

Trend check:
├── Google Trends for key terms
└── Year-over-year comparison

CHECK 5: AUCTION DYNAMICS
──────────────────────────
□ Auction Insights: new competitors?
□ CPCs increased (but bids didn't)?
□ Market consolidation?

IMPRESSION SHARE BREAKDOWN:
───────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Metric                    │ Meaning                     │
├───────────────────────────┼─────────────────────────────┤
│ Search Impression Share   │ % of eligible impressions   │
├───────────────────────────┼─────────────────────────────┤
│ Lost IS (Budget)          │ Lost due to budget          │
├───────────────────────────┼─────────────────────────────┤
│ Lost IS (Rank)            │ Lost due to low Ad Rank     │
└───────────────────────────┴─────────────────────────────┘

If Lost IS (Budget) is high:
└── Increase budget or focus on efficiency

If Lost IS (Rank) is high:
└── Improve Quality Score or increase bids
```

### Clicks Dropped (but Impressions Stable)

```
CTR DROPPED - DIAGNOSIS
════════════════════════

SYMPTOM: Impressions stable, clicks dropped = CTR drop

CHECK 1: AD COPY/CREATIVE
──────────────────────────
□ Ads changed?
□ RSA assets in rotation changed?
□ Ad strength dropped?
□ Extensions removed/paused?

Verification:
├── Compare ad performance pre/post
├── Check RSA asset performance
└── Review extension status

Solution:
├── Revert ad changes
├── Add winning assets
├── Restore extensions
└── Test new variations

CHECK 2: SEARCH TERMS SHIFT
────────────────────────────
□ Different queries triggering ads?
□ Broad match expansion?
□ Low-intent queries?

Verification:
├── Search Terms report
├── Compare top queries pre/post
└── Check query intent

Solution:
├── Add negative keywords
├── Adjust match types
└── Refine ad copy for queries

CHECK 3: COMPETITOR ADS
────────────────────────
□ Competitors with better offers?
□ Competitors with extensions you don't have?
□ Competitors in higher positions?

Verification:
├── Manual search checks
├── Auction Insights
└── SEMrush/SpyFu competitor analysis

Solution:
├── Improve ad USPs
├── Add missing extensions
├── Test promotional offers
└── Bid for better positions (test)

CHECK 4: AD POSITION
─────────────────────
□ Average position dropped?
□ Top of page rate dropped?

Verification:
├── "Search top IS" metric
├── "Abs. top IS" metric
└── Average position trend

Correlation:
├── Lower position = lower CTR (expected)
└── Focus on impression share vs position trade-off

CHECK 5: AUDIENCE FATIGUE
──────────────────────────
□ Retargeting audiences overexposed?
□ Frequency too high?
□ Display/Video ad fatigue?

Symptoms:
├── CTR declining over time
├── Same audience reached too long
└── Creative has become "blind"

Solution:
├── Refresh creatives
├── Expand audiences
├── Implement frequency capping
```

## Delivery Problems

### No Impressions

```
0 IMPRESSIONS - TROUBLESHOOT
═════════════════════════════

URGENCY: No spend = no results

STEP-BY-STEP DIAGNOSIS:

1. CAMPAIGN STATUS
──────────────────
□ Campaign enabled?
□ No "Removed" status?
□ Start/end dates correct?
□ Budget > 0?

2. AD GROUP STATUS
──────────────────
□ Ad groups enabled?
□ At least 1 active ad?
□ At least 1 active keyword (Search)?

3. ADS STATUS
─────────────
□ Ads approved?
□ No "Policy violation"?
□ No "Under review" (too long)?

Common disapprovals:
├── Trademark issues
├── Misleading content
├── Unavailable landing page
├── Prohibited content
└── Technical issues (redirects)

4. KEYWORDS STATUS
──────────────────
□ Keywords active?
□ No "Low search volume"?
□ No "Suspended"?
□ Bids not 0?

5. TARGETING
────────────
□ Locations set correctly?
□ Languages correct?
□ Schedule not too restrictive?
□ Audiences not exclusions-only?

6. BUDGET & BIDS
────────────────
□ Budget sufficient?
□ Bids sufficient for market?
□ Target CPA/ROAS not too aggressive?

7. BILLING
──────────
□ Payment method valid?
□ No account suspension?
□ Credit line available?

QUICK FIX CHECKLIST:
────────────────────
If new campaign:
□ Wait 24-48 hours for initial approval
□ Check policy centre for issues
□ Verify billing setup

If existing campaign suddenly stopped:
□ Check Change History for recent changes
□ Check Notifications for warnings
□ Review Billing for payment issues
```

### No Impressions

```
0 IMPRESSIONS - TROUBLESHOOT
═════════════════════════════

URGENCY: No spend = no results

STEP-BY-STEP DIAGNOSIS:

1. CAMPAIGN STATUS
──────────────────
□ Campaign enabled?
□ No "Removed" status?
□ Start/end dates correct?
□ Budget > 0?

2. AD GROUP STATUS
──────────────────
□ Ad groups enabled?
□ At least 1 active ad?
□ At least 1 active keyword (Search)?

3. ADS STATUS
─────────────
□ Ads approved?
□ No "Policy violation"?
□ No "Under review" (too long)?

Common disapprovals:
├── Trademark issues
├── Misleading content
├── Unavailable landing page
├── Prohibited content
└── Technical issues (redirects)

4. KEYWORDS STATUS
──────────────────
□ Keywords active?
□ No "Low search volume"?
□ No "Suspended"?
□ Bids not 0?

5. TARGETING
────────────
□ Locations set correctly?
□ Languages correct?
□ Schedule not too restrictive?
□ Audiences not exclusions-only?

6. BUDGET & BIDS
────────────────
□ Budget sufficient?
□ Bids sufficient for market?
□ Target CPA/ROAS not too aggressive?

7. BILLING
──────────
□ Payment method valid?
□ No account suspension?
□ Credit line available?

QUICK FIX CHECKLIST:
────────────────────
If new campaign:
□ Wait 24-48 hours for initial approval
□ Check policy centre for issues
□ Verify billing setup

If existing campaign suddenly stopped:
□ Check Change History for recent changes
□ Check Notifications for warnings
□ Review Billing for payment issues
```

## Quality Score Troubleshoot

### Diagnosis

```
QUALITY SCORE ANALYSIS
══════════════════════

QUALITY SCORE COMPONENTS:
──────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Component              │ Weight │ What it measures      │
├────────────────────────┼────────┼───────────────────────┤
│ Expected CTR           │ ~40%   │ Likelihood of click   │
├────────────────────────┼────────┼───────────────────────┤
│ Ad Relevance           │ ~20%   │ Match query<>ad copy  │
├────────────────────────┼────────┼───────────────────────┤
│ Landing Page Exp       │ ~40%   │ Page quality & match  │
└────────────────────────┴────────┴───────────────────────┘

HOW TO ANALYZE:
────────────────
Add columns:
├── Quality Score
├── Quality Score (hist.)
├── Expected CTR
├── Expected CTR (hist.)
├── Ad Relevance
├── Ad Relevance (hist.)
├── Landing Page Exp
└── Landing Page Exp (hist.)

Filter on:
├── QS < 5 (priority fix)
├── High impression keywords with low QS
└── Keywords with QS decline vs previous month

STATUS INTERPRETATION:
──────────────────────
"Below average" = Problem, action required
"Average" = OK, room for improvement
"Above average" = Good, maintain
```

### Solutions per Component

```
EXPECTED CTR - IMPROVE
═══════════════════════

CAUSES OF LOW EXPECTED CTR:
├── Ad copy not compelling
├── No strong CTA
├── Competitors have better ads
└── Keyword-ad mismatch

SOLUTIONS:
──────────

1. IMPROVE AD COPY
   □ Include keyword in headline 1
   □ Strong, specific CTA
   □ USPs and differentiators
   □ Numbers and specifics (15% off, 500+ reviews)

2. USE ALL AD ASSETS
   □ 15 headlines in RSA
   □ 4 descriptions
   □ Pin only strategically
   □ Test variations

3. ADD EXTENSIONS
   □ Sitelinks (min 4)
   □ Callouts (min 4)
   □ Structured snippets
   □ Call/location extensions

4. TEST & ITERATE
   □ A/B test ad variations
   □ Review top performing ads
   □ Pause underperformers
   □ Check RSA asset performance

─────────────────────────────────────────────────────────

AD RELEVANCE - IMPROVE
═══════════════════════

CAUSES OF LOW AD RELEVANCE:
├── Keywords not in ad copy
├── Ad groups too broad
├── Generic ads for specific keywords
└── Outdated ads

SOLUTIONS:
──────────

1. KEYWORD IN AD COPY
   □ Exact keyword in headline (where possible)
   □ Keyword in description
   □ Use {KeyWord:Default} insertion

2. AD GROUP STRUCTURE
   □ Tight theme ad groups (5-20 keywords)
   □ Ads specific to ad group theme
   □ Consider SKAGs for top performers
   └── (Single Keyword Ad Groups)

3. DYNAMIC KEYWORD INSERTION
   □ {KeyWord:Fallback}
   □ Only for relevant positions
   □ Check for awkward insertions

4. REFRESH AD COPY
   □ Remove outdated messaging
   □ Update for current promotions
   □ Match current landing page

─────────────────────────────────────────────────────────

LANDING PAGE EXPERIENCE - IMPROVE
══════════════════════════════════

CAUSES OF LOW LANDING PAGE EXP:
├── Slow page load
├── Poor mobile experience
├── Content mismatch with ad
├── Difficult navigation
└── Missing trust signals

SOLUTIONS:
──────────

1. PAGE SPEED
   □ Target: <3 sec load time
   □ Use PageSpeed Insights
   □ Optimize images
   □ Minimize scripts
   □ Enable caching

2. MOBILE EXPERIENCE
   □ Responsive design
   □ Tap targets large enough
   □ No horizontal scrolling
   □ Easy form filling

3. CONTENT RELEVANCE
   □ Headline matches ad
   □ Keyword in page title/H1
   □ Clear path to conversion
   □ No bait-and-switch

4. USER EXPERIENCE
   □ Clear navigation
   □ Trust signals (reviews, badges)
   □ Contact info visible
   □ Privacy policy linked

5. TECHNICAL SEO
   □ HTTPS required
   □ No broken links
   □ Proper meta tags
   □ Clean URL structure
```

### Diagnosis

```
QUALITY SCORE ANALYSIS
══════════════════════

QUALITY SCORE COMPONENTS:
──────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Component              │ Weight │ What it measures      │
├────────────────────────┼────────┼───────────────────────┤
│ Expected CTR           │ ~40%   │ Likelihood of click   │
├────────────────────────┼────────┼───────────────────────┤
│ Ad Relevance           │ ~20%   │ Match query<>ad copy  │
├────────────────────────┼────────┼───────────────────────┤
│ Landing Page Exp       │ ~40%   │ Page quality & match  │
└────────────────────────┴────────┴───────────────────────┘

HOW TO ANALYZE:
────────────────
Add columns:
├── Quality Score
├── Quality Score (hist.)
├── Expected CTR
├── Expected CTR (hist.)
├── Ad Relevance
├── Ad Relevance (hist.)
├── Landing Page Exp
└── Landing Page Exp (hist.)

Filter on:
├── QS < 5 (priority fix)
├── High impression keywords with low QS
└── Keywords with QS decline vs previous month

STATUS INTERPRETATION:
──────────────────────
"Below average" = Problem, action required
"Average" = OK, room for improvement
"Above average" = Good, maintain
```

## Bidding Problems

### Smart Bidding Issues

```
SMART BIDDING TROUBLESHOOT
══════════════════════════

PROBLEM 1: DELIVERY STOPS/DROPS
────────────────────────────────
Symptom: Impressions suddenly dropped

Causes:
├── Target too aggressive
├── Budget too low
├── Competition increased
└── Tracking issue

Diagnosis:
├── Check bid strategy status
├── Compare target vs actual CPA/ROAS
├── Check conversion tracking
└── Review auction insights

Solution:
├── Relax target (20%)
├── Increase budget
├── Switch to "Maximize" (temporarily)
└── Fix tracking issues

PROBLEM 2: CPA/ROAS FAR FROM TARGET
─────────────────────────────────────
Symptom: Actual far above/below target

Causes:
├── Unrealistic target
├── Market changed
├── Insufficient conversions
└── Learning phase

Diagnosis:
├── Check historical CPA/ROAS
├── Compare target vs market benchmarks
├── Check conversion volume
└── Check learning status

Solution:
├── Adjust target to achievable
├── Use "Maximize" for data collection
├── Increase volume (budget/targeting)
└── Wait for learning complete

PROBLEM 3: ERRATIC PERFORMANCE
───────────────────────────────
Symptom: Large day-to-day swings

Causes:
├── Low conversion volume
├── Inconsistent demand
├── Budget limiting mid-day
└── Competitor auction dynamics

Diagnosis:
├── Check daily conversions (need 15+)
├── Check budget utilization pattern
├── Review hourly performance
└── Compare to historical volatility

Solution:
├── Increase conversions (budget/targeting)
├── Portfolio bid strategy (aggregate)
├── Smooth budget pacing
└── Accept some volatility (normal)

PROBLEM 4: NOT LEARNING
────────────────────────
Symptom: "Learning Limited" persists

See → "Learning Phase Tracker" skill
```

### Smart Bidding Issues

```
SMART BIDDING TROUBLESHOOT
══════════════════════════

PROBLEM 1: DELIVERY STOPS/DROPS
────────────────────────────────
Symptom: Impressions suddenly dropped

Causes:
├── Target too aggressive
├── Budget too low
├── Competition increased
└── Tracking issue

Diagnosis:
├── Check bid strategy status
├── Compare target vs actual CPA/ROAS
├── Check conversion tracking
└── Review auction insights

Solution:
├── Relax target (20%)
├── Increase budget
├── Switch to "Maximize" (temporarily)
└── Fix tracking issues

PROBLEM 2: CPA/ROAS FAR FROM TARGET
─────────────────────────────────────
Symptom: Actual far above/below target

Causes:
├── Unrealistic target
├── Market changed
├── Insufficient conversions
└── Learning phase

Diagnosis:
├── Check historical CPA/ROAS
├── Compare target vs market benchmarks
├── Check conversion volume
└── Check learning status

Solution:
├── Adjust target to achievable
├── Use "Maximize" for data collection
├── Increase volume (budget/targeting)
└── Wait for learning complete

PROBLEM 3: ERRATIC PERFORMANCE
───────────────────────────────
Symptom: Large day-to-day swings

Causes:
├── Low conversion volume
├── Inconsistent demand
├── Budget limiting mid-day
└── Competitor auction dynamics

Diagnosis:
├── Check daily conversions (need 15+)
├── Check budget utilization pattern
├── Review hourly performance
└── Compare to historical volatility

Solution:
├── Increase conversions (budget/targeting)
├── Portfolio bid strategy (aggregate)
├── Smooth budget pacing
└── Accept some volatility (normal)

PROBLEM 4: NOT LEARNING
────────────────────────
Symptom: "Learning Limited" persists

See → "Learning Phase Tracker" skill
```

## Google Ads Script: Performance Alert System

```javascript
/**
 * Performance Troubleshoot Alert System
 *
 * Detects and reports performance anomalies.
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Schedule: Daily at 8:00
 */

var CONFIG = {
  EMAIL: 'you@example.com',

  // Lookback periods
  COMPARE_DAYS: 7,
  BASELINE_DAYS: 14,

  // Alert thresholds (percentage change)
  ALERTS: {
    // Critical alerts (immediate attention)
    CONVERSIONS_DROP_CRITICAL: -0.50,  // -50%
    SPEND_ZERO: true,                   // No spend
    TRACKING_BROKEN: true,              // 0 conversions

    // Warning alerts
    CPA_SPIKE: 0.30,            // +30%
    ROAS_DROP: -0.25,           // -25%
    CTR_DROP: -0.20,            // -20%
    IMPRESSIONS_DROP: -0.30,    // -30%
    CONVERSIONS_DROP: -0.25     // -25%
  },

  // Minimum data for alerts
  MIN_IMPRESSIONS: 100,
  MIN_CLICKS: 20,
  MIN_CONVERSIONS: 3
};

function main() {
  var report = {
    critical: [],
    warnings: [],
    info: [],
    summary: {}
  };

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var campaignCount = 0;
  var alertCount = 0;

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var alerts = analyzeCampaignPerformance(campaign);

    report.critical = report.critical.concat(alerts.critical);
    report.warnings = report.warnings.concat(alerts.warnings);
    report.info = report.info.concat(alerts.info);

    alertCount += alerts.critical.length + alerts.warnings.length;
    campaignCount++;
  }

  report.summary = {
    campaignsAnalyzed: campaignCount,
    criticalAlerts: report.critical.length,
    warnings: report.warnings.length,
    timestamp: new Date().toISOString()
  };

  // Always send if critical alerts, otherwise only if warnings
  if (report.critical.length > 0 || report.warnings.length > 0) {
    sendAlertEmail(report);
  }

  Logger.log('Performance analysis complete');
  Logger.log('Campaigns: ' + campaignCount + ', Alerts: ' + alertCount);
}

function analyzeCampaignPerformance(campaign) {
  var name = campaign.getName();
  var alerts = { critical: [], warnings: [], info: [] };

  // Get stats for comparison periods
  var currentStats = campaign.getStatsFor('LAST_7_DAYS');
  var baselineStats = campaign.getStatsFor('LAST_14_DAYS');

  // Calculate current vs baseline
  var current = {
    impressions: currentStats.getImpressions(),
    clicks: currentStats.getClicks(),
    cost: currentStats.getCost(),
    conversions: currentStats.getConversions(),
    convValue: currentStats.getConversionValue()
  };

  // Baseline (previous period = last 14 days minus last 7 days)
  var baseline = {
    impressions: baselineStats.getImpressions() - current.impressions,
    clicks: baselineStats.getClicks() - current.clicks,
    cost: baselineStats.getCost() - current.cost,
    conversions: baselineStats.getConversions() - current.conversions,
    convValue: baselineStats.getConversionValue() - current.convValue
  };

  // Calculated metrics
  current.ctr = current.impressions > 0 ?
    current.clicks / current.impressions : 0;
  current.cpa = current.conversions > 0 ?
    current.cost / current.conversions : 0;
  current.roas = current.cost > 0 ?
    current.convValue / current.cost : 0;

  baseline.ctr = baseline.impressions > 0 ?
    baseline.clicks / baseline.impressions : 0;
  baseline.cpa = baseline.conversions > 0 ?
    baseline.cost / baseline.conversions : 0;
  baseline.roas = baseline.cost > 0 ?
    baseline.convValue / baseline.cost : 0;

  // CRITICAL ALERTS

  // Zero spend
  if (current.cost === 0 && baseline.cost > 0) {
    alerts.critical.push({
      campaign: name,
      type: 'NO_SPEND',
      message: 'No spend in last 7 days',
      baseline: baseline.cost.toFixed(2) + ' (previous week)'
    });
  }

  // Tracking broken (had conversions, now 0)
  if (current.conversions === 0 && baseline.conversions > 3) {
    alerts.critical.push({
      campaign: name,
      type: 'TRACKING_ISSUE',
      message: '0 conversions while previous period had ' + baseline.conversions.toFixed(0),
      action: 'Check conversion tracking'
    });
  }

  // Conversion drop critical
  if (baseline.conversions >= CONFIG.MIN_CONVERSIONS) {
    var convChange = (current.conversions - baseline.conversions) / baseline.conversions;
    if (convChange <= CONFIG.ALERTS.CONVERSIONS_DROP_CRITICAL) {
      alerts.critical.push({
        campaign: name,
        type: 'CONVERSION_CRASH',
        message: 'Conversions dropped by ' + (convChange * 100).toFixed(0) + '%',
        current: current.conversions.toFixed(0),
        baseline: baseline.conversions.toFixed(0)
      });
    }
  }

  // WARNINGS

  // Skip if insufficient data
  if (baseline.impressions < CONFIG.MIN_IMPRESSIONS) {
    return alerts;
  }

  // CPA spike
  if (baseline.cpa > 0 && current.cpa > 0) {
    var cpaChange = (current.cpa - baseline.cpa) / baseline.cpa;
    if (cpaChange >= CONFIG.ALERTS.CPA_SPIKE) {
      alerts.warnings.push({
        campaign: name,
        type: 'CPA_SPIKE',
        message: 'CPA increased by ' + (cpaChange * 100).toFixed(0) + '%',
        current: current.cpa.toFixed(2),
        baseline: baseline.cpa.toFixed(2)
      });
    }
  }

  // ROAS drop
  if (baseline.roas > 0 && current.roas > 0) {
    var roasChange = (current.roas - baseline.roas) / baseline.roas;
    if (roasChange <= CONFIG.ALERTS.ROAS_DROP) {
      alerts.warnings.push({
        campaign: name,
        type: 'ROAS_DROP',
        message: 'ROAS dropped by ' + (Math.abs(roasChange) * 100).toFixed(0) + '%',
        current: (current.roas * 100).toFixed(0) + '%',
        baseline: (baseline.roas * 100).toFixed(0) + '%'
      });
    }
  }

  // CTR drop
  if (baseline.ctr > 0) {
    var ctrChange = (current.ctr - baseline.ctr) / baseline.ctr;
    if (ctrChange <= CONFIG.ALERTS.CTR_DROP) {
      alerts.warnings.push({
        campaign: name,
        type: 'CTR_DROP',
        message: 'CTR dropped by ' + (Math.abs(ctrChange) * 100).toFixed(0) + '%',
        current: (current.ctr * 100).toFixed(2) + '%',
        baseline: (baseline.ctr * 100).toFixed(2) + '%'
      });
    }
  }

  // Impressions drop
  var impChange = (current.impressions - baseline.impressions) / baseline.impressions;
  if (impChange <= CONFIG.ALERTS.IMPRESSIONS_DROP) {
    alerts.warnings.push({
      campaign: name,
      type: 'IMPRESSIONS_DROP',
      message: 'Impressions dropped by ' + (Math.abs(impChange) * 100).toFixed(0) + '%',
      current: current.impressions,
      baseline: baseline.impressions
    });
  }

  return alerts;
}

function sendAlertEmail(report) {
  var subject = '[ALERT] Performance Issues - ' + AdsApp.currentAccount().getName();

  if (report.critical.length > 0) {
    subject = '[CRITICAL] ' + subject;
  }

  var body = 'Google Ads Performance Alert Report\n';
  body += '====================================\n';
  body += 'Generated: ' + new Date().toLocaleString() + '\n\n';

  body += 'SUMMARY:\n';
  body += '- Campaigns analyzed: ' + report.summary.campaignsAnalyzed + '\n';
  body += '- Critical alerts: ' + report.summary.criticalAlerts + '\n';
  body += '- Warnings: ' + report.summary.warnings + '\n\n';

  if (report.critical.length > 0) {
    body += 'CRITICAL ALERTS (Immediate Action Required):\n';
    body += '─────────────────────────────────────────────\n';

    for (var i = 0; i < report.critical.length; i++) {
      var alert = report.critical[i];
      body += '- ' + alert.campaign + '\n';
      body += '  Issue: ' + alert.message + '\n';
      if (alert.current) body += '  Current: ' + alert.current + '\n';
      if (alert.baseline) body += '  Baseline: ' + alert.baseline + '\n';
      if (alert.action) body += '  Action: ' + alert.action + '\n';
      body += '\n';
    }
  }

  if (report.warnings.length > 0) {
    body += 'WARNINGS:\n';
    body += '─────────\n';

    for (var j = 0; j < report.warnings.length; j++) {
      var warning = report.warnings[j];
      body += '- ' + warning.campaign + '\n';
      body += '  ' + warning.message + '\n';
      body += '  Current: ' + warning.current + ' | Baseline: ' + warning.baseline + '\n\n';
    }
  }

  body += '\n---\nGenerated by Performance Troubleshoot Alert System';
  body += '\nRecommendation: Review campaigns in Google Ads UI for full diagnosis.';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```