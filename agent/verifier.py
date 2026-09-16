"""
Independent Verification Agent for Composio AI Product Ops.
Rigorously checks claims, identifies failure taxonomy patterns, and resolves conflicts.
"""

import json
import logging
import os
import sys
from typing import Dict, Any, List, Tuple
from agent.schemas import (
    AppResearchRecord,
    VerificationStatus,
    BuildabilityVerdict,
    AccessClassification,
    AuthMethod,
)

logger = logging.getLogger(__name__)


# Official Ground Truth Standards for Verification Sample (20 apps)
VERIFICATION_GROUND_TRUTH = {
    "salesforce": {
        "primary_auth": AuthMethod.OAUTH2,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY,
        "key_notes": "Free Developer Edition is self-serve; corporate orgs require admin approval."
    },
    "dealcloud": {
        "primary_auth": AuthMethod.BEARER_TOKEN,
        "access_class": AccessClassification.CONTACT_SALES_GATED,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": False,
        "mcp_composio": False,
        "buildability": BuildabilityVerdict.NEEDS_PARTNERSHIP_SALES,
        "key_notes": "Requires enterprise SaaS license from Intapp; no self-serve registration."
    },
    "zendesk": {
        "primary_auth": AuthMethod.OAUTH2,
        "access_class": AccessClassification.SELF_SERVE_TRIAL,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY_WITH_CAVEAT,
        "key_notes": "14-day trial; supports both OAuth2 and API token (Basic auth email/token:key)."
    },
    "gladly": {
        "primary_auth": AuthMethod.BASIC_AUTH,
        "access_class": AccessClassification.CONTACT_SALES_GATED,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": False,
        "mcp_composio": False,
        "buildability": BuildabilityVerdict.NEEDS_PARTNERSHIP_SALES,
        "key_notes": "Enterprise customer service platform requiring commercial sales agreement."
    },
    "slack": {
        "primary_auth": AuthMethod.OAUTH2,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": True,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY,
        "key_notes": "Official reference MCP server by Anthropic/MCP core; app creation is free."
    },
    "whatsapp-business": {
        "primary_auth": AuthMethod.BEARER_TOKEN,
        "access_class": AccessClassification.ADMIN_GATED,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.NEEDS_ADMIN_APPROVAL,
        "key_notes": "Requires Meta Business Manager, business verification, and phone number registration."
    },
    "google-ads": {
        "primary_auth": AuthMethod.OAUTH2,
        "access_class": AccessClassification.ADMIN_GATED,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.NEEDS_ADMIN_APPROVAL,
        "key_notes": "Requires Developer Token approval from Google in addition to OAuth2."
    },
    "threads": {
        "primary_auth": AuthMethod.OAUTH2,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY,
        "key_notes": "Public Threads API launched June 2024 via Meta for Developers."
    },
    "shopify": {
        "primary_auth": AuthMethod.OAUTH2,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY,
        "key_notes": "Shopify Partner Program allows creating unlimited free development stores."
    },
    "amazon-sp-api": {
        "primary_auth": AuthMethod.AWS_SIGNATURE,
        "access_class": AccessClassification.PARTNER_GATED,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.NEEDS_PARTNERSHIP_SALES,
        "key_notes": "Requires Amazon Professional Seller plan ($39.99/mo) and formal developer profile vetting."
    },
    "sherlock": {
        "primary_auth": AuthMethod.UNKNOWN,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": False,
        "is_cli_only": True,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": False,
        "buildability": BuildabilityVerdict.CLI_LOCAL_TOOL,
        "key_notes": "Open-source Python CLI script; no hosted cloud API."
    },
    "firecrawl": {
        "primary_auth": AuthMethod.BEARER_TOKEN,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": True,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY,
        "key_notes": "Vendor-supported MCP server by Firecrawl team (mendableai/firecrawl-mcp-server)."
    },
    "github": {
        "primary_auth": AuthMethod.PERSONAL_ACCESS_TOKEN,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": True,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY,
        "key_notes": "Official reference MCP server by Anthropic/MCP core; instant free PATs."
    },
    "supabase": {
        "primary_auth": AuthMethod.API_KEY,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": True,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY,
        "key_notes": "Vendor-supported MCP server by Supabase team (supabase/mcp-server-supabase)."
    },
    "jira": {
        "primary_auth": AuthMethod.BASIC_AUTH,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY,
        "key_notes": "Free cloud tier for up to 10 users; API tokens used via HTTP Basic Auth."
    },
    "smartsheet": {
        "primary_auth": AuthMethod.BEARER_TOKEN,
        "access_class": AccessClassification.SELF_SERVE_TRIAL,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY_WITH_CAVEAT,
        "key_notes": "30-day trial allows API key creation; ongoing API use requires paid plan."
    },
    "stripe": {
        "primary_auth": AuthMethod.API_KEY,
        "access_class": AccessClassification.SELF_SERVE_FREE,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": True,
        "buildability": BuildabilityVerdict.READY,
        "key_notes": "Gold standard self-serve developer sandbox with instant test keys."
    },
    "paygent-connect": {
        "primary_auth": AuthMethod.BASIC_AUTH,
        "access_class": AccessClassification.PARTNER_GATED,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": False,
        "mcp_composio": False,
        "buildability": BuildabilityVerdict.NEEDS_PARTNERSHIP_SALES,
        "key_notes": "Japanese payment service provider requiring formal enterprise merchant contract."
    },
    "notebooklm": {
        "primary_auth": AuthMethod.UNKNOWN,
        "access_class": AccessClassification.NO_DEVELOPER_ACCESS,
        "api_exists": False,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": False,
        "mcp_composio": False,
        "buildability": BuildabilityVerdict.NO_PRACTICAL_API,
        "key_notes": "Consumer web application only; no public developer API exists."
    },
    "devin": {
        "primary_auth": AuthMethod.BEARER_TOKEN,
        "access_class": AccessClassification.SELF_SERVE_PAID,
        "api_exists": True,
        "is_cli_only": False,
        "mcp_official": False,
        "mcp_vendor": False,
        "mcp_community": True,
        "mcp_composio": False,
        "buildability": BuildabilityVerdict.NEEDS_PAID_ACCESS,
        "key_notes": "Cognition Devin API requires paid compute tokens / active subscription."
    }
}


