---
name: buyer-persona-framework
description: "This skill should be used when the user asks to \"create buyer personas\", \"define target audiences\", \"build an ICP\", mentions \"customer segmentation\", \"audience research\", or \"translate personas into ad targeting\". Do NOT use for: channel selection decisions (use channel-selection-framework), competitor audience analysis (use competitor-analysis-toolkit), or market size estimation (use market-sizing-guide)."
---
# Buyer Persona Framework for Advertising

## Purpose

Help advertisers create actionable buyer personas that translate directly into ad platform targeting parameters. Moves beyond generic "marketing personas" to advertising-ready audience definitions.

## When to Use This Skill

Invoke when user mentions:
- **Persona creation:** "Help me create buyer personas"
- **Audience definition:** "Who should we target?"
- **Targeting translation:** "How do I target this persona in Meta/Google?"
- **Segmentation:** "How do I segment my audience?"
- **ICP (Ideal Customer Profile):** B2B persona discussions

---

## The Advertising Persona Framework

### Standard Marketing Persona vs. Ad-Ready Persona

| Standard Persona | Ad-Ready Persona |
|------------------|------------------|
| "Sarah, 35, marketing manager" | Demographics + Platform behaviors |
| "Likes yoga and coffee" | Targetable interests & behaviors |
| "Values work-life balance" | Purchase triggers & timing |
| "Pain point: too busy" | Keywords searched, content consumed |
| Generic description | Platform-specific targeting parameters |

### The 7 Components of an Ad-Ready Persona

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           AD-READY PERSONA FRAMEWORK                          │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. IDENTITY          ─────────────────────────────────────────────────────  │
│     Name, archetype, one-line summary                                        │
│                                                                              │
│  2. DEMOGRAPHICS      ─────────────────────────────────────────────────────  │
│     Age, gender, location, income, education, job (B2B)                      │
│     → Directly maps to platform targeting                                    │
│                                                                              │
│  3. PSYCHOGRAPHICS    ─────────────────────────────────────────────────────  │
│     Values, personality, interests, lifestyle                                │
│     → Maps to interest & affinity targeting                                  │
│                                                                              │
│  4. PAIN POINTS & GOALS  ──────────────────────────────────────────────────  │
│     What they're trying to achieve/avoid                                     │
│     → Informs messaging and creative                                         │
│                                                                              │
│  5. BUYING BEHAVIOR   ─────────────────────────────────────────────────────  │
│     Decision drivers, objections, triggers                                   │
│     → Informs funnel strategy and timing                                     │
│                                                                              │
│  6. PLATFORM BEHAVIOR ─────────────────────────────────────────────────────  │
│     Where they spend time, content preferences, device                       │
│     → Informs platform selection and placement                               │
│                                                                              │
│  7. TARGETING PARAMETERS  ─────────────────────────────────────────────────  │
│     Ready-to-use platform targeting                                          │
│     → Copy directly into ad platforms                                        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Persona Building Process

### Step 1: Data Collection

**First-Party Data Sources:**
| Source | Insights Available |
|--------|-------------------|
| GA4 | Demographics, interests, device, acquisition |
| CRM | Purchase history, lifecycle stage, engagement |
| Customer surveys | Psychographics, pain points, preferences |
| Sales team | Objections, decision process, triggers |
| Support tickets | Pain points, language, frustrations |
| Social listening | Interests, sentiment, conversations |

**Platform Data Sources:**
| Platform | Data Available |
|----------|---------------|
| Meta Audience Insights | Demographics, page likes, behaviors |
| Google Analytics | Demographics, interests, in-market |
| LinkedIn | Job titles, skills, company size |
| TikTok | Interest categories, trending content |

**Research Sources:**
| Source | Best For |
|--------|----------|
| Industry reports | Market-level demographics |
| Competitor analysis | Audience they target |
| Keyword research | Search intent and language |
| Social media | Content preferences, influencers |

### Step 2: Pattern Identification

