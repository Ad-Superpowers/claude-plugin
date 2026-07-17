# Meta Ads Naming Conventions Reference

## Why Naming Conventions?

Good naming conventions give you:
- Fast identification in Ads Manager
- Easy filtering and reporting
- Consistency across team workflows
- Better integration with analytics tools

## Recommended Structure

### Campaign Level

```
[Brand]_[Objective]_[Funnel]_[Geo]_[MMYY]
```

| Component | Options | Example |
|-----------|---------|---------|
| Brand | Company name or abbreviation | `Acme`, `ACM` |
| Objective | `Conv`, `Traffic`, `Awareness`, `Leads`, `Engagement` | `Conv` |
| Funnel | `TOFU`, `MOFU`, `BOFU`, `Retarget` | `BOFU` |
| Geo | ISO country code | `NL`, `BE`, `DACH` |
| MMYY | Month/year | `0126` |

**Example**: `Acme_Conv_BOFU_NL_0126`

### Ad Set Level

```
[AudienceType]_[AudienceDetail]_[Placement]
```

| Component | Options | Example |
|-----------|---------|---------|
| AudienceType | `LAL`, `Interest`, `Retarget`, `Broad`, `CustList` | `LAL` |
| AudienceDetail | Specific description | `1pct_Purchasers` |
| Placement | `AllPlace`, `Feed`, `Stories`, `Reels` | `AllPlace` |

**Example**: `LAL_1pct_Purchasers_AllPlace`

### Ad Level

```
[CreativeType]_[Format]_[Version]_[Hook]
```

| Component | Options | Example |
|-----------|---------|---------|
| CreativeType | `UGC`, `Studio`, `Static`, `Carousel`, `Catalog` | `UGC` |
| Format | `Video`, `Image`, `Carousel` | `Video` |
| Version | `v1`, `v2`, `v3` | `v2` |
| Hook | `ProblemHook`, `BenefitHook`, `SocialProof`, `Question` | `ProblemHook` |

**Example**: `UGC_Video_v2_ProblemHook`

## Complete Example

```
Campaign: Acme_Conv_BOFU_NL_0126
└── Ad Set: LAL_1pct_Purchasers_AllPlace
    ├── Ad: UGC_Video_v1_ProblemHook
    ├── Ad: UGC_Video_v2_BenefitHook
    └── Ad: Static_Image_v1_SocialProof
└── Ad Set: Retarget_Cart30d_AllPlace
    ├── Ad: Catalog_Carousel_v1_Reminder
    └── Ad: Static_Image_v1_Urgency
```

## Special Cases

### A/B Tests

Add `_TestA` / `_TestB` to the campaign name:
```
Acme_Conv_BOFU_NL_0126_TestA
Acme_Conv_BOFU_NL_0126_TestB
```

### Seasonal Campaigns

Add the season or event:
```
Acme_Conv_BOFU_NL_BF24  (Black Friday 2024)
Acme_Conv_BOFU_NL_XMAS24
Acme_Conv_BOFU_NL_SUMMER25
```

### Multi-Product

Add the product category:
```
Acme_Conv_BOFU_NL_0126_Shoes
Acme_Conv_BOFU_NL_0126_Bags
```

## UTM Parameters Alignment

Make sure UTM parameters match the naming:

```
utm_source=facebook
utm_medium=paid
utm_campaign=Acme_Conv_BOFU_NL_0126
utm_content=UGC_Video_v2_ProblemHook
```

## Regex Patterns for Validation

### Campaign Name Validation
```regex
^[A-Za-z]+_[A-Za-z]+_[A-Z]{4}_[A-Z]{2,4}_\d{4}(_[A-Za-z0-9]+)?$
```

### Ad Set Name Validation
```regex
^[A-Za-z]+_[A-Za-z0-9]+_[A-Za-z]+$
```

### Ad Name Validation
```regex
^[A-Za-z]+_[A-Za-z]+_v\d+_[A-Za-z]+$
```

## Checklist

- [ ] Consistent format across all campaigns
- [ ] No spaces (use underscores)
- [ ] No special characters
- [ ] Date format consistent (MMYY)
- [ ] Audience type is clear
- [ ] Creative type is identifiable
- [ ] Version tracking is possible
