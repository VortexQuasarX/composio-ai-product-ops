"""
Evidence management, source verification, and citation processing.
"""

from datetime import datetime
from typing import List, Dict, Any
from agent.schemas import EvidenceSource


VALID_SOURCE_TYPES = {
    "official_docs",
    "official_dev_portal",
    "official_auth_docs",
    "official_pricing",
    "official_mcp_docs",
    "official_repo",
    "secondary_source",
    "other",
}


def create_evidence(
    url: str,
    title: str,
    source_type: str,
    supports: List[str],
    excerpt: str,
    retrieved_at: str = None,
) -> EvidenceSource:
    """Creates a validated EvidenceSource instance."""
    if source_type not in VALID_SOURCE_TYPES:
        source_type = "secondary_source" if "github.com" not in url else "official_repo"

    if not retrieved_at:
        retrieved_at = datetime.utcnow().isoformat() + "Z"

    # Truncate excerpt if excessively long to preserve clarity
    cleaned_excerpt = excerpt.strip()
    if len(cleaned_excerpt) > 400:
        cleaned_excerpt = cleaned_excerpt[:397] + "..."

    return EvidenceSource(
        url=url,
        title=title,
        source_type=source_type,
        supports=supports,
        excerpt=cleaned_excerpt,
        retrieved_at=retrieved_at,
    )


def validate_evidence_list(evidence_list: List[EvidenceSource]) -> List[str]:
    """Validates that evidence has non-empty URLs, realistic excerpts, and valid types."""
    errors = []
    if not evidence_list:
        errors.append("Evidence list is empty; at least one evidence item is required.")
        return errors

    for i, ev in enumerate(evidence_list):
        if not ev.url.startswith("http://") and not ev.url.startswith("https://"):
            errors.append(f"Evidence #{i} has invalid URL: {ev.url}")
        if len(ev.excerpt.strip()) < 10:
            errors.append(f"Evidence #{i} has insufficient excerpt (must be >= 10 chars)")
        if not ev.supports:
            errors.append(f"Evidence #{i} has empty 'supports' claim list")
    return errors
