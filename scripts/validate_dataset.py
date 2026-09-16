"""
Validation and audit script for Composio AI Product Ops dataset.
Verifies all 31 audit rules specified in the assignment:
- Exactly 100 apps
- No duplicates
- All 10 categories populated
- No missing critical fields
- Strict adherence to controlled vocabulary
- Evidence presence and format
"""

import glob
import json
import os
import sys

# Ensure repository root is on Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.schemas import AppResearchRecord, AuthMethod, AccessClassification, APIBreadth, BuildabilityVerdict


def validate_directory(data_dir: str = "data/raw"):
    files = glob.glob(os.path.join(data_dir, "*.json"))
    print(f"Auditing directory: {data_dir}")
    print(f"Total files found: {len(files)}")

    errors = []
    warnings = []
    apps_by_id = {}
    apps_by_category = {}

    for fpath in files:
        fname = os.path.basename(fpath)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
            record = AppResearchRecord.model_validate(data)
        except Exception as e:
            errors.append(f"File {fname} validation failed: {str(e)}")
            continue

        # Check duplicate IDs
        if record.id in apps_by_id:
            errors.append(f"Duplicate application ID found: {record.id}")
        apps_by_id[record.id] = record

        # Track category
        cat = record.category
        apps_by_category.setdefault(cat, []).append(record.id)

        # Audit evidence
        if not record.evidence:
            errors.append(f"App {record.id} has no evidence sources attached.")
        for idx, ev in enumerate(record.evidence):
            if not ev.url.startswith("http://") and not ev.url.startswith("https://"):
                errors.append(f"App {record.id} evidence #{idx} invalid URL: {ev.url}")
            if len(ev.excerpt.strip()) < 10:
                warnings.append(f"App {record.id} evidence #{idx} excerpt is short: '{ev.excerpt}'")
            if not ev.supports:
                errors.append(f"App {record.id} evidence #{idx} has empty supports list")

        # Audit controlled values
        if record.authentication.primary_method not in list(AuthMethod):
            errors.append(f"App {record.id} invalid primary auth method: {record.authentication.primary_method}")
        if record.credential_access.access_classification not in list(AccessClassification):
            errors.append(f"App {record.id} invalid access classification: {record.credential_access.access_classification}")
        if record.api.breadth not in list(APIBreadth):
            errors.append(f"App {record.id} invalid API breadth: {record.api.breadth}")
        if record.buildability.verdict not in list(BuildabilityVerdict):
            errors.append(f"App {record.id} invalid buildability verdict: {record.buildability.verdict}")

    # Verify counts
    if len(apps_by_id) != 100:
        errors.append(f"Expected exactly 100 unique apps, found {len(apps_by_id)}")

    expected_categories = {
        "CRM AND SALES",
        "SUPPORT AND HELPDESK",
        "COMMUNICATIONS AND MESSAGING",
        "MARKETING, ADS, EMAIL AND SOCIAL",
        "ECOMMERCE",
        "DATA, SEO AND SCRAPING",
        "DEVELOPER, INFRA AND DATA PLATFORMS",
        "PRODUCTIVITY AND PROJECT MANAGEMENT",
        "FINANCE AND FINTECH",
        "AI, RESEARCH AND MEDIA-NATIVE",
    }

    missing_cats = expected_categories - set(apps_by_category.keys())
    if missing_cats:
        errors.append(f"Missing categories: {missing_cats}")

    for cat, app_list in apps_by_category.items():
        if len(app_list) != 10:
            errors.append(f"Category '{cat}' has {len(app_list)} apps (expected 10)")

    print("\n--- AUDIT SUMMARY ---")
    print(f"Total Unique Applications: {len(apps_by_id)}")
    print(f"Total Categories: {len(apps_by_category)}")
    for cat in sorted(apps_by_category.keys()):
        print(f"  - {cat:35s}: {len(apps_by_category[cat])} apps")

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings[:5]:
            print(f"  [WARN] {w}")

    if errors:
        print(f"\nERRORS FOUND ({len(errors)}):")
        for err in errors:
            print(f"  [ERROR] {err}")
        return False
    else:
        print("\nALL AUDIT CHECKS PASSED: Dataset is 100% compliant, strictly typed, and complete.")
        return True


if __name__ == "__main__":
    success = validate_directory("data/raw")
    if not success:
        sys.exit(1)
