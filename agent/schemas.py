"""
Strict Pydantic data models and controlled vocabulary for Composio Product Ops research.
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl, field_validator


class AuthMethod(str, Enum):
    OAUTH2 = "OAuth2"
    API_KEY = "API Key"
    BASIC_AUTH = "Basic Auth"
    BEARER_TOKEN = "Bearer Token"
    PERSONAL_ACCESS_TOKEN = "Personal Access Token"
    JWT = "JWT"
    SESSION_COOKIE = "Session/Cookie"
    HMAC = "HMAC"
    AWS_SIGNATURE = "AWS Signature"
    OTHER = "Other"
    UNKNOWN = "Unknown"


class AccessClassification(str, Enum):
    SELF_SERVE_FREE = "Self-serve free"
    SELF_SERVE_TRIAL = "Self-serve trial"
    SELF_SERVE_PAID = "Self-serve paid"
    ADMIN_GATED = "Admin-gated"
    CONTACT_SALES_GATED = "Contact-sales gated"
    PARTNER_GATED = "Partner-gated"
    NO_DEVELOPER_ACCESS = "No developer access found"
    UNKNOWN = "Unknown"


class APIBreadth(str, Enum):
    NARROW = "Narrow"
    MODERATE = "Moderate"
    BROAD = "Broad"
    VERY_BROAD = "Very broad"
    UNKNOWN = "Unknown"


class BuildabilityVerdict(str, Enum):
    READY = "Ready"
    READY_WITH_CAVEAT = "Ready with access caveat"
    NEEDS_PAID_ACCESS = "Needs paid access"
    NEEDS_ADMIN_APPROVAL = "Needs admin approval"
    NEEDS_PARTNERSHIP_SALES = "Needs partnership/contact-sales"
    API_UNCLEAR = "API unclear"
    NO_PRACTICAL_API = "No practical public API"
    CLI_LOCAL_TOOL = "CLI/local tool"
    UNKNOWN = "Unknown"


class VerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    MODIFIED = "modified"
    FLAG_CONFLICT = "flag_conflict"


class EvidenceSource(BaseModel):
    url: str
    title: str
    source_type: str = Field(..., description="official_docs, official_dev_portal, official_auth_docs, official_pricing, official_mcp_docs, official_repo, secondary_source, other")
    supports: List[str] = Field(default_factory=list, description="List of claims supported, e.g. ['OAuth2', 'REST API', 'Self-serve free']")
    excerpt: str = Field(..., description="Direct quote or specific technical factual snippet from the source")
    retrieved_at: str


class AuthenticationInfo(BaseModel):
    methods: List[AuthMethod] = Field(default_factory=list)
    primary_method: AuthMethod = AuthMethod.UNKNOWN
    oauth2: bool = False
    api_key: bool = False
    basic_auth: bool = False
    bearer_token: bool = False
    personal_access_token: bool = False
    other: Optional[str] = None


class CredentialAccessInfo(BaseModel):
    self_serve: bool = False
    free_access: bool = False
    trial_available: bool = False
    paid_plan_required: bool = False
    admin_approval_required: bool = False
    contact_sales_required: bool = False
    partnership_required: bool = False
    developer_account_required: bool = True
    access_classification: AccessClassification = AccessClassification.UNKNOWN
    notes: str = ""


class APIInfo(BaseModel):
    exists: bool = False
    public: bool = False
    type: List[str] = Field(default_factory=list, description="REST, GraphQL, SDK, CLI, Webhooks, gRPC, SOAP, etc.")
    rest: bool = False
    graphql: bool = False
    sdk: bool = False
    cli: bool = False
    webhooks: bool = False
    documentation_available: bool = False
    breadth: APIBreadth = APIBreadth.UNKNOWN
    major_resource_areas: List[str] = Field(default_factory=list)


class MCPInfo(BaseModel):
    exists: bool = False
    official: bool = False
    vendor_supported: bool = False
    community: bool = False
    composio_support: bool = False
    url: Optional[str] = None
    notes: str = ""


class BuildabilityInfo(BaseModel):
    verdict: BuildabilityVerdict = BuildabilityVerdict.UNKNOWN
    blocker: str = "None"
    rationale: str = ""


class ConfidenceScore(BaseModel):
    overall: float = Field(ge=0.0, le=1.0, default=0.5)
    auth: float = Field(ge=0.0, le=1.0, default=0.5)
    credential_access: float = Field(ge=0.0, le=1.0, default=0.5)
    api: float = Field(ge=0.0, le=1.0, default=0.5)
    mcp: float = Field(ge=0.0, le=1.0, default=0.5)


class VerificationRecord(BaseModel):
    status: VerificationStatus = VerificationStatus.UNVERIFIED
    verified_claims: List[str] = Field(default_factory=list)
    failed_claims: List[str] = Field(default_factory=list)
    notes: str = ""


class MetadataInfo(BaseModel):
    researched_at: str
    researcher_model: str
    verification_pass: int = 1


class AppResearchRecord(BaseModel):
    id: str
    app_name: str
    category: str
    website: str
    one_line_description: str
    authentication: AuthenticationInfo
    credential_access: CredentialAccessInfo
    api: APIInfo
    mcp: MCPInfo
    buildability: BuildabilityInfo
    evidence: List[EvidenceSource] = Field(default_factory=list)
    confidence: ConfidenceScore
    verification: VerificationRecord
    metadata: MetadataInfo
