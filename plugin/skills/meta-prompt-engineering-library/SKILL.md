---
name: meta-prompt-engineering-library
description: "This skill should be used when the user asks to \"get AI prompts for Meta Ads\", \"optimize prompts for ad analysis\", \"find prompt templates\", or mentions \"prompt engineering for ads\", \"AI workflow prompts\", or \"Meta Ads prompt library\". Do NOT use for: ad copy writing directly (use ad-copy-generator), video scripts (use video-script-writer), campaign diagnostics (use performance-troubleshooter)."
---
# Prompt Engineering Library

## Overview

This skill provides a collection of optimized prompts for leveraging AI (ChatGPT, Claude, Midjourney, etc.) within Meta Ads workflows, from creative briefing to data analysis and copy generation.

## Prompt Fundamentals

### Anatomy of a Good Prompt

```
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT STRUCTURE (CRISP Framework)                             │
│                                                                 │
│  C - Context: Provide background and situation                  │
│  R - Role: Define the expertise you need                        │
│  I - Instructions: Give clear, specific directives              │
│  S - Specifics: Add details, constraints, formats               │
│  P - Parameters: Output format, length, style                   │
└─────────────────────────────────────────────────────────────────┘
```

### Prompt Quality Levels

| Level | Example | Quality |
|-------|---------|---------|
| Bad | "Write ad copy" | Vague, generic result |
| Better | "Write Facebook ad copy for a fitness app" | Better but still incomplete |
| Good | "You are a direct response copywriter. Write 3 Facebook ad copy variations for FitPro app targeting women 25-40 who want to lose weight. Use PAS framework. Max 125 characters primary text." | Specific, actionable |

## Prompt Categories

### Category 1: Ad Copy Generation

#### Primary Text Generator

```
PROMPT: AD COPY GENERATOR

You are an experienced Meta Ads copywriter specialized in
direct response advertising.

CONTEXT:
- Product: [PRODUCT/SERVICE]
- Target Audience: [DEMOGRAPHICS + PSYCHOGRAPHICS]
- Unique Selling Point: [USP]
- Funnel Stage: [TOFU/MOFU/BOFU]
- Offer: [IF APPLICABLE]

TASK:
Write 5 variations of primary text for a Meta ad.

SPECIFICATIONS:
- Framework: Alternate between PAS, AIDA, and BAB
- Hook: First sentence must grab attention within 3 seconds
- Length: 100-150 characters (first 125 visible)
- Tone: [Casual/Professional/Urgent/Friendly]
- CTA: End with a clear call-to-action

OUTPUT FORMAT:
For each variation:
1. [Framework used]
2. Primary text
3. Headline suggestion (max 40 characters)
4. CTA button recommendation
```

#### Hook Generator

```
PROMPT: HOOK GENERATOR

Generate 10 scroll-stopping hooks for a Meta ad.

PRODUCT: [PRODUCT]
TARGET AUDIENCE: [AUDIENCE]
PAIN POINT: [KEY PROBLEM]
DESIRED RESULT: [WHAT THEY WANT TO ACHIEVE]

HOOK TYPES (use a mix):
1. Question hooks ("Did you know...?")
2. Statistic hooks ("80% of...")
3. Contrarian hooks ("Forget everything you knew about...")
4. Result hooks ("Here's how I achieved [X] in [time]")
5. Curiosity hooks ("The secret behind...")

CONSTRAINTS:
- Max 10 words per hook
- Must stop the scroll
- No clickbait that can't be delivered on
- Suitable for [PLATFORM: Feed/Stories/Reels]
```

### Category 2: Creative Briefing

#### UGC Creator Brief Generator

```
PROMPT: UGC BRIEF GENERATOR

Create a complete UGC video brief for creators.

PRODUCT INFO:
- Product: [PRODUCT]
- Price: [PRICE]
- USPs: [LIST OF BENEFITS]
- Website: [URL]

CAMPAIGN INFO:
- Platform: [Instagram Reels/TikTok/Facebook]
- Goal: [Awareness/Consideration/Conversion]
- Target Audience: [DEMOGRAPHICS]
- Tone: [Authentic/Energetic/Informative]

GENERATE A BRIEF WITH:
1. Overview (1 paragraph)
2. Key messages (3-5 bullets)
3. Script outline with timing (hook, body, CTA)
4. Do's and Don'ts
5. Technical specs (format, length, quality)
6. Example hooks to use
7. Examples of what to avoid

OUTPUT: Markdown format, ready to send to creator
```

#### Image Ad Concept Generator

```
PROMPT: AD VISUAL CONCEPT GENERATOR

Generate 5 visual concepts for Meta ad images.

PRODUCT: [PRODUCT]
BRAND GUIDELINES: [COLORS, STYLE, TONE]
TARGET AUDIENCE: [WHO]
MESSAGE: [WHAT TO COMMUNICATE]

FOR EACH CONCEPT, PROVIDE:
1. Concept name
2. Visual description (what you see)
3. Text overlay suggestion
4. Why this works for the target audience
5. Production approach (stock, photoshoot, design)

CONCEPT TYPES (include mix):
- Product-focused (product in action)
- Lifestyle (aspirational scenario)
- Before/After
- Social proof (reviews, ratings visual)
- Problem/Solution split
```

