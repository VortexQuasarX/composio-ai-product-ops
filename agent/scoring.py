"""
Deterministic scoring, buildability rules, and confidence computation.
"""

from typing import List, Tuple
from agent.schemas import (
    AuthenticationInfo,
    CredentialAccessInfo,
    APIInfo,
    MCPInfo,
    BuildabilityInfo,
    BuildabilityVerdict,
    AccessClassification,
    EvidenceSource,
    ConfidenceScore,
)


def evaluate_buildability(
    api: APIInfo,
    creds: CredentialAccessInfo,
    auth: AuthenticationInfo,
    app_id: str = "",
) -> BuildabilityInfo:
    """
    Evaluates buildability deterministically according to strict business logic.
    Follows Section 13 rules:
    - CLI/local tool: pure CLI/library (e.g. Sherlock, Mermaid CLI)
    - No practical public API: api.exists is False
    - Needs partnership/contact-sales: contact_sales_required or partnership_required
    - Needs admin approval: admin_approval_required
    - Needs paid access: paid_plan_required
    - Ready with access caveat: trial_available or complex multi-step quotas
    - Ready: public documented API + self-serve free developer access + standard auth
    """
    # Check CLI or local open source tool
    if app_id in {"sherlock", "mermaid-cli"} or (api.cli and not api.rest and not api.graphql and not api.sdk):
        return BuildabilityInfo(
            verdict=BuildabilityVerdict.CLI_LOCAL_TOOL,
            blocker="No hosted SaaS API; runs as local executable or CLI process",
            rationale="Integration must execute in a local sandbox or CLI subprocess rather than via cloud API requests.",
        )

    # Check YouTube transcript special case
    if app_id == "youtube-transcript":
        # YouTube captions require either YouTube Data API v3 (OAuth/API Key with strict quotas/caption download permissions) or unofficial scraping
        return BuildabilityInfo(
            verdict=BuildabilityVerdict.READY_WITH_CAVEAT,
            blocker="Quota limits and OAuth scope requirements for official Captions API",
            rationale="Official YouTube Data API v3 supports captions download for owned videos; third-party scraping libraries are unofficial.",
        )

    if not api.exists or not api.documentation_available:
        return BuildabilityInfo(
            verdict=BuildabilityVerdict.NO_PRACTICAL_API,
            blocker="No public developer API or documentation available",
            rationale="The platform does not expose documented programmatic interfaces for external agent tools.",
        )

    # Partnership or Contact Sales gating
    if (
        creds.partnership_required
        or creds.contact_sales_required
        or creds.access_classification in {
            AccessClassification.PARTNER_GATED,
            AccessClassification.CONTACT_SALES_GATED,
        }
    ):
        return BuildabilityInfo(
            verdict=BuildabilityVerdict.NEEDS_PARTNERSHIP_SALES,
            blocker="Enterprise sales or formal partnership contract required to obtain API keys",
            rationale="Developers cannot self-provision credentials; contractual approval from sales/BD is mandatory.",
        )

    # Admin approval gating
    if creds.admin_approval_required or creds.access_classification == AccessClassification.ADMIN_GATED:
        return BuildabilityInfo(
            verdict=BuildabilityVerdict.NEEDS_ADMIN_APPROVAL,
            blocker="Workspace administrator approval or enterprise tenant permission required",
            rationale="End-users cannot provision integrations directly; tenant admin consent or security review is mandatory.",
        )

    # Self-serve free access
    if (
        creds.access_classification == AccessClassification.SELF_SERVE_FREE
        or (creds.self_serve and creds.free_access and not creds.paid_plan_required)
    ):
        return BuildabilityInfo(
            verdict=BuildabilityVerdict.READY,
            blocker="None",
            rationale="Publicly documented API with instant self-serve free developer access and standardized auth.",
        )

    # Paid plan required
    if creds.paid_plan_required or creds.access_classification == AccessClassification.SELF_SERVE_PAID:
        return BuildabilityInfo(
            verdict=BuildabilityVerdict.NEEDS_PAID_ACCESS,
            blocker="Active paid subscription required for developer credentials/API access",
            rationale="Free tier does not provide developer API keys or webhooks access; commercial subscription is required.",
        )

    # Trial available (where permanent free tier is NOT available)
    if creds.access_classification == AccessClassification.SELF_SERVE_TRIAL or creds.trial_available:
        return BuildabilityInfo(
            verdict=BuildabilityVerdict.READY_WITH_CAVEAT,
            blocker="Time-limited trial access; will require paid tier for ongoing agent execution",
            rationale="Self-serve trial enables immediate initial building and prototyping, but continuous production usage requires paid billing.",
        )

    # Fallback for public documented APIs
    if api.public:
        return BuildabilityInfo(
            verdict=BuildabilityVerdict.READY_WITH_CAVEAT,
            blocker="Rate limits or account tier restrictions",
            rationale="API is public and documented; developers should verify rate limits and access tiers.",
        )

    return BuildabilityInfo(
        verdict=BuildabilityVerdict.API_UNCLEAR,
        blocker="Ambiguous API onboarding or access terms",
        rationale="API existence is documented but credential provisioning path is unclear from public documentation.",
    )


def calculate_confidence(
    evidence_list: List[EvidenceSource],
    auth: AuthenticationInfo,
    creds: CredentialAccessInfo,
    api: APIInfo,
    mcp: MCPInfo,
) -> ConfidenceScore:
    """
    Calculates granular and overall confidence scores based on evidence depth and source types.
    """
    if not evidence_list:
        return ConfidenceScore(overall=0.2, auth=0.2, credential_access=0.2, api=0.2, mcp=0.2)

    # Official source count
    official_sources = [
        e for e in evidence_list
        if e.source_type in {
            "official_docs",
            "official_dev_portal",
            "official_auth_docs",
            "official_pricing",
            "official_mcp_docs",
            "official_repo",
        }
    ]

    has_auth_support = any("auth" in s.lower() or "oauth" in s.lower() or "api key" in s.lower() for e in evidence_list for s in e.supports)
    has_cred_support = any("access" in s.lower() or "pricing" in s.lower() or "free" in s.lower() or "plan" in s.lower() or "self-serve" in s.lower() for e in evidence_list for s in e.supports)
    has_api_support = any("api" in s.lower() or "rest" in s.lower() or "graphql" in s.lower() or "documentation" in s.lower() for e in evidence_list for s in e.supports)
    has_mcp_support = any("mcp" in s.lower() or "composio" in s.lower() or "tool" in s.lower() for e in evidence_list for s in e.supports)

    base_official = 0.5 + min(0.35, len(official_sources) * 0.1)

    auth_score = base_official if has_auth_support else 0.55
    cred_score = base_official if has_cred_support else 0.50
    api_score = base_official if has_api_support else 0.60
    mcp_score = 0.85 if has_mcp_support else 0.70

    overall = round((auth_score * 0.25) + (cred_score * 0.25) + (api_score * 0.3) + (mcp_score * 0.2), 2)
    overall = max(0.4, min(0.98, overall))

    return ConfidenceScore(
        overall=overall,
        auth=round(min(0.98, auth_score), 2),
        credential_access=round(min(0.98, cred_score), 2),
        api=round(min(0.98, api_score), 2),
        mcp=round(min(0.98, mcp_score), 2),
    )
