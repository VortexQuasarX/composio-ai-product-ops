"""
Metrics calculation module for Composio AI Product Ops 100-app dataset.
Computes comprehensive aggregations across Authentication, Access, API Breadth, MCP, and Buildability.
"""

import glob
import json
import os
from typing import Dict, Any, List


def calculate_metrics(data_dir: str = "data/final") -> Dict[str, Any]:
    files = glob.glob(os.path.join(data_dir, "*.json"))
    total_apps = len(files)
    if total_apps == 0:
        raise ValueError(f"No application records found in {data_dir}")

    records = []
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            records.append(json.load(fp))

    # 1. Authentication Metrics
    oauth2_count = sum(1 for r in records if r["authentication"]["oauth2"])
    api_key_count = sum(1 for r in records if r["authentication"]["api_key"])
    bearer_count = sum(1 for r in records if r["authentication"]["bearer_token"])
    pat_count = sum(1 for r in records if r["authentication"]["personal_access_token"])
    basic_auth_count = sum(1 for r in records if r["authentication"]["basic_auth"])
    multi_auth_count = sum(1 for r in records if len(r["authentication"]["methods"]) > 1)

    auth_primary_counts = {}
    for r in records:
        pm = r["authentication"]["primary_method"]
        auth_primary_counts[pm] = auth_primary_counts.get(pm, 0) + 1

    # 2. Access Classification Metrics
    access_counts = {}
    self_serve_count = sum(1 for r in records if r["credential_access"]["self_serve"])
    free_access_count = sum(1 for r in records if r["credential_access"]["free_access"])
    trial_count = sum(1 for r in records if r["credential_access"]["trial_available"])
    paid_required_count = sum(1 for r in records if r["credential_access"]["paid_plan_required"])
    admin_gated_count = sum(1 for r in records if r["credential_access"]["admin_approval_required"])
    sales_gated_count = sum(1 for r in records if r["credential_access"]["contact_sales_required"])
    partner_gated_count = sum(1 for r in records if r["credential_access"]["partnership_required"])

    for r in records:
        ac = r["credential_access"]["access_classification"]
        access_counts[ac] = access_counts.get(ac, 0) + 1

    # 3. API Surface Metrics
    api_exists_count = sum(1 for r in records if r["api"]["exists"])
    rest_count = sum(1 for r in records if r["api"]["rest"])
    graphql_count = sum(1 for r in records if r["api"]["graphql"])
    sdk_count = sum(1 for r in records if r["api"]["sdk"])
    cli_count = sum(1 for r in records if r["api"]["cli"])
    webhooks_count = sum(1 for r in records if r["api"]["webhooks"])

    breadth_counts = {}
    for r in records:
        b = r["api"]["breadth"]
        breadth_counts[b] = breadth_counts.get(b, 0) + 1

    # 4. MCP Availability Metrics
    mcp_exists_count = sum(1 for r in records if r["mcp"]["exists"])
    mcp_official_count = sum(1 for r in records if r["mcp"]["official"])
    mcp_vendor_count = sum(1 for r in records if r["mcp"]["vendor_supported"])
    mcp_community_count = sum(1 for r in records if r["mcp"]["community"])
    mcp_composio_count = sum(1 for r in records if r["mcp"]["composio_support"])
    mcp_none_count = total_apps - mcp_exists_count

    # 5. Buildability Verdict Metrics
    buildability_counts = {}
    for r in records:
        bv = r["buildability"]["verdict"]
        buildability_counts[bv] = buildability_counts.get(bv, 0) + 1

    # 6. Category-level Cross Aggregations
    categories = sorted(list(set(r["category"] for r in records)))
    category_summary = {}

    for cat in categories:
        cat_records = [r for r in records if r["category"] == cat]
        cat_total = len(cat_records)
        category_summary[cat] = {
            "total": cat_total,
            "ready_count": sum(1 for r in cat_records if r["buildability"]["verdict"] == "Ready"),
            "ready_pct": round(sum(1 for r in cat_records if r["buildability"]["verdict"] == "Ready") / cat_total * 100, 1),
            "self_serve_count": sum(1 for r in cat_records if r["credential_access"]["self_serve"]),
            "self_serve_pct": round(sum(1 for r in cat_records if r["credential_access"]["self_serve"]) / cat_total * 100, 1),
            "oauth2_count": sum(1 for r in cat_records if r["authentication"]["oauth2"]),
            "api_key_count": sum(1 for r in cat_records if r["authentication"]["api_key"]),
            "mcp_count": sum(1 for r in cat_records if r["mcp"]["exists"]),
            "mcp_pct": round(sum(1 for r in cat_records if r["mcp"]["exists"]) / cat_total * 100, 1),
            "composio_count": sum(1 for r in cat_records if r["mcp"]["composio_support"]),
            "composio_pct": round(sum(1 for r in cat_records if r["mcp"]["composio_support"]) / cat_total * 100, 1),
            "sales_partner_gated": sum(1 for r in cat_records if r["buildability"]["verdict"] == "Needs partnership/contact-sales"),
            "admin_gated": sum(1 for r in cat_records if r["buildability"]["verdict"] == "Needs admin approval"),
            "paid_required": sum(1 for r in cat_records if r["buildability"]["verdict"] == "Needs paid access"),
        }

    return {
        "total_apps": total_apps,
        "authentication": {
            "oauth2_total": oauth2_count,
            "oauth2_pct": round(oauth2_count / total_apps * 100, 1),
            "api_key_total": api_key_count,
            "api_key_pct": round(api_key_count / total_apps * 100, 1),
            "bearer_total": bearer_count,
            "bearer_pct": round(bearer_count / total_apps * 100, 1),
            "pat_total": pat_count,
            "pat_pct": round(pat_count / total_apps * 100, 1),
            "basic_auth_total": basic_auth_count,
            "basic_auth_pct": round(basic_auth_count / total_apps * 100, 1),
            "multi_auth_total": multi_auth_count,
            "multi_auth_pct": round(multi_auth_count / total_apps * 100, 1),
            "primary_method_breakdown": {k: {"count": v, "pct": round(v / total_apps * 100, 1)} for k, v in auth_primary_counts.items()},
        },
        "access": {
            "self_serve_total": self_serve_count,
            "self_serve_pct": round(self_serve_count / total_apps * 100, 1),
            "free_access_total": free_access_count,
            "free_access_pct": round(free_access_count / total_apps * 100, 1),
            "trial_total": trial_count,
            "trial_pct": round(trial_count / total_apps * 100, 1),
            "paid_required_total": paid_required_count,
            "paid_required_pct": round(paid_required_count / total_apps * 100, 1),
            "admin_gated_total": admin_gated_count,
            "admin_gated_pct": round(admin_gated_count / total_apps * 100, 1),
            "sales_gated_total": sales_gated_count,
            "sales_gated_pct": round(sales_gated_count / total_apps * 100, 1),
            "partner_gated_total": partner_gated_count,
            "partner_gated_pct": round(partner_gated_count / total_apps * 100, 1),
            "classification_breakdown": {k: {"count": v, "pct": round(v / total_apps * 100, 1)} for k, v in access_counts.items()},
        },
        "api": {
            "exists_total": api_exists_count,
            "exists_pct": round(api_exists_count / total_apps * 100, 1),
            "rest_total": rest_count,
            "rest_pct": round(rest_count / total_apps * 100, 1),
            "graphql_total": graphql_count,
            "graphql_pct": round(graphql_count / total_apps * 100, 1),
            "sdk_total": sdk_count,
            "sdk_pct": round(sdk_count / total_apps * 100, 1),
            "cli_total": cli_count,
            "cli_pct": round(cli_count / total_apps * 100, 1),
            "webhooks_total": webhooks_count,
            "webhooks_pct": round(webhooks_count / total_apps * 100, 1),
            "breadth_breakdown": {k: {"count": v, "pct": round(v / total_apps * 100, 1)} for k, v in breadth_counts.items()},
        },
        "mcp": {
            "exists_total": mcp_exists_count,
            "exists_pct": round(mcp_exists_count / total_apps * 100, 1),
            "official_total": mcp_official_count,
            "official_pct": round(mcp_official_count / total_apps * 100, 1),
            "vendor_supported_total": mcp_vendor_count,
            "vendor_supported_pct": round(mcp_vendor_count / total_apps * 100, 1),
            "community_total": mcp_community_count,
            "community_pct": round(mcp_community_count / total_apps * 100, 1),
            "composio_support_total": mcp_composio_count,
            "composio_support_pct": round(mcp_composio_count / total_apps * 100, 1),
            "none_total": mcp_none_count,
            "none_pct": round(mcp_none_count / total_apps * 100, 1),
        },
        "buildability": {
            "breakdown": {k: {"count": v, "pct": round(v / total_apps * 100, 1)} for k, v in buildability_counts.items()},
            "ready_total": buildability_counts.get("Ready", 0),
            "ready_pct": round(buildability_counts.get("Ready", 0) / total_apps * 100, 1),
        },
        "category_summary": category_summary,
    }


if __name__ == "__main__":
    metrics = calculate_metrics()
    print(json.dumps(metrics, indent=2))
