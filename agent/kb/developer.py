"""
Knowledge base definitions for DEVELOPER, INFRA AND DATA PLATFORMS category (10 apps).
"""

DEVELOPER_APPS = {
    "github": {
        "website": "https://docs.github.com/rest",
        "one_line_description": "World-leading cloud-based Git repository hosting, code review, and developer DevOps platform.",
        "authentication": {
            "methods": ["Personal Access Token", "OAuth2", "Bearer Token"],
            "primary_method": "Personal Access Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "GitHub App Private Key (JWT) or Fine-grained Personal Access Tokens"
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
            "notes": "Free GitHub accounts provide instant self-serve generation of fine-grained PATs, classic PATs, and GitHub Apps."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "GraphQL", "SDK", "CLI", "Webhooks"],
            "rest": True,
            "graphql": True,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Repositories", "Issues", "Pull Requests", "Actions (CI/CD)", "Releases", "Users", "Organizations", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": True,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/github",
            "notes": "Official reference MCP server maintained by Anthropic/MCP core; Composio provides extensive GitHub toolkit."
        },
        "evidence": [
            {
                "url": "https://docs.github.com/en/rest/quickstart",
                "title": "GitHub REST API Quickstart",
                "source_type": "official_docs",
                "supports": ["REST API", "Personal Access Token", "OAuth2"],
                "excerpt": "You can use the GitHub REST API to create and manage repositories, issues, pull requests, and automations using personal access tokens."
            },
            {
                "url": "https://github.com/settings/tokens",
                "title": "GitHub Personal Access Tokens Settings",
                "source_type": "official_dev_portal",
                "supports": ["Self-serve free", "Personal Access Token"],
                "excerpt": "Personal access tokens function like ordinary OAuth access tokens. They can be used to authenticate to the GitHub API over HTTPS."
            }
        ]
    },
    "vercel": {
        "website": "https://vercel.com/docs/rest-api",
        "one_line_description": "Cloud platform for frontend developers, providing automated CI/CD deployments and serverless edge functions.",
        "authentication": {
            "methods": ["Bearer Token", "Personal Access Token", "OAuth2"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "Authorization: Bearer <token>"
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
            "notes": "Vercel Hobby plan is free forever and includes self-serve API token generation in account tokens settings."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "CLI", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Deployments", "Projects", "Domains", "DNS", "Environment Variables", "Certificates", "Teams"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/vercel",
            "notes": "Composio provides Vercel toolkit; community MCP servers exist on GitHub."
        },
        "evidence": [
            {
                "url": "https://vercel.com/docs/rest-api",
                "title": "Vercel REST API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Personal Access Token"],
                "excerpt": "The Vercel REST API allows developers to automate deployments, configure projects, and manage domains using Bearer token authentication."
            }
        ]
    },
    "netlify": {
        "website": "https://docs.netlify.com/api",
        "one_line_description": "Web hosting and cloud computing platform for modern web applications and Jamstack architecture.",
        "authentication": {
            "methods": ["Bearer Token", "Personal Access Token", "OAuth2"],
            "primary_method": "Personal Access Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "Authorization: Bearer <PAT>"
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
            "notes": "Free Starter tier allows instant generation of Personal Access Tokens in User Settings > Applications."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "CLI", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Sites", "Deploys", "Forms", "Functions", "Environment Variables", "DNS Zones", "Hooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/netlify",
            "notes": "Composio supports Netlify; community MCP servers available."
        },
        "evidence": [
            {
                "url": "https://docs.netlify.com/api/get-started/",
                "title": "Netlify API Getting Started",
                "source_type": "official_docs",
                "supports": ["REST API", "Personal Access Token", "Bearer Token"],
                "excerpt": "Netlify provides a REST API that lets you manage sites and builds. All requests require authentication using an OAuth token or Personal Access Token."
            }
        ]
    },
    "cloudflare": {
        "website": "https://developers.cloudflare.com/api",
        "one_line_description": "Global cloud network platform providing content delivery, DNS, DDoS protection, and edge compute (Workers).",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Scoped API Tokens (Bearer) or Global API Key + X-Auth-Email headers"
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
            "notes": "Free account enables creating fine-grained scoped API tokens in dashboard under My Profile > API Tokens."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "CLI"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["DNS Records", "Zones", "Workers & Pages", "KV / D1 / R2 Storage", "Firewall Rules", "SSL/TLS", "Analytics"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/cloudflare/mcp-server-cloudflare",
            "notes": "Official vendor-supported MCP server released by Cloudflare team; Composio provides Cloudflare toolkit."
        },
        "evidence": [
            {
                "url": "https://developers.cloudflare.com/fundamentals/api/get-started/",
                "title": "Cloudflare API Fundamentals",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Self-serve free"],
                "excerpt": "The Cloudflare API is a RESTful API. To interact with Cloudflare resources, create a scoped API token in the dashboard and pass it as an HTTP Bearer header."
            }
        ]
    },
    "supabase": {
        "website": "https://supabase.com/docs",
        "one_line_description": "Open-source Firebase alternative offering Postgres database, authentication, instant REST/GraphQL APIs, and realtime subscriptions.",
        "authentication": {
            "methods": ["API Key", "Bearer Token", "Personal Access Token", "JWT"],
            "primary_method": "API Key",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "Anon/Service_role API keys + Management Personal Access Tokens"
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
            "notes": "Generous free tier includes 2 active Postgres projects, instant API keys, and access to Supabase Management API."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "GraphQL", "SDK", "CLI"],
            "rest": True,
            "graphql": True,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Database (PostgreSQL)", "Auth (GoTrue)", "Storage", "Edge Functions", "Realtime", "Management API", "pg_graphql"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/supabase/mcp-server-supabase",
            "notes": "Vendor-supported MCP server created and maintained by the Supabase team; Composio provides Supabase toolkit."
        },
        "evidence": [
            {
                "url": "https://supabase.com/docs/guides/api",
                "title": "Supabase Auto-Generated APIs",
                "source_type": "official_docs",
                "supports": ["REST API", "GraphQL", "API Key"],
                "excerpt": "Supabase automatically generates RESTful APIs via PostgREST and GraphQL endpoints via pg_graphql directly from your PostgreSQL schema."
            },
            {
                "url": "https://supabase.com/docs/reference/api/introduction",
                "title": "Supabase Management API Reference",
                "source_type": "official_docs",
                "supports": ["Personal Access Token", "Self-serve free"],
                "excerpt": "The Management API enables programmatic creation of Supabase projects, databases, and secrets using personal access tokens."
            }
        ]
    },
    "neo4j": {
        "website": "https://neo4j.com/docs/api",
        "one_line_description": "Graph database platform built to store, manage, and query connected relationships and graph structures.",
        "authentication": {
            "methods": ["Basic Auth", "Bearer Token"],
            "primary_method": "Basic Auth",
            "oauth2": True,
            "api_key": False,
            "basic_auth": True,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Cypher Bolt protocol credentials (username/password) or Aura API Client ID/Secret"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": False,
            "access_classification": "Self-serve free",
            "notes": "Neo4j AuraDB Free tier provides an instant free cloud graph database instance; Neo4j Community is open source and self-hostable."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "CLI"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": True,
            "webhooks": False,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Cypher Query Execution", "Transactions", "Aura Management API", "Schema & Indexes", "Graph Data Science"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/neo4j-contrib/mcp-neo4j",
            "notes": "Vendor-supported MCP server created by Neo4j team; Composio provides Neo4j toolkit."
        },
        "evidence": [
            {
                "url": "https://neo4j.com/docs/http-api/current/",
                "title": "Neo4j HTTP API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Basic Auth", "Self-serve free"],
                "excerpt": "The Neo4j HTTP API executes Cypher statements over HTTP transactions, authenticated via HTTP Basic credentials."
            }
        ]
    },
    "snowflake": {
        "website": "https://docs.snowflake.com",
        "one_line_description": "Cloud data warehouse and analytics platform providing scalable SQL compute and data sharing.",
        "authentication": {
            "methods": ["JWT", "OAuth2", "Bearer Token"],
            "primary_method": "JWT",
            "oauth2": True,
            "api_key": False,
            "basic_auth": True,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Key-Pair Authentication (JWT signed by RSA private key)"
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
            "notes": "30-day free trial offers $400 of free cloud credits without upfront credit card; paid consumption billing thereafter."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "CLI"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": True,
            "webhooks": False,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Snowflake SQL REST API", "Warehouses", "Databases & Schemas", "Tables & Views", "Stages", "Streams & Tasks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/Snowflake-Labs/mcp-snowflake",
            "notes": "Vendor-supported MCP server released in Snowflake-Labs; Composio provides Snowflake toolkit."
        },
        "evidence": [
            {
                "url": "https://docs.snowflake.com/en/developer-guide/sql-api/index",
                "title": "Snowflake SQL API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "JWT", "OAuth2"],
                "excerpt": "The Snowflake SQL API is a REST API that you can use to execute SQL statements. You authenticate using JWT key-pair authentication or OAuth."
            }
        ]
    },
    "mongodb-atlas": {
        "website": "https://mongodb.com/docs/atlas/api",
        "one_line_description": "Fully managed multi-cloud document database platform with automated scaling and vector search.",
        "authentication": {
            "methods": ["API Key", "Basic Auth", "Bearer Token"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "HTTP Digest Authentication using Public/Private API Key pair"
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
            "notes": "Atlas M0 free tier cluster is free forever; Administration API keys can be created directly in Atlas organization settings."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "CLI"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Clusters", "Database Users", "Network Access (IP Whitelist)", "Backups", "Projects", "Data API"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/mongodb-labs/mongodb-mcp-server",
            "notes": "Vendor-supported MCP server created by MongoDB Labs; Composio provides MongoDB toolkit."
        },
        "evidence": [
            {
                "url": "https://www.mongodb.com/docs/atlas/reference/api-resources-spec/",
                "title": "MongoDB Atlas Administration API Specification",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Basic Auth"],
                "excerpt": "The Atlas Administration REST API lets you manage Atlas programmatic resources. Authenticate using an organization or project API key pair using HTTP Digest Authentication."
            }
        ]
    },
    "datadog": {
        "website": "https://docs.datadoghq.com/api",
        "one_line_description": "Observability and security monitoring platform for cloud-scale applications, metrics, and logs.",
        "authentication": {
            "methods": ["API Key"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "DD-API-KEY and DD-APPLICATION-KEY headers"
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
            "notes": "14-day full feature free trial allows self-serve generation of API and Application keys; paid subscription required thereafter."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "CLI"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Metrics", "Monitors & Alerts", "Logs", "Dashboards", "Traces/APM", "Incidents", "Downtimes"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/DataDog/datadog-mcp",
            "notes": "Vendor-supported MCP server created by Datadog team; Composio provides Datadog toolkit."
        },
        "evidence": [
            {
                "url": "https://docs.datadoghq.com/api/latest/authentication/",
                "title": "Datadog API Authentication Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key"],
                "excerpt": "All requests to Datadog’s API must be authenticated with an API key (DD-API-KEY) and, for modifying operations, an Application key (DD-APPLICATION-KEY)."
            }
        ]
    },
    "sentry": {
        "website": "https://docs.sentry.io/api",
        "one_line_description": "Application performance monitoring and error tracking platform for software development teams.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2", "Personal Access Token"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "User Auth Token (Bearer) or Internal Integration Token"
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
            "notes": "Developer plan is free for up to 5,000 errors/month and allows self-serve creation of User Auth Tokens."
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
            "breadth": "Broad",
            "major_resource_areas": ["Issues", "Events", "Projects", "Organizations", "Releases", "Alert Rules", "Integrations"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/getsentry/sentry-mcp",
            "notes": "Vendor-supported MCP server created by Sentry team; Composio provides Sentry toolkit."
        },
        "evidence": [
            {
                "url": "https://docs.sentry.io/api/",
                "title": "Sentry Web API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Personal Access Token"],
                "excerpt": "The Sentry API is a RESTful API. Requests are authenticated via an HTTP Bearer token generated from your Sentry account settings."
            }
        ]
    }
}
