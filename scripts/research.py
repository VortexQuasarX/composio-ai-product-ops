"""
CLI script to execute the research agent across individual apps or the entire 100-app catalog.
Supports:
  python scripts/research.py --app "HubSpot"
  python scripts/research.py --all
"""

import argparse
import json
import logging
import os
import sys

# Ensure repository root is on Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.researcher import ResearchAgent

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("research_cli")


def load_catalog(catalog_path: str = "data/apps.json"):
    with open(catalog_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_research(app_query: str = None, run_all: bool = False, pass_num: int = 1):
    agent = ResearchAgent(raw_dir="data/raw", final_dir="data/final")
    catalog = load_catalog()

    if app_query:
        # Match by id or name case-insensitively
        matches = [
            a for a in catalog
            if a["id"].lower() == app_query.lower() or a["name"].lower() == app_query.lower()
        ]
        if not matches:
            logger.error(f"Application '{app_query}' not found in catalog.")
            sys.exit(1)
        target_apps = matches
    elif run_all:
        target_apps = catalog
    else:
        logger.error("Must specify either --app <name> or --all")
        sys.exit(1)

    logger.info(f"Starting research run for {len(target_apps)} application(s) [Pass {pass_num}]...")
    results = []
    errors = []

    for idx, app in enumerate(target_apps, start=1):
        app_id = app["id"]
        try:
            record = agent.research_app(app, pass_num=pass_num)
            results.append(record)
            print(
                f"[{idx:3d}/{len(target_apps):3d}] {record.app_name:25s} | "
                f"Auth: {record.authentication.primary_method.value:18s} | "
                f"Access: {record.credential_access.access_classification.value:20s} | "
                f"MCP: {str(record.mcp.exists):5s} | "
                f"Buildability: {record.buildability.verdict.value:24s} | "
                f"Conf: {record.confidence.overall:.2f}"
            )
        except Exception as e:
            logger.error(f"Failed to research app {app_id}: {str(e)}", exc_info=True)
            errors.append((app_id, str(e)))

    logger.info(f"Research run completed. Success: {len(results)}, Failures: {len(errors)}")
    if errors:
        print("\nFailures:")
        for fid, err in errors:
            print(f"  - {fid}: {err}")
    return results, errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Composio AI Product Ops Research Agent")
    parser.add_argument("--app", type=str, help="Specific app name or ID to research")
    parser.add_argument("--all", action="store_true", help="Research all 100 applications in catalog")
    parser.add_argument("--pass", dest="pass_num", type=int, default=1, help="Research pass number (1 or 2)")

    args = parser.parse_args()
    run_research(app_query=args.app, run_all=args.all, pass_num=args.pass_num)