Look for clusters in:
1. **Demographics** - Are there 2-3 distinct age/income groups?
2. **Motivations** - What different jobs-to-be-done exist?
3. **Behaviors** - How do different groups research/buy?
4. **Platforms** - Where do different segments engage?

### Step 3: Persona Prioritization

Score each persona on:

| Factor | Weight | Scoring |
|--------|--------|---------|
| Market size | 25% | 1-5 based on addressable audience |
| Revenue potential | 25% | LTV × conversion likelihood |
| Ease of targeting | 20% | Platform availability of targeting |
| Competition | 15% | How crowded is this segment |
| Strategic fit | 15% | Alignment with business goals |

**Formula:** Priority Score = Σ (Factor score × Weight)

---

## Persona Templates by Business Type

### B2C E-commerce Persona Template

```
═══════════════════════════════════════════════════════════════════════════════
PERSONA: [Name] - "[Archetype Title]"
═══════════════════════════════════════════════════════════════════════════════

📋 SUMMARY
"[One sentence capturing who they are and what they want]"

👤 DEMOGRAPHICS
───────────────────────────────────────────────
Age:           [Range, e.g., 25-34]
Gender:        [Male/Female/All]
Location:      [Countries/regions]
Income:        €[Range] / year
Education:     [Level]
Family status: [Single/Married/Children]
Home:          [Own/Rent, Urban/Suburban]

🧠 PSYCHOGRAPHICS
───────────────────────────────────────────────
Values:
• [Value 1 - e.g., "Values quality over price"]
• [Value 2]
• [Value 3]

Personality:
• [Trait 1 - e.g., "Research-driven, reads reviews"]
• [Trait 2]

Interests:
• [Interest 1]
• [Interest 2]
• [Interest 3]

Lifestyle:
• [Lifestyle descriptor]
• [How they spend free time]

😤 PAIN POINTS
───────────────────────────────────────────────
1. "[Pain point in their words]"
   → Messaging angle: [How to address]

2. "[Pain point]"
   → Messaging angle: [How to address]

3. "[Pain point]"
   → Messaging angle: [How to address]

🎯 GOALS
───────────────────────────────────────────────
Primary:   [What they're trying to achieve]
Secondary: [Supporting goals]
Emotional: [How they want to feel]

💳 BUYING BEHAVIOR
───────────────────────────────────────────────
Decision drivers (ranked):
1. [Primary driver - e.g., price, quality, reviews]
2. [Secondary]
3. [Tertiary]

Research behavior:
• [Where they research - Google, social, influencers]
• [How long they research before buying]

Purchase triggers:
• [Trigger 1 - e.g., sale, seasonal need, life event]
• [Trigger 2]

Objections:
• "[Objection 1]" → Counter: [Response]
• "[Objection 2]" → Counter: [Response]

Budget: €[Range] for this category
Frequency: [One-time / Monthly / Yearly]

📱 PLATFORM BEHAVIOR
───────────────────────────────────────────────
| Platform   | Usage      | Content Preference | Best Time   |
|------------|------------|-------------------|-------------|
| Instagram  | [Daily/etc]| [Reels/Stories]   | [Morning]   |
| Facebook   | [Usage]    | [Content type]    | [Time]      |
| TikTok     | [Usage]    | [Content type]    | [Time]      |
| Google     | [Behavior] | [Search intent]   | [When]      |
| YouTube    | [Usage]    | [Content type]    | [Time]      |

Device: [Mobile-first / Desktop / Both]

🎯 TARGETING PARAMETERS
───────────────────────────────────────────────

META ADS:
• Demographics: Age [X-X], [Gender], [Locations]
• Interests: [Interest 1], [Interest 2], [Interest 3]
• Behaviors: [Behavior 1], [Behavior 2]
• Custom audiences: [Website visitors, purchasers, etc.]
• Lookalike: Based on [source]

GOOGLE ADS:
• In-market: [Segment 1], [Segment 2]
• Affinity: [Segment 1], [Segment 2]
• Custom intent keywords: [Keyword 1], [Keyword 2]
• Search keywords: [Keywords with intent]

TIKTOK ADS:
• Interests: [Category 1], [Category 2]
• Behaviors: [Behavior 1]
• Creator similar: [Type of creators they follow]

📝 MESSAGING GUIDELINES
───────────────────────────────────────────────
Tone: [Friendly/Professional/Playful/Authoritative]

Key messages:
1. [Message addressing main pain point]
2. [Message addressing main goal]
3. [Differentiator message]

Words that resonate: [Word 1], [Word 2], [Word 3]
Words to avoid: [Word 1], [Word 2]

Sample headline: "[Example headline]"
Sample CTA: "[Example CTA]"
```

