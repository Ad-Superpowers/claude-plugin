---
name: linkedin-content-strategy
description: "This skill should be used when the user asks to \"choose a LinkedIn ad format\", \"build a B2B content funnel on LinkedIn\", \"compare carousel vs video on LinkedIn\", \"create Thought Leader Ads\", or mentions \"LinkedIn ad format\", \"Sponsored Content strategy\", or \"LinkedIn creative best practices\". Do NOT use for: lead form optimization (use linkedin-lead-gen-optimizer), campaign scaling (use linkedin-campaign-scaling-guide), or ABM targeting (use linkedin-abm-targeting-strategy)."
---

# LinkedIn Ad Format Selection & Content Strategy

## Purpose

Guide advertisers through LinkedIn's complex ad format landscape with data-driven format selection, B2B content funnel design, and format-specific creative optimization. The right format choice can improve performance by 2-4x; the wrong choice wastes budget on formats misaligned with the objective.

## When to Use This Skill

Invoke when user mentions:
- **Format selection:** "Which LinkedIn ad format should I use?"
- **Content strategy:** "What content works best on LinkedIn?"
- **B2B funnel:** "How do I build a content funnel on LinkedIn?"
- **Thought leadership:** "How do I position as a thought leader via ads?"
- **Creative best practices:** "What specs and guidelines for LinkedIn ads?"
- **Format comparison:** "Carousel vs single image vs video on LinkedIn?"

## Required Tools

| Tool | Purpose |
|------|---------|
| `linkedin_query` | Pull campaign data, ad formats, and creative configurations |
| `linkedin_get_creatives_with_images` | Retrieve ad creatives with visual assets for analysis |

---

## Part 1: LinkedIn Ad Format Catalog

### Format Overview with Performance Benchmarks

| Format | Avg CTR | Avg CPM | Avg CPC | Best For | Min Budget |
|--------|---------|---------|---------|----------|------------|
| Single Image | 0.40-0.65% | €25-50 | €5-12 | Lead gen, traffic, awareness | €30/day |
| Carousel | 0.35-0.55% | €20-45 | €6-14 | Storytelling, product features | €30/day |
| Video | 0.30-0.50% | €20-40 | €7-15 | Brand awareness, thought leadership | €50/day |
| Document Ads | 0.50-0.80% | €15-35 | €4-10 | Gated content, education | €30/day |
| Message Ads (InMail) | 25-40% open rate | N/A | €0.50-1.50/send | Direct outreach, events, high-value offers | €50/day |
| Conversation Ads | 40-60% open rate | N/A | €0.30-1.00/send | Multi-path journeys, qualification (deprecated EU/EEA; being phased out globally) | €50/day |
| Text Ads | 0.02-0.05% | €5-15 | €3-8 | Low-budget awareness, retargeting | €10/day |
| Dynamic Ads | 0.08-0.15% | €10-25 | €8-20 | Follower growth, job applicants | €25/day |
| Event Ads | 0.45-0.70% | €20-40 | €5-12 | Event registration, webinars | €30/day |

---

## Part 2: Format Selection Decision Tree

### Primary Decision: What Is the Campaign Objective?

```
                         What is your primary objective?
                                    │
         ┌──────────┬───────────────┼───────────────┬──────────────┐
         ▼          ▼               ▼               ▼              ▼
    Brand         Lead           Website        Event          Direct
   Awareness    Generation      Traffic      Registration    Outreach
         │          │               │               │              │
         ▼          ▼               ▼               ▼              ▼
    Video or     Single Image    Single Image    Event Ad      Message Ad
    Document     + Lead Form     or Carousel                  or Conv. Ad
    Ads               │               │
                      ▼               ▼
               Is content         Is message
               educational?       complex?
               │         │        │         │
               Yes       No       Yes       No
               ▼         ▼        ▼         ▼
           Document   Single   Carousel   Single
           Ads        Image               Image
```

### Secondary Decision: Audience Size and Budget

```
Audience size < 50,000?
├── Yes → Use Message Ads or Conversation Ads (higher per-contact cost but guaranteed delivery)
└── No → Use Sponsored Content formats (better scale economics)

Daily budget < €30?
├── Yes → Text Ads only (lowest minimum, widest reach per euro)
└── No → Full format selection applies

Campaign duration < 14 days?
├── Yes → Single Image (fastest to optimize, least learning period)
└── No → Any format (enough time for LinkedIn's algorithm to learn)
```

### Format-Objective Fit Matrix