### Category 3: Data Analysis

#### Performance Report Analyzer

```
PROMPT: CAMPAIGN ANALYSIS

Analyze the following Meta Ads performance data and provide
actionable insights.

DATA:
[PASTE YOUR CAMPAIGN DATA HERE]

ANALYZE:
1. Top 3 best performing elements (and why)
2. Top 3 underperformers (and possible causes)
3. Trends over time (improving/declining)
4. Anomalies or notable patterns
5. Comparison with benchmarks if provided

PROVIDE RECOMMENDATIONS:
- Quick wins (actionable within 24 hours)
- Medium-term optimizations (this week)
- Strategic changes (next month)

FORMAT:
Use tables where relevant
Prioritize recommendations (High/Medium/Low impact)
Be specific (no vague suggestions)
```

#### A/B Test Results Interpreter

```
PROMPT: A/B TEST ANALYSIS

Interpret the following A/B test results.

TEST SETUP:
- Hypothesis: [WHAT WE TESTED]
- Variant A (Control): [DESCRIPTION]
- Variant B (Test): [DESCRIPTION]
- Test duration: [X DAYS]
- Primary metric: [CPA/CTR/ROAS]

RESULTS:
[PASTE DATA HERE]

ANALYZE:
1. Is the result statistically significant? (why/why not)
2. What is the impact in absolute and relative terms?
3. Are there secondary metrics that provide extra insight?
4. What can we learn from this result?
5. What should the next test be?

RECOMMENDATION:
- Implement winner: Yes/No + why
- Confidence level: High/Medium/Low
- Suggested follow-up action
```

### Category 4: Audience Research

#### Audience Persona Builder

```
PROMPT: TARGET AUDIENCE PERSONA

Create a detailed buyer persona for Meta Ads targeting.

PRODUCT/SERVICE: [WHAT YOU SELL]
CURRENT CUSTOMERS: [WHAT YOU KNOW ABOUT THEM]
PRICE POINT: [PRICE]
MARKET: [B2C/B2B, REGION]

GENERATE PERSONA WITH:

1. DEMOGRAPHICS
├── Age range
├── Gender
├── Location
├── Income/education level
└── Family situation

2. PSYCHOGRAPHICS
├── Values and beliefs
├── Lifestyle
├── Interests and hobbies
└── Media behavior (platforms, content types)

3. PAINS & GAINS
├── Top 3 frustrations/problems
├── Top 3 goals/aspirations
├── What keeps them up at night
└── What would improve their life

4. BUYING BEHAVIOR
├── Where they search for information
├── What triggers a purchase
├── Objections/barriers
└── Decision making process

5. META ADS TARGETING SUGGESTIONS
├── Interest targeting options
├── Lookalike audience sources
├── Custom audience ideas
└── Messaging angles per funnel stage
```

### Category 5: Reporting

#### Weekly Report Generator

```
PROMPT: WEEKLY PERFORMANCE REPORT

Generate a professional weekly report for Meta Ads.

WEEK: [WEEK NUMBER]
ACCOUNT: [ACCOUNT NAME]

PERFORMANCE DATA:
[PASTE METRICS HERE]
- Spend, Impressions, Clicks, CTR
- Conversions, CPA, ROAS
- Top campaigns/ad sets

STRUCTURE REPORT AS:

1. EXECUTIVE SUMMARY (3-5 bullets)
├── Key result
├── Biggest change vs last week
└── Key action item

2. PERFORMANCE OVERVIEW
├── Table with KPIs vs targets
├── Week-over-week comparison
└── Trend indicator (up/down/flat)

3. HIGHLIGHTS
├── Best performer (why)
├── New tests launched
└── Key learnings

4. ATTENTION ITEMS
├── Underperformers
├── Budget issues
└── Upcoming challenges

5. NEXT WEEK PLAN
├── Planned actions
├── Tests to start
└── Budget changes

FORMAT: Professional, scannable, max 1 page
```

### Category 6: AI Image Generation

#### Gemini Image Generation (Native — Preferred)

Ad Superpowers has native Gemini image generation via the `gemini_generate_image` tool. This is the fastest path from brief to Meta-ready creative — images can be uploaded directly to the Meta media library in one call.

```
WORKFLOW: BRIEF → GENERATE → DEPLOY

Step 1: Craft your Gemini prompt using this template:

PROMPT: GEMINI AD IMAGE GENERATOR

Generate [N] ad image variations for [PRODUCT].

Style: [photorealistic product photography / lifestyle / UGC-style / clean studio]
Mood: [energetic/aspirational/calm/premium/playful]
Aspect ratio: [1:1 for Feed / 4:5 for Instagram Feed / 9:16 for Reels/Stories]
Color palette: [describe or reference brand colors]
Key visual: [what should be in focus — product, person, scene]

No text overlays in the image.
Leave visual breathing room for copy overlay.
Avoid faces that look AI-generated.

Step 2: Execute via MCP:
→ gemini_generate_image(
     prompt="...",
     aspect_ratio="1:1",
     account_id="[META_ACCOUNT_ID]"   ← uploads to Meta media library
   )

Returns: image_hash + image_url (CDN) — ready for meta_create_ad immediately.
```

