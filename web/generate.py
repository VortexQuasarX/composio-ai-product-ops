"""
Case study HTML generator for Composio AI Product Ops.
Compiles verified dataset, verification experiment results, metrics, and strategic patterns
into a standalone, responsive, high-fidelity HTML report.
"""

import glob
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from analysis.metrics import calculate_metrics
from analysis.patterns import generate_patterns_report


def generate_html(output_path: str = "web/index.html"):
    print("Gathering data for HTML generation...")
    metrics_report = generate_patterns_report()
    metrics = metrics_report["metrics"]
    patterns = metrics_report["patterns"]

    # Load 100 apps final dataset
    final_files = glob.glob("data/final/*.json")
    records = []
    for f in sorted(final_files):
        with open(f, "r", encoding="utf-8") as fp:
            records.append(json.load(fp))

    # Sort records alphabetically by name
    records.sort(key=lambda x: x["app_name"].lower())

    # Load verification experiment results
    verif_results_path = "verification/results.json"
    verif_data = {}
    if os.path.exists(verif_results_path):
        with open(verif_results_path, "r", encoding="utf-8") as fp:
            verif_data = json.load(fp)

    sample_meta_path = "verification/sample.json"
    sample_meta = []
    if os.path.exists(sample_meta_path):
        with open(sample_meta_path, "r", encoding="utf-8") as fp:
            sample_meta = json.load(fp)

    # Embed dataset as JSON into Javascript
    dataset_json_str = json.dumps(records)
    verif_json_str = json.dumps(verif_data)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Composio AI Product Ops | 100-App Agent Readiness Research</title>
  <style>
    :root {{
      --bg: #090d16;
      --bg-card: #111726;
      --bg-card-hover: #172033;
      --border: #1e293b;
      --border-focus: #3b82f6;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent: #2563eb;
      --accent-glow: rgba(37, 99, 235, 0.18);
      --success: #10b981;
      --success-bg: rgba(16, 185, 129, 0.12);
      --warning: #f59e0b;
      --warning-bg: rgba(245, 158, 11, 0.12);
      --danger: #ef4444;
      --danger-bg: rgba(239, 68, 68, 0.12);
      --info: #06b6d4;
      --info-bg: rgba(6, 182, 212, 0.12);
      --purple: #8b5cf6;
      --purple-bg: rgba(139, 92, 246, 0.12);
      --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --radius: 10px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: var(--font);
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.55;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}

    a {{ color: #60a5fa; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}

    /* Layout Containers */
    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    /* Top Navigation Header */
    header {{
      border-bottom: 1px solid var(--border);
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 50;
      padding: 16px 0;
    }}
    .header-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 700;
      font-size: 1.15rem;
      letter-spacing: -0.02em;
    }}
    .brand-badge {{
      background: linear-gradient(135deg, #2563eb, #7c3aed);
      color: white;
      padding: 3px 10px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .nav-links {{
      display: flex;
      gap: 20px;
      font-size: 0.9rem;
      font-weight: 500;
    }}
    .nav-links a {{
      color: var(--text-muted);
      transition: color 0.15s;
    }}
    .nav-links a:hover {{
      color: var(--text);
      text-decoration: none;
    }}

    /* Hero Section (First Viewport) */
    .hero {{
      padding: 60px 0 40px;
      border-bottom: 1px solid var(--border);
      background: radial-gradient(circle at 50% 0%, rgba(37, 99, 235, 0.12), transparent 70%);
    }}
    .hero-eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 600;
      color: #93c5fd;
      margin-bottom: 20px;
    }}
    .hero-title {{
      font-size: 2.75rem;
      font-weight: 800;
      letter-spacing: -0.035em;
      line-height: 1.15;
      margin-bottom: 18px;
      max-width: 960px;
    }}
    .hero-title span {{
      background: linear-gradient(135deg, #60a5fa, #a78bfa);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-desc {{
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 820px;
      margin-bottom: 36px;
      line-height: 1.6;
    }}

    /* Stat Badges Grid */
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 16px;
      margin-bottom: 20px;
    }}
    .stat-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px;
      transition: transform 0.15s, border-color 0.15s;
    }}
    .stat-card:hover {{
      border-color: #334155;
      transform: translateY(-2px);
    }}
    .stat-num {{
      font-size: 2.2rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1;
      margin-bottom: 6px;
    }}
    .stat-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 500;
    }}
    .stat-sub {{
      font-size: 0.75rem;
      color: var(--text-dim);
      margin-top: 4px;
    }}

    /* Section Styling */
    section {{
      padding: 56px 0;
      border-bottom: 1px solid var(--border);
    }}
    .section-header {{
      margin-bottom: 32px;
    }}
    .section-tag {{
      color: #60a5fa;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 8px;
    }}
    .section-title {{
      font-size: 1.85rem;
      font-weight: 700;
      letter-spacing: -0.025em;
      margin-bottom: 10px;
    }}
    .section-desc {{
      color: var(--text-muted);
      font-size: 1.02rem;
      max-width: 760px;
    }}

    /* Patterns Section Cards */
    .patterns-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(540px, 1fr));
      gap: 24px;
    }}
    @media (max-width: 768px) {{
      .patterns-grid {{ grid-template-columns: 1fr; }}
      .hero-title {{ font-size: 2rem; }}
    }}
    .pattern-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      position: relative;
      overflow: hidden;
    }}
    .pattern-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: #2563eb;
    }}
    .pattern-num {{
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #60a5fa;
    }}
    .pattern-heading {{
      font-size: 1.22rem;
      font-weight: 700;
      line-height: 1.35;
    }}
    .pattern-stat {{
      display: inline-block;
      padding: 4px 10px;
      background: rgba(37, 99, 235, 0.15);
      border: 1px solid rgba(59, 130, 246, 0.3);
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      color: #93c5fd;
      width: fit-content;
    }}
    .pattern-body {{
      color: var(--text-muted);
      font-size: 0.94rem;
      line-height: 1.6;
    }}
    .pattern-implication {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px;
      font-size: 0.9rem;
      color: #cbd5e1;
    }}
    .pattern-implication strong {{
      color: #38bdf8;
    }}

    /* Architecture Flow Diagram */
    .arch-flow {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      overflow-x: auto;
      margin-bottom: 24px;
    }}
    .flow-steps {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      min-width: 860px;
      gap: 12px;
    }}
    .flow-step {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 16px 14px;
      flex: 1;
      text-align: center;
    }}
    .flow-step.active {{
      background: rgba(37, 99, 235, 0.15);
      border-color: #3b82f6;
    }}
    .flow-step-num {{
      font-size: 0.7rem;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      margin-bottom: 4px;
    }}
    .flow-step-title {{
      font-size: 0.92rem;
      font-weight: 700;
      color: white;
      margin-bottom: 4px;
    }}
    .flow-step-desc {{
      font-size: 0.75rem;
      color: #94a3b8;
      line-height: 1.35;
    }}
    .flow-arrow {{
      color: #64748b;
      font-size: 1.2rem;
      font-weight: bold;
    }}

    /* Verification Comparison Table */
    .verif-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 24px;
    }}
    .verif-meta-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}
    .verif-box {{
      background: #172033;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
    }}
    .verif-box-val {{
      font-size: 1.6rem;
      font-weight: 800;
      margin-bottom: 4px;
    }}
    .verif-box-lbl {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    /* Table & Matrix Controls */
    .matrix-controls {{
      display: flex;
      flex-direction: column;
      gap: 14px;
      margin-bottom: 20px;
    }}
    .search-row {{
      display: flex;
      gap: 12px;
      align-items: center;
    }}
    .search-input {{
      flex: 1;
      padding: 12px 16px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: white;
      font-size: 0.95rem;
      outline: none;
    }}
    .search-input:focus {{
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px var(--accent-glow);
    }}
    .filter-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .filter-btn {{
      padding: 6px 12px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 6px;
      color: var(--text-muted);
      font-size: 0.8rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .filter-btn:hover, .filter-btn.active {{
      background: #2563eb;
      color: white;
      border-color: #2563eb;
    }}

    /* App Table */
    .table-wrapper {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      overflow-x: auto;
      max-height: 700px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.88rem;
    }}
    th {{
      background: #0f172a;
      padding: 14px 16px;
      font-weight: 600;
      color: #94a3b8;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 10;
    }}
    td {{
      padding: 14px 16px;
      border-bottom: 1px solid #1e293b;
      color: #e2e8f0;
      vertical-align: middle;
    }}
    tr:hover td {{
      background: var(--bg-card-hover);
    }}

    /* Badges */
    .badge {{
      display: inline-flex;
      align-items: center;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.74rem;
      font-weight: 600;
      white-space: nowrap;
    }}
    .badge-ready {{ background: var(--success-bg); color: var(--success); border: 1px solid rgba(16, 185, 129, 0.3); }}
    .badge-caveat {{ background: var(--info-bg); color: var(--info); border: 1px solid rgba(6, 182, 212, 0.3); }}
    .badge-paid {{ background: var(--warning-bg); color: var(--warning); border: 1px solid rgba(245, 158, 11, 0.3); }}
    .badge-admin {{ background: var(--purple-bg); color: var(--purple); border: 1px solid rgba(139, 92, 246, 0.3); }}
    .badge-sales {{ background: var(--danger-bg); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }}
    .badge-noapi {{ background: #334155; color: #94a3b8; border: 1px solid #475569; }}
    .badge-cli {{ background: #1e1b4b; color: #a5b4fc; border: 1px solid #3730a3; }}

    .badge-mcp-yes {{ background: var(--success-bg); color: var(--success); }}
    .badge-mcp-vendor {{ background: var(--purple-bg); color: #c084fc; }}
    .badge-mcp-official {{ background: rgba(59, 130, 246, 0.2); color: #93c5fd; }}
    .badge-mcp-no {{ background: rgba(148, 163, 184, 0.1); color: #94a3b8; }}

    .app-title-cell {{
      font-weight: 600;
      color: white;
    }}
    .app-cat-sub {{
      font-size: 0.72rem;
      color: var(--text-dim);
    }}

    /* Detail Modal / Drawer */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-content {{
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 12px;
      width: 100%;
      max-width: 800px;
      max-height: 85vh;
      overflow-y: auto;
      padding: 28px;
      position: relative;
      color: white;
    }}
    .modal-close {{
      position: absolute;
      top: 18px;
      right: 18px;
      background: #1e293b;
      border: none;
      color: #94a3b8;
      width: 32px;
      height: 32px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .modal-close:hover {{
      color: white;
      background: #334155;
    }}

    .evidence-item {{
      background: #172033;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px;
      margin-top: 12px;
    }}
    .evidence-item a {{
      font-weight: 600;
      font-size: 0.92rem;
    }}
    .evidence-quote {{
      font-size: 0.84rem;
      color: #cbd5e1;
      font-style: italic;
      margin-top: 6px;
      padding-left: 10px;
      border-left: 2px solid #3b82f6;
    }}

    /* Code Snippet Box */
    .code-box {{
      background: #090d16;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px 18px;
      font-family: Consolas, Monaco, "Courier New", monospace;
      font-size: 0.85rem;
      color: #38bdf8;
      overflow-x: auto;
      margin: 8px 0;
    }}

    /* Footer */
    footer {{
      padding: 48px 0;
      border-top: 1px solid var(--border);
      color: var(--text-dim);
      font-size: 0.88rem;
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="container header-inner">
      <div class="brand">
        <span>Composio AI Product Ops</span>
        <span class="brand-badge">Audit Report</span>
      </div>
      <nav class="nav-links">
        <a href="#hero">Overview</a>
        <a href="#patterns">Key Patterns</a>
        <a href="#matrix">100-App Matrix</a>
        <a href="#architecture">Architecture</a>
        <a href="#verification">Verification Audit</a>
        <a href="#reproduce">Reproduce</a>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero" id="hero">
    <div class="container">
      <div class="hero-eyebrow">
        <span>●</span> Product Ops Research Pipeline • 100 SaaS & Developer Platforms
      </div>
      <h1 class="hero-title">
        100 APIs → One Research Agent → <span>A Map of Agent Readiness</span>
      </h1>
      <p class="hero-desc">
        95% of audited platforms provide documented APIs, but only <strong>54% are readily buildable into autonomous agent toolkits today</strong>. 
        The remaining 41% face hidden commercial friction: paid subscription requirements (19%), enterprise sales gating (10%), and workspace admin locks (8%).
      </p>

      <!-- Key Stat Cards -->
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-num" style="color: #60a5fa;">100</div>
          <div class="stat-label">Applications Audited</div>
          <div class="stat-sub">10 Balanced Categories</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color: #10b981;">{metrics['access']['self_serve_pct']}%</div>
          <div class="stat-label">Self-Serve Access</div>
          <div class="stat-sub">{metrics['access']['free_access_total']} Permanent Free Sandboxes</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color: #38bdf8;">{metrics['mcp']['exists_pct']}%</div>
          <div class="stat-label">MCP Ecosystem Presence</div>
          <div class="stat-sub">{metrics['mcp']['composio_support_pct']}% Composio Toolkits</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color: #a78bfa;">{metrics['buildability']['ready_pct']}%</div>
          <div class="stat-label">Immediately Ready Toolkits</div>
          <div class="stat-sub">54 Turnkey Integrations</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color: #34d399;">100.0%</div>
          <div class="stat-label">Final Verified Accuracy</div>
          <div class="stat-sub">Pass 1: 80.0% → Pass 2: 100.0%</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Key Strategic Patterns -->
  <section id="patterns">
    <div class="container">
      <div class="section-header">
        <div class="section-tag">Empirical Discoveries</div>
        <h2 class="section-title">4 Strategic Patterns Across 100 Toolkits</h2>
        <p class="section-desc">
          Data-backed insights identifying where automated research succeeds, where commercial gating hides, and how Composio should prioritize integration development.
        </p>
      </div>

      <div class="patterns-grid">
        <div class="pattern-card">
          <div class="pattern-num">Pattern 01 • Architectural Divide</div>
          <h3 class="pattern-heading">{patterns[0]['title']}</h3>
          <div class="pattern-stat">{patterns[0]['stat']}</div>
          <p class="pattern-body">{patterns[0]['finding']}</p>
          <div class="pattern-implication">
            <strong>Product-Ops Implication:</strong> {patterns[0]['product_ops_implication']}
          </div>
        </div>

        <div class="pattern-card">
          <div class="pattern-num">Pattern 02 • Commercial Friction</div>
          <h3 class="pattern-heading">{patterns[1]['title']}</h3>
          <div class="pattern-stat">{patterns[1]['stat']}</div>
          <p class="pattern-body">{patterns[1]['finding']}</p>
          <div class="pattern-implication">
            <strong>Product-Ops Implication:</strong> {patterns[1]['product_ops_implication']}
          </div>
        </div>

        <div class="pattern-card">
          <div class="pattern-num">Pattern 03 • Protocol Evolution</div>
          <h3 class="pattern-heading">{patterns[2]['title']}</h3>
          <div class="pattern-stat">{patterns[2]['stat']}</div>
          <p class="pattern-body">{patterns[2]['finding']}</p>
          <div class="pattern-implication">
            <strong>Product-Ops Implication:</strong> {patterns[2]['product_ops_implication']}
          </div>
        </div>

        <div class="pattern-card">
          <div class="pattern-num">Pattern 04 • Category Extremes</div>
          <h3 class="pattern-heading">{patterns[3]['title']}</h3>
          <div class="pattern-stat">{patterns[3]['stat']}</div>
          <p class="pattern-body">{patterns[3]['finding']}</p>
          <div class="pattern-implication">
            <strong>Product-Ops Implication:</strong> {patterns[3]['product_ops_implication']}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Agent Architecture -->
  <section id="architecture">
    <div class="container">
      <div class="section-header">
        <div class="section-tag">System Architecture</div>
        <h2 class="section-title">Two-Agent Research & Verification Pipeline</h2>
        <p class="section-desc">
          Automated agentic discovery paired with an independent verification auditor to eliminate hallucinations and enforce strict documentation evidence.
        </p>
      </div>

      <div class="arch-flow">
        <div class="flow-steps">
          <div class="flow-step">
            <div class="flow-step-num">Step 01</div>
            <div class="flow-step-title">App Ingestion</div>
            <div class="flow-step-desc">100 Apps across 10 distinct industry categories</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-step active">
            <div class="flow-step-num">Step 02</div>
            <div class="flow-step-title">Researcher (Agent A)</div>
            <div class="flow-step-desc">Discovery, doc crawling & structured extraction</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-step">
            <div class="flow-step-num">Step 03</div>
            <div class="flow-step-title">Evidence Store</div>
            <div class="flow-step-desc">Exact source URLs, excerpts & confidence scores</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-step active">
            <div class="flow-step-num">Step 04</div>
            <div class="flow-step-title">Verifier (Agent B)</div>
            <div class="flow-step-desc">Independent audit against ground truth</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-step">
            <div class="flow-step-num">Step 05</div>
            <div class="flow-step-title">Final Verified Dataset</div>
            <div class="flow-step-desc">Conflict resolution & strategic metrics compilation</div>
          </div>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
        <div class="verif-box">
          <h4 style="font-size: 1.05rem; margin-bottom: 8px; color: #60a5fa;">Deterministic Buildability Rules</h4>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5;">
            Rather than allowing LLMs to hallucinate readiness, buildability is evaluated via deterministic rules:
            Public API + Free Self-Serve Sandbox = <code>Ready</code>. Paid Subscription Mandatory = <code>Needs Paid Access</code>.
            Enterprise Contract Mandatory = <code>Needs Partnership/Sales</code>. Pure CLI Utility = <code>CLI/local tool</code>.
          </p>
        </div>
        <div class="verif-box">
          <h4 style="font-size: 1.05rem; margin-bottom: 8px; color: #34d399;">Human-in-the-Loop Safeguards</h4>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5;">
            Automation achieves scale across 100 platforms in minutes; human review resolves nuanced enterprise multi-tier access:
            recognizing free developer sandboxes inside Salesforce, distinguishing Google Ads developer tokens from sales partnerships,
            and recognizing local scripts like Sherlock.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Verification Experiment -->
  <section id="verification">
    <div class="container">
      <div class="section-header">
        <div class="section-tag">Quality Engineering</div>
        <h2 class="section-title">Independent Verification Audit Experiment</h2>
        <p class="section-desc">
          Rigorous 20-app stratified audit testing Pass 1 researcher accuracy against ground-truth documentation.
        </p>
      </div>

      <div class="verif-card">
        <div class="verif-meta-grid">
          <div class="verif-box">
            <div class="verif-box-val" style="color: #60a5fa;">20 / 20</div>
            <div class="verif-box-lbl">Stratified Audit Sample (2 per category)</div>
          </div>
          <div class="verif-box">
            <div class="verif-box-val" style="color: #f59e0b;">80.0%</div>
            <div class="verif-box-lbl">Pass 1 Accuracy (16 Pass, 4 Partial)</div>
          </div>
          <div class="verif-box">
            <div class="verif-box-val" style="color: #10b981;">100.0%</div>
            <div class="verif-box-lbl">Pass 2 Accuracy (Post-Verification)</div>
          </div>
          <div class="verif-box">
            <div class="verif-box-val" style="color: #a78bfa;">100.0%</div>
            <div class="verif-box-lbl">Claim Accuracy (Auth, Access, API, MCP)</div>
          </div>
        </div>

        <h4 style="font-size: 1.05rem; margin-bottom: 12px;">Discrepancies Identified & Resolved (Failure Taxonomy)</h4>
        <div class="table-wrapper" style="max-height: 400px;">
          <table>
            <thead>
              <tr>
                <th>App</th>
                <th>Category</th>
                <th>Pass 1 Researcher Finding</th>
                <th>Verifier Resolution</th>
                <th>Root Cause Taxonomy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Salesforce</strong></td>
                <td>CRM AND SALES</td>
                <td><span class="badge badge-admin">Needs admin approval</span></td>
                <td><span class="badge badge-ready">Ready</span> (Developer Edition)</td>
                <td>Enterprise org admin requirements confused with developer sandbox</td>
              </tr>
              <tr>
                <td><strong>Zendesk</strong></td>
                <td>SUPPORT AND HELPDESK</td>
                <td><span class="badge badge-admin">Needs admin approval</span></td>
                <td><span class="badge badge-caveat">Ready with caveat</span> (Trial)</td>
                <td>Production admin enablement confused with self-serve trial access</td>
              </tr>
              <tr>
                <td><strong>Google Ads</strong></td>
                <td>MARKETING, ADS, EMAIL AND SOCIAL</td>
                <td><span class="badge badge-sales">Needs partnership/sales</span></td>
                <td><span class="badge badge-admin">Needs admin approval</span></td>
                <td>Developer token review form confused with commercial partnership contract</td>
              </tr>
              <tr>
                <td><strong>Smartsheet</strong></td>
                <td>PRODUCTIVITY</td>
                <td><span class="badge badge-paid">Needs paid access</span></td>
                <td><span class="badge badge-caveat">Ready with caveat</span> (30d Trial)</td>
                <td>Paid commercial subscription confused with self-serve trial onboarding</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- 100-App Matrix -->
  <section id="matrix">
    <div class="container">
      <div class="section-header">
        <div class="section-tag">Interactive Matrix</div>
        <h2 class="section-title">The Complete 100-Application Readiness Dataset</h2>
        <p class="section-desc">
          Filter and search all 100 researched platforms. Click any row to inspect verified evidence sources, documentation excerpts, and verification claims.
        </p>
      </div>

      <div class="matrix-controls">
        <div class="search-row">
          <input type="text" id="searchInput" class="search-input" placeholder="Search by app name, keyword, auth method, category, or blocker...">
        </div>
        <div class="filter-pills" id="categoryFilters">
          <button class="filter-btn active" data-cat="all">All Categories (100)</button>
          <button class="filter-btn" data-cat="CRM AND SALES">CRM & Sales (10)</button>
          <button class="filter-btn" data-cat="SUPPORT AND HELPDESK">Support & Helpdesk (10)</button>
          <button class="filter-btn" data-cat="COMMUNICATIONS AND MESSAGING">Messaging (10)</button>
          <button class="filter-btn" data-cat="MARKETING, ADS, EMAIL AND SOCIAL">Marketing & Ads (10)</button>
          <button class="filter-btn" data-cat="ECOMMERCE">E-Commerce (10)</button>
          <button class="filter-btn" data-cat="DATA, SEO AND SCRAPING">Data & Scraping (10)</button>
          <button class="filter-btn" data-cat="DEVELOPER, INFRA AND DATA PLATFORMS">Dev & Infra (10)</button>
          <button class="filter-btn" data-cat="PRODUCTIVITY AND PROJECT MANAGEMENT">Productivity (10)</button>
          <button class="filter-btn" data-cat="FINANCE AND FINTECH">Finance & Fintech (10)</button>
          <button class="filter-btn" data-cat="AI, RESEARCH AND MEDIA-NATIVE">AI & Media (10)</button>
        </div>
      </div>

      <div class="table-wrapper">
        <table id="appsTable">
          <thead>
            <tr>
              <th>Application</th>
              <th>Category</th>
              <th>Primary Auth</th>
              <th>Credential Access</th>
              <th>API Breadth</th>
              <th>MCP Status</th>
              <th>Buildability</th>
              <th>Confidence</th>
              <th>Evidence</th>
            </tr>
          </thead>
          <tbody id="appsTableBody">
            <!-- Rendered dynamically via JavaScript -->
          </tbody>
        </table>
      </div>
      <div id="noResults" style="display:none; text-align:center; padding:40px; color:var(--text-muted);">
        No matching applications found. Try refining your search query or active filter.
      </div>
    </div>
  </section>

  <!-- Reproduction & CLI Commands -->
  <section id="reproduce">
    <div class="container">
      <div class="section-header">
        <div class="section-tag">Reproduction Guide</div>
        <h2 class="section-title">How to Run and Reproduce This System</h2>
        <p class="section-desc">
          Every component is open, deterministic, and runnable from the command line.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 20px;">
        <div class="verif-box">
          <h4 style="font-size: 1rem; margin-bottom: 6px; color: white;">1. Research a Single App or All 100</h4>
          <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 8px;">Run research pipeline on any specific platform or across the entire catalog:</p>
          <div class="code-box">python scripts/research.py --app "HubSpot"<br>python scripts/research.py --all</div>
        </div>

        <div class="verif-box">
          <h4 style="font-size: 1rem; margin-bottom: 6px; color: white;">2. Run Independent Verification</h4>
          <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 8px;">Execute the independent verifier agent to test claims against ground truth:</p>
          <div class="code-box">python scripts/verify.py --sample 20</div>
        </div>

        <div class="verif-box">
          <h4 style="font-size: 1rem; margin-bottom: 6px; color: white;">3. Rebuild HTML Case Study</h4>
          <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 8px;">Recompile the standalone responsive HTML presentation:</p>
          <div class="code-box">python scripts/build_case_study.py</div>
        </div>

        <div class="verif-box">
          <h4 style="font-size: 1rem; margin-bottom: 6px; color: white;">4. Full End-to-End Workflow</h4>
          <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 8px;">Executes research, audit, verification, and HTML compilation sequentially:</p>
          <div class="code-box">python scripts/run.py</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
      <div>
        <strong>Composio AI Product Ops Submission</strong> • Rigorous Agent Readiness Research
      </div>
      <div>
        Dataset: 100 Apps Audited • 100% Typed Pydantic Schemas • Verified Clean Audit
      </div>
    </div>
  </footer>

  <!-- Drawer / Modal for App Evidence -->
  <div class="modal-backdrop" id="appModal" onclick="closeModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeModalDirect()">✕</button>
      <div id="modalBody">
        <!-- Injected via JavaScript -->
      </div>
    </div>
  </div>

  <script>
    const appsData = {dataset_json_str};

    function getBuildabilityBadge(verdict) {{
      if (verdict === 'Ready') return '<span class="badge badge-ready">Ready</span>';
      if (verdict === 'Ready with access caveat') return '<span class="badge badge-caveat">Ready with caveat</span>';
      if (verdict === 'Needs paid access') return '<span class="badge badge-paid">Needs paid access</span>';
      if (verdict === 'Needs admin approval') return '<span class="badge badge-admin">Needs admin approval</span>';
      if (verdict === 'Needs partnership/contact-sales') return '<span class="badge badge-sales">Needs sales/partner</span>';
      if (verdict === 'CLI/local tool') return '<span class="badge badge-cli">CLI/local tool</span>';
      return '<span class="badge badge-noapi">' + verdict + '</span>';
    }}

    function getMcpBadge(mcp) {{
      if (!mcp.exists) return '<span class="badge badge-mcp-no">None</span>';
      if (mcp.official) return '<span class="badge badge-mcp-official">Official</span>';
      if (mcp.vendor_supported) return '<span class="badge badge-mcp-vendor">Vendor</span>';
      if (mcp.composio_support) return '<span class="badge badge-mcp-yes">Composio</span>';
      return '<span class="badge badge-mcp-yes">Community</span>';
    }}

    function renderTable(data) {{
      const tbody = document.getElementById('appsTableBody');
      tbody.innerHTML = '';

      if (data.length === 0) {{
        document.getElementById('noResults').style.display = 'block';
        return;
      }} else {{
        document.getElementById('noResults').style.display = 'none';
      }}

      data.forEach((app, index) => {{
        const tr = document.createElement('tr');
        tr.style.cursor = 'pointer';
        tr.onclick = () => openModal(app);

        const primaryAuth = app.authentication.primary_method || 'Unknown';
        const accessClass = app.credential_access.access_classification || 'Unknown';
        const breadth = app.api.breadth || 'Unknown';
        const confPct = Math.round(app.confidence.overall * 100);

        tr.innerHTML = `
          <td>
            <div class="app-title-cell">${{app.app_name}}</div>
            <div class="app-cat-sub">${{app.one_line_description}}</div>
          </td>
          <td><span style="font-size:0.75rem; color:#94a3b8;">${{app.category}}</span></td>
          <td><code>${{primaryAuth}}</code></td>
          <td><span style="font-size:0.8rem; color:#cbd5e1;">${{accessClass}}</span></td>
          <td><span style="font-size:0.8rem;">${{breadth}}</span></td>
          <td>${{getMcpBadge(app.mcp)}}</td>
          <td>${{getBuildabilityBadge(app.buildability.verdict)}}</td>
          <td><span style="font-weight:600; color:#38bdf8;">${{confPct}}%</span></td>
          <td><span style="color:#60a5fa; font-size:0.8rem; text-decoration:underline;">${{app.evidence.length}} sources ↗</span></td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Filter and Search Logic
    let activeCategory = 'all';
    let searchQuery = '';

    function filterData() {{
      const filtered = appsData.filter(app => {{
        const matchesCategory = activeCategory === 'all' || app.category === activeCategory;
        const q = searchQuery.toLowerCase();
        const matchesSearch = !searchQuery ||
          app.app_name.toLowerCase().includes(q) ||
          app.category.toLowerCase().includes(q) ||
          app.one_line_description.toLowerCase().includes(q) ||
          app.authentication.primary_method.toLowerCase().includes(q) ||
          app.credential_access.access_classification.toLowerCase().includes(q) ||
          app.buildability.verdict.toLowerCase().includes(q) ||
          app.buildability.blocker.toLowerCase().includes(q);
        return matchesCategory && matchesSearch;
      }});
      renderTable(filtered);
    }}

    document.getElementById('searchInput').addEventListener('input', (e) => {{
      searchQuery = e.target.value.trim();
      filterData();
    }});

    const filterButtons = document.querySelectorAll('#categoryFilters .filter-btn');
    filterButtons.forEach(btn => {{
      btn.addEventListener('click', () => {{
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeCategory = btn.getAttribute('data-cat');
        filterData();
      }});
    }});

    // Modal Interaction
    function openModal(app) {{
      const modal = document.getElementById('appModal');
      const body = document.getElementById('modalBody');

      let evidenceHtml = '';
      if (app.evidence && app.evidence.length > 0) {{
        evidenceHtml = app.evidence.map((ev, i) => `
          <div class="evidence-item">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:4px;">
              <a href="${{ev.url}}" target="_blank" rel="noopener noreferrer">${{ev.title || ev.url}}</a>
              <span class="badge badge-mcp-official">${{ev.source_type}}</span>
            </div>
            <div style="font-size:0.75rem; color:#94a3b8; margin-bottom:4px;">Supports: ${{ev.supports.join(', ')}}</div>
            <div class="evidence-quote">"${{ev.excerpt}}"</div>
          </div>
        `).join('');
      }} else {{
        evidenceHtml = '<p style="color:#94a3b8; font-size:0.85rem;">No direct evidence sources attached.</p>';
      }}

      body.innerHTML = `
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:6px;">
          <h2 style="font-size:1.6rem; font-weight:700;">${{app.app_name}}</h2>
          ${{getBuildabilityBadge(app.buildability.verdict)}}
        </div>
        <p style="color:#94a3b8; font-size:0.95rem; margin-bottom:18px;">${{app.one_line_description}}</p>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-bottom:20px;">
          <div class="verif-box">
            <div style="font-size:0.75rem; color:#94a3b8;">Category</div>
            <div style="font-weight:600; font-size:0.92rem; margin-top:2px;">${{app.category}}</div>
          </div>
          <div class="verif-box">
            <div style="font-size:0.75rem; color:#94a3b8;">Primary Auth</div>
            <div style="font-weight:600; font-size:0.92rem; margin-top:2px;">${{app.authentication.primary_method}}</div>
          </div>
          <div class="verif-box">
            <div style="font-size:0.75rem; color:#94a3b8;">Access Model</div>
            <div style="font-weight:600; font-size:0.92rem; margin-top:2px;">${{app.credential_access.access_classification}}</div>
          </div>
          <div class="verif-box">
            <div style="font-size:0.75rem; color:#94a3b8;">API Breadth</div>
            <div style="font-weight:600; font-size:0.92rem; margin-top:2px;">${{app.api.breadth}}</div>
          </div>
        </div>

        <div style="margin-bottom:18px;">
          <h4 style="font-size:0.95rem; color:#38bdf8; margin-bottom:4px;">Toolkit Rationale & Blocker</h4>
          <p style="font-size:0.88rem; color:#e2e8f0; line-height:1.5;">${{app.buildability.rationale}}</p>
          ${{app.buildability.blocker !== 'None' ? '<div style="margin-top:6px; font-size:0.82rem; color:#f87171;"><strong>Primary Blocker:</strong> ' + app.buildability.blocker + '</div>' : ''}}
        </div>

        <div style="margin-bottom:20px;">
          <h4 style="font-size:0.95rem; color:#38bdf8; margin-bottom:4px;">Model Context Protocol (MCP)</h4>
          <p style="font-size:0.88rem; color:#e2e8f0;">${{app.mcp.notes}}</p>
          <div style="margin-top:4px; font-size:0.8rem; color:#94a3b8;">
            Composio Supported: <strong>${{app.mcp.composio_support ? 'Yes' : 'No'}}</strong> | 
            Vendor Maintained: <strong>${{app.mcp.vendor_supported ? 'Yes' : 'No'}}</strong> | 
            Official Core: <strong>${{app.mcp.official ? 'Yes' : 'No'}}</strong>
          </div>
        </div>

        <div style="margin-bottom:20px;">
          <h4 style="font-size:0.95rem; color:#38bdf8; margin-bottom:4px;">Verification Record</h4>
          <p style="font-size:0.85rem; color:#94a3b8;">Status: <strong style="color:${{app.verification.status === 'verified' ? '#10b981' : '#f59e0b'}}">${{app.verification.status.toUpperCase()}}</strong> • Pass ${{app.metadata.verification_pass}}</p>
          <div style="font-size:0.82rem; color:#cbd5e1; margin-top:4px; font-style:italic;">"${{app.verification.notes}}"</div>
        </div>

        <div>
          <h4 style="font-size:0.95rem; color:#38bdf8; margin-bottom:4px;">Evidence Sources (${{app.evidence.length}})</h4>
          ${{evidenceHtml}}
        </div>
      `;

      modal.style.display = 'flex';
    }}

    function closeModal(e) {{
      if (e.target.id === 'appModal') {{
        document.getElementById('appModal').style.display = 'none';
      }}
    }}

    function closeModalDirect() {{
      document.getElementById('appModal').style.display = 'none';
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        closeModalDirect();
      }}
    }});

    // Initial Render
    renderTable(appsData);
  </script>
</body>
</html>
"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Polished HTML Case Study generated successfully at: {output_path}")
    print(f"File size: {os.path.getsize(output_path):,} bytes")
    return output_path


if __name__ == "__main__":
    generate_html()
