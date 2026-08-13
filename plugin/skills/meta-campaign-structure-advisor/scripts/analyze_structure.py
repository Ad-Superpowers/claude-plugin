#!/usr/bin/env python3
"""
Campaign Structure Analyzer
Analyseert campagne structuur data en geeft aanbevelingen.

Dit script kan worden aangeroepen door Claude met data uit Ad Superpowers MCP.

Gebruik:
    python analyze_structure.py --input campaigns.json
    python analyze_structure.py --input campaigns.json --output report.json
"""

import argparse
import json
from datetime import datetime
from typing import Any

# Configuratie
IDEAL_AD_SETS_PER_CAMPAIGN = 5  # Max voor goede learning
MIN_BUDGET_PER_AD_SET = 20  # Minimum voor learning phase
LEARNING_PHASE_CONVERSIONS = 50  # Per week nodig


def safe_number(value: Any, default: float = 0) -> float:
    """
    Safely convert a value to float.

    Meta API often returns numeric values as strings (e.g., "1000" for budget).
    This handles strings, ints, floats, None, and invalid values gracefully.
    """
    if value is None:
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def analyze_naming_convention(name: str) -> dict[str, Any]:
    """Check of naming convention wordt gevolgd."""
    # Verwacht format: Brand_Objective_Funnel_Geo_MMYY
    parts = name.split('_')

    if len(parts) < 4:
        return {
            "valid": False,
            "issue": "Naming convention niet gevolgd",
            "suggestion": "Gebruik format: Brand_Objective_Funnel_Geo_MMYY",
            "current": name
        }

    return {"valid": True, "current": name}

def analyze_budget_distribution(campaign: dict) -> dict[str, Any]:
    """Analyseer budget verdeling over ad sets."""
    # Use safe_number to handle string values from Meta API
    total_budget = safe_number(campaign.get('daily_budget'), 0)
    ad_set_count = int(safe_number(campaign.get('ad_set_count'), 1))

    if ad_set_count == 0:
        return {"issue": "Geen ad sets gevonden", "issues": [], "recommendations": []}

    budget_per_ad_set = total_budget / ad_set_count

    result = {
        "total_budget": total_budget,
        "ad_set_count": ad_set_count,
        "budget_per_ad_set": round(budget_per_ad_set, 2),
        "issues": [],
        "recommendations": []
    }

    if budget_per_ad_set < MIN_BUDGET_PER_AD_SET:
        result["issues"].append(f"Budget per ad set te laag: €{budget_per_ad_set}")
        result["recommendations"].append(
            f"Verhoog budget naar min €{MIN_BUDGET_PER_AD_SET * ad_set_count} "
            f"of reduceer naar {int(total_budget / MIN_BUDGET_PER_AD_SET)} ad sets"
        )

    if ad_set_count > IDEAL_AD_SETS_PER_CAMPAIGN:
        result["issues"].append(f"Te veel ad sets ({ad_set_count})")
        result["recommendations"].append(
            f"Consolideer naar max {IDEAL_AD_SETS_PER_CAMPAIGN} ad sets voor betere learning"
        )

    return result

def analyze_learning_phase(campaign: dict) -> dict[str, Any]:
    """Check learning phase status en haalbaarheid."""
    # Use safe_number to handle string values from Meta API
    conversions_last_7d = safe_number(campaign.get('conversions_7d'), 0)
    ad_set_count = int(safe_number(campaign.get('ad_set_count'), 1))

    conversions_per_ad_set = conversions_last_7d / max(ad_set_count, 1)

    result = {
        "total_conversions_7d": conversions_last_7d,
        "conversions_per_ad_set": round(conversions_per_ad_set, 1),
        "learning_phase_status": "unknown",
        "issues": [],
        "recommendations": []
    }

    if conversions_per_ad_set >= LEARNING_PHASE_CONVERSIONS:
        result["learning_phase_status"] = "exited"
    elif conversions_per_ad_set >= LEARNING_PHASE_CONVERSIONS * 0.5:
        result["learning_phase_status"] = "on_track"
    else:
        result["learning_phase_status"] = "struggling"
        result["issues"].append(
            f"Learning phase moeilijk: {conversions_per_ad_set} conv/ad set/week"
        )
        result["recommendations"].append(
            "Overweeg: hoger funnel event, minder ad sets, of hoger budget"
        )

    return result

def calculate_health_score(issues: list[str]) -> int:
    """Bereken health score op basis van issues."""
    base_score = 100
    deduction_per_issue = 15
    return max(0, base_score - (len(issues) * deduction_per_issue))

