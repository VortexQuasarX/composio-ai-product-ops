"""
Master workflow execution script for Composio AI Product Ops.
Executes the full pipeline:
  Research (100 apps) -> Dataset Validation -> Verification Experiment (20 apps) -> Pattern Analysis -> HTML Case Study
Supports:
  python scripts/run.py
"""

import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def run_step(step_name: str, cmd: list):
    print(f"\n=======================================================")
    print(f" STEP: {step_name}")
    print(f" COMMAND: {' '.join(cmd)}")
    print(f"=======================================================")
    t0 = time.time()
    res = subprocess.run(cmd, capture_output=False, text=True)
    dt = time.time() - t0
    if res.returncode != 0:
        print(f"\n[ERROR] Step '{step_name}' failed with exit code {res.returncode}")
        sys.exit(res.returncode)
    print(f"[SUCCESS] Step '{step_name}' completed in {dt:.2f}s")


def main():
    python_exe = sys.executable
    print("=======================================================")
    print("   COMPOSIO AI PRODUCT OPS - MASTER WORKFLOW RUNNER   ")
    print("=======================================================")

    # Step 1: Research All 100 Apps
    run_step("1. Research All 100 Applications", [python_exe, "scripts/research.py", "--all"])

    # Step 2: Validate Dataset Schema & Integrity
    run_step("2. Audit & Validate Dataset", [python_exe, "scripts/validate_dataset.py"])

    # Step 3: Run Verification Experiment (20 Apps)
    run_step("3. Independent Verification Audit", [python_exe, "scripts/verify.py", "--sample", "20"])

    # Step 4: Generate Strategic Patterns
    run_step("4. Calculate Metrics & Patterns", [python_exe, "analysis/patterns.py"])

    # Step 5: Build Final HTML Case Study
    run_step("5. Compile HTML Case Study", [python_exe, "scripts/build_case_study.py"])

    print("\n=======================================================")
    print("             MASTER WORKFLOW COMPLETE                  ")
    print("=======================================================")
    print("Deliverables generated:")
    print("  - Raw Dataset:         data/raw/ (100 JSON files)")
    print("  - Final Dataset:       data/final/ (100 verified JSON files)")
    print("  - Verification Audit:  verification/results.json")
    print("  - HTML Case Study:     web/index.html")
    print("=======================================================\n")


if __name__ == "__main__":
    main()