| Objective | Best Format | Second Choice | Avoid |
|-----------|-------------|---------------|-------|
| Brand awareness (broad) | Video | Document Ads | Message Ads |
| Thought leadership | Document Ads | Video | Text Ads |
| Lead generation (volume) | Single Image + Lead Form | Carousel + Lead Form | Message Ads |
| Lead generation (quality) | Message Ads | Conversation Ads | Text Ads |
| Content distribution | Document Ads | Carousel | Message Ads |
| Event registration | Event Ads | Conversation Ads | Text Ads |
| Product demo requests | Conversation Ads | Message Ads | Document Ads |
| Retargeting | Single Image | Carousel | Message Ads |
| Follower growth | Dynamic Ads | Video | Message Ads |
| Job applications | Dynamic Ads | Single Image | Carousel |

---

## Part 3: Format-Specific Creative Best Practices

### Single Image Ads

**Specs:**
- Image: 1200x627px (landscape) or 1080x1080px (square)
- Headline: 70 characters max (truncated on mobile after 70)
- Description: 100 characters max
- Introductory text: 150 characters above fold (600 max, truncated with "...see more")

**Performance rules:**
- Square (1:1) images get 10-15% higher CTR than landscape on mobile
- People in images outperform product shots by 20-30%
- Clear, readable text overlay (max 20% of image area)
- High contrast CTA button area in bottom-right quadrant
- Avoid stock photography; authentic imagery wins

**Intro text formula:**
```
Line 1: Hook with a stat, question, or bold claim (stop the scroll)
Line 2: Bridge to the problem your audience faces
Line 3: Tease the solution without revealing everything
Line 4: Clear CTA with value proposition
```

**Example structure:**
```
78% of CFOs say they can't trust their marketing attribution data.

Yet most B2B companies still make budget decisions based on last-click.

We built a framework that reconciles GA4, LinkedIn, and CRM data
into a single source of truth.

Download the attribution playbook →
```

### Carousel Ads

**Specs:**
- 2-10 cards (optimal: 4-6 cards)
- Card image: 1080x1080px (square only)
- Card headline: 45 characters max
- Card description: Not shown on mobile (desktop only)
- Introductory text: same as single image

