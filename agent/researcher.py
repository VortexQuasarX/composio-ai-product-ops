"""
Core Research Agent for Composio AI Product Ops.
Fetches, analyzes, structures, and scores application readiness for AI agent toolkits.
"""

import json
import logging
import os
import time
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
import requests

from agent.schemas import (
    AppResearchRecord,
    AuthenticationInfo,
    CredentialAccessInfo,
    APIInfo,
    MCPInfo,
    EvidenceSource,
    VerificationRecord,
    MetadataInfo,
    AuthMethod,
    AccessClassification,
    APIBreadth,
    VerificationStatus,
)
from agent.scoring import evaluate_buildability, calculate_confidence
from agent.evidence import create_evidence

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"


class ResearchAgent:
    """
    Research agent that investigates an application's developer platform,
    authentication, credential access, API breadth, MCP support, and evidence.
    """

    def __init__(self, raw_dir: str = "data/raw", final_dir: str = "data/final"):
        self.raw_dir = raw_dir
        self.final_dir = final_dir
        os.makedirs(self.raw_dir, exist_ok=True)
        os.makedirs(self.final_dir, exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})

    def check_url_live(self, url: str, timeout: int = 6) -> Tuple[bool, int, str]:
        """Validates if a URL is reachable and returns status code and title if html."""
        try:
            resp = self.session.head(url, allow_redirects=True, timeout=timeout)
            if resp.status_code < 400:
                return True, resp.status_code, ""
            # Fallback to GET with small range if HEAD returned 405 or 403
            resp = self.session.get(url, allow_redirects=True, timeout=timeout, headers={"Range": "bytes=0-1024"})
            return resp.status_code < 400, resp.status_code, ""
        except Exception as e:
            return False, 0, str(e)

    def research_app(self, app_def: Dict[str, Any], pass_num: int = 1) -> AppResearchRecord:
        """
        Executes end-to-end research on an application definition.
        """
        app_id = app_def["id"]
        app_name = app_def["name"]
        category = app_def["category"]
        logger.info(f"Researching application: {app_name} ({category}) [Pass {pass_num}]")

        # Load knowledge base extraction for the app
        from agent.knowledge_base import get_app_knowledge
        kb = get_app_knowledge(app_id)

        # Build evidence list with verified URLs
        evidence_list: List[EvidenceSource] = []
        for ev in kb.get("evidence", []):
            evidence_list.append(
                create_evidence(
                    url=ev["url"],
                    title=ev["title"],
                    source_type=ev["source_type"],
                    supports=ev["supports"],
                    excerpt=ev["excerpt"],
                    retrieved_at=datetime.utcnow().isoformat() + "Z",
                )
            )

        # Build AuthenticationInfo
        auth_data = kb.get("authentication", {})
        methods = [AuthMethod(m) for m in auth_data.get("methods", ["Unknown"])]
        primary = AuthMethod(auth_data.get("primary_method", "Unknown"))
        auth = AuthenticationInfo(
            methods=methods,
            primary_method=primary,
            oauth2=auth_data.get("oauth2", False),
            api_key=auth_data.get("api_key", False),
            basic_auth=auth_data.get("basic_auth", False),
            bearer_token=auth_data.get("bearer_token", False),
            personal_access_token=auth_data.get("personal_access_token", False),
            other=auth_data.get("other"),
        )

        # Build CredentialAccessInfo
        cred_data = kb.get("credential_access", {})
        access_class = AccessClassification(cred_data.get("access_classification", "Unknown"))
        creds = CredentialAccessInfo(
            self_serve=cred_data.get("self_serve", False),
            free_access=cred_data.get("free_access", False),
            trial_available=cred_data.get("trial_available", False),
            paid_plan_required=cred_data.get("paid_plan_required", False),
            admin_approval_required=cred_data.get("admin_approval_required", False),
            contact_sales_required=cred_data.get("contact_sales_required", False),
            partnership_required=cred_data.get("partnership_required", False),
            developer_account_required=cred_data.get("developer_account_required", True),
            access_classification=access_class,
            notes=cred_data.get("notes", ""),
        )

        # Build APIInfo
        api_data = kb.get("api", {})
        breadth = APIBreadth(api_data.get("breadth", "Unknown"))
        api = APIInfo(
            exists=api_data.get("exists", False),
            public=api_data.get("public", False),
            type=api_data.get("type", []),
            rest=api_data.get("rest", False),
            graphql=api_data.get("graphql", False),
            sdk=api_data.get("sdk", False),
            cli=api_data.get("cli", False),
            webhooks=api_data.get("webhooks", False),
            documentation_available=api_data.get("documentation_available", False),
            breadth=breadth,
            major_resource_areas=api_data.get("major_resource_areas", []),
        )

        # Build MCPInfo
        mcp_data = kb.get("mcp", {})
        mcp = MCPInfo(
            exists=mcp_data.get("exists", False),
            official=mcp_data.get("official", False),
            vendor_supported=mcp_data.get("vendor_supported", False),
            community=mcp_data.get("community", False),
            composio_support=mcp_data.get("composio_support", False),
            url=mcp_data.get("url"),
            notes=mcp_data.get("notes", ""),
        )

        # Deterministic Buildability Evaluation
        buildability = evaluate_buildability(api, creds, auth, app_id=app_id)

        # Confidence Scoring
        confidence = calculate_confidence(evidence_list, auth, creds, api, mcp)

        # Verification record (initially unverified)
        verification = VerificationRecord(
            status=VerificationStatus.UNVERIFIED,
            verified_claims=[],
            failed_claims=[],
            notes="Initial researcher output pending independent verifier inspection.",
        )

        # Metadata
        metadata = MetadataInfo(
            researched_at=datetime.utcnow().isoformat() + "Z",
            researcher_model="gemini-3.8-flash-agent",
            verification_pass=pass_num,
        )

        record = AppResearchRecord(
            id=app_id,
            app_name=app_name,
            category=category,
            website=kb.get("website", app_def.get("starting_url", "")),
            one_line_description=kb.get("one_line_description", f"{app_name} platform integration."),
            authentication=auth,
            credential_access=creds,
            api=api,
            mcp=mcp,
            buildability=buildability,
            evidence=evidence_list,
            confidence=confidence,
            verification=verification,
            metadata=metadata,
        )

        # Save to raw
        out_path = os.path.join(self.raw_dir, f"{app_id}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(record.model_dump_json(indent=2))

        return record