### B2B SaaS Persona Template

```
═══════════════════════════════════════════════════════════════════════════════
ICP PERSONA: [Name] - "[Role/Title]"
═══════════════════════════════════════════════════════════════════════════════

📋 SUMMARY
"[One sentence: role, challenge, and what they need]"

👤 PROFESSIONAL PROFILE
───────────────────────────────────────────────
Job title:      [Title]
Department:     [Marketing/Sales/IT/etc.]
Seniority:      [IC/Manager/Director/VP/C-Suite]
Reports to:     [Title they report to]
Team size:      [If manages people]

Company profile:
• Industry:     [Industry]
• Size:         [Employee count]
• Revenue:      €[Range]
• Stage:        [Startup/Scale-up/Enterprise]

BUYING ROLE
───────────────────────────────────────────────
Role in purchase:
• [ ] Decision maker (final authority)
• [ ] Influencer (recommends solutions)
• [ ] User (will use the product)
• [ ] Gatekeeper (controls access)
• [ ] Budget holder

Other stakeholders: [Who else is involved]

😤 PROFESSIONAL PAIN POINTS
───────────────────────────────────────────────
1. "[Professional challenge]"
   KPI impacted: [Metric they're measured on]
   → Position product as: [How we help]

2. "[Challenge]"
   KPI impacted: [Metric]
   → Position product as: [How we help]

🎯 GOALS & KPIs
───────────────────────────────────────────────
Professional goals:
• [Goal 1 - tied to their metrics]
• [Goal 2]

Measured on:
• [KPI 1 - e.g., revenue growth, cost reduction]
• [KPI 2]

Career motivation: [Promotion, recognition, etc.]

💼 BUYING BEHAVIOR (B2B)
───────────────────────────────────────────────
Research sources:
• [Industry publications, G2, peers, events]

Decision criteria:
1. [Criterion 1 - e.g., ROI, integration, support]
2. [Criterion 2]
3. [Criterion 3]

Objections:
• "[Budget objection]" → Counter: [ROI story]
• "[Risk objection]" → Counter: [Social proof]
• "[Timing objection]" → Counter: [Cost of inaction]

Budget authority: €[Range] without approval
Sales cycle: [X weeks/months]
Contract preference: [Monthly/Annual]

BUYING COMMITTEE
───────────────────────────────────────────────
| Role           | Title        | Concerns        |
|----------------|--------------|-----------------|
| Economic buyer | [Title]      | [Main concern]  |
| Technical buyer| [Title]      | [Main concern]  |
| User buyer     | [Title]      | [Main concern]  |
| Champion       | [Title]      | [Motivation]    |

📱 PLATFORM BEHAVIOR
───────────────────────────────────────────────
| Platform   | Usage       | Content         |
|------------|-------------|-----------------|
| LinkedIn   | [High/Med]  | [Content type]  |
| Industry pubs| [Usage]   | [Content type]  |
| Email      | [Behavior]  | [Preferences]   |
| Events     | [Attendance]| [Types]         |
| Podcasts   | [Usage]     | [Topics]        |

🎯 TARGETING PARAMETERS
───────────────────────────────────────────────

LINKEDIN ADS:
• Job titles: [Title 1], [Title 2], [Title 3]
• Job functions: [Function 1], [Function 2]
• Seniority: [Level]
• Industries: [Industry 1], [Industry 2]
• Company size: [Range]
• Skills: [Skill 1], [Skill 2]

GOOGLE ADS:
• In-market: [B2B segment 1], [Segment 2]
• Custom intent: [Keywords they search]
• Placements: [Industry sites]

META ADS:
• Job titles (limited): [If available]
• Interests: [Industry interests]
• Behaviors: [Business behaviors]

📝 MESSAGING GUIDELINES
───────────────────────────────────────────────
Tone: [Professional/Expert/Peer-to-peer]

Lead with: [ROI/Efficiency/Innovation/Risk reduction]

Proof points needed:
• [Case study type they'd trust]
• [Metrics that matter to them]
• [Social proof format]

Content preferences:
• TOFU: [Ebooks, reports, benchmarks]
• MOFU: [Case studies, webinars, comparisons]
• BOFU: [Demos, trials, ROI calculators]
```

