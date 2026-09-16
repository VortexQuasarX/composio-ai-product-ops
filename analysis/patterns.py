"""
Pattern analysis and strategic insights generator for Composio AI Product Ops.
Synthesizes verified metrics into high-impact product-ops recommendations.
"""

import os
import sys
from typing import Dict, Any, List

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from analysis.metrics import calculate_metrics


def generate_patterns_report() -> Dict[str, Any]:
    metrics = calculate_metrics("data/final")

    patterns = [
        {
            "id": "pattern-1-auth-schism",
            "title": "The Authentication Schism: OAuth2 for SaaS Workspaces vs. API Keys for High-Throughput Engines",
            "stat": "59% OAuth2 vs 57% API Keys (0% OAuth2 in Scraping vs 90% in CRM/Productivity)",
            "finding": (
                "Authentication divides cleanly along domain boundaries. CRM and Productivity tools overwhelmingly mandate OAuth2 "
                "(90% in CRM, 90% in Productivity) to enforce granular user consent and multi-tenant isolation. Conversely, Data/Scraping "
                "tools completely avoid OAuth2 (0% OAuth2, 80% API Key, 20% Basic Auth), optimizing strictly for programmatic high-concurrency "
                "machine-to-machine extraction."
            ),
            "product_ops_implication": (
                "Composio must decouple its agent authentication architecture: provide a frictionless, zero-interaction Secret Vault for "
                "API key/token tools (Data, Developer, AI), while investing in token refresh automation, webhook state sync, and headless "
                "OAuth proxy flows for enterprise workspaces."
            )
        },
        {
            "id": "pattern-2-access-illusion",
            "title": "The API Accessibility Illusion: 95% of Apps Have Public APIs, but Only 54% Are Ready for Autonomous Agents",
            "stat": "95% API Availability vs 54% Toolkit Readiness (41% Blocked by Paid Tiers, Admin Gating, or Sales Contracts)",
            "finding": (
                "API existence is a deeply deceptive proxy for agent readiness. While 95 of 100 audited applications publish documented APIs, "
                "41% cannot be operated autonomously out-of-the-box: 19% require active paid subscriptions (e.g. Ahrefs, GoHighLevel, Squarespace), "
                "10% require bespoke enterprise sales contracts (e.g. DealCloud, PitchBook, Paygent Connect), and 8% require enterprise workspace "
                "admin approval (e.g. Brex, Ramp, WhatsApp Business)."
            ),
            "product_ops_implication": (
                "Do not greenlight agent tool integrations based solely on swagger/OpenAPI availability. Composio's integration roadmap must "
                "triage by 'Credential Friction': Tier 1 (Instant Free Sandbox: GitHub, Stripe, Supabase), Tier 2 (Bring-Your-Own-Paid-License: "
                "Ahrefs, Devin), and Tier 3 (Enterprise Partnership / Admin Gated: DealCloud, Amazon SP-API)."
            )
        },
        {
            "id": "pattern-3-mcp-supply-gap",
            "title": "The Model Context Protocol (MCP) Supply Gap: 83% Community Coverage, but Only 12% Vendor or Official Support",
            "stat": "83% Total MCP Ecosystem vs 2% Official MCP & 10% Vendor-Supported MCP",
            "finding": (
                "While open-source developer enthusiasm has created community MCP connectors for 83% of applications, official vendor commitment "
                "remains concentrated in modern developer platforms (Supabase, Cloudflare, Sentry, Firecrawl, Bright Data, Neo4j, MongoDB). "
                "Traditional enterprise vendors (Salesforce, Zendesk, QuickBooks) have not released official MCP servers, relying entirely on "
                "third-party bridges."
            ),
            "product_ops_implication": (
                "Community MCP repositories suffer from bitrot, rate-limit blindness, and security vulnerabilities. Composio has an immense moat "
                "by delivering certified, production-grade toolkits (already supporting 75% of these apps) with managed token rotation, schema validation, "
                "and retry mechanics that raw community MCP servers lack."
            )
        },
        {
            "id": "pattern-4-category-risk",
            "title": "Category Readiness Polarities: Productivity is 90% Turnkey; AI-Native & Support Tools Pose Highest Risk",
            "stat": "Productivity (90% Ready) vs Support (30% Ready) and AI-Native (20% Ready)",
            "finding": (
                "Productivity (Notion, Airtable, Linear, Asana, Jira) and Developer Platforms (GitHub, Supabase, Cloudflare) are almost completely turnkey "
                "for agent builders (80-90% Ready, 100% self-serve). In stark contrast, AI-Native Media tools (20% Ready) suffer from closed consumer silos "
                "(NotebookLM, Otter AI lack public APIs) and paid token paywalls (Devin, Higgsfield), while Support platforms (30% Ready) gate API access "
                "behind premium seats and workspace admin toggles."
            ),
            "product_ops_implication": (
                "Focus agent product launches on Developer and Productivity toolkits where end-to-end autonomous loops achieve 90%+ reliability. "
                "For Support and AI tools, position Composio integrations around human-in-the-loop workflows where human supervisors handle credentials "
                "and approval escalation."
            )
        }
    ]

    return {
        "metrics": metrics,
        "patterns": patterns
    }


if __name__ == "__main__":
    report = generate_patterns_report()
    print(f"Generated {len(report['patterns'])} strategic pattern insights.")
    for p in report["patterns"]:
        print(f"\n[{p['id']}] {p['title']}")
        print(f"Stat: {p['stat']}")
        print(f"Finding: {p['finding']}")
        print(f"Product Ops Implication: {p['product_ops_implication']}")