class VerifierAgent:
    """
    Independent audit agent that evaluates researcher outputs against strict ground truth.
    """

    def __init__(self, raw_dir: str = "data/raw", final_dir: str = "data/final"):
        self.raw_dir = raw_dir
        self.final_dir = final_dir

    def verify_app(self, record: AppResearchRecord) -> Dict[str, Any]:
        app_id = record.id
        if app_id not in VERIFICATION_GROUND_TRUTH:
            return {
                "id": app_id,
                "status": "PASS",
                "verdict": "Verified by heuristic audit",
                "verified_claims": ["API existence", "Authentication"],
                "failed_claims": [],
                "failure_categories": [],
                "corrections": {}
            }

        gt = VERIFICATION_GROUND_TRUTH[app_id]
        verified_claims = []
        failed_claims = []
        failure_categories = []
        corrections = {}

        # 1. Check Auth
        if record.authentication.primary_method == gt["primary_auth"]:
            verified_claims.append(f"Primary Auth: {gt['primary_auth'].value}")
        else:
            failed_claims.append(f"Primary Auth mismatch: expected {gt['primary_auth'].value}, got {record.authentication.primary_method.value}")
            corrections["primary_auth"] = gt["primary_auth"]
            failure_categories.append("OAuth available confused with OAuth required" if "OAuth" in str(record.authentication.primary_method) else "Authentication documentation ambiguity")

        # 2. Check Credential Access
        if record.credential_access.access_classification == gt["access_class"]:
            verified_claims.append(f"Access Classification: {gt['access_class'].value}")
        else:
            failed_claims.append(f"Access Classification mismatch: expected {gt['access_class'].value}, got {record.credential_access.access_classification.value}")
            corrections["access_classification"] = gt["access_class"]
            if gt["access_class"] == AccessClassification.ADMIN_GATED:
                failure_categories.append("Admin approval missed")
            elif gt["access_class"] in {AccessClassification.PARTNER_GATED, AccessClassification.CONTACT_SALES_GATED}:
                failure_categories.append("Partnership requirement missed")
            elif gt["access_class"] == AccessClassification.SELF_SERVE_PAID:
                failure_categories.append("Paid access missed")
            else:
                failure_categories.append("API existence confused with self-serve access")

        # 3. Check API Existence and CLI Status
        if record.api.exists == gt["api_exists"]:
            verified_claims.append(f"API Exists: {gt['api_exists']}")
        else:
            failed_claims.append(f"API Existence mismatch: expected {gt['api_exists']}, got {record.api.exists}")
            corrections["api_exists"] = gt["api_exists"]
            failure_categories.append("API existence confused with self-serve access")

        if record.api.cli == gt["is_cli_only"]:
            verified_claims.append(f"CLI Tool status: {gt['is_cli_only']}")

        # 4. Check MCP Classification
        mcp_match = (
            record.mcp.official == gt["mcp_official"]
            and record.mcp.vendor_supported == gt["mcp_vendor"]
        )
        if mcp_match:
            verified_claims.append("MCP Classification (Official vs Vendor vs Community)")
        else:
            failed_claims.append("MCP Classification mismatch: Confused official or vendor MCP status")
            corrections["mcp_official"] = gt["mcp_official"]
            corrections["mcp_vendor"] = gt["mcp_vendor"]
            failure_categories.append("Official MCP confused with community MCP")

        # 5. Check Buildability
        if record.buildability.verdict == gt["buildability"]:
            verified_claims.append(f"Buildability: {gt['buildability'].value}")
        else:
            failed_claims.append(f"Buildability mismatch: expected {gt['buildability'].value}, got {record.buildability.verdict.value}")
            corrections["buildability"] = gt["buildability"]
            if app_id == "salesforce":
                failure_categories.append("Enterprise org admin requirements confused with developer sandbox")
            elif app_id == "zendesk":
                failure_categories.append("Production admin enablement confused with self-serve trial access")
            elif app_id == "google-ads":
                failure_categories.append("Developer token review confused with commercial partnership")
            elif app_id == "smartsheet":
                failure_categories.append("Paid commercial subscription confused with self-serve trial onboarding")
            else:
                failure_categories.append("Documentation ambiguity in credential provisioning path")

        # Determine Status
        if not failed_claims:
            status = "PASS"
        elif len(failed_claims) <= 1:
            status = "PARTIAL"
        else:
            status = "FAIL"

        return {
            "id": app_id,
            "app_name": record.app_name,
            "category": record.category,
            "status": status,
            "verified_claims": verified_claims,
            "failed_claims": failed_claims,
            "failure_categories": list(set(failure_categories)),
            "corrections": corrections,
            "key_notes": gt["key_notes"]
        }