---

## Industry Persona Archetypes

### E-commerce / D2C

| Archetype | Description | Targeting Approach |
|-----------|-------------|-------------------|
| **The Researcher** | Reads every review, compares extensively | Target with comparison content, detailed specs |
| **The Impulse Buyer** | Decides quickly, responds to urgency | Strong CTAs, limited-time offers |
| **The Loyalist** | Sticks with brands they trust | Retargeting, loyalty programs, upsells |
| **The Deal Hunter** | Waits for discounts | Sale-focused campaigns, price alerts |
| **The Aspirational** | Buys for status/identity | Lifestyle imagery, influencer content |
| **The Practical** | Buys for function, not emotion | Feature-focused, value messaging |

### B2B SaaS

| Archetype | Description | Targeting Approach |
|-----------|-------------|-------------------|
| **The Innovator** | Early adopter, wants cutting-edge | New features, innovation messaging |
| **The ROI-Focused** | Needs clear business case | ROI calculators, case studies with numbers |
| **The Risk-Averse** | Wants proven, safe choice | G2 reviews, enterprise logos, security |
| **The Overwhelmed** | Drowning in work, needs simple | Ease of use, quick wins, automation |
| **The Builder** | Technical, wants flexibility | API docs, customization, integrations |
| **The Delegator** | Will hand off to team | Team features, onboarding, support |

### Professional Services

| Archetype | Description | Targeting Approach |
|-----------|-------------|-------------------|
| **The First-Timer** | Never hired this service before | Education, process explanation, trust |
| **The Upgrader** | Current provider not meeting needs | Comparison, switching incentives |
| **The Referral-Seeker** | Relies on recommendations | Testimonials, case studies, reviews |
| **The DIY-to-DFY** | Tried doing it themselves | Pain of DIY, time savings, expertise |

---

## Platform Targeting Translation

### Demographics to Platform Parameters

| Persona Element | Meta | Google | LinkedIn | TikTok |
|-----------------|------|--------|----------|--------|
| Age 25-34 | Age: 25-34 | Demographics | Age: 25-34 | Age: 25-34 |
| Female | Gender: Female | Demographics | N/A | Gender: Female |
| High income | Income: Top 10% | Household income | N/A | N/A |
| College educated | Education level | N/A | Degrees | N/A |
| Parents | Parents | Parental status | N/A | N/A |
| Homeowners | Homeowners | Homeownership | N/A | N/A |
| Urban | Location + behavior | Location | N/A | Location |

### Interests to Platform Parameters

| Interest Category | Meta Interests | Google Affinity | LinkedIn | TikTok |
|-------------------|----------------|-----------------|----------|--------|
| Fitness | Fitness, Gym, Yoga | Health & Fitness | N/A | Fitness & Sports |
| Luxury | Luxury goods | Luxury shoppers | N/A | Luxury |
| Technology | Technology, Gadgets | Technophiles | Skills | Technology |
| Business | Business, Entrepreneurship | Business prof. | Industries | Business |
| Travel | Travel, Adventure | Travel buffs | N/A | Travel |

