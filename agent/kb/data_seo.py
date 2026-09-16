"""
Knowledge base definitions for DATA, SEO AND SCRAPING category (10 apps).
"""

DATA_SEO_APPS = {
    "dataforseo": {
        "website": "https://docs.dataforseo.com",
        "one_line_description": "Comprehensive SEO and search engine result data API provider with pay-as-you-go pricing.",
        "authentication": {
            "methods": ["Basic Auth"],
            "primary_method": "Basic Auth",
            "oauth2": False,
            "api_key": False,
            "basic_auth": True,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "HTTP Basic Auth using login and password credentials"
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
            "notes": "Self-serve signup includes $1 in free test API balance without requiring a credit card."
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
            "breadth": "Very broad",
            "major_resource_areas": ["SERP API", "Keywords Data", "Backlinks", "On-Page", "Merchant", "Business Data", "Domain Analytics"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": False,
            "url": "https://docs.dataforseo.com",
            "notes": "Community MCP servers exist on GitHub; not currently in Composio tool catalog."
        },
        "evidence": [
            {
                "url": "https://docs.dataforseo.com/v3/",
                "title": "DataForSEO API v3 Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Basic Auth", "Self-serve free"],
                "excerpt": "DataForSEO v3 API allows access to SERP, keyword, and backlink data. All requests must be authenticated using HTTP Basic auth with your API login credentials."
            }
        ]
    },
    "se-ranking": {
        "website": "https://seranking.com/api",
        "one_line_description": "All-in-one SEO and digital marketing platform offering rank tracking, auditing, and competitor analysis.",
        "authentication": {
            "methods": ["API Key"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Authorization: Token <API_KEY>"
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
            "notes": "API access is reserved for active Pro or Business paid plan subscribers; 14-day standard UI trial offered."
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
            "major_resource_areas": ["Rank Tracking", "Keyword Research", "Site Audit", "Competitor Research", "Backlinks"]
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
                "url": "https://seranking.com/api.html",
                "title": "SE Ranking API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Paid plan required"],
                "excerpt": "SE Ranking API enables automated extraction of ranking and audit data. The API is available on Pro and Business pricing plans via API token authentication."
            }
        ]
    },
    "ahrefs": {
        "website": "https://ahrefs.com/api",
        "one_line_description": "Industry-standard SEO toolset and web crawler database for backlink analysis and keyword research.",
        "authentication": {
            "methods": ["API Key", "Bearer Token"],
            "primary_method": "API Key",
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
            "notes": "API v3 requires an Enterprise plan subscription or paid API units add-on; no free trial API tier."
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
            "breadth": "Broad",
            "major_resource_areas": ["Site Explorer", "Backlinks", "Organic Keywords", "Domain Rating", "Pages", "Refdomains"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": False,
            "url": "https://docs.ahrefs.com/docs/api",
            "notes": "Community MCP server available on GitHub; not in Composio catalog."
        },
        "evidence": [
            {
                "url": "https://docs.ahrefs.com/docs/api/reference",
                "title": "Ahrefs API v3 Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Paid plan required"],
                "excerpt": "Ahrefs API v3 is a REST API providing access to backlink indices and SEO metrics. Authentication is performed via API keys sent in Bearer headers, consuming purchased API units."
            }
        ]
    },
    "mrscraper": {
        "website": "https://docs.mrscraper.com",
        "one_line_description": "Visual and programmatic web scraping tool for extracting structured web data at scale.",
        "authentication": {
            "methods": ["API Key", "Bearer Token"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": None
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
            "notes": "Free tier includes free monthly scraping credits and instant API key generation in user dashboard."
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
            "major_resource_areas": ["Scrapes", "Jobs", "Templates", "Webhooks", "Exports"]
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
                "url": "https://docs.mrscraper.com/",
                "title": "MrScraper Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Self-serve free"],
                "excerpt": "MrScraper API lets developers trigger scraping jobs and retrieve parsed structured data using API keys generated in user account settings."
            }
        ]
    },
    "apify": {
        "website": "https://docs.apify.com",
        "one_line_description": "Cloud platform for web scraping, data extraction, and serverless automation Actors.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Token passed in Authorization header or token query parameter"
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
            "notes": "Free plan includes $5 monthly platform credits and instant API token access."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "CLI", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Actors", "Actor Runs", "Datasets", "Key-Value Stores", "Request Queues", "Schedules", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/apify",
            "notes": "Composio provides Apify Actor toolkit; community MCP server implementations exist."
        },
        "evidence": [
            {
                "url": "https://docs.apify.com/api/v2",
                "title": "Apify API v2 Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Self-serve free"],
                "excerpt": "The Apify API v2 allows programmatic control of the Apify platform. Authentication uses personal API tokens generated in Apify Console."
            }
        ]
    },
    "firecrawl": {
        "website": "https://firecrawl.dev",
        "one_line_description": "API service that crawls websites and converts them into clean, LLM-ready markdown or structured data.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Authorization: Bearer <fc-...>"
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
            "notes": "Free plan includes 500 scrape credits with instant self-serve API key creation upon signup."
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
            "major_resource_areas": ["Scrape", "Crawl", "Map", "Extract", "Batch Scrape", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/mendableai/firecrawl-mcp-server",
            "notes": "Vendor-supported MCP server created and maintained by the Firecrawl team; Composio provides Firecrawl toolkit."
        },
        "evidence": [
            {
                "url": "https://docs.firecrawl.dev/api-reference/introduction",
                "title": "Firecrawl API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Self-serve free"],
                "excerpt": "Firecrawl API provides endpoints to turn any website into clean markdown. Authenticate with your Firecrawl API key sent as a Bearer token."
            }
        ]
    },
    "bright-data": {
        "website": "https://brightdata.com",
        "one_line_description": "Enterprise web data platform offering residential proxy networks, web unlockers, and scraping browser APIs.",
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
            "access_classification": "Self-serve trial",
            "notes": "Self-serve signup includes free trial credits; usage billed per gigabyte or request thereafter."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Web Unlocker", "Scraping Browser", "SERP API", "Datasets", "Proxies", "Zones"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/bright-data/brightdata-mcp",
            "notes": "Vendor-supported MCP server created by Bright Data team; Composio supports Bright Data actions."
        },
        "evidence": [
            {
                "url": "https://docs.brightdata.com/api-reference/introduction",
                "title": "Bright Data API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Self-serve trial"],
                "excerpt": "Bright Data REST API allows managing proxies, datasets, and scraping requests using Bearer token authentication."
            }
        ]
    },
    "sherlock": {
        "website": "https://github.com/sherlock-project/sherlock",
        "one_line_description": "Open-source command-line OSINT tool to hunt down social media accounts by username across 300+ platforms.",
        "authentication": {
            "methods": ["Unknown"],
            "primary_method": "Unknown",
            "oauth2": False,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "No authentication required; local CLI execution tool"
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
            "notes": "Open-source Python CLI tool with MIT license; no developer registration or API keys needed."
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
            "major_resource_areas": ["Username Search across Sites", "Output Formatting (CSV/JSON)"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": False,
            "url": "https://github.com/sherlock-project/sherlock",
            "notes": "Community MCP wrapper servers exist on GitHub; Sherlock itself is an open-source CLI script."
        },
        "evidence": [
            {
                "url": "https://github.com/sherlock-project/sherlock",
                "title": "Sherlock GitHub Repository",
                "source_type": "official_repo",
                "supports": ["CLI", "Self-serve free", "No developer access found"],
                "excerpt": "Sherlock is a command-line tool written in Python to find usernames across social networks. It is executed locally via terminal commands, not as a hosted cloud API."
            }
        ]
    },
    "waterfall-io": {
        "website": "https://waterfall.io",
        "one_line_description": "B2B contact enrichment and data waterfall platform aggregating multi-vendor data sources.",
        "authentication": {
            "methods": ["API Key", "Bearer Token"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": None
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
            "notes": "Targeted at enterprise sales and RevOps teams; data enrichment API access requires sales consultation and commercial agreement."
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
            "major_resource_areas": ["Enrichment", "People", "Companies", "Waterfall Providers"]
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
                "url": "https://waterfall.io",
                "title": "Waterfall.io B2B Enrichment",
                "source_type": "official_pricing",
                "supports": ["Contact-sales gated", "Paid plan required"],
                "excerpt": "Waterfall.io provides unified access to B2B data vendors through sequential waterfalls. Enterprise plans are customized via sales consultation."
            }
        ]
    },
    "clay": {
        "website": "https://clay.com",
        "one_line_description": "Data enrichment and outbound growth platform combining 50+ data providers and automated AI research.",
        "authentication": {
            "methods": ["API Key"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "Clay API Key in headers or webhook secret"
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
            "notes": "Free tier includes 100 enrichment credits and self-serve webhook/API integration."
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
            "major_resource_areas": ["Tables", "Rows", "Enrichments", "Webhooks", "Integrations"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/clay",
            "notes": "Composio supports Clay actions; community MCP connectors exist on GitHub."
        },
        "evidence": [
            {
                "url": "https://clay.com/docs",
                "title": "Clay Documentation and Integrations",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Webhooks"],
                "excerpt": "Clay provides webhooks and REST endpoints for writing data into Clay tables and triggering waterfall enrichments."
            }
        ]
    }
}
