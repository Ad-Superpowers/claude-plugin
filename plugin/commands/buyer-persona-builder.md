---
description: "Generate detailed buyer personas combining research with optional platform audience data. Creates 2-4 actionable personas with platform-specific targeting recommendations. (requires Pro subscription)"
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Buyer Persona Builder

Generate 3 data-driven buyer personas for [specify company_name] in [specify industry]. Combines industry research with platform audience data to create actionable personas with targeting recommendations.

**Parameters:** b2c_product | Existing customers: Not provided

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### EXECUTIVE SUMMARY
Based on [evaluate at run time: "platform data and " if ga4_property_id else ""]industry research, 3 buyer personas identified for [specify company_name].
- Primary persona: [Name] ([X]% of ideal customers)
- Secondary personas: [Names]

### PERSONA OVERVIEW
| Persona | Segment | Est. % of Market | Priority | Best Platform |
|---------|---------|------------------|----------|---------------|
| [Name 1] | [Segment] | [XX]% | Primary | [Platform] |
| [Name 2] | [Segment] | [XX]% | Secondary | [Platform] |
| [Name 3] | [Segment] | [XX]% | Tertiary | [Platform] |

### PERSONA [N]: [NAME] - "[Archetype]"

**Identity:** [One sentence describing this persona]

**Demographics:**
| Attribute | Details |
|-----------|---------|
| Age | [XX-XX] |
| Gender | [Distribution] |
| Location | [Geographic focus] |
| Income | [Range] |
| Education | [Level] |

> Conditional: if product_type in ["b2b_saas", "b2b_services"]
| Job Title | [Title] |
| Company Size | [Range] |
> Otherwise
| Family Status | [Status] |

**Goals & Pain Points:**
- Goals: [Top 3 goals as numbered list]
- Pain points: [Top 3 frustrations - use emotional language with representative quotes]
- Desired outcome: [What success looks like]

**Buying Behavior:**
- Decision drivers (ranked): [e.g., price, quality, convenience]
- Information sources: Discovery → Research → Validation
- Key objections: "[Objection]" → Counter: [How to address]
- Triggers: [What prompts purchase - seasonal, life event, pain threshold]
- Budget range & decision timeline

**Platform Behavior:**
| Platform | Usage | Best Content Type | Best Time |
|----------|-------|-------------------|-----------|
| Facebook | [H/M/L] | [Type] | [Time] |
| Instagram | [H/M/L] | [Type] | [Time] |
| LinkedIn | [H/M/L] | [Type] | [Time] |
| TikTok | [H/M/L] | [Type] | [Time] |
| Google | [Search behavior] | [Keywords] | [Intent] |

**Targeting Recommendations:**

*Meta:* Age [XX-XX], interests [[list]], behaviors [[list]], custom audiences [[source]], placements [[recommended]]

*Google Ads:* High-intent keywords [[list]], audience segments [in-market/affinity], negative keywords [[exclusions]]

> Conditional: if product_type in ["b2b_saas", "b2b_services"]
*LinkedIn:* Job titles [[list]], functions [[list]], seniority [[level]], company size [[range]], industries [[list]]

*TikTok:* Age [XX-XX], interests [[categories]], content strategy: hook style, themes, creator style (UGC/polished/educational)

**Messaging:**
- Value prop: "[Tailored to this persona's pain points]"
- Key messages: [3 messages addressing pain point, goal, objection]
- Tone: [Descriptors with example phrases]
- Words that resonate vs avoid

[REPEAT for each persona]

### PERSONA COMPARISON MATRIX
| Attribute | Persona 1 | Persona 2 | Persona 3 |
|-----------|-----------|-----------|-----------|
| Age | [Range] | [Range] | [Range] |
| Primary Platform | [Platform] | [Platform] | [Platform] |
| Main Pain Point | [Pain] | [Pain] | [Pain] |
| Price Sensitivity | [H/M/L] | [H/M/L] | [H/M/L] |
| Decision Speed | [F/M/S] | [F/M/S] | [F/M/S] |
| Best Ad Format | [Format] | [Format] | [Format] |
| Estimated CAC | [Amount] | [Amount] | [Amount] |

### CAMPAIGN STRUCTURE
| Campaign | Persona | Budget % | Platforms | Objective |
|----------|---------|----------|-----------|-----------|
| Prospecting 1 | [Primary] | [XX]% | [Platforms] | [Objective] |
| Prospecting 2 | [Secondary] | [XX]% | [Platforms] | [Objective] |
| Prospecting 3 | [Tertiary] | [XX]% | [Platforms] | [Objective] |

**A/B testing priority:**
1. [Test messaging for Persona 1 vs 2]
2. [Test creative style for Persona X]
3. [Test platform allocation]

### DATA CONFIDENCE
| Data Point | Source | Confidence |
|------------|--------|------------|
| Demographics | [Source] | [H/M/L] |
| Psychographics | [Source] | [H/M/L] |
| Platform behavior | [Source] | [H/M/L] |
| Buying behavior | [Source] | [H/M/L] |

**Validation next steps:** Run creative tests per persona, track conversion rates by targeting, survey customers in 90 days.

## EXECUTION STEPS

### Step 1: Research Industry Buyers
Research typical buyers in [specify industry]: demographics, job titles (B2B), pain points, buying motivations, decision process, trusted information sources, objections. Also analyze competitor targeting for gaps.

> Conditional: if product_type == "b2b_saas" or product_type == "b2b_services"

For B2B: identify decision makers, influencers, end users, budget holders, buying committee size, sales cycle length.

### Step 2: Gather Platform Data (if connected)

> Conditional: if ga4_property_id

**GA4:** `ga4_run_report(property_id="[specify ga4_property_id]", start_date="90daysAgo", end_date="today", metrics=["activeUsers","sessions","conversions"], dimensions=["userAgeBracket","userGender","country","deviceCategory"])`

Also run: `ga4_run_report(property_id="[specify ga4_property_id]", metrics=["sessions","totalUsers","newUsers"], dimensions=["sessionDefaultChannelGrouping"], start_date="90daysAgo", end_date="today")`

**Meta:** `meta_get_insights(account_id=account_id, date_preset="last_90d", level="account", breakdowns=["age","gender","country"])`

**LinkedIn:** `linkedin_get_analytics(account_id=account_id, fields=["impressions","clicks"], demographic_breakdowns=["JOB_FUNCTION","SENIORITY","INDUSTRY","COMPANY_SIZE"])`

### Step 3: Generate Personas
Combine research + platform data. For each persona, fill in all sections from the per-persona template: Identity, Demographics, Goals & Pain Points, Buying Behavior, Platform Behavior, Targeting Recommendations, Messaging.

### Step 4: Create Targeting Recommendations
Translate each persona into concrete platform targeting parameters. Be specific (actual interest names, audience segments, keyword lists).

### Step 5: Present Results
Follow OUTPUT FORMAT above EXACTLY. Fill all tables with real data.

## EDGE CASES
- **No platform data available:** Build research-only personas, mark Data Confidence as LOW, recommend connecting platforms for enrichment
- **B2B vs B2C:** B2B: focus on job roles, buying committees, business outcomes. B2C: focus on lifestyle, emotions, purchase triggers
- **Single platform only:** Still create full personas but note limited data; targeting section focuses on available platform
- **No existing customer data:** Rely on industry research and competitor analysis; flag all data as "hypothesis - validate with real data"
- **Very niche industry:** May only support 2 personas; don't force a third if segments don't differ meaningfully
- **Mixed B2B/B2C:** Create separate personas for each buyer type, clearly label which is B2B vs B2C