**Performance rules:**
- First card must be the strongest hook (50% of users don't swipe)
- Swipe rate benchmark: 15-25% swipe to card 2
- Completion rate benchmark: 5-12% reach final card
- Use sequential storytelling, not random slides
- Final card must have the strongest CTA

**Carousel narrative structures:**

```
STRUCTURE 1: Problem → Solution Journey (best for lead gen)
Card 1: State the problem with a stat
Card 2: Show why current solutions fail
Card 3: Introduce your approach
Card 4: Show key benefit #1
Card 5: Show key benefit #2
Card 6: CTA with social proof

STRUCTURE 2: Listicle (best for awareness/engagement)
Card 1: "5 Things Every [Role] Should Know About [Topic]"
Card 2: Thing #1
Card 3: Thing #2
Card 4: Thing #3
Card 5: Things #4-5 (combine to create urgency)
Card 6: CTA to get the full list/guide

STRUCTURE 3: Case Study (best for consideration)
Card 1: Client name + headline result
Card 2: The challenge they faced
Card 3: What they tried before
Card 4: The solution (your product/service)
Card 5: Key metrics/results
Card 6: CTA to get similar results
```

### Video Ads

**Specs:**
- Aspect ratio: 1:1 (square, best engagement) or 16:9 (landscape) or 9:16 (vertical, mobile-first)
- Length: 15-90 seconds (optimal: 30-45 seconds)
- File size: max 200MB
- Captions: Required (85% watch without sound)

**Performance rules:**
- First 3 seconds must hook (no logo intros, no slow fades)
- 30-second videos get 2x completion rate vs 60-second
- Videos with captions get 28% more engagement
- Talking head + B-roll outperforms pure animation by 35%
- Include on-screen text for key points (reinforces audio)

**Video length by objective:**
| Objective | Optimal Length | Maximum |
|-----------|---------------|---------|
| Brand awareness | 15-30 sec | 60 sec |
| Thought leadership | 30-60 sec | 90 sec |
| Product demo | 45-90 sec | 120 sec |
| Testimonial | 30-45 sec | 60 sec |
| Event promo | 15-30 sec | 45 sec |

**Video retention benchmarks (LinkedIn):**
| Timestamp | Good Retention | Poor Retention |
|-----------|---------------|----------------|
| 3 seconds | >65% | <40% |
| 10 seconds | >45% | <25% |
| 25% of video | >35% | <20% |
| 50% of video | >25% | <12% |
| 75% of video | >15% | <8% |
| 100% of video | >8% | <4% |

### Document Ads

**Specs:**
- Format: PDF only
- Pages: 1-10 pages (optimal: 3-7 pages)
- Gating: Choose which page to gate behind Lead Gen Form (typically page 2-3)
- First page is always visible (acts as the "cover")

**Performance rules:**
- Document Ads get 2-3x higher engagement than standard formats
- Gate at page 2 for maximum leads; gate at page 4-5 for higher quality leads
- Cover page must look like premium content, not an ad
- Use large fonts (min 24pt for body, 36pt for headers)
- Include page numbers and progress indicators
- Mobile-friendly: avoid tiny text or complex charts

**Document types that perform best:**
1. Industry benchmark reports (35-50% lead conversion rate)
2. How-to guides with frameworks (25-40% conversion rate)
3. Checklists and templates (30-45% conversion rate)
4. Research findings with original data (20-35% conversion rate)
5. ROI calculators and tools (15-30% conversion rate)

### Message Ads (InMail)

**Specs:**
- Subject line: 60 characters max
- Body: 1,500 characters max (optimal: 500-800)
- Single CTA button
- Sender: Must be a LinkedIn member (use company employee, not brand page)

**Performance rules:**
- Frequency cap: 1 message per member per 45 days (LinkedIn-enforced)
- Send on Tuesday-Thursday for best open rates
- Personalization with %FIRSTNAME% and %JOBTITLE% increases open rate by 15-25%
- Shorter messages (<500 characters) get 20% higher CTR than longer
- Sender profile matters: VP/Director sender gets 30% higher open vs generic
- Ask one question, make one offer; never stack multiple CTAs

**Subject line formulas:**
```
Formula 1: "Quick question about [their initiative]"
Formula 2: "[Mutual connection] suggested I reach out"
Formula 3: "Idea for [their company]'s [specific challenge]"
Formula 4: "[Stat] that surprised [their job title]s"
Formula 5: "Exclusive invite: [event/offer] for [their industry]"
```

### Conversation Ads

> **Deprecation notice:** Conversation Ads are no longer available in the EU/EEA due to privacy regulations, and LinkedIn is phasing them out globally. For markets where they are still available, the guidance below applies. For EU/EEA campaigns, use Message Ads for direct outreach or Sponsored Content for qualification flows.

**Specs:**
- Multiple CTA buttons per message (max 5)
- Branching logic: up to 5 levels deep
- Each branch leads to a different message and CTA set

**Performance rules:**
- Keep decision trees to 3 levels max (completion drops 40% per level)
- First message should have 2-3 options, not more
- Each path should end with a specific, relevant CTA
- Use conversation flows for qualification (self-selecting personas)

**Conversation flow template:**
```
Message 1: "Hi %FIRSTNAME%, I noticed you're in [industry]. Are you currently:"
├── Option A: "Looking to solve [problem 1]" → Message 2A
├── Option B: "Exploring [problem 2]" → Message 2B
└── Option C: "Just browsing" → Message 2C (light content offer)

Message 2A: Problem 1 specific pitch
├── Option: "See case study" → Link to case study
└── Option: "Book a demo" → Calendar link

Message 2B: Problem 2 specific pitch
├── Option: "Download guide" → Lead form
└── Option: "Talk to specialist" → Calendar link

Message 2C: "No worries! Here's a quick resource..."
└── Option: "Get the report" → Ungated content link
```

---

## Part 4: B2B Content Funnel Architecture

### LinkedIn Content Funnel Map

```
FUNNEL STAGE     │ CONTENT TYPE            │ FORMAT              │ CTA                    │ KPI
─────────────────┼─────────────────────────┼─────────────────────┼────────────────────────┼──────────────
Awareness        │ Industry trends         │ Video (30s)         │ Follow page            │ Reach, VTR
(Cold audience)  │ Surprising statistics   │ Document Ads (3p)   │ Read more              │ Engagement
                 │ Expert commentary       │ Single Image        │ Learn more             │ Brand lift
─────────────────┼─────────────────────────┼─────────────────────┼────────────────────────┼──────────────
Interest         │ How-to frameworks       │ Document Ads (5p)   │ Download guide         │ Doc opens
(Engaged)        │ Comparison guides       │ Carousel (5 cards)  │ See comparison         │ Swipe rate
                 │ Webinar replays         │ Video (60s)         │ Watch full webinar     │ VTR 50%
─────────────────┼─────────────────────────┼─────────────────────┼────────────────────────┼──────────────
Consideration    │ Case studies            │ Carousel (6 cards)  │ Read case study        │ CTR
(Warm audience)  │ Product demos           │ Video (45-90s)      │ See demo               │ Completions
                 │ ROI calculators         │ Single Image        │ Calculate your ROI     │ Leads
─────────────────┼─────────────────────────┼─────────────────────┼────────────────────────┼──────────────
Decision         │ Free trial / demo offer │ Message Ads         │ Start free trial       │ Leads (qual)
(Hot audience)   │ Consultation offer      │ Conversation Ads    │ Book consultation      │ MQLs
                 │ Limited-time offer      │ Single Image        │ Claim offer            │ Pipeline
─────────────────┼─────────────────────────┼─────────────────────┼────────────────────────┼──────────────
Retention        │ Customer stories        │ Video               │ Join community         │ Engagement
(Existing)       │ Feature announcements   │ Carousel            │ Try new feature        │ Expansion
                 │ Exclusive events        │ Event Ads           │ Register now           │ Retention
```

### Content Rotation Schedule

Prevent fatigue while maintaining funnel coverage:

| Week | Awareness | Interest | Consideration | Decision |
|------|-----------|----------|---------------|----------|
| 1 | Video A | Doc Ad A | Carousel Case A | InMail A |
| 2 | Doc Ad B | Carousel B | Video Demo A | Conv Ad A |
| 3 | Image A | Video C | Image Case B | InMail A (new audience) |
| 4 | Video B | Doc Ad C | Carousel Case B | Conv Ad B |

Rotate creative every 2-3 weeks per audience segment. InMail has a 45-day frequency cap, so rotation is less critical there.

---

## Part 5: Thought Leadership Positioning

### Thought Leadership Ad Framework

LinkedIn rewards authentic expertise over polished corporate messaging. The algorithm favors content that generates meaningful comments and shares.

**Thought Leadership Content Types (by performance):**

1. **Contrarian takes** (highest engagement): Challenge industry assumptions with data
2. **Original research** (highest lead quality): Share proprietary data or survey results
3. **Behind-the-scenes** (highest authenticity): Show real processes, failures, learnings
4. **Predictions** (highest shareability): Forecast industry changes with reasoning
5. **Frameworks** (highest saves): Provide actionable mental models

**Thought Leadership Ad Rules:**
- Use Thought Leader Ads (boost employee posts) for 40-60% lower CPC vs brand posts
- Personal profile images outperform logos by 2-3x on LinkedIn
- Comments on thought leadership ads are 5x more likely to include decision makers
- Never use more than one hashtag in paid content (looks inauthentic)
- Controversial (not offensive) opinions generate 8x more comments than neutral content

### Analyzing Current Creative Performance

```
linkedin_query(
    account_id="<account>",
    entity_type="creatives",
    status=["ACTIVE"]
)

linkedin_get_creatives_with_images(
    account_id="<account>",
    campaign_id="<campaign_id>"
)
```

Review creative types, messaging angles, and visual styles currently in use to identify gaps in the content funnel.

---

## Part 6: Format Migration Framework

### When to Switch Formats

| Current Format | Signal to Switch | Switch To | Expected Impact |
|---------------|-----------------|-----------|-----------------|
| Single Image | CTR declining below 0.30% | Carousel or Video | +25-40% CTR recovery |
| Carousel | Swipe rate below 10% | Single Image or Video | Better first-impression impact |
| Video | Completion rate below 15% | Shorter video or Document Ad | Better engagement quality |
| Document Ad | Gate completion below 5% | Move gate later or use Single Image + LP | Better lead quality |
| Message Ads | Open rate below 20% | Change sender or switch to Conversation Ads | +15-25% open rate |
| Text Ads | CTR below 0.02% | Single Image (budget increase needed) | 10-20x CTR improvement |

---

## Quick Reference: Format Selection Cheat Sheet

| If you want... | Use this format | With this objective |
|-----------------|-----------------|---------------------|
| Most leads | Single Image + Lead Gen Form | Lead Generation |
| Best quality leads | Message Ads | Lead Generation |
| Highest engagement | Document Ads | Engagement |
| Strongest brand awareness | Video (30s, square) | Brand Awareness |
| Best storytelling | Carousel (5-6 cards) | Engagement |
| Lowest cost per result | Text Ads | Website Visits |
| Event signups | Event Ads | Event Registration |
| Qualification | Conversation Ads | Lead Generation |
| Retargeting | Single Image | Website Conversions |
| Follower growth | Dynamic Follower Ads | Engagement |