### Behaviors to Platform Parameters

| Behavior | Meta | Google | LinkedIn | TikTok |
|----------|------|--------|----------|--------|
| Recent purchaser | Engaged shoppers | In-market | N/A | N/A |
| Business owner | Small business owners | N/A | Company size: 1-10 | N/A |
| Frequent traveler | Frequent travelers | Travel in-market | N/A | N/A |
| Tech early adopter | Early adopters | Custom intent | Skills | N/A |
| Online buyer | Online purchases (30d) | N/A | N/A | N/A |

---

## Persona Validation Checklist

Before finalizing a persona, validate:

**Data Quality**
- [ ] Based on actual customer data (not assumptions)
- [ ] Validated with customer interviews/surveys
- [ ] Cross-referenced with platform data
- [ ] Sales team agrees with characterization

**Targetability**
- [ ] Can target in Meta with available options
- [ ] Can target in Google with available options
- [ ] Can target in LinkedIn (if B2B)
- [ ] Audience size is sufficient (>100K for broad, >10K for niche)

**Actionability**
- [ ] Clear messaging angles identified
- [ ] Distinct from other personas
- [ ] Team understands how to create content for them
- [ ] Measurable (can track performance by persona)

**Completeness**
- [ ] All 7 framework components filled
- [ ] Platform-specific targeting ready
- [ ] Messaging guidelines included
- [ ] Prioritization score calculated

---

## Common Persona Mistakes

### Mistake 1: Too Many Personas
**Problem:** 10+ personas dilute focus and budget
**Solution:** Maximum 3-4 personas, 1-2 primary

### Mistake 2: Demographic-Only Personas
**Problem:** "Women 25-45" isn't actionable
**Solution:** Include psychographics, behaviors, and pain points

### Mistake 3: Aspirational vs. Actual
**Problem:** Describing who you wish bought, not who does
**Solution:** Base on actual customer data

### Mistake 4: Static Personas
**Problem:** Created once, never updated
**Solution:** Quarterly review with performance data

### Mistake 5: Not Translating to Targeting
**Problem:** Nice document, but can't use it
**Solution:** Always include platform-specific targeting

---

## Output Template

When creating personas, provide:

```
## Buyer Personas for [Company]

### Overview
- Total personas: [X]
- Primary: [Name] ([X]% of budget allocation)
- Secondary: [Names]

### Persona 1: [Name]
[Use template from above based on B2C/B2B]

### Persona 2: [Name]
[Use template]

### Persona Comparison Matrix
| Attribute | Persona 1 | Persona 2 | Persona 3 |
|-----------|-----------|-----------|-----------|
| Age | [Range] | [Range] | [Range] |
| Primary platform | [Platform] | [Platform] | [Platform] |
| Main pain point | [Pain] | [Pain] | [Pain] |
| Decision driver | [Driver] | [Driver] | [Driver] |
| Est. CAC | €[X] | €[X] | €[X] |
| Budget allocation | [X]% | [X]% | [X]% |

### Campaign Structure Recommendation
[How to structure campaigns by persona]

### Next Steps
1. [Validate with customer interviews]
2. [Set up audience segments in platforms]
3. [Create persona-specific creative]
4. [Run tests to compare performance]
```

---

## Optional: Enrich with Live Data

If the user has connected accounts, ground persona demographics in actual audience data rather than assumptions:

```python
# Pull real demographic breakdown from GA4
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    start_date="30daysAgo",
    end_date="today",
    metrics=["totalUsers", "sessions"],
    dimensions=["userAgeBracket", "userGender"]
)
```

```python
# Cross-reference with Meta audience insights for top-performing campaigns
meta_get_insights(account_id="act_XXXXX", level="campaign", date_preset="last_30d", fields=["campaign_name","spend","actions"])
```

Compare GA4 demographics against what you assumed in the persona framework. Surprises (e.g., older audience than expected) should update persona priorities and platform channel mix.

*Last updated: February 2026*
