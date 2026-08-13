---
description: "Detect audience overlap issues in Meta campaigns. Find where you're competing against yourself and wasting budget. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Audience Overlap Detector

Detect and resolve audience overlap in Meta Ads campaigns
> Conditional: if include_recommendations
 with detailed fix recommendations.

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### OVERLAP SUMMARY
| Metric | Value |
|--------|-------|
| Active Ad Sets Scanned | |
| High Overlap Pairs | |
| Medium Overlap Pairs | |
| Est. Monthly Budget Waste | |

### HIGH OVERLAP PAIRS (Action Required)
| Ad Set A | Ad Set B | Overlap Type | Severity | Combined Spend | Fix |
|----------|----------|-------------|----------|----------------|-----|
(Sorted by combined spend descending)

### LOOKALIKE STACKING ISSUES
| Seed Audience | 1% LAL | 2% LAL | 3%+ LAL | Issue | Fix |
|---------------|--------|--------|---------|-------|-----|
Recommendation: Use non-overlapping bands (0-1%, 1-2%, 2-3%) or keep only the 1%.

### EXCLUSION GAPS
| Ad Set | Missing Exclusion | Impact | Priority |
|--------|-------------------|--------|----------|
(Ad sets that should exclude certain audiences but don't)

### PROPER EXCLUSION HIERARCHY
**Prospecting campaigns should exclude:**
- All purchasers (180 days)
- All leads (90 days)
- Website visitors (if retargeting runs separately)

**Retargeting campaigns should exclude:**
- Recent purchasers (based on purchase cycle)
- Already converted leads (if lead gen)

### ACTION PLAN
1. [Highest impact fix - estimated savings]
2. [Second fix]
3. [Third fix]

## EXECUTION STEPS

### Step 1: Discover Account
- `meta_list_ad_accounts()`

### Step 2: Pull All Active Ad Sets with Targeting

`meta_query(account_id="FROM_STEP_1", edge="adsets", params={"fields":"name,targeting,status,daily_budget,lifetime_budget,optimization_goal,campaign_id", "filtering":[{"field":"status","operator":"IN","value":["ACTIVE"]}], "limit":100})`

### Step 3: Pull Campaign Names for Context

`meta_query(account_id="FROM_STEP_1", edge="campaigns", params={"fields":"name,objective,status,buying_type", "filtering":[{"field":"status","operator":"IN","value":["ACTIVE"]}], "limit":50})`

### Step 4: Pull Ad Set Performance (to quantify waste)

`meta_get_insights(account_id="FROM_STEP_1", date_preset="last_30d", level="adset", fields=["adset_name","spend","impressions","reach","frequency","cpm","actions","cost_per_action_type"])`

### Step 5: Pull Custom Audiences List

`meta_query(account_id="FROM_STEP_1", edge="customaudiences", params={"fields":"name,subtype,approximate_count,data_source,lookalike_spec", "limit":100})`

### Step 6: Analyze Overlap

**Direct Overlap Detection:**
- Same custom_audience IDs in multiple ad sets = HIGH overlap
- Same lookalike seed with overlapping percentages (e.g., 1% and 2%) = HIGH overlap (1% is fully contained in 2%)
- Identical interest/behavior targeting across ad sets = HIGH overlap
- Same geo + age + gender with similar interests = MEDIUM overlap

**Indirect Overlap Detection:**
- Broad targeting (no interests) competing with interest-based targeting = MEDIUM overlap
- Retargeting ad sets without prospecting exclusions = HIGH overlap
- Lookalike audiences overlapping with their source custom audience = MEDIUM overlap

**Overlap Severity Scoring:**
```
HIGH (70-100% est. overlap):
  - Same custom audience in multiple ad sets
  - Nested lookalikes (1% inside 3%)
  - Identical interest stacks

MEDIUM (30-70% est. overlap):
  - Similar but not identical interests
  - Broad vs specific in same geo
  - LAL from similar seeds

LOW (10-30% est. overlap):
  - Different interest categories, same geo
  - Different age ranges with same interests
```

**Budget Waste Estimation:**
- For each overlapping pair: overlap_pct * min(spend_a, spend_b) * 0.3 = estimated waste
- The 0.3 multiplier accounts for auction dynamics (overlap doesn't mean 100% waste)

### Step 7: Present Results
Follow OUTPUT FORMAT above EXACTLY. Fill all tables with real data.

## EDGE CASES
- Single active ad set: No overlap possible - note "Only 1 active ad set found, no overlap analysis needed"
- No custom audiences: Skip Custom Audiences and LAL sections, analyze interest/demographic targeting only
- Advantage+ Sales campaigns (formerly ASC): These use Meta's ML targeting - note "Advantage+ campaigns manage audiences automatically, overlap analysis limited to non-Advantage+ ad sets"
- Advantage+ Audience (broad targeting): Flag that broad targeting may overlap with everything - recommend consolidation
- All ad sets in one campaign: Lower concern (Meta's internal auction dedup helps within a campaign) - note this
- Advantage Campaign Budget active: Note that campaign-level budget reduces but doesn't eliminate overlap waste
- Very large account (100+ ad sets): Focus analysis on top 20 ad sets by spend