"""
Knowledge base definitions for AI, RESEARCH AND MEDIA-NATIVE category (10 apps).
"""

AI_MEDIA_APPS = {
    "notebooklm": {
        "website": "https://notebooklm.google.com",
        "one_line_description": "Personalized AI research assistant and source-grounded notebook powered by Google Gemini.",
        "authentication": {
            "methods": ["Unknown"],
            "primary_method": "Unknown",
            "oauth2": False,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "No public developer API available; consumer web application only"
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": False,
            "access_classification": "No developer access found",
            "notes": "Google NotebookLM currently exists as a standalone web interface without an official public developer API or programmatic SDK."
        },
        "api": {
            "exists": False,
            "public": False,
            "type": [],
            "rest": False,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": False,
            "documentation_available": False,
            "breadth": "Unknown",
            "major_resource_areas": []
        },
        "mcp": {
            "exists": False,
            "official": False,
            "vendor_supported": False,
            "community": False,
            "composio_support": False,
            "url": None,
            "notes": "No official or vendor MCP server exists; not in Composio catalog."
        },
        "evidence": [
            {
                "url": "https://notebooklm.google.com",
                "title": "Google NotebookLM Home",
                "source_type": "official_docs",
                "supports": ["No developer access found"],
                "excerpt": "NotebookLM is an experimental web application developed by Google Labs. It offers no public API endpoints for third-party developer integrations."
            }
        ]
    },
    "otter-ai": {
        "website": "https://otter.ai",
        "one_line_description": "AI transcription and meeting summary tool for virtual meetings and live audio recording.",
        "authentication": {
            "methods": ["Unknown"],
            "primary_method": "Unknown",
            "oauth2": False,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "No self-serve developer API; enterprise partnership inquiry only"
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": True,
            "admin_approval_required": True,
            "contact_sales_required": True,
            "partnership_required": True,
            "developer_account_required": True,
            "access_classification": "Partner-gated",
            "notes": "Otter.ai does not offer a public self-serve developer API; integration requests require direct enterprise partnership contracts."
        },
        "api": {
            "exists": False,
            "public": False,
            "type": [],
            "rest": False,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": False,
            "documentation_available": False,
            "breadth": "Narrow",
            "major_resource_areas": []
        },
        "mcp": {
            "exists": False,
            "official": False,
            "vendor_supported": False,
            "community": False,
            "composio_support": False,
            "url": None,
            "notes": "No official MCP server found; not supported by Composio."
        },
        "evidence": [
            {
                "url": "https://otter.ai",
                "title": "Otter.ai Platform",
                "source_type": "official_pricing",
                "supports": ["Partner-gated", "No developer access found"],
                "excerpt": "Otter.ai provides automated meeting summaries and live transcription. No public developer API documentation or self-serve developer credentials exist."
            }
        ]
    },
    "fathom": {
        "website": "https://fathom.video",
        "one_line_description": "AI meeting assistant that records, transcribes, highlights, and summarizes video conference calls.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Authorization: Bearer <API_KEY>"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Fathom provides self-serve API access for users to retrieve meeting transcripts and summaries in dashboard settings."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Moderate",
            "major_resource_areas": ["Meetings", "Transcripts", "Summaries", "Action Items", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": False,
            "url": "https://docs.fathom.video",
            "notes": "Community MCP server available on GitHub; not in Composio catalog."
        },
        "evidence": [
            {
                "url": "https://docs.fathom.video/",
                "title": "Fathom API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Self-serve free"],
                "excerpt": "The Fathom API lets you programmatically access meeting transcripts, highlights, and action items using Bearer API keys."
            }
        ]
    },
    "consensus": {
        "website": "https://consensus.app",
        "one_line_description": "AI-powered academic search engine finding claims and insights in scientific research papers.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Authorization: Bearer <API_KEY>"
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": True,
            "admin_approval_required": False,
            "contact_sales_required": True,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Contact-sales gated",
            "notes": "Consensus Academic Search API is provided for institutional and enterprise AI builders via commercial inquiry and paid credits."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": False,
            "documentation_available": True,
            "breadth": "Moderate",
            "major_resource_areas": ["Search", "Claims", "Papers", "Yearly Filters", "Study Types"]
        },
        "mcp": {
            "exists": False,
            "official": False,
            "vendor_supported": False,
            "community": False,
            "composio_support": False,
            "url": None,
            "notes": "No MCP server found; not supported by Composio."
        },
        "evidence": [
            {
                "url": "https://consensus.app/home/blog/api/",
                "title": "Consensus Search API Announcement",
                "source_type": "official_pricing",
                "supports": ["REST API", "Contact-sales gated", "Paid plan required"],
                "excerpt": "Consensus provides access to over 200 million research papers via REST API for enterprise AI agents, available through customized commercial access tiers."
            }
        ]
    },
    "reducto": {
        "website": "https://reducto.ai",
        "one_line_description": "Developer platform converting complex PDFs, financial reports, and scanned tables into structured LLM-ready data.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Authorization: Bearer <API_KEY>"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Free tier provides instant API key generation upon self-serve registration with free parsing credits."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Moderate",
            "major_resource_areas": ["Parse", "Extract", "Chunk", "Job Status", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": False,
            "url": "https://docs.reducto.ai",
            "notes": "Community MCP server available on GitHub; not in Composio catalog."
        },
        "evidence": [
            {
                "url": "https://docs.reducto.ai/api-reference/introduction",
                "title": "Reducto API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Self-serve free"],
                "excerpt": "Reducto API extracts structured content from documents. All requests require Bearer token authentication with your Reducto API key."
            }
        ]
    },
    "devin": {
        "website": "https://devin.ai",
        "one_line_description": "Autonomous AI software engineering agent developed by Cognition for building and debugging code.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Authorization: Bearer <API_KEY>"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": True,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve paid",
            "notes": "Cognition Devin API provides programmatic session control for paid plan subscribers."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Moderate",
            "major_resource_areas": ["Sessions", "Messages", "Snapshots", "Artifacts", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": False,
            "url": "https://docs.devin.ai",
            "notes": "Community MCP server available on GitHub; not in Composio catalog."
        },
        "evidence": [
            {
                "url": "https://docs.devin.ai/api-reference",
                "title": "Devin API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Paid plan required"],
                "excerpt": "The Devin API allows developers to spawn and interact with Devin sessions programmatically using Bearer API keys."
            }
        ]
    },
    "higgsfield": {
        "website": "https://higgsfield.ai",
        "one_line_description": "Generative AI video creation and cinematic camera motion platform for content creators and animators.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Authorization: Bearer <API_KEY>"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": False,
            "trial_available": True,
            "paid_plan_required": True,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve paid",
            "notes": "Video generation API requires purchasing compute credits or an active developer subscription."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Moderate",
            "major_resource_areas": ["Video Generation", "Camera Motion", "Tasks", "Assets"]
        },
        "mcp": {
            "exists": False,
            "official": False,
            "vendor_supported": False,
            "community": False,
            "composio_support": False,
            "url": None,
            "notes": "No MCP server found; not supported by Composio."
        },
        "evidence": [
            {
                "url": "https://higgsfield.ai",
                "title": "Higgsfield AI Platform",
                "source_type": "official_pricing",
                "supports": ["REST API", "Paid plan required"],
                "excerpt": "Higgsfield AI offers camera control and AI video models via web interface and commercial developer API endpoints."
            }
        ]
    },
    "mermaid-cli": {
        "website": "https://github.com/mermaid-js/mermaid-cli",
        "one_line_description": "Command-line interface for Mermaid.js that compiles text-based markdown diagram syntax into SVG, PNG, and PDF formats.",
        "authentication": {
            "methods": ["Unknown"],
            "primary_method": "Unknown",
            "oauth2": False,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "No authentication required; local Node.js CLI tool"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": False,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": False,
            "access_classification": "Self-serve free",
            "notes": "Open-source Node.js package (@mermaid-js/mermaid-cli) with MIT license; installed via npm."
        },
        "api": {
            "exists": False,
            "public": False,
            "type": ["CLI"],
            "rest": False,
            "graphql": False,
            "sdk": False,
            "cli": True,
            "webhooks": False,
            "documentation_available": True,
            "breadth": "Narrow",
            "major_resource_areas": ["CLI Diagram Rendering (mmdc)", "Configuration File Parsing", "Puppeteer PDF/PNG Export"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": False,
            "url": "https://github.com/mermaid-js/mermaid-cli",
            "notes": "Community MCP wrapper servers exist on GitHub; mermaid-cli itself is an npm CLI binary."
        },
        "evidence": [
            {
                "url": "https://github.com/mermaid-js/mermaid-cli",
                "title": "Mermaid CLI GitHub Repository",
                "source_type": "official_repo",
                "supports": ["CLI", "Self-serve free", "No developer access found"],
                "excerpt": "mermaid-cli is a command-line tool that takes a mermaid definition file and outputs an SVG, PNG, or PDF file. It runs locally via Node/npm without a hosted web API."
            }
        ]
    },
    "youtube-transcript": {
        "website": "https://developers.google.com/youtube/v3/docs/captions",
        "one_line_description": "Programmatic video subtitle and closed caption extraction via official YouTube Data API v3 and scraping libraries.",
        "authentication": {
            "methods": ["OAuth2", "API Key"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Official YouTube Data API v3 requires OAuth 2.0 or API key; python youtube-transcript-api library accesses public timed text"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Google Cloud Console provides free self-serve API keys for YouTube Data API v3 (10,000 daily quota units free); downloading third-party transcripts officially requires video owner OAuth authorization."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": False,
            "documentation_available": True,
            "breadth": "Narrow",
            "major_resource_areas": ["Captions (List/Download)", "Videos", "Timed Text Formats"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/youtube",
            "notes": "Composio provides YouTube action tools (including transcripts); community MCP servers available."
        },
        "evidence": [
            {
                "url": "https://developers.google.com/youtube/v3/docs/captions",
                "title": "YouTube Data API v3 Captions Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "API Key"],
                "excerpt": "A caption resource represents a YouTube caption track. The API supports downloading caption tracks via HTTP requests authorized with OAuth 2.0."
            }
        ]
    },
    "grain": {
        "website": "https://grain.com",
        "one_line_description": "AI meeting recorder that captures, transcribes, and summarizes business conversations with CRM sync.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Authorization: Bearer <API_KEY>"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": False,
            "trial_available": True,
            "paid_plan_required": True,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve paid",
            "notes": "API access requires an active Grain Business or Enterprise paid plan; 14-day trial offered."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Moderate",
            "major_resource_areas": ["Recordings", "Highlights", "Transcripts", "Users", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": False,
            "url": "https://docs.grain.com",
            "notes": "Community MCP server available on GitHub; not in Composio catalog."
        },
        "evidence": [
            {
                "url": "https://docs.grain.com/",
                "title": "Grain Developer API",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Paid plan required"],
                "excerpt": "The Grain Public API provides programmatic access to your organization's recorded calls, transcripts, and highlights using Bearer tokens on paid plans."
            }
        ]
    }
}