def analyze_campaign(campaign: dict) -> dict[str, Any]:
    """Volledige analyse van één campagne."""
    # Defensive check: skip invalid entries
    if not isinstance(campaign, dict):
        return {
            "error": f"Invalid campaign data: expected dict, got {type(campaign).__name__}",
            "health_score": 0,
            "all_issues": ["Invalid campaign data format"],
            "all_recommendations": []
        }

    analysis = {
        "campaign_id": campaign.get('id'),
        "campaign_name": campaign.get('name'),
        "objective": campaign.get('objective'),
        "status": campaign.get('status'),
        "analyses": {}
    }

    all_issues = []
    all_recommendations = []

    # Naming convention check
    naming = analyze_naming_convention(campaign.get('name', ''))
    analysis["analyses"]["naming"] = naming
    if not naming.get("valid"):
        all_issues.append(naming.get("issue"))

    # Budget distribution
    budget = analyze_budget_distribution(campaign)
    analysis["analyses"]["budget"] = budget
    all_issues.extend(budget.get("issues", []))
    all_recommendations.extend(budget.get("recommendations", []))

    # Learning phase
    learning = analyze_learning_phase(campaign)
    analysis["analyses"]["learning_phase"] = learning
    all_issues.extend(learning.get("issues", []))
    all_recommendations.extend(learning.get("recommendations", []))

    # Overall score
    analysis["health_score"] = calculate_health_score(all_issues)
    analysis["all_issues"] = all_issues
    analysis["all_recommendations"] = all_recommendations

    return analysis

def analyze_account(campaigns: list[dict]) -> dict[str, Any]:
    """Analyseer alle campagnes in een account."""
    results = {
        "analysis_date": datetime.now().isoformat(),
        "total_campaigns": len(campaigns),
        "campaigns": [],
        "summary": {
            "average_health_score": 0,
            "total_issues": 0,
            "critical_issues": [],
            "top_recommendations": []
        }
    }

    all_scores = []
    all_issues = []
    all_recommendations = []

    for campaign in campaigns:
        analysis = analyze_campaign(campaign)
        results["campaigns"].append(analysis)
        all_scores.append(analysis["health_score"])
        all_issues.extend(analysis["all_issues"])
        all_recommendations.extend(analysis["all_recommendations"])

    # Summary calculations
    if all_scores:
        results["summary"]["average_health_score"] = round(sum(all_scores) / len(all_scores), 1)

    results["summary"]["total_issues"] = len(all_issues)

    # Get unique recommendations, sorted by frequency
    rec_counts = {}
    for rec in all_recommendations:
        rec_counts[rec] = rec_counts.get(rec, 0) + 1

    results["summary"]["top_recommendations"] = sorted(
        rec_counts.keys(),
        key=lambda x: rec_counts[x],
        reverse=True
    )[:5]

    return results

def extract_campaigns(data: Any) -> list[dict]:
    """
    Extract campaigns list from various input formats.

    Supports:
    - Direct list: [{"id": "...", "name": "..."}]
    - Wrapped: {"campaigns": [...]}
    - Nested: {"data": {"campaigns": [...]}}
    """
    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        # Try common wrapper keys
        if 'campaigns' in data:
            return data['campaigns']
        if 'data' in data:
            nested = data['data']
            if isinstance(nested, dict) and 'campaigns' in nested:
                return nested['campaigns']
            if isinstance(nested, list):
                return nested

    # Fallback: wrap in list if single campaign
    if isinstance(data, dict) and 'id' in data:
        return [data]

    raise ValueError(
        f"Cannot extract campaigns from input. "
        f"Expected list of campaigns or dict with 'campaigns' key. "
        f"Got: {type(data).__name__}"
    )


def main():
    parser = argparse.ArgumentParser(description='Analyze campaign structure')
    parser.add_argument('--input', '-i', required=True, help='Input JSON file with campaigns')
    parser.add_argument('--output', '-o', help='Output JSON file for results')
    parser.add_argument('--format', choices=['json', 'summary'], default='json')

    args = parser.parse_args()

    # Load input
    with open(args.input) as f:
        input_data = json.load(f)

    # Extract campaigns from various input formats
    campaigns = extract_campaigns(input_data)

    # Analyze
    results = analyze_account(campaigns)

    # Output
    if args.format == 'summary':
        print(f"\n{'='*50}")
        print("CAMPAIGN STRUCTURE ANALYSIS")
        print(f"{'='*50}")
        print(f"Date: {results['analysis_date'][:10]}")
        print(f"Campaigns analyzed: {results['total_campaigns']}")
        print(f"Average Health Score: {results['summary']['average_health_score']}/100")
        print(f"Total Issues Found: {results['summary']['total_issues']}")
        print("\nTop Recommendations:")
        for i, rec in enumerate(results['summary']['top_recommendations'], 1):
            print(f"  {i}. {rec}")
    else:
        output = json.dumps(results, indent=2, ensure_ascii=False)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"Results written to {args.output}")
        else:
            print(output)

if __name__ == "__main__":
    main()