#### Midjourney Ad Image Prompts

```
PROMPT: MIDJOURNEY AD VISUALS

Generate Midjourney prompts for Meta ad images.

PRODUCT: [PRODUCT]
STYLE: [Photorealistic/Illustration/Minimalist]
MOOD: [Energetic/Calm/Premium/Playful]
COLOR PALETTE: [COLORS]

GENERATE 5 MIDJOURNEY PROMPTS:

Format per prompt:
/imagine [description], [style parameters], [technical specs]

INCLUDE IN EACH PROMPT:
- Subject/scene description
- Lighting (soft, dramatic, natural)
- Composition (centered, rule of thirds)
- Camera angle if relevant
- Style references
- Technical params: --ar 1:1 --v 6 --style raw --q 2

VARIATIONS:
1. Product hero shot
2. Lifestyle/usage scenario
3. Abstract/conceptual
4. Social proof visual
5. Problem/solution visual
```

#### DALL-E Ad Concepts

```
PROMPT: DALL-E AD VISUALS

Generate DALL-E prompts for social media advertisements.

PRODUCT: [PRODUCT]
MESSAGE: [KEY MESSAGE]
FORMAT: [1:1 Square / 4:5 / 9:16]

GENERATE 5 DALL-E PROMPTS:

Format:
"[Detailed description], [style], [lighting],
[composition], digital art/photography/illustration"

CONSIDERATIONS:
- No text in image (add later)
- Clear focal point
- Room for text overlay
- Brand-consistent colors
- No faces (copyright issues)
```

## Prompt Templates Library

### Quick Copy Prompts

```
HEADLINE GENERATOR:
"Generate 10 headlines for [PRODUCT] targeting [AUDIENCE].
Max 40 characters. Focus on [BENEFIT]. Mix of question, statement
and urgency formats."

CTA VARIATIONS:
"Provide 8 call-to-action variations for [ACTION] that evoke
[EMOTION]. Stronger than 'Click here'. Max 3 words."

SOCIAL PROOF COPY:
"Rewrite this review as short ad copy (50 words):
[REVIEW]. Make it compelling without exaggerating."

URGENCY CREATOR:
"Generate 5 urgency elements for [OFFER] that create FOMO
without sounding spammy. Ethical and honest."
```

### Quick Analysis Prompts

```
QUICK AUDIT:
"Review these metrics [DATA] and provide in 3 bullets:
1) Biggest problem 2) Quick win 3) Priority this week"

COMPETITOR COPY ANALYSIS:
"Analyze this competitor ad [COPY]. What works? What doesn't?
How can we do this better for [OUR PRODUCT]?"

AUDIENCE INSIGHT:
"Based on this engagement data [DATA], what does this tell
about our target audience? Provide 3 actionable targeting insights."
```

## Example Interaction

**User**: "I need prompts to quickly generate ad copy for my skincare brand."

**Claude response**:

"Here are optimized prompts for your skincare brand:

---

**PROMPT 1: Primary Text Generator**

```
You are a beauty copywriter specialized in skincare DTC brands.

BRAND: [Your brand name]
PRODUCT: [Specific product, e.g. "Vitamin C Serum"]
TARGET AUDIENCE: Women 25-45, interested in clean beauty
USP: [E.g. "100% natural, visible results in 2 weeks"]
FUNNEL: BOFU (retargeting)

Write 5 primary text variations:
- Mix of PAS and AIDA frameworks
- First sentence = scroll-stopping hook
- 100-125 characters
- End with soft CTA

Also deliver: matching headline (max 40 char) per variation
```

---

**PROMPT 2: Hook Generator (Quick)**

```
Generate 10 hooks for skincare ad. Product: [X]
Problem: [acne/wrinkles/dull skin]
Result: [glowing skin/fewer wrinkles]

Mix: question, statistic, before/after, curiosity
Max 8 words per hook. Scroll-stopping.
```

---

**PROMPT 3: Testimonial Rewriter**

```
Rewrite this customer review as ad copy:

"[Paste review here]"

Make it:
- Shorter (max 80 words)
- More engaging (add hook)
- With clear result highlight
- Including emojis (max 3)
Maintain authenticity, no overclaims.
```

---

**BONUS — Generate an image directly:**

If you want to test a visual immediately, use Gemini image generation:
```
gemini_generate_image(
  prompt="Skincare serum product photography, soft studio lighting, clean white background, premium minimal aesthetic, 4:5 aspect ratio, no text",
  aspect_ratio="4:5",
  account_id="[YOUR_META_ACCOUNT_ID]"
)
```
This uploads the image to your Meta media library and returns an `image_hash` ready for `meta_create_ad`.

Would you like me to also create prompts for visual concepts or UGC briefings?"
