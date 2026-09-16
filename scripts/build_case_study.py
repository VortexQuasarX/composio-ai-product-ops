"""
CLI script to trigger HTML case study generation.
Supports:
  python scripts/build_case_study.py
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from web.generate import generate_html


def main():
    out_file = generate_html("web/index.html")
    print(f"HTML Case Study ready at {out_file}")


if __name__ == "__main__":
    main()
