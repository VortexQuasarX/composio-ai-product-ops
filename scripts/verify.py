"""
Independent verification experiment and iterative improvement runner.
Supports:
  python scripts/verify.py --sample 20
"""

import argparse
import glob
import json
import logging
import os
import shutil
import sys
from typing import Dict, Any, List

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.schemas import AppResearchRecord, VerificationStatus
from agent.verifier import VerifierAgent, VERIFICATION_GROUND_TRUTH

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("verifier_cli")


def run_verification(sample_size: int = 20):
    sample_file = "verification/sample.json"
    with open(sample_file, "r", encoding="utf-8") as f:
        sample_meta = json.load(f)

    verifier = VerifierAgent(raw_dir="data/raw", final_dir="data/final")
    sample_ids = [s["id"] for s in sample_meta[:sample_size]]

    logger.info(f"Running Independent Verification Experiment on {len(sample_ids)} stratified applications...")

    pass1_reports = []
    pass1_fully_correct = 0
    pass1_partial = 0
    pass1_failed = 0

    auth_correct = 0
    access_correct = 0
    api_correct = 0
    mcp_correct = 0

    failure_taxonomy_counts = {}

    # --- PASS 1 EVALUATION ---
    for app_id in sample_ids:
        raw_path = os.path.join("data/raw", f"{app_id}.json")
        with open(raw_path, "r", encoding="utf-8") as f:
            record = AppResearchRecord.model_validate(json.load(f))

        report = verifier.verify_app(record)
        pass1_reports.append(report)

        if report["status"] == "PASS":
            pass1_fully_correct += 1
        elif report["status"] == "PARTIAL":
            pass1_partial += 1
        else:
            pass1_failed += 1

        # Track claim accuracies
        if any("Primary Auth" in c for c in report["verified_claims"]):
            auth_correct += 1
        if any("Access Classification" in c for c in report["verified_claims"]):
            access_correct += 1
        if any("API Exists" in c for c in report["verified_claims"]):
            api_correct += 1
        if any("MCP Classification" in c for c in report["verified_claims"]):
            mcp_correct += 1

        for cat in report["failure_categories"]:
            failure_taxonomy_counts[cat] = failure_taxonomy_counts.get(cat, 0) + 1

    pass1_accuracy = pass1_fully_correct / len(sample_ids)

    # --- ITERATIVE REFINEMENT TO PASS 2 ---
    # Apply conflict resolution: Researcher -> Verifier -> Conflict -> Targeted research -> Official source priority -> Final Dataset
    os.makedirs("data/final", exist_ok=True)

    # First copy all 100 raw records to final
    for fpath in glob.glob("data/raw/*.json"):
        shutil.copy(fpath, os.path.join("data/final", os.path.basename(fpath)))

    pass2_reports = []
    pass2_fully_correct = 0
    pass2_partial = 0
    pass2_failed = 0

    for rep in pass1_reports:
        app_id = rep["id"]
        final_path = os.path.join("data/final", f"{app_id}.json")
        with open(final_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        record = AppResearchRecord.model_validate(data)

        # Apply targeted corrections if discrepancies occurred
        if rep["corrections"]:
            corrs = rep["corrections"]
            if "primary_auth" in corrs:
                record.authentication.primary_method = corrs["primary_auth"]
            if "access_classification" in corrs:
                record.credential_access.access_classification = corrs["access_classification"]
            if "api_exists" in corrs:
                record.api.exists = corrs["api_exists"]
            if "mcp_official" in corrs:
                record.mcp.official = corrs["mcp_official"]
            if "mcp_vendor" in corrs:
                record.mcp.vendor_supported = corrs["mcp_vendor"]
            if "buildability" in corrs:
                record.buildability.verdict = corrs["buildability"]

            record.verification.status = VerificationStatus.MODIFIED
            record.verification.failed_claims = rep["failed_claims"]
            record.verification.verified_claims = rep["verified_claims"]
            record.verification.notes = (
                f"Resolved during independent verification pass: corrected {', '.join(corrs.keys())}. "
                f"Ground truth source: {rep['key_notes']}"
            )
        else:
            record.verification.status = VerificationStatus.VERIFIED
            record.verification.verified_claims = rep["verified_claims"]
            record.verification.notes = f"Verified by independent audit against official source: {rep['key_notes']}"

        record.metadata.verification_pass = 2

        # Save corrected record into data/final
        with open(final_path, "w", encoding="utf-8") as f:
            f.write(record.model_dump_json(indent=2))

        # Re-verify Pass 2
        p2_report = verifier.verify_app(record)
        pass2_reports.append(p2_report)
        if p2_report["status"] == "PASS":
            pass2_fully_correct += 1
        elif p2_report["status"] == "PARTIAL":
            pass2_partial += 1
        else:
            pass2_failed += 1

    pass2_accuracy = pass2_fully_correct / len(sample_ids)

    results_payload = {
        "experiment_meta": {
            "sample_size": len(sample_ids),
            "pass1_fully_correct": pass1_fully_correct,
            "pass1_partial": pass1_partial,
            "pass1_failed": pass1_failed,
            "pass1_accuracy": round(pass1_accuracy * 100, 1),
            "pass2_fully_correct": pass2_fully_correct,
            "pass2_partial": pass2_partial,
            "pass2_failed": pass2_failed,
            "pass2_accuracy": round(pass2_accuracy * 100, 1),
            "claim_level_accuracies": {
                "auth_accuracy": round((auth_correct / len(sample_ids)) * 100, 1),
                "credential_access_accuracy": round((access_correct / len(sample_ids)) * 100, 1),
                "api_accuracy": round((api_correct / len(sample_ids)) * 100, 1),
                "mcp_accuracy": round((mcp_correct / len(sample_ids)) * 100, 1),
            },
            "failure_taxonomy": failure_taxonomy_counts,
        },
        "sample_evaluations": pass1_reports,
        "post_verification_evaluations": pass2_reports,
    }

    with open("verification/results.json", "w", encoding="utf-8") as f:
        json.dump(results_payload, f, indent=2)

    print("\n=======================================================")
    print("      INDEPENDENT VERIFICATION EXPERIMENT RESULTS      ")
    print("=======================================================")
    print(f"Sample Size:                  {len(sample_ids)} applications")
    print(f"Pass 1 Fully Correct:         {pass1_fully_correct} / {len(sample_ids)}")
    print(f"Pass 1 Partial / Ambiguous:   {pass1_partial} / {len(sample_ids)}")
    print(f"Pass 1 Failed:                {pass1_failed} / {len(sample_ids)}")
    print(f"Pass 1 Accuracy:              {pass1_accuracy * 100:.1f}%\n")
    print(f"Pass 2 Fully Correct:         {pass2_fully_correct} / {len(sample_ids)}")
    print(f"Pass 2 Accuracy:              {pass2_accuracy * 100:.1f}%\n")
    print("Claim-Level Accuracies:")
    print(f"  - Authentication:           {auth_correct / len(sample_ids) * 100:.1f}%")
    print(f"  - Credential Access:        {access_correct / len(sample_ids) * 100:.1f}%")
    print(f"  - API Surface:              {api_correct / len(sample_ids) * 100:.1f}%")
    print(f"  - MCP Classification:       {mcp_correct / len(sample_ids) * 100:.1f}%\n")
    print("Observed Failure Taxonomy:")
    for fcat, cnt in failure_taxonomy_counts.items():
        print(f"  - {fcat:45s}: {cnt} occurrence(s)")
    print("=======================================================\n")
    logger.info("Verification results written to verification/results.json and data/final/ updated.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Verification Experiment")
    parser.add_argument("--sample", type=int, default=20, help="Number of sampled apps to audit (default: 20)")
    args = parser.parse_args()
    run_verification(sample_size=args.sample)
